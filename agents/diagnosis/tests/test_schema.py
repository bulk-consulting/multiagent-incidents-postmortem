"""Test: does the Diagnosis schema accept good answers and reject bad ones?
No model call, so it runs in a second.

Run from the repository root:
    python -m agents.diagnosis.tests.test_schema
"""
from agents.diagnosis.schema import DiagnosisResult, check_based_on, parse_diagnosis_answer
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

print("\nReading the model's text")
fenced = ('Here is my diagnosis:\n```json\n{"evidence_sufficient": false, "gaps": ["x"], '
          '"next_step": "report"}\n```')
checker.check("JSON inside a ```json fence", parse_diagnosis_answer(fenced).next_step == "report")
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

checker.finish()
