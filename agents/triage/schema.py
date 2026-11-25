"""The shape of the triage agent's answer, checked with Pydantic.

Pydantic is a "mold": if the model's answer does not fit the mold, it raises an error
and the agent asks the model to answer again.
"""
from typing import Literal, Optional, get_args

from pydantic import BaseModel, Field, model_validator

# Categories of the danluu dataset (the post-mortems that the research agent searches).
# "Uncategorized" is not in the list: for us, "no category" is simply None.
Category = Literal[
    "Config Errors",
    "Hardware/Power Failures",
    "Conflicts",
    "Database",
    "Time",
]
CATEGORIES = list(get_args(Category))  # the same names as a plain list (used in the prompt)


class RelatedIncident(BaseModel):
    """An open investigation that is the same problem the analyst reports."""

    incident_id: str  # example: "INC-042"
    title: str  # the summary of that investigation


class TriageResult(BaseModel):
    """Everything the triage agent returns for one analyst message."""

    # What is failing, in short English phrases (even if the analyst wrote in Portuguese).
    symptoms: list[str] = Field(default_factory=list)

    # Which service or product is affected ("checkout"), or None if the message does not say.
    affected_service: Optional[str] = None

    # What changed right before the problem, as the analyst said it, in English: a deploy, a command someone ran,
    # a configuration or data change, a migration... One item per change (the analyst may mention more than one:
    # the Diagnosis agent must consider all of them). Empty if the analyst did not mention any.
    triggers: list[str] = Field(default_factory=list)

    # Type of cause, only if the analyst gave a clear hint. Usually None.
    category: Optional[Category] = None

    # Is there enough information to start investigating? (what fails + where)
    enough_information: bool

    # If not enough information: the questions to ask the analyst.
    missing_information: list[str] = Field(default_factory=list)

    # The open investigation that is the same problem, or None.
    related_incident: Optional[RelatedIncident] = None

    @model_validator(mode="after")
    def check_consistency(self):
        """Rules that involve more than one field."""
        if not self.enough_information:
            if not self.missing_information:
                raise ValueError(
                    "enough_information is false, so missing_information must list "
                    "the questions to ask the analyst"
                )
            if self.related_incident is not None:
                raise ValueError(
                    "related_incident must be null when enough_information is false"
                )
        return self


def parse_triage_answer(text):
    """Turn the model's text into a TriageResult.

    The model should answer with only a JSON object, but sometimes it adds words
    or a ```json fence around it. So we take everything between the first "{"
    and the last "}".
    Raises ValueError (Pydantic's errors are ValueErrors too) if the answer is not valid.
    """
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end < start:
        raise ValueError("the answer does not contain a JSON object")
    return TriageResult.model_validate_json(text[start : end + 1])
