"""
Gera os vetores (embeddings) dos chunks com um modelo e grava em arquivo, para avaliar os modelos
fora do banco antes de carregar o vencedor no pgvector.

Modelos (chave -> modelo, prefixo dos documentos):
    e5      intfloat/multilingual-e5-base     "passage: "  (as perguntas usam "query: ")
    bge-m3  BAAI/bge-m3                       sem prefixo
    qwen3   Qwen/Qwen3-Embedding-0.6B         sem prefixo  (as perguntas usam uma instrução)

O modelo roda na GPU (CUDA, fp16) se houver, senão no processador (float32, bem mais lento: ~2 h para
os ~2.900 chunks com o Qwen3 num notebook de 6 núcleos, contra ~3,5 min na GPU). Os vetores são
normalizados (similaridade = produto escalar). carregar_modelo() é usada também pela busca e pela
avaliação, para todos escolherem o dispositivo do mesmo jeito.

Uso (a partir da raiz do repositório), um modelo por vez:
    multiagent_env/bin/python -I ingestion/corpus/gerar_embeddings.py qwen3
    multiagent_env/bin/python -I ingestion/corpus/gerar_embeddings.py qwen3 --cpu      # força o processador
    multiagent_env/bin/python -I ingestion/corpus/gerar_embeddings.py qwen3 --conferir # só diz se os vetores
                                                                                        # atuais batem com os chunks

Lê:    ingestion/corpus/chunks_{resumo,texto,fichas}.jsonl  (fichas é opcional: pulado se não existir)
Grava: ingestion/corpus/embeddings/<chave>/<tipo>.npy        (float16, uma linha por chunk)
       ingestion/corpus/embeddings/<chave>/<tipo>_ids.json   (chunk_id na mesma ordem)
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
TIPOS = ("resumo", "texto", "fichas")  # arquivos chunks_<tipo>.jsonl; o de fichas é opcional


def tipos_presentes() -> list[str]:
    return [t for t in TIPOS if (PASTA / f"chunks_{t}.jsonl").exists()]


MODELOS = {
    "e5": {"nome": "intfloat/multilingual-e5-base", "prefixo_doc": "passage: ", "prefixo_query": "query: ",
           "max_seq": 512},
    "bge-m3": {"nome": "BAAI/bge-m3", "prefixo_doc": "", "prefixo_query": "", "max_seq": 1024},
    "qwen3": {"nome": "Qwen/Qwen3-Embedding-0.6B", "prefixo_doc": "",
              "prefixo_query": "Instruct: Given a description of a production incident, retrieve "
                               "post-mortem passages about similar incidents\nQuery: ",
              "max_seq": 1024},
}


def carregar_modelo(chave: str, forcar_cpu: bool = False) -> tuple[SentenceTransformer, str]:
    """Carrega o modelo na GPU (fp16) se houver CUDA; senão no processador (float32). Devolve (modelo, dispositivo)."""
    cfg = MODELOS[chave]
    if torch.cuda.is_available() and not forcar_cpu:
        modelo, dispositivo = SentenceTransformer(cfg["nome"], device="cuda",
                                                  model_kwargs={"dtype": torch.float16}), "cuda"
    else:
        modelo, dispositivo = SentenceTransformer(cfg["nome"], device="cpu",
                                                  model_kwargs={"dtype": torch.float32}), "cpu"
    modelo.max_seq_length = cfg["max_seq"]
    return modelo, dispositivo


def vetores_atualizados(chave: str) -> tuple[bool, str]:
    """Os vetores gravados correspondem aos chunks atuais (mesmos ids, na mesma ordem) e ao modelo?"""
    saida = PASTA / "embeddings" / chave
    try:
        meta = json.loads((saida / "meta.json").read_text(encoding="utf-8"))
        if meta.get("nome") != MODELOS[chave]["nome"]:
            return False, f"modelo diferente ({meta.get('nome')})"
        for nome in tipos_presentes():
            ids_chunks = [json.loads(l)["chunk_id"] for l in (PASTA / f"chunks_{nome}.jsonl").open(encoding="utf-8")]
            ids_vet = json.loads((saida / f"{nome}_ids.json").read_text(encoding="utf-8"))
            n_vet = np.load(saida / f"{nome}.npy", mmap_mode="r").shape[0]
            if ids_chunks != ids_vet or n_vet != len(ids_vet):
                return False, f"os chunks de {nome} mudaram desde a geração dos vetores"
    except FileNotFoundError as e:
        return False, f"arquivo ausente: {Path(e.filename).name}"
    return True, f"vetores de {meta['data']} batem com os chunks atuais"


def main() -> None:
    args = sys.argv[1:]
    chaves = [a for a in args if not a.startswith("--")]
    if len(chaves) != 1 or chaves[0] not in MODELOS:
        sys.exit(__doc__)
    chave = chaves[0]
    cfg = MODELOS[chave]
    if "--conferir" in args:
        ok, motivo = vetores_atualizados(chave)
        print(f"{chave}: {motivo}")
        sys.exit(0 if ok else 1)
    saida = PASTA / "embeddings" / chave
    saida.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    modelo, dispositivo = carregar_modelo(chave, forcar_cpu="--cpu" in args)
    t_carga = time.time() - t0
    print(f"{chave}: modelo carregado em {dispositivo} ({t_carga:.0f}s)", flush=True)

    tempos = {}
    for nome in tipos_presentes():
        chunks = [json.loads(l) for l in (PASTA / f"chunks_{nome}.jsonl").open(encoding="utf-8")]
        textos = [cfg["prefixo_doc"] + c["texto_embedding"] for c in chunks]
        t1 = time.time()
        vetores = modelo.encode(textos, batch_size=16 if dispositivo == "cuda" else 8, normalize_embeddings=True,
                                convert_to_numpy=True, show_progress_bar=False)
        tempos[nome] = round(time.time() - t1, 1)
        np.save(saida / f"{nome}.npy", vetores.astype(np.float16))
        (saida / f"{nome}_ids.json").write_text(json.dumps([c["chunk_id"] for c in chunks]), encoding="utf-8")
        print(f"{chave} {nome}: {len(chunks)} chunks, dim {vetores.shape[1]}, {tempos[nome]}s")

    meta = {**cfg, "chave": chave, "data": date.today().isoformat(), "dispositivo": dispositivo,
            "dtype_modelo": "float16" if dispositivo == "cuda" else "float32",
            "normalizado": True, "carga_s": round(t_carga, 1), "encode_s": tempos,
            "pico_ram_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024),
            "pico_vram_mb": round(torch.cuda.max_memory_allocated() / 2**20) if dispositivo == "cuda" else 0}
    (saida / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{chave}: carga {meta['carga_s']}s, pico RAM {meta['pico_ram_mb']} MB, pico VRAM {meta['pico_vram_mb']} MB")


if __name__ == "__main__":
    main()
