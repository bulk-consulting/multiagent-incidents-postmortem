"""
Compara fichas geradas com o gabarito, campo a campo (teste de regressão do prompt).

Compara só campos de classificação, que têm resposta certa: triagem, categoria, status,
níveis, presença ou ausência de gatilho, duração, confiança. Textos livres e trechos
não entram (cada extração escreve diferente); as contagens de fatores, passos e ações
aparecem só como informação.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python ingestion/fichas/comparar_fichas.py ingestion/fichas/saida_teste
    multiagent_env/bin/python ingestion/fichas/comparar_fichas.py <pasta_gerada> [<pasta_gabarito>]

Saída:
    concordância por campo e lista de divergências no terminal
    <pasta_gerada>/comparacao.csv
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

GABARITO = Path(__file__).resolve().parent / "gabarito"


def pegar(ficha: dict, caminho: str):
    """Lê 'a.b.c' da ficha; None se algum nível faltar ou for null."""
    no = ficha
    for parte in caminho.split("."):
        if not isinstance(no, dict):
            return None
        no = no.get(parte)
    return no


def presenca(valor) -> str:
    return "preenchido" if valor else "null"


def duracao(valor) -> str:
    return str(valor["minutos"]) if isinstance(valor, dict) else "null"


# (nome exibido, caminho na ficha, conversão)
CAMPOS = [
    ("catalogo", "triagem.catalogo", str),
    ("autoria", "triagem.autoria", str),
    ("tipo", "triagem.tipo", str),
    ("dominio", "triagem.dominio", str),
    ("seguranca", "triagem.seguranca", str),
    ("problemas_texto", "triagem.problemas_texto", lambda v: ",".join(sorted(v or [])) or "-"),
    ("data_incidente", "incidente.data_incidente", str),
    ("status_relatorio", "incidente.status_relatorio", str),
    ("categoria_causa", "incidente.categoria_causa", str),
    ("deteccao.forma", "incidente.deteccao.forma", str),
    ("deteccao.descricao", "incidente.deteccao.descricao", presenca),
    ("gatilho", "incidente.gatilho", presenca),
    ("causa_raiz.status", "incidente.causa_raiz.status", str),
    ("mudanca_causadora", "incidente.mudanca_causadora.nivel", str),
    ("mitigacao", "incidente.mitigacao.nivel", str),
    ("prevencao", "incidente.prevencao.nivel", str),
    ("duracao", "incidente.duracao", duracao),
    ("perguntas_em_aberto", "incidente.perguntas_em_aberto", lambda v: "sim" if v else "nao"),
    ("confianca", "confianca", str),
]

CONTAGENS = [
    ("fatores", "incidente.fatores_contribuintes"),
    ("passos", "incidente.mitigacao.passos"),
    ("acoes", "incidente.prevencao.acoes"),
]


def main() -> None:
    if not 1 <= len(sys.argv) - 1 <= 2:
        sys.exit(__doc__)
    gerada = Path(sys.argv[1])
    gabarito = Path(sys.argv[2]) if len(sys.argv) > 2 else GABARITO

    ids = sorted(p.stem for p in gabarito.glob("DAN-*.json"))
    faltando = [i for i in ids if not (gerada / f"{i}.json").exists()]
    ids = [i for i in ids if i not in faltando]
    if not ids:
        sys.exit(f"Nenhuma ficha de {gabarito} encontrada em {gerada}")

    linhas = []
    for cid in ids:
        ref = json.loads((gabarito / f"{cid}.json").read_text(encoding="utf-8"))
        nova = json.loads((gerada / f"{cid}.json").read_text(encoding="utf-8"))
        for nome, caminho, conv in CAMPOS:
            a, b = conv(pegar(ref, caminho)), conv(pegar(nova, caminho))
            linhas.append({"catalog_id": cid, "campo": nome, "gabarito": a, "gerada": b, "igual": a == b})
        for nome, caminho in CONTAGENS:
            a, b = len(pegar(ref, caminho) or []), len(pegar(nova, caminho) or [])
            linhas.append({"catalog_id": cid, "campo": f"n_{nome}", "gabarito": a, "gerada": b, "igual": None})

    print(f"Concordância por campo ({len(ids)} fichas):")
    for nome, _, _ in CAMPOS:
        iguais = sum(1 for l in linhas if l["campo"] == nome and l["igual"])
        print(f"  {nome:20} {iguais:>2}/{len(ids)}")
    comparadas = [l for l in linhas if l["igual"] is not None]
    total = sum(1 for l in comparadas if l["igual"])
    print(f"  {'TOTAL':20} {total}/{len(comparadas)} ({100 * total / len(comparadas):.0f}%)")

    print("\nDivergências:")
    for l in comparadas:
        if not l["igual"]:
            print(f"  {l['catalog_id']}  {l['campo']:20} gabarito={l['gabarito']!s:22} gerada={l['gerada']}")

    print("\nContagens (só informação: gabarito -> gerada):")
    for cid in ids:
        partes = [f"{l['campo'][2:]} {l['gabarito']}->{l['gerada']}"
                  for l in linhas if l["catalog_id"] == cid and l["igual"] is None]
        print(f"  {cid}  " + "  ".join(partes))
    if faltando:
        print(f"\nSem ficha gerada: {', '.join(faltando)}")

    with (gerada / "comparacao.csv").open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=["catalog_id", "campo", "gabarito", "gerada", "igual"])
        escritor.writeheader()
        escritor.writerows(linhas)
    print(f"\n-> {gerada / 'comparacao.csv'}")


if __name__ == "__main__":
    main()
