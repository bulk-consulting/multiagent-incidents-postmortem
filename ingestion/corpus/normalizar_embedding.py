"""
Normalização do texto que gera o vetor (embedding). Não altera o texto guardado como `content`
do chunk, que continua igual ao do corpus (e, portanto, aos trechos das fichas).

Ajustes, nesta ordem:
1. tabelas: linhas separadoras (|---|---|, +----+, ----|----) saem; linhas de tabela viram as
   células não vazias separadas por " | ";
2. links: [texto](url) vira "texto", ![alt](url) vira "alt", e URLs soltas viram "[link]";
3. escapes do Markdown: "\\_" vira "_", "\\~" vira "~" etc.;
4. tags HTML que sobraram (<sup>, </sup>, <br>...) saem, ficando o conteúdo;
5. espaços repetidos dentro da linha viram um só.

Uso como módulo:   normalizar_para_embedding(texto) -> str
Uso como script (relatório sobre o corpus, sem gravar nada):
    multiagent_env/bin/python -I ingestion/corpus/normalizar_embedding.py [DAN-xxx ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent

SEPARADOR = re.compile(r"^\s*[|+]?[\s:|+=-]*-{3,}[\s:|+=-]*[|+]?\s*$")
LINHA_TABELA = re.compile(r"^\s*\|.*\|\s*$")
CELULA = re.compile(r"(?<!\\)\|")
LINK_MD = re.compile(r"(!?)\[([^\]]*)\]\((?:[^()\s]|\([^()]*\))+\)")
URL = re.compile(r"(?:https?://|www\.)[^\s<>\"')\]]+")
ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!~|<>])")
TAG = re.compile(r"</?(?:sup|sub|br|span|div|p|a|b|i|em|strong|u|small)\b[^>]*>", re.I)


def tabela(linha: str) -> str | None:
    """None se a linha deve sair; senão a linha (reescrita se for linha de tabela)."""
    if SEPARADOR.match(linha):
        return None
    if LINHA_TABELA.match(linha):
        celulas = [c.strip() for c in CELULA.split(linha.strip().strip("|"))]
        celulas = [c for c in celulas if c]
        return " | ".join(celulas) if celulas else None
    return linha


def normalizar_para_embedding(texto: str) -> str:
    linhas = []
    for linha in texto.split("\n"):
        linha = tabela(linha)
        if linha is None:
            continue
        linha = LINK_MD.sub(lambda m: m.group(2), linha)
        linha = URL.sub("[link]", linha)
        linha = ESCAPE.sub(r"\1", linha)
        linha = TAG.sub("", linha)
        linha = re.sub(r"[ \t\xa0\u2009\u202f]{2,}", " ", linha.replace("\xa0", " ")).rstrip()
        linhas.append(linha)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()


def main() -> None:
    alvo = set(sys.argv[1:])
    docs = [json.loads(l) for l in (PASTA / "corpus.jsonl").open(encoding="utf-8")]
    contagem = {"separadores": 0, "linhas_tabela": 0, "links_md": 0, "urls": 0, "escapes": 0, "tags": 0}
    afetados = {k: set() for k in contagem}
    for d in docs:
        t = d["text"]
        n = {
            "separadores": sum(bool(SEPARADOR.match(l)) for l in t.split("\n")),
            "linhas_tabela": sum(bool(LINHA_TABELA.match(l)) and not SEPARADOR.match(l) for l in t.split("\n")),
            "links_md": len(LINK_MD.findall(t)),
            "urls": len(URL.findall(LINK_MD.sub("", t))),
            "escapes": len(ESCAPE.findall(t)),
            "tags": len(TAG.findall(t)),
        }
        for k, v in n.items():
            contagem[k] += v
            if v:
                afetados[k].add(d["catalog_id"])
        if d["catalog_id"] in alvo:
            novo = normalizar_para_embedding(t)
            print(f"===== {d['catalog_id']} ({len(t)} -> {len(novo)} caracteres)")
            antes = [l for l in t.split("\n") if ESCAPE.search(l) or URL.search(l) or LINHA_TABELA.match(l)][:6]
            for l in antes:
                print("  ANTES :", l[:160])
                print("  DEPOIS:", normalizar_para_embedding(l)[:160] or "(linha removida)")
    print(f"{len(docs)} documentos")
    for k, v in contagem.items():
        print(f"  {k}: {v} ocorrências em {len(afetados[k])} documentos")


if __name__ == "__main__":
    main()
