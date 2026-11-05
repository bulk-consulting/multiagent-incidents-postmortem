"""Divide os post-mortems limpos em chunks para o RAG.

Lê data/processed/danluu_clean.jsonl e grava data/chunks/danluu_chunks.jsonl.
Para cada documento:
- chunk 0: cabeçalho + summary;
- chunks seguintes: cabeçalho + grupo de parágrafos (separados por "\\n\\n"),
  somados até MAX_TOKENS. Um parágrafo maior que MAX_TOKENS é dividido em
  janelas de tokens com OVERLAP_TOKENS de sobreposição.
Os tokens são contados com o tokenizer do modelo de embeddings.
"""

import json
import statistics
from pathlib import Path

from transformers import AutoTokenizer

DATA = Path(__file__).resolve().parent.parent / "data"
INPUT = DATA / "processed" / "danluu_clean.jsonl"
OUTPUT = DATA / "chunks" / "danluu_chunks.jsonl"

MODEL = "intfloat/multilingual-e5-base"
MAX_TOKENS = 400
OVERLAP_TOKENS = 60
# Um último grupo menor que isso é juntado ao grupo anterior
MIN_TOKENS = 50

tokenizer = AutoTokenizer.from_pretrained(MODEL)


def count_tokens(text: str) -> int:
    return len(tokenizer(text, add_special_tokens=False)["input_ids"])


def split_large_paragraph(paragraph: str) -> list[str]:
    ids = tokenizer(paragraph, add_special_tokens=False)["input_ids"]
    step = MAX_TOKENS - OVERLAP_TOKENS
    return [tokenizer.decode(ids[i:i + MAX_TOKENS]) for i in range(0, len(ids), step)
            if i == 0 or i + OVERLAP_TOKENS < len(ids)]


def group_paragraphs(text: str) -> list[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    pieces = []
    for paragraph in paragraphs:
        if count_tokens(paragraph) > MAX_TOKENS:
            pieces.extend(split_large_paragraph(paragraph))
        else:
            pieces.append(paragraph)

    groups, current = [], []
    for piece in pieces:
        # Um título começa um grupo novo, junto com o conteúdo que vem depois,
        # a menos que o grupo atual seja pequeno demais para ficar sozinho
        starts_section = piece.startswith("#") and count_tokens("\n\n".join(current)) >= MIN_TOKENS
        too_big = count_tokens("\n\n".join(current + [piece])) > MAX_TOKENS
        only_titles = all(p.startswith("#") for p in current)
        if current and not only_titles and (starts_section or too_big):
            groups.append("\n\n".join(current))
            current = []
        current.append(piece)
    if current:
        groups.append("\n\n".join(current))

    if len(groups) > 1 and count_tokens(groups[-1]) < MIN_TOKENS:
        last = groups.pop()
        groups[-1] = groups[-1] + "\n\n" + last

    return groups


def main() -> None:
    documents = [json.loads(line) for line in INPUT.open(encoding="utf-8")]

    chunks = []
    for doc in documents:
        header = f"Company: {doc['company']} | Title: {doc['title']} | Category: {doc['category']}"
        texts = [("summary", f"{header}\nSummary: {doc['summary']}")]
        texts += [("text", f"{header}\n\n{group}") for group in group_paragraphs(doc["extracted_text"])]

        for index, (chunk_type, text) in enumerate(texts):
            chunks.append({
                "chunk_id": f"{doc['catalog_id']}-{index:03d}",
                "catalog_id": doc["catalog_id"],
                "chunk_index": index,
                "chunk_type": chunk_type,
                "token_count": count_tokens(text),
                "text": text,
                "title": doc["title"],
                "source_url": doc["source_url"],
                "company": doc["company"],
                "category": doc["category"],
            })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    for chunk_type in ("summary", "text"):
        sizes = [c["token_count"] for c in chunks if c["chunk_type"] == chunk_type]
        print(f"Chunks {chunk_type}: {len(sizes)} | tokens mín {min(sizes)}, "
              f"mediana {statistics.median(sizes):.0f}, máx {max(sizes)}")
    print(f"Documentos: {len(documents)} | chunks: {len(chunks)} em {OUTPUT}")


if __name__ == "__main__":
    main()
