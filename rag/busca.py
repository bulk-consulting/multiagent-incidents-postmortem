"""
Busca em duas etapas no banco da ingestão (tabelas incident e chunk, ver db/schema.sql).

Etapa 1: compara a pergunta com todos os chunks (summary e text) e ranqueia os incidentes pelo
         melhor chunk de cada um. Devolve n_docs incidentes distintos, cada um com o seu resumo
         (o chunk summary, que é o resumo do catálogo do danluu).
Etapa 2: nesses incidentes, compara a pergunta só com os chunks text e devolve os n_trechos mais
         parecidos de cada um (detalhes e evidência literal para o prompt).

A pergunta vira vetor com o mesmo modelo e a mesma instrução do dataset_nela/danluu-ingestion/scripts/
search.py (Qwen3-Embedding-0.6B). A busca de uma etapa daquele script devolve chunks soltos, que
podem ser todos do mesmo incidente; o prompt do RAG precisa de incidentes distintos.

Conexão: DATABASE_URL no .env da raiz do repositório.

Uso (a partir da raiz do repositório):
    python rag/busca.py "texto da pergunta" [--docs 5] [--trechos 2]
"""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

import numpy as np
import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

MODELO = "Qwen/Qwen3-Embedding-0.6B"
PREFIXO_PERGUNTA = ("Instruct: Given a description of a production incident, retrieve post-mortem passages "
                    "about similar incidents\nQuery: ")

ETAPA1 = """
SELECT DISTINCT ON (c.catalog_id) c.catalog_id, i.company, i.title, i.source_url, s.content AS resumo,
       c.chunk_type, c.content, 1 - (c.embedding <=> %(q)s) AS similaridade
FROM chunk c
JOIN incident i USING (catalog_id)
LEFT JOIN chunk s ON s.catalog_id = c.catalog_id AND s.chunk_type = 'summary'
ORDER BY c.catalog_id, c.embedding <=> %(q)s
"""

ETAPA2 = """
SELECT catalog_id, content, similaridade FROM (
    SELECT c.catalog_id, c.content, 1 - (c.embedding <=> %(q)s) AS similaridade,
           row_number() OVER (PARTITION BY c.catalog_id ORDER BY c.embedding <=> %(q)s) AS pos
    FROM chunk c
    WHERE c.chunk_type = 'text' AND c.catalog_id = ANY(%(docs)s)
) t WHERE pos <= %(n)s
ORDER BY catalog_id, similaridade DESC
"""

# Os chunks text começam com "Company: ... | Title: ... | Category: ...". No prompt, o bloco do
# incidente já mostra empresa e título, então o cabeçalho sai do trecho.
CABECALHO = re.compile(r"\ACompany: [^\n]*\n+")

_modelo = None


def vetorizar(pergunta: str) -> np.ndarray:
    global _modelo
    if _modelo is None:
        import torch
        from sentence_transformers import SentenceTransformer
        kwargs = {} if torch.cuda.is_available() else {"model_kwargs": {"dtype": torch.float32}}
        _modelo = SentenceTransformer(MODELO, **kwargs)
        _modelo.max_seq_length = 1024
    return _modelo.encode(PREFIXO_PERGUNTA + pergunta, normalize_embeddings=True).astype(np.float32)


def _secao_e_texto(content: str) -> tuple[str, str]:
    """Tira o cabeçalho e, se o trecho começa com um título ("## Root cause"), usa-o como seção."""
    texto = CABECALHO.sub("", content, count=1).strip()
    primeira = texto.split("\n", 1)[0]
    secao = primeira.lstrip("#").strip() if primeira.startswith("#") else ""
    return secao, texto


def buscar(pergunta: str, n_docs: int = 5, n_trechos: int = 2) -> list[dict]:
    q = vetorizar(pergunta)
    with psycopg.connect(os.environ["DATABASE_URL"]) as con:
        register_vector(con)
        with con.cursor() as cur:
            cur.execute(ETAPA1, {"q": q})
            etapa1 = sorted(cur.fetchall(), key=lambda r: -r[7])[:n_docs]
            docs = [r[0] for r in etapa1]
            cur.execute(ETAPA2, {"q": q, "docs": docs, "n": n_trechos})
            detalhes: dict[str, list] = {}
            for catalog_id, content, sim in cur.fetchall():
                secao, texto = _secao_e_texto(content)
                detalhes.setdefault(catalog_id, []).append({"secao": secao, "content": texto, "similaridade": float(sim)})
    saida = []
    for cid, company, title, url, resumo, tipo, content, sim in etapa1:
        secao, texto = _secao_e_texto(content)
        saida.append({"doc_id": cid, "company": company, "title": title, "url": url, "resumo": resumo,
                      "melhor_chunk": {"tipo": "resumo" if tipo == "summary" else "texto", "secao": secao, "content": texto},
                      "similaridade": float(sim), "detalhes": detalhes.get(cid, [])})
    return saida


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pergunta", nargs="+")
    ap.add_argument("--docs", type=int, default=5)
    ap.add_argument("--trechos", type=int, default=2)
    a = ap.parse_args()
    for k, r in enumerate(buscar(" ".join(a.pergunta), a.docs, a.trechos), 1):
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
