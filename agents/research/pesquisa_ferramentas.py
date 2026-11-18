"""
Ferramentas (tools) do Agente Pesquisa RAG: o LLM decide quando e como chamá-las.

    search_inside_incidents  busca causa e correção DENTRO de incidentes já encontrados
    find_similar_incidents   procura OUTROS incidentes parecidos com o atual

Os nomes ficam em inglês e começam de forma diferente (search_ / find_) para o modelo não confundir
uma com a outra e para a correção do nome vazado pelo formato harmony funcionar por prefixo.

Cada ferramenta devolve duas coisas (response_format="content_and_artifact"):
    content   texto curto que volta para o LLM como ToolMessage
    artifact  os dados completos (trechos, similaridade, consultas feitas), que o nó montar_achados
              usa para montar a saída do agente; o LLM não precisa ler tudo isso
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Annotated

from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rag"))
import busca  # noqa: E402
from prompts import _id_curto  # noqa: E402

MAX_INCIDENTES_POR_CHAMADA = 3
MAX_CONSULTAS_POR_CHAMADA = 2
N_TRECHOS = 2              # trechos por consulta dentro de um incidente
N_DOCS = 5                 # incidentes por consulta em find_similar_incidents
INCLUIR_DESCRICAO_NA_1A_BUSCA = False  # modo híbrido (experimento): ver find_similar_incidents
EXTRAS_LLM = 5             # no modo híbrido, incidentes novos das consultas do LLM somados aos da descrição
MIN_CHARS_TRECHO = 200     # trechos menores que isso quase sempre são só um título ("Further details here.")
CHARS_TRECHO_PARA_LLM = 700
# Consultas fixas somadas à do LLM em todo aprofundamento (o LLM às vezes escreve uma consulta genérica).
# Eram uma só ("what was the root cause and how was the problem fixed"); a conferência de 2026-11-17
# mostrou que ela puxava a narrativa e a causa, e a seção de correção ficava entre o 4º e o 12º lugar.
CONSULTA_CAUSA = "what was the root cause of the failure"
CONSULTA_CORRECAO = "how the problem was corrected, remediation, action items, prevention, next steps"
N_CAUSA = 1                # trechos da consulta fixa de causa (a do LLM costuma cobrir a causa)
N_CORRECAO = 2             # trechos de correção
# títulos de seção (ou rótulos em maiúsculas) que indicam correção ou prevenção: esses trechos têm preferência
TITULO_CORRECAO = re.compile(r"fix|correct|remediat|prevent|action item|next step|lesson|moving forward|going forward"
                             r"|improv|follow[- ]?up|what we.{0,10}(doing|changing)|resolution|resolved|mitigat"
                             r"|changes|recover", re.I)
ROTULO_CORRECAO = re.compile(r"\b(REMEDIATION|PREVENTION|RESOLUTION|ACTION ITEMS|NEXT STEPS|CORRECTIVE)\b")


class BuscaNoIncidente(BaseModel):
    incident_id: str = Field(description="ID de um incidente já encontrado, ex.: DAN-017")
    query: str = Field(description="consulta curta em inglês, em palavras-chave, sobre a causa e a correção desse incidente")
    why: str = Field(description="uma frase curta, em português, dizendo por que escolheu este incidente: "
                                 "o que bate com o incidente atual e o que não bate")


def _eh_correcao(d: dict) -> bool:
    return bool(TITULO_CORRECAO.search(d.get("secao") or "")) or bool(ROTULO_CORRECAO.search(d["content"]))


def trechos_do_incidente(i: str, consulta_llm: str | None, textos: set[str]) -> tuple[list[dict], list[dict]]:
    """Os trechos de um incidente para o Diagnóstico: até 2 pela consulta do LLM, 1 pela consulta fixa de causa
    e 2 de correção. Para a correção, os trechos cujo título de seção indica correção ("How was the problem
    corrected", "Remediation", "Action Items"…) vêm antes dos demais. `textos` evita repetir trechos.
    Devolve (trechos, registro das buscas)."""
    trechos, registro = [], []

    def aceitar(d: dict, consulta: str, fonte: str) -> bool:
        # os chunks da ingestão se sobrepõem: dois trechos podem começar igual (o mesmo bloco duas vezes)
        inicio = "inicio:" + d["content"][:300]
        if d["content"] in textos or inicio in textos or len(d["content"]) < MIN_CHARS_TRECHO:
            return False
        textos.update({d["content"], inicio})
        d.update({"origem": "aprofundamento", "consulta": consulta, "fonte_consulta": fonte})
        trechos.append(d)
        return True

    for consulta, fonte, n in ((consulta_llm, "llm", N_TRECHOS), (CONSULTA_CAUSA, "causa", N_CAUSA)):
        if not consulta:
            continue
        k = 0
        for d in busca.buscar_no_incidente(i, consulta, n + 3):
            if k < n and aceitar(d, consulta, fonte):
                k += 1
        registro.append({"etapa": "search_inside_incidents", "consulta": consulta, "filtro": {"incidente": i}, "ids": [i]})
    todos = busca.buscar_no_incidente(i, CONSULTA_CORRECAO, 40)  # o incidente inteiro, ordenado pela consulta
    k = 0
    for d in sorted(todos, key=lambda d: not _eh_correcao(d)):  # sorted é estável: mantém a ordem de similaridade
        if k < N_CORRECAO and aceitar(d, CONSULTA_CORRECAO, "correcao"):
            k += 1
    registro.append({"etapa": "search_inside_incidents", "consulta": CONSULTA_CORRECAO, "filtro": {"incidente": i}, "ids": [i]})
    return trechos, registro


def _ids_conhecidos(estado: dict) -> set[str]:
    """Incidentes que o agente já viu: candidatos, vistos em rodadas anteriores e achados por find_similar_incidents."""
    ids = {r["doc_id"] for r in estado.get("candidatos", [])} | set(estado.get("ids_vistos", []))
    for m in estado.get("messages", []):
        if isinstance(m, ToolMessage) and m.name == "find_similar_incidents" and m.artifact:
            ids |= {r["doc_id"] for r in m.artifact.get("incidentes", [])}
    return ids


@tool(response_format="content_and_artifact")
def search_inside_incidents(searches: list[BuscaNoIncidente],
                            state: Annotated[dict, InjectedState]) -> tuple[str, dict]:
    """Busca, DENTRO de incidentes já encontrados, os trechos que explicam a causa raiz e a correção.
    Use para os incidentes que se parecem de fato com o incidente atual (até 3 numa chamada), dizendo
    para cada um por que o escolheu (why)."""
    conhecidos = _ids_conhecidos(state)
    resultados, registro, linhas, avisos = {}, [], [], []
    justificativas: dict[str, str] = {}
    textos_por_id: dict[str, set] = {}  # o LLM às vezes pede 2 buscas no mesmo incidente: não repetir trechos
    for s in searches[:MAX_INCIDENTES_POR_CHAMADA]:
        i = _id_curto(s.incident_id.strip().upper())
        if i not in conhecidos:
            avisos.append(f"{i} não está entre os incidentes encontrados; ignorado.")
            continue
        justificativas[i] = s.why.strip()
        novos, reg = trechos_do_incidente(i, s.query.strip(), textos_por_id.setdefault(i, set()))
        resultados.setdefault(i, []).extend(novos)
        registro += reg
        linhas.append(f"### [{i}] consulta: {s.query.strip()}")
        linhas += [f"Trecho ({d['secao'] or 'sem seção'}): {d['content'][:CHARS_TRECHO_PARA_LLM]}" for d in novos]
    if len(searches) > MAX_INCIDENTES_POR_CHAMADA:
        avisos.append(f"Só os {MAX_INCIDENTES_POR_CHAMADA} primeiros incidentes foram buscados.")
    texto = "\n\n".join(linhas) or "Nenhum trecho encontrado."
    if avisos:
        texto += "\n\nAvisos: " + " ".join(avisos)
    return texto, {"resultados": resultados, "justificativas": justificativas, "buscas": registro, "avisos": avisos}


@tool(response_format="content_and_artifact")
def find_similar_incidents(queries: list[str], state: Annotated[dict, InjectedState]) -> tuple[str, dict]:
    """Procura OUTROS incidentes parecidos com o atual, com consultas novas (até 2, curtas, em inglês).
    Os incidentes já vistos ficam de fora. Use quando nenhum dos encontrados se parece com o atual,
    ou quando o pedido do diagnóstico pede outro tipo de incidente."""
    excluir = sorted(_ids_conhecidos(state))
    por_id, registro = {}, []
    garantidos: list[dict] = []
    primeira = not any(isinstance(m, ToolMessage) and m.name == "find_similar_incidents" for m in state.get("messages", []))
    if INCLUIR_DESCRICAO_NA_1A_BUSCA and primeira and state.get("descricao"):
        # Modo híbrido: a 1ª busca do LLM inclui também a descrição original (feita em código). Os
        # N_DOCS incidentes dela entram sempre; as consultas do LLM acrescentam até EXTRAS_LLM novos.
        garantidos = busca.buscar(state["descricao"], N_DOCS, N_TRECHOS, excluir=excluir)
        for r in garantidos:
            r["doc_id"] = _id_curto(r["doc_id"])
            for d in r.get("detalhes", []):
                d.update({"origem": "similar", "consulta": state["descricao"]})
        registro.append({"etapa": "find_similar_incidents (descrição)", "consulta": state["descricao"],
                         "filtro": {"excluir": excluir}, "ids": [r["doc_id"] for r in garantidos]})
    for consulta in [q.strip() for q in queries if q.strip()][:MAX_CONSULTAS_POR_CHAMADA]:
        res = busca.buscar(consulta, N_DOCS, N_TRECHOS, excluir=excluir)
        for r in res:
            r["doc_id"] = _id_curto(r["doc_id"])
            for d in r.get("detalhes", []):
                d.update({"origem": "similar", "consulta": consulta})
            if r["doc_id"] not in por_id or r["similaridade"] > por_id[r["doc_id"]]["similaridade"]:
                por_id[r["doc_id"]] = r
        registro.append({"etapa": "find_similar_incidents", "consulta": consulta,
                         "filtro": {"excluir": excluir}, "ids": [r["doc_id"] for r in res]})
    if garantidos:
        ids_g = {r["doc_id"] for r in garantidos}
        extras = [r for r in sorted(por_id.values(), key=lambda r: -r["similaridade"]) if r["doc_id"] not in ids_g]
        incidentes = garantidos + extras[:EXTRAS_LLM]
    else:
        incidentes = sorted(por_id.values(), key=lambda r: -r["similaridade"])[:N_DOCS]
    linhas = [f"### [{r['doc_id']}] {r['company']} — {r['title']}\nResumo: {r.get('resumo') or '(sem resumo)'}"
              for r in incidentes]
    texto = ("\n\n".join(linhas) + "\n\nPara ver causa e correção de algum deles, use search_inside_incidents."
             if linhas else "Nenhum incidente novo encontrado.")
    return texto, {"incidentes": incidentes, "buscas": registro}


FERRAMENTAS = [search_inside_incidents, find_similar_incidents]
NOMES = {f.name for f in FERRAMENTAS}
