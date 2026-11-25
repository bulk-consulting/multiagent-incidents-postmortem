"""
Search-only test (no LLM) with the post-mortem cases: for each text that could go to the Research agent's code
search, in which position does the right post-mortem appear (top 20)?

Texts per case (from the Triage scenario runs):
    first     the vague first message of the conversation (floor)
    concat0   conversation glued as in the E5 contract, Triage WITHOUT the trigger question (3 rounds)
    concat1   conversation glued, Triage WITH the trigger question (3 rounds)
    st0       search_text written by the Triage agent, WITHOUT the trigger question (3 rounds)
    st1       search_text written by the Triage agent, WITH the trigger question (3 rounds)
    complete  the operator's complete message (ceiling)

The database search is deterministic. The LLM's choice is not measured here.

Usage (from the repository root):
    multiagent_env/bin/python -I agents/orchestration/experiments/retrieval_scenarios.py
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from agents.orchestration.experiments.run_triage_scenarios import load_case  # noqa: E402
from agents.research import tools  # noqa: E402

RES = HERE / "results"
RUN_NO_TRIGGER = RES / "triage_scenarios_2026-11-23_1934.json"
RUN_TRIGGER_REWRITE = RES / "triage_scenarios_2026-11-23_2116_ask-trigger_rewrite.json"  # reworded cases
RUN_TRIGGER = RES / "triage_scenarios_2026-11-23_2024_ask-trigger.json"  # 12 cases (the 1946 run had only the first 5)
CASES = ["DAN-104", "DAN-145", "DAN-211", "DAN-125", "DAN-018", "DAN-017", "DAN-116", "DAN-164",
         "DAN-004", "DAN-121", "DAN-154", "DAN-197"]  # the last 4 have no trigger known during the incident
TOP = 20


def position(text, case_id):
    ids = [r["incident_id"] for r in tools.search_incidents(text, TOP, 1)]
    return ids.index(case_id) + 1 if case_id in ids else 0  # 0 = not in the top 20


def texts_from(run_file, case_id):
    """(glued conversation, search_text) of each round of scenario B."""
    out = []
    for r in json.loads(run_file.read_text()):
        if r["case"] == case_id and r["scenario"] == "B" and r["turns"]:
            last = r["turns"][-1]
            out.append((last["description"], last["result"]["search_text"]))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rewrite", action="store_true", help="reworded cases (DAN-xxx_rewrite.json and their Triage run)")
    a = ap.parse_args()
    tools.busca.vetorizar("warm-up")
    rows = []
    for case_id in CASES:
        case = load_case(case_id, a.rewrite)
        no_t = [] if a.rewrite else texts_from(RUN_NO_TRIGGER, case_id)
        with_t = texts_from(RUN_TRIGGER_REWRITE if a.rewrite else RUN_TRIGGER, case_id)
        row = {"case": case_id,
               "first": [position(case["conversation"][0]["analyst"], case_id)],
               "concat0": [position(c, case_id) for c, _ in no_t],
               "concat1": [position(c, case_id) for c, _ in with_t],
               "st0": [position(s, case_id) for _, s in no_t],
               "st1": [position(s, case_id) for _, s in with_t],
               "complete": [position(case["complete_message"], case_id)]}
        rows.append(row)
    cols = ["first", "concat0", "concat1", "st0", "st1", "complete"]
    print(f"position of the right post-mortem in the top {TOP} (0 = not there; one number per Triage round)\n")
    print(f"{'case':8} " + " ".join(f"{c:>12}" for c in cols))
    for r in rows:
        print(f"{r['case']:8} " + " ".join(f"{'/'.join(map(str, r[c])):>12}" for c in cols))
    print("\nin the top 10 (all rounds together):")
    for c in cols:
        vals = [v for r in rows for v in r[c]]
        print(f"  {c:9} {sum(1 for v in vals if 0 < v <= 10)}/{len(vals)}")
    out = RES / f"retrieval_scenarios_{datetime.now():%Y-%m-%d_%H%M}{'_rewrite' if a.rewrite else ''}.json"
    out.write_text(json.dumps(rows, indent=1))
    print(f"\nsaved to {out}")


if __name__ == "__main__":
    main()
