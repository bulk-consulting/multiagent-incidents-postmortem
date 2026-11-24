"""Test: does the Reporting agent write a good report in each situation?

Each scenario is a simulated input (agents/reporting/tests/fixtures/) plus what we expect. It calls the
model for real, so each scenario takes about 20 to 60 seconds.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.reporting.tests.test_scenarios                       (all scenarios)
    .venv/Scripts/python.exe -m agents.reporting.tests.test_scenarios thin_passages_edge    (only this one)

What is checked in every scenario: the report is valid (the rules in code found no problem), the
fallback was not needed, the kind is the right one, and the code filled in the incident_id.
"""
import re
import sys
import time

from agents.reporting.agent import run_reporting_agent
from agents.reporting.tests.checks import Checker
from agents.reporting.tests.fixtures import NAMES, load_fixture

# The Windows console cannot print some characters the model writes.
sys.stdout.reconfigure(encoding="utf-8")

PORTUGUESE_WORDS = {"que", "não", "com", "uma", "para", "foi", "dados", "pode", "causa", "de", "do", "da", "os", "as", "um", "em"}
ENGLISH_WORDS = {"the", "and", "was", "that", "with", "for", "this", "is", "of", "to", "a", "in"}


def language_of(text):
    """A very simple guess: which language has more of its common words in the text."""
    words = re.findall(r"[a-zçãõáéíóúâêô]+", text.lower())
    portuguese = sum(word in PORTUGUESE_WORDS for word in words)
    english = sum(word in ENGLISH_WORDS for word in words)
    return "portuguese" if portuguese > english else "english"


def check_scenario(name, report, checker):
    """The checks that are different in each scenario."""
    if name == "gitlab_diagnosis_en":
        checker.check(f"{name}: two causes, as in the diagnosis", len(report.causes) == 2, f"(got {len(report.causes)})")
        checker.check(f"{name}: the answer is in English", language_of(report.message) == "english")
        checker.check(f"{name}: the first cause says how it was fixed or what to prevent",
                      bool(report.causes[0].remediation_steps or report.causes[0].prevention_checklist))
    elif name == "gitlab_diagnosis_pt":
        checker.check(f"{name}: the answer is in Portuguese", language_of(report.message) == "portuguese",
                      f"(guess: {language_of(report.message)})")
        checker.check(f"{name}: the summary is in Portuguese", language_of(report.summary) == "portuguese",
                      f"(guess: {language_of(report.summary)})")
    elif name == "inconclusive_weak_evidence":
        checker.check(f"{name}: it says what is missing", len(report.gaps) >= 1)
        checker.check(f"{name}: any cause it lists has low confidence", all(c.confidence == "low" for c in report.causes))
        checker.check(f"{name}: it suggests what to check", len(report.suggested_checks) >= 1)
    elif name == "thin_passages_edge":
        # The only incident has a short summary and no text about the fix: the agent must not invent one.
        checker.check(f"{name}: it does not invent remediation steps",
                      all(c.remediation_steps == [] for c in report.causes), f"(got {[c.remediation_steps for c in report.causes]})")
        checker.check(f"{name}: it does not invent a prevention checklist",
                      all(c.prevention_checklist == [] for c in report.causes), f"(got {[c.prevention_checklist for c in report.causes]})")
        checker.check(f"{name}: it does not invent code or configuration changes", all(c.changes is None for c in report.causes))
    elif name == "no_hypotheses_edge":
        checker.check(f"{name}: there are no causes", report.causes == [])
        checker.check(f"{name}: it says what is missing", len(report.gaps) >= 1)


EXPECTED_KINDS = {"gitlab_diagnosis_en": "diagnosis", "gitlab_diagnosis_pt": "diagnosis",
                  "inconclusive_weak_evidence": "inconclusive", "thin_passages_edge": "diagnosis",
                  "no_hypotheses_edge": "inconclusive"}

names = sys.argv[1:]  # optional: run only the scenarios with these names
selected = [n for n in NAMES if not names or n in names]
if not selected:
    sys.exit(f"No scenario matches {names}. Available: {NAMES}")

checker = Checker()
for name in selected:
    state = load_fixture(name)
    print(f"\n=== {name}")
    print(f"analyst: {state['description']}")

    start = time.time()
    try:
        report, messages, attempts, problems = run_reporting_agent(state)
    except Exception as error:  # the model call crashed
        checker.check(f"{name}: the agent finished", False, f"({error})")
        continue
    print(f"finished in {time.time() - start:.0f}s, attempts: {attempts}")
    print(report.model_dump_json(indent=2, exclude={"message"}))
    print("--- message ---")
    print(report.message)

    checker.check(f"{name}: the model's report was valid (no fallback)", problems == [], f"(problems: {problems})")
    checker.check(f"{name}: the kind is {EXPECTED_KINDS[name]}", report.kind == EXPECTED_KINDS[name], f"(got {report.kind})")
    checker.check(f"{name}: the incident_id was filled in", report.incident_id == state["incident_id"])
    check_scenario(name, report, checker)

print("\n=== SUMMARY")
checker.finish()
