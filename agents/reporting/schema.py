"""The shape of the Reporting agent's answer, checked with Pydantic.

Same idea as agents/triage/schema.py: if the model's answer does not fit this shape, Pydantic raises
an error, and the agent asks the model to answer again.

The Reporting agent receives the diagnosis and the evidence, and writes the final answer for the analyst:
  - kind "diagnosis":    the most likely causes, each with the fix, a prevention checklist and the source;
  - kind "inconclusive": what we could not find out, and what the analyst can check now.

The shape follows the contract in docs/E5_Orchestrated_Multi_Agent_System/E5_Estado_e_Formatos.md (section 6).
"""
from typing import Literal, Optional

from pydantic import BaseModel, Field, model_validator

Confidence = Literal["high", "medium", "low"]
# The kinds of answer the analyst can get. The Reporting agent (the LLM) writes only "diagnosis" and "inconclusive".
# The other two are built in code, in the same shape, so every answer of the graph looks the same:
#   "related_incident"  the problem is already being investigated (agents/reporting/related.py)
#   "questions"         information is missing: the message asks the analyst (api/services/incident_service.py)
ReportKind = Literal["diagnosis", "inconclusive", "related_incident", "questions"]


class Source(BaseModel):
    """A past incident that the report is based on."""

    post_mortem_id: str  # the PAST incident (post-mortem), for example "DAN-164"
    title: str
    url: str          # must be exactly the url of that incident in the findings


class ReportCause(BaseModel):
    """One probable cause of the current incident."""

    # The cause in the past incident, and why it applies to the current one. 1 to 3 sentences.
    root_cause: str = Field(min_length=1)

    # What was done to fix it. Empty if the post-mortem text we have does not say.
    remediation_steps: list[str] = Field(default_factory=list)

    # Code or configuration that was changed, only if the post-mortem says so.
    changes: Optional[str] = None

    # What to do so it does not happen again. Empty if the text does not say.
    prevention_checklist: list[str] = Field(default_factory=list)

    # At least one source. The code checks that each one really exists in the findings.
    sources: list[Source] = Field(min_length=1)

    # Comes from the Diagnosis agent. The Reporting agent repeats it, it does not change it.
    confidence: Confidence


class Report(BaseModel):
    """Everything the Reporting agent returns."""

    # The id of this investigation. The code fills it in, the model does not write it.
    incident_id: str = ""

    kind: ReportKind

    # 2 or 3 sentences for the analyst, in the analyst's language.
    summary: str = Field(min_length=1)

    # The final answer for the chat, in Markdown, ready to show as it is. The model writes it freely
    # (the Reporting agent is the "artist"), but the code checks that its links are real and that it
    # shows the sources. The fields below are the same information in a structured form.
    message: str = Field(min_length=1)

    # The probable causes, from the most to the least likely. Can be empty in an inconclusive report.
    causes: list[ReportCause] = Field(default_factory=list)

    # What is missing to be sure. Required in an inconclusive report.
    gaps: list[str] = Field(default_factory=list)

    # What the analyst can check right now.
    suggested_checks: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def check_consistency(self):
        """Rules that involve more than one field."""
        if self.kind == "diagnosis" and not self.causes:
            raise ValueError('kind is "diagnosis", so there must be at least one cause')
        if self.kind == "inconclusive" and not self.gaps:
            raise ValueError('kind is "inconclusive", so gaps must say what is missing')
        return self


def parse_report_answer(text):
    """Turn the model's text into a Report.

    The model should answer with only a JSON object, but sometimes it adds words or a ```json fence
    around it. So we take everything between the first "{" and the last "}".
    Raises ValueError (Pydantic's errors are ValueErrors too) if the answer is not valid.
    """
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end < start:
        raise ValueError("the answer does not contain a JSON object")
    return Report.model_validate_json(text[start : end + 1])
