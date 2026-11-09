"""
Chunks de resumo: um por incidente, com o resumo do catálogo do danluu (escrito por pessoas).

Entram na etapa 1 da busca junto com os chunks do texto completo: o resumo descreve o incidente
inteiro em poucas frases e é o que mais ajuda a achar o incidente certo (ingestion/avaliacao/
RESULTADOS.md). Não é dividido (o maior tem bem menos que o limite de tokens).

Cada chunk guarda `content` (o resumo, como está no corpus), `texto_embedding` (cabeçalho
empresa — título + resumo normalizado, o mesmo cabeçalho dos chunks de texto) e metadados do
documento, incluindo `resumo_origem` (danluu; no futuro, `gerado` para incidentes novos cujo
resumo for escrito por um LLM).

Documento sem resumo não tem este chunk (continua achável pelos chunks de texto).

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/corpus/chunk_resumo.py [--estimado]

Lê:    ingestion/corpus/corpus.jsonl
Grava: ingestion/corpus/chunks_resumo.jsonl
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location("chunk_fichas", PASTA / "chunk_fichas.py")
_cf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cf)


def montar_chunk(doc: dict, contar) -> dict | None:
    resumo = (doc.get("resumo") or "").strip()
    if not resumo:
        return None
    cabeca = f"{doc.get('company') or ''} — {_cf.titulo_do_documento(doc)}".strip(" —")
    emb = cabeca + "\n" + _cf.normalizar_para_embedding(resumo)
    return {
        "chunk_id": f"{doc['catalog_id']}:resumo",
        "catalog_id": doc["catalog_id"],
        "tipo": "resumo",
        "ordem": None,
        "secao": None,
        "content": resumo,
        "texto_embedding": emb,
        "tokens": contar(emb),
        "resumo_origem": doc.get("resumo_origem"),
        "company": doc.get("company"),
        "title": doc.get("title"),
        "url": doc.get("url"),
        "incident_date": doc.get("incident_date"),
        "text_source": doc.get("text_source"),
        "catalogo": doc.get("catalogo"),
    }


def main() -> None:
    contar, metodo = _cf.escolher_contador(sys.argv)
    docs = [json.loads(l) for l in (PASTA / "corpus.jsonl").open(encoding="utf-8")]
    chunks = [c for c in (montar_chunk(d, contar) for d in docs) if c]
    with (PASTA / "chunks_resumo.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    tam = sorted(c["tokens"] for c in chunks)
    sem = [d["catalog_id"] for d in docs if not (d.get("resumo") or "").strip()]
    print(f"{len(chunks)} chunks de resumo de {len(docs)} documentos (contagem: {metodo}) -> "
          f"{(PASTA / 'chunks_resumo.jsonl').relative_to(ROOT)}")
    print(f"  tokens: mediana {tam[len(tam)//2]}  min {tam[0]}  max {tam[-1]}")
    print(f"  documentos sem resumo: {len(sem)} {sem or ''}")


if __name__ == "__main__":
    main()
