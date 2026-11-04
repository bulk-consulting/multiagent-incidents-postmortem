"""
Gera os vetores (embeddings) dos chunks com um modelo e grava em arquivo, para avaliar os modelos
fora do banco antes de carregar o vencedor no pgvector.

Modelos (chave -> modelo, prefixo dos documentos):
    e5      intfloat/multilingual-e5-base     "passage: "  (as perguntas usam "query: ")
    bge-m3  BAAI/bge-m3                       sem prefixo
    qwen3   Qwen/Qwen3-Embedding-0.6B         sem prefixo  (as perguntas usam uma instrução)

O modelo é carregado em fp16 na GPU; os vetores são normalizados (similaridade = produto escalar).

Uso (a partir da raiz do repositório), um modelo por vez:
    multiagent_env/bin/python -I ingestion/corpus/gerar_embeddings.py e5

Lê:    ingestion/corpus/chunks_fichas.jsonl, ingestion/corpus/chunks_texto.jsonl
Grava: ingestion/corpus/embeddings/<chave>/{fichas,texto}.npy   (float16, uma linha por chunk)
       ingestion/corpus/embeddings/<chave>/{fichas,texto}_ids.json  (chunk_id na mesma ordem)
       ingestion/corpus/embeddings/<chave>/meta.json
"""
from __future__ import annotations

import json
import resource
import sys
import time
from datetime import date
from pathlib import Path

import numpy as np
import torch
from sentence_transformers import SentenceTransformer

PASTA = Path(__file__).resolve().parent
MODELOS = {
    "e5": {"nome": "intfloat/multilingual-e5-base", "prefixo_doc": "passage: ", "prefixo_query": "query: ",
           "max_seq": 512},
    "bge-m3": {"nome": "BAAI/bge-m3", "prefixo_doc": "", "prefixo_query": "", "max_seq": 1024},
    "qwen3": {"nome": "Qwen/Qwen3-Embedding-0.6B", "prefixo_doc": "",
              "prefixo_query": "Instruct: Given a description of a production incident, retrieve "
                               "post-mortem passages about similar incidents\nQuery: ",
              "max_seq": 1024},
}


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in MODELOS:
        sys.exit(__doc__)
    chave = sys.argv[1]
    cfg = MODELOS[chave]
    saida = PASTA / "embeddings" / chave
    saida.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    modelo = SentenceTransformer(cfg["nome"], device="cuda", model_kwargs={"torch_dtype": torch.float16})
    modelo.max_seq_length = cfg["max_seq"]
    t_carga = time.time() - t0

    tempos = {}
    for nome in ("fichas", "texto"):
        chunks = [json.loads(l) for l in (PASTA / f"chunks_{nome}.jsonl").open(encoding="utf-8")]
        textos = [cfg["prefixo_doc"] + c["texto_embedding"] for c in chunks]
        t1 = time.time()
        vetores = modelo.encode(textos, batch_size=16, normalize_embeddings=True,
                                convert_to_numpy=True, show_progress_bar=False)
        tempos[nome] = round(time.time() - t1, 1)
        np.save(saida / f"{nome}.npy", vetores.astype(np.float16))
        (saida / f"{nome}_ids.json").write_text(json.dumps([c["chunk_id"] for c in chunks]), encoding="utf-8")
        print(f"{chave} {nome}: {len(chunks)} chunks, dim {vetores.shape[1]}, {tempos[nome]}s")

    meta = {**cfg, "chave": chave, "data": date.today().isoformat(), "dtype_modelo": "float16",
            "normalizado": True, "carga_s": round(t_carga, 1), "encode_s": tempos,
            "pico_ram_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024),
            "pico_vram_mb": round(torch.cuda.max_memory_allocated() / 2**20)}
    (saida / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{chave}: carga {meta['carga_s']}s, pico RAM {meta['pico_ram_mb']} MB, pico VRAM {meta['pico_vram_mb']} MB")


if __name__ == "__main__":
    main()
