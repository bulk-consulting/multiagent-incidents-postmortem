"""Test: the answer for a problem that is already under investigation (no model, runs in a second).

Run from the repository root:
    python -m agents.reporting.tests.test_related
"""
from agents.reporting.related import analyst_language, related_incident_node
from agents.reporting.tests.checks import Checker
from agents.triage.schema import RelatedIncident, TriageResult

checker = Checker()
triage = TriageResult(enough_information=True, symptoms=["login page returns error 500"], affected_service="login",
                      related_incident=RelatedIncident(incident_id="INC-042", title="Login page returns HTTP 500"))

print("The language of the analyst")
checker.check("English message", analyst_language("The login page returns 500 for all users.") == "en")
checker.check("Portuguese message", analyst_language("A página de login não abre, está dando erro 500.") == "pt")

print("\nThe report")
out = related_incident_node({"incident_id": "INC-100", "description": "The login page returns 500.",
                             "triage_result": triage})["report"]
checker.check("kind related_incident, with the open investigation",
              out["kind"] == "related_incident" and out["related_incident"]["incident_id"] == "INC-042")
checker.check("the message names the investigation, the service and the symptoms",
              all(x in out["message"] for x in ("INC-042", "login", "login page returns error 500")))
checker.check("the message says what to do if it is another problem", "not the same problem" in out["message"])
checker.check("the incident id of this investigation", out["incident_id"] == "INC-100")

out = related_incident_node({"incident_id": "INC-101", "description": "A página de login não abre, está dando erro 500.",
                             "triage_result": triage})["report"]
checker.check("in Portuguese when the analyst writes in Portuguese",
              "Já em investigação" in out["message"] and "Acompanhe" in out["message"])

out = related_incident_node({"triage_result": triage.model_dump()})["report"]
checker.check("the Triage result can also be a dict", out["related_incident"]["incident_id"] == "INC-042")

checker.finish()
