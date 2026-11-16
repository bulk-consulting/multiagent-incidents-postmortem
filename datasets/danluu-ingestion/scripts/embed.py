"""Gera os embeddings dos chunks e grava no PostgreSQL + pgvector.

Os vetores ficam guardados em data/embeddings/qwen3/ (versionados no git), para
quem não tem GPU não precisar gerá-los de novo (no processador leva horas):
- vectors.npy: um vetor por linha (float16);
- index.json:  o modelo e, na mesma ordem das linhas, o chunk_id e o hash do
               texto que virou vetor.
Um vetor só é reaproveitado se o chunk_id E o hash do texto forem os mesmos:
se o texto de um chunk muda (mesmo com o mesmo id), o vetor é gerado de novo.
Os vetores são guardados a cada bloco de SAVE_EVERY chunks: se a execução for
interrompida, basta rodar de novo que ela continua de onde parou.

Depois apaga e recria as tabelas (db/schema.sql) e carrega os incidentes e os
chunks que têm vetor.

Uso:
    python embed.py              # gera os vetores que faltam e carrega o banco
    python embed.py --limit 1    # gera no máximo 1 vetor novo (para testar)
"""

import argparse
import hashlib
import json
import os
import time
from datetime import date
from pathlib import Path

import numpy as np
import psycopg
from pgvector.psycopg import register_vector

from search import DATABASE_URL, DIMENSIONS, MODEL, ROOT, load_model

SCHEMA = ROOT / "db" / "schema.sql"
DATA = Path(__file__).resolve().parent.parent / "data"
INPUT = DATA / "chunks" / "danluu_chunks.jsonl"
CACHE = DATA / "embeddings" / "qwen3"
# Os vetores são guardados a cada SAVE_EVERY chunks (~5 min no processador)
SAVE_EVERY = 64


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def load_cache() -> dict[tuple[str, str], np.ndarray]:
    """{(chunk_id, hash): vetor} dos vetores guardados, se forem do mesmo modelo."""
    try:
        index = json.loads((CACHE / "index.json").read_text(encoding="utf-8"))
        vectors = np.load(CACHE / "vectors.npy")
    except FileNotFoundError:
        return {}
    if index["model"] != MODEL or len(index["chunks"]) != len(vectors):
        print(f"Vetores guardados ignorados (modelo {index['model']}, {len(vectors)} vetores)")
        return {}
    return {(chunk_id, h): v for (chunk_id, h), v in zip(index["chunks"], vectors)}


def save_cache(chunks: list[dict], vectors: dict[tuple[str, str], np.ndarray]) -> None:
    """Guarda só os vetores dos chunks atuais, na ordem dos chunks.

    Grava em arquivos temporários e só depois troca pelos definitivos: se o processo
    for interrompido no meio da gravação, os arquivos anteriores continuam válidos.
    """
    keys = [(c["chunk_id"], c["hash"]) for c in chunks if (c["chunk_id"], c["hash"]) in vectors]
    CACHE.mkdir(parents=True, exist_ok=True)
    matrix = np.array([vectors[k] for k in keys], dtype=np.float16).reshape(-1, DIMENSIONS)
    index = {"model": MODEL, "dimensions": DIMENSIONS, "updated": date.today().isoformat(),
             "chunks": [list(k) for k in keys]}
    with open(CACHE / "vectors.tmp.npy", "wb") as f:
        np.save(f, matrix)
    (CACHE / "index.tmp.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    os.replace(CACHE / "vectors.tmp.npy", CACHE / "vectors.npy")
    os.replace(CACHE / "index.tmp.json", CACHE / "index.json")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, help="gera no máximo N vetores novos (para testar)")
    args = parser.parse_args()

    chunks = [json.loads(line) for line in INPUT.open(encoding="utf-8")]
    for c in chunks:
        c["hash"] = text_hash(c["text"])

    vectors = load_cache()
    missing = [c for c in chunks if (c["chunk_id"], c["hash"]) not in vectors]
    to_encode = missing[:args.limit] if args.limit is not None else missing
    print(f"Chunks: {len(chunks)} | vetores reaproveitados: {len(chunks) - len(missing)} | "
          f"a gerar: {len(to_encode)}")

    if to_encode:
        model = load_model()
        start = time.time()
        # Gera em blocos e guarda depois de cada um: se o processo for interrompido,
        # a próxima execução reaproveita o que já foi gerado e continua dali
        for i in range(0, len(to_encode), SAVE_EVERY):
            block = to_encode[i:i + SAVE_EVERY]
            new = model.encode([c["text"] for c in block], batch_size=16, normalize_embeddings=True)
            for c, v in zip(block, new):
                vectors[(c["chunk_id"], c["hash"])] = v
            save_cache(chunks, vectors)
            done = i + len(block)
            elapsed = time.time() - start
            remaining = elapsed / done * (len(to_encode) - done)
            print(f"  {done}/{len(to_encode)} vetores | {elapsed / 60:.0f} min | "
                  f"faltam ~{remaining / 60:.0f} min", flush=True)
        print(f"Vetores guardados em {CACHE}")

    ready = [c for c in chunks if (c["chunk_id"], c["hash"]) in vectors]
    if len(ready) < len(chunks):
        print(f"AVISO: {len(chunks) - len(ready)} chunks sem vetor ficam fora do banco "
              f"(rode sem --limit para gerar todos)")

    incidents = {c["catalog_id"]: (c["catalog_id"], c["company"], c["title"], c["source_url"], c["category"])
                 for c in chunks}
    with psycopg.connect(DATABASE_URL) as conn:
        # O tamanho do vetor depende do modelo: as tabelas são recriadas a cada carga
        conn.execute("DROP TABLE IF EXISTS chunk, incident")
        conn.execute(SCHEMA.read_text(encoding="utf-8"))
        register_vector(conn)
        with conn.cursor() as cur:
            cur.executemany(
                "INSERT INTO incident (catalog_id, company, title, source_url, category) VALUES (%s, %s, %s, %s, %s)",
                list(incidents.values()),
            )
            cur.executemany(
                "INSERT INTO chunk (chunk_id, catalog_id, chunk_type, content, embedding) VALUES (%s, %s, %s, %s, %s)",
                [(c["chunk_id"], c["catalog_id"], c["chunk_type"], c["text"],
                  vectors[(c["chunk_id"], c["hash"])].astype(np.float32)) for c in ready],
            )
        total_incidents = conn.execute("SELECT count(*) FROM incident").fetchone()[0]
        total_chunks = conn.execute("SELECT count(*) FROM chunk").fetchone()[0]

    print(f"Banco: incidentes {total_incidents} | chunks {total_chunks}")


if __name__ == "__main__":
    main()
