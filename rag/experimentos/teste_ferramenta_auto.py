"""Teste: o GPT-OSS-20B no NIM chama ferramentas sozinho (tool_choice="auto")?

Pergunta que este teste responde antes da etapa dos agentes: se o modelo puder ESCOLHER entre
buscar, responder ou registrar, ele (1) chama a busca quando deve, (2) passa argumentos válidos,
(3) termina registrando a resposta com a ferramenta, e (4) cita só IDs que vieram das buscas?

Nos testes de 2026-11-09 o modelo só devolveu saída estruturada de forma confiável com a
ferramenta OBRIGATÓRIA. Aqui ele tem liberdade, como teria um agente.

Montagem (laço à mão no LangGraph, usando ChatNVIDIA do langchain-nvidia-ai-endpoints):

    START -> agente -(pediu ferramenta)-> ferramentas -(registrou)-> END
               ^                              |
               +------(buscou: volta)---------+
    agente -(respondeu em texto, sem ferramenta)-> END   (conta como falha)

Ferramentas oferecidas ao modelo:
    buscar_incidentes(consulta)   -> roda ingestion/banco/busca.py (5 incidentes, 2 trechos)
    registrar_resposta(...)       -> mesmo schema do pipeline da E3 (resposta, IDs, evidência)

Uso (precisa do Docker com o Postgres no ar e da NVIDIA_API_KEY no .env):
    multiagent_env/bin/python -I rag/experimentos/teste_ferramenta_auto.py
    multiagent_env/bin/python -I rag/experimentos/teste_ferramenta_auto.py --perguntas q07,q12
    multiagent_env/bin/python -I rag/experimentos/teste_ferramenta_auto.py --modelo openai/gpt-oss-120b

Cada chamada ao NIM gratuito leva ~2 min; com 4 perguntas e 2 a 3 chamadas cada, conte 20 a 30 min.
O resultado vai para rag/experimentos/resultados/tool_auto_<data>.json e .md.
"""
from __future__ import annotations

import argparse
import json
import operator
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Annotated, Literal

from dotenv import dotenv_values
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.types import RetryPolicy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rag"))
import grafo  # noqa: E402  (reaproveita busca() e normalizar())
import prompts  # noqa: E402

PADRAO = ["q07", "q08", "q10", "q12"]  # sintoma difícil x2, busca que falha, fora do corpus
MAX_BUSCAS = 3
ID_RE = re.compile(r"\bDAN-\d{3}\b")
SAIDA = ROOT / "rag" / "experimentos" / "resultados"

# --- ferramentas (schemas no formato OpenAI, como no llm.py) --------------------------------

FERRAMENTA_BUSCA = {
    "type": "function",
    "function": {
        "name": "buscar_incidentes",
        "description": ("Busca no histórico de postmortems os 5 incidentes mais parecidos com a consulta "
                        "e devolve o resumo e trechos de cada um, com o ID [DAN-123]. Pode ser chamada "
                        f"mais de uma vez com termos diferentes (no máximo {MAX_BUSCAS} vezes)."),
        "parameters": {
            "type": "object",
            "properties": {"consulta": {"type": "string",
                                        "description": "Texto da busca: sintomas, componentes, causa ou nome do serviço."}},
            "required": ["consulta"],
            "additionalProperties": False,
        },
    },
}
FERRAMENTA_REGISTRO = {
    "type": "function",
    "function": {"name": prompts.NOME_FERRAMENTA, "description": prompts.DESCRICAO_FERRAMENTA,
                 "parameters": prompts.SCHEMA_RESPOSTA},
}
NOMES = {"buscar_incidentes", prompts.NOME_FERRAMENTA}


def nome_corrigido(nome: str) -> str:
    """O GPT-OSS às vezes vaza o canal do formato harmony no nome da ferramenta:
    'registrar_resposta<|channel|>commentary', 'buscar_incidentescommentary'.
    Se o nome começa com o de uma ferramenta conhecida, usa esse nome."""
    if nome in NOMES:
        return nome
    for conhecido in sorted(NOMES, key=len, reverse=True):
        if nome.startswith(conhecido):
            return conhecido
    return nome


def corrigir_nomes(msg: AIMessage) -> int:
    """Corrige os nomes em msg.tool_calls e no tool_calls bruto (additional_kwargs), que é o que
    o ChatNVIDIA reenvia ao NIM no histórico. Devolve quantos nomes foram corrigidos."""
    n = 0
    for c in msg.tool_calls:
        novo = nome_corrigido(c["name"])
        if novo != c["name"]:
            c["name"], n = novo, n + 1
    for c in msg.additional_kwargs.get("tool_calls", []):
        f = c.get("function", {})
        if "name" in f:
            f["name"] = nome_corrigido(f["name"])
    return n

# Mesmas regras da v2, mas o contexto agora vem das buscas que o próprio modelo faz.
_regras = prompts.SISTEMA_V2.split("Regras:", 1)[1].split("Ao terminar", 1)[0].strip()
SISTEMA = f"""Você é um assistente de análise de incidentes de produção para times de SRE.
Você recebe uma pergunta e tem acesso a uma base histórica de postmortems públicos pela ferramenta \
buscar_incidentes. O CONTEXTO, nas regras abaixo, é o texto devolvido pelas suas buscas. Cada incidente \
tem um ID no formato [DAN-123].

Como trabalhar:
- Antes de responder, busque com buscar_incidentes. Se o resultado não trouxer o que a pergunta pede, \
pode buscar de novo com outros termos (no máximo {MAX_BUSCAS} buscas).
- Ao terminar, registre a resposta com a ferramenta {prompts.NOME_FERRAMENTA}. Não responda só em texto.

Regras:
{_regras}"""


class Estado(MessagesState):
    pergunta: str
    buscas: Annotated[list[dict], operator.add]       # {"consulta", "ids", "segundos"}
    chamadas_llm: Annotated[list[dict], operator.add]  # {"segundos", "tool_calls", "invalidas", "texto"}
    final: dict


def criar_grafo(modelo: str, chave: str, base_url: str, espera_inicial: float = 15.0, corrigir: bool = False):
    llm = ChatNVIDIA(model=modelo, api_key=chave, base_url=base_url, temperature=1.0,
                     max_completion_tokens=2048, timeout=300)
    llm_com_ferramentas = llm.bind_tools([FERRAMENTA_BUSCA, FERRAMENTA_REGISTRO], tool_choice="auto")

    def agente(estado: Estado) -> dict:
        t = time.time()
        msg = llm_com_ferramentas.invoke([SystemMessage(SISTEMA)] + estado["messages"])
        info = {"segundos": round(time.time() - t, 1),
                "tool_calls": [{"nome": c["name"], "args": c["args"]} for c in msg.tool_calls],
                "invalidas": [{"nome": c.get("name"), "args": c.get("args"), "erro": c.get("error")}
                              for c in msg.invalid_tool_calls],
                "texto": (msg.content or "")[:500] if isinstance(msg.content, str) else str(msg.content)[:500]}
        info["nomes_corrigidos"] = corrigir_nomes(msg) if corrigir else 0  # info guarda o nome original
        print(f"[agente] {info['segundos']}s · ferramentas: {[c['nome'] for c in info['tool_calls']] or 'nenhuma'}"
              + (f" · {len(info['invalidas'])} chamada(s) malformada(s)" if info["invalidas"] else "")
              + (f" · {info['nomes_corrigidos']} nome(s) corrigido(s)" if info["nomes_corrigidos"] else ""), flush=True)
        return {"messages": [msg], "chamadas_llm": [info]}

    def ferramentas(estado: Estado) -> dict:
        ultima: AIMessage = estado["messages"][-1]
        saidas, buscas, final = [], [], None
        feitas = len(estado.get("buscas", []))
        for c in ultima.tool_calls:
            if c["name"] == "buscar_incidentes":
                consulta = str(c["args"].get("consulta", "")).strip()
                if feitas + len(buscas) >= MAX_BUSCAS:
                    texto = f"Limite de {MAX_BUSCAS} buscas atingido. Registre a resposta com o que já encontrou."
                elif not consulta:
                    texto = "Consulta vazia. Informe o texto da busca."
                else:
                    t = time.time()
                    rec = grafo.busca().buscar(consulta, 5, 2)
                    ids = [prompts._id_curto(r["doc_id"]) for r in rec]
                    buscas.append({"consulta": consulta, "ids": ids, "segundos": round(time.time() - t, 1)})
                    print(f"[busca] {consulta!r} -> {ids}", flush=True)
                    texto = prompts.montar_contexto(rec)
                saidas.append(ToolMessage(texto, tool_call_id=c["id"]))
            elif c["name"] == prompts.NOME_FERRAMENTA:
                final = grafo.normalizar(c["args"])
                saidas.append(ToolMessage("Resposta registrada.", tool_call_id=c["id"]))
            else:
                saidas.append(ToolMessage(f"Ferramenta desconhecida: {c['name']}", tool_call_id=c["id"]))
        out = {"messages": saidas, "buscas": buscas}
        if final is not None:
            out["final"] = final
        return out

    def depois_do_agente(estado: Estado) -> Literal["ferramentas", "__end__"]:
        return "ferramentas" if estado["messages"][-1].tool_calls else END

    def depois_das_ferramentas(estado: Estado) -> Literal["agente", "__end__"]:
        return END if estado.get("final") else "agente"

    g = StateGraph(Estado)
    g.add_node("agente", agente, retry_policy=RetryPolicy(max_attempts=3, initial_interval=espera_inicial,
                                                          backoff_factor=2.0, jitter=True))
    g.add_node("ferramentas", ferramentas)
    g.add_edge(START, "agente")
    g.add_conditional_edges("agente", depois_do_agente, ["ferramentas", END])
    g.add_conditional_edges("ferramentas", depois_das_ferramentas, ["agente", END])
    return g.compile()


def avaliar(q: dict, estado: dict, erro: str | None, segundos: float) -> dict:
    buscas = estado.get("buscas", [])
    chamadas = estado.get("chamadas_llm", [])
    final = estado.get("final")
    recuperados = {i for b in buscas for i in b["ids"]}
    citados = sorted(set(final.get("incidentes_citados", [])) | set(ID_RE.findall(final.get("resposta", "")))) if final else []
    esperado = q.get("esperado", [])
    if final:
        termino = "registrou" + (" (com erro depois)" if erro else "")
    elif erro:
        termino = "erro"
    elif chamadas and not chamadas[-1]["tool_calls"]:
        termino = "texto_sem_ferramenta"
    else:
        termino = "parou_sem_registrar"
    return {
        "id": q["id"], "tipo": q.get("tipo"), "pergunta": q["pergunta"], "esperado": esperado,
        "termino": termino, "erro": erro, "segundos": round(segundos, 1),
        "chamou_busca": bool(buscas), "n_buscas": len(buscas), "consultas": [b["consulta"] for b in buscas],
        "chamadas_llm": len(chamadas),
        # JSON inválido (invalid_tool_calls) + nome de ferramenta que não existe (ex.: "registrar_resposta<|channel|>commentary")
        "chamadas_malformadas": sum(len(c["invalidas"]) + sum(t["nome"] not in NOMES for t in c["tool_calls"])
                                    for c in chamadas),
        "esperado_recuperado": any(e in recuperados for e in esperado) if esperado else None,
        "cita_esperado": any(e in citados for e in esperado) if esperado else None,
        "citados": citados, "fora_das_buscas": [c for c in citados if c not in recuperados],
        "evidencia": final.get("evidencia") if final else None,
        "resposta": final.get("resposta") if final else (chamadas[-1]["texto"] if chamadas else None),
        "detalhe": {"buscas": buscas, "chamadas_llm": chamadas},
    }


def relatorio_md(meta: dict, res: list[dict]) -> str:
    s = lambda b: "sim" if b else ("—" if b is None else "não")  # noqa: E731
    linhas = [f"# Teste tool_choice=auto — {meta['data']}", "",
              f"Modelo: `{meta['modelo']}` · máximo de {MAX_BUSCAS} buscas · temperatura 1,0 · "
              f"correção de nomes: {'sim' if meta.get('corrigir_nomes') else 'não'}", "",
              "| pergunta | término | buscas | chamadas ao LLM | malformadas | esperado recuperado | cita esperado | fora das buscas | evidência | tempo |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        linhas.append(f"| {r['id']} ({r['tipo']}) | {r['termino']} | {r['n_buscas']} | {r['chamadas_llm']} | {r['chamadas_malformadas']} | "
                      f"{s(r['esperado_recuperado'])} | {s(r['cita_esperado'])} | {', '.join(r['fora_das_buscas']) or '—'} | "
                      f"{r['evidencia'] or '—'} | {r['segundos']}s |")
    linhas += ["", "## Detalhe", ""]
    for r in res:
        linhas += [f"### {r['id']} — {r['termino']}", "", f"**Pergunta:** {r['pergunta']}", ""]
        for i, b in enumerate(r["detalhe"]["buscas"], 1):
            linhas.append(f"- busca {i}: `{b['consulta']}` → {', '.join(b['ids'])}")
        if r["erro"]:
            linhas.append(f"- erro: `{r['erro']}`")
        linhas += ["", f"**Resposta** (evidência: {r['evidencia'] or '—'}):", "", (r["resposta"] or "(vazia)"), ""]
    return "\n".join(linhas)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--perguntas", default=",".join(PADRAO), help="IDs separados por vírgula (padrão: %(default)s)")
    ap.add_argument("--modelo", default=None, help="padrão: LLM_MODEL do .env ou openai/gpt-oss-20b")
    ap.add_argument("--corrigir-nomes", action="store_true",
                    help="corrige nomes de ferramenta com o canal harmony vazado (ex.: registrar_resposta<|channel|>commentary)")
    a = ap.parse_args()

    env = dotenv_values(ROOT / ".env")
    chave = env.get("NVIDIA_API_KEY")
    if not chave:
        sys.exit(f"NVIDIA_API_KEY não encontrada em {ROOT / '.env'}")
    modelo = a.modelo or env.get("LLM_MODEL", "openai/gpt-oss-20b")
    base_url = env.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")

    todas = {q["id"]: q for q in json.loads((ROOT / "rag" / "avaliacao" / "perguntas.json").read_text())["perguntas"]}
    ids = [i.strip() for i in a.perguntas.split(",") if i.strip()]
    faltando = [i for i in ids if i not in todas]
    if faltando:
        sys.exit(f"perguntas inexistentes: {faltando}")

    g = criar_grafo(modelo, chave, base_url, corrigir=a.corrigir_nomes)
    resultados = []
    for i in ids:
        q = todas[i]
        print(f"\n=== {i} ({q.get('tipo')}): {q['pergunta']}", flush=True)
        estado, erro, t = {}, None, time.time()
        try:
            for parte in g.stream({"pergunta": q["pergunta"], "messages": [HumanMessage(q["pergunta"])]},
                                  stream_mode="values", config={"recursion_limit": 30}):
                estado = parte
        except Exception as e:  # registra e segue para a próxima pergunta
            erro = f"{type(e).__name__}: {str(e)[:300]}"
            print(f"[erro] {erro}", flush=True)
        r = avaliar(q, estado, erro, time.time() - t)
        resultados.append(r)
        print(f"--> término: {r['termino']} · buscas: {r['n_buscas']} · cita esperado: {r['cita_esperado']} · "
              f"fora das buscas: {r['fora_das_buscas'] or 'nenhum'}", flush=True)

    SAIDA.mkdir(parents=True, exist_ok=True)
    data = datetime.now().strftime("%Y-%m-%d_%H%M")
    meta = {"data": data, "modelo": modelo, "max_buscas": MAX_BUSCAS, "perguntas": ids,
            "corrigir_nomes": a.corrigir_nomes}
    (SAIDA / f"tool_auto_{data}.json").write_text(json.dumps({"meta": meta, "resultados": resultados},
                                                             ensure_ascii=False, indent=2))
    (SAIDA / f"tool_auto_{data}.md").write_text(relatorio_md(meta, resultados))
    print(f"\nresultado salvo em {SAIDA / f'tool_auto_{data}.md'}")


if __name__ == "__main__":
    main()
