"""Run the agent with ONE message and show everything that happened. Good for studying.

It calls the model 2 or 3 times, so it takes a few minutes.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_agent_loop
    .venv/Scripts/python.exe -m agents.triage.tests.test_agent_loop "your own message here"
"""
import sys
import time

from agents.triage.agent import run_agent
from agents.triage.routing import next_step

# The Windows console cannot print some characters the model writes (like special hyphens).
sys.stdout.reconfigure(encoding="utf-8")

DEFAULT_MESSAGE ="Since the deploy this afternoon the checkout page is returning 500 errors."
message = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MESSAGE

print(f"analyst: {message}")
print("running the agent (a few minutes)...")
start = time.time()
result, messages = run_agent(message)
print(f"done in {time.time() - start:.0f}s")

# 1) The messages history: the memory of the agent, step by step.
print("\n--- messages history at the end ---")
for item in messages[1:]:  # skip the long system prompt
    if item.get("tool_calls"):
        calls = [(c["function"]["name"], c["function"]["arguments"]) for c in item["tool_calls"]]
        text = f"(asks for tool: {calls})"
    else:
        text = item["content"]
    print(f"{item['role']:>9}: {text[:400]}")

# 2) The validated answer.
print("\n--- triage result ---")
print(result.model_dump_json(indent=2))

# 3) What the code decides to do next.
print(f"\nnext step (decided in code): {next_step(result)}")
