"""
Mostra, passo a passo, o que o LangGraph faz ao rodar o grafo do RAG (rag/grafo.py).

Para cada nó: quem o acionou, o que estava no estado quando ele começou, o que ele devolveu
e como o estado ficou depois. Também mostra a decisão da aresta condicional e as novas
tentativas da RetryPolicy. Serve para estudo; o pipeline em si continua em rag/grafo.py.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I rag/ver_fluxo.py "texto da pergunta"     # de verdade (pgvector + NIM, ~2 min)
    multiagent_env/bin/python -I rag/ver_fluxo.py --simulado              # sem banco nem NIM, em segundos
    multiagent_env/bin/python -I rag/ver_fluxo.py --simulado --citacao-errada   # mostra o laço de correção
    multiagent_env/bin/python -I rag/ver_fluxo.py --simulado --falha-nim        # mostra a RetryPolicy
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grafo  # noqa: E402
import llm  # noqa: E402
import prompts  # noqa: E402

LINHA = "━" * 70


def resumir(chave: str, valor) -> str:
    """Versão curta de cada campo do estado, para caber no terminal."""
    if chave == "recuperados":
        return f"{len(valor)} incidentes: " + ", ".join(
            f"{prompts._id_curto(r['doc_id'])} ({r['similaridade']:.3f})" for r in valor)
    if chave == "contexto":
        return f"{len(valor)} caracteres, começa com {valor.splitlines()[0][:50]!r}"
    if chave == "mensagens":
        return f"{len(valor)} mensagens: " + ", ".join(f"{m['role']} ({len(m['content'])} car.)" for m in valor)
    if chave == "resposta":
        return (f"evidência={valor.get('evidencia')}, citados={valor.get('incidentes_citados')}, "
                f"texto={valor.get('resposta', '')[:60]!r}…")
    texto = repr(valor)
    return texto if len(texto) <= 90 else texto[:90] + "…"


def ver(pergunta: str, espera_inicial: float) -> None:
    g = grafo.criar_grafo(espera_inicial)
    entrada = {"pergunta": pergunta, "n_docs": 5, "n_trechos": 2}
    print(f"{LINHA}\nENTRADA do grafo.stream(): {entrada}\n{LINHA}")
    passo, anterior, inicio, estado = 0, "START", {}, {}
    for parte in g.stream(entrada, stream_mode=["tasks", "updates", "values"], version="v2"):
        tipo, dados = parte["type"], parte["data"]

        if tipo == "tasks" and "input" in dados:            # um nó vai começar
            passo += 1
            inicio[dados["id"]] = time.time()
            print(f"\n▶ passo {passo}: nó '{dados['name']}'   (veio de: {anterior})")
            print(f"  estado que o nó recebe: chaves {sorted(dados['input'])}")

        elif tipo == "tasks" and "result" in dados:         # um nó terminou
            if dados["error"]:
                print(f"  ✗ '{dados['name']}' falhou: {dados['error']}")
            else:
                print(f"◀ '{dados['name']}' terminou em {time.time() - inicio[dados['id']]:.1f}s")

        elif tipo == "updates":                             # o que o nó devolveu (só o que mudou)
            for no, delta in dados.items():
                print(f"  o nó devolveu (o LangGraph junta isto ao estado):")
                for k, v in delta.items():
                    obs = "  ← reducer: soma à lista" if k == "uso" else "  ← reducer: junta ao dict" if k == "tempos" else ""
                    print(f"     {k} = {resumir(k, v)}{obs}")
                anterior = no

        elif tipo == "values":                              # estado completo depois do passo
            estado = dados
            if passo:
                print(f"  estado agora tem: {sorted(estado)}")
            if anterior == "verificar_citacoes":
                destino = grafo.depois_de_verificar(estado)
                print(f"  ◆ aresta condicional depois_de_verificar(): invalidos={estado['invalidos']}, "
                      f"tentativas={estado['tentativas']} → {'gerar (nova tentativa)' if destino == 'gerar' else 'END'}")

    print(f"\n{LINHA}\nFIM. Resposta final:\n{estado['resposta']['resposta']}")
    print(f"\nevidência: {estado['resposta']['evidencia']}   citados: {estado['citados']}")
    print(f"uso (somado pelo reducer): {estado['uso']}\ntempos (juntado pelo reducer): {estado['tempos']}\n{LINHA}")


def simular(citacao_errada: bool, falha_nim: bool) -> None:
    """Troca a busca e o LLM por versões falsas e rápidas. O grafo e o LangGraph são os de verdade."""
    falsos = [("DAN-137", "Cloudflare", "WAF regex outage", 0.673),
              ("DAN-224", "Stack Exchange", "Outage Postmortem", 0.629)]

    def recuperar_falso(estado):
        time.sleep(0.5)
        return {"recuperados": [{"doc_id": f"danluu:{i}", "company": c, "title": t, "url": "https://exemplo",
                                 "resumo": "resumo de teste", "similaridade": s,
                                 "detalhes": [{"secao": "Root cause", "content": "trecho de teste", "similaridade": s}]}
                                for i, c, t, s in falsos],
                "tempos": {"recuperar": 0.5}}

    chamadas = {"n": 0}

    def estruturado_falso(mensagens, *a, **k):
        chamadas["n"] += 1
        time.sleep(1)
        if falha_nim and chamadas["n"] == 1:
            raise llm.ErroTemporarioLLM("HTTP 502: Upstream request failed (simulado)")
        corrigindo = mensagens[-1]["role"] == "user" and "não estão no CONTEXTO" in mensagens[-1]["content"]
        if citacao_errada and not corrigindo:
            dados = {"resposta": "Sim, aconteceu em [DAN-137] e em [DAN-999].",
                     "incidentes_citados": ["DAN-137", "DAN-999"], "evidencia": "forte"}
        else:
            dados = {"resposta": "Sim, aconteceu em [DAN-137] (regex no WAF esgotou a CPU).",
                     "incidentes_citados": ["DAN-137"], "evidencia": "forte"}
        return {"dados": dados, "raciocinio": "", "segundos": 1.0,
                "uso": {"prompt_tokens": 1000, "completion_tokens": 100, "total_tokens": 1100}}

    grafo.recuperar = recuperar_falso      # precisa ser trocado antes de criar_grafo()
    llm.estruturado = estruturado_falso


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pergunta", nargs="*")
    ap.add_argument("--simulado", action="store_true", help="sem banco nem NIM")
    ap.add_argument("--citacao-errada", action="store_true", help="(simulado) 1ª resposta cita um ID inexistente")
    ap.add_argument("--falha-nim", action="store_true", help="(simulado) 1ª chamada ao LLM devolve 502")
    a = ap.parse_args()
    pergunta = " ".join(a.pergunta) or "Uma regex derrubou a CPU dos servidores. Já aconteceu?"
    if a.simulado:
        simular(a.citacao_errada, a.falha_nim)
        print("MODO SIMULADO: busca e LLM falsos; o grafo e o LangGraph são os de verdade.")
    elif not a.pergunta:
        ap.error("informe a pergunta ou use --simulado")
    ver(pergunta, espera_inicial=2.0 if a.simulado else 15.0)


if __name__ == "__main__":
    main()
