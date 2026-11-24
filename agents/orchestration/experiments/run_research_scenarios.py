"""
Step 3 of the Triage → Research test with the reworded post-mortem cases (DAN-xxx_rewrite.json): the Research
agent in HYBRID mode receives each text that the Triage stage could hand over, and we check whether it finds and
looks inside (deepens) the right post-mortem.

Inputs per case (texts from the Triage run triage_scenarios_2026-11-23_2116_ask-trigger_rewrite.json):
    concat    conversation glued as in the E5 contract (first message + "Analyst answer: ..."), scenario B
    search    search_text written by the Triage agent at the end of the conversation, scenario B
    complete  the operator's complete message, scenario A
Each input is run once per Triage round (3 rounds), with that round's Triage symptoms as context.

Usage (from the repository root, database up):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_research_scenarios.py [--parallel 3]
Output: agents/orchestration/experiments/results/research_scenarios_<date>.json
"""
from __future__ import annotations

import argparse
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from agents.research import agent, tools  # noqa: E402

TRIAGE_RUN = HERE / "results" / "triage_scenarios_2026-11-23_2116_ask-trigger_rewrite.json"


def jobs_from_triage():
    jobs = []
    for r in json.loads(TRIAGE_RUN.read_text()):
        if not r["turns"]:
            continue
        last = r["turns"][-1]
        res = last["result"]
        base = {"case": r["case"], "round": r["round"], "symptoms": res["symptoms"], "trigger": res["trigger"],
                "triage": {k: res.get(k) for k in ("trigger", "affected_service", "category", "symptoms")}}
        if r["scenario"] == "B":
            jobs.append({**base, "input": "concat", "text": last["description"]})
            jobs.append({**base, "input": "search", "text": last["result"]["search_text"]})
        else:
            jobs.append({**base, "input": "complete", "text": last["description"]})
    return sorted(jobs, key=lambda j: (j["round"], j["case"], j["input"]))


def run_one(job):
    start = time.time()
    try:
        state = agent.research(job["text"], job["symptoms"], triage=job["triage"] if agent.TRIAGE_CONTEXT else None)
    except Exception as e:  # record it and go on
        return {**job, "error": f"{type(e).__name__}: {str(e)[:300]}", "seconds": round(time.time() - start)}
    case = job["case"]
    findings = [r["incident_id"] for r in state["findings"]]
    deepened = [d["id"] for d in state["plan"]["deepen"]]
    found = [r["incident_id"] for r in state.get("new_incidents", [])]
    exp = next((r for r in state["findings"] if r["incident_id"] == case), None)
    return {**job,
            "found": case in found, "found_position": found.index(case) + 1 if case in found else 0,
            "deepened": case in deepened, "findings_position": findings.index(case) + 1 if case in findings else 0,
            "deepened_ids": deepened, "queries": state["plan"]["new_queries"],
            "why": exp.get("why") if exp else None, "llm_calls": len(state.get("llm_calls", [])),
            "seconds": round(time.time() - start)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--parallel", type=int, default=3)
    ap.add_argument("--mode", choices=["hybrid", "agentic"], default="hybrid")
    ap.add_argument("--triage-context", action="store_true", help="give the LLM the whole Triage output + guidance")
    ap.add_argument("--inputs", default="concat,search,complete", help="e.g. concat")
    a = ap.parse_args()
    agent.enable_hybrid_mode() if a.mode == "hybrid" else agent.enable_agentic_mode()
    agent.TRIAGE_CONTEXT = a.triage_context
    tools.busca.vetorizar("warm-up")
    agent.llm_with_tools()
    jobs = [j for j in jobs_from_triage() if j["input"] in a.inputs.split(",")]
    suffix = f"_{a.mode}" + ("_triage-context" if a.triage_context else "") + "_rewrite"
    out = HERE / "results" / f"research_scenarios_{datetime.now():%Y-%m-%d_%H%M}{suffix}.json"
    done, lock, start = [], threading.Lock(), time.time()

    def one(job):
        r = run_one(job)
        with lock:
            done.append(r)
            out.write_text(json.dumps(done, ensure_ascii=False, indent=1))
            n, total = len(done), len(jobs)
            elapsed = time.time() - start
            status = r.get("error", "")[:60] or (f"deepened (findings #{r['findings_position']})" if r["deepened"]
                                                 else ("found, NOT deepened" if r["found"] else "NOT found"))
            print(f"progress: {n}/{total} · {elapsed / 60:.1f} min · ~{elapsed / n * (total - n) / 60:.0f} min left · "
                  f"r{r['round']} {r['case']} {r['input']}: {status}", flush=True)
        return r

    with ThreadPoolExecutor(max_workers=max(1, a.parallel)) as pool:
        list(pool.map(one, jobs))
    print("\nexpected post-mortem deepened (of 12 cases x 3 rounds):")
    for inp in a.inputs.split(","):
        rs = [r for r in done if r["input"] == inp and "error" not in r]
        print(f"  {inp:9} deepened {sum(r['deepened'] for r in rs)}/{len(rs)} · found {sum(r['found'] for r in rs)}/{len(rs)}"
              f" · errors {sum(1 for r in done if r['input'] == inp and 'error' in r)}")
    print(f"saved to {out}")


if __name__ == "__main__":
    main()
