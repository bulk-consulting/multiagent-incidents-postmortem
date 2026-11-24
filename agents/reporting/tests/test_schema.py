"""Test: does Pydantic accept good reports and reject bad ones?

No model call, it runs in a second.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.reporting.tests.test_schema
"""
from agents.reporting.schema import Report, parse_report_answer
from agents.reporting.tests.checks import Checker


def is_accepted(data):
    """True if Pydantic accepts this data."""
    try:
        Report.model_validate(data)
    except ValueError:
        return False
    return True


SOURCE = {"incident_id": "DAN-164", "title": "Postmortem of database outage", "url": "https://example.com/dan-164"}
CAUSE = {
    "root_cause": "An admin deleted the wrong directory and the backups were not working.",
    "remediation_steps": ["Restore from the staging database copy."],
    "prevention_checklist": ["Test the backups every week."],
    "sources": [SOURCE],
    "confidence": "high",
}
DIAGNOSIS = {"kind": "diagnosis", "summary": "Most likely a deletion on the wrong host.",
             "message": "## Probable cause\nA deletion on the wrong host.", "causes": [CAUSE]}
INCONCLUSIVE = {"kind": "inconclusive", "summary": "We could not find a clear cause.",
                "message": "We could not find a clear cause yet.", "gaps": ["No logs."]}

checker = Checker()

checker.check("a good diagnosis is accepted", is_accepted(DIAGNOSIS))
checker.check("a good inconclusive report is accepted", is_accepted(INCONCLUSIVE))
checker.check("incident_id is optional (the code fills it in)", Report.model_validate(DIAGNOSIS).incident_id == "")

checker.check("a diagnosis without causes is rejected", not is_accepted({**DIAGNOSIS, "causes": []}))
checker.check("an inconclusive report without gaps is rejected", not is_accepted({**INCONCLUSIVE, "gaps": []}))
checker.check("a cause without sources is rejected", not is_accepted({**DIAGNOSIS, "causes": [{**CAUSE, "sources": []}]}))
checker.check("an unknown confidence is rejected",
              not is_accepted({**DIAGNOSIS, "causes": [{**CAUSE, "confidence": "very high"}]}))
checker.check("an unknown kind is rejected", not is_accepted({**DIAGNOSIS, "kind": "maybe"}))
checker.check("an empty summary is rejected", not is_accepted({**DIAGNOSIS, "summary": ""}))
checker.check("an empty message is rejected", not is_accepted({**DIAGNOSIS, "message": ""}))
checker.check("a report without a message is rejected", not is_accepted({k: v for k, v in DIAGNOSIS.items() if k != "message"}))

# The honest case: the post-mortem does not say how it was fixed. Empty lists must be allowed.
no_fix = {**DIAGNOSIS, "causes": [{**CAUSE, "remediation_steps": [], "prevention_checklist": []}]}
checker.check("a cause may have no remediation steps (the text does not say)", is_accepted(no_fix))

# The model's text, as it really arrives.
checker.check("the answer is read from text with a ```json fence",
              parse_report_answer('Here it is:\n```json\n{"kind":"inconclusive","summary":"x","message":"x","gaps":["y"]}\n```').kind == "inconclusive")
try:
    parse_report_answer("I could not write the report.")
    rejected_text = False
except ValueError:
    rejected_text = True
checker.check("text with no JSON is rejected", rejected_text)

checker.finish()
