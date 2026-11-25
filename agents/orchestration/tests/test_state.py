"""Test: does the shared state work inside a real LangGraph graph with a checkpointer?

A tiny graph with fake nodes (no model, no database), so it runs in a second. What we check:
  - the Pydantic results (TriageResult, DiagnosisResult) come back from the checkpointer as the same objects,
    with the allowlist serializer (make_serializer), so a future strict LangGraph will still read them
  - errors and trace accumulate (reducers) instead of being replaced
  - interrupt() pauses the graph and Command(resume=...) continues it with the analyst's answer,
    on the same thread_id (= incident_id)

Run from the repository root:
    python -m agents.orchestration.tests.test_state
"""
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from agents.diagnosis.schema import DiagnosisResult
from agents.orchestration.state import InvestigationState, make_serializer
from agents.triage.schema import TriageResult
from agents.triage.tests.checks import Checker

checker = Checker()


def fake_triage(state):
    if "checkout" not in state["description"]:  # first time: not enough information
        result = TriageResult(enough_information=False, missing_information=["Which service is failing?"])
        return {"triage_result": result, "pending_questions": result.missing_information,
                "trace": [{"node": "triage", "summary": "asks the analyst"}]}
    result = TriageResult(enough_information=True, symptoms=["checkout returns 500"], affected_service="checkout")
    return {"triage_result": result, "symptoms": result.symptoms,
            "trace": [{"node": "triage", "summary": "new problem"}]}


def ask_analyst(state):
    # Nothing expensive before interrupt(): this node runs again from the start when the graph resumes.
    answer = interrupt({"incident_id": state["incident_id"], "questions": state["pending_questions"]})
    return {"description": state["description"] + "\n\nAnalyst answer: " + answer,
            "analyst_answers": [answer], "pending_questions": [],
            "trace": [{"node": "ask_analyst", "summary": "got the answer"}]}


def fake_diagnosis(state):
    result = DiagnosisResult(evidence_sufficient=False, gaps=["no similar incident"], next_step="report")
    return {"diagnosis": result, "errors": [{"node": "diagnosis", "error": "fake error, to test the reducer"}],
            "trace": [{"node": "diagnosis", "summary": "inconclusive"}]}


def after_triage(state):
    return "diagnosis" if state["triage_result"].enough_information else "ask_analyst"


g = StateGraph(InvestigationState)
g.add_node("triage", fake_triage)
g.add_node("ask_analyst", ask_analyst)
g.add_node("diagnosis", fake_diagnosis)
g.add_edge(START, "triage")
g.add_conditional_edges("triage", after_triage)
g.add_edge("ask_analyst", "triage")
g.add_edge("diagnosis", END)
graph = g.compile(checkpointer=InMemorySaver(serde=make_serializer()))
config = {"configurable": {"thread_id": "INC-TEST-1"}}

print("1st run: the graph pauses to ask the analyst")
first = graph.invoke({"incident_id": "INC-TEST-1", "description": "Something is broken!"}, config, version="v2")
checker.check("the run stopped at interrupt()", len(first.interrupts) == 1)
checker.check("the pause carries the questions",
              first.interrupts and first.interrupts[0].value["questions"] == ["Which service is failing?"])
saved = graph.get_state(config)
checker.check("the next node is ask_analyst", saved.next == ("ask_analyst",))
checker.check("triage_result comes back as a TriageResult", isinstance(saved.values["triage_result"], TriageResult))

print("\n2nd run: the analyst answers and the graph continues from the pause")
final = graph.invoke(Command(resume="The checkout page returns error 500."), config, version="v2").value
checker.check("the answer was added to the description", "checkout page returns error 500" in final["description"])
checker.check("analyst_answers has the answer", final["analyst_answers"] == ["The checkout page returns error 500."])
checker.check("triage ran again with the answer", final["symptoms"] == ["checkout returns 500"])
checker.check("diagnosis comes back as a DiagnosisResult", isinstance(final["diagnosis"], DiagnosisResult))
checker.check("trace accumulated every step (reducer)",
              [t["node"] for t in final["trace"]] == ["triage", "ask_analyst", "triage", "diagnosis"])
checker.check("errors accumulated instead of being replaced", len(final["errors"]) == 1)

checker.finish()
