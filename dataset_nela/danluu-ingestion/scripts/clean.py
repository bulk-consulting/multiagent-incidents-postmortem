"""Limpeza básica dos post-mortems da danluu.

Lê os JSON de data/extracted/ e o data/catalog.csv, descarta documentos sem
conteúdo útil e grava o resultado em data/processed/danluu_clean.jsonl.
Os arquivos de entrada não são alterados.
"""

import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
EXTRACTED = DATA / "extracted"
CATALOG = DATA / "catalog.csv"
OUTPUT = DATA / "processed" / "danluu_clean.jsonl"

MIN_PALAVRAS = 50

# Documentos com texto, mas cujo conteúdo não é o post-mortem
EXCLUIDOS = {
    "DAN-146": "Dropbox: a coleta pegou o menu do blog",
    "DAN-150": "Elastic: a coleta pegou um anúncio de patrocínio de F1",
}

# Títulos que a extração não conseguiu obter
TITULOS_MANUAIS = {
    "DAN-155": "CA Flowdock – Outage 22nd & 23rd April 2020",
}

# Documentos que trazem uma tradução depois do texto em inglês: o texto é
# cortado a partir do início da tradução
TRADUCOES = {
    "DAN-063": "Gostaríamos de compartilhar",  # AWS SA-EAST-1: versão em português
}


def main() -> None:
    with CATALOG.open(encoding="utf-8") as f:
        summaries = {row["catalog_id"]: row["description"] for row in csv.DictReader(f)}

    lidos = sem_texto = curtos = excluidos = 0
    documentos = []

    for path in sorted(EXTRACTED.glob("DAN-*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        lidos += 1

        texto = (doc.get("extracted_text") or "").strip()
        if not texto:
            sem_texto += 1
            continue
        if len(texto.split()) < MIN_PALAVRAS:
            curtos += 1
            continue
        if doc["catalog_id"] in EXCLUIDOS:
            excluidos += 1
            continue
        if doc["catalog_id"] in TRADUCOES:
            texto = texto.split(TRADUCOES[doc["catalog_id"]])[0].strip()

        documentos.append({
            "extracted_text": texto,
            "title": doc.get("title") or TITULOS_MANUAIS.get(doc["catalog_id"]),
            "source_url": doc.get("source_url"),
            "company": doc.get("company"),
            "catalog_id": doc["catalog_id"],
            "category": doc.get("category"),
            "summary": summaries.get(doc["catalog_id"]),
        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        for doc in documentos:
            f.write(json.dumps(doc, ensure_ascii=False) + "\n")

    print(f"Lidos: {lidos}")
    print(f"Descartados sem texto: {sem_texto}")
    print(f"Descartados < {MIN_PALAVRAS} palavras: {curtos}")
    print(f"Descartados manualmente: {excluidos}")
    print(f"Gravados: {len(documentos)} em {OUTPUT}")


if __name__ == "__main__":
    main()
