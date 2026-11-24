"""
Step 1 of the Triage → Research experiment: runs the Triage agent ONCE on the 32 test questions
(12 E3 questions + 20 hard ones) and saves what it returns, so that step 2 can give the same symptoms to
the three Research modes (a fair comparison: the Triage agent uses the LLM and could answer differently
each time).

The questions were written to test the search, not as analyst messages, so some may be stopped by the
Triage agent (ask_user). This step shows how many, and whether the symptoms make sense.

The Triage agent's model calls go through rag/limite_llm.py (calls per minute + long waits on HTTP 429),
without changing Mari's code: this script wraps agents.triage.agent.chat.

Usage (from the repository root):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_triage.py [--questions q01,q-012]
Output: agents/orchestration/experiments/results/triage_<date>.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import agents.triage.agent as triage_agent  # noqa: E402
from agents.triage.routing import next_step  # noqa: E402
from rag import limite_llm  # noqa: E402

QUESTION_FILES = [ROOT / "rag/avaliacao/perguntas.json", ROOT / "agents/research/experiments/questions_hard.json"]

_original_chat = triage_agent.chat


def _chat_with_limit(messages, tools=None, max_tokens=2048):
    return limite_llm.chamar(lambda: _original_chat(messages, tools=tools, max_tokens=max_tokens), aviso="triage")


triage_agent.chat = _chat_with_limit  # every call of run_agent() now respects the rate limit


def tool_calls_in(messages):
    return [(c["function"]["name"], c["function"]["arguments"]) for m in messages for c in m.get("tool_calls", [])]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--questions", help="e.g. q01,q-012 (default: all 32)")
    a = ap.parse_args()
    questions = []
    for f in QUESTION_FILES:
        for q in json.loads(f.read_text())["perguntas"]:
            questions.append({**q, "source_file": f.name})
    if a.questions:
        wanted = set(a.questions.split(","))
        questions = [q for q in questions if q["id"] in wanted]

    out = HERE / "results" / f"triage_{datetime.now():%Y-%m-%d_%H%M}.json"
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
        except Exception as e:  # record it and go on
            row["error"] = f"{type(e).__name__}: {str(e)[:300]}"
        row["seconds"] = round(time.time() - t, 1)
        results.append(row)
        out.write_text(json.dumps(results, ensure_ascii=False, indent=1))  # saved after every question
        elapsed = time.time() - start
        status = row.get("error", "")[:60] or f"{row['next_step']} · symptoms: {row['triage_result']['symptoms']}"
        print(f"progress: {n}/{len(questions)} · {elapsed / 60:.1f} min · ~{elapsed / n * (len(questions) - n) / 60:.0f} min left"
              f" · {q['id']}: {status}"[:300], flush=True)
    steps = {}
    for r in results:
        steps[r.get("next_step", "error")] = steps.get(r.get("next_step", "error"), 0) + 1
    print(f"total: {time.time() - start:.0f}s · {steps}")
    print(f"saved to {out}")


if __name__ == "__main__":
    main()
