"""Test: does the Triage node work inside a real LangGraph graph?

We build a tiny graph around the node and replace the agent with a fake one, so there is no
model call and it runs in a second. What we check:
  - the node reads "description" and writes "triage_result" and "symptoms"
  - the graph goes to the right place for each of the three next steps

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_node
"""
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

import agents.triage.node as node
from agents.triage.routing import ASK_USER, GO_TO_RESEARCH, TELL_RELATED_INCIDENT
from agents.triage.schema import RelatedIncident, TriageResult
from agents.triage.tests.checks import Checker


class State(TypedDict, total=False):
    description: str
    triage_result: TriageResult
    symptoms: list
    went_to: str


# Three fake answers of the agent, one for each next step.
FAKE_RESULTS = {
    "vague message": TriageResult(enough_information=False, missing_information=["Which service fails?"]),
    "login error": TriageResult(
        enough_information=True,
        symptoms=["login page returns error 500"],
        affected_service="login",
        related_incident=RelatedIncident(incident_id="INC-042", title="Login page returns HTTP 500"),
    ),
    "new problem": TriageResult(enough_information=True, symptoms=["empty lists"], affected_service="recommendations"),
}


def fake_run_agent(message):
    return FAKE_RESULTS[message], []  # same shape as the real run_agent: (result, messages history)


def mark(name):
    """A node that only records where the graph went."""
    return lambda state: {"went_to": name}


def build_graph():
    graph = StateGraph(State)
    graph.add_node("triage", node.triage_node)
    graph.add_node("ask_user", mark(ASK_USER))
    graph.add_node("tell_related", mark(TELL_RELATED_INCIDENT))
    graph.add_node("research", mark(GO_TO_RESEARCH))
    graph.add_edge(START, "triage")
    graph.add_conditional_edges("triage", node.route_after_triage, {
        ASK_USER: "ask_user",
        TELL_RELATED_INCIDENT: "tell_related",
        GO_TO_RESEARCH: "research",
    })
    for end_node in ("ask_user", "tell_related", "research"):
        graph.add_edge(end_node, END)
    return graph.compile()


node.run_agent = fake_run_agent  # the node uses the fake agent in this test
graph = build_graph()
checker = Checker()

final = graph.invoke({"description": "vague message"})
checker.check("vague message: the graph goes to ask_user", final["went_to"] == ASK_USER, f"(got {final.get('went_to')})")
checker.check("vague message: no symptoms are passed on", final["symptoms"] == [])

final = graph.invoke({"description": "login error"})
checker.check("related incident: the graph goes to tell_related_incident", final["went_to"] == TELL_RELATED_INCIDENT, f"(got {final.get('went_to')})")
checker.check("related incident: the result keeps the incident_id", final["triage_result"].related_incident.incident_id == "INC-042")

final = graph.invoke({"description": "new problem"})
checker.check("new problem: the graph goes to go_to_research", final["went_to"] == GO_TO_RESEARCH, f"(got {final.get('went_to')})")
checker.check("new problem: the symptoms are ready for the Research agent", final["symptoms"] == ["empty lists"])
checker.check("new problem: the original message is still in the state", final["description"] == "new problem")

checker.finish()
