"""
Monta o prompt de extração já preenchido para cada documento (peça 2; ver FICHA.md).

Lê o modelo prompt_extracao.md, tira o comentário interno do topo e preenche o bloco
INPUT com os dados do catálogo e o texto extraído. O resultado é o texto exato que o
modelo extrator recebe, sem nada desta conversa.

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
        # replace sequencial: o texto extraído entra por último para que chaves dentro
        # dele nunca sejam confundidas com campos do modelo
        texto = (modelo
                 .replace("{catalog_id}", cid)
                 .replace("{company}", cat["company"])
                 .replace("{catalog_description}", cat["description"])
                 .replace("{source_url}", doc.get("source_url") or cat["url"])
                 .replace("{extracted_text}", doc.get("extracted_text") or ""))
        (saida / f"{cid}.txt").write_text(texto, encoding="utf-8")
        print(f"{cid}: {len(texto):>7} caracteres -> {(saida / f'{cid}.txt').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
