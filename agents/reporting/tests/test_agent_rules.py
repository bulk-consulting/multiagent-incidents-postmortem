"""Test: does the agent's loop work when the model behaves badly?

We replace the model by a fake one that gives the answers we choose, so there is no model call
and it runs in a second. What we check:
  - a good answer is accepted at the first attempt
  - a bad answer is sent back with the problems, and the second answer is accepted
  - an answer inside a ```json fence is read
  - an empty answer is a problem, not a crash
  - the code fills in the incident_id, whatever the model writes
  - if the model never gives a valid report, the code builds a simple inconclusive one

Run from the repository root:
    .venv/Scripts/python.exe -m agents.reporting.tests.test_agent_rules
"""
import json

import agents.reporting.agent as agent
from agents.reporting.tests.checks import Checker
from agents.reporting.tests.fixtures import good_report_for, load_fixture

state = load_fixture("gitlab_diagnosis_en")
GOOD = good_report_for(state).model_dump_json()

# A bad report: it cites an incident that is not in the findings.
bad = json.loads(GOOD)
bad["causes"][0]["sources"] = [{"post_mortem_id": "DAN-999", "title": "Made up", "url": "https://made.up"}]
BAD = json.dumps(bad)


def run_with_answers(answers):
    """Run the agent with a fake model that gives these answers, one per call. Returns the result and the calls."""
    calls = []

    def fake_chat(messages, **kwargs):
        calls.append(len(messages))
        return {"role": "assistant", "content": answers[min(len(calls), len(answers)) - 1]}

    agent.chat = fake_chat
    report, messages, attempts, problems = agent.run_reporting_agent(state)
    return report, messages, attempts, problems, calls


checker = Checker()

report, messages, attempts, problems, calls = run_with_answers([GOOD])
checker.check("a good answer is accepted at the first attempt", attempts == 1 and problems == [] and report.kind == "diagnosis")
checker.check("the code fills in the incident_id", report.incident_id == state["incident_id"], f"(got {report.incident_id!r})")

report, messages, attempts, problems, calls = run_with_answers([BAD, GOOD])
checker.check("a bad answer is corrected at the second attempt", attempts == 2 and problems == [])
checker.check("the model is told the problem", "DAN-999" in messages[-2]["content"], f"(got {messages[-2]['content'][:80]!r})")

report, messages, attempts, problems, calls = run_with_answers(["Here you go:\n```json\n" + GOOD + "\n```"])
checker.check("an answer inside a ```json fence is read", attempts == 1 and report.kind == "diagnosis")

report, messages, attempts, problems, calls = run_with_answers(["", GOOD])
checker.check("an empty answer is a problem, and the next attempt works", attempts == 2 and problems == [])

# The model writes its own incident_id: the code must replace it.
other_id = json.loads(GOOD)
other_id["incident_id"] = "INV-9999"
report, messages, attempts, problems, calls = run_with_answers([json.dumps(other_id)])
checker.check("the incident_id written by the model is replaced", report.incident_id == state["incident_id"])

# The model never gives a valid report.
report, messages, attempts, problems, calls = run_with_answers([BAD])
checker.check("after the last attempt, the code builds the fallback report", attempts == agent.MAX_ATTEMPTS and len(calls) == agent.MAX_ATTEMPTS)
checker.check("the fallback is an inconclusive report", report.kind == "inconclusive" and report.gaps != [])
checker.check("the fallback keeps the incident_id", report.incident_id == state["incident_id"])
checker.check("the fallback shows the links of the findings", all(f["url"] in report.message for f in state["findings"][:3]))
checker.check("the problems that were left are returned", problems != [] and any("DAN-999" in p for p in problems))

checker.finish()
