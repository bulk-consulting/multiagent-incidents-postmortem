"""Loads the simulated inputs of the Reporting agent (the JSON files in the fixtures folder).

Each file looks like the shared state of an investigation, with the keys the Reporting agent will read:
    incident_id, description, triage_result, findings, diagnosis, research_rounds

The evidence is real text taken from the danluu post-mortem corpus (GitLab, Keepthescore, Spotify, Allegro).
The similarity numbers and the "why" sentences are invented.
"""
import json
from pathlib import Path

from agents.reporting.schema import Report, ReportCause, Source

FIXTURES_DIR = Path(__file__).parent / "fixtures"

NAMES = [
    "gitlab_diagnosis_en",          # normal case: enough evidence, analyst writes in English
    "gitlab_diagnosis_pt",          # same evidence, analyst writes in Portuguese
    "inconclusive_weak_evidence",   # weak evidence and the research limit reached
    "thin_passages_edge",           # enough evidence, but the incident has only a short summary (no fix text)
    "no_hypotheses_edge",           # no hypothesis at all, research limit reached
]


def load_fixture(name):
    return json.loads((FIXTURES_DIR / f"{name}.json").read_text(encoding="utf-8"))


def good_report_for(data):
    """A correct diagnosis for a fixture, written by hand: one cause per hypothesis, same order,
    same confidence, real sources, and a message that shows every link. Used to test the rules and the loop."""
    findings = {f["post_mortem_id"]: f for f in data["findings"]}
    causes = []
    for hypothesis in data["diagnosis"]["hypotheses"]:
        sources = [Source(post_mortem_id=i, title=findings[i]["title"], url=findings[i]["url"]) for i in hypothesis["based_on"]]
        causes.append(ReportCause(root_cause=hypothesis["cause"], sources=sources, confidence=hypothesis["confidence"]))
    message = "Most likely causes:\n" + "\n".join(f"- {s.title}: {s.url}" for c in causes for s in c.sources)
    return Report(kind="diagnosis", summary="A short summary.", message=message, causes=causes)
