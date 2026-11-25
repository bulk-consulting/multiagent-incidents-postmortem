"""Application logic: turns the analyst's conversation into the graph input, runs the graph, returns the report.

The API (app/api) only calls this file. The graph is the main graph of the 4 agents
(agents/orchestration/graph.py: Triage -> Research -> Diagnosis -> Report).

Every message of the chat is a new, independent run of the graph:
  - the graph receives everything the analyst wrote in the conversation (build_description);
  - when the graph needs more information it pauses (interrupt) with questions. For now we do not resume
    that pause: we send the questions to the chat, and the analyst's answer starts a new run.
"""
from __future__ import annotations

import logging
import time
import uuid
from functools import lru_cache

from langgraph.checkpoint.memory import InMemorySaver

from agents.orchestration.graph import build_graph
from agents.orchestration.state import make_serializer
from agents.reporting.related import analyst_language
from agents.reporting.schema import Report
from app.schemas.incident import IncidentRequest, IncidentResponse

log = logging.getLogger(__name__)

# The text before the questions, in the analyst's language.
QUESTIONS_INTRO = {
    "pt": "Para continuar a investigação, preciso de mais algumas informações:",
    "en": "To continue the investigation, I need some more information:",
}


@lru_cache(maxsize=1)
def get_graph():
    """Builds the graph once and reuses it in every request.

    The checkpointer keeps the state of each run in memory (no database). The graph needs one,
    because the pause for questions (interrupt) only works with a checkpointer.
    """
    checkpointer = InMemorySaver(serde=make_serializer())
    return build_graph(checkpointer=checkpointer)


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


def previous_answers(request: IncidentRequest) -> list[str]:
    """The answers the analyst already gave to the system's questions in this conversation.

    The graph asks the analyst at most MAX_ANALYST_ROUNDS times (3); after that it writes the report with what
    it has. The graph counts the answers in the state key "analyst_answers", but every message of our chat is a
    new run, so the graph would always count 0 and could ask forever. Here we give it the count from the chat.

    Example: "uploads fail" (first message), then "the storage service" (answer 1), then "no deploy" (answer 2).
    """
    analyst_messages = []
    for old_message in request.history:
        if old_message.role == "user":
            analyst_messages.append(old_message.content)
    analyst_messages.append(request.message)

    # The first message describes the problem; every message after it answers a question.
    return analyst_messages[1:]


def run_graph(incident_id: str, description: str, answers: list[str]) -> tuple[dict, list[str]]:
    """Runs the graph step by step and writes one log line per agent.

    Returns (final state, questions). The questions list is empty unless the graph paused to ask the analyst.
    """
    graph = get_graph()
    config = {"configurable": {"thread_id": incident_id}}
    graph_input = {"incident_id": incident_id, "description": description, "analyst_answers": answers}
    questions = []

    # stream(): the graph gives us what each node wrote, as soon as the node finishes.
    for step in graph.stream(graph_input, config, stream_mode="updates"):
        for node_name, update in step.items():

            # The graph paused to ask the analyst (ask_analyst node).
            if node_name == "__interrupt__":
                pause = update[0].value
                questions = list(pause.get("questions", []))
                log.info("%s: [pause] %d question(s) for the analyst", incident_id, len(questions))
                continue

            # Every node writes one line in "trace": how long it took and a summary of its result.
            for line in (update or {}).get("trace", []):
                log.info("%s: [%s] %ss %s", incident_id, line["node"], line["seconds"], line["summary"])

    final_state = graph.get_state(config).values
    return final_state, questions


def questions_report(incident_id: str, description: str, questions: list[str]) -> Report:
    """The answer when the graph paused because information is missing: the questions, in the same shape."""
    intro = QUESTIONS_INTRO[analyst_language(description)]
    lines = [intro, ""]
    for question in questions:
        lines.append(f"- {question}")

    return Report(
        incident_id=incident_id,
        kind="questions",
        summary=intro,
        message="\n".join(lines),
        gaps=questions,
    )


def to_report(raw_report) -> Report:
    """The report of the graph as a Report.

    The Reporting agent returns a Report object. The reports built in code (an agent failed, or the problem
    is already under investigation) are dicts with the same fields. Here all of them become a Report.
    """
    if isinstance(raw_report, Report):
        return raw_report
    return Report.model_validate(raw_report)


def investigate(request: IncidentRequest) -> IncidentResponse:
    incident_id = f"INC-{uuid.uuid4().hex[:8]}"  # no database yet: only to follow the run in the logs
    description = build_description(request)
    answers = previous_answers(request)
    log.info("%s: start (%d chars, %d answers from the analyst)", incident_id, len(description), len(answers))

    start = time.perf_counter()
    final_state, questions = run_graph(incident_id, description, answers)
    seconds = round(time.perf_counter() - start, 2)

    if questions:
        report = questions_report(incident_id, description, questions)
    else:
        report = to_report(final_state["report"])

    log.info("%s: done in %.2fs (kind=%s)", incident_id, seconds, report.kind)
    return IncidentResponse(incident_id=incident_id, seconds=seconds, report=report)
