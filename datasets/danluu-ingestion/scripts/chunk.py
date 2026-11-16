"""Divide os post-mortems limpos em chunks para o RAG.

Lê data/processed/danluu_clean.jsonl e grava data/chunks/danluu_chunks.jsonl.
Para cada documento:
- chunk 0: o summary do catálogo, sem cabeçalho;
- chunks seguintes: cabeçalho + grupo de parágrafos (separados por "\\n\\n"),
  somados até MAX_TOKENS, contando o cabeçalho. Um parágrafo grande demais é
  dividido em partes de tamanho parecido, cortadas no fim de uma frase, e cada
  parte repete as últimas frases da anterior (até OVERLAP_TOKENS).
- quando uma seção longa é dividida em vários chunks, cada chunk que continua a
  seção começa repetindo o título dela ("## Root cause"), para não ficar sem
  contexto.
Os tokens são contados com o tokenizer do multilingual-e5-base (limite de 512).
O modelo de embeddings (Qwen3-Embedding-0.6B) tem outro tokenizer e lê bem mais
que isso; a contagem do e5 serve como aproximação do tamanho.
"""

import json
import math
import re
import statistics
from pathlib import Path

from transformers import AutoTokenizer

DATA = Path(__file__).resolve().parent.parent / "data"
INPUT = DATA / "processed" / "danluu_clean.jsonl"
OUTPUT = DATA / "chunks" / "danluu_chunks.jsonl"

TOKENIZER = "intfloat/multilingual-e5-base"
# Tamanho máximo do chunk inteiro, com o cabeçalho
MAX_TOKENS = 450
OVERLAP_TOKENS = 60
# Um último grupo menor que isso é juntado ao grupo anterior
MIN_TOKENS = 50
# Fim de frase (. ! ? seguido de espaço) ou quebra de linha; fim de trecho (, ; :)
SENTENCE_END = r"(?<=[.!?])(?=\s)|(?=\n)"
CLAUSE_END = r"(?<=[,;:])(?=\s)"

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER)
tokenizer.model_max_length = 10**9  # só contamos tokens; o aviso de sequência longa não se aplica


def count_tokens(text: str) -> int:
    return len(tokenizer(text, add_special_tokens=False)["input_ids"])


def is_title(piece: str) -> bool:
    return piece.startswith("#")


def split_at(text: str, pattern: str) -> list[str]:
    # Corta logo depois do separador; cada pedaço mantém o espaço que vinha antes dele
    return [piece for piece in re.split(pattern, text) if piece.strip()]


def split_units(paragraph: str, max_tokens: int) -> list[str]:
    """Quebra o parágrafo em frases (ou linhas). Uma frase grande demais é quebrada
    nas vírgulas e, em último caso, por tokens."""
    limit = max_tokens - OVERLAP_TOKENS
    units = []
    for sentence in split_at(paragraph, SENTENCE_END):
        if count_tokens(sentence) <= limit:
            units.append(sentence)
            continue
        for clause in split_at(sentence, CLAUSE_END):
            if count_tokens(clause) <= limit:
                units.append(clause)
            else:
                ids = tokenizer(clause, add_special_tokens=False)["input_ids"]
                units += [" " + tokenizer.decode(ids[i:i + limit]) for i in range(0, len(ids), limit)]
    return units


def split_large_paragraph(paragraph: str, max_tokens: int) -> list[str]:
    """Divide um parágrafo grande em partes de tamanho parecido (até max_tokens),
    sempre no fim de uma frase. Cada parte começa repetindo as últimas frases da
    anterior, até OVERLAP_TOKENS."""
    units = split_units(paragraph, max_tokens)
    sizes = [count_tokens(u) for u in units]
    total = sum(sizes)
    n_parts = math.ceil((total - OVERLAP_TOKENS) / (max_tokens - OVERLAP_TOKENS))
    target = math.ceil((total + (n_parts - 1) * OVERLAP_TOKENS) / n_parts)

    parts, start, previous_start = [], 0, 0
    while start < len(units):
        # Overlap: frases inteiras do fim da parte anterior, até OVERLAP_TOKENS
        first, size = start, 0
        while parts and first - 1 > previous_start and size + sizes[first - 1] <= OVERLAP_TOKENS:
            first -= 1
            size += sizes[first]
        end = start
        while end < len(units) and (
                end == start
                or size + sizes[end] <= target
                or size + sum(sizes[end:]) <= max_tokens):  # o resto cabe: não deixa sobra pequena
            size += sizes[end]
            end += 1
        parts.append("".join(units[first:end]).strip())
        previous_start, start = start, end
    return parts


def group_paragraphs(text: str, header: str) -> list[str]:
    def size(parts: list[str]) -> int:
        return count_tokens(header + "\n\n" + "\n\n".join(parts))

    # 1) parágrafos, com os grandes demais já divididos. Cada pedaço guarda o título
    #    da seção em que está, para ser repetido se a seção continuar em outro chunk.
    pieces: list[tuple[str, str | None]] = []
    section = None
    for paragraph in (p.strip() for p in text.split("\n\n")):
        if not paragraph:
            continue
        if is_title(paragraph):
            section = paragraph.split("\n", 1)[0]
        title = [section] if section and section != paragraph.split("\n", 1)[0] else []
        if size(title + [paragraph]) > MAX_TOKENS:
            budget = MAX_TOKENS - size(title) - 2
            pieces += [(part, section) for part in split_large_paragraph(paragraph, budget)]
        else:
            pieces.append((paragraph, section))

    # 2) junta os pedaços em grupos até MAX_TOKENS
    groups: list[list[str]] = []
    current: list[str] = []
    continues_section = False  # o grupo atual começa com o título repetido
    for piece, section in pieces:
        # Um título começa um grupo novo, junto com o conteúdo que vem depois,
        # a menos que o grupo atual seja pequeno demais para ficar sozinho
        starts_section = is_title(piece) and size(current) >= MIN_TOKENS
        too_big = size(current + [piece]) > MAX_TOKENS
        only_titles = all(is_title(p) for p in current)
        if current and not only_titles and (starts_section or too_big):
            groups.append(current)
            current = []
            # a seção continua neste grupo novo: ele começa com o título dela
            continues_section = not is_title(piece) and section is not None
            if continues_section:
                current = [section]
        current.append(piece)
    if current:
        groups.append(current)

    # 3) um último grupo pequeno volta para o anterior, se couber
    if len(groups) > 1 and size(groups[-1]) < MIN_TOKENS:
        last = groups[-1][1:] if continues_section else groups[-1]
        if size(groups[-2] + last) <= MAX_TOKENS:
            groups.pop()
            groups[-1] = groups[-1] + last

    return ["\n\n".join(g) for g in groups]


def main() -> None:
    documents = [json.loads(line) for line in INPUT.open(encoding="utf-8")]

    chunks = []
    for doc in documents:
        header = f"Company: {doc['company']} | Title: {doc['title']} | Category: {doc['category']}"
        # O summary vai sem cabeçalho: ele já descreve o incidente inteiro, e o cabeçalho
        # (título longo, categoria) deixava o vetor menos parecido com as perguntas
        texts = [("summary", doc["summary"])]
        # Alguns documentos trazem o mesmo trecho duas vezes (páginas de status que repetem o
        # relatório): um chunk idêntico a outro do mesmo documento é descartado
        groups = list(dict.fromkeys(group_paragraphs(doc["extracted_text"], header)))
        texts += [("text", f"{header}\n\n{group}") for group in groups]

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
              f"mediana {statistics.median(sizes):.0f}, máx {max(sizes)} | acima de {MAX_TOKENS}: "
              f"{sum(s > MAX_TOKENS for s in sizes)}")
    print(f"Documentos: {len(documents)} | chunks: {len(chunks)} em {OUTPUT}")


if __name__ == "__main__":
    main()
