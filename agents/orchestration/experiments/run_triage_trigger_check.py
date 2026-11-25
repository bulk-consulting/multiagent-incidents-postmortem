"""
Does the Triage agent (agents/triage, with the trigger question) ask about recent changes only when it should,
and list every change the analyst mentions (triggers)?

For each reworded case (scenario B of the Triage run): the first message alone (no change mentioned → it should
ask) and the whole conversation (the analyst already answered → it should not ask again).

Usage (from the repository root):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_triage_trigger_check.py [--cases DAN-018,...]
Output: agents/orchestration/experiments/results/triage_trigger_check_<date>.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from agents.orchestration.experiments.run_diagnosis_cases import CASES, TRIAGE_RUN  # noqa: E402
from agents.triage.agent import run_agent  # noqa: E402

CHANGE_WORDS = re.compile(r"chang|deploy|before|recent|update|release|migration|mudan|alter", re.I)


def conversation(case_id):
    for r in json.loads(TRIAGE_RUN.read_text()):
        if r["case"] == case_id and r["scenario"] == "B" and r["round"] == 1 and r["turns"]:
            return r["turns"][0]["description"], r["turns"][-1]["description"]
    raise LookupError(case_id)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=",".join(CASES))
    a = ap.parse_args()
    out = HERE / "results" / f"triage_trigger_check_{datetime.now():%Y-%m-%d_%H%M}.json"
    rows = []
    for case_id in a.cases.split(","):
        first, full = conversation(case_id)
        for kind, text in (("first message", first), ("whole conversation", full)):
            row = {"case": case_id, "input": kind, "text": text}
            try:
                result, _ = run_agent(text)
                asks_change = any(CHANGE_WORDS.search(q) for q in result.missing_information)
                row.update({"enough_information": result.enough_information, "questions": result.missing_information,
                            "asks_about_changes": asks_change, "triggers": result.triggers,
                            "affected_service": result.affected_service})
            except Exception as e:  # record it and go on
                row["error"] = f"{type(e).__name__}: {str(e)[:200]}"
            rows.append(row)
            out.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
            print(f"{case_id} [{kind}] " + (row.get("error") or
                  f"enough={row['enough_information']} asks_changes={row['asks_about_changes']} "
                  f"triggers={row['triggers']} questions={row['questions']}"), flush=True)
    print(f"\nsaved to {out}")


if __name__ == "__main__":
    main()
