"""
Recoleta das timelines completas dos status pages (API pública Statuspage v2).

O que muda em relação ao crawler da IncidentDB:
  1. Guarda TODAS as atualizações de cada incidente (o crawler cortava em 8 e
     perdia justamente as primeiras, porque a API lista do mais novo para o mais antigo).
  2. Mantém as atualizações com status "postmortem" (é onde a causa raiz aparece).
  3. Salva o JSON bruto de cada provedor, para rastreabilidade e reprocessamento.
  4. Não inventa nada: nenhum campo de causa, remediação ou config é gerado.
  5. Extrai os links citados nas atualizações (ex.: post-mortem em blog), para buscar depois.

Uso:
  python recoleta_statuspage.py                    # baixa da API e processa
  python recoleta_statuspage.py --from-dir raw/    # reprocessa JSONs já baixados (sem rede)

Saídas:
  raw/<provedor>.json          resposta bruta da API
  timelines.jsonl              um incidente por linha, timeline completa em ordem cronológica
"""
from __future__ import annotations
import argparse, html, json, re, sys, time, urllib.request
from pathlib import Path

PROVIDERS = {
    "GitHub":       "https://www.githubstatus.com/api/v2/incidents.json",
    "Cloudflare":   "https://www.cloudflarestatus.com/api/v2/incidents.json",
    "OpenAI":       "https://status.openai.com/api/v2/incidents.json",
    "Datadog":      "https://status.datadoghq.com/api/v2/incidents.json",
    "Vercel":       "https://www.vercel-status.com/api/v2/incidents.json",
    "Discord":      "https://discordstatus.com/api/v2/incidents.json",
    "npm":          "https://status.npmjs.org/api/v2/incidents.json",
    "Sentry":       "https://status.sentry.io/api/v2/incidents.json",
    "HashiCorp":    "https://status.hashicorp.com/api/v2/incidents.json",
    "DigitalOcean": "https://status.digitalocean.com/api/v2/incidents.json",
    # Provedores que o crawler original listava mas que não entraram na base:
    "Supabase":     "https://status.supabase.com/api/v2/incidents.json",
    "Atlassian":    "https://status.atlassian.com/api/v2/incidents.json",
    "Reddit":       "https://www.redditstatus.com/api/v2/incidents.json",
    "CircleCI":     "https://status.circleci.com/api/v2/incidents.json",
}

URL_RE = re.compile(r"https?://[^\s)\"'<>\]]+")


def clean(text: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", text or "")
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "incident-copilot-research/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def normalize(company: str, inc: dict) -> dict | None:
    updates = inc.get("incident_updates") or []
    if not updates:
        return None
    # A API devolve do mais novo para o mais antigo; ordenamos cronologicamente.
    updates = sorted(updates, key=lambda u: u.get("created_at") or "")
    timeline, links = [], []
    for u in updates:
        body = clean(u.get("body", ""))
        if not body:
            continue
        timeline.append({
            "at": u.get("created_at"),
            "status": u.get("status"),          # investigating, identified, monitoring, resolved, postmortem...
            "body": body,
        })
        links += [u.rstrip(".,;:") for u in URL_RE.findall(body)]
    return {
        "company": company,
        "incident_id": inc.get("id"),
        "title": inc.get("name"),
        "impact": inc.get("impact"),              # none / minor / major / critical (como veio da API)
        "status": inc.get("status"),
        "created_at": inc.get("created_at"),
        "resolved_at": inc.get("resolved_at"),
        "components": [c.get("name") for c in inc.get("components") or [] if c.get("name")],
        "source_url": inc.get("shortlink"),
        "n_updates": len(timeline),
        "has_postmortem_update": any(t["status"] == "postmortem" for t in timeline),
        "linked_urls": sorted(set(links)),
        "timeline": timeline,
        "timeline_text": "\n".join(f"[{t['at']}] ({t['status']}) {t['body']}" for t in timeline),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-dir", help="processa JSONs já salvos nesta pasta, sem acessar a rede")
    ap.add_argument("--raw-dir", default="raw")
    ap.add_argument("--out", default="timelines.jsonl")
    args = ap.parse_args()

    raw_dir = Path(args.from_dir or args.raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)
    records, report = [], []

    for company, url in PROVIDERS.items():
        path = raw_dir / f"{company}.json"
        try:
            if args.from_dir:
                if not path.exists():
                    continue
                data = json.loads(path.read_text(encoding="utf-8"))
            else:
                data = fetch(url)
                path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
                time.sleep(1)
        except Exception as e:  # noqa: BLE001
            report.append(f"{company:13} FALHOU: {e}")
            continue
        incs = data.get("incidents", [])
        recs = [r for r in (normalize(company, i) for i in incs) if r]
        records += recs
        report.append(f"{company:13} {len(recs):3} incidentes | "
                      f"mediana de updates: {sorted(r['n_updates'] for r in recs)[len(recs)//2] if recs else 0} | "
                      f"com post-mortem: {sum(r['has_postmortem_update'] for r in recs)}")

    with open(args.out, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print("\n".join(report))
    print(f"\nTotal: {len(records)} incidentes -> {args.out}")
    print(f"Com mais de 8 updates (seriam cortados pelo crawler original): "
          f"{sum(r['n_updates'] > 8 for r in records)}")
    print(f"Com update de post-mortem: {sum(r['has_postmortem_update'] for r in records)}")
    print(f"Com links externos citados: {sum(bool(r['linked_urls']) for r in records)}")


if __name__ == "__main__":
    sys.exit(main())
