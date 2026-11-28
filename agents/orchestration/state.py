"""The shared state of one investigation: the "folder" that goes from agent to agent.

The agents do not talk to each other. Each node of the main graph reads what it needs from this state,
does its work and writes its result back. Code (the routing) reads the state and decides which node
runs next. The state is saved by the LangGraph checkpointer after every step, with
thread_id = incident_id, so an investigation can pause (interrupt) and continue later.

This is the "contract" of docs/E5_Orchestrated_Multi_Agent_System/E5_Estado_e_Formatos.md (section 3). Changing a key here means
changing that document too, and telling whoever owns the nodes that read or write it.

Who writes what:
    description, analyst_answers     input / ask_analyst
    triage_result, symptoms          triage           (agents/triage/node.py)
    findings, seen_ids, ...          research         (agents/research)
    search_request                   diagnosis        (read by research in a refinement)
    diagnosis                        diagnosis        (agents/diagnosis)
    pending_questions                routing          (questions from triage or diagnosis)
    report, report_problems, ...     report / validate_report (agents/report)
    route, errors, trace             every node
"""
from __future__ import annotations

import operator
from typing import Annotated, Any, TypedDict

from agents.diagnosis.schema import DiagnosisResult
from agents.triage.schema import TriageResult

MAX_RESEARCH_ROUNDS = 3   # the first research + up to 2 refinements asked by the Diagnosis agent
MAX_REPORT_FIXES = 2      # times the Report agent can fix a report that failed validation


class InvestigationState(TypedDict, total=False):
    # identification and input
    incident_id: str                     # = thread_id of the checkpointer
    description: str                     # the analyst's message + their answers (input of triage and research)
    analyst_answers: Annotated[list[str], operator.add]  # answers given to the data requests

    # Triage agent
    triage_result: TriageResult
    symptoms: list[str]                  # = triage_result.symptoms (input of the Research agent)

    # Research agent
    findings: list[dict]                 # up to 8 past incidents (format: agents/research/agent.py, build_findings)
    seen_ids: list[str]                  # incidents already seen (a refinement does not bring them again)
    search_request: str                  # what the Diagnosis agent wants the next search to find; empty at first
    research_rounds: int                 # how many times the Research agent ran (limit: MAX_RESEARCH_ROUNDS)

    # Diagnosis agent
    diagnosis: DiagnosisResult

    # data request (interrupt)
    pending_questions: list[str]         # questions sent to the analyst

    # Report agent
    report: Any                          # agents.reporting.schema.Report (Mari's agent), or a dict (code)
    report_problems: list[str]           # what the validation found wrong; goes back to the Report agent
    report_attempts: int                 # limit: MAX_REPORT_FIXES

    # control
    route: str                           # last routing decision (for the log and the demo)
    errors: Annotated[list[dict], operator.add]  # {"node": ..., "error": ...}: what failed and where
    trace: Annotated[list[dict], operator.add]   # {"node": ..., "seconds": ..., "summary": ...}: step by step


# The checkpointer saves the state with msgpack. Reading our Pydantic classes back from a checkpoint works
# today with a warning, and LangGraph says it will be blocked in a future version unless the classes are on
# an allowlist (a safety measure: whoever can write to the checkpoint database could make it build any class).
# Every Pydantic class that goes into the state must be listed here.
STATE_CLASSES = [
    ("agents.triage.schema", "TriageResult"),
    ("agents.triage.schema", "RelatedIncident"),
    ("agents.diagnosis.schema", "DiagnosisResult"),
    ("agents.diagnosis.schema", "Hypothesis"),
    ("agents.reporting.schema", "Report"),
    ("agents.reporting.schema", "ReportCause"),
    ("agents.reporting.schema", "Source"),
]


def make_serializer():
    """The serializer for the checkpointer (InMemorySaver in tests, PostgresSaver in the demo)."""
    from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer
    return JsonPlusSerializer(allowed_msgpack_modules=STATE_CLASSES)
