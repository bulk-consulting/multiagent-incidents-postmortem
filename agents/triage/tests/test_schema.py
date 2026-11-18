"""Test: does the Pydantic schema accept good answers and reject bad ones?
No model call, so it runs in a second.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_schema
"""
from agents.triage.schema import TriageResult, parse_triage_answer
from agents.triage.tests.checks import Checker

checker = Checker()


def is_rejected(data):
    """True if Pydantic refuses this data."""
    try:
        TriageResult(**data)
        return False
    except ValueError:  # Pydantic's ValidationError is a kind of ValueError
        return True


print("Good answers are accepted")
complete = {
    "symptoms": ["checkout returns 500"],
    "affected_service": "checkout",
    "category": "Config Errors",
    "enough_information": True,
    "related_incident": {"incident_id": "INC-042", "title": "Checkout returns HTTP 500"},
}
checker.check("complete answer", not is_rejected(complete))

minimal = {"enough_information": True}
checker.check("only the required field (the rest has defaults)", not is_rejected(minimal))

vague = {"enough_information": False, "missing_information": ["Which service is failing?"]}
checker.check("not enough information, with questions", not is_rejected(vague))

print("\nBad answers are rejected")
checker.check("category not in the list", is_rejected({**complete, "category": "Network"}))
checker.check("missing the required field", is_rejected({"symptoms": ["slow"]}))
checker.check(
    "not enough information but no questions",
    is_rejected({"enough_information": False}),
)
checker.check(
    "not enough information but a related incident",
    is_rejected({**vague, "related_incident": {"incident_id": "INC-042", "title": "x"}}),
)

print("\nReading the model's text")
fenced = 'Here is the result:\n```json\n{"enough_information": true, "symptoms": ["slow"]}\n```'
checker.check("JSON inside a ```json fence", parse_triage_answer(fenced).symptoms == ["slow"])

try:
    parse_triage_answer("I think this is a new incident.")
    no_json_rejected = False
except ValueError:
    no_json_rejected = True
checker.check("text without JSON is rejected", no_json_rejected)

checker.finish()
