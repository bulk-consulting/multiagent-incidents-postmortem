"""Gera um HTML que mostra, em cores, como um post-mortem foi dividido em chunks.

Uso: python visualize_chunks.py [catalog_id]   (padrão: DAN-004, que tem overlap)

Lê data/chunks/danluu_chunks.jsonl e grava data/exports/chunks_<catalog_id>.html.
Serve para explicar a estratégia de chunking (docs/E2_3_Estrategia_Chunking.md).
"""

import html
import json
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
CHUNKS = DATA / "chunks" / "danluu_chunks.jsonl"

# Mesmos valores de chunk.py
MAX_TOKENS = 450
MODEL_LIMIT = 512

COLORS = ["#dbeafe", "#dcfce7", "#fef9c3", "#fce7f3", "#ede9fe", "#ffedd5", "#ccfbf1"]
BORDERS = ["#3b82f6", "#22c55e", "#eab308", "#ec4899", "#8b5cf6", "#f97316", "#14b8a6"]

CSS = """
body { font-family: system-ui, sans-serif; max-width: 860px; margin: 2rem auto; padding: 0 1rem;
       line-height: 1.55; color: #1f2937; }
h1 { font-size: 1.5rem; margin-bottom: .25rem; }
.source { color: #6b7280; font-size: .9rem; margin-bottom: 1.5rem; }
.chunk { border-left: 6px solid; border-radius: 6px; padding: .5rem 1rem 1rem; margin: 1rem 0; }
.meta { display: flex; justify-content: space-between; align-items: center; font-size: .8rem;
        font-weight: 600; color: #374151; }
.bar { width: 160px; height: 8px; background: #fff; border-radius: 4px; position: relative; }
.bar span { position: absolute; left: 0; top: 0; bottom: 0; border-radius: 4px; }
.bar i { position: absolute; top: -3px; bottom: -3px; width: 2px; background: #111; }
.header { font-family: ui-monospace, monospace; font-size: .75rem; color: #6b7280;
          background: rgba(255,255,255,.6); padding: .2rem .4rem; border-radius: 4px; margin: .4rem 0; }
.chunk h3 { font-size: 1.05rem; margin: .75rem 0 .25rem; }
.chunk p { margin: .5rem 0; }
.summary { background: #f3f4f6; border-color: #111827; }
mark.overlap { background: repeating-linear-gradient(45deg, #fca5a5, #fca5a5 6px, #fecaca 6px, #fecaca 12px); }
.split { border: 2px dashed #ef4444; border-radius: 10px; padding: .25rem .75rem; margin: 1.5rem 0; }
"""

def overlap_length(previous: str, current: str) -> int:
    """Tamanho do início de `current` que repete o fim de `previous` (0 se não houver)."""
    # O tokenizer.decode pode mudar espaços no fim da janela, então procuramos o
    # maior prefixo de `current` que aparece perto do fim de `previous`
    tail = previous[-1500:]
    # O chunk que continua uma seção começa repetindo o título dela; o overlap vem depois
    if current.startswith("#") and "\n\n" in current:
        title, rest = current.split("\n\n", 1)
        k = overlap_length(previous, rest)
        return len(title) + 2 + k if k else 0
    k = 0
    while k < len(current) and current[:k + 1] in tail:
        k += 1
    return k if k >= 20 and len(tail) - (tail.rfind(current[:k]) + k) < 10 else 0


def overlap_text(body: str, head: int) -> str:
    """O trecho repetido do chunk anterior, sem o título da seção repetido no início."""
    if not head:
        return ""
    if body.startswith("#") and "\n\n" in body:
        title, rest = body.split("\n\n", 1)
        return rest[:head - len(title) - 2]
    return body[:head]


def mark(text: str) -> str:
    return f'<mark class="overlap">{html.escape(text)}</mark>'


def render_paragraph(paragraph: str, head: int = 0, tail: str = "") -> str:
    """`head`: caracteres iniciais repetidos do chunk anterior; `tail`: trecho final repetido no próximo."""
    if paragraph.startswith("#"):
        return f"<h3>{html.escape(paragraph.lstrip('#').rstrip('#').strip())}</h3>"
    lines = paragraph.split("\n")
    if not head and not tail and all(line.startswith("- ") for line in lines):
        items = "".join(f"<li>{html.escape(line[2:])}</li>" for line in lines)
        return f"<ul>{items}</ul>"
    tail_start = paragraph.rfind(tail) if tail else -1
    if tail_start < 0:  # sem overlap com o próximo chunk (ou trecho não encontrado): nada marcado no fim
        tail, tail_start = "", len(paragraph)
    tail_start = max(tail_start, head)
    text = (mark(paragraph[:head]) if head else "") + html.escape(paragraph[head:tail_start]) \
        + (mark(paragraph[tail_start:]) if tail else "")
    # Lista com overlap: mantém uma linha por item
    is_list = all(line.startswith("- ") for line in lines)
    return f'<p style="white-space:pre-line">{text}</p>' if is_list else f"<p>{text}</p>"


def render_chunk(chunk: dict, color_index: int, head: int, tail: str, part: str) -> str:
    if chunk["chunk_type"] == "summary":  # o summary não tem cabeçalho
        header, body = "", chunk["text"]
    else:
        header, _, body = chunk["text"].partition("\n")
        body = body.strip()
    tokens = chunk["token_count"]
    color, border = COLORS[color_index % len(COLORS)], BORDERS[color_index % len(BORDERS)]
    if chunk["chunk_type"] == "summary":
        css_class, style, border = "chunk summary", "", "#111827"
        content = f"<p>{html.escape(body)}</p>"
        label = "summary do catálogo"
    else:
        css_class, style = "chunk", f'style="background:{color};border-color:{border}"'
        paragraphs = body.split("\n\n")
        # com o título da seção repetido no início, o overlap começa no parágrafo seguinte
        first = 1 if head and paragraphs[0].startswith("#") and len(paragraphs) > 1 else 0
        head_first = head - (len(paragraphs[0]) + 2) if first else head
        rendered = []
        for i, p in enumerate(paragraphs):
            rendered.append(render_paragraph(p, head_first if i == first else 0,
                                             tail if i == len(paragraphs) - 1 else ""))
        content = "".join(rendered)
        label = part or f"{len(paragraphs)} parágrafo(s)"
    return f"""
<section class="{css_class}" {style} title="{chunk['chunk_id']} · {tokens} tokens">
  <div class="meta">
    <span>{chunk['chunk_id']} · {label}</span>
    <span>{tokens} tokens
      <span class="bar" style="display:inline-block;margin-left:.5rem">
        <span style="width:{min(tokens / MODEL_LIMIT, 1) * 100:.0f}%;background:{border}"></span>
        <i style="left:{MAX_TOKENS / MODEL_LIMIT * 100:.0f}%"></i>
      </span>
    </span>
  </div>
  <div class="header">{html.escape(header)}</div>
  {content}
</section>"""


def main() -> None:
    catalog_id = sys.argv[1] if len(sys.argv) > 1 else "DAN-004"
    chunks = [c for c in map(json.loads, CHUNKS.open(encoding="utf-8")) if c["catalog_id"] == catalog_id]
    if not chunks:
        sys.exit(f"Nenhum chunk encontrado para {catalog_id}")

    bodies = [c["text"].partition("\n")[2].strip() for c in chunks]
    # heads[i]: quantos caracteres do início do chunk i repetem o chunk i-1
    heads = [0] * len(chunks)
    for i in range(2, len(chunks)):
        heads[i] = overlap_length(bodies[i - 1], bodies[i])

    # Sequências de partes de um mesmo parágrafo longo: [início, fim]
    runs = []
    for i in range(len(chunks)):
        if heads[i]:
            if runs and runs[-1][1] == i - 1:
                runs[-1][1] = i
            else:
                runs.append([i - 1, i])

    sections = []
    i = 0
    while i < len(chunks):
        run = next((r for r in runs if r[0] == i), None)
        indexes = range(run[0], run[1] + 1) if run else [i]
        parts = []
        for n, j in enumerate(indexes):
            tail = overlap_text(bodies[j + 1], heads[j + 1]) if j + 1 < len(chunks) else ""
            extra = len(bodies[j].split("\n\n")) - 1
            part = f"parte {n + 1} de {len(indexes)} do parágrafo longo" if run else ""
            if part and extra:
                part += f" + {extra} parágrafo(s)"
            parts.append(render_chunk(chunks[j], j - 1, heads[j], tail, part))
        if run:
            sections.append(f'<div class="split">{"".join(parts)}</div>')
        else:
            sections.extend(parts)
        i = indexes[-1] + 1

    first = chunks[0]
    n_overlap = sum(1 for h in heads if h)
    page = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="utf-8"><title>Chunks de {catalog_id}</title><style>{CSS}</style></head>
<body>
<h1>{html.escape(first['title'])}</h1>
<div class="source">{catalog_id} · {html.escape(first['company'])} · {html.escape(first['category'])} ·
  <a href="{html.escape(first['source_url'])}">post-mortem original</a></div>

{''.join(sections)}
</body>
</html>"""

    output = DATA / "exports" / f"chunks_{catalog_id}.html"
    output.write_text(page, encoding="utf-8")
    print(f"{len(chunks)} chunks ({n_overlap} com overlap) -> {output}")


if __name__ == "__main__":
    main()
