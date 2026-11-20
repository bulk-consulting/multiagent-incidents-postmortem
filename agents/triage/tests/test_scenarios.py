"""Test: does the agent make the right decisions in different situations?

Each scenario is an analyst message plus what we expect. It calls the model for real,
so each scenario takes a few minutes (the free NIM plan is slow).

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_scenarios                 (all scenarios)
    .venv/Scripts/python.exe -m agents.triage.tests.test_scenarios vague duplicate (only these)

The test investigations are in agents/triage/data/investigations.json:
    INC-041 payments-api (open)   INC-042 login (open)
    INC-043 batch-jobs (closed)   INC-044 search (open)
"""
import sys
import time

from agents.triage.agent import run_agent
from agents.triage.routing import ASK_USER, GO_TO_RESEARCH, TELL_RELATED_INCIDENT, next_step
from agents.triage.tests.checks import Checker

# The Windows console cannot print some characters the model writes (like special hyphens).
sys.stdout.reconfigure(encoding="utf-8")

# For each scenario:
#   message      what the analyst writes
#   next_step    what the code should decide after the agent
#   related_id   the investigation that should be found (None = none)
#   uses_tool    should the agent call list_investigations?
SCENARIOS = [
    {
        "name": "duplicate",
        "message": "Since the deploy this afternoon the login page is returning error 500.",
        "next_step": TELL_RELATED_INCIDENT,
        "related_id": "INC-042",
        "uses_tool": True,
    },
    {
        "name": "duplicate_in_portuguese",
        "message": "A página de login está retornando erro 500 desde o deploy das 14h.",
        "next_step": TELL_RELATED_INCIDENT,
        "related_id": "INC-042",
        "uses_tool": True,
    },
    {
        "name": "new_problem",
        "message": "Our recommendations service returns empty lists since this morning. There are no errors in the logs.",
        "next_step": GO_TO_RESEARCH,
        "related_id": None,
        "uses_tool": True,
    },
    {
        "name": "same_service_different_problem",
        "message": "The login page loads very slowly since this morning, but it does not show any error.",
        "next_step": GO_TO_RESEARCH,
        "related_id": None,
        "uses_tool": True,
    },
    {
        "name": "closed_investigation_is_ignored",
        "message": "The batch-jobs service was killed again last night because it ran out of memory (OOMKilled).",
        "next_step": GO_TO_RESEARCH,
        "related_id": None,
        "uses_tool": True,
    },
    {
        "name": "vague",
        "message": "Something is broken, please help!",
        "next_step": ASK_USER,
        "related_id": None,
        "uses_tool": False,
    },
]


def tool_calls_in(messages):
    """The tool calls the agent made, as (name, arguments) pairs."""
    calls = []
    for item in messages:
        for call in item.get("tool_calls", []):
            calls.append((call["function"]["name"], call["function"]["arguments"]))
    return calls


def run_scenario(scenario, checker):
    print(f"\n=== {scenario['name']}")
    print(f"analyst: {scenario['message']}")

    start = time.time()
    try:
        result, messages = run_agent(scenario["message"])
    except Exception as error:  # the agent could not produce a valid answer
        checker.check(f"{scenario['name']}: the agent finished", False, f"({error})")
        return
    print(f"finished in {time.time() - start:.0f}s")

    calls = tool_calls_in(messages)
    print(f"tool calls: {calls or 'none'}")
    print(result.model_dump_json(indent=2))

    related_id = result.related_incident.incident_id if result.related_incident else None
    step = next_step(result)
    name = scenario["name"]

    # Only the checks that fail show details, so we put the actual values in `detail`.
    checker.check(f"{name}: next step is {scenario['next_step']}", step == scenario["next_step"], f"(got {step})")
    checker.check(f"{name}: related incident is {scenario['related_id']}", related_id == scenario["related_id"], f"(got {related_id})")
    checker.check(f"{name}: tool used = {scenario['uses_tool']}", bool(calls) == scenario["uses_tool"], f"(calls: {calls})")


names = sys.argv[1:]  # optional: run only the scenarios with these names
selected = [s for s in SCENARIOS if not names or s["name"] in names]
if not selected:
    sys.exit(f"No scenario matches {names}. Available: {[s['name'] for s in SCENARIOS]}")

checker = Checker()
for scenario in selected:
    run_scenario(scenario, checker)

print("\n=== SUMMARY")
checker.finish()
