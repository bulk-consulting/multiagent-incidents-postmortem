"""Test: does the Diagnosis schema accept good answers and reject bad ones?
No model call, so it runs in a second.

Run from the repository root:
    python -m agents.diagnosis.tests.test_schema
"""
from agents.diagnosis.schema import DiagnosisDraft, DiagnosisResult, check_based_on, decide, parse_diagnosis_answer
from agents.triage.tests.checks import Checker

checker = Checker()


def is_rejected(data):
    """True if Pydantic refuses this data."""
    try:
        DiagnosisResult(**data)
        return False
    except ValueError:  # Pydantic's ValidationError is a kind of ValueError
        return True


hypothesis = {
    "cause": "The cloud provider changed its API without notice.",
    "based_on": ["DAN-197"],
    "matches": "Calls to the provider's API started failing with no change on our side.",
    "differs": "Metrist used Azure CosmosDB; the current service may use another API.",
    "same_trigger": "yes",
    "same_component": "yes",
    "confidence": "high",
}
sufficient = {"hypotheses": [hypothesis], "evidence_sufficient": True, "next_step": "report"}
refine = {"hypotheses": [], "evidence_sufficient": False, "gaps": ["no similar incident"],
          "next_step": "refine_search", "search_request": "third-party API breaking change"}
ask = {"evidence_sufficient": False, "next_step": "ask_analyst",
       "questions_for_analyst": ["Which error code do the calls return?"]}

print("Good answers are accepted")
checker.check("enough evidence, with a hypothesis", not is_rejected(sufficient))
checker.check("not enough evidence, asks for a new search", not is_rejected(refine))
checker.check("not enough evidence, asks the analyst", not is_rejected(ask))
checker.check("not enough evidence, gives up (inconclusive report)",
              not is_rejected({"evidence_sufficient": False, "gaps": ["nothing fits"], "next_step": "report"}))

print("\nBad answers are rejected")
checker.check("enough evidence but no hypothesis", is_rejected({**sufficient, "hypotheses": []}))
checker.check("enough evidence but asks for a new search",
              is_rejected({**sufficient, "next_step": "refine_search", "search_request": "x"}))
checker.check("new search without saying what to look for", is_rejected({**refine, "search_request": " "}))
checker.check("asks the analyst without questions", is_rejected({**ask, "questions_for_analyst": []}))
checker.check("more than 3 hypotheses", is_rejected({**sufficient, "hypotheses": [hypothesis] * 4}))
checker.check("hypothesis not based on any incident",
              is_rejected({**sufficient, "hypotheses": [{**hypothesis, "based_on": []}]}))
checker.check("confidence as a number", is_rejected({**sufficient, "hypotheses": [{**hypothesis, "confidence": 0.9}]}))
checker.check("next step not in the list", is_rejected({**sufficient, "next_step": "escalate"}))
checker.check("comparison not in the list",
              is_rejected({**sufficient, "hypotheses": [{**hypothesis, "same_trigger": "maybe"}]}))

print("\nReading the model's text")
fenced = 'Here is my diagnosis:\n```json\n{"hypotheses": [], "gaps": ["x"], "search_request": "y"}\n```'
checker.check("JSON inside a ```json fence", parse_diagnosis_answer(fenced).gaps == ["x"])
try:
    parse_diagnosis_answer("The cause is probably the provider.")
    no_json_rejected = False
except ValueError:
    no_json_rejected = True
checker.check("text without JSON is rejected", no_json_rejected)

print("\nThe hypotheses use only incidents from the findings")
result = DiagnosisResult(**sufficient)
try:
    check_based_on(result, ["DAN-197", "DAN-184"])
    known_ok = True
except ValueError:
    known_ok = False
checker.check("incident in the findings is accepted", known_ok)
try:
    check_based_on(result, ["DAN-184"])
    invented_rejected = False
except ValueError:
    invented_rejected = True
checker.check("incident not in the findings is rejected", invented_rejected)

print("\nCode decides the confidence limit, whether the evidence is enough and the next step")


def draft(*hyps, search="api breaking change", questions=()):
    return DiagnosisDraft(hypotheses=[{**hypothesis, **h} for h in hyps], gaps=["g"], search_request=search,
                          questions_for_analyst=list(questions))


r = decide(draft({}), ["DAN-197"])
checker.check("same trigger and component, deepened: high is kept and the evidence is enough",
              r.hypotheses[0].confidence == "high" and r.evidence_sufficient and r.next_step == "report")
r = decide(draft({"same_component": "no"}), ["DAN-197"])
checker.check("different component: high becomes medium", r.hypotheses[0].confidence == "medium")
checker.check("different component: the evidence is not enough, new search", not r.evidence_sufficient
              and r.next_step == "refine_search" and r.search_request == "api breaking change")
r = decide(draft({"same_component": "no", "same_trigger": "no"}), ["DAN-197"])
checker.check("trigger and component differ: low", r.hypotheses[0].confidence == "low")
r = decide(draft({"same_trigger": "unknown", "confidence": "medium"}), ["DAN-197"])
checker.check("trigger unknown, same component, medium: the evidence is enough",
              r.evidence_sufficient and r.next_step == "report")
r = decide(draft({}), [])
checker.check("based on an incident without passages: the evidence is not enough", not r.evidence_sufficient)
r = decide(draft({"confidence": "low"}), ["DAN-197"])
checker.check("only a low hypothesis: the evidence is not enough", not r.evidence_sufficient)
r = decide(draft({"same_component": "no"}, questions=["Which error?"]), ["DAN-197"], research_round=3)
checker.check("last round, not enough, with questions: ask the analyst",
              r.next_step == "ask_analyst" and r.questions_for_analyst == ["Which error?"] and not r.search_request)
r = decide(draft({"same_component": "no"}), ["DAN-197"], research_round=3)
checker.check("last round, not enough, no questions: inconclusive report",
              r.next_step == "report" and not r.evidence_sufficient)
r = decide(draft({"same_component": "no"}, search="", questions=["Which error?"]), ["DAN-197"])
checker.check("no search request: ask the analyst instead", r.next_step == "ask_analyst")
r = decide(draft({}, questions=["Which error?"]), ["DAN-197"])
checker.check("enough evidence: the questions are dropped", r.next_step == "report" and not r.questions_for_analyst)

checker.finish()
