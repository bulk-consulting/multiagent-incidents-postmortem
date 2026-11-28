"""Test: do the rules in code catch a dishonest report?

We build a good report from a simulated input, check that it passes, and then break it in one way at a time.
No model call, it runs in a second.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.reporting.tests.test_validation
"""
from agents.reporting.schema import Report, Source
from agents.reporting.tests.checks import Checker
from agents.reporting.tests.fixtures import good_report_for, load_fixture
from agents.reporting.validation import validate_report


def problems_of(report, data):
    return validate_report(report, data["findings"], data["diagnosis"])


def changed(report, **changes):
    """A copy of the report with some fields changed."""
    return report.model_copy(update=changes)


checker = Checker()
gitlab = load_fixture("gitlab_diagnosis_en")
good = good_report_for(gitlab)

checker.check("a correct diagnosis has no problems", problems_of(good, gitlab) == [], f"({problems_of(good, gitlab)})")

# 1) the kind
wrong_kind = changed(good, kind="inconclusive", gaps=["x"])
checker.check("inconclusive when the evidence is enough is flagged",
              any("kind must be" in p for p in problems_of(wrong_kind, gitlab)))

# 2) the sources
invented = good.causes[0].model_copy(update={"sources": [Source(post_mortem_id="DAN-999", title="Made up", url="https://made.up")]})
checker.check("an invented source is flagged",
              any("DAN-999" in p for p in problems_of(changed(good, causes=[invented, good.causes[1]]), gitlab)))

real_id_wrong_url = good.causes[0].model_copy(
    update={"sources": [Source(post_mortem_id="DAN-164", title="x", url="https://wrong.example")]})
checker.check("a real incident with a wrong url is flagged",
              any("url of DAN-164" in p for p in problems_of(changed(good, causes=[real_id_wrong_url, good.causes[1]]), gitlab)))

# 3) the causes follow the diagnosis
checker.check("a missing cause is flagged",
              any("must have 2 cause" in p for p in problems_of(changed(good, causes=good.causes[:1]), gitlab)))

other_confidence = good.causes[0].model_copy(update={"confidence": "low"})
checker.check("a changed confidence is flagged",
              any("confidence must be" in p for p in problems_of(changed(good, causes=[other_confidence, good.causes[1]]), gitlab)))

forgot_based_on = good.causes[1].model_copy(update={"sources": good.causes[0].sources})
checker.check("a cause that forgets the incident its hypothesis is based on is flagged",
              any("DAN-043" in p for p in problems_of(changed(good, causes=[good.causes[0], forgot_based_on]), gitlab)))

# 4) the free message
checker.check("a message with a link that is not in the findings is flagged",
              any("https://made.up/page" in p for p in problems_of(
                  changed(good, message=good.message + "\nSee also https://made.up/page."), gitlab)))
checker.check("a link followed by a full stop is read correctly",
              problems_of(changed(good, message=good.message + "\nSource: " + good.causes[0].sources[0].url + "."), gitlab) == [])
checker.check("a message that hides the link of a source is flagged",
              any("must show the link of DAN-043" in p for p in problems_of(
                  changed(good, message="Most likely a deletion on the wrong host: " + good.causes[0].sources[0].url), gitlab)))

# The inconclusive cases
weak = load_fixture("inconclusive_weak_evidence")
inconclusive = Report(kind="inconclusive", summary="We could not find a clear cause.",
                      message="We could not find a clear cause yet.", gaps=["No logs."])
checker.check("a correct inconclusive report has no problems", problems_of(inconclusive, weak) == [])

claims_diagnosis = good_report_for(load_fixture("gitlab_diagnosis_en"))
checker.check("a diagnosis when the evidence is NOT enough is flagged",
              any("kind must be" in p for p in problems_of(claims_diagnosis, weak)))

no_hypotheses = load_fixture("no_hypotheses_edge")
checker.check("an inconclusive report with no hypothesis is valid", problems_of(inconclusive, no_hypotheses) == [])

# The diagnosis may also come as a Pydantic object (inside the graph) instead of a dict (in these tests).
class FakeDiagnosisObject:
    def __init__(self, data):
        self.data = data

    def model_dump(self):
        return self.data

checker.check("the diagnosis can be an object with model_dump (as in the graph)",
              validate_report(good, gitlab["findings"], FakeDiagnosisObject(gitlab["diagnosis"])) == [])

checker.finish()
