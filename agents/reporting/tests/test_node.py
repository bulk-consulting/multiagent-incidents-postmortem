"""Test: does the Reporting node work inside a real LangGraph graph?

We build a tiny graph with only this node and replace the agent with a fake one, so there is no model
call and it runs in a second. What we check:
  - the node reads the state and writes the report, the attempts and the problems
  - if the model call crashes, the node still writes a report and records the error

Run from the repository root:
    .venv/Scripts/python.exe -m agents.reporting.tests.test_node
"""
import operator
from typing import Annotated, Any, TypedDict

from langgraph.graph import END, START, StateGraph

import agents.reporting.node as node
from agents.reporting.tests.checks import Checker
from agents.reporting.tests.fixtures import good_report_for, load_fixture


class State(TypedDict, total=False):
    incident_id: str
    description: str
    triage_result: Any
    findings: list
    diagnosis: Any
    report: Any
    report_attempts: int
    report_problems: list
    errors: Annotated[list, operator.add]  # the graph adds to this list, like the real state


def build_graph():
    graph = StateGraph(State)
    graph.add_node("reporting", node.reporting_node)
    graph.add_edge(START, "reporting")
    graph.add_edge("reporting", END)
    return graph.compile()


state = load_fixture("gitlab_diagnosis_en")
checker = Checker()

# 1) The agent works.
good = good_report_for(state)
node.run_reporting_agent = lambda s: (good, [], 1, [])
final = build_graph().invoke(state)
checker.check("the report is written in the state", final["report"].kind == "diagnosis")
checker.check("the attempts are recorded", final["report_attempts"] == 1)
checker.check("no problems and no errors", final["report_problems"] == [] and final.get("errors", []) == [])
checker.check("the other keys of the state are not lost", final["incident_id"] == state["incident_id"] and final["findings"] == state["findings"])

# 2) The agent used the fallback (it returns the problems that were left).
node.run_reporting_agent = lambda s: (good, [], 3, ["cause 1: source DAN-999 is not in the findings."])
final = build_graph().invoke(state)
checker.check("the problems that were left go to report_problems", final["report_problems"] == ["cause 1: source DAN-999 is not in the findings."])
checker.check("and an error is recorded for the log", final["errors"] == [{"node": "reporting", "error": "cause 1: source DAN-999 is not in the findings."}])


# 3) The model call crashes (network, key, busy server).
def crash(s):
    raise RuntimeError("The model call failed 3 times.")


node.run_reporting_agent = crash
final = build_graph().invoke(state)
checker.check("when the model call crashes, there is still a report", final["report"].kind == "inconclusive")
checker.check("the crash is recorded as an error", final["errors"] and "model call failed" in final["errors"][0]["error"])

checker.finish()
