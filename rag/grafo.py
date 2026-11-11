"""
Pipeline RAG de ponta a ponta em LangGraph (entrega 3.3).

    START → recuperar → montar_prompt → gerar → verificar_citacoes → END
                                          ▲              │
                                          └── IDs fora do contexto (no máximo 1 nova tentativa)

    recuperar           busca em duas etapas no pgvector (ingestion/banco/busca.py, entrega 3.1)
    montar_prompt       system prompt + contexto formatado + pergunta (rag/prompts.py, entrega 3.4)
    gerar               GPT-OSS-20B no NVIDIA NIM, com resposta estruturada (rag/llm.py, entrega 3.2)
    verificar_citacoes  confere, sem LLM, se cada ID citado está entre os recuperados

Não usa o pacote langchain: os nós chamam a busca e o NIM diretamente. Ainda não tem
checkpointer nem aprovação humana; isso entra na etapa dos agentes.

Uso (a partir da raiz do repositório, com o container do pgvector no ar):
    multiagent_env/bin/python -I rag/grafo.py "texto da pergunta" [--docs 5] [--trechos 2]
                                              [--mostrar-prompt] [--json saida.json]
    multiagent_env/bin/python -I rag/grafo.py --mermaid      # desenho do grafo (texto Mermaid)
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import operator
import re
import sys
import time
from pathlib import Path
from typing import Annotated, Literal, TypedDict

import psycopg
from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import llm  # noqa: E402
import prompts  # noqa: E402

MAX_TENTATIVAS_CITACAO = 2  # geração original + 1 correção
ID_RE = re.compile(r"\bDAN-\d{3}\b")

_busca = None


def busca():
    """Carrega ingestion/banco/busca.py sob demanda (o modelo de embedding demora para carregar)."""
    global _busca
    if _busca is None:
        spec = importlib.util.spec_from_file_location("busca", ROOT / "ingestion" / "banco" / "busca.py")
        _busca = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_busca)
    return _busca


class Estado(TypedDict, total=False):
    pergunta: str
    n_docs: int
    n_trechos: int
    prompt_versao: str                             # "v1" ou "v2" (padrão: prompts.VERSAO)
    recuperados: list[dict]
    contexto: str
    mensagens: list[dict]
    resposta: dict
    citados: list[str]
    invalidos: list[str]
    tentativas: int
    uso: Annotated[list[dict], operator.add]      # tokens de cada chamada ao LLM
    tempos: Annotated[dict, operator.or_]          # segundos por etapa


def recuperar(estado: Estado) -> dict:
    t = time.time()
    rec = busca().buscar(estado["pergunta"], estado.get("n_docs", 5), estado.get("n_trechos", 2))
    return {"recuperados": rec, "tempos": {"recuperar": round(time.time() - t, 1)}}


def montar_prompt(estado: Estado) -> dict:
    contexto = prompts.montar_contexto(estado["recuperados"])
    versao = estado.get("prompt_versao", prompts.VERSAO)
    return {"contexto": contexto, "mensagens": prompts.mensagens(estado["pergunta"], contexto, versao), "tentativas": 0}


def gerar(estado: Estado) -> dict:
    msgs = list(estado["mensagens"])
    if estado.get("invalidos"):  # nova tentativa: mostra a resposta anterior e pede a correção
        validos = [prompts._id_curto(r["doc_id"]) for r in estado["recuperados"]]
        msgs += [{"role": "assistant", "content": estado["resposta"]["resposta"]},
                 {"role": "user", "content": prompts.correcao_citacoes(estado["invalidos"], validos)}]
    try:
        r = llm.estruturado(msgs, prompts.NOME_FERRAMENTA, prompts.DESCRICAO_FERRAMENTA, prompts.SCHEMA_RESPOSTA)
    except llm.TENTAR_DE_NOVO as e:
        # avisa e devolve a exceção para a RetryPolicy do nó tentar de novo
        print(f"[gerar] falha temporária ({type(e).__name__}: {str(e)[:120]}); o grafo vai tentar de novo", flush=True)
        raise
    n = estado.get("tentativas", 0) + 1
    return {"resposta": r["dados"], "tentativas": n,
            "uso": [{"tentativa": n, "segundos": r["segundos"], **r["uso"]}],
            "tempos": {f"gerar_{n}": r["segundos"]}}


HIFENS = str.maketrans({"‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-"})


def normalizar(resp: dict) -> dict:
    """Corrige variações de formato vistas nos testes com o GPT-OSS-20B:
    `incidentes_citados` como texto em vez de lista, IDs com hífen tipográfico (DAN‑145)
    e quebras de linha escapadas ("\\n" literal) no texto da resposta."""
    texto = resp.get("resposta", "")
    if "\\n" in texto and "\n" not in texto:
        texto = texto.replace("\\n", "\n")
    texto = texto.translate(HIFENS)
    citados = resp.get("incidentes_citados", [])
    if isinstance(citados, str):
        citados = [citados]
    citados = sorted({i for c in citados for i in ID_RE.findall(str(c).translate(HIFENS))})
    return {**resp, "resposta": texto, "incidentes_citados": citados}


def verificar_citacoes(estado: Estado) -> dict:
    validos = {prompts._id_curto(r["doc_id"]) for r in estado["recuperados"]}
    resp = normalizar(estado["resposta"])
    citados = sorted(set(resp["incidentes_citados"]) | set(ID_RE.findall(resp["resposta"])))
    return {"resposta": resp, "citados": citados, "invalidos": [c for c in citados if c not in validos]}


def depois_de_verificar(estado: Estado) -> Literal["gerar", "__end__"]:
    if estado["invalidos"] and estado["tentativas"] < MAX_TENTATIVAS_CITACAO:
        return "gerar"
    return END


def criar_grafo(espera_inicial: float = 15.0):
    """`espera_inicial`: segundos antes da 2ª tentativa de chamar o LLM (depois dobra: 15, 30, 60)."""
    g = StateGraph(Estado)
    g.add_node("recuperar", recuperar, retry_policy=RetryPolicy(max_attempts=2, retry_on=psycopg.OperationalError))
    g.add_node("montar_prompt", montar_prompt)
    # O NIM gratuito às vezes devolve 502 ("Upstream request failed") ou demora demais; até 4 tentativas.
    g.add_node("gerar", gerar, retry_policy=RetryPolicy(max_attempts=4, initial_interval=espera_inicial,
                                                        backoff_factor=2.0, jitter=True, retry_on=llm.TENTAR_DE_NOVO))
    g.add_node("verificar_citacoes", verificar_citacoes)
    g.add_edge(START, "recuperar")
    g.add_edge("recuperar", "montar_prompt")
    g.add_edge("montar_prompt", "gerar")
    g.add_edge("gerar", "verificar_citacoes")
    g.add_conditional_edges("verificar_citacoes", depois_de_verificar, {"gerar": "gerar", END: END})
    return g.compile()


def perguntar(pergunta: str, n_docs: int = 5, n_trechos: int = 2, mostrar=None, espera_inicial: float = 15.0,
              prompt_versao: str = prompts.VERSAO) -> dict:
    """Roda o grafo e devolve o estado final. `mostrar(no, delta)` recebe o progresso de cada etapa."""
    grafo = criar_grafo(espera_inicial)
    estado: dict = {}
    entrada = {"pergunta": pergunta, "n_docs": n_docs, "n_trechos": n_trechos, "prompt_versao": prompt_versao}
    for parte in grafo.stream(entrada, stream_mode=["updates", "values"], version="v2"):
        if parte["type"] == "updates" and mostrar:
            for no, delta in parte["data"].items():
                mostrar(no, delta)
        elif parte["type"] == "values":
            estado = parte["data"]
    return estado


def _progresso(no: str, delta: dict) -> None:
    if no == "recuperar":
        print(f"[recuperar] {len(delta['recuperados'])} incidentes em {delta['tempos']['recuperar']}s")
        for k, r in enumerate(delta["recuperados"], 1):
            print(f"   {k}. {prompts._id_curto(r['doc_id'])}  {r['similaridade']:.3f}  {r['company']} — {r['title'][:70]}")
    elif no == "montar_prompt":
        print(f"[montar_prompt] contexto com {len(delta['contexto'])} caracteres")
        print("[gerar] chamando o GPT-OSS-20B no NIM (pode levar uns 2 minutos)...", flush=True)
    elif no == "gerar":
        u = delta["uso"][0]
        rotulo = "resposta recebida" if delta["tentativas"] == 1 else f"resposta corrigida ({delta['tentativas']}ª geração)"
        print(f"[gerar] {rotulo}: {u['segundos']}s, {u.get('completion_tokens')} tokens gerados")
    elif no == "verificar_citacoes":
        if delta["invalidos"]:
            print(f"[verificar_citacoes] IDs fora do contexto: {delta['invalidos']}")
        else:
            print(f"[verificar_citacoes] ok: {delta['citados']}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pergunta", nargs="*")
    ap.add_argument("--docs", type=int, default=5)
    ap.add_argument("--trechos", type=int, default=2)
    ap.add_argument("--mostrar-prompt", action="store_true")
    ap.add_argument("--json", type=Path, help="salva o estado final (pergunta, recuperados, resposta) em JSON")
    ap.add_argument("--mermaid", action="store_true", help="imprime o desenho do grafo e sai")
    a = ap.parse_args()
    if a.mermaid:
        print(criar_grafo().get_graph().draw_mermaid())
        return
    if not a.pergunta:
        ap.error("informe a pergunta")
    pergunta = " ".join(a.pergunta)

    try:
        estado = perguntar(pergunta, a.docs, a.trechos, mostrar=_progresso)
    except (llm.ErroLLM, *llm.TENTAR_DE_NOVO) as e:
        sys.exit(f"\nERRO: o LLM não respondeu depois de 4 tentativas ({type(e).__name__}: {str(e)[:200]}).\n"
                 "O NIM gratuito fica instável às vezes; tente de novo em alguns minutos.")
    except psycopg.OperationalError as e:
        sys.exit(f"\nERRO: não consegui conectar ao PostgreSQL ({str(e).strip()[:150]}).\n"
                 "Confira se o Docker Desktop está aberto e o container e2-pgvector-andre está no ar.")
    if a.mostrar_prompt:
        print("\n" + "=" * 30 + " PROMPT " + "=" * 30)
        for m in estado["mensagens"]:
            print(f"--- {m['role']} ---\n{m['content']}\n")
    resp = estado["resposta"]
    print("\n" + "=" * 30 + " RESPOSTA " + "=" * 30)
    print(resp["resposta"])
    print(f"\nevidência: {resp['evidencia']}   citados: {', '.join(estado['citados']) or '—'}")
    if estado["invalidos"]:
        print(f"ATENÇÃO: a resposta ainda cita IDs fora do contexto: {estado['invalidos']}")
    print("fontes:")
    for r in estado["recuperados"]:
        if prompts._id_curto(r["doc_id"]) in estado["citados"]:
            print(f"   [{prompts._id_curto(r['doc_id'])}] {r['url']}")
    if a.json:
        saida = {k: estado[k] for k in ("pergunta", "recuperados", "resposta", "citados", "invalidos", "tentativas", "uso", "tempos")}
        saida["prompt_versao"] = estado.get("prompt_versao", prompts.VERSAO)
        saida["modelo"] = llm.MODELO
        a.json.write_text(json.dumps(saida, ensure_ascii=False, indent=1))
        print(f"\nestado salvo em {a.json}")


if __name__ == "__main__":
    main()
