"""Test: does the "Decision in code" box choose the right next step?
No model call, so it runs in a second.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_routing
"""
from agents.triage.routing import ASK_USER, GO_TO_RESEARCH, TELL_RELATED_INCIDENT, next_step
from agents.triage.schema import RelatedIncident, TriageResult
from agents.triage.tests.checks import Checker

checker = Checker()

not_enough = TriageResult(enough_information=False, missing_information=["Which service fails?"])
checker.check("not enough information -> ask the user", next_step(not_enough) == ASK_USER)

similar_exists = TriageResult(
    enough_information=True,
    related_incident=RelatedIncident(incident_id="INC-042", title="Checkout returns HTTP 500"),
)
checker.check(
    "similar investigation exists -> tell the user",
    next_step(similar_exists) == TELL_RELATED_INCIDENT,
)

new_problem = TriageResult(enough_information=True, symptoms=["slow search"])
checker.check("new problem -> go to research", next_step(new_problem) == GO_TO_RESEARCH)

checker.finish()
