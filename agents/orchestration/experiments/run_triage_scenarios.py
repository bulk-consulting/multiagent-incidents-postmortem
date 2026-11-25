"""
Triage test with real post-mortems (agents/orchestration/experiments/postmortems/DAN-xxx.json, prepared by an
external LLM from the full post-mortem texts): two scenarios for each case.

    A  complete message: the operator's complete_message, once
    B  conversation: the vague first message; whenever the Triage agent asks for more information
       (ask_user), a simulated analyst answers with the script items that match the questions, the answer is
       added to the description as in the E5 contract ("Analyst answer: ..."), and the Triage agent runs again
       (at most MAX_ANSWERS answers)

The simulated analyst matches questions to the script by keywords (reproducible). If no question matches, it
answers with the "affected service" item.

The Triage agent is Mari's loop, prompt and tool, with an experimental output (swapped only while this runs):
    trigger      what happened right before the problem, as the analyst said it; null if not said
    search_text  the whole incident in 1-3 English sentences, written for the search of the Research agent

Usage (from the repository root):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_triage_scenarios.py --cases DAN-104 [--rounds 3]
Output: agents/orchestration/experiments/results/triage_scenarios_<date>.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import agents.triage.agent as triage_agent  # noqa: E402
from agents.triage import prompts as triage_prompts  # noqa: E402
from agents.triage.routing import ASK_USER, next_step  # noqa: E402
from agents.triage.schema import TriageResult  # noqa: E402
from rag import limite_llm  # noqa: E402

CASES_DIR = HERE / "postmortems"
MAX_ANSWERS = 3


# ---------------------------------------------------------------- experimental Triage output

class TriageResultExp(TriageResult):
    trigger: Optional[str] = None
    search_text: str


def parse_exp(text):
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end < start:
        raise ValueError("the answer does not contain a JSON object")
    return TriageResultExp.model_validate_json(text[start : end + 1])


OLD_EXAMPLE = triage_prompts.EXAMPLE_ANSWER
NEW_EXAMPLE = json.dumps(
    {**json.loads(OLD_EXAMPLE),
     "trigger": "we rebuilt the search index this morning",
     "search_text": "Our search requests time out and the error rate is above 20% since we rebuilt the search "
                    "index this morning."},
    indent=2,
)
NEW_RULES = """
- trigger: what happened right before the problem started, in English, as the analyst said it: for example a
  deploy, a command someone ran, a configuration or data change, a capacity change, an expired certificate,
  a time event. null if the analyst does not mention any. Do not guess a trigger.
- search_text: one to three sentences in English describing the whole incident with everything the analyst
  said in all their messages: what is failing, where, the trigger and the timing, and how far it spreads.
  Keep the analyst's point of view ("our", "we"). Describe only the incident: do not comment on what is
  missing, do not add causes, names or details that the analyst did not give. Write it even when
  enough_information is false.
"""
assert OLD_EXAMPLE in triage_prompts.SYSTEM_PROMPT
triage_agent.SYSTEM_PROMPT = triage_prompts.SYSTEM_PROMPT.replace(OLD_EXAMPLE, NEW_EXAMPLE).rstrip() + "\n" + NEW_RULES
triage_agent.parse_triage_answer = parse_exp
_original_chat = triage_agent.chat
triage_agent.chat = lambda messages, tools=None, max_tokens=2048: limite_llm.chamar(
    lambda: _original_chat(messages, tools=tools, max_tokens=max_tokens), aviso="triage")


# Variant (--ask-trigger): the Triage agent also asks, once, whether anything changed right before the problem.
ASK_TRIGGER_RULE = """
- Recent change: if no analyst message says anything about recent changes, ask ONCE whether anything changed
  right before the problem started (a deploy, a command, a configuration or data change, a migration): set
  enough_information=false and add that question to missing_information, together with any other question.
  The analyst HAS ALREADY ANSWERED, so do NOT ask, when any message says something like: "we haven't identified
  a trigger", "we don't know what changed", "nothing changed", "we haven't changed it in months", "we are
  investigating recent deployments". An uncertain answer is still an answer: never ask about changes twice.
"""


# ---------------------------------------------------------------- simulated analyst

TOPICS = ["service", "trigger", "timing", "symptoms"]  # conversation[1..4], in the order of the script
KEYWORDS = {
    "service": ["service", "system", "component", "application", "product", "which", "name", "platform"],
    "trigger": ["change", "deploy", "before", "recent", "trigger", "update", "release", "maintenance",
                "command", "migration", "upgrade", "config"],
    "timing": ["when", "start", "since", "time", "who", "how many", "users", "customers", "scope", "region",
               "impact", "affect"],
    "symptoms": ["error", "symptom", "message", "log", "code", "behavior", "behaviour", "see", "metric",
                 "status", "latency", "fail", "observ"],
}


def load_case(case_id, rewrite=False):
    """rewrite=True reads DAN-xxx_rewrite.json: the same facts reworded without the post-mortem's vocabulary."""
    text = (CASES_DIR / f"{case_id}{'_rewrite' if rewrite else ''}.json").read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError:  # file with the prompt pasted before the answer: take the last JSON object
        return json.loads(text[text.rindex("\n{"):])


def answer_for(questions, conversation):
    """The script items that match the Triage agent's questions (all matching topics, in the script order)."""
    script = {topic: conversation[k + 1]["analyst"] for k, topic in enumerate(TOPICS)}
    text = " ".join(questions).lower()
    matched = [t for t in TOPICS if any(w in text for w in KEYWORDS[t])]
    if not matched:
        matched = ["service"]
    return " ".join(script[t] for t in matched), matched


# ---------------------------------------------------------------- scenarios

def run_triage(description):
    t = time.time()
    result, messages = triage_agent.run_agent(description)
    return {"description": description, "next_step": next_step(result), "result": result.model_dump(),
            "tool_calls": [(c["function"]["name"], c["function"]["arguments"])
                           for m in messages for c in m.get("tool_calls", [])],
            "seconds": round(time.time() - t, 1)}


def scenario_a(case):
    return {"turns": [run_triage(case["complete_message"])]}


def scenario_b(case):
    description = case["conversation"][0]["analyst"]
    turns = []
    for _ in range(MAX_ANSWERS + 1):
        turn = run_triage(description)
        turns.append(turn)
        if turn["next_step"] != ASK_USER or len(turns) > MAX_ANSWERS:
            break
        answer, topics = answer_for(turn["result"]["missing_information"], case["conversation"])
        turn["analyst_answer"], turn["answer_topics"] = answer, topics
        description = f"{description}\n\nAnalyst answer: {answer}"
    return {"turns": turns}


def show(case_id, name, run):
    print(f"\n{'=' * 100}\n{case_id} · scenario {name}\n{'=' * 100}")
    for k, t in enumerate(run["turns"], 1):
        r = t["result"]
        print(f"--- triage run {k} ({t['seconds']}s) → {t['next_step']}")
        if k == 1 or name == "A":
            print(f"    input: {t['description'][:400]}")
        print(f"    symptoms: {r['symptoms']}")
        print(f"    service: {r['affected_service']} | category: {r['category']} | trigger: {r['trigger']}")
        print(f"    search_text: {r['search_text']}")
        if r["missing_information"]:
            print(f"    asks: {r['missing_information']}")
        if t.get("analyst_answer"):
            print(f"    analyst answers ({', '.join(t['answer_topics'])}): {t['analyst_answer']}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default="DAN-104,DAN-145,DAN-211,DAN-125,DAN-018")
    ap.add_argument("--rounds", type=int, default=1)
    ap.add_argument("--scenarios", default="A,B")
    ap.add_argument("--rewrite", action="store_true", help="use DAN-xxx_rewrite.json (reworded cases)")
    ap.add_argument("--ask-trigger", action="store_true", help="variant: the Triage agent asks once about recent changes")
    a = ap.parse_args()
    if a.ask_trigger:
        triage_agent.SYSTEM_PROMPT = triage_agent.SYSTEM_PROMPT.rstrip() + "\n" + ASK_TRIGGER_RULE
    suffix = ("_ask-trigger" if a.ask_trigger else "") + ("_rewrite" if a.rewrite else "")
    out = HERE / "results" / f"triage_scenarios_{datetime.now():%Y-%m-%d_%H%M}{suffix}.json"
    results = []
    for rnd in range(1, a.rounds + 1):
        for case_id in a.cases.split(","):
            case = load_case(case_id, a.rewrite)
            for name in a.scenarios.split(","):
                try:
                    run = scenario_a(case) if name == "A" else scenario_b(case)
                except Exception as e:  # record it and go on
                    run = {"error": f"{type(e).__name__}: {str(e)[:300]}", "turns": []}
                run.update({"case": case_id, "scenario": name, "round": rnd})
                results.append(run)
                out.write_text(json.dumps(results, ensure_ascii=False, indent=1))
                if run.get("error"):
                    print(f"\n{case_id} · scenario {name} · ERROR: {run['error']}")
                else:
                    show(case_id, name, run)
    print(f"\nsaved to {out}")


if __name__ == "__main__":
    main()
