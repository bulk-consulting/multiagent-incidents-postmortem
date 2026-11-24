"""
Diagnosis agent on the reworded post-mortem cases: Triage output (from the Triage run) → Research agent (hybrid)
→ Diagnosis agent. Saves, for each case, what the Diagnosis agent said next to the real root cause of the
post-mortem ("discovered_later" in DAN-xxx_rewrite.json), to be checked by hand.

Usage (from the repository root, database up):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_diagnosis_cases.py --cases DAN-104 [--round 1]
Output: agents/orchestration/experiments/results/diagnosis_cases_<date>.json
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
from agents.diagnosis import agent as diagnosis  # noqa: E402
from agents.diagnosis.schema import parse_diagnosis_answer  # noqa: E402
from agents.orchestration.experiments.run_triage_scenarios import load_case  # noqa: E402
from agents.research import agent as research  # noqa: E402

TRIAGE_RUN = HERE / "results" / "triage_scenarios_2026-11-23_2116_ask-trigger_rewrite.json"
CASES = ["DAN-104", "DAN-145", "DAN-211", "DAN-125", "DAN-018", "DAN-017", "DAN-116", "DAN-164",
         "DAN-004", "DAN-121", "DAN-154", "DAN-197"]


def triage_output(case_id, rnd):
    for r in json.loads(TRIAGE_RUN.read_text()):
        if r["case"] == case_id and r["scenario"] == "B" and r["round"] == rnd and r["turns"]:
            last = r["turns"][-1]
            res = last["result"]
            return last["description"], {k: res.get(k) for k in ("affected_service", "trigger", "symptoms", "category")}
    raise LookupError(f"no Triage run for {case_id} round {rnd}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=",".join(CASES))
    ap.add_argument("--round", type=int, default=1, help="which Triage round to take the conversation from")
    a = ap.parse_args()
    research.enable_hybrid_mode()
    out = HERE / "results" / f"diagnosis_cases_{datetime.now():%Y-%m-%d_%H%M}.json"
    results = []
    for case_id in a.cases.split(","):
        t0 = time.time()
        description, triage = triage_output(case_id, a.round)
        row = {"case": case_id, "round": a.round, "description": description, "triage": triage,
               "real_root_cause": load_case(case_id, rewrite=True)["discovered_later"]["root_cause"]}
        try:
            state = research.research(description, triage["symptoms"])
            findings = state["findings"]
            row["findings"] = [{"id": r["incident_id"], "deepened": r["deepened"], "title": r.get("title")} for r in findings]
            row["right_incident_in_findings"] = any(r["incident_id"] == case_id for r in findings)
            row["right_incident_deepened"] = any(r["incident_id"] == case_id and r["deepened"] for r in findings)
            result, messages = diagnosis.run_agent(description, triage, findings)
            row["diagnosis"] = result.model_dump()
            # The model's own confidence, before the limit applied by code (schema.decide)
            draft = parse_diagnosis_answer(messages[-1]["content"])
            row["model_confidence"] = [h.confidence for h in draft.hypotheses]
            row["diagnosis_turns"] = sum(m["role"] == "assistant" for m in messages)
            row["prompt_chars"] = len(messages[1]["content"])
        except Exception as e:  # record it and go on
            row["error"] = f"{type(e).__name__}: {str(e)[:300]}"
        row["seconds"] = round(time.time() - t0)
        results.append(row)
        out.write_text(json.dumps(results, ensure_ascii=False, indent=1))
        d = row.get("diagnosis") or {}
        print(f"\n{'=' * 100}\n{case_id} ({row['seconds']}s) · right incident deepened: {row.get('right_incident_deepened')}"
              f" · {row.get('error', '')}")
        print(f"REAL CAUSE: {row['real_root_cause'][:400]}")
        for h in d.get("hypotheses", []):
            print(f"  [{h['confidence']}] trigger={h['same_trigger']} component={h['same_component']} {h['cause']}  (based on {h['based_on']})")
        print(f"  evidence_sufficient={d.get('evidence_sufficient')} next_step={d.get('next_step')} "
              f"search_request={d.get('search_request')!r} questions={d.get('questions_for_analyst')}")
        print(f"  gaps: {d.get('gaps')}")
    print(f"\nsaved to {out}")


if __name__ == "__main__":
    main()
