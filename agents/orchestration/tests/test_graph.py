"""Integration test of the main graph with fake agents (no model, no database): it runs in a few seconds.

The fakes replace graph.run_triage, graph.run_research and graph.run_diagnosis. The checkpointer is an InMemorySaver
with the same serializer as the demo (state.make_serializer) and LANGGRAPH_STRICT_MSGPACK on, so a Pydantic class
missing from STATE_CLASSES would break the test.

Scenarios (docs/E5_Orchestrated_Multi_Agent_System/E5_Estado_e_Formatos.md, section 10):
    1. new problem with a similar case → diagnosis report with valid sources
    2. vague message → pause with questions; resume with the answer → report
    3. duplicate → related incident, the Research agent is not called
    4. out of the corpus → refinement up to the limit → inconclusive report
    5. refinement that improves the evidence → diagnosis in the 2nd round
    6. resume in another run (same checkpointer, new graph object)
    7. an agent fails → inconclusive report, the flow does not break
    8. report with an invented link → the validation rejects it and the report is fixed (with the optional
       validation node; Mari's Reporting agent does the same inside itself: agents/reporting/tests/test_validation.py)
    plus: the Diagnosis agent asks the analyst (the investigation starts again) and the limit of answers.

Run from the repository root:
    multiagent_env/bin/python -m agents.orchestration.tests.test_graph
"""
import os

os.environ["LANGGRAPH_STRICT_MSGPACK"] = "true"

from langgraph.checkpoint.memory import InMemorySaver  # noqa: E402
from langgraph.types import Command  # noqa: E402

import agents.orchestration.graph as graph  # noqa: E402
from agents.diagnosis.schema import DiagnosisResult, Hypothesis  # noqa: E402
from agents.orchestration.state import MAX_REPORT_FIXES, MAX_RESEARCH_ROUNDS, make_serializer  # noqa: E402
from agents.triage.schema import RelatedIncident, TriageResult  # noqa: E402
from agents.triage.tests.checks import Checker  # noqa: E402

checker = Checker()

GOOD_TRIAGE = TriageResult(enough_information=True, symptoms=["reads fail"], affected_service="object store")
VAGUE_TRIAGE = TriageResult(enough_information=False, missing_information=["Which service fails?"])
RELATED_TRIAGE = TriageResult(enough_information=True, symptoms=["login 500"], affected_service="login",
                              related_incident=RelatedIncident(incident_id="INC-042", title="Login returns 500"))


def finding(i, deepened=True):
    return {"post_mortem_id": i, "company": "Acme", "title": f"title {i}", "url": f"https://example.com/{i}", "summary": "s",
            "deepened": deepened, "passages": [{"section": "Root cause", "content": "c", "query_source": "cause"}]}


def hypothesis(i, confidence="high"):
    return Hypothesis(cause=f"cause from {i}", based_on=[i], matches="m", differs="d", same_trigger="yes",
                      same_component="yes", same_mechanism="yes", confidence=confidence)


SUFFICIENT = lambda i: DiagnosisResult(hypotheses=[hypothesis(i)], evidence_sufficient=True, next_step="report")  # noqa: E731
REFINE = DiagnosisResult(hypotheses=[hypothesis("DAN-001", "low")], evidence_sufficient=False,
                         gaps=["nothing fits"], next_step="refine_search", search_request="other kind of incident")
INCONCLUSIVE = DiagnosisResult(evidence_sufficient=False, gaps=["nothing fits"], next_step="report")
ASK = DiagnosisResult(evidence_sufficient=False, gaps=["error code unknown"], next_step="ask_analyst",
                      questions_for_analyst=["Which error code do the calls return?"])


class Fakes:
    """Scripted agents. Each call is recorded, to check what the graph passed to them."""

    def __init__(self, triage=None, research=None, diagnosis=None):
        self.triage, self.research, self.diagnosis = triage or [], research or [], diagnosis or []
        self.calls = {"triage": [], "research": [], "diagnosis": []}
        graph.run_triage, graph.run_research, graph.run_diagnosis = self.run_triage, self.run_research, self.run_diagnosis
        graph.run_reporting = graph.code_report_node  # the report built in code, instead of the LLM

    @staticmethod
    def _next(items, k):
        item = items[min(k, len(items) - 1)]
        if isinstance(item, Exception):
            raise item
        return item

    def run_triage(self, description):
        self.calls["triage"].append(description)
        return self._next(self.triage, len(self.calls["triage"]) - 1)

    def run_research(self, description, symptoms, request, previous):
        self.calls["research"].append({"description": description, "request": request, "previous": previous})
        findings = self._next(self.research, len(self.calls["research"]) - 1)
        seen = sorted({r["post_mortem_id"] for r in findings} | set((previous or {}).get("seen_ids", [])))
        return {"findings": findings, "seen_ids": seen}

    def run_diagnosis(self, description, triage, findings, research_round, max_rounds, previous_requests):
        self.calls["diagnosis"].append({"round": research_round, "ids": [r["post_mortem_id"] for r in findings],
                                        "previous": previous_requests, "triage": triage})
        return self._next(self.diagnosis, len(self.calls["diagnosis"]) - 1)


def new_graph(checkpointer=None, **kw):
    return graph.build_graph(checkpointer or InMemorySaver(serde=make_serializer()), **kw)


def run(g, incident_id, description):
    config = {"configurable": {"thread_id": incident_id}}
    return g.invoke({"incident_id": incident_id, "description": description}, config), config


print("1. New problem with a similar case")
f = Fakes([GOOD_TRIAGE], [[finding("DAN-104"), finding("DAN-189", False)]], [SUFFICIENT("DAN-104")])
out, _ = run(new_graph(), "INC-1", "Our object store is down.")
report = out["report"]
checker.check("ends with a diagnosis report", report["kind"] == "diagnosis")
checker.check("the source has the url of the findings",
              report["causes"][0]["sources"][0]["url"] == "https://example.com/DAN-104")
checker.check("one round of each agent", [len(f.calls[k]) for k in ("triage", "research", "diagnosis")] == [1, 1, 1])
checker.check("the validation found no problem", out["report_problems"] == [])
checker.check("the trace has every node in order",
              [t["node"] for t in out["trace"]] == ["triage", "research", "diagnosis", "report"])

print("\n2. Vague message: pause and resume")
f = Fakes([VAGUE_TRIAGE, GOOD_TRIAGE], [[finding("DAN-104")]], [SUFFICIENT("DAN-104")])
g = new_graph()
out, config = run(g, "INC-2", "Something is broken.")
paused = out.get("__interrupt__")
checker.check("the graph pauses with the Triage questions",
              bool(paused) and paused[0].value["questions"] == ["Which service fails?"])
checker.check("nothing was searched yet", f.calls["research"] == [])
out = g.invoke(Command(resume="The object store."), config)
checker.check("after the answer, the Triage agent reads the description with the answer",
              f.calls["triage"][-1] == "Something is broken.\n\nAnalyst answer: The object store.")
checker.check("the investigation goes on to the report", out["report"]["kind"] == "diagnosis")
checker.check("the answer is kept", out["analyst_answers"] == ["The object store."])

print("\n3. Duplicate: related incident")
f = Fakes([RELATED_TRIAGE])
out, _ = run(new_graph(), "INC-3", "Login returns 500.")
checker.check("answers with the related incident", out["report"]["kind"] == "related_incident"
              and out["report"]["related_incident"]["incident_id"] == "INC-042")
checker.check("the Research agent is not called", f.calls["research"] == [])
checker.check("the answer has a message for the chat (Mari's node)", "INC-042" in out["report"]["message"])

print("\n4. Out of the corpus: refinement up to the limit")
f = Fakes([GOOD_TRIAGE], [[finding("DAN-001")], [finding("DAN-002")], [finding("DAN-003")]],
          [REFINE, REFINE, INCONCLUSIVE])
out, _ = run(new_graph(), "INC-4", "Something new.")
checker.check(f"the Research agent runs {MAX_RESEARCH_ROUNDS} times", len(f.calls["research"]) == MAX_RESEARCH_ROUNDS)
checker.check("the refinement passes the request and the earlier findings",
              f.calls["research"][1]["request"] == "other kind of incident"
              and [r["post_mortem_id"] for r in f.calls["research"][1]["previous"]["findings"]] == ["DAN-001"])
checker.check("the 1st round is not a refinement", f.calls["research"][0]["previous"] is None
              and f.calls["research"][0]["request"] == "")
checker.check("the Diagnosis agent knows the round", [c["round"] for c in f.calls["diagnosis"]] == [1, 2, 3])
checker.check("from the 2nd round, it knows the request already made",
              f.calls["diagnosis"][0]["previous"] == [] and f.calls["diagnosis"][1]["previous"] == ["other kind of incident"])
checker.check("ends with an inconclusive report", out["report"]["kind"] == "inconclusive" and out["report"]["gaps"])

f = Fakes([GOOD_TRIAGE], [[finding("DAN-001")]], [REFINE])  # a Diagnosis agent that always asks to refine
out, _ = run(new_graph(), "INC-4b", "Something new.")
checker.check("even if the Diagnosis agent keeps asking, the loop stops at the limit",
              len(f.calls["research"]) == MAX_RESEARCH_ROUNDS and out["report"]["kind"] == "inconclusive")

TRIGGERS_TRIAGE = TriageResult(enough_information=True, symptoms=["console fails"], affected_service="console",
                               triggers=["a console update", "an account backend revision"])
f = Fakes([TRIGGERS_TRIAGE], [[finding("DAN-018")]], [SUFFICIENT("DAN-018")])
run(new_graph(), "INC-4c", "The console fails.")
checker.check("the Diagnosis agent receives all the changes the analyst mentioned",
              f.calls["diagnosis"][0]["triage"]["triggers"] == ["a console update", "an account backend revision"])

print("\n5. The refinement improves the evidence")
f = Fakes([GOOD_TRIAGE], [[finding("DAN-001")], [finding("DAN-104"), finding("DAN-001")]],
          [REFINE, SUFFICIENT("DAN-104")])
out, _ = run(new_graph(), "INC-5", "Our object store is down.")
checker.check("diagnosis in the 2nd round", len(f.calls["research"]) == 2 and out["report"]["kind"] == "diagnosis"
              and out["report"]["causes"][0]["sources"][0]["post_mortem_id"] == "DAN-104")

print("\n6. Resume in another run (same checkpointer, new graph)")
saver = InMemorySaver(serde=make_serializer())
f = Fakes([VAGUE_TRIAGE, GOOD_TRIAGE], [[finding("DAN-104")]], [SUFFICIENT("DAN-104")])
out, config = run(new_graph(saver), "INC-6", "Something is broken.")
checker.check("paused in the first run", bool(out.get("__interrupt__")))
out = new_graph(saver).invoke(Command(resume="The object store."), config)
checker.check("a new graph object resumes from the saved state", out["report"]["kind"] == "diagnosis"
              and isinstance(out["triage_result"], TriageResult))

print("\n7. An agent fails: inconclusive report")
for name, scripts in [("Triage", ([RuntimeError("model down")],)),
                      ("Research", ([GOOD_TRIAGE], [RuntimeError("503")])),
                      ("Diagnosis", ([GOOD_TRIAGE], [[finding("DAN-104")]], [RuntimeError("invalid answers")]))]:
    Fakes(*scripts)
    out, _ = run(new_graph(), f"INC-7-{name}", "Our object store is down.")
    checker.check(f"{name} fails → inconclusive report with the error",
                  out["report"]["kind"] == "inconclusive" and out["errors"][0]["node"] == name.lower()
                  and any("failed" in gap for gap in out["report"]["gaps"]))
f = Fakes([GOOD_TRIAGE], [[finding("DAN-001")], RuntimeError("503"), [finding("DAN-003")]],
          [REFINE, REFINE, INCONCLUSIVE])
out, _ = run(new_graph(), "INC-7b", "Something new.")
checker.check("a failed refinement keeps the earlier findings and the loop goes on",
              f.calls["diagnosis"][1]["ids"] == ["DAN-001"] and out["report"]["kind"] == "inconclusive")

print("\n8. Report with an invented link: the validation rejects it")
calls = []


def report_with_bad_link_once(state):
    calls.append(state.get("report_problems", []))
    url = "https://invented.example" if len(calls) == 1 else "https://example.com/DAN-104"
    return {"report": {"kind": "diagnosis", "summary": "s", "gaps": [], "suggested_checks": [],
                       "causes": [{"root_cause": "c", "confidence": "high",
                                   "sources": [{"post_mortem_id": "DAN-104", "title": "t", "url": url}]}]}}


f = Fakes([GOOD_TRIAGE], [[finding("DAN-104")]], [SUFFICIENT("DAN-104")])
out, _ = run(new_graph(report=report_with_bad_link_once, validate_report=graph.validate_report_node), "INC-8",
             "Our object store is down.")
checker.check("the report is written again with the problems", len(calls) == 2 and "url" in calls[1][0])
checker.check("the fixed report passes", out["report_problems"] == [])

calls.clear()


def always_bad(state):
    calls.append(1)
    return {"report": {"kind": "diagnosis", "causes": []}}


f = Fakes([GOOD_TRIAGE], [[finding("DAN-104")]], [SUFFICIENT("DAN-104")])
out, _ = run(new_graph(report=always_bad, validate_report=graph.validate_report_node), "INC-8b",
             "Our object store is down.")
checker.check(f"a report that never passes stops after {MAX_REPORT_FIXES} fixes", len(calls) == MAX_REPORT_FIXES + 1)

print("\nThe Diagnosis agent asks the analyst")
f = Fakes([GOOD_TRIAGE], [[finding("DAN-001")], [finding("DAN-104")]], [ASK, SUFFICIENT("DAN-104")])
g = new_graph()
out, config = run(g, "INC-9", "Calls to the provider fail.")
checker.check("pauses with the Diagnosis questions",
              out["__interrupt__"][0].value["questions"] == ["Which error code do the calls return?"])
out = g.invoke(Command(resume="InvalidParameter on create container."), config)
checker.check("the investigation starts again: Triage reads the answer, fresh search",
              len(f.calls["triage"]) == 2 and f.calls["research"][1]["previous"] is None
              and "InvalidParameter" in f.calls["research"][1]["description"])
checker.check("the rounds start again", f.calls["diagnosis"][1]["round"] == 1)
checker.check("ends with the diagnosis", out["report"]["kind"] == "diagnosis")

f = Fakes([VAGUE_TRIAGE])  # an analyst whose answers never help
g = new_graph()
out, config = run(g, "INC-10", "Something is broken.")
for k in range(graph.MAX_ANALYST_ROUNDS):
    out = g.invoke(Command(resume=f"answer {k}"), config)
checker.check(f"after {graph.MAX_ANALYST_ROUNDS} answers, an inconclusive report instead of another question",
              "__interrupt__" not in out and out["report"]["kind"] == "inconclusive")

print("\nMari's Reporting agent inside the graph (fake model)")
import json  # noqa: E402

import agents.reporting.agent as reporting_agent  # noqa: E402
from agents.reporting.node import reporting_node  # noqa: E402
from agents.reporting.schema import Report  # noqa: E402

model_calls = []
VALID_REPORT = json.dumps({
    "kind": "diagnosis", "summary": "Too much capacity was removed.",
    "message": "Most likely cause: too much capacity removed. Source: https://example.com/DAN-104",
    "causes": [{"root_cause": "cause from DAN-104", "remediation_steps": [], "prevention_checklist": [],
                "sources": [{"post_mortem_id": "DAN-104", "title": "title DAN-104", "url": "https://example.com/DAN-104"}],
                "confidence": "high"}],
    "gaps": [], "suggested_checks": []})


def fake_model(messages, max_tokens=None, **kw):
    model_calls.append(messages)
    return {"content": VALID_REPORT}


reporting_agent.chat = fake_model
f = Fakes([GOOD_TRIAGE], [[finding("DAN-104")]], [SUFFICIENT("DAN-104")])
graph.run_reporting = reporting_node  # the real node, with the fake model
g = new_graph()
out, config = run(g, "INC-11", "Our object store is down.")
checker.check("the Reporting agent writes a Report (Pydantic) with the incident id",
              isinstance(out["report"], Report) and out["report"].kind == "diagnosis"
              and out["report"].incident_id == "INC-11")
checker.check("its own validation passed at the first attempt",
              out["report_attempts"] == 1 and out["report_problems"] == [] and len(model_calls) == 1)
checker.check("the Report survives the checkpoint (strict mode)",
              isinstance(g.get_state(config).values["report"], Report))

model_calls.clear()
f = Fakes([GOOD_TRIAGE], [[finding("DAN-104")]], [RuntimeError("invalid answers")])
graph.run_reporting = reporting_node
out, _ = run(new_graph(), "INC-12", "Our object store is down.")
checker.check("no diagnosis (the agent failed): inconclusive report in code, the model is not called",
              out["report"]["kind"] == "inconclusive" and model_calls == [])

checker.finish()
