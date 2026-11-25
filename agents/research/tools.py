"""The tools of the Research RAG agent: the LLM decides when and how to call them.

    search_inside_incidents  searches for the cause and the fix INSIDE incidents already found
    find_similar_incidents   looks for OTHER incidents similar to the current one

The names start differently (search_ / find_) so the model does not confuse them, and so the fix for a
tool name with extra text glued to it can work by prefix (see fixed_tool_name in agent.py).

Each tool returns two things (response_format="content_and_artifact"):
    content   short text that goes back to the LLM as a ToolMessage
    artifact  the full data (passages, similarity, queries made), which the build_findings node uses
              to build the agent's output; the LLM does not need to read all of it

The search itself is in rag/busca.py (the E3 RAG, written in Portuguese). The two functions at the top
of this file are the only bridge to it: they translate its results to the English keys used here.
"""
from __future__ import annotations

import re
from typing import Annotated

from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState
from pydantic import BaseModel, Field

from rag import busca
from rag.prompts import _id_curto as short_id  # "danluu-017" -> "DAN-017"

MAX_INCIDENTS_PER_CALL = 3
MAX_QUERIES_PER_CALL = 2
N_PASSAGES = 2             # passages per query inside an incident
N_DOCS = 5                 # incidents per query in find_similar_incidents
INCLUDE_DESCRIPTION_IN_FIRST_SEARCH = False  # hybrid mode: see find_similar_incidents
EXTRA_FROM_LLM = 5         # hybrid mode: new incidents from the LLM queries added to the description's
# Experiment (2026-11-23): the description and the Triage symptoms in ONE search text, instead of one search
# per symptom (normal mode) or the description alone (hybrid's guaranteed search). See description_query().
SYMPTOMS_IN_ONE_QUERY = False
# Experiments: incidents treated as if they were not in the corpus (no search returns them). Used to test a new
# problem whose right post-mortem does not exist (agents/orchestration/experiments/run_diagnosis_cases.py --hide-right).
HIDDEN_IDS: set[str] = set()
MIN_PASSAGE_CHARS = 200    # shorter passages are almost always just a title ("Further details here.")
PASSAGE_CHARS_FOR_LLM = 700
# Fixed queries added to the LLM's query in every search inside an incident (the LLM sometimes writes a
# generic query). They used to be one ("what was the root cause and how was the problem fixed"); the
# check of 2026-11-17 showed it found the story and the cause, and the fix section ended up 4th to 12th.
CAUSE_QUERY = "what was the root cause of the failure"
FIX_QUERY = "how the problem was corrected, remediation, action items, prevention, next steps"
N_CAUSE = 1                # passages from the fixed cause query (the LLM's query usually covers the cause)
N_FIX = 2                  # passages about the fix
# Section titles (or labels in capitals) that mean fix or prevention: these passages come first.
FIX_TITLE = re.compile(r"fix|correct|remediat|prevent|action item|next step|lesson|moving forward|going forward"
                       r"|improv|follow[- ]?up|what we.{0,10}(doing|changing)|resolution|resolved|mitigat"
                       r"|changes|recover", re.I)
FIX_LABEL = re.compile(r"\b(REMEDIATION|PREVENTION|RESOLUTION|ACTION ITEMS|NEXT STEPS|CORRECTIVE)\b")


# ---------------------------------------------------------------- bridge to rag/busca.py

def _passage(d: dict) -> dict:
    return {"section": d.get("secao", ""), "content": d["content"], "similarity": d["similaridade"]}


def search_incidents(query: str, n_docs: int, n_passages: int, exclude: list[str] | None = None) -> list[dict]:
    """Incidents similar to the query (two-step search in pgvector), with English keys."""
    incidents = []
    exclude = sorted(set(exclude or []) | HIDDEN_IDS)
    for r in busca.buscar(query, n_docs, n_passages, excluir=exclude):
        best = r.get("melhor_chunk") or {}
        incidents.append({
            "incident_id": short_id(r["doc_id"]), "company": r["company"], "title": r["title"], "url": r.get("url"),
            "summary": r.get("resumo") or "", "similarity": r["similaridade"],
            "best_chunk": {"type": "summary" if best.get("tipo") == "resumo" else "text",
                           "section": best.get("secao", ""), "content": best.get("content", "")},
            "passages": [_passage(d) for d in r.get("detalhes", [])],
        })
    return incidents


def search_in_incident(incident_id: str, query: str, n: int) -> list[dict]:
    """The n passages of one incident most similar to the query, with English keys."""
    return [_passage(d) for d in busca.buscar_no_incidente(incident_id, query, n)]


def description_query(state: dict) -> str:
    """The text of the code search for the description: the description alone or, with SYMPTOMS_IN_ONE_QUERY,
    the description followed by the symptoms joined in one text."""
    symptoms = [s for s in state.get("symptoms") or [] if s.strip()]
    if SYMPTOMS_IN_ONE_QUERY and symptoms:
        return f"{state['description']} {'; '.join(symptoms)}"
    return state["description"]


# ---------------------------------------------------------------- search_inside_incidents

class SearchInIncident(BaseModel):
    incident_id: str = Field(description="ID of an incident already found, e.g. DAN-017")
    query: str = Field(description="short query in English, as keywords, about the cause and the fix of this incident")
    why: str = Field(description="one short sentence saying why you chose this incident: "
                                 "what matches the current incident and what does not")


def is_fix_passage(d: dict) -> bool:
    """True if the section title or a capital label says the passage is about the fix or prevention."""
    return bool(FIX_TITLE.search(d.get("section") or "")) or bool(FIX_LABEL.search(d["content"]))


def passages_for_incident(incident_id: str, llm_query: str | None, seen: set[str]) -> tuple[list[dict], list[dict]]:
    """The passages of one incident for the Diagnosis agent: up to 2 from the LLM's query, 1 from the fixed
    cause query and 2 about the fix. For the fix, passages whose section title says fix ("How was the problem
    corrected", "Remediation", "Action Items"...) come before the others. `seen` avoids repeated passages.
    Returns (passages, search log)."""
    passages, log = [], []

    def accept(d: dict, query: str, source: str) -> bool:
        # the ingestion chunks overlap: two passages can start the same way (the same block twice)
        start = "start:" + d["content"][:300]
        if d["content"] in seen or start in seen or len(d["content"]) < MIN_PASSAGE_CHARS:
            return False
        seen.update({d["content"], start})
        d.update({"origin": "deep_search", "query": query, "query_source": source})
        passages.append(d)
        return True

    for query, source, n in ((llm_query, "llm", N_PASSAGES), (CAUSE_QUERY, "cause", N_CAUSE)):
        if not query:
            continue
        k = 0
        for d in search_in_incident(incident_id, query, n + 3):
            if k < n and accept(d, query, source):
                k += 1
        log.append({"step": "search_inside_incidents", "query": query, "filter": {"incident": incident_id},
                    "ids": [incident_id]})
    whole = search_in_incident(incident_id, FIX_QUERY, 40)  # the whole incident, ordered by the fix query
    k = 0
    for d in sorted(whole, key=lambda d: not is_fix_passage(d)):  # sorted is stable: keeps the similarity order
        if k < N_FIX and accept(d, FIX_QUERY, "fix"):
            k += 1
    log.append({"step": "search_inside_incidents", "query": FIX_QUERY, "filter": {"incident": incident_id},
                "ids": [incident_id]})
    return passages, log


def known_ids(state: dict) -> set[str]:
    """Incidents the agent has already seen: candidates, seen in earlier rounds and found by find_similar_incidents."""
    ids = {r["incident_id"] for r in state.get("candidates", [])} | set(state.get("seen_ids", []))
    for m in state.get("messages", []):
        if isinstance(m, ToolMessage) and m.name == "find_similar_incidents" and m.artifact:
            ids |= {r["incident_id"] for r in m.artifact.get("incidents", [])}
    return ids


@tool(response_format="content_and_artifact")
def search_inside_incidents(searches: list[SearchInIncident],
                            state: Annotated[dict, InjectedState]) -> tuple[str, dict]:
    """Searches INSIDE incidents already found for the passages that explain the root cause and the fix.
    Use it for the incidents that really look like the current one (up to 3 in one call), saying for
    each one why you chose it (why)."""
    known = known_ids(state)
    passages_by_incident, log, lines, warnings = {}, [], [], []
    reasons: dict[str, str] = {}
    seen_by_id: dict[str, set] = {}  # the LLM sometimes asks for 2 searches in the same incident: no repeats
    for s in searches[:MAX_INCIDENTS_PER_CALL]:
        i = short_id(s.incident_id.strip().upper())
        if i not in known:
            warnings.append(f"{i} is not among the incidents found; ignored.")
            continue
        reasons[i] = s.why.strip()
        new, entries = passages_for_incident(i, s.query.strip(), seen_by_id.setdefault(i, set()))
        passages_by_incident.setdefault(i, []).extend(new)
        log += entries
        lines.append(f"### [{i}] query: {s.query.strip()}")
        lines += [f"Passage ({d['section'] or 'no section'}): {d['content'][:PASSAGE_CHARS_FOR_LLM]}" for d in new]
    if len(searches) > MAX_INCIDENTS_PER_CALL:
        warnings.append(f"Only the first {MAX_INCIDENTS_PER_CALL} incidents were searched.")
    text = "\n\n".join(lines) or "No passage found."
    if warnings:
        text += "\n\nWarnings: " + " ".join(warnings)
    return text, {"passages_by_incident": passages_by_incident, "reasons": reasons, "search_log": log,
                  "warnings": warnings}


# ---------------------------------------------------------------- find_similar_incidents

@tool(response_format="content_and_artifact")
def find_similar_incidents(queries: list[str], state: Annotated[dict, InjectedState]) -> tuple[str, dict]:
    """Looks for OTHER incidents similar to the current one, with new queries (up to 2, short, in English).
    Incidents already seen are left out. Use it when none of the incidents found looks like the current
    one, or when the diagnosis request asks for another kind of incident."""
    exclude = sorted(known_ids(state))
    by_id, log = {}, []
    guaranteed: list[dict] = []
    first = not any(isinstance(m, ToolMessage) and m.name == "find_similar_incidents" for m in state.get("messages", []))
    if INCLUDE_DESCRIPTION_IN_FIRST_SEARCH and first and state.get("description"):
        # Hybrid mode: the LLM's first search also searches with the original description (done in code).
        # Its N_DOCS incidents always come in; the LLM queries add up to EXTRA_FROM_LLM new ones.
        guaranteed = search_incidents(description_query(state), N_DOCS, N_PASSAGES, exclude)
        for r in guaranteed:
            r["found_by"] = "description"
            for d in r["passages"]:
                d.update({"origin": "similar", "query": description_query(state)})
        log.append({"step": "find_similar_incidents (description)", "query": description_query(state),
                    "filter": {"exclude": exclude}, "ids": [r["incident_id"] for r in guaranteed]})
    for query in [q.strip() for q in queries if q.strip()][:MAX_QUERIES_PER_CALL]:
        found = search_incidents(query, N_DOCS, N_PASSAGES, exclude)
        for r in found:
            r.setdefault("found_by", "llm_query")
            for d in r["passages"]:
                d.update({"origin": "similar", "query": query})
            if r["incident_id"] not in by_id or r["similarity"] > by_id[r["incident_id"]]["similarity"]:
                by_id[r["incident_id"]] = r
        log.append({"step": "find_similar_incidents", "query": query, "filter": {"exclude": exclude},
                    "ids": [r["incident_id"] for r in found]})
    if guaranteed:
        guaranteed_ids = {r["incident_id"] for r in guaranteed}
        extra = [r for r in sorted(by_id.values(), key=lambda r: -r["similarity"]) if r["incident_id"] not in guaranteed_ids]
        incidents = guaranteed + extra[:EXTRA_FROM_LLM]
    else:
        incidents = sorted(by_id.values(), key=lambda r: -r["similarity"])[:N_DOCS]
    lines = [f"### [{r['incident_id']}] {r['company']} — {r['title']}\nSummary: {r['summary'] or '(no summary)'}"
             for r in incidents]
    text = ("\n\n".join(lines) + "\n\nTo see the cause and the fix of one of them, use search_inside_incidents."
            if lines else "No new incident found.")
    return text, {"incidents": incidents, "search_log": log}


TOOLS = [search_inside_incidents, find_similar_incidents]
TOOL_NAMES = {t.name for t in TOOLS}
