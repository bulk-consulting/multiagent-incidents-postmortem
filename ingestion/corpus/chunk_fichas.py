"""
Chunks das fichas (etapa 1 da busca: achar incidentes parecidos).

Cada ficha do corpus vira até 4 chunks, um por assunto:
- resumo:     resumo + detecção + serviços afetados + tecnologias + categoria da causa
- causa:      causa raiz + gatilho + mudança causadora + fatores contribuintes
- mitigacao:  passos que restauraram o serviço
- prevencao:  ações para não repetir (com o estado: Already done / In progress / Planned)

Campo vazio não vira chunk. Se um chunk passa do limite de tokens, ele é dividido num ponto
natural: a parte fixa (no de causa: causa raiz + gatilho + mudança) fica num chunk e os itens
(fatores, passos, ações) vão em grupos que cabem no limite, cada grupo com o mesmo rótulo.

Cada chunk guarda:
- content: o texto montado da ficha (em inglês, como a ficha), que o agente lê;
- texto_embedding: cabeçalho (empresa — título — assunto) + content normalizado, que vira vetor
  (os prefixos próprios de cada modelo, como "passage: ", entram só na hora do embedding);
- trechos: os trechos literais do documento que provam cada afirmação do chunk (evidência);
- metadados do documento e da ficha, para filtros e para mostrar a fonte.

A contagem de tokens é uma estimativa (palavras x 1,35) até o modelo de embedding ser escolhido;
depois ela passa a usar o tokenizador do modelo (parâmetro `contar`).

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/corpus/chunk_fichas.py [--limite 400]

Lê:    ingestion/corpus/corpus.jsonl, ingestion/fichas/saida/DAN-*.json
Grava: ingestion/corpus/chunks_fichas.jsonl
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent
FICHAS = ROOT / "ingestion" / "fichas" / "saida"

_spec = importlib.util.spec_from_file_location("normalizar_embedding", PASTA / "normalizar_embedding.py")
_norm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_norm)
normalizar_para_embedding = _norm.normalizar_para_embedding

ROTULO = {"resumo": "Incident summary", "causa": "Root cause", "mitigacao": "Mitigation", "prevencao": "Prevention"}


SUFIXO_SITE = re.compile(r"blog|engineering|status|discuss|announcements|news|medium|wiki|dashboard|"
                         r"incident|community|forum|hacker news|reddit|the free encyclopedia", re.I)


def titulo_limpo(titulo: str | None, empresa: str | None) -> str:
    """Tira do título da página os sufixos de site ("| Datadog", "- The GitHub Blog")."""
    partes = re.split(r"\s+[|–—-]\s+|\s+::\s+|\s+»\s*$", (titulo or "").strip())
    partes = [p for p in partes if p]
    emp = re.sub(r"\.(io|com|org|net|co)$", "", (empresa or "").lower().split(" (")[0].strip())
    while len(partes) > 1 and ((emp and emp in partes[-1].lower()) or SUFIXO_SITE.search(partes[-1])):
        partes.pop()
    # prefixo de página de status: "Travis CI Status - <incidente>"
    while len(partes) > 1 and re.search(r"\bstatus$", partes[0], re.I):
        partes.pop(0)
    return " - ".join(partes)


TITULO_GENERICO = re.compile(r"^(incident details|.*status dashboard|service health|final incident report|"
                             r"incident report|postmortem|post-mortem|update\b.*|resolved|investigating|summary|"
                             r"background|overview|introduction|timeline|what happened\??|.* status|status updates?|details|"
                             r"\d{1,2} \w{3,9},? \d{4}\b.*|\w{3,9} \d{1,2},? \d{4}\b.*)$", re.I)


def titulo_do_documento(doc: dict, ficha: dict) -> str:
    """Título limpo; se for genérico ou vazio, o 1º intertítulo útil do texto; senão o início do resumo."""
    t = titulo_limpo(doc.get("title"), doc.get("company"))
    if t and not TITULO_GENERICO.match(t):
        return t
    for h in re.findall(r"^#{1,6} (.+)$", doc.get("text", ""), re.M):
        h = h.strip().strip("*_# ").strip()
        if h and not TITULO_GENERICO.match(h) and not h.endswith("?"):
            return h
    resumo = (ficha.get("incidente") or {}).get("resumo") or doc["catalog_id"]
    frase = re.split(r"(?<=[.;])\s", resumo, 1)[0]
    return frase if len(frase) <= 120 else frase[:117].rsplit(" ", 1)[0] + "..."


def estimar_tokens(texto: str) -> int:
    return int(len(texto.split()) * 1.35) + 1


def afirmacao(o) -> tuple[str, list[str]]:
    """(texto, trechos) de um objeto {"texto", "trechos"}; ("", []) se vazio."""
    if isinstance(o, dict) and o.get("texto"):
        return o["texto"], list(o.get("trechos") or [])
    return "", []


def partes_da_ficha(ficha: dict) -> dict[str, tuple[list[str], list[tuple[str, list[str]]], list[str]]]:
    """Para cada assunto: (linhas fixas, itens [(linha, trechos)], trechos das linhas fixas)."""
    i = ficha["incidente"]
    partes = {}

    # resumo
    fixas, tr = [f"Summary: {i['resumo']}"], []
    det_txt, det_tr = afirmacao((i.get("deteccao") or {}).get("descricao"))
    forma = (i.get("deteccao") or {}).get("forma")
    if det_txt:
        fixas.append(f"Detection ({forma}): {det_txt}" if forma else f"Detection: {det_txt}")
        tr += det_tr
    if i.get("servicos_afetados"):
        fixas.append("Affected services: " + ", ".join(i["servicos_afetados"]))
    if i.get("tecnologias"):
        fixas.append("Technologies: " + ", ".join(i["tecnologias"]))
    if i.get("categoria_causa"):
        fixas.append(f"Root cause category: {i['categoria_causa']}")
    partes["resumo"] = (fixas, [], tr)

    # causa
    fixas, tr = [], []
    causa = i.get("causa_raiz") or {}
    c_txt, c_tr = afirmacao(causa.get("descricao"))
    if c_txt:
        status = causa.get("status")
        fixas.append(f"Root cause ({status}): {c_txt}" if status else f"Root cause: {c_txt}")
        tr += c_tr
    g_txt, g_tr = afirmacao(i.get("gatilho"))
    if g_txt:
        fixas.append(f"Trigger: {g_txt}")
        tr += g_tr
    mud = i.get("mudanca_causadora") or {}
    m_txt, m_tr = afirmacao(mud.get("descricao"))
    if m_txt:
        fixas.append(f"Causal change ({mud.get('nivel')}): {m_txt}")
        tr += m_tr
    itens = []
    for f in i.get("fatores_contribuintes") or []:
        t, ftr = afirmacao(f)
        if t:
            itens.append((f"- Contributing factor: {t}", ftr))
    if fixas or itens:
        partes["causa"] = (fixas, itens, tr)

    # mitigação
    passos = [afirmacao(p) for p in (i.get("mitigacao") or {}).get("passos") or []]
    itens = [(f"{k}. {t}", ptr) for k, (t, ptr) in enumerate([p for p in passos if p[0]], 1)]
    if itens:
        partes["mitigacao"] = (["Mitigation steps:"], itens, [])

    # prevenção
    acoes = [afirmacao(a) for a in (i.get("prevencao") or {}).get("acoes") or []]
    itens = [(f"- {t}", atr) for t, atr in acoes if t]
    if itens:
        partes["prevencao"] = (["Prevention actions:"], itens, [])
    return partes


def montar_chunks(ficha: dict, doc: dict, limite: int, contar=estimar_tokens) -> list[dict]:
    cabeca_base = f"{doc.get('company') or ''} — {titulo_do_documento(doc, ficha)}".strip(" —")
    chunks = []
    for assunto, (fixas, itens, tr_fixas) in partes_da_ficha(ficha).items():
        cabeca = f"{cabeca_base} — {ROTULO[assunto]}"
        grupos: list[tuple[list[str], list[str]]] = []  # (linhas, trechos)
        tudo = fixas + [l for l, _ in itens]
        if contar(cabeca + "\n" + "\n".join(tudo)) <= limite or not itens:
            grupos.append((tudo, tr_fixas + [t for _, ts in itens for t in ts]))
        else:
            # parte fixa sozinha (se houver conteúdo além do rótulo) e itens em grupos que cabem
            rotulo_itens = fixas if assunto in ("mitigacao", "prevencao") else []
            if fixas and not rotulo_itens:
                grupos.append((fixas, tr_fixas))
            atual, atual_tr = list(rotulo_itens), []
            for linha, ltr in itens:
                if len(atual) > len(rotulo_itens) and contar(cabeca + "\n" + "\n".join(atual + [linha])) > limite:
                    grupos.append((atual, atual_tr))
                    atual, atual_tr = list(rotulo_itens), []
                atual.append(linha)
                atual_tr += ltr
            grupos.append((atual, atual_tr))
        for parte, (linhas, trechos) in enumerate(grupos, 1):
            content = "\n".join(linhas)
            chunks.append({
                "chunk_id": f"{ficha['catalog_id']}:ficha:{assunto}" + (f":{parte}" if len(grupos) > 1 else ""),
                "catalog_id": ficha["catalog_id"],
                "tipo": "ficha",
                "assunto": assunto,
                "parte": parte,
                "partes": len(grupos),
                "content": content,
                "texto_embedding": cabeca + "\n" + normalizar_para_embedding(content),
                "tokens_estimados": contar(cabeca + "\n" + content),
                "trechos": list(dict.fromkeys(trechos)),
                "company": doc.get("company"),
                "title": doc.get("title"),
                "url": doc.get("url"),
                "incident_date": doc.get("incident_date"),
                "categoria_causa": ficha["incidente"].get("categoria_causa"),
                "dominio": ficha["triagem"].get("dominio"),
                "tipo_documento": ficha["triagem"].get("tipo"),
                "confianca": ficha.get("confianca"),
                "catalogo": doc.get("catalogo"),
                "problemas_texto": doc.get("problemas_texto", []),
            })
    return chunks


def main() -> None:
    limite = 400
    if "--limite" in sys.argv:
        limite = int(sys.argv[sys.argv.index("--limite") + 1])
    docs = [json.loads(l) for l in (PASTA / "corpus.jsonl").open(encoding="utf-8")]
    todos = []
    for doc in docs:
        ficha = json.loads((FICHAS / f"{doc['catalog_id']}.json").read_text(encoding="utf-8"))
        if not ficha.get("incidente"):
            continue
        todos += montar_chunks(ficha, doc, limite)
    with (PASTA / "chunks_fichas.jsonl").open("w", encoding="utf-8") as f:
        for c in todos:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    por_assunto: dict[str, list[int]] = {}
    for c in todos:
        por_assunto.setdefault(c["assunto"], []).append(c["tokens_estimados"])
    print(f"{len(todos)} chunks de {len(docs)} documentos (limite {limite}) -> "
          f"{(PASTA / 'chunks_fichas.jsonl').relative_to(ROOT)}")
    for a, v in por_assunto.items():
        v = sorted(v)
        print(f"  {a:10} {len(v):4} chunks  mediana {v[len(v)//2]:4}  p90 {v[int(.9*len(v))]:4}  max {v[-1]:4}")
    divididos = sorted({c["chunk_id"].rsplit(":", 1)[0] for c in todos if c["partes"] > 1})
    print(f"  divididos ({len(divididos)}): {', '.join(divididos)}")
    acima = [c["chunk_id"] for c in todos if c["tokens_estimados"] > limite]
    print(f"  acima do limite depois da divisão: {len(acima)} {acima}")


if __name__ == "__main__":
    main()
