"""Limpeza básica dos post-mortems da danluu.

Lê os JSON de data/extracted/ e o data/catalog.csv, descarta documentos sem
conteúdo útil e grava o resultado em data/processed/danluu_clean.jsonl.
Os arquivos de entrada não são alterados.

Quando existe um texto reextraído em data/reextracted/ (refeito a partir do
HTML salvo, com regras para cada formato de página), ele substitui o
texto de data/extracted/: a extração original tinha pegado menus, rodapés,
comentários ou outra página no lugar do post-mortem.

Depois saem as traduções, os comentários de leitores, os parágrafos em outra
escrita, os parágrafos longos repetidos e os parágrafos de plantilla do site
(idênticos em 3 ou mais documentos). Por fim, um título que se repete em
vários documentos recebe a primeira frase do resumo, para identificar o incidente. Só saem trechos inteiros: nenhuma
frase é alterada.
"""

import csv
import json
import re
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
EXTRACTED = DATA / "extracted"
REEXTRACTED = DATA / "reextracted"
CATALOG = DATA / "catalog.csv"
OUTPUT = DATA / "processed" / "danluu_clean.jsonl"

MIN_PALAVRAS = 50

# Documentos com texto, mas cujo conteúdo não é o post-mortem
EXCLUIDOS = {
    "DAN-150": "Elastic: a coleta pegou um anúncio de patrocínio de F1",
    "DAN-202": "North American Electric Power System: a coleta pegou uma licença ambiental da EPA",
}

# Títulos que a extração não conseguiu obter ou que não identificam o incidente
TITULOS_MANUAIS = {
    "DAN-155": "CA Flowdock – Outage 22nd & 23rd April 2020",
    "DAN-191": "IT Infrastructure Resiliency Review (23 February 2017)",
    "DAN-002": "Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)",
    "DAN-104": "Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region",
}

# Documentos que trazem uma tradução depois do texto em inglês: o texto é
# cortado a partir do início da tradução
TRADUCOES = {
    "DAN-063": "Gostaríamos de compartilhar",  # AWS SA-EAST-1: versão em português
}

# Documentos que terminam com comentários de leitores: o texto é cortado onde
# eles começam (ponto achado à mão em cada documento)
COMENTARIOS = {
    "DAN-022": "Very cool. Any chance you’re going to release the source?",
    "DAN-025": "## 5 comments",
    "DAN-119": "## Jan\n\non 26 Mar 14",
    "DAN-187": "Robbie\nOctober 21st, 2013",
}


# Parágrafos removidos (só saem parágrafos inteiros):
# - em outra escrita (coreano, japonês...), se sobrar texto latino suficiente;
# - longos e repetidos (algumas páginas da AWS trazem o texto duas vezes).
MIN_LATINO = 1000     # caracteres de texto latino que precisam sobrar
MIN_REPETIDO = 200    # parágrafos menores que isso podem repetir (linhas de tabela, títulos)


def fracao_nao_latina(paragrafo: str) -> float:
    letras = [c for c in paragrafo if c.isalpha()]
    return sum(1 for c in letras if ord(c) > 0x024F) / len(letras) if letras else 0.0


def remover_paragrafos(texto: str) -> tuple[str, int, int]:
    """Devolve (texto, parágrafos em outra escrita removidos, parágrafos repetidos removidos)."""
    paragrafos = texto.split("\n\n")
    latinos = [p for p in paragrafos if fracao_nao_latina(p) < 0.3]
    outra_escrita = 0
    if len(latinos) < len(paragrafos) and sum(map(len, latinos)) >= MIN_LATINO:
        outra_escrita = len(paragrafos) - len(latinos)
        paragrafos = latinos
    vistos, unicos = set(), []
    for p in paragrafos:
        chave = p.strip()
        if len(chave) >= MIN_REPETIDO and chave in vistos:
            continue
        vistos.add(chave)
        unicos.append(p)
    return "\n\n".join(unicos), outra_escrita, len(paragrafos) - len(unicos)


# Parágrafos de plantilla do site (publicidade, avisos, "posts relacionados"): o mesmo
# parágrafo, idêntico, em PLANTILLA_DOCS ou mais documentos. Títulos e parágrafos curtos
# ("## Root cause", "Thanks") ficam, porque se repetem legitimamente.
PLANTILLA_DOCS = 3
PLANTILLA_MIN = 100   # caracteres


def remover_plantillas(documentos: list[dict]) -> int:
    """Remove dos documentos os parágrafos de plantilla; devolve quantos foram removidos."""
    def candidatos(texto: str) -> set[str]:
        return {p.strip() for p in texto.split("\n\n") if len(p.strip()) >= PLANTILLA_MIN and not p.strip().startswith("#")}

    contagem = Counter(p for doc in documentos for p in candidatos(doc["extracted_text"]))
    plantillas = {p for p, n in contagem.items() if n >= PLANTILLA_DOCS}
    removidos = 0
    for doc in documentos:
        paragrafos = doc["extracted_text"].split("\n\n")
        mantidos = [p for p in paragrafos if p.strip() not in plantillas]
        removidos += len(paragrafos) - len(mantidos)
        doc["extracted_text"] = "\n\n".join(mantidos)
    return removidos


def distinguir_titulos(documentos: list[dict]) -> int:
    """Títulos repetidos em 2+ documentos ("Google Cloud Status Dashboard") não dizem de qual
    incidente se trata: recebem a primeira frase do resumo. Devolve quantos títulos mudaram."""
    contagem = Counter(doc["title"] for doc in documentos)
    mudados = 0
    for doc in documentos:
        if contagem[doc["title"]] > 1 and doc["summary"]:
            frase = re.split(r"(?<=[.;])\s", doc["summary"], maxsplit=1)[0].rstrip(".;")
            if len(frase) > 120:
                frase = frase[:117].rsplit(" ", 1)[0] + "..."
            doc["title"] = f"{doc['title']} — {frase}"
            mudados += 1
    return mudados


LINK_MD = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def resumo_sem_links(resumo: str | None) -> str | None:
    """O resumo do catálogo sem os links markdown: [texto](url) -> texto."""
    return re.sub(r"\s+", " ", LINK_MD.sub(r"\1", resumo)).strip() if resumo else resumo


def cortar(texto: str, marca: str, catalog_id: str) -> str:
    if marca not in texto:
        print(f"  aviso: {catalog_id}: marca de corte não encontrada ({marca[:40]!r})")
        return texto
    return texto.split(marca)[0].strip()


def main() -> None:
    with CATALOG.open(encoding="utf-8") as f:
        summaries = {row["catalog_id"]: row["description"] for row in csv.DictReader(f)}

    lidos = sem_texto = curtos = excluidos = reextraidos = outra_escrita = repetidos = 0
    documentos = []

    for path in sorted(EXTRACTED.glob("DAN-*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        catalog_id = doc["catalog_id"]
        lidos += 1

        texto = (doc.get("extracted_text") or "").strip()
        titulo = doc.get("title")
        reextraido = REEXTRACTED / path.name
        if reextraido.exists():
            novo = json.loads(reextraido.read_text(encoding="utf-8"))
            texto = (novo.get("extracted_text") or "").strip()
            titulo = novo.get("title") or titulo
            reextraidos += 1

        if not texto:
            sem_texto += 1
            continue
        if len(texto.split()) < MIN_PALAVRAS:
            curtos += 1
            continue
        if catalog_id in EXCLUIDOS:
            excluidos += 1
            continue
        if catalog_id in TRADUCOES:
            texto = cortar(texto, TRADUCOES[catalog_id], catalog_id)
        if catalog_id in COMENTARIOS:
            texto = cortar(texto, COMENTARIOS[catalog_id], catalog_id)
        texto, n_escrita, n_repetidos = remover_paragrafos(texto)
        outra_escrita += n_escrita
        repetidos += n_repetidos

        documentos.append({
            "extracted_text": texto,
            "title": TITULOS_MANUAIS.get(catalog_id) or titulo,
            "source_url": doc.get("source_url"),
            "company": doc.get("company"),
            "catalog_id": catalog_id,
            "category": doc.get("category"),
            "summary": resumo_sem_links(summaries.get(catalog_id)),
            "text_source": "reextracted" if reextraido.exists() else "extracted",
        })

    plantillas = remover_plantillas(documentos)
    titulos = distinguir_titulos(documentos)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        for doc in documentos:
            f.write(json.dumps(doc, ensure_ascii=False) + "\n")

    print(f"Lidos: {lidos} (texto reextraído: {reextraidos})")
    print(f"Descartados sem texto: {sem_texto}")
    print(f"Descartados < {MIN_PALAVRAS} palavras: {curtos}")
    print(f"Descartados manualmente: {excluidos}")
    print(f"Parágrafos removidos: {outra_escrita} em outra escrita, {repetidos} repetidos, "
          f"{plantillas} de plantilla do site (em {PLANTILLA_DOCS}+ documentos)")
    print(f"Títulos repetidos completados com o resumo: {titulos}")
    print(f"Gravados: {len(documentos)} em {OUTPUT}")


if __name__ == "__main__":
    main()
