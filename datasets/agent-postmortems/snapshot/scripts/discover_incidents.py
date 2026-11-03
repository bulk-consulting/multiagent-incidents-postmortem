#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "requests"]
# ///
"""Weekly incident discovery — the deterministic, LLM-free front of the curation pipeline.

Harvests candidate agent-failure reports from public, keyless sources — Google News
RSS, the arXiv API, plain RSS/Atom feeds, the NVD CVE keyword API, and the GitHub
global Security Advisory database (all configured in discovery_sources.yaml) —
de-duplicates them against the existing corpus, ranks by relevance, and emits a
candidate list. It never writes an incident — a human (or the auto-draft layer)
turns a candidate into a schema-valid record, which still goes through PR review.

Dedup drops a candidate if its URL (or bare domain+path) is already cited in any
incident, and flags likely duplicates whose title strongly overlaps an existing
incident title. Nothing here contacts an LLM or merges anything.

Usage:
  uv run scripts/discover_incidents.py                 # human-readable summary
  uv run scripts/discover_incidents.py --json out.json # machine-readable candidates
  uv run scripts/discover_incidents.py --markdown       # GitHub-issue-ready checklist
  uv run scripts/discover_incidents.py --days 14 --limit 30
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import yaml

REPO = Path(__file__).resolve().parent.parent
INCIDENTS_DIR = REPO / "incidents"
SOURCES_FILE = Path(__file__).resolve().parent / "discovery_sources.yaml"
UA = {"User-Agent": "agent-postmortems-discovery/1.0 (+https://github.com/swarmproof/agent-postmortems)"}
TIMEOUT = 30
STOPWORDS = {"the", "a", "an", "ai", "and", "of", "to", "in", "on", "for", "after",
            "its", "it", "with", "into", "was", "were", "how", "why", "s"}


# --------------------------------------------------------------------------- corpus
def load_corpus() -> tuple[set[str], list[set[str]], set[str]]:
    """Return (cited URL keys, tokenized existing titles, cited CVE ids) for dedup."""
    urls: set[str] = set()
    titles: list[set[str]] = []
    cves: set[str] = set()
    for path in INCIDENTS_DIR.glob("*.yaml"):
        if path.name.startswith("_"):
            continue
        rec = yaml.safe_load(path.read_text())
        for src in rec.get("sources", []):
            url = src["url"] if isinstance(src, dict) else src
            urls.add(url_key(url))
        for text in (rec.get("title", ""), rec.get("incident_id", "")):
            titles.append(tokenize(text))
        for cve in rec.get("cve", []) or []:
            cves.add(cve.upper())
    return urls, titles, cves


def url_key(url: str) -> str:
    """Normalize a URL to host+path (drop scheme, www, query, trailing slash)."""
    try:
        p = urllib.parse.urlsplit(url.strip().lower())
        host = p.netloc.removeprefix("www.")
        return f"{host}{p.path.rstrip('/')}"
    except ValueError:
        return url.strip().lower()


def tokenize(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", (text or "").lower())
            if w not in STOPWORDS and len(w) > 2}


# --------------------------------------------------------------------------- sources
def fetch(url: str) -> str | None:
    try:
        r = requests.get(url, headers=UA, timeout=TIMEOUT)
        r.raise_for_status()
        return r.text
    except requests.RequestException as exc:
        print(f"  (source failed: {url} — {type(exc).__name__})", file=sys.stderr)
        return None


def parse_rss_items(xml_text: str) -> list[dict]:
    """Parse RSS <item> and Atom <entry> into {title, url, date, summary}."""
    items = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return items
    for it in root.iter():
        tag = it.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue
        title = link = date = summary = ""
        for child in it:
            ctag = child.tag.split("}")[-1]
            if ctag == "title":
                title = (child.text or "").strip()
            elif ctag == "link":
                link = (child.get("href") or child.text or "").strip()
            elif ctag in ("pubDate", "published", "updated"):
                date = date or (child.text or "").strip()
            elif ctag in ("description", "summary", "content"):
                summary = summary or re.sub(r"<[^>]+>", " ", child.text or "")
        if title and link:
            items.append({"title": html.unescape(title), "url": html.unescape(link),
                          "date": date, "summary": html.unescape(summary)[:500]})
    return items


def google_news(query: str) -> list[dict]:
    q = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
    xml_text = fetch(url)
    return parse_rss_items(xml_text) if xml_text else []


def arxiv(query: str, limit: int = 15) -> list[dict]:
    q = urllib.parse.quote(query)
    url = (f"http://export.arxiv.org/api/query?search_query={q}"
           f"&sortBy=submittedDate&sortOrder=descending&max_results={limit}")
    xml_text = fetch(url)
    items = parse_rss_items(xml_text) if xml_text else []
    for it in items:  # arXiv abstract links are the canonical URL
        it["title"] = re.sub(r"\s+", " ", it["title"])
    return items


def nvd(query: str, limit: int = 20) -> list[dict]:
    """NVD CVE keyword search (keyless). Free-text, targets agent/LLM/MCP CVEs."""
    q = urllib.parse.quote(query)
    url = (f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={q}"
           f"&resultsPerPage={limit}")
    body = fetch(url)
    if not body:
        return []
    try:
        data = json.loads(body)
    except ValueError:
        return []
    items = []
    for v in data.get("vulnerabilities", []):
        cve = v.get("cve", {})
        cid = cve.get("id", "")
        descs = [d["value"] for d in cve.get("descriptions", []) if d.get("lang") == "en"]
        desc = descs[0] if descs else ""
        if not cid:
            continue
        items.append({
            "title": f"{cid}: {desc[:140]}",
            "url": f"https://nvd.nist.gov/vuln/detail/{cid}",
            "date": cve.get("published", ""),
            "summary": desc[:500],
            "cve_id": cid.upper(),
        })
    return items


def github_advisories(pages: int = 1, per_page: int = 100) -> list[dict]:
    """GitHub global Security Advisory DB (unauth). No free-text filter, so we pull
    recent advisories and keyword-filter locally in discover()."""
    items = []
    for page in range(1, pages + 1):
        url = (f"https://api.github.com/advisories?per_page={per_page}"
               f"&sort=published&page={page}")
        body = fetch(url)
        if not body:
            break
        try:
            rows = json.loads(body)
        except ValueError:
            break
        if not isinstance(rows, list) or not rows:
            break
        for a in rows:
            summary = a.get("summary") or ""
            ghsa = a.get("ghsa_id") or ""
            items.append({
                "title": summary or ghsa,
                "url": a.get("html_url") or f"https://github.com/advisories/{ghsa}",
                "date": a.get("published_at", ""),
                "summary": ((a.get("description") or "")[:500]),
                "cve_id": (a.get("cve_id") or "").upper(),
            })
    return items


# --------------------------------------------------------------------------- pipeline
def score(item: dict, keywords: list[str]) -> int:
    hay = f"{item['title']} {item.get('summary', '')}".lower()
    return sum(1 for kw in keywords if kw.lower() in hay)


def discover(days: int, limit: int) -> list[dict]:
    cfg = yaml.safe_load(SOURCES_FILE.read_text())
    cited_urls, corpus_titles, cited_cves = load_corpus()
    keywords = cfg.get("relevance_keywords", [])

    raw: list[dict] = []
    for q in cfg.get("google_news_queries", []):
        raw += [dict(it, source="google-news") for it in google_news(q)]
    for q in cfg.get("arxiv_queries", []):
        raw += [dict(it, source="arxiv") for it in arxiv(q)]
    for feed in cfg.get("rss_feeds", []):
        xml_text = fetch(feed)
        if xml_text:
            raw += [dict(it, source="rss") for it in parse_rss_items(xml_text)]
    for i, q in enumerate(cfg.get("cve_queries", [])):
        if i:
            time.sleep(6)                          # NVD keyless rate limit: ~5 req / 30s
        raw += [dict(it, source="cve") for it in nvd(q)]
    if cfg.get("github_advisories", {}).get("enabled"):
        pages = cfg["github_advisories"].get("pages", 1)
        raw += [dict(it, source="ghsa") for it in github_advisories(pages)]

    seen_keys: set[str] = set()
    seen_cves: set[str] = set()
    candidates: list[dict] = []
    for it in raw:
        key = url_key(it["url"])
        cid = it.get("cve_id", "")
        if key in seen_keys or (cid and cid in seen_cves):   # dedup within this run
            continue
        seen_keys.add(key)
        if cid:
            seen_cves.add(cid)
        if key in cited_urls or (cid and cid in cited_cves):  # already in the corpus
            continue
        toks = tokenize(it["title"])
        likely_dupe = any(len(toks & t) >= 3 and len(toks & t) / max(len(toks), 1) > 0.6
                          for t in corpus_titles)
        rel = score(it, keywords)
        if rel == 0:                               # not agent-relevant enough
            continue
        # Curated primaries (research feeds, incident DBs, arXiv, CVE/GHSA) outrank
        # general news of equal keyword relevance — favours signal over news volume.
        if it["source"] in ("arxiv", "rss", "cve", "ghsa"):
            rel += 2
        candidates.append({
            "title": it["title"], "url": it["url"], "date": it.get("date", ""),
            "source": it["source"], "relevance": rel, "likely_duplicate": likely_dupe,
        })

    candidates.sort(key=lambda c: (c["likely_duplicate"], -c["relevance"]))
    return candidates[:limit]


# --------------------------------------------------------------------------- output
def emit_markdown(cands: list[dict]) -> str:
    if not cands:
        return "_No new candidate incidents found this week._\n"
    fresh = [c for c in cands if not c["likely_duplicate"]]
    dupes = [c for c in cands if c["likely_duplicate"]]
    lines = [f"Found **{len(fresh)}** new candidate incident(s) "
             f"(+{len(dupes)} possible duplicates). De-duped against the corpus; "
             "ranked by relevance. Each needs a human to draft it from "
             "`incidents/_TEMPLATE.yaml` and open a PR.\n"]
    for c in fresh:
        lines.append(f"- [ ] **{c['title']}** — [{c['source']}]({c['url']}) "
                     f"· relevance {c['relevance']} · {c['date']}")
    if dupes:
        lines.append("\n<details><summary>Possible duplicates (verify before "
                     "discarding)</summary>\n")
        for c in dupes:
            lines.append(f"- [ ] {c['title']} — [{c['source']}]({c['url']})")
        lines.append("</details>")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", metavar="PATH", help="write candidates as JSON")
    ap.add_argument("--markdown", action="store_true", help="print GitHub-issue markdown")
    ap.add_argument("--days", type=int, default=14, help="lookback hint (advisory)")
    ap.add_argument("--limit", type=int, default=40)
    args = ap.parse_args()

    cands = discover(args.days, args.limit)

    if args.json:
        Path(args.json).write_text(json.dumps(cands, indent=2, ensure_ascii=False))
    if args.markdown:
        print(emit_markdown(cands))
    if not args.markdown:
        fresh = sum(1 for c in cands if not c["likely_duplicate"])
        for c in cands:
            flag = "DUP?" if c["likely_duplicate"] else f"r{c['relevance']:<2}"
            print(f"{flag}  {c['title'][:80]}  <{c['source']}>")
        print(f"\n{len(cands)} candidate(s): {fresh} new, {len(cands) - fresh} possible dupes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
