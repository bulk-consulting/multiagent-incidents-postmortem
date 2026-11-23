"""
Agente Pesquisa RAG: encontra evidência histórica para o Agente Diagnóstico.

    1ª volta:     START → busca_inicial → agente ⇄ ferramentas → montar_achados → END
    refinamento:  START → agente ⇄ ferramentas → montar_achados → END
                  (entra com os achados anteriores e o pedido do Diagnóstico)

    busca_inicial   código: busca com a descrição e com cada sintoma; junta por incidente (top 5)
    agente          LLM (GPT-OSS-20B no NIM, via ChatNVIDIA) com tool_choice="auto": lê os incidentes
                    e decide se chama search_inside_incidents, find_similar_incidents ou nenhuma
    ferramentas     ToolNode do LangGraph: executa as ferramentas pedidas (pesquisa_ferramentas.py)
    montar_achados  código: incidentes + trechos (similar / aprofundamento) + registro das buscas

Volta ao agente depois das ferramentas só se ele chamou find_similar_incidents (há incidentes novos
para olhar) e ainda há chamadas disponíveis (MAX_CHAMADAS_LLM). Depois de search_inside_incidents, o
trabalho da rodada está feito e o fluxo segue para montar_achados, sem gastar outra chamada (~2,5 min).

O agente não avalia se a evidência basta: isso é do Agente Diagnóstico. O contador de tentativas do
loop de refinamento fica no roteamento do grafo principal.

Uso (a partir da raiz do repositório, com o banco no ar):
    multiagent_env/bin/python -I agents/research/pesquisa.py "descrição do incidente" [--sintoma "..."]...
        [--sem-llm] [--json saida.json] [--modelo nvidia/nemotron-3.5-super-vl-120b-a12b]
    # refinamento: parte dos achados de uma rodada anterior e de um pedido do Diagnóstico
    multiagent_env/bin/python -I agents/research/pesquisa.py "descrição" --anteriores saida.json --pedido "..."
"""
from __future__ import annotations

import argparse
import json
import operator
import sys
import time
from pathlib import Path
from typing import Annotated, Literal, TypedDict

from dotenv import dotenv_values
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage, ToolMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langgraph.types import RetryPolicy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rag"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import busca  # noqa: E402
import limite_llm  # noqa: E402
import pesquisa_ferramentas as pf  # noqa: E402
import pesquisa_prompt as pp  # noqa: E402
from prompts import _id_curto  # noqa: E402

N_DOCS = 10                # candidatos da busca inicial (o LLM vê título e resumo de cada um)
MAX_ACHADOS = 8            # incidentes na saída: os aprofundados primeiro, depois os mais parecidos
MIN_CHARS_RESUMO = 100     # resumo mais curto que isso vai acompanhado do início do trecho mais parecido
N_TRECHOS_SIMILAR = 2      # trechos parecidos com a descrição, por incidente
MAX_TRECHOS = 7            # teto de trechos por incidente nos achados (até 5 do aprofundamento + 2 da busca inicial)
MAX_CHAMADAS_LLM = 2       # por execução do agente
# Modo agêntico (um dos três modos; ver ativar_modo_agentico): sem busca inicial em código; o LLM escreve as próprias
# consultas com find_similar_incidents desde a 1ª chamada. Ligado por --agentico.
MODO_AGENTICO = False
MAX_CHAMADAS_AGENTICO = 4
N_DOCS_FIND_AGENTICO = 10  # incidentes que find_similar_incidents devolve no modo agêntico (como os 10 candidatos)


class EstadoPesquisa(TypedDict, total=False):
    # entrada
    descricao: str
    sintomas: list[str]
    pedido_busca: str                                 # do Diagnóstico; vazio na 1ª volta
    candidatos: list[dict]                            # incidentes encontrados (no refinamento: achados anteriores)
    ids_vistos: list[str]
    sem_llm: bool                                     # testes: chamada fixa, sem o NIM
    # produzido pelo agente
    messages: Annotated[list[AnyMessage], add_messages]
    achados: list[dict]
    aprofundados: dict                                # doc_id -> trechos de search_inside_incidents
    novos: list[dict]                                 # incidentes de find_similar_incidents
    plano: dict                                       # resumo das decisões (para relatórios)
    buscas: Annotated[list[dict], operator.add]       # registro de cada busca (rastreabilidade)
    chamadas_llm: Annotated[list[dict], operator.add]
    tempos: Annotated[dict, operator.or_]


# ---------------------------------------------------------------- busca inicial (código)

def _marcar(incidentes: list[dict], consulta: str) -> list[dict]:
    for r in incidentes:
        r["doc_id"] = _id_curto(r["doc_id"])
        for d in r.get("detalhes", []):
            d.setdefault("origem", "similar")
            d.setdefault("consulta", consulta)
    return incidentes


def _juntar(listas: list[list[dict]]) -> list[dict]:
    """Um registro por incidente, com a maior similaridade e os trechos de todas as buscas (sem repetir)."""
    por_id: dict[str, dict] = {}
    for lista in listas:
        for r in lista:
            atual = por_id.get(r["doc_id"])
            if atual is None:
                por_id[r["doc_id"]] = {**r, "detalhes": list(r.get("detalhes", []))}
                continue
            textos = {d["content"] for d in atual["detalhes"]}
            atual["detalhes"] += [d for d in r.get("detalhes", []) if d["content"] not in textos]
            if r["similaridade"] > atual["similaridade"]:
                atual.update({k: v for k, v in r.items() if k != "detalhes"})
    return sorted(por_id.values(), key=lambda r: -r["similaridade"])


def busca_inicial(estado: EstadoPesquisa) -> dict:
    t = time.time()
    listas, registro = [], []
    for c in [estado["descricao"], *estado.get("sintomas", [])]:
        res = _marcar(busca.buscar(c, N_DOCS, N_TRECHOS_SIMILAR), c)
        listas.append(res)
        registro.append({"etapa": "busca_inicial", "consulta": c, "filtro": None, "ids": [r["doc_id"] for r in res]})
    return {"candidatos": _juntar(listas)[:N_DOCS], "buscas": registro,
            "tempos": {"busca_inicial": round(time.time() - t, 1)}}


# ---------------------------------------------------------------- agente (LLM com ferramentas)

_llm = None
RACIOCINIO = True  # False: enable_thinking=False (o modelo responde sem raciocínio interno; menos tokens)
MODELO_FORCADO: str | None = None  # testes: troca o modelo do .env só nesta execução (avaliar_pesquisa.py --modelo)


def llm_com_ferramentas():
    """ChatNVIDIA com as duas ferramentas e tool_choice="auto" (o modelo decide se e qual chamar)."""
    global _llm
    if _llm is None:
        from langchain_nvidia_ai_endpoints import ChatNVIDIA
        env = dotenv_values(ROOT / ".env")
        modelo = ChatNVIDIA(model=MODELO_FORCADO or env.get("LLM_MODEL", "nvidia/nemotron-3.5-super-vl-120b-a12b"), api_key=env["NVIDIA_API_KEY"],
                            base_url=env.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1"),
                            temperature=1.0, max_completion_tokens=4096,  # modelos com raciocínio gastam tokens antes da resposta
                            timeout=300)  # o polling do ChatNVIDIA desiste em 60 s por padrão; o NIM leva ~2,5 min
        _llm = modelo.bind_tools(pf.FERRAMENTAS, tool_choice="auto")
    return _llm


def nome_corrigido(nome: str) -> str:
    """O GPT-OSS às vezes vaza o canal do formato harmony no nome da ferramenta
    ('search_inside_incidents<|channel|>commentary'). Se o nome começa com o de uma ferramenta, usa esse."""
    if nome in pf.NOMES:
        return nome
    for conhecido in sorted(pf.NOMES, key=len, reverse=True):
        if nome.startswith(conhecido):
            return conhecido
    return nome


def corrigir_nomes(msg: AIMessage) -> int:
    """Corrige msg.tool_calls e o tool_calls bruto (additional_kwargs), que o ChatNVIDIA reenvia ao NIM."""
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


def _fechar_json(texto: str) -> dict | None:
    """O GPT-OSS às vezes esquece de fechar o JSON dos argumentos (visto em 2026-11-17:
    '{"searches":[{...},{...}]' sem o '}' final). Completa as chaves e colchetes que faltam."""
    pilha, em_string, escape = [], False, False
    for ch in texto:
        if em_string:
            escape = (ch == "\\") and not escape
            if ch == '"' and not escape:
                em_string = False
            continue
        if ch == '"':
            em_string = True
        elif ch in "{[":
            pilha.append("}" if ch == "{" else "]")
        elif ch in "}]" and pilha:
            pilha.pop()
    if em_string:
        return None
    try:
        dados = json.loads(texto + "".join(reversed(pilha)))
    except json.JSONDecodeError:
        return None
    return dados if isinstance(dados, dict) else None


def consertar_malformadas(msg: AIMessage) -> int:
    """Transforma em chamada válida cada invalid_tool_call cujo JSON só estava sem fechar.
    Atualiza também o tool_calls bruto (additional_kwargs), que o ChatNVIDIA reenvia ao NIM."""
    consertadas, restantes = [], []
    for c in msg.invalid_tool_calls:
        args = _fechar_json(str(c.get("args") or ""))
        nome = nome_corrigido(str(c.get("name") or ""))
        if args is not None and nome in pf.NOMES:
            consertadas.append({"name": nome, "args": args, "id": c.get("id"), "type": "tool_call"})
        else:
            restantes.append(c)
    if consertadas:
        msg.tool_calls = list(msg.tool_calls) + consertadas
        msg.invalid_tool_calls = restantes
        brutos = {c.get("id"): c for c in msg.additional_kwargs.get("tool_calls", [])}
        for c in consertadas:
            if c["id"] in brutos:
                brutos[c["id"]].setdefault("function", {}).update({"name": c["name"], "arguments": json.dumps(c["args"])})
    return len(consertadas)


def montar_lista_resumos(candidatos: list[dict]) -> str:
    """O que o LLM lê para decidir: ID, empresa, título e resumo de cada candidato (os resumos do catálogo
    do danluu têm mediana de ~250 caracteres e costumam dizer o que aconteceu e por quê). Os trechos não
    vão: os detalhes de causa e correção chegam por search_inside_incidents. Assim cabem mais candidatos
    com menos texto (10 resumos ≈ 2.500 caracteres; 5 incidentes com trechos ≈ 15.000)."""
    blocos = []
    for k, r in enumerate(candidatos, 1):
        resumo = (r.get("resumo") or "").strip()
        linhas = [f"### {k}. [{r['doc_id']}] {r['company']} — {r['title']}", f"Resumo: {resumo or '(sem resumo)'}"]
        if len(resumo) < MIN_CHARS_RESUMO:
            m = r.get("melhor_chunk") or {}
            if m.get("tipo") == "resumo" or not m.get("content"):  # o melhor trecho era o próprio resumo
                m = (r.get("detalhes") or [{}])[0]
            if m.get("content"):
                linhas.append(f"Trecho mais parecido: {m['content'][:300]}")
        blocos.append("\n".join(linhas))
    return "\n\n".join(blocos) if blocos else "(nenhum incidente encontrado)"


def completar_argumentos(msg: AIMessage) -> int:
    """Arruma argumentos fora do formato antes de a ferramenta validar: lista mandada como texto (JSON dentro de
    uma string) vira lista, e o campo why esquecido em search_inside_incidents é preenchido com
    um valor neutro para a ferramenta rodar mesmo assim, em vez de falhar na validação. Devolve quantos campos
    foram preenchidos (fica registrado: é sinal de que o modelo não seguiu o formato)."""
    n = 0
    for c in msg.tool_calls:
        # Lista mandada como texto com um JSON dentro (visto com o Nemotron 3.5 em 2026-11-18:
        # {"searches": "[{\"incident_id\": ...}]"}): converte para lista antes de a ferramenta validar.
        for campo in ("searches", "queries"):
            valor = c["args"].get(campo)
            if isinstance(valor, str) and valor.strip().startswith("["):
                try:
                    convertido = json.loads(valor)
                except json.JSONDecodeError:
                    convertido = (_fechar_json('{"x": ' + valor) or {}).get("x")
                if isinstance(convertido, list):
                    c["args"][campo], n = convertido, n + 1
        if c["name"] != "search_inside_incidents":
            continue
        for item in c["args"].get("searches") or []:
            if isinstance(item, dict) and not isinstance(item.get("why"), str):
                item["why"], n = "", n + 1
    if n:
        brutos = {b.get("id"): b for b in msg.additional_kwargs.get("tool_calls", [])}
        for c in msg.tool_calls:
            if c["id"] in brutos:
                brutos[c["id"]].setdefault("function", {})["arguments"] = json.dumps(c["args"])
    return n


def _chamada_fixa(estado: EstadoPesquisa) -> AIMessage:
    """Modo --sem-llm: aprofunda os 3 primeiros candidatos só com as consultas fixas de causa e de correção."""
    buscas = [{"incident_id": r["doc_id"], "query": "", "why": ""}
              for r in estado.get("candidatos", [])[:pf.MAX_INCIDENTES_POR_CHAMADA]]
    return AIMessage("", tool_calls=[{"name": "search_inside_incidents",
                                      "args": {"searches": buscas},
                                      "id": "sem-llm-1", "type": "tool_call"}])


def agente(estado: EstadoPesquisa) -> dict:
    novas = []
    agentico = MODO_AGENTICO and not estado.get("candidatos")
    if not estado.get("messages") and agentico:  # 1ª chamada, modo agêntico: sem incidentes; o LLM procura
        novas.append(HumanMessage(pp.mensagem_usuario_agentico(estado["descricao"], estado.get("sintomas", []),
                                                               estado.get("pedido_busca", ""))))
    elif not estado.get("messages"):  # 1ª chamada: monta a mensagem com os incidentes encontrados
        contexto = montar_lista_resumos(estado.get("candidatos", []))
        novas.append(HumanMessage(pp.mensagem_usuario(estado["descricao"], estado.get("sintomas", []),
                                                      contexto, estado.get("pedido_busca", ""))))
    if estado.get("sem_llm"):
        msg = _chamada_fixa(estado) if not estado.get("messages") else AIMessage("modo --sem-llm: fim.")
        return {"messages": novas + [msg]}
    sistema = pp.SISTEMA_AGENTICO if MODO_AGENTICO else pp.SISTEMA
    historico = [SystemMessage(sistema)] + list(estado.get("messages", [])) + novas
    infos, n = [], len(estado.get("chamadas_llm", []))
    for tentativa in range(2):  # 2ª só se a chamada vier malformada ou vazia
        msg, info = _chamar_llm(historico)
        n += 1
        infos.append(info)
        vazia = not msg.tool_calls and not msg.invalid_tool_calls and not str(msg.content or "").strip()
        if tentativa == 1 or msg.tool_calls or not (msg.invalid_tool_calls or vazia):
            break
        if vazia:
            # Resposta sem texto e sem ferramenta (visto com o Nemotron 3.5: o raciocínio gasta o limite de tokens
            # antes da resposta). Pede de novo uma vez, sem mudar o histórico.
            print("[agente] resposta vazia; pedindo de novo", flush=True)
            continue
        # Chamada malformada (JSON inválido nos argumentos): a mensagem ruim não entra no histórico
        # (o NIM recusaria um tool_call sem resposta); o modelo recebe o erro e tenta de novo.
        erro = "; ".join(str(c.get("error") or "argumentos inválidos")[:200] for c in msg.invalid_tool_calls)
        print(f"[agente] chamada de ferramenta malformada ({erro}); pedindo de novo", flush=True)
        aviso = HumanMessage(f"Sua chamada de ferramenta veio malformada ({erro}). Chame a ferramenta de novo, "
                             "com os argumentos em JSON válido, seguindo o formato da ferramenta.")
        novas.append(aviso)
        historico.append(aviso)
    return {"messages": novas + [msg], "chamadas_llm": infos,
            "tempos": {f"agente_{len(estado.get('chamadas_llm', [])) + 1}": round(sum(i["segundos"] for i in infos), 1)}}


def _chamar_llm(historico: list) -> tuple[AIMessage, dict]:
    t = time.time()
    try:
        extra = {} if RACIOCINIO else {"chat_template_kwargs": {"enable_thinking": False}}
        msg = limite_llm.chamar(lambda: llm_com_ferramentas().invoke(historico, **extra), aviso="agente")
    except Exception as e:
        print(f"[agente] falha ({type(e).__name__}: {str(e)[:120]}); o grafo vai tentar de novo", flush=True)
        raise
    info = {"segundos": round(time.time() - t, 1),
            "tool_calls": [{"nome": c["name"], "args": c["args"]} for c in msg.tool_calls],  # nome como veio
            "invalidas": [{"nome": c.get("name"), "args": str(c.get("args"))[:500], "erro": str(c.get("error"))[:300]}
                          for c in msg.invalid_tool_calls],
            "texto": msg.content if isinstance(msg.content, str) else str(msg.content),
            "uso": dict(msg.usage_metadata or {})}
    info["nomes_corrigidos"] = corrigir_nomes(msg)
    info["json_consertados"] = consertar_malformadas(msg)
    if info["json_consertados"]:  # registra também as chamadas que passaram a valer depois do conserto
        info["tool_calls"] += [{"nome": c["name"], "args": c["args"]} for c in msg.tool_calls[-info["json_consertados"]:]]
    info["campos_completados"] = completar_argumentos(msg)
    return msg, info


def _tentar_de_novo(e: Exception) -> bool:
    # erros de programação não valem nova tentativa; o resto (timeout, 429, 5xx do NIM) vale
    return not isinstance(e, (ValueError, TypeError, KeyError, AttributeError, NameError))


# ---------------------------------------------------------------- roteamento

def ativar_modo_agentico() -> None:
    """Liga o modo agêntico (experimento): sem busca inicial em código, até 4 chamadas ao LLM e
    find_similar_incidents devolvendo 10 incidentes."""
    global MODO_AGENTICO
    MODO_AGENTICO = True
    pf.N_DOCS = N_DOCS_FIND_AGENTICO


def ativar_modo_hibrido() -> None:
    """Modo agêntico + rede de segurança: a 1ª busca do LLM inclui também a descrição original (feita em
    código); os 10 incidentes dela entram sempre e as consultas do LLM acrescentam até 5 novos."""
    ativar_modo_agentico()
    pf.INCLUIR_DESCRICAO_NA_1A_BUSCA = True
    pp.SISTEMA_AGENTICO = pp.SISTEMA_AGENTICO + pp.AVISO_HIBRIDO


def rota_entrada(estado: EstadoPesquisa) -> Literal["busca_inicial", "agente"]:
    return "agente" if estado.get("candidatos") or MODO_AGENTICO else "busca_inicial"


def depois_do_agente(estado: EstadoPesquisa) -> Literal["ferramentas", "montar_achados"]:
    ultima = estado["messages"][-1]
    return "ferramentas" if isinstance(ultima, AIMessage) and ultima.tool_calls else "montar_achados"


def depois_das_ferramentas(estado: EstadoPesquisa) -> Literal["agente", "montar_achados"]:
    rodada = []
    for m in reversed(estado["messages"]):
        if not isinstance(m, ToolMessage):
            break
        rodada.append(m.name)
    chamadas = len(estado.get("chamadas_llm", []))
    limite = MAX_CHAMADAS_AGENTICO if MODO_AGENTICO else MAX_CHAMADAS_LLM
    if "find_similar_incidents" in rodada and chamadas < limite and not estado.get("sem_llm"):
        return "agente"
    return "montar_achados"


# ---------------------------------------------------------------- saída (código)

def montar_achados(estado: EstadoPesquisa) -> dict:
    aprofundados, novos, justificativas, buscas, avisos = {}, [], {}, [], []
    plano = {"aprofundar": [], "novas_consultas": [], "descartar": [], "justificativa": "", "avisos": avisos}
    for m in estado.get("messages", []):
        if isinstance(m, AIMessage):
            for c in m.tool_calls:
                if c["name"] == "search_inside_incidents":
                    plano["aprofundar"] += [{"id": _id_curto(str(s.get("incident_id", ""))), "consulta": s.get("query", ""),
                                             "why": s.get("why")}
                                            for s in c["args"].get("searches", []) if isinstance(s, dict)]
                elif c["name"] == "find_similar_incidents":
                    plano["novas_consultas"] += list(c["args"].get("queries", []))
                else:
                    avisos.append(f"ferramenta desconhecida: {c['name']}")
            if not m.tool_calls and isinstance(m.content, str) and m.content.strip():
                plano["justificativa"] = m.content.strip()
        elif isinstance(m, ToolMessage):
            if m.status == "error":
                avisos.append(f"{m.name}: {str(m.content)[:200]}")
            art = m.artifact or {}
            for i, trechos in art.get("resultados", {}).items():
                aprofundados.setdefault(i, []).extend(trechos)
            novos += art.get("incidentes", [])
            justificativas.update(art.get("justificativas", {}))
            buscas += art.get("buscas", [])
            avisos += art.get("avisos", [])
    achados, ja = [], set()
    for r in [*estado.get("candidatos", []), *novos]:
        if r["doc_id"] in ja:
            continue
        ja.add(r["doc_id"])
        detalhes = list(r.get("detalhes", []))
        textos = {d["content"] for d in detalhes}
        extra = [d for d in aprofundados.get(r["doc_id"], []) if d["content"] not in textos]
        aprofundado = r["doc_id"] in aprofundados or bool(r.get("aprofundado"))  # refinamento: mantém o anterior
        achados.append({**r, "aprofundado": aprofundado, "why": justificativas.get(r["doc_id"], r.get("why")),
                        "detalhes": (extra + detalhes)[:MAX_TRECHOS]})  # aprofundamento primeiro
    # ordem: os que o LLM aprofundou, na ordem em que ele os listou (o primeiro é o que ele acha mais parecido);
    # depois os aprofundados em rodadas anteriores (refinamento); depois os demais, por similaridade
    ordem_llm = {}
    for item in plano["aprofundar"]:
        ordem_llm.setdefault(item["id"], len(ordem_llm))
    achados.sort(key=lambda r: (0, ordem_llm[r["doc_id"]]) if r["doc_id"] in ordem_llm and r["doc_id"] in aprofundados
                 else ((1, 0) if r["aprofundado"] else (2, 0)))
    achados = achados[:MAX_ACHADOS]  # os que sobram ficam em ids_vistos (não voltam numa busca nova)
    vistos = sorted(set(estado.get("ids_vistos", [])) | ja)
    return {"achados": achados, "aprofundados": aprofundados, "novos": novos, "plano": plano,
            "ids_vistos": vistos, "buscas": buscas}


def criar_grafo(espera_inicial: float = 15.0):
    g = StateGraph(EstadoPesquisa)
    g.add_node("busca_inicial", busca_inicial)
    g.add_node("agente", agente, retry_policy=RetryPolicy(max_attempts=3, initial_interval=espera_inicial,
                                                          backoff_factor=2.0, jitter=True, retry_on=_tentar_de_novo))
    g.add_node("ferramentas", ToolNode(pf.FERRAMENTAS))
    g.add_node("montar_achados", montar_achados)
    g.add_conditional_edges(START, rota_entrada)
    g.add_edge("busca_inicial", "agente")
    g.add_conditional_edges("agente", depois_do_agente)
    g.add_conditional_edges("ferramentas", depois_das_ferramentas)
    g.add_edge("montar_achados", END)
    return g.compile()


# ---------------------------------------------------------------- execução

def _mostrar(no: str, delta: dict) -> None:
    seg = (delta.get("tempos") or {})
    print(f"\n== {no}" + (f" ({list(seg.values())[0]}s)" if seg else ""), flush=True)
    if no == "busca_inicial":
        for b in delta["buscas"]:
            print(f"   busca: {b['consulta'][:90]!r} -> {', '.join(b['ids'])}")
    elif no == "agente":
        for m in delta.get("messages", []):
            if isinstance(m, AIMessage):
                for c in m.tool_calls:
                    print(f"   chama {c['name']}: {json.dumps(c['args'], ensure_ascii=False)[:400]}")
                if not m.tool_calls:
                    print(f"   sem ferramenta: {str(m.content)[:300]}")
        for c in delta.get("chamadas_llm", []):
            if c.get("nomes_corrigidos"):
                print(f"   ({c['nomes_corrigidos']} nome(s) de ferramenta corrigido(s))")
    elif no == "ferramentas":
        for m in delta.get("messages", []):
            print(f"   {m.name} ({m.status}): {str(m.content)[:300].replace(chr(10), ' ')}")
    elif no == "montar_achados":
        for r in delta["achados"]:
            n_ap = sum(d.get("origem") == "aprofundamento" for d in r["detalhes"])
            print(f"   {r['doc_id']} {r['similaridade']:.3f} {r['company']} — {r['title'][:50]}  "
                  f"{'APROFUNDADO ' if r['aprofundado'] else ''}trechos: {len(r['detalhes'])} ({n_ap} de aprofundamento)")
            if r.get("why"):
                print(f"      por quê: {r['why'][:150]}")
        for a in delta["plano"]["avisos"]:
            print(f"   aviso: {a}")


def pesquisar(descricao: str, sintomas: list[str] | None = None, pedido: str = "", anteriores: dict | None = None,
              sem_llm: bool = False, mostrar=None) -> dict:
    entrada: dict = {"descricao": descricao, "sintomas": sintomas or [], "pedido_busca": pedido, "sem_llm": sem_llm}
    if anteriores:
        entrada.update({"candidatos": anteriores["achados"], "ids_vistos": anteriores.get("ids_vistos", [])})
    estado: dict = {}
    for parte in criar_grafo().stream(entrada, {"recursion_limit": 20}, stream_mode=["updates", "values"], version="v2"):
        if parte["type"] == "values":
            estado = parte["data"]
        elif mostrar:
            for no, delta in parte["data"].items():
                mostrar(no, delta or {})
    return estado


def _serializavel(estado: dict) -> dict:
    """Troca as mensagens do LangChain por dicionários simples, para salvar em JSON."""
    out = {k: v for k, v in estado.items() if k != "messages"}
    out["messages"] = [{"tipo": m.type, "conteudo": m.content if isinstance(m.content, str) else str(m.content),
                        **({"tool_calls": m.tool_calls} if isinstance(m, AIMessage) and m.tool_calls else {}),
                        **({"ferramenta": m.name} if isinstance(m, ToolMessage) else {})}
                       for m in estado.get("messages", [])]
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("descricao", nargs="+")
    ap.add_argument("--sintoma", action="append", default=[], help="pode repetir")
    ap.add_argument("--pedido", default="", help="pedido do Diagnóstico (refinamento)")
    ap.add_argument("--anteriores", type=Path, help="JSON de uma rodada anterior (refinamento)")
    ap.add_argument("--sem-llm", action="store_true", help="chamada fixa, sem o NIM")
    ap.add_argument("--json", type=Path, help="salva o estado final")
    ap.add_argument("--modelo", help="modelo do NIM só nesta execução (padrão: LLM_MODEL do .env)")
    ap.add_argument("--agentico", action="store_true", help="experimento: o LLM faz a 1ª busca (sem busca inicial em código)")
    ap.add_argument("--hibrido", action="store_true", help="experimento: modo agêntico + a descrição original na 1ª busca")
    a = ap.parse_args()
    if a.modelo:
        global MODELO_FORCADO
        MODELO_FORCADO = a.modelo
    if a.hibrido:
        ativar_modo_hibrido()
    elif a.agentico:
        ativar_modo_agentico()
    anteriores = json.loads(a.anteriores.read_text()) if a.anteriores else None
    t = time.time()
    estado = pesquisar(" ".join(a.descricao), a.sintoma, a.pedido, anteriores, a.sem_llm, _mostrar)
    print(f"\ntotal: {time.time() - t:.0f}s, {len(estado.get('chamadas_llm', []))} chamada(s) ao LLM, "
          f"{len(estado.get('buscas', []))} busca(s)")
    if a.json:
        a.json.write_text(json.dumps(_serializavel(estado), ensure_ascii=False, indent=1, default=str))
        print(f"estado salvo em {a.json}")


if __name__ == "__main__":
    main()
