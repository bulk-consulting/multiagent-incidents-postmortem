"""Run the Reporting agent on ONE simulated input and show everything, to study how it works.

It prints the messages history (what the model read and wrote), the structured report, and the message
that the frontend would show. It calls the model for real, so it takes some seconds.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.reporting.tests.test_agent_loop                       (default input)
    .venv/Scripts/python.exe -m agents.reporting.tests.test_agent_loop inconclusive_weak_evidence

The inputs are in agents/reporting/tests/fixtures/ (names in fixtures.py).
"""
import sys

from agents.reporting.agent import run_reporting_agent
from agents.reporting.tests.fixtures import NAMES, load_fixture

# The Windows console cannot print some characters the model writes.
sys.stdout.reconfigure(encoding="utf-8")

name = sys.argv[1] if len(sys.argv) > 1 else NAMES[0]
if name not in NAMES:
    sys.exit(f"No input called {name!r}. Available: {NAMES}")

state = load_fixture(name)
print(f"input: {name}")
print(f"analyst: {state['description']}")
print("running the agent...")

report, messages, attempts, problems = run_reporting_agent(state)

# 1) The messages history: what the model read, and what it answered.
print("\n--- messages history at the end ---")
for number, item in enumerate(messages, 1):
    text = item["content"]
    shown = text if len(text) < 500 else text[:500] + f"... ({len(text)} characters)"
    print(f"{number}. [{item['role']}] {shown}\n")

# 2) The structured report.
print("--- the report (structured) ---")
print(report.model_dump_json(indent=2))

# 3) The message for the frontend.
print("\n--- the message for the chat ---")
print(report.message)

print(f"\nattempts: {attempts}   problems left: {problems or 'none'}")
