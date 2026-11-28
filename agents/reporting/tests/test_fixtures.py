"""Test: are the simulated inputs well formed?

If the fixtures are wrong, every later test would be wrong too, so we check them first.
No model call, it runs in a second.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.reporting.tests.test_fixtures
"""
from agents.reporting.tests.checks import Checker
from agents.reporting.tests.fixtures import NAMES, load_fixture
from agents.reporting.validation import expected_kind

# The kind of report each fixture should lead to.
EXPECTED_KINDS = {
    "gitlab_diagnosis_en": "diagnosis",
    "gitlab_diagnosis_pt": "diagnosis",
    "inconclusive_weak_evidence": "inconclusive",
    "thin_passages_edge": "diagnosis",
    "no_hypotheses_edge": "inconclusive",
}
FINDING_KEYS = {"post_mortem_id", "company", "title", "url", "summary", "similarity", "deepened", "why", "passages"}

checker = Checker()
for name in NAMES:
    data = load_fixture(name)
    findings = data["findings"]
    finding_ids = {f["post_mortem_id"] for f in findings}

    checker.check(f"{name}: has the keys of the shared state",
                  {"incident_id", "description", "triage_result", "findings", "diagnosis"} <= set(data))
    checker.check(f"{name}: findings have the format of the Research agent",
                  all(FINDING_KEYS <= set(f) for f in findings))
    checker.check(f"{name}: every hypothesis is based on a finding that exists",
                  all(i in finding_ids for h in data["diagnosis"]["hypotheses"] for i in h["based_on"]))
    checker.check(f"{name}: the kind of report would be {EXPECTED_KINDS[name]}",
                  expected_kind(data["diagnosis"]) == EXPECTED_KINDS[name])

# The edge case really has no text about the fix.
thin = load_fixture("thin_passages_edge")
checker.check("thin_passages_edge: the only finding has no passages", thin["findings"][0]["passages"] == [])

# The Portuguese case differs from the English one only in the analyst's message.
english, portuguese = load_fixture("gitlab_diagnosis_en"), load_fixture("gitlab_diagnosis_pt")
checker.check("gitlab_diagnosis_pt: same evidence, other language",
              english["findings"] == portuguese["findings"] and english["description"] != portuguese["description"])

checker.finish()
