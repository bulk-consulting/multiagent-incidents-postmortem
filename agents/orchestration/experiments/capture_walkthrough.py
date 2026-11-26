"""
Records, step by step, everything that happens in one investigation through the real graph, to explain the system.

For each node: what it read from the state, what the agent did inside (the model's messages, tool calls, searches,
the Diagnosis comparisons and the rules applied, the Reporting attempts) and what it wrote back; and, after each
node, which routing rule chose the next one. The agents are not changed: the script wraps the functions the graph
uses to call them (graph.run_triage, run_research, run_diagnosis, run_reporting).

Scenarios: a vague message → the Triage agent asks → pause → the analyst answers → Research → Diagnosis (with the
refinement loop) → Reporting. Every pause is answered (up to MAX_ANALYST_ROUNDS): the first answer is the scenario's,
the next ones come from the case's script (simulated analyst). dan104 (default) and dan197, from the demos of the E5 tests.

Usage (from the repository root, database up):
    multiagent_env/bin/python -I agents/orchestration/experiments/capture_walkthrough.py [dan104|dan197]
Output: agents/orchestration/experiments/results/walkthrough_<date>.json
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from langgraph.checkpoint.memory import InMemorySaver  # noqa: E402
from langgraph.types import Command  # noqa: E402

import agents.orchestration.graph as graph  # noqa: E402
from agents.diagnosis import agent as diagnosis_agent  # noqa: E402
from agents.diagnosis.schema import parse_diagnosis_answer  # noqa: E402
from agents.orchestration.state import make_serializer  # noqa: E402
from agents.reporting.agent import run_reporting_agent  # noqa: E402
from agents.triage.agent import run_agent as run_triage_agent  # noqa: E402
from agents.orchestration.experiments.run_trigger_policy import answer_for, load_case  # noqa: E402

SCENARIOS = {
    # FINAL-EN of the E5 tests (DAN-197): a vague message about failing checks
    "dan197": ("Our automated checks are failing sporadically.",
               "We monitor a hosted database offering, and the failing step is the probe that provisions a new "
               "container. Our provisioning logic and request method have been unchanged for months. We are unaware of "
               "anything changing just before the errors appeared. Requests to provision containers keep getting "
               "rejected because a parameter is deemed unacceptable. Some attempts pass, and the diagnostics do not "
               "tell us which parameter caused the rejection."),
    # DEMO-104 of the E5 tests (DAN-104): a vague message about a whole region failing
    "dan104": ("Requests are failing across an entire region.",
               "It is our cloud object store, and products relying on it are having trouble too. We were looking into "
               "unusually slow billing progress. An engineer followed our usual operating procedure to take a handful "
               "of machines out of infrastructure supporting that process. Failures appeared abruptly this morning in "
               "our US East location, affecting users of the object store and products relying on it. We cannot read, "
               "enumerate, write or erase objects through the APIs."),
}
SCENARIO = sys.argv[1] if len(sys.argv) > 1 else "dan104"
CASE_IDS = {"dan197": "DAN-197", "dan104": "DAN-104"}
FIRST_MESSAGE, ANSWER = SCENARIOS[SCENARIO]

inside = []  # what each agent did, in call order (the graph's node update comes separately)


def _dump(x):
    return x.model_dump() if hasattr(x, "model_dump") else x


def _short(text, n=1500):
    text = text if isinstance(text, str) else json.dumps(text, ensure_ascii=False, default=str)
    return text if len(text) <= n else text[:n] + " …"


def traced_triage(description):
    t0 = time.time()
    result, messages = run_triage_agent(description)
    inside.append({"agent": "triage", "seconds": round(time.time() - t0, 1), "input": {"description": description},
                   "messages": [{"role": m["role"], "content": _short(m.get("content") or ""),
                                 "tool_calls": [{"name": c["function"]["name"], "arguments": c["function"]["arguments"]}
                                                for c in m.get("tool_calls") or []]}
                                for m in messages[1:]],  # the system prompt is in agents/triage/prompts.py
                   "result": _dump(result)})
    return result


def traced_research(description, symptoms, request, previous):
    t0 = time.time()
    state = graph._run_research(description, symptoms, request, previous)
    inside.append({
        "agent": "research", "seconds": round(time.time() - t0, 1),
        "input": {"symptoms": symptoms, "request": request,
                  "previous_ids": [r["incident_id"] for r in (previous or {}).get("findings", [])]},
        "searches": [{"step": e.get("step"), "query": _short(e.get("query") or "", 300),
                      "excluded": len((e.get("filter") or {}).get("exclude") or []), "ids": e.get("ids")}
                     for e in state.get("search_log", [])],
        "llm_calls": [{"seconds": c.get("seconds"), "tool_calls": c.get("tool_calls"), "text": _short(c.get("text") or "", 600)}
                      for c in state.get("llm_calls", [])],
        "plan": state.get("plan"),
        "findings": [{"id": r["incident_id"], "company": r.get("company"), "title": r.get("title"),
                      "deepened": r.get("deepened"), "why": r.get("why"),
                      "passages": [{"section": d.get("section"), "source": d.get("query_source") or d.get("origin"),
                                    "content": _short(d.get("content") or "", 400)} for d in r.get("passages", [])[:4]]}
                     for r in state.get("findings", [])],
    })
    return state


def traced_diagnosis(description, triage, findings, research_round, max_rounds, previous_requests):
    t0 = time.time()
    result, messages = diagnosis_agent.run_agent(description, triage, findings, research_round, max_rounds,
                                                 previous_requests)
    draft = parse_diagnosis_answer(messages[-1]["content"])
    inside.append({"agent": "diagnosis", "seconds": round(time.time() - t0, 1),
                   "input": {"triage": triage, "research_round": research_round, "previous_requests": previous_requests,
                             "findings": [(r["incident_id"], r.get("deepened")) for r in findings]},
                   "user_message": _short(messages[1]["content"], 6000),
                   "model_draft": _dump(draft), "turns": sum(m["role"] == "assistant" for m in messages),
                   "decided_by_code": _dump(result)})
    return result


def traced_reporting(state):
    t0 = time.time()
    report, messages, attempts, problems = run_reporting_agent(state)
    inside.append({"agent": "reporting", "seconds": round(time.time() - t0, 1), "attempts": attempts,
                   "problems": problems, "report": _dump(report),
                   "fix_requests": [m["content"] for m in messages[3:] if m["role"] == "user"]})
    errors = [{"node": "reporting", "error": "; ".join(problems)}] if problems else []
    return {"report": report, "report_attempts": attempts, "report_problems": problems, "errors": errors}


# The routing rule that chose the next node, by node (agents/orchestration/graph.py)
ROUTES = {"triage": "route_after_triage", "research": "route_after_research", "diagnosis": "route_after_diagnosis",
          "ask_analyst": "edge ask_analyst → triage", "report": "edge report → END"}


def run_phase(g, graph_input, config, steps):
    for part in g.stream(graph_input, config, stream_mode="updates"):
        for node, update in part.items():
            if node == "__interrupt__":
                steps.append({"node": "pause", "interrupt": update[0].value})
                return True
            step = {"node": node, "update": {k: _dump(v) for k, v in (update or {}).items() if k != "trace"},
                    "trace": (update or {}).get("trace"), "inside": inside[:]}
            inside.clear()
            steps.append(step)
    return False


def main() -> None:
    graph.run_triage, graph.run_research = traced_triage, traced_research
    graph.run_diagnosis, graph.run_reporting = traced_diagnosis, traced_reporting
    g = graph.build_graph(InMemorySaver(serde=make_serializer()))
    config = {"configurable": {"thread_id": f"WALK-{time.time():.0f}"}}
    steps = []
    paused = run_phase(g, {"incident_id": "WALK-1", "description": FIRST_MESSAGE}, config, steps)
    # The analyst answers every pause, up to the graph's limit: the first answer is the scenario's; the next ones
    # (questions of the Diagnosis agent) come from the case's script, matched by topic (the simulated analyst of
    # run_trigger_policy.py).
    conversation = load_case(CASE_IDS[SCENARIO])["conversation"]
    answers = 0
    while paused and answers < graph.MAX_ANALYST_ROUNDS:
        questions = steps[-1]["interrupt"].get("questions", [])
        answer = ANSWER if answers == 0 else answer_for(questions, conversation)[0]
        steps.append({"node": "analyst", "answer": answer})
        answers += 1
        paused = run_phase(g, Command(resume=answer), config, steps)
    # the next node of each step is the node of the following step (the pause stands for ask_analyst)
    real = [s for s in steps if s["node"] not in ("analyst",)]
    for a, b in zip(real, real[1:]):
        a["next"] = "ask_analyst (pause)" if b["node"] == "pause" else b["node"]
        a["rule"] = ROUTES.get(a["node"])
    out = HERE / "results" / f"walkthrough_{SCENARIO}_{datetime.now():%Y-%m-%d_%H%M}.json"
    final = {k: _dump(v) for k, v in g.get_state(config).values.items()}
    out.write_text(json.dumps({"first_message": FIRST_MESSAGE, "answer": ANSWER, "steps": steps,
                               "final_state": final}, ensure_ascii=False, indent=1, default=str))
    for s in steps:
        print(s["node"], (s.get("trace") or [{}])[0].get("summary", "") if s.get("trace") else "", "→", s.get("next", ""))
    print(f"\nsaved to {out}")


if __name__ == "__main__":
    main()
