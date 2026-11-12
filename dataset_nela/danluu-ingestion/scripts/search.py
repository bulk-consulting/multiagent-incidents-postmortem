"""Busca os 5 chunks mais parecidos com um texto.

Uso: python search.py "descrição do incidente"
"""

import os
import sys
from pathlib import Path

import psycopg
import torch
from dotenv import load_dotenv
from pgvector.psycopg import register_vector
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parents[3]
load_dotenv(ROOT / ".env")
DATABASE_URL = os.environ["DATABASE_URL"]

MODEL = "Qwen/Qwen3-Embedding-0.6B"
DIMENSIONS = 1024
# O Qwen3 recebe uma instrução antes da pergunta; os chunks são codificados sem prefixo
QUERY_PREFIX = ("Instruct: Given a description of a production incident, retrieve post-mortem passages "
                "about similar incidents\nQuery: ")

SQL = """
SELECT c.chunk_id, i.company, i.title, i.source_url, 1 - (c.embedding <=> %s) AS similarity, c.content
FROM chunk c JOIN incident i USING (catalog_id)
ORDER BY c.embedding <=> %s
LIMIT %s
"""


def load_model() -> SentenceTransformer:
    # Usa a GPU se houver. No processador, float32: o padrão do Qwen3 (bfloat16) foi 2x mais
    # lento num notebook (10,3 s contra 5,3 s por chunk), com vetores praticamente iguais.
    kwargs = {} if torch.cuda.is_available() else {"model_kwargs": {"dtype": torch.float32}}
    model = SentenceTransformer(MODEL, **kwargs)
    model.max_seq_length = 1024  # os chunks têm até ~450 tokens; folga para o tokenizer do Qwen3
    return model


def encode_query(model, text: str):
    return model.encode(QUERY_PREFIX + text, normalize_embeddings=True)


def search(conn, model, text: str, limit: int = 5) -> list[tuple]:
    embedding = encode_query(model, text)
    return conn.execute(SQL, (embedding, embedding, limit)).fetchall()


def main() -> None:
    text = " ".join(sys.argv[1:])
    if not text:
        sys.exit('Uso: python search.py "descrição do incidente"')

    model = load_model()
    with psycopg.connect(DATABASE_URL) as conn:
        register_vector(conn)
        for position, (chunk_id, company, title, url, similarity, _content) in enumerate(search(conn, model, text), 1):
            print(f"{position}. {chunk_id} | {company} | {title}")
            print(f"   similaridade {similarity:.3f} | {url}")


if __name__ == "__main__":
    main()
