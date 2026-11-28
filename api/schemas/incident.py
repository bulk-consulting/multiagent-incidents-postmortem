"""Input and output of the /incidents endpoint, checked with Pydantic (invalid input → 422)."""
from typing import Literal

from pydantic import BaseModel, Field

from agents.reporting.schema import Report


class ChatMessage(BaseModel):
    """One earlier message of the conversation, as the frontend shows it."""

    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=20_000)


class IncidentRequest(BaseModel):
    """What the analyst sends: the new message and, optionally, the conversation so far."""

    message: str = Field(min_length=1, max_length=5_000, examples=["O banco de dados parou de replicar e perdemos dados."])
    history: list[ChatMessage] = Field(default_factory=list, max_length=50)


class IncidentResponse(BaseModel):
    """What the API returns: the Reporting agent's answer and some data for the log and the screen."""

    incident_id: str
    seconds: float
    report: Report
