"""The main graph: Triage → Research → Diagnosis → Report, with the refinement loop and the pause for the analyst.

    START → triage ─┬─ ask_user ──────────────► ask_analyst (interrupt) ──► triage
                    ├─ tell_related_incident ─► related_incident ──► END
                    ├─ go_to_research ────────► research ──► diagnosis ─┬─ evidence enough ─────────► report
                    │                              │ (failed, nothing found ──► report)
                    │                              ▲                    ├─ refine, rounds left ─────► research
                    │                              └────────────────────┤
                    │                                                   ├─ data from the analyst ───► ask_analyst
                    │                                                   └─ otherwise / error ───────► report (inconclusive)
                    └─ error ─────────────────► report (inconclusive)
    report ──► END        (Mari's Reporting agent validates its own report and fixes it, up to 3 attempts)

The contract (state keys, formats, who owns each node) is docs/E5_Estado_e_Formatos.md; the state is
agents/orchestration/state.py.

The agents are not rewritten: each node calls an agent and writes its result into the state. The agents are reached
through the module variables run_triage, run_research, run_diagnosis and run_reporting, so the integration tests can
replace them with fake ones (no model call).

The report is written by Mari's Reporting agent (agents/reporting/node.py), which also validates it (sources and links
in the findings, causes = the diagnosis hypotheses) and fixes it. When there is no diagnosis (an agent failed before
it), the report is the inconclusive one built in code (code_report_node), because the Reporting agent needs the
diagnosis. A separate validation node (validate_report_node, the first design of the contract) can still be added
with build_graph(validate_report=...). The related-incident answer is still provisional (related_incident_node).

Errors: when an agent fails (after its own retries), the node writes the error in `errors` and the routing goes to
the report, which comes out inconclusive. An investigation always ends with an answer.

After the analyst answers (ask_analyst), the investigation starts again with the richer description: the Triage
agent reads it, and the Research agent searches from scratch (rounds back to 0). The analyst is asked at most
MAX_ANALYST_ROUNDS times per investigation; after that the report comes out inconclusive.
"""
from __future__ import annotations

import time
from typing import Literal

from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt

from agents.diagnosis import agent as diagnosis_agent
from agents.orchestration.state import MAX_REPORT_FIXES, MAX_RESEARCH_ROUNDS, InvestigationState
from agents.reporting.node import reporting_node
from agents.research import agent as research_agent
from agents.triage import node as triage_node_module
from agents.triage.routing import ASK_USER, GO_TO_RESEARCH, TELL_RELATED_INCIDENT

MAX_ANALYST_ROUNDS = 3   # answers the analyst can give in one investigation (triage + diagnosis questions)
ANSWER_PREFIX = "\n\nAnalyst answer: "  # how an answer is joined to the description (same as the experiments)


# ---------------------------------------------------------------- the agents (replaced by fakes in the tests)

def _run_triage(description: str):
    """Mari's Triage node, with the state names it still uses (descricao/sintomas) translated."""
    out = triage_node_module.triage_node({"descricao": description})
    return out["triage_result"]


def _run_research(description: str, symptoms: list[str], request: str, previous: dict | None) -> dict:
    """The Research agent (hybrid mode, the best in the E5 tests). Returns its final state."""
    research_agent.enable_hybrid_mode()
    return research_agent.research(description, symptoms, request=request, previous=previous)


def _run_diagnosis(description, triage: dict, findings, research_round: int, max_rounds: int):
    result, _messages = diagnosis_agent.run_agent(description, triage, findings, research_round, max_rounds)
    return result


run_triage = _run_triage
run_research = _run_research
run_diagnosis = _run_diagnosis
run_reporting = reporting_node  # Mari's node: report, report_attempts, report_problems, errors


def _step(node: str, start: float, summary: str) -> dict:
    return {"trace": [{"node": node, "seconds": round(time.time() - start, 1), "summary": summary}]}


def _error(node: str, start: float, e: Exception) -> dict:
    text = f"{type(e).__name__}: {str(e)[:300]}"
    return {"errors": [{"node": node, "error": text}], **_step(node, start, f"error: {text[:120]}")}


# ---------------------------------------------------------------- nodes

def triage_node(state: InvestigationState) -> dict:
    start = time.time()
    try:
        result = run_triage(state["description"])
    except Exception as e:  # the agent gave up (model down, invalid answers): inconclusive report
        return {"triage_result": None, **_error("triage", start, e)}
    update = {"triage_result": result, "symptoms": list(result.symptoms)}
    if not result.enough_information:
        update["pending_questions"] = list(result.missing_information)
    return {**update, **_step("triage", start, f"enough information: {result.enough_information}; "
                                               f"symptoms: {len(result.symptoms)}")}


def related_incident_node(state: InvestigationState) -> dict:
    """Provisional (Mari's node): the answer "this is already being investigated", without the LLM."""
    start = time.time()
    related = state["triage_result"].related_incident
    report = {"incident_id": state.get("incident_id"), "kind": "related_incident",
              "related_incident": {"incident_id": related.incident_id, "title": related.title},
              "summary": f"This looks like an incident already under investigation: {related.incident_id} "
                         f"({related.title})."}
    return {"report": report, **_step("related_incident", start, related.incident_id)}


def research_node(state: InvestigationState) -> dict:
    start = time.time()
    rounds = state.get("research_rounds", 0)
    previous = ({"findings": state.get("findings", []), "seen_ids": state.get("seen_ids", [])}
                if rounds > 0 else None)  # a refinement starts from what was already found
    request = state.get("search_request", "") if rounds > 0 else ""
    try:
        out = run_research(state["description"], state.get("symptoms", []), request, previous)
    except Exception as e:
        # the round counts, so that a broken search does not loop forever
        return {"research_rounds": rounds + 1, **_error("research", start, e)}
    findings = out.get("findings", [])
    deepened = [r["incident_id"] for r in findings if r.get("deepened")]
    return {"findings": findings, "seen_ids": out.get("seen_ids", []), "research_rounds": rounds + 1,
            **_step("research", start, f"round {rounds + 1}: {len(findings)} incidents, deepened {deepened}"
                                       + (f"; request: {request[:80]!r}" if request else ""))}


def _triage_for_diagnosis(triage_result) -> dict:
    if triage_result is None:
        return {}
    triage = {"affected_service": triage_result.affected_service, "symptoms": list(triage_result.symptoms),
              "category": triage_result.category}
    if hasattr(triage_result, "trigger"):  # only if the Triage agent extracts it (proposed to Mari in the E5 tests)
        triage["trigger"] = triage_result.trigger
    return triage


def diagnosis_node(state: InvestigationState) -> dict:
    start = time.time()
    rounds = state.get("research_rounds", 1)
    try:
        result = run_diagnosis(state["description"], _triage_for_diagnosis(state.get("triage_result")),
                               state.get("findings", []), rounds, MAX_RESEARCH_ROUNDS)
    except Exception as e:
        return {"diagnosis": None, **_error("diagnosis", start, e)}
    update = {"diagnosis": result, "search_request": result.search_request,
              "pending_questions": list(result.questions_for_analyst)}
    top = result.hypotheses[0] if result.hypotheses else None
    summary = (f"{result.next_step}; sufficient: {result.evidence_sufficient}"
               + (f"; top: [{top.confidence}] {top.based_on}" if top else "; no hypothesis"))
    return {**update, **_step("diagnosis", start, summary)}


def ask_analyst_node(state: InvestigationState) -> dict:
    """Pauses with the questions; the answer is joined to the description and the investigation starts again.
    Nothing expensive before interrupt(): the node runs again from the start when the graph is resumed."""
    answer = interrupt({"incident_id": state.get("incident_id"), "questions": state.get("pending_questions", [])})
    answer = str(answer).strip()
    return {"description": state["description"] + ANSWER_PREFIX + answer, "analyst_answers": [answer],
            "pending_questions": [],
            # start again with the richer description: a fresh search, not a refinement
            "research_rounds": 0, "findings": [], "seen_ids": [], "search_request": "", "diagnosis": None,
            "trace": [{"node": "ask_analyst", "seconds": 0, "summary": f"answer: {answer[:80]!r}"}]}


def report_node(state: InvestigationState) -> dict:
    """The Reporting agent (Mari's) when there is a diagnosis; the inconclusive report built in code otherwise."""
    if state.get("diagnosis") is None or state.get("triage_result") is None:
        return code_report_node(state)
    start = time.time()
    out = run_reporting(state)
    report = out.get("report")
    report = (report.model_dump() if hasattr(report, "model_dump") else report) or {}
    summary = f"{report.get('kind')}, {len(report.get('causes', []))} causes, attempts: {out.get('report_attempts')}"
    if out.get("report_problems"):
        summary += f"; fallback after problems: {len(out['report_problems'])}"
    return {**out, **_step("report", start, summary)}


def code_report_node(state: InvestigationState) -> dict:
    """The report built in code from the diagnosis and the findings, in the format of the contract (section 6),
    without the LLM. Used when there is no diagnosis (inconclusive), and by the tests as a fake Reporting agent."""
    start = time.time()
    d = state.get("diagnosis")
    by_id = {r["incident_id"]: r for r in state.get("findings", [])}
    errors = state.get("errors", [])
    if d is not None and d.evidence_sufficient:
        causes = [{"root_cause": h.cause, "remediation_steps": [], "changes": None, "prevention_checklist": [],
                   "sources": [{"incident_id": i, "title": by_id[i].get("title", ""), "url": by_id[i].get("url", "")}
                               for i in h.based_on if i in by_id],
                   "confidence": h.confidence} for h in d.hypotheses if h.confidence in ("high", "medium")]
        report = {"incident_id": state.get("incident_id"), "kind": "diagnosis",
                  "summary": f"Most likely cause: {d.hypotheses[0].cause}", "causes": causes, "gaps": list(d.gaps),
                  "suggested_checks": []}
    else:
        gaps = list(d.gaps) if d is not None else []
        if errors:
            gaps.append("The investigation could not finish: " + "; ".join(f"{e['node']} failed" for e in errors))
        if not gaps:
            gaps = ["No past incident gave enough evidence for a diagnosis."]
        report = {"incident_id": state.get("incident_id"), "kind": "inconclusive",
                  "summary": "The evidence found is not enough for a diagnosis.", "causes": [], "gaps": gaps,
                  "suggested_checks": list(d.questions_for_analyst) if d is not None else []}
    return {"report": report, "report_problems": [],
            **_step("report", start, f"{report['kind']}, {len(report['causes'])} causes")}


def validate_report_node(state: InvestigationState) -> dict:
    """Provisional (Mari's validation): every source must be in the findings with the same url; a diagnosis needs
    at least 1 cause with a source; an inconclusive report needs at least 1 gap."""
    start = time.time()
    report = state.get("report") or {}
    report = report.model_dump() if hasattr(report, "model_dump") else report
    urls = {r["incident_id"]: r.get("url", "") for r in state.get("findings", [])}
    problems = []
    if report.get("kind") == "diagnosis":
        if not report.get("causes"):
            problems.append("a diagnosis report needs at least 1 cause")
        for c in report.get("causes", []):
            if not c.get("sources"):
                problems.append(f"cause without a source: {c.get('root_cause', '')[:60]}")
            for s in c.get("sources", []):
                if s.get("incident_id") not in urls:
                    problems.append(f"source not in the findings: {s.get('incident_id')}")
                elif s.get("url") != urls[s["incident_id"]]:
                    problems.append(f"url of {s['incident_id']} differs from the findings")
    elif report.get("kind") == "inconclusive" and not report.get("gaps"):
        problems.append("an inconclusive report needs at least 1 gap")
    attempts = state.get("report_attempts", 0) + (1 if problems else 0)
    return {"report_problems": problems, "report_attempts": attempts,
            **_step("validate_report", start, "ok" if not problems else f"{len(problems)} problems")}


# ---------------------------------------------------------------- routing (code)

def route_after_triage(state: InvestigationState) -> Literal["ask_analyst", "related_incident", "research", "report"]:
    result = state.get("triage_result")
    if result is None:  # the Triage agent failed
        return "report"
    step = triage_node_module.route_after_triage({"triage_result": result})
    if step == ASK_USER:
        if len(state.get("analyst_answers", [])) >= MAX_ANALYST_ROUNDS or not state.get("pending_questions"):
            return "report"
        return "ask_analyst"
    if step == TELL_RELATED_INCIDENT:
        return "related_incident"
    assert step == GO_TO_RESEARCH, step
    return "research"


def route_after_research(state: InvestigationState) -> Literal["diagnosis", "report"]:
    # the Research agent failed and there is nothing to diagnose (a failed refinement keeps the earlier findings)
    return "diagnosis" if state.get("findings") else "report"


def route_after_diagnosis(state: InvestigationState) -> Literal["report", "research", "ask_analyst"]:
    d = state.get("diagnosis")
    if d is None:  # the Diagnosis agent failed
        return "report"
    if d.evidence_sufficient:
        return "report"
    if d.next_step == "refine_search" and state.get("research_rounds", 0) < MAX_RESEARCH_ROUNDS:
        return "research"
    if (d.next_step == "ask_analyst" and state.get("pending_questions")
            and len(state.get("analyst_answers", [])) < MAX_ANALYST_ROUNDS):
        return "ask_analyst"
    return "report"


def route_after_validation(state: InvestigationState) -> Literal["report", "__end__"]:
    if state.get("report_problems") and state.get("report_attempts", 0) <= MAX_REPORT_FIXES:
        return "report"
    return END


# ---------------------------------------------------------------- the graph

def build_graph(checkpointer=None, report=None, validate_report=None, related_incident=None):
    """The compiled main graph. checkpointer: InMemorySaver in the tests, PostgresSaver in the demo (needed for the
    pause: interrupt). report: replaces report_node (Reporting agent + code fallback). validate_report: an optional
    validation node after the report (e.g. validate_report_node). related_incident: replaces the provisional node."""
    g = StateGraph(InvestigationState)
    g.add_node("triage", triage_node)
    g.add_node("related_incident", related_incident or related_incident_node)
    g.add_node("research", research_node)
    g.add_node("diagnosis", diagnosis_node)
    g.add_node("ask_analyst", ask_analyst_node)
    g.add_node("report", report or report_node)
    if validate_report:
        g.add_node("validate_report", validate_report)
    g.add_edge(START, "triage")
    g.add_conditional_edges("triage", route_after_triage)
    g.add_edge("related_incident", END)
    g.add_conditional_edges("research", route_after_research)
    g.add_conditional_edges("diagnosis", route_after_diagnosis)
    g.add_edge("ask_analyst", "triage")
    if validate_report:  # optional: Mari's Reporting agent already validates its own report
        g.add_edge("report", "validate_report")
        g.add_conditional_edges("validate_report", route_after_validation)
    else:
        g.add_edge("report", END)
    return g.compile(checkpointer=checkpointer)
