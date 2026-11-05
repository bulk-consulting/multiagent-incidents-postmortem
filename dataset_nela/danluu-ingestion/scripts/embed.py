"""Gera os embeddings dos chunks e grava no PostgreSQL + pgvector.

Cria as tabelas (db/schema.sql) se não existirem, esvazia as tabelas e carrega
de novo todos os incidentes e chunks de data/chunks/danluu_chunks.jsonl.
"""

import json
import os
from pathlib import Path

import psycopg
from pgvector.psycopg import register_vector
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "db" / "schema.sql"
INPUT = Path(__file__).resolve().parent.parent / "data" / "chunks" / "danluu_chunks.jsonl"

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://copilot:copilot@localhost:5432/incident_copilot")
MODEL = "intfloat/multilingual-e5-base"


def main() -> None:
    chunks = [json.loads(line) for line in INPUT.open(encoding="utf-8")]

    incidents = {}
    for c in chunks:
        incidents[c["catalog_id"]] = (c["catalog_id"], c["company"], c["title"], c["source_url"], c["category"])

    # O modelo e5 pede o prefixo "passage: " nos textos que serão buscados
    model = SentenceTransformer(MODEL)
    embeddings = model.encode(
        [f"passage: {c['text']}" for c in chunks],
        batch_size=32,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute(SCHEMA.read_text(encoding="utf-8"))
        register_vector(conn)
        conn.execute("TRUNCATE chunk, incident")
        with conn.cursor() as cur:
            cur.executemany(
                "INSERT INTO incident (catalog_id, company, title, source_url, category) VALUES (%s, %s, %s, %s, %s)",
                list(incidents.values()),
            )
            cur.executemany(
                "INSERT INTO chunk (chunk_id, catalog_id, chunk_type, content, embedding) VALUES (%s, %s, %s, %s, %s)",
                [(c["chunk_id"], c["catalog_id"], c["chunk_type"], c["text"], e) for c, e in zip(chunks, embeddings)],
            )
        total_incidents = conn.execute("SELECT count(*) FROM incident").fetchone()[0]
        total_chunks = conn.execute("SELECT count(*) FROM chunk").fetchone()[0]

    print(f"Incidentes: {total_incidents} | chunks: {total_chunks}")


if __name__ == "__main__":
    main()
