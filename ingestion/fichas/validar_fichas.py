"""
Validador das fichas de post-mortem (peça 4; ver FICHA.md).

Para cada ficha confere:
  1. formato e valores contra ficha.schema.json;
  2. se cada trecho citado existe no texto extraído do documento original;
  3. avisos que o schema não cobre (palavras de culpa no texto livre, nome do arquivo).

Só lê datasets/danluu-ingestion/; não altera nada lá.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python ingestion/fichas/validar_fichas.py              # todas em saida/
    multiagent_env/bin/python ingestion/fichas/validar_fichas.py saida/DAN-164.json ...

Saída:
    resultado por ficha no terminal
    validacao.csv na pasta das fichas validadas (a do primeiro arquivo)
    código de saída 1 se alguma ficha falhar
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent
SCHEMA = PASTA / "ficha.schema.json"
SAIDA = PASTA / "saida"
EXTRAIDOS = ROOT / "datasets" / "danluu-ingestion" / "data" / "extracted"
REEXTRAIDOS = ROOT / "ingestion" / "reextracao" / "extraidos"


def caminho_extraido(cid: str) -> Path:
    """Texto reextraído (ingestion/reextracao/extraidos/) quando existir; senão, o original do danluu."""
    novo = REEXTRAIDOS / f"{cid}.json"
    return novo if novo.exists() else EXTRAIDOS / f"{cid}.json"

# Mesma ideia do validate.py do agent-postmortems: palavras de culpa não entram
# nos campos factuais. Aqui é aviso, não falha.
PALAVRAS_CULPA = [
    "negligent", "reckless", "stupid", "incompetent", "careless", "clueless",
    "idiotic", "pathetic", "shameful", "disgraceful", "terrible", "horrible",
    "awful", "laughable", "sloppy", "lazy",
]

ASPAS = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"',
                       "–": "-", "—": "-", " ": " "})


def normalizar(texto: str) -> str:
    """Tolera só diferenças de forma: espaços, aspas tipográficas, marcação Markdown e caixa."""
    texto = unicodedata.normalize("NFKC", texto).translate(ASPAS)
    texto = re.sub(r"[*_`#>]", "", texto)
    return re.sub(r"\s+", " ", texto).strip().casefold()


def trechos_da_ficha(no, caminho: str = ""):
    """Percorre a ficha e devolve (caminho, trecho) de toda lista 'trechos'."""
    if isinstance(no, dict):
        for chave, valor in no.items():
            sub = f"{caminho}.{chave}" if caminho else chave
            if chave == "trechos" and isinstance(valor, list):
                for i, trecho in enumerate(valor):
                    yield f"{sub}[{i}]", trecho
            else:
                yield from trechos_da_ficha(valor, sub)
    elif isinstance(no, list):
        for i, item in enumerate(no):
            yield from trechos_da_ficha(item, f"{caminho}[{i}]")


def textos_livres(no):
    """Campos de texto livre escritos pelo LLM (para o aviso de palavras de culpa)."""
    if isinstance(no, dict):
        for chave, valor in no.items():
            if chave in ("texto", "resumo", "motivo_confianca_baixa", "observacoes") and isinstance(valor, str):
                yield chave, valor
            elif chave == "perguntas_em_aberto" and isinstance(valor, list):
                yield from ((chave, v) for v in valor if isinstance(v, str))
            elif chave != "trechos":
                yield from textos_livres(valor)
    elif isinstance(no, list):
        for item in no:
            yield from textos_livres(item)


def validar(caminho: Path, validador: Draft202012Validator) -> dict:
    erros: list[str] = []
    avisos: list[str] = []
    contagem = {"exato": 0, "normalizado": 0, "ausente": 0}

    try:
        ficha = json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return {"arquivo": caminho.name, "catalog_id": "", "ok": False,
                "erros": [f"JSON inválido: {e}"], "avisos": [], **contagem}

    for erro in sorted(validador.iter_errors(ficha), key=lambda e: list(e.absolute_path)):
        local = "/".join(map(str, erro.absolute_path)) or "(raiz)"
        erros.append(f"schema {local}: {erro.message[:120]}")

    cid = ficha.get("catalog_id", "")
    if cid and caminho.stem != cid:
        avisos.append(f"nome do arquivo ({caminho.name}) diferente do catalog_id ({cid})")

    extraido = caminho_extraido(cid)
    if not extraido.exists():
        erros.append(f"documento original não encontrado: {extraido.relative_to(ROOT)}")
    else:
        original = json.loads(extraido.read_text(encoding="utf-8")).get("extracted_text") or ""
        original_norm = normalizar(original)
        for local, trecho in trechos_da_ficha(ficha):
            if not isinstance(trecho, str):
                continue
            if trecho in original:
                contagem["exato"] += 1
            elif normalizar(trecho) in original_norm:
                contagem["normalizado"] += 1
            else:
                contagem["ausente"] += 1
                erros.append(f"trecho não encontrado no original {local}: {trecho[:80]!r}")

    for campo, texto in textos_livres(ficha):
        for palavra in PALAVRAS_CULPA:
            if re.search(rf"\b{palavra}\b", texto, re.I):
                avisos.append(f"palavra de culpa '{palavra}' em {campo}")

    return {"arquivo": caminho.name, "catalog_id": cid, "ok": not erros,
            "erros": erros, "avisos": avisos, **contagem}


def main() -> None:
    validador = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    arquivos = [Path(a) for a in sys.argv[1:]] or sorted(SAIDA.glob("DAN-*.json"))
    if not arquivos:
        sys.exit(f"Nenhuma ficha encontrada em {SAIDA.relative_to(ROOT)}")

    resultados = [validar(a, validador) for a in arquivos]
    for r in resultados:
        trechos = r["exato"] + r["normalizado"] + r["ausente"]
        print(f"{'OK   ' if r['ok'] else 'FALHA'} {r['arquivo']:14} trechos: {trechos} "
              f"(exatos {r['exato']}, normalizados {r['normalizado']}, ausentes {r['ausente']})")
        for e in r["erros"]:
            print(f"      erro:  {e}")
        for a in r["avisos"]:
            print(f"      aviso: {a}")

    relatorio = arquivos[0].resolve().parent / "validacao.csv"
    with relatorio.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["arquivo", "catalog_id", "ok", "trechos_exatos", "trechos_normalizados",
                           "trechos_ausentes", "erros", "avisos"])
        for r in resultados:
            escritor.writerow([r["arquivo"], r["catalog_id"], r["ok"], r["exato"], r["normalizado"],
                               r["ausente"], " | ".join(r["erros"]), " | ".join(r["avisos"])])

    falhas = sum(1 for r in resultados if not r["ok"])
    print(f"\n{len(resultados)} fichas: {len(resultados) - falhas} ok, {falhas} com falha "
          f"-> {relatorio}")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
