"""Gera o catálogo de post-mortems a partir do README.md de danluu/post-mortems.

Baixa o README de um commit fixo, transforma cada entrada "[Empresa](url). texto"
em uma linha do CSV e grava data/catalog_from_readme.csv. Se data/catalog.csv
existir, compara os dois e imprime as diferenças. O catalog.csv não é alterado.
"""

import csv
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

# Commit de 31/08/2026, usado para gerar o catalog.csv original
COMMIT = "630562e55281ff28961704e8042a7dc9569a96e7"
README_URL = f"https://raw.githubusercontent.com/danluu/post-mortems/{COMMIT}/README.md"

DATA = Path(__file__).resolve().parent.parent / "data"
OUTPUT = DATA / "catalog_from_readme.csv"
CATALOG = DATA / "catalog.csv"

COLUNAS = ["catalog_id", "category", "company", "url", "domain", "description", "priority"]

# Seções do README que não são incidentes
SECOES_IGNORADAS = {"Table of Contents", "Other lists of postmortems", "Analysis", "Contributors"}

SECAO = re.compile(r"^## (.+)")
ENTRADA = re.compile(r"^\[([^\]]+)\]\((\S+?)\)\.?\s*(.*)")


def ler_readme() -> list[dict]:
    with urllib.request.urlopen(README_URL, timeout=30) as resposta:
        linhas = resposta.read().decode("utf-8").splitlines()

    entradas = []
    secao = None
    for linha in linhas:
        m = SECAO.match(linha)
        if m:
            secao = m.group(1).strip()
            continue
        m = ENTRADA.match(linha)
        if m and secao and secao not in SECOES_IGNORADAS:
            company, url, description = m.groups()
            entradas.append({
                "catalog_id": f"DAN-{len(entradas) + 1:03d}",
                "category": secao,
                "company": company,
                "url": url,
                "domain": urlparse(url).netloc,
                "description": description.strip(),
                "priority": "",
            })
    return entradas


def comparar(novas: list[dict]) -> None:
    with CATALOG.open(encoding="utf-8") as f:
        antigas = {row["catalog_id"]: row for row in csv.DictReader(f)}
    novas_por_id = {row["catalog_id"]: row for row in novas}

    diferencas = 0
    for catalog_id in sorted(antigas.keys() | novas_por_id.keys()):
        antiga, nova = antigas.get(catalog_id), novas_por_id.get(catalog_id)
        if antiga is None or nova is None:
            onde = "só no catalog.csv" if nova is None else "só no README"
            print(f"{catalog_id}: {onde}")
            diferencas += 1
            continue
        for coluna in COLUNAS:
            if antiga[coluna] != nova[coluna]:
                print(f"{catalog_id} [{coluna}]\n  catalog.csv: {antiga[coluna]}\n  README:      {nova[coluna]}")
                diferencas += 1

    print(f"Comparação com catalog.csv: {diferencas} diferença(s)")


def main() -> None:
    entradas = ler_readme()
    with OUTPUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUNAS)
        writer.writeheader()
        writer.writerows(entradas)
    print(f"Entradas: {len(entradas)} gravadas em {OUTPUT}")

    if CATALOG.exists():
        comparar(entradas)


if __name__ == "__main__":
    main()
