"""Test: the rule that stops the model from inventing a related incident.
No model call, so it runs in a second.

We build a fake messages history (as if the tool had already answered) and check that
check_related_incident accepts only open investigations that the tool really returned.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_agent_rules
"""
import json

from agents.triage.agent import check_related_incident, check_tool_was_used
from agents.triage.schema import RelatedIncident, TriageResult
from agents.triage.tests.checks import Checker
from agents.triage.tools import list_investigations

checker = Checker()

# A messages history in which the tool already returned all investigations.
messages = [
    {"role": "user", "content": "The login page returns 500."},
    {"role": "tool", "tool_call_id": "1", "content": json.dumps(list_investigations())},
]


def result_related_to(incident_id):
    return TriageResult(
        enough_information=True,
        related_incident=RelatedIncident(incident_id=incident_id, title="any title"),
    )


def is_rejected(result, messages):
    try:
        check_related_incident(result, messages)
        return False
    except ValueError:
        return True


checker.check("an open investigation is accepted", not is_rejected(result_related_to("INC-042"), messages))
checker.check("a closed investigation is rejected", is_rejected(result_related_to("INC-043"), messages))
checker.check("an invented id is rejected", is_rejected(result_related_to("INC-999"), messages))
checker.check(
    "no related incident is always fine",
    not is_rejected(TriageResult(enough_information=True), messages),
)
checker.check(
    "a related incident without ever calling the tool is rejected",
    is_rejected(result_related_to("INC-042"), messages[:1]),
)

print("\nThe tool must be used when there is enough information")


def tool_check_rejects(result, messages):
    try:
        check_tool_was_used(result, messages)
        return False
    except ValueError:
        return True


enough = TriageResult(enough_information=True)
not_enough = TriageResult(enough_information=False, missing_information=["Which service fails?"])
checker.check("enough information and the tool was used: accepted", not tool_check_rejects(enough, messages))
checker.check("enough information but the tool was not used: rejected", tool_check_rejects(enough, messages[:1]))
checker.check("not enough information: the tool is not needed", not tool_check_rejects(not_enough, messages[:1]))

checker.finish()
