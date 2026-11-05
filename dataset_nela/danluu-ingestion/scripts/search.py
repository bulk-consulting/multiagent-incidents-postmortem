"""Busca os 5 chunks mais parecidos com um texto.

Uso: python search.py "descrição do incidente"
"""

import os
import sys

import psycopg
from pgvector.psycopg import register_vector
from sentence_transformers import SentenceTransformer

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://copilot:copilot@localhost:5432/incident_copilot")
MODEL = "intfloat/multilingual-e5-base"

SQL = """
SELECT c.chunk_id, i.company, i.title, i.source_url, 1 - (c.embedding <=> %s) AS similarity
FROM chunk c JOIN incident i USING (catalog_id)
ORDER BY c.embedding <=> %s
LIMIT %s
"""


def search(conn, model, text: str, limit: int = 5) -> list[tuple]:
    # O modelo e5 pede o prefixo "query: " nas buscas
    embedding = model.encode(f"query: {text}", normalize_embeddings=True)
    return conn.execute(SQL, (embedding, embedding, limit)).fetchall()


def main() -> None:
    text = " ".join(sys.argv[1:])
    if not text:
        sys.exit('Uso: python search.py "descrição do incidente"')

    model = SentenceTransformer(MODEL)
    with psycopg.connect(DATABASE_URL) as conn:
        register_vector(conn)
        for position, (chunk_id, company, title, url, similarity) in enumerate(search(conn, model, text), 1):
            print(f"{position}. {chunk_id} | {company} | {title}")
            print(f"   similaridade {similarity:.3f} | {url}")


if __name__ == "__main__":
    main()
