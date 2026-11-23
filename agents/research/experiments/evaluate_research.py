"""
Runs the Research RAG agent on the 12 E3 questions (rag/avaliacao/perguntas.json), or on another file
(--file agents/research/experiments/questions_hard.json), and records for each question what needs to be checked:
    - is the expected incident in the initial search? in the findings?
    - did the LLM look inside (deepen) the expected incident?
    - the deep search passages (section + start of the text, to check by hand whether they are cause/fix)

The question files keep the keys of the E3 evaluation (rag/avaliacao): id, tipo, pergunta, esperado, aceitos,
posicao_busca_inicial.

Usage (from the repository root, with the database up):
    multiagent_env/bin/python -I agents/research/experiments/evaluate_research.py [--questions q01,q10] [--no-llm]
        [--parallel 3] [--hybrid | --agentic]
Output: agents/research/experiments/results/research_<date>.json and .md
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
if str(ROOT) not in sys.path:  # lets "python agents/research/experiments/evaluate_research.py" find the packages
    sys.path.insert(0, str(ROOT))
from agents.research import agent, tools  # noqa: E402


def evaluate(q: dict, no_llm: bool) -> dict:
    start = time.time()
    try:
        state = agent.research(q["pergunta"], no_llm=no_llm)
    except Exception as e:  # record it and go on to the next question
        return {"id": q["id"], "error": f"{type(e).__name__}: {str(e)[:300]}", "seconds": round(time.time() - start)}
    expected = set(q.get("esperado", [])) | set(q.get("aceitos", []))
    initial = [r["incident_id"] for r in state.get("candidates", [])]
    findings = [r["incident_id"] for r in state["findings"]]
    plan = state["plan"]
    deepened_ids = [d["id"] for d in plan["deepen"]]
    passages = {i: [{"section": d["section"], "similarity": round(d["similarity"], 3),
                     "query_source": d.get("query_source", "llm"),
                     "start": d["content"][:300].replace("\n", " ")} for d in ps]
                for i, ps in state.get("deepened", {}).items()}
    # full passages of the expected incident (to check by hand whether they bring the cause and the fix)
    expected_passages = {r["incident_id"]: [{"source": d.get("query_source") or d.get("origin"),
                                             "section": d.get("section", ""),
                                             "fix_title": tools.is_fix_passage(d), "text": d["content"]}
                                            for d in r["passages"]]
                         for r in state["findings"] if r["incident_id"] in expected}
    return {
        "id": q["id"], "type": q["tipo"], "expected": sorted(expected),
        "expected_passages": expected_passages,
        "initial_search_position": q.get("posicao_busca_inicial"),
        "expected_in_new": sorted(expected & {r["incident_id"] for r in state.get("new_incidents", [])}),
        "initial_search": initial, "findings": findings,
        "expected_in_initial_search": sorted(expected & set(initial)),
        "expected_in_findings": sorted(expected & set(findings)),
        "expected_deepened": sorted(expected & set(deepened_ids)),
        "plan": plan, "deep_search_passages": passages,
        "new_incidents": [r["incident_id"] for r in state.get("new_incidents", [])],
        "search_log": state.get("search_log", []),
        "llm_calls": [{"seconds": c.get("seconds"), "tokens": (c.get("usage") or {}).get("total_tokens"),
                       "tools": [t["name"] for t in c.get("tool_calls", [])],
                       "names_fixed": c.get("names_fixed", 0), "json_repaired": c.get("json_repaired", 0),
                       "fields_filled": c.get("fields_filled", 0), "malformed": len(c.get("invalid", [])),
                       "malformed_detail": c.get("invalid", []), "text": (c.get("text") or "")[:300]}
                      for c in state.get("llm_calls", [])],
        "seconds": round(time.time() - start),
    }


def _tools_used(r: dict) -> str:
    """E.g. 'find → search' per LLM call; '(text)' when it answered without a tool; notes on names/format."""
    parts = []
    for c in r.get("llm_calls", []):
        names = [n.split("_")[0] for n in c["tools"]] or ["(text)"]
        extra = (f" [{c['names_fixed']} name fixed]" if c["names_fixed"] else "") + \
                (f" [{c['malformed']} malformed]" if c["malformed"] else "") + \
                (f" [{c['json_repaired']} JSON repaired]" if c["json_repaired"] else "")
        parts.append("+".join(names) + extra)
    return " → ".join(parts) or "—"


def to_markdown(results: list[dict], no_llm: bool) -> str:
    lines = [f"# Research RAG agent ({'without LLM' if no_llm else 'with LLM'})", "",
             "| q | expected | position in search | in initial search | deepened | tools called | found by new query | in findings | new queries | s |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        if "error" in r:
            lines.append(f"| {r['id']} | error: {r['error'][:80]} | | | | | | | | {r['seconds']} |")
            continue
        yes = lambda k: ("—" if not r["expected"] else ("yes" if r[k] else "no"))  # noqa: E731
        lines.append(f"| {r['id']} | {', '.join(r['expected']) or '(none)'} | {r.get('initial_search_position') or '—'} | "
                     f"{yes('expected_in_initial_search')} | {yes('expected_deepened')} | {_tools_used(r)} | "
                     f"{yes('expected_in_new')} | {yes('expected_in_findings')} | {len(r['plan']['new_queries'])} | "
                     f"{r['seconds']} |")
    lines.append("")
    for r in results:
        if "error" in r:
            continue
        p = r["plan"]
        lines += [f"## {r['id']} (expected: {', '.join(r['expected']) or 'none'})", "",
                  f"- initial search: {', '.join(r['initial_search'])}",
                  f"- final note: {p['final_note']}"]
        lines += [f"- deepen {d['id']}: `{d['query']}`" + (f" — {d['why']}" if d.get("why") else "") for d in p["deepen"]]
        lines += [f"- new query: `{s['query']}` → {', '.join(s['ids'])}" for s in r.get("search_log", [])
                  if s["step"].startswith("find_similar_incidents")]
        if r["new_incidents"]:
            lines.append(f"- new incidents in the findings: {', '.join(r['new_incidents'])}")
        lines += [f"- warning: {w}" for w in p.get("warnings", [])]
        for i, ps in r["deep_search_passages"].items():
            for d in ps:
                lines.append(f"  - {i} ({d.get('query_source', 'llm')}) [{d['section'] or 'no section'}] "
                             f"{d['similarity']}: {d['start'][:200]}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--questions", help="e.g. q01,q10 (default: all)")
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--file", type=Path, default=ROOT / "rag/avaliacao/perguntas.json",
                    help="JSON with {'perguntas': [...]} (default: the 12 E3 questions; e.g. questions_hard.json)")
    ap.add_argument("--parallel", type=int, default=1, help="how many questions at the same time (default: 1)")
    ap.add_argument("--model", help="NIM model for this run only (default: LLM_MODEL in .env)")
    ap.add_argument("--agentic", action="store_true", help="agentic mode: the LLM runs the first search")
    ap.add_argument("--hybrid", action="store_true", help="hybrid mode: agentic + the original description in the first search")
    ap.add_argument("--no-reasoning", action="store_true", help="enable_thinking=False in the LLM (fewer tokens)")
    ap.add_argument("--candidates", type=int, help="candidates of the initial search the LLM reads (default: agent.N_DOCS)")
    a = ap.parse_args()
    all_questions = json.loads(a.file.read_text())["perguntas"]
    wanted = set(a.questions.split(",")) if a.questions else None
    questions = [q for q in all_questions if not wanted or q["id"] in wanted]
    if a.model:
        agent.MODEL_OVERRIDE = a.model
    if a.candidates:
        agent.N_DOCS = a.candidates
    if a.no_reasoning:
        agent.REASONING = False
    if a.hybrid:
        agent.enable_hybrid_mode()
    elif a.agentic:
        agent.enable_agentic_mode()
    # Load the embedding model and the LLM client before the threads (avoids loading them twice at once).
    tools.busca.vetorizar("warm-up")
    if not a.no_llm:
        agent.llm_with_tools()

    suffix = "" if a.file.name == "perguntas.json" else "_" + a.file.stem
    if a.model:
        suffix += "_" + a.model.split("/")[-1].replace(".", "-")  # no dots: with_suffix would cut the name
    if a.candidates:
        suffix += f"_{a.candidates}cand"
    if a.no_reasoning:
        suffix += "_no-reasoning"
    if a.hybrid:
        suffix += "_hybrid"
    elif a.agentic:
        suffix += "_agentic"
    out = HERE / "results" / f"research_{datetime.now():%Y-%m-%d_%H%M}{suffix}{'_nollm' if a.no_llm else ''}"
    out.parent.mkdir(exist_ok=True)
    partial = out.with_name(out.name + "_partial.json")

    # Visible progress and partial saves: after each question, a "progress:" line with how many finished, the
    # time and the estimate of what is left; what is done goes to *_partial.json (if the run is stopped,
    # nothing that ran is lost).
    start = time.time()
    done: dict[str, dict] = {}
    lock = threading.Lock()

    def one(q: dict) -> dict:
        r = evaluate(q, a.no_llm)
        with lock:
            done[q["id"]] = r
            n, total = len(done), len(questions)
            elapsed = time.time() - start
            left = elapsed / n * (total - n)
            errors = sum("error" in x for x in done.values())
            status = r.get("error", "")[:60] or ("expected deepened" if r.get("expected_deepened")
                                                  else ("—" if not r.get("expected") else "expected NOT deepened"))
            print(f"progress: {n}/{total} questions ({errors} with error) · {elapsed / 60:.1f} min · "
                  f"~{left / 60:.0f} min left · {q['id']}: {status}", flush=True)
            partial.write_text(json.dumps([done[x["id"]] for x in questions if x["id"] in done], ensure_ascii=False))
        return r

    # The questions are independent; pool.map returns them in the order of the questions.
    with ThreadPoolExecutor(max_workers=max(1, a.parallel)) as pool:
        results = list(pool.map(one, questions))
    print(f"total: {time.time() - start:.0f}s with {a.parallel} in parallel", flush=True)
    out.with_suffix(".json").write_text(json.dumps(results, ensure_ascii=False, indent=1))
    out.with_suffix(".md").write_text(to_markdown(results, a.no_llm))
    partial.unlink(missing_ok=True)
    print(f"saved to {out}.md / .json")


if __name__ == "__main__":
    main()
