"""The triage agent: an LLM that can use a tool, inside a loop.

run_agent(user_message) returns two things:
  - the TriageResult (the validated answer),
  - the full messages history (useful to see what happened step by step).
"""
import json

from agents.triage.llm import chat
from agents.triage.prompts import SYSTEM_PROMPT, build_system_prompt
from agents.triage.schema import parse_triage_answer
from agents.triage.tools import TOOLS, clean_tool_name, run_tool

MAX_TURNS = 5  # the code, not the model, decides the maximum number of loops


def set_trigger_policy(policy):
    """Choose when the agent asks about recent changes: "B" (default) or "A" (see agents/triage/prompts.py)."""
    global SYSTEM_PROMPT
    SYSTEM_PROMPT = build_system_prompt(policy)


def open_investigation_ids(messages):
    """The ids of the OPEN investigations that the tool returned during this run."""
    ids = set()
    for message in messages:
        if message["role"] != "tool":
            continue
        data = json.loads(message["content"])
        # An error result is also a dict, but it has no "investigations" key.
        for item in data.get("investigations", []):
            if item["status"] == "open":
                ids.add(item["incident_id"])
    return ids


def check_related_incident(result, messages):
    """The related incident must be a real, open investigation returned by the tool.
    This stops the model from inventing an id. Raises ValueError if it is not."""
    if result.related_incident is None:
        return
    allowed = open_investigation_ids(messages)
    if result.related_incident.incident_id not in allowed:
        raise ValueError(
            f"related_incident must be one of the open investigations returned by "
            f"the tool: {sorted(allowed)}. If none of them is the same problem, use null."
        )


def check_tool_was_used(result, messages):
    """If there is enough information, the agent must check the investigations first.
    Without this rule the model sometimes answers directly and misses a duplicate.
    Raises ValueError if the tool was not used."""
    tool_was_used = any(message["role"] == "tool" for message in messages)
    if result.enough_information and not tool_was_used:
        raise ValueError(
            "enough_information is true, so you must first call list_investigations "
            "to check whether the problem is already being investigated."
        )


def run_agent(user_message):
    # The messages history: this is the agent's memory during one run.
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    for _ in range(MAX_TURNS):
        reply = chat(messages, tools=TOOLS)
        tool_calls = reply.get("tool_calls")

        # The model asked for a tool.
        if tool_calls:
            # Save its request in the list...
            for call in tool_calls:
                call["function"]["name"] = clean_tool_name(call["function"]["name"])
            messages.append(
                {"role": "assistant", "content": reply.get("content") or "", "tool_calls": tool_calls}
            )
            # ...run each tool and add the result to the list. Then the loop calls the model again.
            for call in tool_calls:
                result = run_tool(call["function"]["name"], call["function"]["arguments"])
                messages.append(
                    {"role": "tool", "tool_call_id": call["id"], "content": json.dumps(result)}
                )
            continue

        # No tool requested: the model gave its final answer. Check it.
        text = reply.get("content") or ""
        messages.append({"role": "assistant", "content": text})
        try:
            result = parse_triage_answer(text)
            check_tool_was_used(result, messages)
            check_related_incident(result, messages)
            return result, messages
        except ValueError as error:
            # Not valid: tell the model what is wrong and let it try again.
            messages.append(
                {
                    "role": "user",
                    "content": f"Your answer is not valid: {error}\n"
                    "Fix it. Your final answer must be only the JSON object.",
                }
            )

    raise RuntimeError(f"The agent did not produce a valid answer in {MAX_TURNS} turns")
