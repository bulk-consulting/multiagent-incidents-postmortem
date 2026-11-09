"""
Avalia a busca de documentos com um modelo de embedding, usando os vetores já gerados
(ingestion/corpus/embeddings/<modelo>/) e as suítes de perguntas (suite_ipa.json, suite_propria.json
e suite_mari.json, esta fora do total "TODAS").

Para cada pergunta, os documentos são ranqueados pela maior similaridade entre a pergunta e os
chunks de cada documento, em cinco índices:
- resumo+texto:  resumo do danluu + chunks do texto completo (etapa 1 da busca, o índice usado)
- resumo:        só o resumo do danluu (um chunk por incidente)
- texto:         só os chunks do texto completo
- fichas:        só os chunks das fichas (etapa 1 até a versão anterior; as fichas agora são opcionais)
- fichas+texto:  fichas + texto
Os índices com fichas só são avaliados se houver vetores de fichas.

Métricas por pergunta com resposta: posição do documento esperado (rank); daí hit@1, hit@3, hit@5 e
MRR (posições além de 20 contam 0). Perguntas sem resposta guardam a maior similaridade (para
escolher depois um limiar de "não achei").

Uso (a partir da raiz do repositório), um modelo por processo:
    multiagent_env/bin/python -I ingestion/avaliacao/avaliar.py e5
    multiagent_env/bin/python -I ingestion/avaliacao/avaliar.py --resumo   # tabelas dos modelos já avaliados

Grava: ingestion/avaliacao/resultados/<modelo>.json
"""
from __future__ import annotations

import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent
EMB = ROOT / "ingestion" / "corpus" / "embeddings"
RES = PASTA / "resultados"
INDICES = ("resumo+texto", "resumo", "texto", "fichas", "fichas+texto")
PRINCIPAL = "resumo+texto"
SUITES = ("suite_ipa.json", "suite_propria.json", "suite_mari.json")
MAX_RANK = 20


def carregar_casos() -> list[dict]:
    casos = []
    for nome in SUITES:
        for c in json.loads((PASTA / nome).read_text(encoding="utf-8"))["casos"]:
            casos.append({**c, "suite": nome.split("_")[1].split(".")[0]})
    return casos


def ranquear(sims: np.ndarray, doc_de_chunk: np.ndarray, n_docs: int) -> tuple[np.ndarray, np.ndarray]:
    """Nota de cada documento = maior similaridade entre seus chunks; devolve (ordem, notas)."""
    notas = np.full(n_docs, -np.inf, dtype=np.float32)
    np.maximum.at(notas, doc_de_chunk, sims)
    return np.argsort(-notas), notas


def avaliar(chave: str) -> None:
    spec = importlib.util.spec_from_file_location("g", ROOT / "ingestion" / "corpus" / "gerar_embeddings.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    cfg = g.MODELOS[chave]

    vet, docs_chunk = {}, {}
    for nome in ("resumo", "texto", "fichas"):
        if not (EMB / chave / f"{nome}.npy").exists():
            continue
        vet[nome] = np.load(EMB / chave / f"{nome}.npy").astype(np.float32)
        docs_chunk[nome] = [i.split(":")[0] for i in json.loads((EMB / chave / f"{nome}_ids.json").read_text())]
    docs = sorted(set().union(*docs_chunk.values()))
    pos = {d: k for k, d in enumerate(docs)}
    for a, b in (("resumo", "texto"), ("fichas", "texto")):
        if a in vet and b in vet:
            vet[f"{a}+{b}"] = np.vstack([vet[a], vet[b]])
            docs_chunk[f"{a}+{b}"] = docs_chunk[a] + docs_chunk[b]
    indices = [n for n in INDICES if n in vet]
    idx = {n: np.array([pos[d] for d in docs_chunk[n]]) for n in indices}

    casos = carregar_casos()
    modelo, _ = g.carregar_modelo(chave)
    q = modelo.encode([cfg["prefixo_query"] + c["pergunta"] for c in casos], batch_size=32,
                      normalize_embeddings=True, convert_to_numpy=True).astype(np.float32)

    saida = []
    for c, qv in zip(casos, q):
        r = {k: c[k] for k in ("id", "suite", "idioma", "variante", "dificuldade", "esperado")}
        for n in indices:
            ordem, notas = ranquear(vet[n] @ qv, idx[n], len(docs))
            top = [docs[i] for i in ordem[:MAX_RANK]]
            rank = next((k + 1 for k, d in enumerate(top) if d in c["esperado"]), None)
            r[n] = {"rank": rank, "top5": top[:5], "nota_top1": float(notas[ordem[0]])}
        saida.append(r)
    RES.mkdir(exist_ok=True)
    (RES / f"{chave}.json").write_text(json.dumps({"modelo": cfg["nome"], "casos": saida}, ensure_ascii=False, indent=1),
                                       encoding="utf-8")
    print(f"{chave}: {len(saida)} perguntas avaliadas -> {(RES / f'{chave}.json').relative_to(ROOT)}")


def metricas(linhas: list[dict], indice: str) -> dict:
    ranks = [l[indice]["rank"] for l in linhas]
    n = len(ranks)
    hit = lambda k: sum(1 for r in ranks if r and r <= k) / n
    return {"n": n, "hit@1": hit(1), "hit@3": hit(3), "hit@5": hit(5),
            "mrr": sum(1 / r for r in ranks if r) / n}


def resumo() -> None:
    arquivos = sorted(RES.glob("*.json"))
    dados = {a.stem: json.loads(a.read_text(encoding="utf-8"))["casos"] for a in arquivos}
    print("Perguntas com resposta (documento esperado entre os primeiros):\n")
    cortes = [("TODAS", lambda l: l["suite"] != "mari"),
              ("sintoma", lambda l: l["variante"] == "sintoma"),
              ("causa", lambda l: l["variante"] == "causa"),
              ("sintoma pt", lambda l: l["variante"] == "sintoma" and l["idioma"] == "pt"),
              ("sintoma en", lambda l: l["variante"] == "sintoma" and l["idioma"] == "en"),
              ("sintoma difícil", lambda l: l["variante"] == "sintoma" and l["dificuldade"] == "hard"),
              ("IPA (todas)", lambda l: l["suite"] == "ipa"),
              ("própria (todas)", lambda l: l["suite"] == "propria"),
              ("Mari pt", lambda l: l["suite"] == "mari" and l["idioma"] == "pt"),
              ("Mari en", lambda l: l["suite"] == "mari" and l["idioma"] == "en")]
    for indice in INDICES:
        n = 0
        com = {m: casos for m, casos in dados.items() if all(indice in l for l in casos)}  # modelos avaliados nele
        if not com:
            continue
        print(f"## índice: {indice}")
        print(f"{'corte':18} " + "  ".join(f"{m:>22}" for m in com))
        for nome, f in cortes:
            cel = []
            for m, casos in com.items():
                linhas = [l for l in casos if l["esperado"] and f(l)]
                if not linhas:  # suíte que esse modelo não avaliou
                    cel.append("—")
                    continue
                x = metricas(linhas, indice)
                n = x["n"]
                cel.append(f"h1 {x['hit@1']:.2f} h5 {x['hit@5']:.2f} mrr {x['mrr']:.2f}")
            print(f"{nome:18} " + "  ".join(f"{c:>22}" for c in cel) + f"   (n={n})")
        print()
    print(f"Sem resposta: maior similaridade (top-1) nas perguntas sem resposta x nas com resposta (índice {PRINCIPAL}):")
    for m, casos in dados.items():
        if not all(PRINCIPAL in l for l in casos):
            continue
        neg = sorted(l[PRINCIPAL]["nota_top1"] for l in casos if not l["esperado"])
        pos_ = sorted(l[PRINCIPAL]["nota_top1"] for l in casos if l["esperado"])
        print(f"  {m:8} sem resposta: {', '.join(f'{v:.3f}' for v in neg)} | com resposta: p10 {pos_[len(pos_)//10]:.3f}, mediana {pos_[len(pos_)//2]:.3f}")


if __name__ == "__main__":
    if sys.argv[1:] == ["--resumo"]:
        resumo()
    elif len(sys.argv) == 2:
        avaliar(sys.argv[1])
    else:
        sys.exit(__doc__)
