"""
Demonstration of the Research RAG agent in hybrid mode, step by step, for screen recording (E4).

    multiagent_env/bin/python -I agents/research/demo.py                   # default example (hard case)
    multiagent_env/bin/python -I agents/research/demo.py --example mars    # Mars Pathfinder example
    multiagent_env/bin/python -I agents/research/demo.py "your incident description" [--pause 2]

It runs the same agent (agents/research/agent.py, hybrid mode) and prints each step of the LangGraph flow:
the queries the LLM writes, where each candidate came from (analyst's text or LLM queries), which incidents
the LLM chooses and why, and the root-cause and fix passages found inside them.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:  # lets "python agents/research/demo.py" find the packages agents/ and rag/
    sys.path.insert(0, str(ROOT))
from agents.research import agent  # noqa: E402
from langchain_core.messages import AIMessage, ToolMessage  # noqa: E402

EXAMPLES = {
    "tail": "Our service suddenly started failing on calls to a cloud provider's API, with no change on our side.",
    "mars": "The onboard computer keeps resetting itself every now and then, a few days after going into operation.",
}
QUERY_SOURCE = {"llm": "LLM query", "cause": "fixed: root cause", "fix": "fixed: fix / prevention"}

console = Console(width=110)


def pause(seconds: float) -> None:
    if seconds:
        time.sleep(seconds)


def step(n: int, title: str, subtitle: str) -> None:
    console.print()
    console.print(Rule(f"[bold cyan]STEP {n} · {title}[/]"))
    console.print(f"[dim]{subtitle}[/]")


def show_agent(delta: dict, call: int, pause_s: float) -> None:
    for m in delta.get("messages", []):
        if not isinstance(m, AIMessage):
            continue
        secs = (delta.get("llm_calls") or [{}])[-1].get("seconds", "?")
        for c in m.tool_calls:
            if c["name"] == "find_similar_incidents":
                step(1 if call == 1 else 3, "The LLM decides how to search",
                     f"LLM call {call} ({secs}s) → tool [bold]find_similar_incidents[/]")
                for q in c["args"].get("queries", []):
                    console.print(f"   🔎  [yellow]{q}[/]")
                console.print("   [dim]+ the code always adds the analyst's original text as one more search[/]")
            elif c["name"] == "search_inside_incidents":
                step(3, "The LLM chooses which incidents to investigate",
                     f"LLM call {call} ({secs}s) → tool [bold]search_inside_incidents[/]")
                for s in c["args"].get("searches", []):
                    console.print(f"   ✅  [bold green]{s.get('incident_id')}[/]  query: [yellow]{s.get('query')}[/]")
                    if s.get("why"):
                        console.print(f"       [italic]why: {s.get('why')}[/]")
        if not m.tool_calls:
            step(3, "The LLM stops searching", f"LLM call {call} ({secs}s): {str(m.content)[:200]}")
    pause(pause_s)


def show_tools(delta: dict, pause_s: float) -> None:
    for m in delta.get("messages", []):
        if not isinstance(m, ToolMessage):
            continue
        art = m.artifact or {}
        if m.name == "find_similar_incidents":
            step(2, "Vector search in pgvector (code, < 1 s)",
                 "Candidates from the analyst's text + extra candidates found only by the LLM queries")
            t = Table(show_lines=False, header_style="bold")
            t.add_column("#", justify="right")
            t.add_column("Incident")
            t.add_column("Company / title")
            t.add_column("Found by")
            t.add_column("Similarity", justify="right")
            for k, r in enumerate(art.get("incidents", []), 1):
                found_by = "[magenta]LLM query (new)[/]" if r.get("found_by") == "llm_query" else "analyst's text"
                t.add_row(str(k), r["incident_id"], f"{r['company']} — {r['title']}"[:52], found_by,
                          f"{r['similarity']:.3f}")
            console.print(t)
        elif m.name == "search_inside_incidents":
            step(4, "Search inside the chosen incidents (code, < 1 s)",
                 "LLM query + fixed 'root cause' query + fixed 'fix / prevention' query, inside each incident")
            for incident_id, passages in art.get("passages_by_incident", {}).items():
                console.print(f"   [bold green]{incident_id}[/]")
                for d in passages:
                    section = d.get("section") or "(no section title)"
                    text = d["content"].replace("\n", " ")
                    if text.startswith("#"):
                        text = text.split(" ", 1)[-1]
                    console.print(f"     • [cyan]{section[:45]}[/]  [dim]({QUERY_SOURCE.get(d.get('query_source'), '')})[/]")
                    console.print(f"       [dim]{text[len(section):][:170].strip()}…[/]")
    pause(pause_s)


def show_findings(delta: dict) -> None:
    step(5, "Output for the Diagnosis Agent (code)", "Structured findings: deepened incidents first, with the reason and the passages")
    t = Table(header_style="bold")
    t.add_column("Incident")
    t.add_column("Company / title")
    t.add_column("Deepened", justify="center")
    t.add_column("Passages", justify="right")
    for r in delta["findings"]:
        t.add_row(r["incident_id"], f"{r['company']} — {r['title']}"[:58], "✅" if r["deepened"] else "",
                  str(len(r["passages"])))
    console.print(t)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("description", nargs="*", help="incident description (default: --example)")
    ap.add_argument("--example", choices=sorted(EXAMPLES), default="tail")
    ap.add_argument("--pause", type=float, default=1.5, help="seconds between steps (for recording)")
    a = ap.parse_args()
    description = " ".join(a.description) or EXAMPLES[a.example]

    agent.enable_hybrid_mode()
    console.print(Panel.fit(
        "[bold]Incident Copilot · Research RAG Agent[/] (hybrid mode)\n"
        "LangGraph · LLM: NVIDIA NIM nemotron-3.5-super-vl · pgvector (2,494 passages, 212 post-mortems)\n\n"
        f"[bold]Analyst:[/] [white]{description}[/]", border_style="cyan"))
    console.print("[dim]loading the embedding model…[/]")
    agent.tools.busca.vetorizar("warm-up")

    start, call = time.time(), 0
    entry = {"description": description, "symptoms": [], "search_request": "", "no_llm": False}
    state: dict = {}
    for part in agent.build_graph().stream(entry, {"recursion_limit": 20}, stream_mode=["updates", "values"],
                                           version="v2"):
        if part["type"] == "values":
            state = part["data"]
            continue
        for node, delta in part["data"].items():
            delta = delta or {}
            if node == "agent":
                call += len(delta.get("llm_calls", [])) or 1
                show_agent(delta, call, a.pause)
            elif node == "tools":
                show_tools(delta, a.pause)
            elif node == "build_findings":
                show_findings(delta)

    console.print()
    console.print(Panel.fit(
        f"[bold]Total:[/] {time.time() - start:.0f}s · {len(state.get('llm_calls', []))} LLM calls · "
        f"{len(state.get('search_log', []))} database searches", border_style="green"))


if __name__ == "__main__":
    main()
