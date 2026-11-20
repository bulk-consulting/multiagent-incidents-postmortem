"""Run the agent with ONE message and show everything that happened. Good for studying.

It calls the model 2 or 3 times, so it takes a few minutes.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_agent_loop
    .venv/Scripts/python.exe -m agents.triage.tests.test_agent_loop "your own message here"
"""
import json
import sys
import time

from rich.console import Console
from rich.markup import escape

from agents.triage.agent import run_agent
from agents.triage.routing import next_step

# The Windows console cannot print some characters the model writes (like special hyphens).
sys.stdout.reconfigure(encoding="utf-8")

# Force ANSI colors: on Windows rich falls back to the old console mode and Git Bash shows no colors.
console = Console(force_terminal=True, color_system="truecolor", legacy_windows=False, highlight=False)

ROLE_COLORS = {"user": "bold green", "assistant": "bold magenta", "tool": "bold yellow"}

DEFAULT_MESSAGE ="Since the deploy this afternoon the login page is returning error 500."
message = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MESSAGE

console.print(f"[bold green]analyst:[/] {escape(message)}")
console.print("[dim]running the agent (a few minutes)...[/]")
start = time.time()
result, messages = run_agent(message)
console.print(f"[dim]done in {time.time() - start:.0f}s[/]")

# 1) The messages history: the memory of the agent, step by step.
console.rule("[bold cyan]messages history at the end")
for item in messages[1:]:  # skip the long system prompt
    role = item["role"]
    color = ROLE_COLORS.get(role, "bold white")
    console.print(f"[{color}]{role:>9}:[/] ", end="")
    if item.get("tool_calls"):
        calls = [(c["function"]["name"], c["function"]["arguments"]) for c in item["tool_calls"]]
        console.print(f"[yellow](asks for tool: {escape(str(calls))})[/]")
        continue
    text = item["content"] or ""
    try:
        console.print_json(text)  # JSON answers get colors
    except (json.JSONDecodeError, TypeError):
        console.print(escape(text[:400]))

# 2) The validated answer.
console.rule("[bold cyan]triage result")
console.print_json(result.model_dump_json())

# 3) What the code decides to do next.
console.print(f"\n[bold]next step (decided in code):[/] [bold black on green] {next_step(result)} [/]")
