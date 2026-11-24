"""
Search-only test (no LLM): for the questions the Triage agent sent to research, is the expected incident among
the 10 candidates of the code search, and in which position, for different ways of using the symptoms?

    E  message only (baseline; also the guaranteed search of the hybrid mode)
    A  message + one search per symptom, merged by the highest similarity (normal mode today)
    B  message + one search with all symptoms joined, merged by the highest similarity
    C  one search with the message and the joined symptoms in the same text (no merge)
    D  the 10 of the message always stay; the joined-symptoms search only adds up to 5 new incidents
    F  the incident_summary of the Triage v2 run, alone

The database search is deterministic, so one run is enough. The LLM's choice is not measured here.

Usage (from the repository root):
    multiagent_env/bin/python -I agents/orchestration/experiments/retrieval_variants.py
Output: agents/orchestration/experiments/results/retrieval_variants_<date>.json (+ table on the screen)
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from agents.research import agent, tools  # noqa: E402

TRIAGE = HERE / "results" / "triage_2026-11-23_1639.json"
TRIAGE_V2 = HERE / "results" / "triage_v2_2026-11-23_1730.json"
N = 10
EXTRA = 5


def search(query):
    return tools.search_incidents(query, N, 2)


def merged(queries):
    return [r["incident_id"] for r in agent._merge_by_incident([search(q) for q in queries])[:N]]


def variants(message, symptoms, summary):
    joined = "; ".join(symptoms)
    msg = [r["incident_id"] for r in search(message)]
    out = {"E": msg}
    out["A"] = merged([message, *symptoms]) if symptoms else msg
    out["B"] = merged([message, joined]) if symptoms else msg
    out["C"] = [r["incident_id"] for r in search(f"{message} {joined}")] if symptoms else msg
    if symptoms:
        extra = [r["incident_id"] for r in search(joined) if r["incident_id"] not in msg][:EXTRA]
        out["D"] = msg + extra
    else:
        out["D"] = msg
    out["F"] = [r["incident_id"] for r in search(summary)] if summary else None
    return out


def position(ids, expected):
    if ids is None:
        return None
    hits = [k for k, i in enumerate(ids, 1) if i in expected]
    return hits[0] if hits else 0  # 0 = not among the candidates


def main() -> None:
    v1 = [x for x in json.loads(TRIAGE.read_text()) if x.get("next_step") == "go_to_research"]
    v2 = {x["id"]: x for x in json.loads(TRIAGE_V2.read_text())}
    tools.busca.vetorizar("warm-up")
    rows = []
    for x in v1:
        if not x["expected"]:
            continue
        expected = set(x["expected"])
        summary = (v2.get(x["id"], {}).get("triage_result") or {}).get("incident_summary")
        lists = variants(x["question"], x["triage_result"]["symptoms"], summary)
        rows.append({"id": x["id"], "expected": sorted(expected), "symptoms": x["triage_result"]["symptoms"],
                     "positions": {k: position(v, expected) for k, v in lists.items()}, "lists": lists})
    names = ["E", "A", "B", "C", "D", "F"]
    print("position of the expected incident among the candidates (0 = not there; D has up to 15 candidates)")
    print("id      " + "  ".join(f"{n:>3}" for n in names))
    for r in rows:
        print(f"{r['id']:7} " + "  ".join(f"{('-' if r['positions'][n] is None else r['positions'][n]):>3}" for n in names))
    print("found  " + "  ".join(f"{sum(1 for r in rows if r['positions'][n]):>3}" for n in names), f"(of {len(rows)})")
    out = HERE / "results" / f"retrieval_variants_{datetime.now():%Y-%m-%d_%H%M}.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
    print(f"saved to {out}")


if __name__ == "__main__":
    main()
