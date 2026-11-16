"""Mede a qualidade da busca com as perguntas de evaluation/questions.json.

Cada pergunta tem o incidente que deveria aparecer. Os incidentes são ordenados
pela maior similaridade entre a pergunta e os seus chunks (summary e text, como
na busca), e anotamos em que posição o incidente esperado ficou:
- 1º lugar: fração das perguntas em que ele veio em primeiro;
- top 5:    fração em que ele ficou entre os 5 primeiros;
- MRR:      média de 1/posição (posições além de 20 contam 0).

Serve para medir uma mudança no chunking, na limpeza ou no modelo: rodar antes
e depois e comparar os números.

Lê os vetores guardados por embed.py (data/embeddings/qwen3/); não usa o banco.

Uso: python evaluate.py
Grava: evaluation/results.json (posição do incidente esperado em cada pergunta)
"""

import json
from pathlib import Path

import numpy as np

from embed import CACHE, INPUT, text_hash
from search import MODEL, QUERY_PREFIX, load_model

EVALUATION = Path(__file__).resolve().parent.parent / "evaluation"
MAX_RANK = 20

GRUPOS = [
    ("Todas", lambda q: True),
    ("Sintoma", lambda q: q["tipo"] == "sintoma"),
    ("Causa", lambda q: q["tipo"] == "causa"),
    ("Geral", lambda q: q["tipo"] == "geral"),
    ("Português", lambda q: q["idioma"] == "pt"),
    ("Inglês", lambda q: q["idioma"] == "en"),
]


def load_vectors() -> tuple[list[dict], np.ndarray]:
    """Chunks atuais e a matriz de vetores, na mesma ordem."""
    index = json.loads((CACHE / "index.json").read_text(encoding="utf-8"))
    vectors = np.load(CACHE / "vectors.npy").astype(np.float32)
    row = {tuple(k): i for i, k in enumerate(index["chunks"])}
    chunks = [json.loads(line) for line in INPUT.open(encoding="utf-8")]
    keys = [(c["chunk_id"], text_hash(c["text"])) for c in chunks]
    if index["model"] != MODEL or any(k not in row for k in keys):
        raise SystemExit("Os vetores guardados não correspondem aos chunks atuais; rode embed.py antes")
    return chunks, vectors[[row[k] for k in keys]]


def main() -> None:
    chunks, vectors = load_vectors()
    questions = json.loads((EVALUATION / "questions.json").read_text(encoding="utf-8"))["perguntas"]

    model = load_model()
    queries = model.encode([QUERY_PREFIX + q["pergunta"] for q in questions], batch_size=16,
                           normalize_embeddings=True, show_progress_bar=True)
    similarities = queries @ vectors.T  # perguntas x chunks

    docs = sorted({c["catalog_id"] for c in chunks})
    position = {d: k for k, d in enumerate(docs)}
    doc_of_chunk = np.array([position[c["catalog_id"]] for c in chunks], dtype=np.int64)
    for q, sims in zip(questions, similarities):
        scores = np.full(len(docs), -np.inf, dtype=np.float32)
        np.maximum.at(scores, doc_of_chunk, sims)  # nota do incidente = melhor chunk
        top = [docs[k] for k in np.argsort(-scores)[:MAX_RANK]]
        q["posicao"] = next((k + 1 for k, d in enumerate(top) if d in q["esperado"]), None)
        q["top5"] = top[:5]
        q["similaridade"] = round(float(scores.max()), 3)

    print(f"\n{'':12}{'perguntas':>10}{'1º lugar':>10}{'top 5':>8}{'MRR':>7}")
    for nome, filtro in GRUPOS:
        ranks = [q["posicao"] for q in questions if q["esperado"] and filtro(q)]
        first = sum(1 for r in ranks if r == 1) / len(ranks)
        top5 = sum(1 for r in ranks if r and r <= 5) / len(ranks)
        mrr = sum(1 / r for r in ranks if r) / len(ranks)
        print(f"{nome:12}{len(ranks):>10}{first:>10.0%}{top5:>8.0%}{mrr:>7.2f}")

    sem = sorted(q["similaridade"] for q in questions if not q["esperado"])
    com = sorted(q["similaridade"] for q in questions if q["esperado"])
    print(f"\nMaior similaridade nas {len(sem)} perguntas sem incidente parecido: "
          f"{', '.join(f'{v:.3f}' for v in sem)}")
    print(f"Nas perguntas com resposta: mediana {com[len(com) // 2]:.3f}, 10% abaixo de {com[len(com) // 10]:.3f}")

    saida = EVALUATION / "results.json"
    saida.write_text(json.dumps({"modelo": MODEL, "perguntas": questions}, ensure_ascii=False, indent=1) + "\n",
                     encoding="utf-8")
    print(f"\nResultado de cada pergunta em {saida}")


if __name__ == "__main__":
    main()
