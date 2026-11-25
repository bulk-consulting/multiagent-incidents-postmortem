"""The Research RAG agent: finds historical evidence for the Diagnosis agent.

    first round:  START → initial_search → agent ⇄ tools → build_findings → END
    refinement:   START → initial_search → agent ⇄ tools → build_findings → END
                  (the Diagnosis agent's request; the incidents already seen are left out of every search)

    initial_search  code: searches with the description and each symptom; merges by incident (top 10).
                    In a refinement: searches with the request and the description, leaving out the incidents
                    already seen, so the LLM reads only NEW candidates
    agent           LLM (Nemotron 3.5 on NVIDIA NIM, via ChatNVIDIA) with tool_choice="auto": reads the
                    candidates and decides whether to call search_inside_incidents, find_similar_incidents or none
    tools           LangGraph ToolNode: runs the tools the LLM asked for (tools.py)
    build_findings  code: incidents + passages (similar / deep search) + log of every search

After the tools, the flow goes back to the agent only if it called find_similar_incidents (there are new
incidents to look at) and there are LLM calls left (MAX_LLM_CALLS). After search_inside_incidents, the work
of the round is done and the flow goes to build_findings without spending another call.

Three search modes (see enable_agentic_mode and enable_hybrid_mode):
    normal (default)  the code runs the initial search; the LLM reads 10 candidates and picks
    agentic           no initial search: the LLM writes its own queries with find_similar_incidents
    hybrid            agentic + the code also searches with the original description in the first search

The agent does not judge whether the evidence is enough: that is the Diagnosis agent's job. The counter
of the refinement loop belongs to the routing of the main graph.

Run from the repository root, with the database up:
    multiagent_env/bin/python -I agents/research/agent.py "incident description" [--symptom "..."]...
        [--no-llm] [--json out.json] [--model nvidia/nemotron-3.5-super-vl-120b-a12b] [--agentic | --hybrid]
    # refinement: starts from the findings of a previous run and a request from the Diagnosis agent
    multiagent_env/bin/python -I agents/research/agent.py "description" --previous out.json --request "..."
"""
from __future__ import annotations

import argparse
import json
import operator
import sys
import time
from pathlib import Path
from typing import Annotated, Literal, TypedDict

from dotenv import dotenv_values
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage, ToolMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langgraph.types import RetryPolicy

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:  # lets "python agents/research/agent.py" find the packages agents/ and rag/
    sys.path.insert(0, str(ROOT))
from agents.research import prompts, tools  # noqa: E402
from rag import limite_llm  # noqa: E402  (calls per minute and long waits on HTTP 429)

N_DOCS = 10                # candidates of the initial search (the LLM sees the title and summary of each one)
MAX_FINDINGS = 8           # incidents in the output: the deepened ones first, then the most similar
MIN_SUMMARY_CHARS = 100    # a shorter summary goes with the start of the most similar passage
N_SIMILAR_PASSAGES = 2     # passages similar to the description, per incident
MAX_PASSAGES = 7           # passages per incident in the findings (up to 5 from the deep search + 2 similar)
MAX_LLM_CALLS = 2          # per run of the agent
# Agentic mode (see enable_agentic_mode): no initial search in code; the LLM writes its own queries with
# find_similar_incidents from the first call. Turned on by --agentic (or --hybrid).
AGENTIC_MODE = False
MAX_LLM_CALLS_AGENTIC = 4
N_DOCS_FIND_AGENTIC = 10   # incidents that find_similar_incidents returns in agentic mode (like the 10 candidates)
# Experiment (2026-11-24): in agentic/hybrid mode, give the LLM the whole structured Triage output (state["triage"])
# and the guidance on how to use it in its queries (prompts.TRIAGE_GUIDANCE).
TRIAGE_CONTEXT = False


class ResearchState(TypedDict, total=False):
    # input
    description: str
    symptoms: list[str]
    search_request: str                               # from the Diagnosis agent; empty in the first round
    triage: dict                                      # experiment (TRIAGE_CONTEXT): trigger, affected_service, category, symptoms
    candidates: list[dict]                            # incidents found by the initial search
    previous_findings: list[dict]                     # refinement: the findings of the earlier rounds
    seen_ids: list[str]                               # incidents already seen: left out of every search
    no_llm: bool                                      # tests: fixed call, without NIM
    # produced by the agent
    messages: Annotated[list[AnyMessage], add_messages]
    findings: list[dict]                              # the output for the Diagnosis agent
    deepened: dict                                    # incident_id -> passages from search_inside_incidents
    new_incidents: list[dict]                         # incidents from find_similar_incidents
    plan: dict                                        # summary of the LLM's decisions (for reports)
    search_log: Annotated[list[dict], operator.add]   # every search made (traceability)
    llm_calls: Annotated[list[dict], operator.add]
    timings: Annotated[dict, operator.or_]


# ---------------------------------------------------------------- initial search (code)

def _tag_origin(incidents: list[dict], query: str) -> list[dict]:
    for r in incidents:
        for d in r["passages"]:
            d.setdefault("origin", "similar")
            d.setdefault("query", query)
    return incidents


def _merge_by_incident(lists: list[list[dict]]) -> list[dict]:
    """One record per incident, with the highest similarity and the passages of all searches (no repeats)."""
    by_id: dict[str, dict] = {}
    for found in lists:
        for r in found:
            current = by_id.get(r["incident_id"])
            if current is None:
                by_id[r["incident_id"]] = {**r, "passages": list(r["passages"])}
                continue
            texts = {d["content"] for d in current["passages"]}
            current["passages"] += [d for d in r["passages"] if d["content"] not in texts]
            if r["similarity"] > current["similarity"]:
                current.update({k: v for k, v in r.items() if k != "passages"})
    return sorted(by_id.values(), key=lambda r: -r["similarity"])


def initial_search(state: ResearchState) -> dict:
    start = time.time()
    lists, log = [], []
    exclude = sorted(state.get("seen_ids", []))
    if state.get("previous_findings"):  # refinement: the request and the description, without the incidents seen
        queries = [q for q in (state.get("search_request", ""), state["description"]) if q.strip()]
    elif tools.SYMPTOMS_IN_ONE_QUERY:  # experiment: description + symptoms in one search text
        queries = [tools.description_query(state)]
    else:  # the description and one search per symptom
        queries = [state["description"], *state.get("symptoms", [])]
    for query in queries:
        found = _tag_origin(tools.search_incidents(query, N_DOCS, N_SIMILAR_PASSAGES, exclude), query)
        lists.append(found)
        log.append({"step": "initial_search", "query": query, "filter": {"exclude": exclude} if exclude else None,
                    "ids": [r["incident_id"] for r in found]})
    return {"candidates": _merge_by_incident(lists)[:N_DOCS], "search_log": log,
            "timings": {"initial_search": round(time.time() - start, 1)}}


# ---------------------------------------------------------------- agent (LLM with tools)

_llm = None
REASONING = True  # False: enable_thinking=False (the model answers without internal reasoning; fewer tokens)
MODEL_OVERRIDE: str | None = None  # tests: replaces the .env model in this run only (evaluate_research.py --model)


def llm_with_tools():
    """ChatNVIDIA with the two tools and tool_choice="auto" (the model decides if and which one to call)."""
    global _llm
    if _llm is None:
        from langchain_nvidia_ai_endpoints import ChatNVIDIA
        env = dotenv_values(ROOT / ".env")
        model = ChatNVIDIA(model=MODEL_OVERRIDE or env.get("LLM_MODEL", "nvidia/nemotron-3.5-super-vl-120b-a12b"),
                           api_key=env["NVIDIA_API_KEY"],
                           base_url=env.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1"),
                           temperature=1.0, max_completion_tokens=4096,  # reasoning models spend tokens before answering
                           timeout=300)  # ChatNVIDIA's polling gives up after 60 s by default; NIM can take minutes
        _llm = model.bind_tools(tools.TOOLS, tool_choice="auto")
    return _llm


def fixed_tool_name(name: str) -> str:
    """GPT-OSS sometimes leaked its "harmony" channel into the tool name
    ('search_inside_incidents<|channel|>commentary'). If the name starts with a known tool name, use that."""
    if name in tools.TOOL_NAMES:
        return name
    for known in sorted(tools.TOOL_NAMES, key=len, reverse=True):
        if name.startswith(known):
            return known
    return name


def fix_tool_names(msg: AIMessage) -> int:
    """Fixes msg.tool_calls and the raw tool_calls (additional_kwargs), which ChatNVIDIA sends back to NIM."""
    n = 0
    for c in msg.tool_calls:
        new = fixed_tool_name(c["name"])
        if new != c["name"]:
            c["name"], n = new, n + 1
    for c in msg.additional_kwargs.get("tool_calls", []):
        f = c.get("function", {})
        if "name" in f:
            f["name"] = fixed_tool_name(f["name"])
    return n


def _close_json(text: str) -> dict | None:
    """GPT-OSS sometimes forgot to close the JSON of the arguments (seen on 2026-11-17:
    '{"searches":[{...},{...}]' without the final '}'). Adds the missing braces and brackets."""
    stack, in_string, escape = [], False, False
    for ch in text:
        if in_string:
            escape = (ch == "\\") and not escape
            if ch == '"' and not escape:
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch in "{[":
            stack.append("}" if ch == "{" else "]")
        elif ch in "}]" and stack:
            stack.pop()
    if in_string:
        return None
    try:
        data = json.loads(text + "".join(reversed(stack)))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def repair_malformed_calls(msg: AIMessage) -> int:
    """Turns into a valid call each invalid_tool_call whose JSON was only missing its closing braces.
    Also updates the raw tool_calls (additional_kwargs), which ChatNVIDIA sends back to NIM."""
    repaired, remaining = [], []
    for c in msg.invalid_tool_calls:
        args = _close_json(str(c.get("args") or ""))
        name = fixed_tool_name(str(c.get("name") or ""))
        if args is not None and name in tools.TOOL_NAMES:
            repaired.append({"name": name, "args": args, "id": c.get("id"), "type": "tool_call"})
        else:
            remaining.append(c)
    if repaired:
        msg.tool_calls = list(msg.tool_calls) + repaired
        msg.invalid_tool_calls = remaining
        raw = {c.get("id"): c for c in msg.additional_kwargs.get("tool_calls", [])}
        for c in repaired:
            if c["id"] in raw:
                raw[c["id"]].setdefault("function", {}).update({"name": c["name"], "arguments": json.dumps(c["args"])})
    return len(repaired)


def build_summary_list(candidates: list[dict]) -> str:
    """What the LLM reads to decide: ID, company, title and summary of each candidate (the danluu catalog
    summaries have a median of ~250 characters and usually say what happened and why). The passages do not
    go: the cause and fix details come through search_inside_incidents. This way more candidates fit in less
    text (10 summaries ≈ 2,500 characters; 5 incidents with passages ≈ 15,000)."""
    blocks = []
    for k, r in enumerate(candidates, 1):
        summary = (r.get("summary") or "").strip()
        lines = [f"### {k}. [{r['incident_id']}] {r['company']} — {r['title']}", f"Summary: {summary or '(no summary)'}"]
        if len(summary) < MIN_SUMMARY_CHARS:
            best = r.get("best_chunk") or {}
            if best.get("type") == "summary" or not best.get("content"):  # the best chunk was the summary itself
                best = (r.get("passages") or [{}])[0]
            if best.get("content"):
                lines.append(f"Most similar passage: {best['content'][:300]}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) if blocks else "(no incident found)"


def fill_missing_arguments(msg: AIMessage) -> int:
    """Fixes arguments in the wrong format before the tool validates them: a list sent as text (JSON inside
    a string) becomes a list, and a missing why in search_inside_incidents gets a neutral value so the tool
    still runs instead of failing validation. Returns how many fields were filled (it is logged: a sign
    that the model did not follow the format)."""
    n = 0
    for c in msg.tool_calls:
        # List sent as text with JSON inside (seen with Nemotron 3.5 on 2026-11-18:
        # {"searches": "[{\"incident_id\": ...}]"}): convert it to a list before the tool validates it.
        for field in ("searches", "queries"):
            value = c["args"].get(field)
            if isinstance(value, str) and value.strip().startswith("["):
                try:
                    converted = json.loads(value)
                except json.JSONDecodeError:
                    converted = (_close_json('{"x": ' + value) or {}).get("x")
                if isinstance(converted, list):
                    c["args"][field], n = converted, n + 1
        if c["name"] != "search_inside_incidents":
            continue
        for item in c["args"].get("searches") or []:
            if isinstance(item, dict) and not isinstance(item.get("why"), str):
                item["why"], n = "", n + 1
    if n:
        raw = {b.get("id"): b for b in msg.additional_kwargs.get("tool_calls", [])}
        for c in msg.tool_calls:
            if c["id"] in raw:
                raw[c["id"]].setdefault("function", {})["arguments"] = json.dumps(c["args"])
    return n


def _fixed_call(state: ResearchState) -> AIMessage:
    """--no-llm mode: looks inside the first 3 candidates with only the fixed cause and fix queries."""
    searches = [{"incident_id": r["incident_id"], "query": "", "why": ""}
                for r in state.get("candidates", [])[:tools.MAX_INCIDENTS_PER_CALL]]
    return AIMessage("", tool_calls=[{"name": "search_inside_incidents", "args": {"searches": searches},
                                      "id": "no-llm-1", "type": "tool_call"}])


def _system_prompt() -> str:
    if not AGENTIC_MODE:
        return prompts.SYSTEM_PROMPT
    hybrid = prompts.HYBRID_NOTE if tools.INCLUDE_DESCRIPTION_IN_FIRST_SEARCH else ""
    guidance = prompts.TRIAGE_GUIDANCE if TRIAGE_CONTEXT else ""
    return prompts.AGENTIC_SYSTEM_PROMPT + hybrid + guidance


def agent(state: ResearchState) -> dict:
    new = []
    agentic = AGENTIC_MODE and not state.get("candidates")
    if not state.get("messages") and agentic:  # first call, agentic mode: no incidents yet; the LLM searches
        triage = state.get("triage") if TRIAGE_CONTEXT else None
        new.append(HumanMessage(prompts.agentic_user_message(state["description"], state.get("symptoms", []),
                                                             state.get("search_request", ""), triage)))
    elif not state.get("messages"):  # first call: the message with the incidents found
        candidates_text = build_summary_list(state.get("candidates", []))
        new.append(HumanMessage(prompts.user_message(state["description"], state.get("symptoms", []),
                                                     candidates_text, state.get("search_request", ""))))
    if state.get("no_llm"):
        msg = _fixed_call(state) if not state.get("messages") else AIMessage("--no-llm mode: done.")
        return {"messages": new + [msg]}
    history = [SystemMessage(_system_prompt())] + list(state.get("messages", [])) + new
    infos = []
    for attempt in range(2):  # the 2nd only if the call comes back malformed or empty
        msg, info = _call_llm(history)
        infos.append(info)
        empty = not msg.tool_calls and not msg.invalid_tool_calls and not str(msg.content or "").strip()
        if attempt == 1 or msg.tool_calls or not (msg.invalid_tool_calls or empty):
            break
        if empty:
            # Answer with no text and no tool (seen with Nemotron 3.5: the reasoning uses up the token limit
            # before the answer). Ask once more, without changing the history.
            print("[agent] empty answer; asking again", flush=True)
            continue
        # Malformed call (invalid JSON in the arguments): the bad message does not go into the history
        # (NIM would refuse a tool_call without an answer); the model gets the error and tries again.
        error = "; ".join(str(c.get("error") or "invalid arguments")[:200] for c in msg.invalid_tool_calls)
        print(f"[agent] malformed tool call ({error}); asking again", flush=True)
        notice = HumanMessage(f"Your tool call was malformed ({error}). Call the tool again, with the arguments "
                              "in valid JSON, following the tool's format.")
        new.append(notice)
        history.append(notice)
    return {"messages": new + [msg], "llm_calls": infos,
            "timings": {f"agent_{len(state.get('llm_calls', [])) + 1}": round(sum(i["seconds"] for i in infos), 1)}}


def _call_llm(history: list) -> tuple[AIMessage, dict]:
    start = time.time()
    try:
        extra = {} if REASONING else {"chat_template_kwargs": {"enable_thinking": False}}
        msg = limite_llm.chamar(lambda: llm_with_tools().invoke(history, **extra), aviso="research agent")
    except Exception as e:
        print(f"[agent] failed ({type(e).__name__}: {str(e)[:120]}); the graph will try again", flush=True)
        raise
    info = {"seconds": round(time.time() - start, 1),
            "tool_calls": [{"name": c["name"], "args": c["args"]} for c in msg.tool_calls],  # name as it came
            "invalid": [{"name": c.get("name"), "args": str(c.get("args"))[:500], "error": str(c.get("error"))[:300]}
                        for c in msg.invalid_tool_calls],
            "text": msg.content if isinstance(msg.content, str) else str(msg.content),
            "usage": dict(msg.usage_metadata or {})}
    info["names_fixed"] = fix_tool_names(msg)
    info["json_repaired"] = repair_malformed_calls(msg)
    if info["json_repaired"]:  # also log the calls that became valid after the repair
        info["tool_calls"] += [{"name": c["name"], "args": c["args"]} for c in msg.tool_calls[-info["json_repaired"]:]]
    info["fields_filled"] = fill_missing_arguments(msg)
    return msg, info


def _should_retry(e: Exception) -> bool:
    # programming errors are not worth another attempt; the rest (timeout, 429, NIM 5xx) is
    return not isinstance(e, (ValueError, TypeError, KeyError, AttributeError, NameError))


# ---------------------------------------------------------------- modes and routing

def enable_agentic_mode() -> None:
    """Agentic mode: no initial search in code, up to 4 LLM calls and find_similar_incidents returning
    10 incidents."""
    global AGENTIC_MODE
    AGENTIC_MODE = True
    tools.N_DOCS = N_DOCS_FIND_AGENTIC


def enable_hybrid_mode() -> None:
    """Agentic mode + a safety net: the LLM's first search also searches with the original description (in
    code); its 10 incidents always come in, and the LLM queries add up to 5 new ones."""
    enable_agentic_mode()
    tools.INCLUDE_DESCRIPTION_IN_FIRST_SEARCH = True


def route_start(state: ResearchState) -> Literal["initial_search", "agent"]:
    if state.get("previous_findings"):  # refinement: always a new search in code (all modes)
        return "initial_search"
    return "agent" if state.get("candidates") or AGENTIC_MODE else "initial_search"


def after_agent(state: ResearchState) -> Literal["tools", "build_findings"]:
    last = state["messages"][-1]
    return "tools" if isinstance(last, AIMessage) and last.tool_calls else "build_findings"


def after_tools(state: ResearchState) -> Literal["agent", "build_findings"]:
    this_round = []
    for m in reversed(state["messages"]):
        if not isinstance(m, ToolMessage):
            break
        this_round.append(m.name)
    calls = len(state.get("llm_calls", []))
    limit = MAX_LLM_CALLS_AGENTIC if AGENTIC_MODE else MAX_LLM_CALLS
    if "find_similar_incidents" in this_round and calls < limit and not state.get("no_llm"):
        return "agent"
    return "build_findings"


# ---------------------------------------------------------------- output (code)

def build_findings(state: ResearchState) -> dict:
    deepened, new_incidents, reasons, log, warnings = {}, [], {}, [], []
    plan = {"deepen": [], "new_queries": [], "final_note": "", "warnings": warnings}
    for m in state.get("messages", []):
        if isinstance(m, AIMessage):
            for c in m.tool_calls:
                if c["name"] == "search_inside_incidents":
                    plan["deepen"] += [{"id": tools.short_id(str(s.get("incident_id", ""))), "query": s.get("query", ""),
                                        "why": s.get("why")}
                                       for s in c["args"].get("searches", []) if isinstance(s, dict)]
                elif c["name"] == "find_similar_incidents":
                    plan["new_queries"] += list(c["args"].get("queries", []))
                else:
                    warnings.append(f"unknown tool: {c['name']}")
            if not m.tool_calls and isinstance(m.content, str) and m.content.strip():
                plan["final_note"] = m.content.strip()
        elif isinstance(m, ToolMessage):
            if m.status == "error":
                warnings.append(f"{m.name}: {str(m.content)[:200]}")
            art = m.artifact or {}
            for i, passages in art.get("passages_by_incident", {}).items():
                deepened.setdefault(i, []).extend(passages)
            new_incidents += art.get("incidents", [])
            reasons.update(art.get("reasons", {}))
            log += art.get("search_log", [])
            warnings += art.get("warnings", [])
    findings, done = [], set()
    for r in [*state.get("candidates", []), *new_incidents]:
        if r["incident_id"] in done:
            continue
        done.add(r["incident_id"])
        passages = list(r.get("passages", []))
        texts = {d["content"] for d in passages}
        extra = [d for d in deepened.get(r["incident_id"], []) if d["content"] not in texts]
        is_deepened = r["incident_id"] in deepened or bool(r.get("deepened"))  # refinement: keeps the earlier one
        findings.append({**r, "deepened": is_deepened, "why": reasons.get(r["incident_id"], r.get("why")),
                         "passages": (extra + passages)[:MAX_PASSAGES]})  # deep search passages first
    # Order: the ones the LLM looked inside, in the order it listed them (the first is the one it finds most
    # similar); then the ones deepened in earlier rounds (refinement); then the others, by similarity.
    llm_order = {}
    for item in plan["deepen"]:
        llm_order.setdefault(item["id"], len(llm_order))
    findings.sort(key=lambda r: (0, llm_order[r["incident_id"]])
                  if r["incident_id"] in llm_order and r["incident_id"] in deepened
                  else ((1, 0) if r["deepened"] else (2, 0)))
    # Refinement: the incidents deepened in earlier rounds come back after the new deepened ones, as evidence
    # (the others from earlier rounds do not: they would take the places of the new ones).
    old = [r for r in state.get("previous_findings", []) if r.get("deepened") and r["incident_id"] not in done]
    findings = [r for r in findings if r["incident_id"] in llm_order and r["incident_id"] in deepened] + old + \
               [r for r in findings if not (r["incident_id"] in llm_order and r["incident_id"] in deepened)]
    findings = findings[:MAX_FINDINGS]  # the rest stay in seen_ids (they do not come back in a new search)
    done |= {r["incident_id"] for r in state.get("previous_findings", [])}
    seen = sorted(set(state.get("seen_ids", [])) | done)
    return {"findings": findings, "deepened": deepened, "new_incidents": new_incidents, "plan": plan,
            "seen_ids": seen, "search_log": log}


def build_graph(first_retry_wait: float = 15.0):
    g = StateGraph(ResearchState)
    g.add_node("initial_search", initial_search)
    g.add_node("agent", agent, retry_policy=RetryPolicy(max_attempts=3, initial_interval=first_retry_wait,
                                                        backoff_factor=2.0, jitter=True, retry_on=_should_retry))
    g.add_node("tools", ToolNode(tools.TOOLS))
    g.add_node("build_findings", build_findings)
    g.add_conditional_edges(START, route_start)
    g.add_edge("initial_search", "agent")
    g.add_conditional_edges("agent", after_agent)
    g.add_conditional_edges("tools", after_tools)
    g.add_edge("build_findings", END)
    return g.compile()


# ---------------------------------------------------------------- running

def _show(node: str, delta: dict) -> None:
    secs = delta.get("timings") or {}
    print(f"\n== {node}" + (f" ({list(secs.values())[0]}s)" if secs else ""), flush=True)
    if node == "initial_search":
        for s in delta["search_log"]:
            print(f"   search: {s['query'][:90]!r} -> {', '.join(s['ids'])}")
    elif node == "agent":
        for m in delta.get("messages", []):
            if isinstance(m, AIMessage):
                for c in m.tool_calls:
                    print(f"   calls {c['name']}: {json.dumps(c['args'], ensure_ascii=False)[:400]}")
                if not m.tool_calls:
                    print(f"   no tool: {str(m.content)[:300]}")
        for c in delta.get("llm_calls", []):
            if c.get("names_fixed"):
                print(f"   ({c['names_fixed']} tool name(s) fixed)")
    elif node == "tools":
        for m in delta.get("messages", []):
            print(f"   {m.name} ({m.status}): {str(m.content)[:300].replace(chr(10), ' ')}")
    elif node == "build_findings":
        for r in delta["findings"]:
            n_deep = sum(d.get("origin") == "deep_search" for d in r["passages"])
            print(f"   {r['incident_id']} {r['similarity']:.3f} {r['company']} — {r['title'][:50]}  "
                  f"{'DEEPENED ' if r['deepened'] else ''}passages: {len(r['passages'])} ({n_deep} from deep search)")
            if r.get("why"):
                print(f"      why: {r['why'][:150]}")
        for w in delta["plan"]["warnings"]:
            print(f"   warning: {w}")


def research(description: str, symptoms: list[str] | None = None, request: str = "", previous: dict | None = None,
             no_llm: bool = False, show=None, triage: dict | None = None) -> dict:
    """Runs the agent once and returns its final state (the output is in state["findings"])."""
    entry: dict = {"description": description, "symptoms": symptoms or [], "search_request": request, "no_llm": no_llm}
    if triage:
        entry["triage"] = triage
    if previous:
        seen = set(previous.get("seen_ids", [])) | {r["incident_id"] for r in previous["findings"]}
        entry.update({"previous_findings": previous["findings"], "seen_ids": sorted(seen)})
    state: dict = {}
    for part in build_graph().stream(entry, {"recursion_limit": 20}, stream_mode=["updates", "values"], version="v2"):
        if part["type"] == "values":
            state = part["data"]
        elif show:
            for node, delta in part["data"].items():
                show(node, delta or {})
    return state


def _to_json_ready(state: dict) -> dict:
    """Replaces the LangChain messages with plain dicts, to save the state as JSON."""
    out = {k: v for k, v in state.items() if k != "messages"}
    out["messages"] = [{"type": m.type, "content": m.content if isinstance(m.content, str) else str(m.content),
                        **({"tool_calls": m.tool_calls} if isinstance(m, AIMessage) and m.tool_calls else {}),
                        **({"tool": m.name} if isinstance(m, ToolMessage) else {})}
                       for m in state.get("messages", [])]
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("description", nargs="+")
    ap.add_argument("--symptom", action="append", default=[], help="can be repeated")
    ap.add_argument("--request", default="", help="request from the Diagnosis agent (refinement)")
    ap.add_argument("--previous", type=Path, help="JSON of a previous run (refinement)")
    ap.add_argument("--no-llm", action="store_true", help="fixed call, without NIM")
    ap.add_argument("--json", type=Path, help="saves the final state")
    ap.add_argument("--model", help="NIM model for this run only (default: LLM_MODEL in .env)")
    ap.add_argument("--agentic", action="store_true", help="agentic mode: the LLM runs the first search")
    ap.add_argument("--hybrid", action="store_true", help="hybrid mode: agentic + the original description in the first search")
    a = ap.parse_args()
    if a.model:
        global MODEL_OVERRIDE
        MODEL_OVERRIDE = a.model
    if a.hybrid:
        enable_hybrid_mode()
    elif a.agentic:
        enable_agentic_mode()
    previous = json.loads(a.previous.read_text()) if a.previous else None
    start = time.time()
    state = research(" ".join(a.description), a.symptom, a.request, previous, a.no_llm, _show)
    print(f"\ntotal: {time.time() - start:.0f}s, {len(state.get('llm_calls', []))} LLM call(s), "
          f"{len(state.get('search_log', []))} search(es)")
    if a.json:
        a.json.write_text(json.dumps(_to_json_ready(state), ensure_ascii=False, indent=1, default=str))
        print(f"state saved to {a.json}")


if __name__ == "__main__":
    main()
