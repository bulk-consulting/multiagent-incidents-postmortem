"""
Busca em duas etapas no PostgreSQL + pgvector.

Etapa 1: compara a pergunta com os chunks de resumo (resumo do danluu, um por incidente) e de
         texto completo, e ranqueia os documentos pelo melhor chunk de cada um (incidentes
         parecidos), devolvendo o resumo do incidente e o chunk que mais combinou.
Etapa 2: nos documentos da etapa 1, compara a pergunta com os chunks do texto completo e devolve
         os trechos mais parecidos de cada documento (detalhes e evidência literal).

As fichas (chunks com tipo 'ficha') não entram na busca: são enriquecimento opcional.

A pergunta vira vetor com o mesmo modelo dos chunks (Qwen3-Embedding-0.6B, com a instrução de
pergunta), na GPU se houver CUDA e senão no processador.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/banco/busca.py "texto da pergunta" [--docs 5] [--trechos 2]
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

import numpy as np

# saída limpa (sem barras de progresso nem avisos do Hugging Face ao carregar o modelo)
for _var, _valor in {"TRANSFORMERS_VERBOSITY": "error", "HF_HUB_DISABLE_PROGRESS_BARS": "1",
                     "HF_HUB_VERBOSITY": "error", "TOKENIZERS_PARALLELISM": "false"}.items():
    os.environ.setdefault(_var, _valor)

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
SELECT DISTINCT ON (c.doc_id) c.doc_id, d.company, d.title, d.url, d.resumo, c.tipo, c.secao, c.content,
       1 - (c.embedding <=> %(q)s) AS similaridade
FROM chunks c JOIN documents d USING (doc_id)
WHERE c.dataset = %(dataset)s AND c.tipo IN ('resumo', 'texto')
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
        etapa1 = sorted(cur.fetchall(), key=lambda r: -r[8])[:n_docs]
        docs = [r[0] for r in etapa1]
        cur.execute(ETAPA2, {"q": q, "docs": docs, "n": n_trechos})
        detalhes: dict[str, list] = {}
        for doc_id, secao, content, sim in cur.fetchall():
            detalhes.setdefault(doc_id, []).append({"secao": secao, "content": content, "similaridade": float(sim)})
    return [{"doc_id": r[0], "company": r[1], "title": r[2], "url": r[3], "resumo": r[4],
             "melhor_chunk": {"tipo": r[5], "secao": r[6], "content": r[7]}, "similaridade": float(r[8]),
             "detalhes": detalhes.get(r[0], [])} for r in etapa1]


def main() -> None:
    args = [a for a in sys.argv[1:]]
    n_docs = int(args[args.index("--docs") + 1]) if "--docs" in args else 5
    n_trechos = int(args[args.index("--trechos") + 1]) if "--trechos" in args else 2
    pergunta = " ".join(a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or not args[i - 1].startswith("--")))
    if not pergunta:
        sys.exit(__doc__)
    for k, r in enumerate(buscar(pergunta, n_docs, n_trechos), 1):
        print(f"{k}. {r['doc_id']}  {r['similaridade']:.3f}  {r['company']} — {r['title']}")
        if r["resumo"]:
            print(f"   resumo: {r['resumo'][:160]}")
        m = r["melhor_chunk"]
        print(f"   achado pelo {m['tipo']}" + (f" [{m['secao']}]" if m["tipo"] == "texto" and m["secao"] else ""))
        for d in r["detalhes"]:
            print(f"   texto [{d['secao'] or '—'}] {d['similaridade']:.3f}: {d['content'][:150].replace(chr(10), ' ')}")
        print()


if __name__ == "__main__":
    main()
