"""
Carrega o corpus do danluu no PostgreSQL + pgvector (container de ingestion/banco/docker-compose.yml).

Lê:
    ingestion/corpus/corpus.jsonl                 documentos (texto limpo e metadados)
    ingestion/fichas/saida/DAN-*.json             fichas (entram inteiras em documents.ficha)
    ingestion/corpus/chunks_{fichas,texto}.jsonl  chunks
    ingestion/corpus/embeddings/<modelo>/         vetores (.npy) e ids na mesma ordem
    ingestion/banco/.env                          conexão

Substitui tudo do dataset numa transação só (apaga e insere de novo): rodar duas vezes dá o
mesmo resultado, e se algo falhar nada muda no banco. Antes de gravar, confere se cada vetor
corresponde ao seu chunk (mesma ordem de ids) e se a dimensão é a da coluna.

Uso (a partir da raiz do repositório, com o container de pé):
    multiagent_env/bin/python -I ingestion/banco/carregar.py [--modelo qwen3]
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent
CORPUS = ROOT / "ingestion" / "corpus"
FICHAS = ROOT / "ingestion" / "fichas" / "saida"
DATASET = "danluu"
DIMENSAO = 1024


def conectar() -> psycopg.Connection:
    load_dotenv(PASTA / ".env")
    con = psycopg.connect(host=os.environ.get("POSTGRES_HOST", "127.0.0.1"), port=os.environ["POSTGRES_PORT"],
                          user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"],
                          dbname=os.environ["POSTGRES_DB"])
    register_vector(con)
    return con


def main() -> None:
    chave = sys.argv[sys.argv.index("--modelo") + 1] if "--modelo" in sys.argv else "qwen3"
    emb = CORPUS / "embeddings" / chave
    meta = json.loads((emb / "meta.json").read_text(encoding="utf-8"))

    docs = [json.loads(l) for l in (CORPUS / "corpus.jsonl").open(encoding="utf-8")]
    linhas_docs = []
    for d in docs:
        ficha = json.loads((FICHAS / f"{d['catalog_id']}.json").read_text(encoding="utf-8"))
        tri, inc = ficha["triagem"], ficha.get("incidente") or {}
        linhas_docs.append((
            f"{DATASET}:{d['catalog_id']}", DATASET, d["catalog_id"], d.get("company"), d.get("title"),
            d.get("page_title"), d.get("url"), d.get("incident_date"), d.get("text_source"), d.get("catalogo"),
            d.get("problemas_texto") or [], inc.get("categoria_causa"), tri.get("dominio"), tri.get("tipo"),
            tri.get("seguranca"), ficha.get("confianca"), json.dumps(ficha, ensure_ascii=False), d["text"]))

    linhas_chunks = []
    for nome in ("fichas", "texto"):
        chunks = [json.loads(l) for l in (CORPUS / f"chunks_{nome}.jsonl").open(encoding="utf-8")]
        ids = json.loads((emb / f"{nome}_ids.json").read_text(encoding="utf-8"))
        vetores = np.load(emb / f"{nome}.npy").astype(np.float32)
        if [c["chunk_id"] for c in chunks] != ids or len(ids) != len(vetores):
            sys.exit(f"{nome}: os vetores de {emb} não correspondem aos chunks atuais; gere os embeddings de novo")
        if vetores.shape[1] != DIMENSAO:
            sys.exit(f"{nome}: dimensão {vetores.shape[1]} diferente da coluna vector({DIMENSAO})")
        for c, v in zip(chunks, vetores):
            linhas_chunks.append((
                f"{DATASET}:{c['chunk_id']}", f"{DATASET}:{c['catalog_id']}", DATASET, c["tipo"],
                c.get("assunto"), c.get("secao"), c.get("ordem"), c["content"], c["texto_embedding"],
                c.get("tokens"), json.dumps(c.get("trechos", []), ensure_ascii=False), meta["nome"], v))

    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True).stdout.strip()
    with conectar() as con, con.cursor() as cur:
        cur.execute("DELETE FROM documents WHERE dataset = %s", (DATASET,))  # chunks saem em cascata
        cur.executemany("""INSERT INTO documents (doc_id, dataset, source_id, company, title, page_title, url,
                incident_date, text_source, catalogo, problemas_texto, categoria_causa, dominio, tipo_documento,
                seguranca, confianca, ficha, texto)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", linhas_docs)
        cur.executemany("""INSERT INTO chunks (chunk_id, doc_id, dataset, tipo, assunto, secao, ordem, content,
                texto_embedding, tokens, trechos, modelo, embedding)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", linhas_chunks)
        cur.execute("INSERT INTO cargas (dataset, modelo, documentos, chunks, origem) VALUES (%s,%s,%s,%s,%s)",
                    (DATASET, meta["nome"], len(linhas_docs), len(linhas_chunks), f"commit {commit}"))
        cur.execute("SELECT tipo, count(*) FROM chunks WHERE dataset = %s GROUP BY tipo ORDER BY tipo", (DATASET,))
        contagem = dict(cur.fetchall())
    print(f"{DATASET}: {len(linhas_docs)} documentos e {len(linhas_chunks)} chunks carregados "
          f"({contagem}) com {meta['nome']} (commit {commit})")


if __name__ == "__main__":
    main()
