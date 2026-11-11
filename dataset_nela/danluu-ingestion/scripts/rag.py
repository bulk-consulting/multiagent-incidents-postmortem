"""Pipeline RAG: pergunta -> busca no pgvector -> prompt -> GPT-OSS-20B -> resposta.

Os templates do prompt estão em prompts.py.

Uso: python rag.py "pergunta"
"""

import sys
import time

import psycopg
from pgvector.psycopg import register_vector
from sentence_transformers import SentenceTransformer

from llm import ask
from prompts import FORMATO, SYSTEM, USER
from search import DATABASE_URL, MODEL, search


def build_prompt(question: str, results: list[tuple]) -> str:
    trechos = [
        f"[{n}] {company} | {title} | {url}\n{content}"
        for n, (_chunk_id, company, title, url, _similarity, content) in enumerate(results, 1)
    ]
    return USER.format(incidente=question, trechos="\n\n".join(trechos), formato=FORMATO)


def main() -> None:
    question = " ".join(sys.argv[1:])
    if not question:
        sys.exit('Uso: python rag.py "pergunta"')

    # Retrival
    model = SentenceTransformer(MODEL)
    with psycopg.connect(DATABASE_URL) as conn:
        register_vector(conn)
        inicio = time.perf_counter()
        results = search(conn, model, question)
        tempo_busca = time.perf_counter() - inicio

    # Augmented
    prompt = build_prompt(question, results)
    
    # Generation
    inicio = time.perf_counter()
    resposta = ask(prompt, system=SYSTEM)
    tempo_llm = time.perf_counter() - inicio

    print(f"Pergunta: {question}\n")
    print(f"Resposta:\n{resposta}\n")
    print("Fontes:")
    for n, (chunk_id, company, title, url, similarity, _content) in enumerate(results, 1):
        print(f"[{n}] {chunk_id} | {company} | {title}")
        print(f"    similaridade {similarity:.3f} | {url}")
    print(f"\nTempo: busca {tempo_busca:.1f} s | LLM {tempo_llm:.1f} s")


if __name__ == "__main__":
    main()
