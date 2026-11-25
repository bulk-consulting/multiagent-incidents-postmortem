"""
Test 1 of the Triage output proposal: the same Triage agent (Mari's loop, prompt and tool) with two NEW
fields in the answer, without changing agents/triage:

    trigger           what happened right before the problem (a deploy, a command, a config or data change...)
    incident_summary  the whole incident in 1-2 English sentences, written for the search

Why: in the run of 2026-11-23 (triage_2026-11-23_1639.json) the symptoms lost the trigger and the cause hints
("an operator ran a command to remove servers", "certificate expired", "leap second", "we downsized the
database"), which are what tell one incident from another.

This script swaps the prompt and the schema of agents.triage.agent only while it runs. Everything else
(the loop, the tool, the two rules in code) is Mari's code.

Usage (from the repository root):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_triage_v2.py [--questions q01,q-022]
Output: agents/orchestration/experiments/results/triage_v2_<date>.json
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
from agents.triage.routing import next_step  # noqa: E402
from agents.triage.schema import TriageResult  # noqa: E402
from rag import limite_llm  # noqa: E402

QUESTION_FILES = [ROOT / "rag/avaliacao/perguntas.json", ROOT / "agents/research/experiments/questions_hard.json"]


# ---------------------------------------------------------------- the proposed output

class TriageResultV2(TriageResult):
    """Mari's TriageResult plus two fields."""

    trigger: Optional[str] = None   # what happened right before the problem, as the analyst said it; None if not said
    incident_summary: str           # the whole incident in 1-2 English sentences, for the search


def parse_triage_answer_v2(text):
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end < start:
        raise ValueError("the answer does not contain a JSON object")
    return TriageResultV2.model_validate_json(text[start : end + 1])


OLD_EXAMPLE = triage_prompts.EXAMPLE_ANSWER
NEW_EXAMPLE = json.dumps(
    {
        **json.loads(OLD_EXAMPLE),
        "trigger": "the search index was rebuilt this morning",
        "incident_summary": "Search requests time out and the error rate is above 20% since the search index "
                            "was rebuilt this morning.",
    },
    indent=2,
)
NEW_RULES = """
- trigger: what happened right before the problem started, in English, as the analyst said it: for example a
  deploy, a command someone ran, a configuration or data change, a capacity change, an expired certificate,
  a time event. null if the analyst does not mention any. Do not guess a trigger.
- incident_summary: one or two sentences in English describing the whole incident: what is failing, where,
  the trigger and the timing, and how far it spreads. Use only what the analyst said: do not add causes,
  names or details that are not in the message. Write it even when enough_information is false.
"""
assert OLD_EXAMPLE in triage_prompts.SYSTEM_PROMPT
SYSTEM_PROMPT_V2 = triage_prompts.SYSTEM_PROMPT.replace(OLD_EXAMPLE, NEW_EXAMPLE).rstrip() + "\n" + NEW_RULES

# swap only while this script runs
triage_agent.SYSTEM_PROMPT = SYSTEM_PROMPT_V2
triage_agent.parse_triage_answer = parse_triage_answer_v2
_original_chat = triage_agent.chat
triage_agent.chat = lambda messages, tools=None, max_tokens=2048: limite_llm.chamar(
    lambda: _original_chat(messages, tools=tools, max_tokens=max_tokens), aviso="triage v2")


def tool_calls_in(messages):
    return [(c["function"]["name"], c["function"]["arguments"]) for m in messages for c in m.get("tool_calls", [])]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--questions", help="e.g. q01,q-022 (default: all 32)")
    a = ap.parse_args()
    questions = []
    for f in QUESTION_FILES:
        for q in json.loads(f.read_text())["perguntas"]:
            questions.append({**q, "source_file": f.name})
    if a.questions:
        wanted = set(a.questions.split(","))
        questions = [q for q in questions if q["id"] in wanted]

    out = HERE / "results" / f"triage_v2_{datetime.now():%Y-%m-%d_%H%M}.json"
    out.parent.mkdir(exist_ok=True)
    results, start = [], time.time()
    for n, q in enumerate(questions, 1):
        t = time.time()
        row = {"id": q["id"], "source_file": q["source_file"], "question": q["pergunta"],
               "expected": sorted(set(q.get("esperado", [])) | set(q.get("aceitos", []))),
               "initial_search_position": q.get("posicao_busca_inicial")}
        try:
            result, messages = triage_agent.run_agent(q["pergunta"])
            row.update({"next_step": next_step(result), "triage_result": result.model_dump(),
                        "tool_calls": tool_calls_in(messages),
                        "model_calls": sum(m["role"] == "assistant" for m in messages)})
        except Exception as e:
            row["error"] = f"{type(e).__name__}: {str(e)[:300]}"
        row["seconds"] = round(time.time() - t, 1)
        results.append(row)
        out.write_text(json.dumps(results, ensure_ascii=False, indent=1))
        elapsed = time.time() - start
        r = row.get("triage_result") or {}
        status = row.get("error", "")[:60] or f"{row['next_step']} · trigger: {r.get('trigger')}"
        print(f"progress: {n}/{len(questions)} · {elapsed / 60:.1f} min · ~{elapsed / n * (len(questions) - n) / 60:.0f} min left"
              f" · {q['id']}: {status}"[:300], flush=True)
    steps = {}
    for r in results:
        steps[r.get("next_step", "error")] = steps.get(r.get("next_step", "error"), 0) + 1
    print(f"total: {time.time() - start:.0f}s · {steps}")
    print(f"saved to {out}")


if __name__ == "__main__":
    main()
