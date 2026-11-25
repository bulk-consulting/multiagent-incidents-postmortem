"""
Diagnosis agent on the reworded post-mortem cases: Triage output (from the Triage run) → Research agent (hybrid)
→ Diagnosis agent. Saves, for each case, what the Diagnosis agent said next to the real root cause of the
post-mortem ("discovered_later" in DAN-xxx_rewrite.json), to be checked by hand.

Usage (from the repository root, database up):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_diagnosis_cases.py --cases DAN-104 [--round 1]
        [--hide-right]   # the right post-mortem is hidden from every search: a new problem, outside the corpus
        [--loop]         # refinement loop: while the Diagnosis asks for refine_search, run the Research agent again
                         # with its request (up to MAX_RESEARCH_ROUNDS), like the graph will do
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
from agents.research import tools  # noqa: E402
from agents.orchestration.state import MAX_RESEARCH_ROUNDS  # noqa: E402

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
    ap.add_argument("--hide-right", action="store_true",
                    help="hide the right post-mortem from every search (a new problem, outside the corpus)")
    ap.add_argument("--loop", action="store_true", help="refinement loop up to MAX_RESEARCH_ROUNDS")
    a = ap.parse_args()
    research.enable_hybrid_mode()
    tag = ("_hidden" if a.hide_right else "") + ("_loop" if a.loop else "")
    out = HERE / "results" / f"diagnosis_cases_{datetime.now():%Y-%m-%d_%H%M}{tag}.json"
    results = []
    for case_id in a.cases.split(","):
        t0 = time.time()
        description, triage = triage_output(case_id, a.round)
        tools.HIDDEN_IDS = {case_id} if a.hide_right else set()
        row = {"case": case_id, "round": a.round, "hidden": sorted(tools.HIDDEN_IDS), "description": description,
               "triage": triage,
               "real_root_cause": load_case(case_id, rewrite=True)["discovered_later"]["root_cause"]}
        state, request, rounds = None, "", []
        try:
            max_rounds = MAX_RESEARCH_ROUNDS if a.loop else 1
            for rnd in range(1, max_rounds + 1):
                state = research.research(description, triage["symptoms"], request=request, previous=state)
                findings = state["findings"]
                result, messages = diagnosis.run_agent(description, triage, findings, rnd, MAX_RESEARCH_ROUNDS)
                draft = parse_diagnosis_answer(messages[-1]["content"])
                rounds.append({
                    "research_round": rnd, "request": request,
                    "research_warnings": (state.get("plan") or {}).get("warnings", []),
                    "research_llm_calls": len(state.get("llm_calls", [])),
                    "searches": [{"step": e.get("step"), "query": (e.get("query") or "")[:150], "ids": e.get("ids")}
                                 for e in state.get("search_log", [])],
                    "findings": [{"id": r["incident_id"], "deepened": r["deepened"], "title": r.get("title")}
                                 for r in findings],
                    "right_incident_in_findings": any(r["incident_id"] == case_id for r in findings),
                    "right_incident_deepened": any(r["incident_id"] == case_id and r["deepened"] for r in findings),
                    "diagnosis": result.model_dump(),
                    # the model's own confidence, before the limit applied by code (schema.decide)
                    "model_confidence": [h.confidence for h in draft.hypotheses],
                    "diagnosis_turns": sum(m["role"] == "assistant" for m in messages),
                    "prompt_chars": len(messages[1]["content"]),
                })
                if result.next_step != "refine_search":
                    break
                request = result.search_request
            last = rounds[-1]
            row.update({k: last[k] for k in ("findings", "right_incident_in_findings", "right_incident_deepened",
                                             "diagnosis", "model_confidence", "diagnosis_turns", "prompt_chars")})
            if a.loop:
                row["rounds"] = rounds
        except Exception as e:  # record it and go on
            row["error"] = f"{type(e).__name__}: {str(e)[:300]}"
            row["error_round"] = len(rounds) + 1
            if a.loop:
                row["rounds"] = rounds
            if getattr(e, "messages", None):  # the Diagnosis agent's answers that were rejected
                row["error_answers"] = [{"role": m["role"], "content": m["content"][:1500]}
                                        for m in e.messages[2:]]
        row["seconds"] = round(time.time() - t0)
        results.append(row)
        out.write_text(json.dumps(results, ensure_ascii=False, indent=1))
        d = row.get("diagnosis") or {}
        print(f"\n{'=' * 100}\n{case_id} ({row['seconds']}s) · right incident deepened: {row.get('right_incident_deepened')}"
              f" · rounds: {len(row.get('rounds', [])) or 1} · {row.get('error', '')}")
        for k in row.get("rounds", [])[:-1]:
            dk = k["diagnosis"]
            print(f"  round {k['research_round']}: {[h['confidence'] for h in dk['hypotheses']]} "
                  f"→ {dk['next_step']} {dk['search_request']!r}")
        print(f"REAL CAUSE: {row['real_root_cause'][:400]}")
        for h in d.get("hypotheses", []):
            print(f"  [{h['confidence']}] trigger={h['same_trigger']} component={h['same_component']} {h['cause']}  (based on {h['based_on']})")
        print(f"  evidence_sufficient={d.get('evidence_sufficient')} next_step={d.get('next_step')} "
              f"search_request={d.get('search_request')!r} questions={d.get('questions_for_analyst')}")
        print(f"  gaps: {d.get('gaps')}")
    print(f"\nsaved to {out}")


if __name__ == "__main__":
    main()
