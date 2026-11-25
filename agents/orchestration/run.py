"""Demonstration of the whole flow: the analyst's message goes in, the report comes out.

The state of each investigation is saved in Postgres (the same database as the RAG, DATABASE_URL in .env), with
thread_id = incident_id. When the flow pauses to ask the analyst, you can answer right away or stop the program and
answer later, in another run, with --resume.

Run from the repository root, with the database up:
    # new investigation (asks the questions in the terminal, if there are any)
    multiagent_env/bin/python -I agents/orchestration/run.py "Requests are failing across an entire region."
    # choose the incident id (default: INC-<date-time>)
    multiagent_env/bin/python -I agents/orchestration/run.py "..." --incident INC-123
    # answer a paused investigation later, in another run
    multiagent_env/bin/python -I agents/orchestration/run.py --resume INC-123 "It is our object store."
    # see where an investigation stopped
    multiagent_env/bin/python -I agents/orchestration/run.py --show INC-123
    # without Postgres (the state lives only while the program runs)
    multiagent_env/bin/python -I agents/orchestration/run.py "..." --memory
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv  # noqa: E402
from langgraph.types import Command  # noqa: E402

from agents.orchestration.graph import build_graph  # noqa: E402
from agents.orchestration.state import make_serializer  # noqa: E402

load_dotenv(ROOT / ".env")


@contextmanager
def checkpointer(memory: bool):
    """PostgresSaver on the project database (tables created on the first run), or InMemorySaver."""
    if memory:
        from langgraph.checkpoint.memory import InMemorySaver
        yield InMemorySaver(serde=make_serializer())
        return
    from langgraph.checkpoint.postgres import PostgresSaver
    from psycopg import Connection
    from psycopg.rows import dict_row
    with Connection.connect(os.environ["DATABASE_URL"], autocommit=True, prepare_threshold=0,
                            row_factory=dict_row) as conn:
        saver = PostgresSaver(conn, serde=make_serializer())
        saver.setup()  # creates the checkpoint tables if they do not exist
        yield saver


def show_step(node: str, update: dict) -> None:
    for t in (update or {}).get("trace", []):
        print(f"  [{t['node']}] {t['summary']}  ({t['seconds']}s)", flush=True)


def run_until_pause_or_end(graph, graph_input, config) -> dict | None:
    """Runs the graph, printing each step. Returns the pause (interrupt) value, or None when it ended."""
    for part in graph.stream(graph_input, config, stream_mode="updates"):
        for node, update in part.items():
            if node == "__interrupt__":
                return update[0].value
            show_step(node, update)
    return None


def print_report(graph, config) -> None:
    state = graph.get_state(config).values
    report = state.get("report")
    report = report.model_dump() if hasattr(report, "model_dump") else report
    print("\n" + "=" * 80 + "\nREPORT\n" + "=" * 80)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if state.get("errors"):
        print("\nerrors:", json.dumps(state["errors"], ensure_ascii=False, indent=2))


def ask_in_terminal(pause: dict) -> str | None:
    print("\nThe investigation needs more information:")
    for q in pause.get("questions", []):
        print(f"  - {q}")
    print(f"(Enter to stop now and answer later with --resume {pause.get('incident_id')} \"...\")")
    try:
        answer = input("answer> ").strip()
    except EOFError:  # no terminal (e.g. run in the background): stop here
        print()
        return None
    return answer or None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("message", nargs="*", help="the analyst's message (or the answer, with --resume)")
    ap.add_argument("--incident", help="incident id (= thread_id); default INC-<date-time>")
    ap.add_argument("--resume", metavar="INCIDENT", help="answer a paused investigation")
    ap.add_argument("--show", metavar="INCIDENT", help="show where an investigation stopped")
    ap.add_argument("--memory", action="store_true", help="InMemorySaver instead of Postgres")
    a = ap.parse_args()
    text = " ".join(a.message).strip()

    with checkpointer(a.memory) as saver:
        graph = build_graph(saver)
        if a.show:
            config = {"configurable": {"thread_id": a.show}}
            snap = graph.get_state(config)
            if not snap.values:
                sys.exit(f"no investigation {a.show}")
            print(f"next: {snap.next or 'ended'}")
            for t in snap.values.get("trace", []):
                print(f"  [{t['node']}] {t['summary']}")
            if snap.next:
                pending = snap.values.get("pending_questions", [])
                print("waiting for the analyst:", pending)
            else:
                print_report(graph, config)
            return
        if a.resume:
            if not text:
                sys.exit("--resume needs the answer")
            incident_id, graph_input = a.resume, Command(resume=text)
        else:
            if not text:
                sys.exit("write the analyst's message")
            incident_id = a.incident or f"INC-{datetime.now():%Y%m%d-%H%M%S}"
            graph_input = {"incident_id": incident_id, "description": text}
        config = {"configurable": {"thread_id": incident_id}}
        print(f"investigation {incident_id}")
        while True:
            pause = run_until_pause_or_end(graph, graph_input, config)
            if pause is None:
                print_report(graph, config)
                return
            answer = ask_in_terminal(pause)
            if answer is None:
                print(f"paused. To continue: run.py --resume {incident_id} \"your answer\"")
                return
            graph_input = Command(resume=answer)


if __name__ == "__main__":
    main()
