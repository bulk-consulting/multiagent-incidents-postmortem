"""
Gera o material para o gabarito humano da régua (docs/triagem/regua.md):
uma planilha em branco e um arquivo de leitura por documento.

A seleção cobre as respostas da régua (tipos de texto, domínios, níveis de
causa, problemas de extração) e inclui documentos sorteados entre os que
nenhuma avaliação anterior leu. A planilha e os textos não mostram o motivo da
escolha nem avaliações anteriores, para que a classificação seja feita às cegas.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python ingestion/triagem/02_gerar_gabarito.py
    multiagent_env/bin/python ingestion/triagem/02_gerar_gabarito.py --sobrescrever

Requer ingestion/triagem/saida/inventario.csv (01_inventario.py).

Saída em ingestion/triagem/gabarito/:
    gabarito.csv     planilha para preencher
    textos/          um .md por documento, com a descrição do catálogo e o texto extraído
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DANLUU = ROOT / "datasets" / "danluu-ingestion"
INVENTARIO = Path(__file__).resolve().parent / "saida" / "inventario.csv"
DESTINO = Path(__file__).resolve().parent / "gabarito"

# Escolhidos para cobrir as respostas da régua. O motivo de cada um fica só
# aqui, fora do material de leitura, para não induzir a classificação.
ESCOLHIDOS = {
    "DAN-009": "post-mortem completo; mudança específica",
    "DAN-143": "títulos perdidos na extração",
    "DAN-230": "causa incerta",
    "DAN-135": "Statuspage com atualizações perdidas",
    "DAN-235": "só atualizações de status",
    "DAN-162": "relatório periódico; referenciado pela avaliação do IPA",
    "DAN-022": "artigo técnico em que o incidente é uma parte; comentários",
    "DAN-068": "infraestrutura física de datacenter",
    "DAN-140": "segurança: ataque",
    "DAN-204": "exposição de dados sem ataque",
    "DAN-200": "fora de TI",
    "DAN-121": "autoria: empresa escrevendo sobre o próprio serviço em blog institucional",
    "DAN-074": "fonte secundária (imprensa); pode não corresponder ao catálogo",
    "DAN-002": "outro idioma no texto",
    "DAN-045": "texto curto com mudança específica",
    "DAN-104": "incidente conhecido; referenciado pela avaliação do IPA",
    "DAN-078": "títulos perdidos; referenciado pela avaliação do IPA",
    "DAN-146": "texto muito curto; pode não corresponder ao catálogo",
    "DAN-088": "lista de e-mails (P3 = outro)",
}
SORTEADOS = 3
SEMENTE = 42
PALAVRAS_SORTEIO = (300, 4000)  # faixa legível em 10 a 15 minutos

COLUNAS = [
    "ordem", "catalog_id", "empresa", "palavras", "arquivo_texto", "url_original",
    "p1_catalogo", "p2_autoria", "p3_tipo", "p4_dominio", "p5_seguranca",
    "p6_causa", "p7_recuperacao", "p8_mudanca", "p9_prevencao",
    "p10_problemas_leitura", "p10_problemas_script",
    "evidencia_p6", "confianca", "minutos", "observacoes",
]


def sortear(inventario: dict[str, dict]) -> list[str]:
    """Sorteia entre os documentos utilizáveis que nenhuma avaliação anterior leu."""
    minimo, maximo = PALAVRAS_SORTEIO
    candidatos = sorted(
        cid for cid, r in inventario.items()
        if cid not in ESCOLHIDOS
        and r["aprovado_e13"] == "False"
        and r["amostra_independente"] == "False"
        and r["p11_qualidade_preliminar"] != "inutilizavel"
        and minimo <= int(r["palavras"]) <= maximo
    )
    return random.Random(SEMENTE).sample(candidatos, SORTEADOS)


def arquivo_leitura(cid: str, catalogo: dict, doc: dict) -> str:
    return "\n".join([
        f"# {cid} — {doc.get('company')}",
        "",
        f"- **Título extraído:** {doc.get('title') or '(sem título)'}",
        f"- **URL do catálogo:** {doc.get('source_url')}",
        f"- **URL final:** {doc.get('final_url')}",
        f"- **Arquivo original:** `datasets/danluu-ingestion/{doc.get('raw_path')}`",
        f"- **Palavras:** {doc.get('word_count')}",
        "",
        "## Descrição do catálogo (para a P1)",
        "",
        catalogo["description"],
        "",
        "## Texto extraído (é isto que o LLM vai ler)",
        "",
        doc.get("extracted_text") or "(vazio)",
        "",
    ])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sobrescrever", action="store_true",
                    help="regera a planilha mesmo que já exista (apaga o que foi preenchido)")
    args = ap.parse_args()

    planilha = DESTINO / "gabarito.csv"
    if planilha.exists() and not args.sobrescrever:
        sys.exit(f"{planilha.relative_to(ROOT)} já existe; use --sobrescrever para regerar.")

    inventario = {r["catalog_id"]: r for r in csv.DictReader(INVENTARIO.open(encoding="utf-8"))}
    catalogo = {r["catalog_id"]: r for r in
                csv.DictReader((DANLUU / "data" / "catalog.csv").open(encoding="utf-8"))}

    ids = list(ESCOLHIDOS) + sortear(inventario)
    # Ordem embaralhada para que documentos parecidos não fiquem em sequência.
    random.Random(SEMENTE).shuffle(ids)

    textos = DESTINO / "textos"
    textos.mkdir(parents=True, exist_ok=True)
    linhas = []
    for ordem, cid in enumerate(ids, start=1):
        doc = json.loads((DANLUU / "data" / "extracted" / f"{cid}.json").read_text(encoding="utf-8"))
        nome = f"{ordem:02d}_{cid}.md"
        (textos / nome).write_text(arquivo_leitura(cid, catalogo[cid], doc), encoding="utf-8")
        linhas.append({
            "ordem": ordem,
            "catalog_id": cid,
            "empresa": doc.get("company"),
            "palavras": doc.get("word_count"),
            "arquivo_texto": f"textos/{nome}",
            "url_original": doc.get("source_url"),
            "p10_problemas_script": inventario[cid]["p10_problemas_script"],
        })

    with planilha.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS)
        escritor.writeheader()
        escritor.writerows(linhas)

    print(f"{len(linhas)} documentos -> {planilha.relative_to(ROOT)}")
    print(f"Palavras no total: {sum(int(l['palavras']) for l in linhas)}")


if __name__ == "__main__":
    main()
