"""
Inventário automático do danluu: preenche, para cada entrada do catálogo, as
marcações de P10 que podem ser medidas sem interpretação e uma P11 preliminar
(ver docs/triagem/regua.md).

Só lê datasets/danluu-ingestion/ e datasets/incident-postmortem-assistant/;
não altera nada lá.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python ingestion/triagem/01_inventario.py

Saída:
    ingestion/triagem/saida/inventario.csv   uma linha por entrada do catálogo (240)
    resumo das contagens no terminal
"""
from __future__ import annotations

import collections
import csv
import json
import re
import unicodedata
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
DANLUU = ROOT / "datasets" / "danluu-ingestion"
RAW = DANLUU / "data" / "raw"
EDITORIAL = DANLUU / "data" / "reviews" / "editorial_reviews.csv"
AMOSTRA = DANLUU / "investigacao_independente" / "avaliacao_amostra_danluu.csv"
MAPA_IPA = ROOT / "datasets" / "incident-postmortem-assistant" / "mapeamento_corpus.csv"
SAIDA = Path(__file__).resolve().parent / "saida"

# Limiares (régua, P10)
PALAVRAS_CURTO = 300
LIMIAR_OUTRO_IDIOMA = 0.05   # fração de letras não latinas
LIMIAR_REPETICAO = 0.10      # fração de parágrafos repetidos
MIN_TITULOS_ARTIGO = 3       # títulos do corpo no HTML para considerar perda
MIN_ATUALIZACOES = 2         # updates de Statuspage para considerar perda
LIMIAR_PRESENCA = 0.5        # fração mínima de updates/datas presentes no JSON


def normalizar(texto: str) -> str:
    """Minúsculas, sem marcação Markdown e com espaços colapsados."""
    texto = re.sub(r"[*_`#>\[\]]", "", texto or "")
    return re.sub(r"\s+", " ", texto).strip().lower()


def fracao_nao_latina(texto: str) -> float:
    letras = [c for c in texto if c.isalpha()]
    if not letras:
        return 0.0
    nao_latinas = sum(1 for c in letras if not unicodedata.name(c, "").startswith("LATIN"))
    return nao_latinas / len(letras)


def fracao_repetida(texto: str) -> float:
    paragrafos = [p.strip() for p in texto.split("\n") if len(p.strip()) > 60]
    if not paragrafos:
        return 0.0
    contagem = collections.Counter(paragrafos)
    return sum(n - 1 for n in contagem.values()) / len(paragrafos)


def presente(trecho: str, texto_norm: str, tamanho: int = 60) -> bool:
    alvo = normalizar(trecho)[:tamanho]
    return bool(alvo) and alvo in texto_norm


def analisar_html(caminho: Path, texto_norm: str) -> dict:
    """Títulos do corpo do artigo e updates de Statuspage, e quantos chegaram ao JSON."""
    sopa = BeautifulSoup(caminho.read_bytes(), "html.parser")

    # Um título pertence ao artigo se o parágrafo seguinte foi extraído; isso
    # descarta "Related posts", chamadas de marketing etc.
    titulos_artigo = 0
    for h in sopa.find_all(["h2", "h3", "h4"]):
        p = h.find_next("p")
        if p and presente(p.get_text(" ", strip=True), texto_norm):
            titulos_artigo += 1

    updates = sopa.select(".update-row")
    corpos = [u.select_one(".update-body") for u in updates]
    datas = [u.find("small") for u in updates]
    corpos_ok = sum(1 for c in corpos if c and presente(c.get_text(" ", strip=True), texto_norm))
    datas_ok = sum(1 for d in datas if d and presente(d.get_text(" ", strip=True), texto_norm, 20))

    return {
        "titulos_artigo_html": titulos_artigo,
        "atualizacoes_html": len(updates),
        "atualizacoes_no_json": corpos_ok,
        "datas_atualizacoes_no_json": datas_ok,
    }


def hospedagem(manifesto: dict) -> str:
    url = manifesto.get("final_url") or manifesto.get("source_url") or ""
    if (manifesto.get("content_type") or "").startswith("application/pdf"):
        return "pdf"
    if "web.archive.org" in url:
        return "wayback"
    if re.search(r"status|statuspage", url):
        return "statuspage"
    return "outro"


def carregar_auxiliares() -> tuple[set[str], set[str], dict[str, str]]:
    aprovados = {r["catalog_id"] for r in csv.DictReader(EDITORIAL.open(encoding="utf-8"))
                 if r["editorial_decision"] == "approved"}
    amostra = {r["catalog_id"] for r in csv.DictReader(AMOSTRA.open(encoding="utf-8-sig"))}
    ref_ipa = {r["id_danluu"]: r["doc_id"]
               for r in csv.DictReader(MAPA_IPA.open(encoding="utf-8-sig")) if r["id_danluu"]}
    return aprovados, amostra, ref_ipa


def qualidade(problemas: list[str]) -> str:
    """P11 preliminar; o LLM ainda pode acrescentar marcações (comentários, rodapé, PDF)."""
    p = set(problemas)
    if p & {"nao_coletado", "vazio", "duplicado"}:
        return "inutilizavel"
    if p & {"titulos_perdidos", "atualizacoes_perdidas"}:
        return "precisa_reextracao"
    if p & {"outro_idioma", "repeticao"}:
        return "precisa_limpeza"
    return "ok"


def main() -> None:
    aprovados, amostra, ref_ipa = carregar_auxiliares()
    manifestos = [json.loads(p.read_text(encoding="utf-8"))
                  for p in sorted(RAW.glob("DAN-[0-9][0-9][0-9].json"))]

    # Duplicatas: só entre documentos com texto; o primeiro ID do grupo é mantido.
    por_hash = collections.defaultdict(list)
    for m in manifestos:
        if m.get("content_hash") and (m.get("word_count") or 0) > 0:
            por_hash[m["content_hash"]].append(m["catalog_id"])
    duplicado_de = {cid: ids[0] for ids in por_hash.values() for cid in ids[1:]}

    linhas = []
    for m in manifestos:
        cid = m["catalog_id"]
        extracao = DANLUU / "data" / "extracted" / f"{cid}.json"
        doc = json.loads(extracao.read_text(encoding="utf-8")) if extracao.exists() else m
        texto = doc.get("extracted_text") or ""
        palavras = doc.get("word_count") or 0
        problemas: list[str] = []
        html = {}

        if not extracao.exists():
            problemas.append("nao_coletado")
        elif palavras == 0:
            problemas.append("vazio")
        else:
            if palavras < PALAVRAS_CURTO:
                problemas.append("curto")
            if cid in duplicado_de:
                problemas.append("duplicado")
            if fracao_nao_latina(texto) > LIMIAR_OUTRO_IDIOMA:
                problemas.append("outro_idioma")
            if fracao_repetida(texto) > LIMIAR_REPETICAO:
                problemas.append("repeticao")

            raw_path = doc.get("raw_path") or ""
            if raw_path.endswith(".html") and (DANLUU / raw_path).exists():
                html = analisar_html(DANLUU / raw_path, normalizar(texto))
                titulos_json = len(re.findall(r"^#{1,6} ", texto, re.M))
                if (html["titulos_artigo_html"] >= MIN_TITULOS_ARTIGO
                        and titulos_json < html["titulos_artigo_html"] / 2):
                    problemas.append("titulos_perdidos")
                n = html["atualizacoes_html"]
                if n >= MIN_ATUALIZACOES and (
                        html["atualizacoes_no_json"] / n < LIMIAR_PRESENCA
                        or html["datas_atualizacoes_no_json"] / n < LIMIAR_PRESENCA):
                    problemas.append("atualizacoes_perdidas")

        linhas.append({
            "catalog_id": cid,
            "empresa": doc.get("company"),
            "titulo": doc.get("title") or "",
            "categoria_catalogo": doc.get("category"),
            "status_pipeline": doc.get("status"),
            "motivo_pipeline": ";".join(doc.get("review_reason") or []),
            "hospedagem": hospedagem(doc),
            "metodo_extracao": doc.get("extraction_method") or "",
            "palavras": palavras,
            "titulos_markdown_json": len(re.findall(r"^#{1,6} ", texto, re.M)),
            "titulos_artigo_html": html.get("titulos_artigo_html", ""),
            "atualizacoes_html": html.get("atualizacoes_html", ""),
            "atualizacoes_no_json": html.get("atualizacoes_no_json", ""),
            "fracao_nao_latina": round(fracao_nao_latina(texto), 3),
            "fracao_repetida": round(fracao_repetida(texto), 3),
            "duplicado_de": duplicado_de.get(cid, ""),
            "aprovado_e13": cid in aprovados,
            "amostra_independente": cid in amostra,
            "ref_avaliacao_ipa": ref_ipa.get(cid, ""),
            "p10_problemas_script": ";".join(problemas),
            "p11_qualidade_preliminar": qualidade(problemas),
        })

    SAIDA.mkdir(parents=True, exist_ok=True)
    destino = SAIDA / "inventario.csv"
    with destino.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=list(linhas[0]))
        escritor.writeheader()
        escritor.writerows(linhas)

    contar = collections.Counter
    print(f"Entradas do catálogo: {len(linhas)} -> {destino.relative_to(ROOT)}")
    print("\nP11 preliminar:")
    for valor, n in contar(l["p11_qualidade_preliminar"] for l in linhas).most_common():
        print(f"  {valor:20} {n}")
    print("\nP10 (marcações do script):")
    for valor, n in contar(p for l in linhas for p in l["p10_problemas_script"].split(";") if p).most_common():
        print(f"  {valor:22} {n}")
    print("\nHospedagem:")
    for valor, n in contar(l["hospedagem"] for l in linhas).most_common():
        print(f"  {valor:12} {n}")
    ja_avaliados = sum(1 for l in linhas if l["aprovado_e13"] or l["amostra_independente"])
    print(f"\nJá avaliados por humano (E1.3 ou amostra): {ja_avaliados}")
    print(f"Referenciados pela avaliação do IPA: {sum(1 for l in linhas if l['ref_avaliacao_ipa'])}")


if __name__ == "__main__":
    main()
