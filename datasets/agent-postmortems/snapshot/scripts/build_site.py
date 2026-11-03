#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Static-site generator for the agent-postmortems corpus (M5).

Reads incidents/*.yaml and emits a self-contained static site to site/:
  site/index.html          browsable index with client-side filters + search
  site/<incident_id>/index.html   per-incident permalink page + "Cite this"
  site/feed.xml            RSS feed of incidents, newest first
  site/style.css           shared styles (light/dark)

No backend, no build framework — plain HTML/CSS + a little vanilla JS for the
filters. Navigation links are relative, so the output works at any base path
(GitHub Pages project subpath, a custom domain, or file://). Absolute URLs
(citations, RSS) use SITE_BASE_URL.

Usage:
  uv run scripts/build_site.py
  SITE_BASE_URL=https://agent-postmortems.dev uv run scripts/build_site.py
"""
from __future__ import annotations

import datetime
import html
import os
import shutil
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
INCIDENTS_DIR = REPO / "incidents"
OUT = REPO / "site"
SITE_BASE = os.environ.get("SITE_BASE_URL", "https://swarmproof.github.io/agent-postmortems").rstrip("/")

SEVERITY_ORDER = {"critical": 0, "high": 1, "moderate": 2, "low": 3, "informational": 4}
FRAMEWORKS = yaml.safe_load((REPO / "schema" / "framework-mappings.yaml").read_text())["frameworks"]
FRAMEWORK_LABELS = {"owasp_llm": "OWASP LLM", "owasp_agentic": "OWASP Agentic", "mitre_atlas": "MITRE ATLAS"}


def esc(x) -> str:
    return html.escape(str(x if x is not None else ""), quote=True)


def normalize(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [normalize(v) for v in obj]
    return obj


def load_incidents() -> list[dict]:
    recs = []
    for p in sorted(INCIDENTS_DIR.glob("*.yaml")):
        if p.name.startswith("_"):
            continue
        recs.append(normalize(yaml.safe_load(p.read_text())))
    recs.sort(key=lambda r: r.get("date", ""), reverse=True)
    return recs


# --------------------------------------------------------------------------- page shell
def page(title: str, body: str, css_href: str, description: str = "") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="stylesheet" href="{css_href}">
<link rel="alternate" type="application/rss+xml" title="agent-postmortems" href="{SITE_BASE}/feed.xml">
</head>
<body>
<header class="site-head">
  <a class="brand" href="{'.' if css_href == 'style.css' else '..'}/">agent-postmortems</a>
  <span class="tagline">a structured database of real AI-agent failures</span>
</header>
<main>
{body}
</main>
<footer class="site-foot">
  <span>Data: <a href="https://github.com/swarmproof/agent-postmortems">github.com/swarmproof/agent-postmortems</a></span>
  <span>Corpus CC-BY-4.0 · code Apache-2.0</span>
</footer>
</body>
</html>
"""


def badge(text: str, kind: str) -> str:
    return f'<span class="badge badge-{esc(kind)}">{esc(text)}</span>'


def chain_str(rec: dict) -> str:
    parts = []
    for fc in rec.get("failure_classes", []):
        c = fc.get("class", "")
        s = fc.get("subclass")
        parts.append(f"{c}/{s}" if s else c)
    return " → ".join(parts)


# --------------------------------------------------------------------------- index
def render_index(recs: list[dict]) -> str:
    classes = sorted({fc.get("class") for r in recs for fc in r.get("failure_classes", [])})
    severities = [s for s in SEVERITY_ORDER if any(r.get("severity") == s for r in recs)]
    years = sorted({(r.get("date") or "")[:4] for r in recs if r.get("date")}, reverse=True)

    def opts(values):
        return "".join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in values)

    rows = []
    for r in recs:
        rid = r["incident_id"]
        rclasses = " ".join(sorted({fc.get("class", "") for fc in r.get("failure_classes", [])}))
        rows.append(f"""<a class="card" href="{esc(rid)}/"
     data-classes="{esc(rclasses)}" data-severity="{esc(r.get('severity',''))}"
     data-type="{esc(r.get('incident_type',''))}" data-year="{esc((r.get('date') or '')[:4])}"
     data-text="{esc((r.get('title','') + ' ' + rid).lower())}">
  <div class="card-head">
    <span class="card-date">{esc(r.get('date',''))}</span>
    {badge(r.get('incident_type','?'), 'type-' + esc(r.get('incident_type','')))}
    {badge(r.get('severity','?'), 'sev-' + esc(r.get('severity','')))}
  </div>
  <div class="card-title">{esc(r.get('title', rid))}</div>
  <div class="card-chain">{esc(chain_str(r))}</div>
</a>""")

    body = f"""
<section class="intro">
  <h1>Agent incident post-mortems</h1>
  <p>{len(recs)} sourced, structured post-mortems of real AI-agent failures — prompt injection,
  tool misuse, data exfiltration, sandbox escapes, cost blowups, and more. Every record follows
  <a href="https://github.com/swarmproof/agent-postmortems/blob/main/SCHEMA.md">one schema</a> and
  cites public sources. <a href="{SITE_BASE}/feed.xml">RSS</a>.</p>
</section>
<section class="filters" aria-label="Filters">
  <input type="search" id="q" placeholder="Search title…" aria-label="Search">
  <select id="f-class"><option value="">All classes</option>{opts(classes)}</select>
  <select id="f-sev"><option value="">All severities</option>{opts(severities)}</select>
  <select id="f-type"><option value="">Incident &amp; hazard</option><option value="incident">incident</option><option value="hazard">hazard</option></select>
  <select id="f-year"><option value="">All years</option>{opts(years)}</select>
  <span id="count" class="count"></span>
</section>
<section class="cards" id="cards">
{''.join(rows)}
</section>
<script>
const cards = [...document.querySelectorAll('.card')];
const q = document.getElementById('q'), fClass = document.getElementById('f-class'),
      fSev = document.getElementById('f-sev'), fType = document.getElementById('f-type'),
      fYear = document.getElementById('f-year'), count = document.getElementById('count');
function apply() {{
  const t = q.value.trim().toLowerCase(), c = fClass.value, s = fSev.value, ty = fType.value, y = fYear.value;
  let n = 0;
  for (const el of cards) {{
    const ok = (!t || el.dataset.text.includes(t))
      && (!c || el.dataset.classes.split(' ').includes(c))
      && (!s || el.dataset.severity === s)
      && (!ty || el.dataset.type === ty)
      && (!y || el.dataset.year === y);
    el.style.display = ok ? '' : 'none';
    if (ok) n++;
  }}
  count.textContent = n + ' / ' + cards.length + ' shown';
}}
[q, fClass, fSev, fType, fYear].forEach(e => e.addEventListener('input', apply));
apply();
</script>
"""
    return page("agent-postmortems — AI-agent failure database", body, "style.css",
                "A structured, sourced database of real AI-agent failures.")


# --------------------------------------------------------------------------- incident page
def field(label: str, value: str) -> str:
    return f'<div class="kv"><dt>{esc(label)}</dt><dd>{value}</dd></div>' if value else ""


def prose(label: str, text) -> str:
    return f'<section class="prose"><h2>{esc(label)}</h2><p>{esc(text)}</p></section>' if text else ""


def render_sources(rec: dict) -> str:
    items = []
    for s in rec.get("sources", []):
        url = s.get("url", "")
        title = s.get("title") or url
        meta = " · ".join(filter(None, [s.get("publisher"), s.get("type")]))
        arch = f' · <a href="{esc(s.get("archive_url"))}">archived</a>' if s.get("archive_url") else ""
        items.append(f'<li><a href="{esc(url)}">{esc(title)}</a><span class="src-meta">{esc(meta)}{arch}</span></li>')
    return f'<section class="prose"><h2>Sources</h2><ul class="sources">{"".join(items)}</ul></section>' if items else ""


def render_blast(rec: dict) -> str:
    b = rec.get("blast_radius") or {}
    rows = []
    cost = b.get("cost") or {}
    if cost.get("amount_usd") is not None:
        amt = f"${cost['amount_usd']:,.0f}" + (" (est.)" if cost.get("estimated") else "")
        rows.append(field("Cost", esc(amt)))
    data = b.get("data") or {}
    if data.get("description") or data.get("classification"):
        d = esc(data.get("description", ""))
        cls = f' <span class="tag">{esc(data.get("classification"))}</span>' if data.get("classification") else ""
        rows.append(field("Data", d + cls))
    uh = b.get("user_harm") or {}
    if uh.get("description") or uh.get("categories"):
        cats = " ".join(f'<span class="tag">{esc(c)}</span>' for c in uh.get("categories", []))
        rows.append(field("User harm", esc(uh.get("description", "")) + " " + cats))
    if b.get("scope"):
        rows.append(field("Scope", esc(b["scope"])))
    if b.get("reversibility"):
        rows.append(field("Reversibility", esc(b["reversibility"])))
    return f'<section class="prose"><h2>Blast radius</h2><dl class="kvs">{"".join(rows)}</dl></section>' if rows else ""


def bibtex(rec: dict, url: str) -> str:
    year = (rec.get("date") or "")[:4]
    return (f"@misc{{{rec['incident_id']},\n"
            f"  title = {{{rec.get('title','')}}},\n"
            f"  year = {{{year}}},\n"
            f"  howpublished = {{agent-postmortems}},\n"
            f"  url = {{{url}}}\n}}")


def render_incident(rec: dict, all_ids: set[str]) -> str:
    rid = rec["incident_id"]
    url = f"{SITE_BASE}/{rid}/"
    sys = rec.get("system") or {}
    sys_rows = "".join([
        field("Framework", esc(sys.get("framework"))),
        field("Models", esc(", ".join(sys.get("models", [])))),
        field("Tools", esc(", ".join(sys.get("tools", [])))),
        field("Vendor", esc(sys.get("vendor"))),
        field("Autonomy", esc(sys.get("autonomy_level"))),
    ])
    caus = rec.get("causation") or {}
    class_rows = "".join([
        field("Primary class", esc(rec.get("primary_failure_class"))),
        field("Chain", esc(chain_str(rec))),
        field("Attack vector", esc(rec.get("attack_vector"))),
        field("Causation", esc(" · ".join(f"{k}: {v}" for k, v in caus.items())) if caus else ""),
    ])
    mapping_rows = ""
    for key, label in FRAMEWORK_LABELS.items():
        ids = (rec.get("mappings") or {}).get(key)
        if not ids:
            continue
        names = FRAMEWORKS[key]["ids"]
        chips = " ".join(f'<span class="tag" title="{esc(names.get(i, ""))}">{esc(i)}</span>' for i in ids)
        lbl = f'<a href="{esc(FRAMEWORKS[key]["url"])}">{esc(label)}</a>'
        mapping_rows += f'<div class="kv"><dt>{lbl}</dt><dd>{chips}</dd></div>'
    xref = "".join([
        field("CVE", " ".join(f'<a href="https://nvd.nist.gov/vuln/detail/{esc(c)}">{esc(c)}</a>' for c in rec.get("cve", []))),
        field("CWE", esc(", ".join(rec.get("cwe", [])))),
        mapping_rows,
        field("Related", " ".join(
            f'<a href="../{esc(r)}/">{esc(r)}</a>' if r in all_ids else esc(r)
            for r in rec.get("related_incidents", []))),
        field("Tags", " ".join(f'<span class="tag">{esc(t)}</span>' for t in rec.get("tags", []))),
    ])
    factors = ""
    if rec.get("contributing_factors"):
        lis = "".join(f"<li>{esc(x)}</li>" for x in rec["contributing_factors"])
        factors = f'<section class="prose"><h2>Contributing factors</h2><ul>{lis}</ul></section>'
    timeline = ""
    if rec.get("timeline"):
        lis = "".join(f'<li><span class="tl-at">{esc(e.get("at",""))}</span> {esc(e.get("event",""))}</li>'
                      for e in rec["timeline"])
        timeline = f'<section class="prose"><h2>Timeline</h2><ul class="timeline">{lis}</ul></section>'

    body = f"""
<article class="incident">
  <p class="crumb"><a href="../">← all incidents</a></p>
  <div class="badges">
    {badge(rec.get('incident_type','?'), 'type-' + esc(rec.get('incident_type','')))}
    {badge(rec.get('severity','?'), 'sev-' + esc(rec.get('severity','')))}
    {badge('confidence: ' + esc(rec.get('confidence','?')), 'neutral') if rec.get('confidence') else ''}
    {badge('status: ' + esc(rec.get('status','?')), 'neutral') if rec.get('status') else ''}
  </div>
  <h1>{esc(rec.get('title', rid))}</h1>
  <p class="sub"><code>{esc(rid)}</code> · {esc(rec.get('date',''))}</p>
  {f'<p class="summary">{esc(rec.get("summary"))}</p>' if rec.get('summary') else ''}

  <section class="prose"><h2>System</h2><dl class="kvs">{sys_rows}</dl></section>
  <section class="prose"><h2>Classification</h2><dl class="kvs">{class_rows}</dl></section>
  {prose('Trigger', rec.get('trigger'))}
  {prose('Root cause', rec.get('root_cause'))}
  {factors}
  {prose('Detection', rec.get('detection'))}
  {prose('Recovery', rec.get('recovery'))}
  {prose('Prevention', rec.get('prevention'))}
  {render_blast(rec)}
  {timeline}
  <section class="prose"><h2>References</h2><dl class="kvs">{xref}</dl></section>
  {render_sources(rec)}

  <section class="cite">
    <h2>Cite this incident</h2>
    <p class="permalink">Permalink: <a href="{url}">{esc(url)}</a></p>
    <pre id="bib">{esc(bibtex(rec, url))}</pre>
    <button onclick="navigator.clipboard.writeText(document.getElementById('bib').textContent)">Copy BibTeX</button>
  </section>
</article>
"""
    return page(f"{rec.get('title', rid)} — agent-postmortems", body, "../style.css",
                rec.get("summary", ""))


# --------------------------------------------------------------------------- feed
def render_feed(recs: list[dict]) -> str:
    latest = recs[0]["date"] if recs else ""
    items = []
    for r in recs[:50]:
        link = f"{SITE_BASE}/{r['incident_id']}/"
        items.append(f"""  <item>
    <title>{esc(r.get('title', r['incident_id']))}</title>
    <link>{esc(link)}</link>
    <guid isPermaLink="true">{esc(link)}</guid>
    <pubDate>{esc(r.get('date',''))}</pubDate>
    <description>{esc(r.get('summary',''))}</description>
  </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>agent-postmortems</title>
  <link>{SITE_BASE}/</link>
  <description>A structured database of real AI-agent failures.</description>
  <lastBuildDate>{esc(latest)}</lastBuildDate>
{chr(10).join(items)}
</channel>
</rss>
"""


CSS = """
:root { --bg:#fbfbfa; --fg:#1a1a1a; --muted:#666; --card:#fff; --line:#e5e5e3; --accent:#3b5bdb; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#15161a; --fg:#e8e8ea; --muted:#9a9aa2; --card:#1e1f25; --line:#2c2d34; --accent:#8aa0ff; }
}
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
a { color:var(--accent); text-decoration:none; } a:hover { text-decoration:underline; }
main { max-width:820px; margin:0 auto; padding:0 20px 64px; }
.site-head { max-width:820px; margin:0 auto; padding:20px; display:flex; gap:12px; align-items:baseline; flex-wrap:wrap; }
.brand { font-weight:700; font-size:18px; color:var(--fg); }
.tagline { color:var(--muted); font-size:14px; }
.site-foot { max-width:820px; margin:0 auto; padding:24px 20px; border-top:1px solid var(--line); color:var(--muted); font-size:13px; display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; }
h1 { font-size:28px; line-height:1.25; margin:8px 0 12px; }
h2 { font-size:15px; text-transform:uppercase; letter-spacing:.04em; color:var(--muted); margin:28px 0 8px; }
.intro p { color:var(--fg); }
.filters { display:flex; gap:8px; flex-wrap:wrap; align-items:center; margin:20px 0; position:sticky; top:0; background:var(--bg); padding:10px 0; }
.filters input, .filters select { padding:7px 9px; border:1px solid var(--line); border-radius:8px; background:var(--card); color:var(--fg); font-size:14px; }
.filters #q { flex:1; min-width:160px; }
.count { color:var(--muted); font-size:13px; margin-left:auto; }
.cards { display:flex; flex-direction:column; gap:10px; }
.card { display:block; padding:14px 16px; border:1px solid var(--line); border-radius:12px; background:var(--card); color:var(--fg); }
.card:hover { border-color:var(--accent); text-decoration:none; }
.card-head { display:flex; gap:8px; align-items:center; margin-bottom:6px; }
.card-date { color:var(--muted); font-size:13px; font-variant-numeric:tabular-nums; }
.card-title { font-weight:600; }
.card-chain { color:var(--muted); font-size:13px; margin-top:4px; }
.badges { display:flex; gap:6px; flex-wrap:wrap; margin:4px 0 8px; }
.badge { font-size:12px; font-weight:600; padding:2px 8px; border-radius:999px; border:1px solid var(--line); white-space:nowrap; }
.badge-sev-critical { background:#fdecec; color:#b42318; border-color:#f6c9c4; }
.badge-sev-high { background:#fdf1e7; color:#b54708; border-color:#f6d5b3; }
.badge-sev-moderate { background:#fffaeb; color:#93700a; border-color:#f5e3a1; }
.badge-sev-low { background:#ecfdf3; color:#137a3e; border-color:#bbe9cc; }
.badge-sev-informational { background:#f2f4f7; color:#475467; border-color:#e0e4ea; }
.badge-type-incident { background:#eef2ff; color:#3538cd; border-color:#cfd6ff; }
.badge-type-hazard { background:#f2f4f7; color:#475467; border-color:#e0e4ea; }
.badge-neutral { color:var(--muted); }
@media (prefers-color-scheme: dark) { .badge { background:transparent !important; } }
.crumb { margin:0 0 12px; font-size:14px; }
.sub { color:var(--muted); margin:0 0 16px; }
.sub code { background:var(--card); padding:2px 6px; border-radius:6px; border:1px solid var(--line); }
.summary { font-size:18px; line-height:1.5; }
.prose p { margin:0 0 8px; }
.kvs { margin:0; } .kv { display:flex; gap:12px; padding:5px 0; border-bottom:1px solid var(--line); }
.kv dt { flex:0 0 130px; color:var(--muted); font-size:14px; } .kv dd { margin:0; flex:1; }
.tag { display:inline-block; font-size:12px; padding:1px 7px; border-radius:6px; background:var(--card); border:1px solid var(--line); color:var(--muted); margin:1px 2px; }
.sources { margin:0; padding-left:18px; } .sources li { margin:6px 0; }
.src-meta { color:var(--muted); font-size:13px; margin-left:6px; }
.timeline { list-style:none; padding:0; } .timeline li { padding:4px 0; border-bottom:1px solid var(--line); }
.tl-at { color:var(--muted); font-variant-numeric:tabular-nums; margin-right:8px; }
.cite { margin-top:36px; padding:16px; border:1px solid var(--line); border-radius:12px; background:var(--card); }
.cite pre { overflow-x:auto; background:var(--bg); padding:12px; border-radius:8px; border:1px solid var(--line); font-size:13px; }
.cite button { padding:7px 12px; border:1px solid var(--line); border-radius:8px; background:var(--bg); color:var(--fg); cursor:pointer; }
"""


def main() -> int:
    recs = load_incidents()
    ids = {r["incident_id"] for r in recs}
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "style.css").write_text(CSS)
    (OUT / "index.html").write_text(render_index(recs))
    (OUT / "feed.xml").write_text(render_feed(recs))
    for r in recs:
        d = OUT / r["incident_id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(render_incident(r, ids))
    # .nojekyll so GitHub Pages serves files/dirs verbatim
    (OUT / ".nojekyll").write_text("")
    print(f"built site/ — {len(recs)} incidents, index + feed, base {SITE_BASE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
