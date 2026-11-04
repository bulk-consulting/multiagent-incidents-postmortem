"""
Busca em duas etapas no PostgreSQL + pgvector.

Etapa 1: compara a pergunta com os chunks das fichas e ranqueia os documentos pelo melhor chunk
         (incidentes parecidos), devolvendo o chunk que mais combinou e seus trechos de evidência.
Etapa 2: nos documentos da etapa 1, compara a pergunta com os chunks do texto completo e devolve
         os trechos mais parecidos de cada documento (detalhes).

A pergunta vira vetor com o mesmo modelo dos chunks (Qwen3-Embedding-0.6B, com a instrução de
pergunta), na GPU se houver CUDA e senão no processador.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/banco/busca.py "texto da pergunta" [--docs 5] [--trechos 2]
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent


def _modulo(caminho: Path, nome: str):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_carregar = _modulo(PASTA / "carregar.py", "carregar")
_gerar = _modulo(ROOT / "ingestion" / "corpus" / "gerar_embeddings.py", "gerar_embeddings")
_modelo = None

ETAPA1 = """
SELECT DISTINCT ON (c.doc_id) c.doc_id, d.company, d.title, d.url, c.assunto, c.content, c.trechos,
       1 - (c.embedding <=> %(q)s) AS similaridade
FROM chunks c JOIN documents d USING (doc_id)
WHERE c.dataset = %(dataset)s AND c.tipo = 'ficha'
ORDER BY c.doc_id, c.embedding <=> %(q)s
"""

ETAPA2 = """
SELECT doc_id, secao, content, similaridade FROM (
    SELECT c.doc_id, c.secao, c.content, 1 - (c.embedding <=> %(q)s) AS similaridade,
           row_number() OVER (PARTITION BY c.doc_id ORDER BY c.embedding <=> %(q)s) AS pos
    FROM chunks c
    WHERE c.tipo = 'texto' AND c.doc_id = ANY(%(docs)s)
) t WHERE pos <= %(n)s
ORDER BY doc_id, similaridade DESC
"""


def vetorizar(pergunta: str) -> np.ndarray:
    global _modelo
    cfg = _gerar.MODELOS["qwen3"]
    if _modelo is None:
        _modelo, _ = _gerar.carregar_modelo("qwen3")
    return _modelo.encode([cfg["prefixo_query"] + pergunta], normalize_embeddings=True)[0].astype(np.float32)


def buscar(pergunta: str, n_docs: int = 5, n_trechos: int = 2, dataset: str = "danluu") -> list[dict]:
    q = vetorizar(pergunta)
    with _carregar.conectar() as con, con.cursor() as cur:
        cur.execute(ETAPA1, {"q": q, "dataset": dataset})
        etapa1 = sorted(cur.fetchall(), key=lambda r: -r[7])[:n_docs]
        docs = [r[0] for r in etapa1]
        cur.execute(ETAPA2, {"q": q, "docs": docs, "n": n_trechos})
        detalhes: dict[str, list] = {}
        for doc_id, secao, content, sim in cur.fetchall():
            detalhes.setdefault(doc_id, []).append({"secao": secao, "content": content, "similaridade": float(sim)})
    return [{"doc_id": r[0], "company": r[1], "title": r[2], "url": r[3], "assunto": r[4], "ficha_chunk": r[5],
             "trechos": r[6], "similaridade": float(r[7]), "detalhes": detalhes.get(r[0], [])} for r in etapa1]


def main() -> None:
    args = [a for a in sys.argv[1:]]
    n_docs = int(args[args.index("--docs") + 1]) if "--docs" in args else 5
    n_trechos = int(args[args.index("--trechos") + 1]) if "--trechos" in args else 2
    pergunta = " ".join(a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or not args[i - 1].startswith("--")))
    if not pergunta:
        sys.exit(__doc__)
    for k, r in enumerate(buscar(pergunta, n_docs, n_trechos), 1):
        print(f"{k}. {r['doc_id']}  {r['similaridade']:.3f}  {r['company']} — {r['title']}")
        print(f"   ficha ({r['assunto']}): {r['ficha_chunk'][:160].replace(chr(10), ' ')}")
        if r["trechos"]:
            print(f"   evidência: \"{r['trechos'][0][:150]}\"")
        for d in r["detalhes"]:
            print(f"   texto [{d['secao'] or '—'}] {d['similaridade']:.3f}: {d['content'][:150].replace(chr(10), ' ')}")
        print()


if __name__ == "__main__":
    main()
