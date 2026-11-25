"""Test: does the message that the model reads have everything it needs?

No model call, it runs in a second.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.reporting.tests.test_prompt
"""
from agents.reporting.prompts import build_user_message
from agents.reporting.tests.checks import Checker
from agents.reporting.tests.fixtures import load_fixture

checker = Checker()

gitlab = load_fixture("gitlab_diagnosis_en")
text = build_user_message(gitlab)
checker.check("it has the analyst's message", gitlab["description"] in text)
checker.check("it says the kind of report: diagnosis", 'KIND OF REPORT TO WRITE: "diagnosis"' in text)
checker.check("it has every hypothesis with its confidence", "Hypothesis 1 (confidence: high)" in text and "Hypothesis 2 (confidence: medium)" in text)
checker.check("it has the link of every past incident", all(f["url"] in text for f in gitlab["findings"]))
checker.check("it has the passages of the deepened incidents", "Root cause analysis" in text)
checker.check("it says when an incident has no passages", "(no passages: only the summary is available)" in text)

weak = load_fixture("inconclusive_weak_evidence")
text = build_user_message(weak)
checker.check("weak evidence: the kind is inconclusive", 'KIND OF REPORT TO WRITE: "inconclusive"' in text)
checker.check("weak evidence: the gaps are there", "There are no error messages or logs" in text)

empty = load_fixture("no_hypotheses_edge")
checker.check("no hypotheses: the model is told so", "There is no hypothesis" in build_user_message(empty))

# The diagnosis and the triage result can also be Pydantic objects (inside the graph).
class AsObject:
    def __init__(self, data):
        self.data = data

    def model_dump(self):
        return self.data

as_objects = {**gitlab, "triage_result": AsObject(gitlab["triage_result"]), "diagnosis": AsObject(gitlab["diagnosis"])}
checker.check("it also works with Pydantic objects (as in the graph)", build_user_message(as_objects) == build_user_message(gitlab))

# The analyst's language is decided in code (an English conversation used to get a report in Portuguese).
from agents.reporting.prompts import SYSTEM_PROMPT  # noqa: E402

english = build_user_message({**gitlab, "description": "Requests are failing across an entire region."})
portuguese = build_user_message({**gitlab, "description": "A página de login não abre, está dando erro 500."})
checker.check("English analyst: the language is said and there are no Portuguese fixed words",
              "ANALYST LANGUAGE: English" in english and "O que aconteceu" not in english)
checker.check("Portuguese analyst: the language and the fixed words are given",
              "ANALYST LANGUAGE: Portuguese" in portuguese and "O que aconteceu" in portuguese)
checker.check("the system prompt has no Portuguese words", "O que aconteceu" not in SYSTEM_PROMPT)

checker.finish()
