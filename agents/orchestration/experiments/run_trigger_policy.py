"""
When should the Triage agent ask whether anything changed before the problem? Two policies, through the real graph.

    A  ask ONCE whenever no analyst message mentions recent changes
    B  ask about changes only when another question is needed anyway (the symptom or the service is missing)
Both rules are in agents/triage/prompts.py (TRIGGER_RULES); B is the default since 2026-11-25.

The first message of each reworded case says WHAT fails and WHERE, but no change (conversation[0] + the answers about
the service and the symptoms): the situation where A and B behave differently. A simulated analyst answers the
questions with the case's script (conversation). The graph runs Triage → Research → Diagnosis with the refinement
loop; the report is built in code (the Reporting agent is not what is measured here).

Measured per case: questions answered by the analyst, triggers that reached the Diagnosis agent, whether the right
post-mortem was found and deepened, and whether the top hypothesis is based on it.

Usage (from the repository root, database up):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_trigger_policy.py --policy A [--cases DAN-018,...]
        [--real-report]   # Mari's Reporting agent (default: the report built in code)
        [--postgres]      # PostgresSaver, as in the demo (default: InMemorySaver)
Output: agents/orchestration/experiments/results/trigger_policy_<A|B>_<date>.json
"""
from __future__ import annotations

import argparse
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
import agents.triage.agent as triage_agent  # noqa: E402
from agents.orchestration.state import make_serializer  # noqa: E402

CASES = ["DAN-104", "DAN-145", "DAN-211", "DAN-125", "DAN-018", "DAN-017", "DAN-116", "DAN-164",
         "DAN-004", "DAN-121", "DAN-154", "DAN-197"]
CASES_DIR = HERE / "postmortems"
MAX_ANSWERS = 3

# The simulated analyst (same matching as run_triage_scenarios.py, copied to avoid that module's prompt changes).
TOPICS = ["service", "trigger", "timing", "symptoms"]  # conversation[1..4]
KEYWORDS = {
    "service": ["service", "system", "component", "application", "product", "which", "name", "platform"],
    "trigger": ["change", "deploy", "before", "recent", "trigger", "update", "release", "maintenance",
                "command", "migration", "upgrade", "config"],
    "timing": ["when", "start", "since", "time", "who", "how many", "users", "customers", "scope", "region",
               "impact", "affect"],
    "symptoms": ["error", "symptom", "message", "log", "code", "behavior", "behaviour", "see", "metric",
                 "status", "latency", "fail", "observ"],
}


def load_case(case_id):
    return json.loads((CASES_DIR / f"{case_id}_rewrite.json").read_text(encoding="utf-8"))


def first_message(case):
    """What fails and where, without any change: conversation[0] + the service and symptoms answers."""
    conv = case["conversation"]
    return " ".join([conv[0]["analyst"], conv[1]["analyst"], conv[4]["analyst"]])


def answer_for(questions, conversation):
    script = {topic: conversation[k + 1]["analyst"] for k, topic in enumerate(TOPICS)}
    text = " ".join(questions).lower()
    matched = [t for t in TOPICS if any(w in text for w in KEYWORDS[t])] or ["service"]
    return " ".join(script[t] for t in matched), matched


def _report_dict(report):
    return (report.model_dump() if hasattr(report, "model_dump") else report) or {}


def run_case(g, case_id):
    case = load_case(case_id)
    config = {"configurable": {"thread_id": f"{case_id}-{time.time()}"}}
    out = g.invoke({"incident_id": case_id, "description": first_message(case)}, config)
    pauses = []
    while out.get("__interrupt__") and len(pauses) < MAX_ANSWERS:
        questions = out["__interrupt__"][0].value["questions"]
        answer, topics = answer_for(questions, case["conversation"])
        pauses.append({"questions": questions, "answer_topics": topics})
        out = g.invoke(Command(resume=answer), config)
    state = g.get_state(config).values
    d = state.get("diagnosis")
    top = d.hypotheses[0].based_on if d is not None and d.hypotheses else []
    research_traces = [t["summary"] for t in state.get("trace", []) if t["node"] == "research"]
    return {
        "case": case_id, "first_message": first_message(case), "pauses": pauses,
        "questions_answered": len(pauses), "asked_about_changes": any(
            "trigger" in p["answer_topics"] for p in pauses),
        "triggers": list(getattr(state.get("triage_result"), "triggers", []) or []),
        "research_rounds": len(research_traces), "research": research_traces,
        "right_deepened_any_round": any(case_id in s.split("deepened")[1] for s in research_traces if "deepened" in s),
        "right_in_final_findings": any(r["incident_id"] == case_id for r in state.get("findings", [])),
        "top_based_on": top, "top_is_right": case_id in top,
        "final": _report_dict(state.get("report")).get("kind"), "next_paused": bool(out.get("__interrupt__")),
        "report": _report_dict(state.get("report")), "report_attempts": state.get("report_attempts"),
        "report_problems": state.get("report_problems", []),
        "diagnosis": d.model_dump() if d is not None else None,
        "findings_ids": [(r["incident_id"], r.get("deepened")) for r in state.get("findings", [])],
        "errors": state.get("errors", []),
        "real_trigger": case["discovered_later"].get("trigger") if isinstance(case.get("discovered_later"), dict) else None,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--policy", choices=["A", "B"], required=True)
    ap.add_argument("--cases", default=",".join(CASES))
    ap.add_argument("--real-report", action="store_true", help="Mari's Reporting agent instead of the report in code")
    ap.add_argument("--postgres", action="store_true", help="PostgresSaver (as in the demo) instead of InMemorySaver")
    ap.add_argument("--report-no-thinking", action="store_true",
                    help="the Reporting agent's model with the reasoning off and temperature 0 (the test of "
                         "2026-11-25, section 17 of the report; since then it is the default in agents/reporting)")
    a = ap.parse_args()
    triage_agent.set_trigger_policy(a.policy)
    if not a.real_report:
        graph.run_reporting = graph.code_report_node  # the report in code: not measured here
    if a.report_no_thinking:
        import agents.reporting.agent as reporting_agent
        from agents.triage.llm import chat
        reporting_agent.chat = lambda messages, max_tokens=8192, **kw: chat(
            messages, max_tokens=max_tokens, temperature=0, chat_template_kwargs={"enable_thinking": False})
    from agents.orchestration.run import checkpointer
    tag = ("_report" if a.real_report else "") + ("_nothink" if a.report_no_thinking else "") + ("_pg" if a.postgres else "")
    out = HERE / "results" / f"trigger_policy_{a.policy}{tag}_{datetime.now():%Y-%m-%d_%H%M}.json"
    with checkpointer(memory=not a.postgres) as saver:
        run_all(graph.build_graph(saver), a.cases.split(","), out)


def run_all(g, cases, out):
    rows = []
    for case_id in cases:
        t0 = time.time()
        try:
            row = run_case(g, case_id)
        except Exception as e:  # record it and go on
            row = {"case": case_id, "error": f"{type(e).__name__}: {str(e)[:300]}"}
        row["seconds"] = round(time.time() - t0)
        rows.append(row)
        out.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
        print(f"{case_id} ({row['seconds']}s) " + (row.get("error") or
              f"answers={row['questions_answered']} asked_changes={row['asked_about_changes']} "
              f"triggers={len(row['triggers'])} rounds={row['research_rounds']} "
              f"right_deepened={row['right_deepened_any_round']} top_right={row['top_is_right']} final={row['final']} "
              f"report_attempts={row['report_attempts']} problems={len(row['report_problems'])}"),
              flush=True)
    print(f"\nsaved to {out}")


if __name__ == "__main__":
    main()
