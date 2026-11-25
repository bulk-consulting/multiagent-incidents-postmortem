"""Application logic: turns the analyst's conversation into the graph input, runs the graph, returns the report.

The API (app/api) only calls this file. It does not know which graph runs behind it.
"""
from __future__ import annotations

import logging
import time
import uuid
from functools import lru_cache

from app.schemas.incident import IncidentRequest, IncidentResponse

log = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_graph():
    """Builds the graph once and reuses it in every request."""
    # TEMPORARY: the fake graph, until the real graph of the 4 agents is ready.
    # Then only this import changes (and the input/output names, if the real graph uses others).
    from app.services.fake_graph import build_graph
    return build_graph()


def build_description(request: IncidentRequest) -> str:
    """Puts together, in one text, everything the analyst wrote in this conversation.

    Example: if the analyst first wrote "uploads are failing" and now writes "it is a 401 error",
    the graph receives both messages, so it understands the whole incident.
    """
    analyst_messages = []

    # 1. The messages the analyst wrote before (we skip the system's answers).
    for old_message in request.history:
        if old_message.role == "user":
            analyst_messages.append(old_message.content)

    # 2. The new message.
    analyst_messages.append(request.message)

    # 3. One text, with a blank line between messages.
    return "\n\n".join(analyst_messages)


def investigate(request: IncidentRequest) -> IncidentResponse:
    incident_id = f"INC-{uuid.uuid4().hex[:8]}"  # no database yet: only to follow the request in the logs
    description = build_description(request)
    log.info("%s: start (%d chars, %d earlier messages)", incident_id, len(description), len(request.history))

    start = time.perf_counter()
    result = get_graph().invoke({"incident_id": incident_id, "description": description})
    seconds = round(time.perf_counter() - start, 2)

    report = result["report"]
    log.info("%s: done in %.2fs (kind=%s)", incident_id, seconds, report.kind)
    return IncidentResponse(incident_id=incident_id, seconds=seconds, report=report)
