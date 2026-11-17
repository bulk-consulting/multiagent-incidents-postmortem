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
MIN_CHARS_TRECHO = 200     # trechos menores que isso quase sempre são só um título ("Further details here.")
CHARS_TRECHO_PARA_LLM = 700
# consulta fixa somada à do LLM em todo search_inside_incidents: se a do LLM sair genérica,
# esta ainda traz os trechos de causa e correção (teste de 2026-11-16: ajudou em 5 de 11 perguntas)
CONSULTA_CAUSA = "what was the root cause and how was the problem fixed"


class BuscaNoIncidente(BaseModel):
    incident_id: str = Field(description="ID de um incidente já encontrado, ex.: DAN-017")
    query: str = Field(description="consulta curta em inglês, em palavras-chave, sobre a causa e a correção desse incidente")


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
    Use para os incidentes que se parecem de fato com o incidente atual (até 3 numa chamada)."""
    conhecidos = _ids_conhecidos(state)
    resultados, registro, linhas, avisos = {}, [], [], []
    textos_por_id: dict[str, set] = {}  # o LLM às vezes pede 2 buscas no mesmo incidente: não repetir trechos
    for s in searches[:MAX_INCIDENTES_POR_CHAMADA]:
        i = _id_curto(s.incident_id.strip().upper())
        if i not in conhecidos:
            avisos.append(f"{i} não está entre os incidentes encontrados; ignorado.")
            continue
        trechos, textos = resultados.setdefault(i, []), textos_por_id.setdefault(i, set())
        n_antes = len(trechos)
        for consulta, fonte in ((s.query.strip(), "llm"), (CONSULTA_CAUSA, "fixa")):
            if not consulta:
                continue
            for d in busca.buscar_no_incidente(i, consulta, N_TRECHOS + 1):
                if d["content"] in textos or len(d["content"]) < MIN_CHARS_TRECHO:
                    continue
                textos.add(d["content"])
                d.update({"origem": "aprofundamento", "consulta": consulta, "fonte_consulta": fonte})
                trechos.append(d)
                if sum(t["consulta"] == consulta for t in trechos[n_antes:]) >= N_TRECHOS:
                    break
            registro.append({"etapa": "search_inside_incidents", "consulta": consulta,
                             "filtro": {"incidente": i}, "ids": [i]})
        linhas.append(f"### [{i}] consulta: {s.query.strip()}")
        linhas += [f"Trecho ({d['secao'] or 'sem seção'}): {d['content'][:CHARS_TRECHO_PARA_LLM]}" for d in trechos[n_antes:]]
    if len(searches) > MAX_INCIDENTES_POR_CHAMADA:
        avisos.append(f"Só os {MAX_INCIDENTES_POR_CHAMADA} primeiros incidentes foram buscados.")
    texto = "\n\n".join(linhas) or "Nenhum trecho encontrado."
    if avisos:
        texto += "\n\nAvisos: " + " ".join(avisos)
    return texto, {"resultados": resultados, "buscas": registro, "avisos": avisos}


@tool(response_format="content_and_artifact")
def find_similar_incidents(queries: list[str], state: Annotated[dict, InjectedState]) -> tuple[str, dict]:
    """Procura OUTROS incidentes parecidos com o atual, com consultas novas (até 2, curtas, em inglês).
    Os incidentes já vistos ficam de fora. Use quando nenhum dos encontrados se parece com o atual,
    ou quando o pedido do diagnóstico pede outro tipo de incidente."""
    excluir = sorted(_ids_conhecidos(state))
    por_id, registro = {}, []
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
    incidentes = sorted(por_id.values(), key=lambda r: -r["similaridade"])[:N_DOCS]
    linhas = [f"### [{r['doc_id']}] {r['company']} — {r['title']}\nResumo: {r.get('resumo') or '(sem resumo)'}"
              for r in incidentes]
    texto = ("\n\n".join(linhas) + "\n\nPara ver causa e correção de algum deles, use search_inside_incidents."
             if linhas else "Nenhum incidente novo encontrado.")
    return texto, {"incidentes": incidentes, "buscas": registro}


FERRAMENTAS = [search_inside_incidents, find_similar_incidents]
NOMES = {f.name for f in FERRAMENTAS}
