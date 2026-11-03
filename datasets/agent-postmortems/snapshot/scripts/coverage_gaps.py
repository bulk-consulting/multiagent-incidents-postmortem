#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "requests"]
# ///
"""Completeness critic (S5) — find agent incidents that curated external sources
have and our corpus does not.

Systematises the "what did we miss?" review. It diffs our corpus against curated,
machine-readable reference lists (configured in discovery_sources.yaml under
`coverage_sources`) and reports the entries we don't yet cover:

  - markdown_headings: awesome-lists organised as `### YYYY-MM-DD - <incident>`
    headings (e.g. awesome-ai-agent-attacks). Each heading is one incident;
    CVE ids in the heading are matched against our records.
  - rss: incident-database feeds (e.g. AIID), keyword-filtered to agent relevance.

An entry counts as COVERED if any CVE it names is already in a record's `cve:`
field, or its title strongly overlaps an existing incident title; otherwise it is
a GAP. It never writes an incident — output is a triage list for a human.

Usage:
  uv run scripts/coverage_gaps.py               # human-readable gap list
  uv run scripts/coverage_gaps.py --markdown     # GitHub-issue-ready
  uv run scripts/coverage_gaps.py --json out.json
  uv run scripts/coverage_gaps.py --limit 50
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

# Reuse the discovery helpers (same directory is on sys.path when run directly).
from discover_incidents import fetch, load_corpus, parse_rss_items, score, tokenize, url_key

SOURCES_FILE = Path(__file__).resolve().parent / "discovery_sources.yaml"
CVE_RE = re.compile(r"CVE-\d{4}-\d+", re.IGNORECASE)
HEADING_RE = re.compile(r"^#{2,4}\s+(\d{4}-\d{2}-\d{2})\s*[-–—]\s*(.+?)\s*$")
LINK_RE = re.compile(r"\((https?://[^)]+)\)")


def extract_headings(md_text: str) -> list[dict]:
    """Parse `### YYYY-MM-DD - <incident>` entries; grab the first link under each.

    `url` is the incident's own primary source; it stays empty when no independent
    link is found (we never fall back to the aggregator list's own URL)."""
    lines = md_text.splitlines()
    entries = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if not m:
            continue
        date, title = m.group(1), m.group(2)
        url = ""
        for nxt in lines[i + 1:i + 12]:
            if HEADING_RE.match(nxt):
                break
            lm = LINK_RE.search(nxt)
            if lm and "awesome.re" not in lm.group(1) and "shields.io" not in lm.group(1):
                url = lm.group(1)
                break
        entries.append({
            "title": title, "date": date, "url": url,
            "cves": sorted({c.upper() for c in CVE_RE.findall(title)}),
        })
    return entries


def covered(entry: dict, cited_urls: set, corpus_titles: list[set], cited_cves: set) -> bool:
    if set(entry["cves"]) & cited_cves:
        return True
    if url_key(entry["url"]) in cited_urls:
        return True
    toks = tokenize(entry["title"])
    return any(len(toks & t) >= 4 for t in corpus_titles)


def find_gaps(limit: int) -> tuple[list[dict], int]:
    cfg = yaml.safe_load(SOURCES_FILE.read_text())
    cov = cfg.get("coverage_sources", {}) or {}
    keywords = cfg.get("relevance_keywords", [])
    # Broad incident DBs (AIID) cover general "AI harms"; require a genuine agent
    # signal so we stay agent-scoped and don't import out-of-scope entries.
    rss_keywords = cfg.get("coverage_rss_keywords", keywords)
    cited_urls, corpus_titles, cited_cves = load_corpus()

    entries: list[dict] = []
    for list_url in cov.get("markdown_headings", []):
        md = fetch(list_url)
        if md:
            entries += [dict(e, ref="awesome-list") for e in extract_headings(md)]
    for feed in cov.get("rss", []):
        xml = fetch(feed)
        for it in (parse_rss_items(xml) if xml else []):
            if score(it, rss_keywords) == 0:        # must match an agent-identity term
                continue
            entries.append({
                "title": it["title"], "date": (it.get("date") or "")[:10],
                "url": it["url"], "cves": sorted({c.upper() for c in CVE_RE.findall(it.get("summary", ""))}),
                "ref": "aiid",
            })

    seen: set[str] = set()
    gaps: list[dict] = []
    for e in entries:
        key = url_key(e["url"]) + "|" + e["title"][:40].lower()
        if key in seen:
            continue
        seen.add(key)
        if not covered(e, cited_urls, corpus_titles, cited_cves):
            gaps.append(e)

    gaps.sort(key=lambda e: e["date"], reverse=True)
    return gaps[:limit], len(gaps)


def emit_markdown(gaps: list[dict], total: int) -> str:
    if not gaps:
        return "_No new candidate incidents to review this week._\n"
    lines = [f"**{total}** candidate incident(s) to review for the corpus "
             f"(showing newest {len(gaps)}). Each is a candidate to draft from "
             "`incidents/_TEMPLATE.yaml`; some may be surveys or reports rather than "
             "incidents — triage before drafting.\n"]
    for g in gaps:
        cves = (" · " + ", ".join(sorted(g["cves"]))) if g["cves"] else ""
        title = f"[{g['title']}]({g['url']})" if g.get("url") else g["title"]
        lines.append(f"- [ ] **{g['date']}** — {title}{cves}")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", metavar="PATH")
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--limit", type=int, default=50)
    args = ap.parse_args()

    gaps, total = find_gaps(args.limit)

    if args.json:
        import json
        Path(args.json).write_text(json.dumps(gaps, indent=2, ensure_ascii=False))
    if args.markdown:
        print(emit_markdown(gaps, total))
    else:
        for g in gaps:
            cves = (" " + ",".join(sorted(g["cves"]))) if g["cves"] else ""
            print(f"{g['date']}  [{g['ref']}] {g['title'][:88]}{cves}")
        print(f"\n{total} gap(s) vs curated external sources; showing {len(gaps)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
