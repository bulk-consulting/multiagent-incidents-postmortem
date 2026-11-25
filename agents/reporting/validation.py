"""Rules in code that check the report against what the other agents really delivered.

Pydantic (schema.py) checks the SHAPE of the report. This file checks that the CONTENT is honest:
the model cannot invent a source, change a confidence, or call "inconclusive" what the diagnosis says
is enough. It is the same idea as the Triage agent's check_related_incident.

validate_report returns a list of problems. An empty list means the report is valid.
If there are problems, the agent sends them back to the model, so it can fix the report.
"""


import re

# A link in the text: from "http" up to a space or a closing bracket.
LINK_PATTERN = re.compile(r"https?://[^\s)>\]]+")


def _urls_in(text):
    """The links that appear in a text, without the punctuation that ends a sentence."""
    return {link.rstrip(".,;:!?") for link in LINK_PATTERN.findall(text)}


def _as_dict(value):
    """The diagnosis can arrive as a Pydantic object (inside the graph), as a dict (in the tests), or be missing
    (an agent before failed): then it counts as an empty diagnosis, which asks for an inconclusive report."""
    if value is None:
        return {"hypotheses": [], "evidence_sufficient": False, "gaps": []}
    return value.model_dump() if hasattr(value, "model_dump") else value


def expected_kind(diagnosis):
    """The kind of report is decided by code, not by the model: enough evidence means a diagnosis."""
    return "diagnosis" if _as_dict(diagnosis).get("evidence_sufficient") else "inconclusive"


def validate_report(report, findings, diagnosis):
    """Check the report against the findings (Research agent) and the diagnosis (Diagnosis agent)."""
    diagnosis = _as_dict(diagnosis)
    problems = []

    # 1) The kind must be the one the diagnosis calls for.
    wanted = expected_kind(diagnosis)
    if report.kind != wanted:
        problems.append(f'kind must be "{wanted}" (evidence_sufficient is {diagnosis["evidence_sufficient"]}), '
                        f'but the report says "{report.kind}".')

    # 2) Every source must be a real finding, with exactly its url.
    url_of = {f["incident_id"]: f.get("url", "") for f in findings or []}
    for number, cause in enumerate(report.causes, 1):
        for source in cause.sources:
            if source.incident_id not in url_of:
                problems.append(f"cause {number}: source {source.incident_id} is not in the findings. "
                                f"Use only: {sorted(url_of)}.")
            elif source.url != url_of[source.incident_id]:
                problems.append(f"cause {number}: the url of {source.incident_id} must be exactly "
                                f"{url_of[source.incident_id]}.")

    # 3) In a diagnosis, the causes are the diagnosis hypotheses: same number, same order, same confidence,
    #    and each cause cites the incidents its hypothesis is based on. The report presents; it does not decide.
    if report.kind == "diagnosis" and wanted == "diagnosis":
        hypotheses = diagnosis["hypotheses"]
        if len(report.causes) != len(hypotheses):
            problems.append(f"the report must have {len(hypotheses)} cause(s), one for each hypothesis "
                            f"of the diagnosis, in the same order. It has {len(report.causes)}.")
        else:
            for number, (cause, hypothesis) in enumerate(zip(report.causes, hypotheses), 1):
                if cause.confidence != hypothesis["confidence"]:
                    problems.append(f'cause {number}: confidence must be "{hypothesis["confidence"]}", '
                                    f'as in the diagnosis, not "{cause.confidence}".')
                cited = {s.incident_id for s in cause.sources}
                missing = [i for i in hypothesis["based_on"] if i not in cited]
                if missing:
                    problems.append(f"cause {number}: it must cite the incident(s) {missing}, "
                                    "which the hypothesis is based on.")

    # 4) The message is free text, but its links must be honest: no link outside the findings,
    #    and the link of every source of the report must appear in it.
    valid_urls = set(url_of.values())
    for url in sorted(_urls_in(report.message) - valid_urls):
        problems.append(f"message: the link {url} is not one of the findings. Use only the links you were given.")
    for number, cause in enumerate(report.causes, 1):
        for source in cause.sources:
            if source.url in valid_urls and source.url not in report.message:
                problems.append(f"message: it must show the link of {source.incident_id} ({source.url}).")

    return problems
