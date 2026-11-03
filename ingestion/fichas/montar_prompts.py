"""
Monta o prompt de extração já preenchido para cada documento (peça 2; ver FICHA.md).

Lê o modelo prompt_extracao.md, tira o comentário interno do topo e preenche o bloco
INPUT com os dados do catálogo e o texto extraído. O resultado é o texto exato que o
modelo extrator recebe, sem nada desta conversa.

Antes de entrar no prompt, o texto passa por uma limpeza que só remove parágrafos
inteiros, sem alterar nenhum: cópias em outro idioma (parágrafos majoritariamente em
escrita não latina, quando sobra texto latino suficiente) e parágrafos longos repetidos.
Assim todo trecho citado continua existindo no extracted_text original, que é contra
o que o validar_fichas.py confere.

Só lê datasets/danluu-ingestion/; não altera nada lá.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python ingestion/fichas/montar_prompts.py DAN-024 DAN-027 ...
    multiagent_env/bin/python ingestion/fichas/montar_prompts.py --gabarito   # os ids de gabarito/
    multiagent_env/bin/python ingestion/fichas/montar_prompts.py --lote 01    # um lote de lotes/lotes.csv

Saída:
    ingestion/fichas/prompts_prontos/DAN-xxx.txt
    ingestion/fichas/prompts_prontos/lote_NN/DAN-xxx.txt  (com --lote; a pasta é recriada)
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent
MODELO = PASTA / "prompt_extracao.md"
GABARITO = PASTA / "gabarito"
SAIDA = PASTA / "prompts_prontos"
LOTES = PASTA / "lotes" / "lotes.csv"
DANLUU = ROOT / "datasets" / "danluu-ingestion" / "data"

MIN_LATINO = 1000      # só remove outros idiomas se sobrar pelo menos isso de texto latino
MIN_REPETIDO = 200     # parágrafos repetidos menores que isso ficam (linhas de tabela, títulos)


def fracao_nao_latina(paragrafo: str) -> float:
    letras = [c for c in paragrafo if c.isalpha()]
    if not letras:
        return 0.0
    return sum(1 for c in letras if ord(c) > 0x024F) / len(letras)


def limpar(texto: str) -> tuple[str, list[str]]:
    """Remove parágrafos em outro idioma e parágrafos longos repetidos; devolve o que fez."""
    paragrafos = texto.split("\n\n")
    feito = []
    latinos = [p for p in paragrafos if fracao_nao_latina(p) < 0.3]
    if len(latinos) < len(paragrafos) and sum(map(len, latinos)) >= MIN_LATINO:
        feito.append(f"{len(paragrafos) - len(latinos)} paragraphs in another language")
        paragrafos = latinos
    vistos, unicos = set(), []
    for p in paragrafos:
        chave = p.strip()
        if len(chave) >= MIN_REPETIDO and chave in vistos:
            continue
        vistos.add(chave)
        unicos.append(p)
    if len(unicos) < len(paragrafos):
        feito.append(f"{len(paragrafos) - len(unicos)} repeated paragraphs")
    return "\n\n".join(unicos), feito


def main() -> None:
    args = sys.argv[1:]
    saida = SAIDA
    if args == ["--gabarito"]:
        ids = sorted(p.stem for p in GABARITO.glob("DAN-*.json"))
    elif len(args) == 2 and args[0] == "--lote":
        lote = args[1].zfill(2)
        ids = [r["catalog_id"] for r in csv.DictReader(LOTES.open(encoding="utf-8")) if r["lote"] == lote]
        if not ids:
            sys.exit(f"Lote {lote} não existe em {LOTES.relative_to(ROOT)}")
        saida = SAIDA / f"lote_{lote}"
        for velho in saida.glob("*.txt"):
            velho.unlink()
    else:
        ids = args
    if not ids:
        sys.exit(__doc__)

    modelo = MODELO.read_text(encoding="utf-8")
    modelo = re.sub(r"\A<!--.*?-->\s*", "", modelo, flags=re.S)
    catalogo = {r["catalog_id"]: r for r in csv.DictReader(
        (DANLUU / "catalog.csv").open(encoding="utf-8"))}

    saida.mkdir(parents=True, exist_ok=True)
    for cid in ids:
        doc = json.loads((DANLUU / "extracted" / f"{cid}.json").read_text(encoding="utf-8"))
        cat = catalogo[cid]
        extraido, feito = limpar(doc.get("extracted_text") or "")
        rotulo = "Document (extracted text):"
        if feito:
            rotulo = ("Document (extracted text; removed before this prompt: " + ", ".join(feito)
                      + ". Quote only from what follows):")
        # replace sequencial: o texto extraído entra por último para que chaves dentro
        # dele nunca sejam confundidas com campos do modelo
        texto = (modelo
                 .replace("{catalog_id}", cid)
                 .replace("{company}", cat["company"])
                 .replace("{catalog_description}", cat["description"])
                 .replace("{source_url}", doc.get("source_url") or cat["url"])
                 .replace("Document (extracted text):", rotulo)
                 .replace("{extracted_text}", extraido))
        (saida / f"{cid}.txt").write_text(texto, encoding="utf-8")
        nota = f"  [limpeza: {', '.join(feito)}]" if feito else ""
        print(f"{cid}: {len(texto):>7} caracteres -> {(saida / f'{cid}.txt').relative_to(ROOT)}{nota}")


if __name__ == "__main__":
    main()
