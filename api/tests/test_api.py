"""Test: the API with the real graph, but with fake agents (no model, no database, runs in seconds).

It checks that every way the graph can end becomes the same answer shape (a Report) in the API.

Run from the repository root:
    python -m api.tests.test_api
"""
from fastapi.testclient import TestClient

from agents.diagnosis.schema import DiagnosisResult, Hypothesis
from agents.orchestration import graph
from agents.triage.schema import RelatedIncident, TriageResult
from api.main import app

client = TestClient(app)
results = []


def check(name, ok):
    results.append(ok)
    print(("  PASS  " if ok else "  FAIL  ") + name)


# ---------------------------------------------------------------- fake agents

GOOD_TRIAGE = TriageResult(enough_information=True, symptoms=["uploads fail with 401"], affected_service="storage")
VAGUE_TRIAGE = TriageResult(enough_information=False, missing_information=["Qual serviço está falhando?"])
RELATED_TRIAGE = TriageResult(enough_information=True, symptoms=["uploads fail"], affected_service="storage",
                              related_incident=RelatedIncident(incident_id="INC-042", title="Uploads return 401"))

FINDING = {"incident_id": "DAN-015", "company": "Cloudflare", "title": "Cloudflare incident on March 21, 2025",
           "url": "https://blog.cloudflare.com/cloudflare-incident-march-21-2025/", "summary": "s",
           "deepened": True, "passages": []}

HYPOTHESIS = Hypothesis(cause="credentials deployed to the wrong environment", based_on=["DAN-015"], matches="m",
                        differs="d", same_trigger="yes", same_component="yes", same_mechanism="yes", confidence="high")
SUFFICIENT = DiagnosisResult(hypotheses=[HYPOTHESIS], evidence_sufficient=True, next_step="report")
ASK = DiagnosisResult(evidence_sufficient=False, gaps=["error code unknown"], next_step="ask_analyst",
                      questions_for_analyst=["Which error code do the calls return?"])


def use_fake_agents(triage, diagnosis=SUFFICIENT):
    """Replaces the 4 agents of the graph with fake ones that give fixed answers."""
    def fake_triage(description):
        if isinstance(triage, Exception):
            raise triage
        return triage

    graph.run_triage = fake_triage
    graph.run_research = lambda description, symptoms, request, previous: {"findings": [FINDING],
                                                                           "seen_ids": ["DAN-015"]}
    graph.run_diagnosis = lambda *args: diagnosis
    graph.run_reporting = graph.code_report_node  # the report built in code, instead of the LLM


def ask(message, history=None):
    response = client.post("/api/v1/incidents", json={"message": message, "history": history or []})
    return response.status_code, response.json()


def conversation(answers):
    """A chat history: the first description, then one question of the system and one answer per item."""
    history = [{"role": "user", "content": "The database returns no data for today."}]
    for answer in answers:
        history.append({"role": "assistant", "content": "To continue the investigation, I need some more information"})
        history.append({"role": "user", "content": answer})
    return history


# ---------------------------------------------------------------- the cases

print("1. Enough information: diagnosis")
use_fake_agents(GOOD_TRIAGE)
status, data = ask("Desde as 21h40 os uploads falham com 401 Unauthorized.")
check("200 and kind diagnosis", status == 200 and data["report"]["kind"] == "diagnosis")
check("the source is the post-mortem found",
      data["report"]["causes"][0]["sources"][0]["incident_id"] == "DAN-015")
check("there is a message for the chat", "DAN-015" in data["report"]["message"])

print("\n2. Vague message: the Triage agent asks")
use_fake_agents(VAGUE_TRIAGE)
status, data = ask("o upload está dando erro")
check("200 and kind questions", status == 200 and data["report"]["kind"] == "questions")
check("the message has the question", "Qual serviço está falhando?" in data["report"]["message"])
check("the intro is in Portuguese", "Para continuar" in data["report"]["message"])

print("\n3. The Diagnosis agent asks")
use_fake_agents(GOOD_TRIAGE, diagnosis=ASK)
status, data = ask("Uploads are failing with 401 since 21:40.")
check("200 and kind questions", status == 200 and data["report"]["kind"] == "questions")
check("the intro is in English", "To continue" in data["report"]["message"])

print("\n4. Already under investigation")
use_fake_agents(RELATED_TRIAGE)
status, data = ask("Os uploads estão falhando com erro 401 desde hoje.")
check("200 and kind related_incident", status == 200 and data["report"]["kind"] == "related_incident")
check("the message names the open investigation", "INC-042" in data["report"]["message"])

print("\n5. An agent fails")
use_fake_agents(RuntimeError("NIM is down"))
status, data = ask("Uploads are failing with 401 since 21:40.")
check("200 and kind inconclusive (the flow does not break)",
      status == 200 and data["report"]["kind"] == "inconclusive")
check("the message says what failed", "failed" in data["report"]["message"])

print("\n6. The limit of questions (3 answers from the analyst)")
use_fake_agents(GOOD_TRIAGE, diagnosis=ASK)
status, data = ask("Only for today.", conversation(["A dbt migration."]))
check("2 answers: the Diagnosis agent can still ask", data["report"]["kind"] == "questions")
status, data = ask("Postgres.", conversation(["A dbt migration.", "Only for today."]))
check("3 answers: no more questions, inconclusive report",
      status == 200 and data["report"]["kind"] == "inconclusive")
use_fake_agents(VAGUE_TRIAGE)
status, data = ask("I don't know.", conversation(["No idea.", "Not sure."]))
check("the limit also stops the Triage agent's questions", data["report"]["kind"] == "inconclusive")

print("\n7. Invalid input")
status, _ = ask("")
check("empty message: 422", status == 422)

print(f"\n{sum(results)} of {len(results)} checks passed")
