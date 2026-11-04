"""
Monta o corpus do danluu: um registro por documento, com o texto já limpo.

Quais documentos: os que têm ficha em ingestion/fichas/saida/ com triagem.catalogo `sim` ou
`parcial` (211). Ficam de fora `nao`, `nao_verificavel` e os `inutilizavel` (que não têm ficha).

Qual texto: o reextraído (ingestion/reextracao/extraidos/) quando existe, senão o original do
danluu. Os documentos do gabarito (DAN-053, DAN-183) ficam com o texto original nas fichas, por
causa do teste de regressão; no corpus eles entram com o texto reextraído, gerado aqui.

Limpeza (só remove blocos ou linhas inteiras; nenhuma frase é alterada, então os trechos das
fichas continuam existindo no texto):
1. parágrafos em outro idioma (escrita não latina), quando sobra texto latino suficiente;
2. parágrafos longos repetidos;
3. linhas sem letra nem número que não são estrutura (marcadores soltos, caracteres de largura
   zero, pontuação isolada). Ficam: linhas de tabela (com "|" ou "+"), réguas "---"/"===" e
   linhas dentro de blocos de código.

4. comentários de leitores: nos documentos com a marca `comentarios`, o texto é cortado onde os
   comentários começam (tabela CORTE_COMENTARIOS, ponto achado à mão em cada um). DAN-236 não é
   cortado: é uma issue do GitHub, e a discussão faz parte do relato.

5. títulos: quando o título da página não diz de que incidente se trata, vale o da tabela
   TITULO_MANUAL (o título da página fica em `page_title`).

Ao final confere se cada trecho das fichas existe no texto do corpus (mesma normalização do
validar_fichas.py) e lista os que não existem.

Só lê datasets/ e ingestion/; não altera nada fora de ingestion/corpus/.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/corpus/montar_corpus.py

Grava:
    ingestion/corpus/corpus.jsonl        um documento por linha
    ingestion/corpus/limpeza.csv         o que foi removido em cada documento
"""
from __future__ import annotations

import csv
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent
FICHAS = ROOT / "ingestion" / "fichas"
DANLUU = ROOT / "datasets" / "danluu-ingestion" / "data"


def modulo(caminho: Path, nome: str):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


prompts = modulo(FICHAS / "montar_prompts.py", "montar_prompts")      # limpar(), caminho_extraido()
validar = modulo(FICHAS / "validar_fichas.py", "validar_fichas")      # normalizar(), trechos_da_ficha()
reextrair = modulo(ROOT / "ingestion" / "reextracao" / "reextrair.py", "reextrair")

GABARITO = {p.stem for p in (FICHAS / "gabarito").glob("DAN-*.json")}
REEXTRAIR_LISTA = {r["catalog_id"] for r in csv.DictReader(
    (ROOT / "ingestion" / "reextracao" / "lista.csv").open(encoding="utf-8"))}
# texto a partir do qual começam os comentários de leitores (achado à mão em cada documento)
CORTE_COMENTARIOS = {
    "DAN-022": "Very cool. Any chance you’re going to release the source?",
    "DAN-025": "## 5 comments",
    "DAN-119": "## Jan\n\non 26 Mar 14",
    "DAN-187": "Robbie\nOctober 21st, 2013",
}
# título da página que não identifica o incidente -> título tirado do próprio documento
TITULO_MANUAL = {
    "DAN-191": "IT Infrastructure Resiliency Review (23 February 2017)",
}
ESTRUTURA = re.compile(r"[|+]|^[-=]{3,}$")


def tirar_linhas_vazias_de_sentido(texto: str) -> tuple[str, int]:
    """Remove linhas sem letra nem número que não são tabela, régua ou código."""
    saida, removidas, codigo = [], 0, False
    for linha in texto.split("\n"):
        s = linha.strip().replace("​", "").replace("‌", "").replace("﻿", "")
        if linha.strip().startswith("```"):
            codigo = not codigo
        elif not codigo and linha.strip() and not re.search(r"\w", s) and not ESTRUTURA.search(s):
            removidas += 1
            continue
        saida.append(linha)
    texto = "\n".join(saida)
    texto = re.sub(r"\n{3,}", "\n\n", texto)  # a remoção pode deixar parágrafos vazios
    return texto, removidas


def texto_do_documento(cid: str) -> tuple[str, str, dict]:
    """Devolve (texto, origem, metadados do arquivo de origem)."""
    if cid in GABARITO and cid in REEXTRAIR_LISTA:
        doc = reextrair.reextrair(cid)
        return doc["extracted_text"], "reextraido_corpus", doc
    caminho = prompts.caminho_extraido(cid)
    doc = json.loads(caminho.read_text(encoding="utf-8"))
    origem = "reextraido" if "reextracao" in caminho.parts else "original"
    return doc.get("extracted_text") or "", origem, doc


def main() -> None:
    catalogo = {r["catalog_id"]: r for r in csv.DictReader(
        (DANLUU / "catalog.csv").open(encoding="utf-8"))}
    registros, relatorio, faltando = [], [], []
    for caminho in sorted((FICHAS / "saida").glob("DAN-*.json")):
        ficha = json.loads(caminho.read_text(encoding="utf-8"))
        if ficha["triagem"]["catalogo"] not in ("sim", "parcial"):
            continue
        cid = ficha["catalog_id"]
        bruto, origem, doc = texto_do_documento(cid)
        texto, feito = prompts.limpar(bruto)
        texto, linhas = tirar_linhas_vazias_de_sentido(texto)
        if linhas:
            feito.append(f"{linhas} lines without letters or digits")
        problemas = list(ficha["triagem"].get("problemas_texto", []))
        if cid in CORTE_COMENTARIOS:
            pos = texto.find(CORTE_COMENTARIOS[cid])
            if pos < 0:
                raise SystemExit(f"{cid}: ponto de corte dos comentários não encontrado")
            removidas = len(texto[pos:].split())
            texto = texto[:pos].rstrip() + "\n"
            feito.append(f"reader comments cut ({removidas} words)")
            problemas = [x for x in problemas if x != "comentarios"]
        cat = catalogo.get(cid, {})
        inc = ficha.get("incidente") or {}
        registros.append({
            "catalog_id": cid,
            "company": cat.get("company") or doc.get("company"),
            "title": TITULO_MANUAL.get(cid, doc.get("title")),
            "page_title": doc.get("title"),
            "url": doc.get("source_url") or cat.get("url"),
            "incident_date": inc.get("data_incidente"),
            "text_source": origem,
            "catalogo": ficha["triagem"]["catalogo"],
            "problemas_texto": problemas,
            "cleaning": feito,
            "word_count": len(texto.split()),
            "text": texto,
        })
        relatorio.append({"catalog_id": cid, "text_source": origem,
                          "palavras_antes": len(bruto.split()), "palavras_depois": len(texto.split()),
                          "limpeza": "; ".join(feito)})
        # os trechos da ficha continuam no texto do corpus?
        if origem != "reextraido_corpus":  # gabarito: trechos foram validados contra o original
            norm = validar.normalizar(texto)
            for local, trecho in validar.trechos_da_ficha(ficha):
                if isinstance(trecho, str) and trecho not in texto and validar.normalizar(trecho) not in norm:
                    faltando.append((cid, local, trecho[:80]))

    with (PASTA / "corpus.jsonl").open("w", encoding="utf-8") as f:
        for r in registros:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (PASTA / "limpeza.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(relatorio[0]))
        w.writeheader()
        w.writerows(relatorio)

    origens = {}
    for r in registros:
        origens[r["text_source"]] = origens.get(r["text_source"], 0) + 1
    limpos = [r for r in relatorio if r["limpeza"]]
    print(f"{len(registros)} documentos -> {(PASTA / 'corpus.jsonl').relative_to(ROOT)}  origem: {origens}")
    print(f"{len(limpos)} documentos com alguma remoção:")
    for r in limpos:
        print(f"  {r['catalog_id']}: {r['limpeza']}  ({r['palavras_antes']} -> {r['palavras_depois']} palavras)")
    print(f"trechos de fichas ausentes no corpus: {len(faltando)}")
    for cid, local, trecho in faltando[:20]:
        print(f"  {cid} {local}: {trecho!r}")


if __name__ == "__main__":
    main()
