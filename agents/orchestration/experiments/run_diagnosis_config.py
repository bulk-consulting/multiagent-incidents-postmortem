"""
Which model settings make the Diagnosis agent's judgments repeatable, without invalid answers?

The Research agent runs ONCE per case and its findings are saved (results/diagnosis_config_findings/<case>.json);
then the Diagnosis agent runs several times on the SAME findings with each setting. So any change between the
repetitions comes from the Diagnosis model alone.

Cases: the 4 that changed judgment or claimed a wrong cause with the right post-mortem hidden (DAN-145, DAN-211,
DAN-018, DAN-116) and 2 normal cases (DAN-104, DAN-154), so that no setting makes the common path worse.

Usage (from the repository root, database up):
    multiagent_env/bin/python -I agents/orchestration/experiments/run_diagnosis_config.py [--configs A,B] [--reps 3]
Output: agents/orchestration/experiments/results/diagnosis_config_<date>.json
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
from agents.orchestration.experiments.run_diagnosis_cases import triage_output  # noqa: E402
from agents.orchestration.experiments.run_triage_scenarios import load_case  # noqa: E402
from agents.research import agent as research  # noqa: E402
from agents.research import tools  # noqa: E402

# case -> right post-mortem hidden?
CASES = {"DAN-145": True, "DAN-211": True, "DAN-018": True, "DAN-116": True, "DAN-104": False, "DAN-154": False}

NO_THINKING = {"chat_template_kwargs": {"enable_thinking": False}}
CONFIGS = {
    "A": {"label": "reasoning, default temperature, 4096 tokens", "temperature": None, "max_tokens": 4096, "options": {}},
    "B": {"label": "reasoning, default temperature, 8192 tokens", "temperature": None, "max_tokens": 8192, "options": {}},
    "C": {"label": "reasoning, temperature 0, 8192 tokens", "temperature": 0, "max_tokens": 8192, "options": {}},
    "D": {"label": "reasoning, temperature 0.3, top_p 0.95, 8192 tokens", "temperature": 0.3, "max_tokens": 8192,
          "options": {"top_p": 0.95}},
    "E": {"label": "reasoning, temperature 0.6, top_p 0.95, 8192 tokens", "temperature": 0.6, "max_tokens": 8192,
          "options": {"top_p": 0.95}},
    "F": {"label": "no reasoning, temperature 0, 4096 tokens", "temperature": 0, "max_tokens": 4096,
          "options": NO_THINKING},
    "G": {"label": "no reasoning, temperature 0.3, 4096 tokens", "temperature": 0.3, "max_tokens": 4096,
          "options": NO_THINKING},
}
FINDINGS_DIR = HERE / "results" / "diagnosis_config_findings"


def findings_for(case_id, hidden):
    """The Research agent's findings for this case: saved on the first run, read back afterwards."""
    path = FINDINGS_DIR / f"{case_id}{'_hidden' if hidden else ''}.json"
    if path.exists():
        return json.loads(path.read_text())
    description, triage = triage_output(case_id, 1)
    tools.HIDDEN_IDS = {case_id} if hidden else set()
    state = research.research(description, triage["symptoms"])
    tools.HIDDEN_IDS = set()
    data = {"case": case_id, "hidden": hidden, "description": description, "triage": triage,
            "warnings": (state.get("plan") or {}).get("warnings", []), "findings": state["findings"]}
    FINDINGS_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    return data


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--configs", default=",".join(CONFIGS))
    ap.add_argument("--cases", default=",".join(CASES))
    ap.add_argument("--reps", type=int, default=3)
    a = ap.parse_args()
    research.enable_hybrid_mode()
    out = HERE / "results" / f"diagnosis_config_{datetime.now():%Y-%m-%d_%H%M}.json"
    cases = {c: findings_for(c, CASES[c]) for c in a.cases.split(",")}
    for c, d in cases.items():
        print(f"{c}: {len(d['findings'])} findings, deepened {[r['incident_id'] for r in d['findings'] if r['deepened']]}"
              f"{' · warnings: ' + str(d['warnings']) if d['warnings'] else ''}", flush=True)
    rows = []
    for name in a.configs.split(","):
        cfg = CONFIGS[name]
        diagnosis.TEMPERATURE, diagnosis.MAX_TOKENS, diagnosis.LLM_OPTIONS = cfg["temperature"], cfg["max_tokens"], cfg["options"]
        for rep in range(1, a.reps + 1):
            for case_id, d in cases.items():
                t0 = time.time()
                row = {"config": name, "label": cfg["label"], "rep": rep, "case": case_id, "hidden": d["hidden"]}
                try:
                    result, messages = diagnosis.run_agent(d["description"], d["triage"], d["findings"], 1, 3)
                    row["diagnosis"] = result.model_dump()
                    row["turns"] = sum(m["role"] == "assistant" for m in messages)
                except Exception as e:  # record it and go on
                    row["error"] = f"{type(e).__name__}: {str(e)[:200]}"
                    msgs = getattr(e, "messages", None) or []
                    row["answer_lengths"] = [len(m["content"]) for m in msgs[2:] if m["role"] == "assistant"]
                row["seconds"] = round(time.time() - t0)
                rows.append(row)
                out.write_text(json.dumps({"configs": CONFIGS, "rows": rows}, ensure_ascii=False, indent=1))
                dg = row.get("diagnosis") or {}
                hyps = " | ".join(f"{h['confidence']} T={h['same_trigger']} C={h['same_component']} "
                                  f"M={h['same_mechanism']} {h['based_on']}" for h in dg.get("hypotheses", []))
                print(f"[{name} rep{rep}] {case_id} ({row['seconds']}s) "
                      + (f"ERROR {row['error'][:80]} {row.get('answer_lengths')}" if "error" in row else
                         f"{dg['next_step']} sufficient={dg['evidence_sufficient']} turns={row['turns']} :: {hyps}"),
                      flush=True)
    print(f"\nsaved to {out}")


if __name__ == "__main__":
    main()
