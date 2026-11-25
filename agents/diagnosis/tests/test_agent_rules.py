"""Test: does the Diagnosis agent's loop accept good answers, reject bad ones and ask the model to fix them?
The model is replaced by a fake one that returns scripted answers, so it runs in a second.

Run from the repository root:
    python -m agents.diagnosis.tests.test_agent_rules
"""
import json

import agents.diagnosis.agent as agent
from agents.diagnosis.prompts import findings_text, user_message
from agents.triage.tests.checks import Checker

checker = Checker()

FINDINGS = [
    {"incident_id": "DAN-104", "company": "Amazon", "title": "S3 disruption", "summary": "A command removed too "
     "many servers.", "deepened": True, "why": "same trigger",
     "passages": [{"section": "Summary", "content": "One of the commands was entered incorrectly.",
                   "query_source": "cause"},
                  {"section": "Changes", "content": "We modified the tool to remove capacity more slowly.",
                   "query_source": "fix"}]},
    {"incident_id": "DAN-189", "company": "Joyent", "title": "us-east-1 outage", "summary": "An operator "
     "rebooted all servers.", "deepened": False, "passages": []},
]
TRIAGE = {"affected_service": "object store", "trigger": "an engineer took machines out", "symptoms": ["reads fail"],
          "category": None}
HYP = {"cause": "Too much capacity removed.", "based_on": ["DAN-104"], "matches": "trigger", "differs": "subsystem",
       "same_trigger": "yes", "same_component": "yes", "same_mechanism": "yes", "confidence": "high"}
GOOD = {"hypotheses": [HYP], "gaps": [], "search_request": "capacity removal storage outage"}
INVENTED = {**GOOD, "hypotheses": [{**HYP, "based_on": ["DAN-999"]}]}
# Based only on the incident without passages (DAN-189): the evidence is not enough.
WEAK = {"hypotheses": [{**HYP, "based_on": ["DAN-189"], "same_component": "no"}], "gaps": ["nothing fits"],
        "search_request": "capacity removal storage outage", "questions_for_analyst": ["Which command was run?"]}


def run_with(answers, research_round=1):
    """Run the agent with a fake model that returns `answers` in order. Returns (result or error, calls)."""
    replies = iter(answers)
    calls = []

    def fake_chat(messages):
        calls.append(list(messages))
        return {"content": next(replies)}

    agent._chat = fake_chat
    try:
        result, _ = agent.run_agent("Our object store is down.", TRIAGE, FINDINGS, research_round, 3)
        return result, calls
    except RuntimeError as error:
        return error, calls


print("The findings text")
text = findings_text(FINDINGS)
checker.check("deepened incident shows its passages", "One of the commands was entered incorrectly" in text)
checker.check("passages say what they are about", "about the cause" in text and "about the fix" in text)
checker.check("non-deepened incident has no passages", "(not deepened: no passages)" in text)
long = [{**FINDINGS[0], "incident_id": f"DAN-{k:03d}", "passages": [{"section": "x", "content": "word " * 2000,
                                                                       "query_source": "cause"}] * 7}
        for k in range(20)]
checker.check("the text is cut before the length limit", len(findings_text(long)) < 33000)
checker.check("the last round is announced", "LAST research round" in user_message("x", TRIAGE, FINDINGS, 3, 3))
checker.check("an earlier round is not", "LAST research round" not in user_message("x", TRIAGE, FINDINGS, 1, 3))

print("\nThe loop")
result, calls = run_with([json.dumps(GOOD)])
checker.check("a good answer is accepted at once", getattr(result, "next_step", None) == "report" and len(calls) == 1)

result, calls = run_with(["The cause is probably the servers.", json.dumps(GOOD)])
checker.check("text without JSON: the model is asked again", len(calls) == 2 and getattr(result, "evidence_sufficient", False))

result, calls = run_with([json.dumps(INVENTED), json.dumps(GOOD)])
checker.check("an incident not in the findings is rejected and fixed", len(calls) == 2
              and "DAN-999" in calls[1][-1]["content"])

result, calls = run_with([json.dumps(WEAK)], research_round=1)
checker.check("weak evidence in an earlier round: code asks for a new search", len(calls) == 1
              and result.next_step == "refine_search" and result.hypotheses[0].confidence == "medium")

result, calls = run_with([json.dumps(WEAK)], research_round=3)
checker.check("weak evidence in the last round: code asks the analyst", result.next_step == "ask_analyst")

result, calls = run_with(["no json"] * 3)
checker.check("after 3 invalid answers the agent gives up with an error", isinstance(result, RuntimeError))

checker.finish()
