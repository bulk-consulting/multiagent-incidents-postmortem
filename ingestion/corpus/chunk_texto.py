"""
Chunks do texto completo. Entram nas duas etapas da busca: na etapa 1, junto com o chunk de
resumo, para achar os incidentes; na etapa 2, para trazer os detalhes e a evidência literal.

Regras:
1. o texto é dividido nos intertítulos (linhas "# ...", "## ..."); o que vem antes do primeiro
   intertítulo é uma seção sem título. Documento sem intertítulos = uma seção só;
2. seções curtas (abaixo de --minimo tokens) se juntam às seguintes enquanto couberem no limite;
   o chunk leva os títulos juntados ("Monitoring / Update");
3. seção acima do limite é dividida entre parágrafos (blocos separados por linha em branco),
   nunca no meio de um; cada parte mantém o título da seção;
4. parágrafo sozinho acima do limite é dividido entre frases (ou linhas, se não houver frases),
   com sobreposição de uma frase entre as partes; é o único caso com sobreposição. Sobreposição
   de ~60 tokens entre chunks foi testada e não mudou a busca (ingestion/avaliacao/RESULTADOS.md).

Cada chunk guarda `content` (o texto do corpus, exato), `texto_embedding` (cabeçalho
empresa — título — seção + content normalizado) e metadados do documento. Os tokens são contados
sobre o texto_embedding com o tokenizador do multilingual-e5-base (ver chunk_fichas.py).

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/corpus/chunk_texto.py [--limite 450] [--minimo 100] [--estimado]

Lê:    ingestion/corpus/corpus.jsonl
Grava: ingestion/corpus/chunks_texto.jsonl
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location("chunk_fichas", PASTA / "chunk_fichas.py")
_cf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cf)
normalizar_para_embedding = _cf.normalizar_para_embedding
titulo_do_documento = _cf.titulo_do_documento
estimar_tokens = _cf.estimar_tokens
escolher_contador = _cf.escolher_contador

INTERTITULO = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
FRASE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(\[])")


def secoes(texto: str) -> list[tuple[str, list[str]]]:
    """[(título, parágrafos)], na ordem do texto."""
    saida: list[tuple[str, list[str]]] = [("", [])]
    for bloco in re.split(r"\n\s*\n", texto):
        linhas = bloco.strip("\n").split("\n")
        # um bloco pode começar com intertítulo e trazer texto colado logo abaixo
        while linhas and INTERTITULO.match(linhas[0].strip()):
            titulo = INTERTITULO.match(linhas[0].strip()).group(1).strip("*_ ").strip()
            saida.append((titulo, []))
            linhas = linhas[1:]
        resto = "\n".join(linhas).strip()
        if resto:
            saida[-1][1].append(resto)
    return [(t, ps) for t, ps in saida if ps or t]


def cortar_por_palavras(texto: str, cabeca: str, limite: int, contar) -> list[str]:
    """Corta em pedaços de palavras inteiras, cada um com o máximo que cabe no limite (busca binária)."""
    palavras, pedacos, i = texto.split(), [], 0
    while i < len(palavras):
        lo, hi = 1, len(palavras) - i
        while lo < hi:
            meio = (lo + hi + 1) // 2
            if contar(cabeca + "\n" + normalizar_para_embedding(" ".join(palavras[i:i + meio]))) <= limite:
                lo = meio
            else:
                hi = meio - 1
        pedacos.append(" ".join(palavras[i:i + lo]))
        i += lo
    return pedacos


def partir_paragrafo(p: str, cabeca: str, limite: int, contar) -> list[str]:
    """Divide um parágrafo grande entre frases (ou linhas), com 1 frase de sobreposição."""
    unidades = [u for u in FRASE.split(p) if u.strip()]
    if len(unidades) <= 1:
        unidades = [u for u in p.split("\n") if u.strip()]
    if len(unidades) <= 1:  # sem frases nem linhas: corta por palavras
        return cortar_por_palavras(p, cabeca, limite, contar)
    partes, atual = [], []
    for u in unidades:
        if atual and contar(cabeca + "\n" + normalizar_para_embedding(" ".join(atual + [u]))) > limite:
            partes.append(" ".join(atual))
            atual = [atual[-1]] if contar(cabeca + "\n" + atual[-1]) < limite / 3 else []
        atual.append(u)
    if atual:
        partes.append(" ".join(atual))
    # último recurso: parte que ainda passa do limite (linha enorme de código ou tabela) é cortada por palavras
    finais = []
    for parte in partes:
        if contar(cabeca + "\n" + normalizar_para_embedding(parte)) <= limite:
            finais.append(parte)
            continue
        finais += cortar_por_palavras(parte, cabeca, limite, contar)
    return finais


def montar_chunks(doc: dict, limite: int, minimo: int, contar=estimar_tokens) -> list[dict]:
    base = f"{doc.get('company') or ''} — {titulo_do_documento(doc)}".strip(" —")

    titulo_doc = titulo_do_documento(doc).lower()

    def cab(titulos: list[str]) -> str:
        # o título da seção que repete o título do documento não entra de novo no cabeçalho
        t = " / ".join(dict.fromkeys(x for x in titulos if x and x.lower() != titulo_doc))
        return f"{base} — {t}" if t else base

    def para_embedding(content: str) -> str:
        # as linhas "## Título" já estão no cabeçalho; no vetor elas não se repetem
        sem_titulos = "\n".join(l for l in content.split("\n") if not INTERTITULO.match(l.strip()))
        return normalizar_para_embedding(sem_titulos)

    def tam(titulos, paragrafos) -> int:
        return contar(cab(titulos) + "\n" + para_embedding("\n\n".join(paragrafos)))

    # 1) unidades = (títulos, parágrafos) já dentro do limite
    unidades: list[tuple[list[str], list[str]]] = []
    for titulo, paragrafos in secoes(doc["text"]):
        bloco_titulo = [f"## {titulo}"] if titulo else []
        atual: list[str] = []
        for p in paragrafos:
            if tam([titulo], bloco_titulo + [p]) > limite:
                if atual:
                    unidades.append(([titulo], bloco_titulo + atual))
                    atual = []
                for pedaco in partir_paragrafo(p, cab([titulo]) + "\n" + "\n".join(bloco_titulo), limite, contar):
                    unidades.append(([titulo], bloco_titulo + [pedaco]))
                continue
            if atual and tam([titulo], bloco_titulo + atual + [p]) > limite:
                unidades.append(([titulo], bloco_titulo + atual))
                atual = []
            atual.append(p)
        if atual or (titulo and not paragrafos):
            unidades.append(([titulo], bloco_titulo + atual))

    # 2) junta unidades curtas com as seguintes enquanto couberem
    juntas: list[tuple[list[str], list[str]]] = []
    for titulos, ps in unidades:
        if juntas and tam(*juntas[-1]) < minimo and tam(juntas[-1][0] + titulos, juntas[-1][1] + ps) <= limite:
            juntas[-1] = (juntas[-1][0] + titulos, juntas[-1][1] + ps)
        else:
            juntas.append((titulos, ps))
    # a última, se curta, volta para a anterior quando couber
    if len(juntas) > 1 and tam(*juntas[-1]) < minimo and tam(juntas[-2][0] + juntas[-1][0], juntas[-2][1] + juntas[-1][1]) <= limite:
        t, p = juntas.pop()
        juntas[-1] = (juntas[-1][0] + t, juntas[-1][1] + p)

    chunks = []
    for k, (titulos, ps) in enumerate(juntas):
        content = "\n\n".join(ps)
        if not content.strip():
            continue
        cabeca = cab(titulos)
        emb = cabeca + "\n" + para_embedding(content)
        chunks.append({
            "chunk_id": f"{doc['catalog_id']}:texto:{k:03d}",
            "catalog_id": doc["catalog_id"],
            "tipo": "texto",
            "ordem": k,
            "secao": " / ".join(dict.fromkeys(x for x in titulos if x)) or None,
            "content": content,
            "texto_embedding": emb,
            "tokens": contar(emb),
            "company": doc.get("company"),
            "title": doc.get("title"),
            "url": doc.get("url"),
            "incident_date": doc.get("incident_date"),
            "text_source": doc.get("text_source"),
            "catalogo": doc.get("catalogo"),
            "problemas_texto": doc.get("problemas_texto", []),
        })
    return chunks


def main() -> None:
    limite, minimo = 450, 100
    contar, metodo = escolher_contador(sys.argv)
    if "--limite" in sys.argv:
        limite = int(sys.argv[sys.argv.index("--limite") + 1])
    if "--minimo" in sys.argv:
        minimo = int(sys.argv[sys.argv.index("--minimo") + 1])
    docs = [json.loads(l) for l in (PASTA / "corpus.jsonl").open(encoding="utf-8")]
    todos, por_doc = [], {}
    for doc in docs:
        cs = montar_chunks(doc, limite, minimo, contar)
        por_doc[doc["catalog_id"]] = len(cs)
        todos += cs
    with (PASTA / "chunks_texto.jsonl").open("w", encoding="utf-8") as f:
        for c in todos:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    tam = sorted(c["tokens"] for c in todos)
    n = sorted(por_doc.values())
    print(f"{len(todos)} chunks de {len(docs)} documentos (limite {limite}, mínimo {minimo}, contagem: {metodo}) -> "
          f"{(PASTA / 'chunks_texto.jsonl').relative_to(ROOT)}")
    print(f"  tokens: mediana {tam[len(tam)//2]}  p10 {tam[len(tam)//10]}  p90 {tam[int(.9*len(tam))]}  max {tam[-1]}")
    print(f"  abaixo do mínimo: {sum(t < minimo for t in tam)}  acima do limite: {sum(t > limite for t in tam)}")
    print(f"  chunks por documento: mediana {n[len(n)//2]}  max {n[-1]} "
          f"({max(por_doc, key=por_doc.get)})  min {n[0]} ({min(por_doc, key=por_doc.get)})")
    print(f"  sem seção (doc sem intertítulos ou introdução): {sum(1 for c in todos if not c['secao'])}")


if __name__ == "__main__":
    main()
