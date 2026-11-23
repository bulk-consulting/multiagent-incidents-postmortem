"""
Demonstration of the Research RAG Agent in hybrid mode, step by step, for screen recording (E4).

    multiagent_env/bin/python -I agents/research/demo.py                 # default example (hard case)
    multiagent_env/bin/python -I agents/research/demo.py --exemplo mars  # Mars Pathfinder example
    multiagent_env/bin/python -I agents/research/demo.py "your incident description" [--pausa 2]

It runs the same agent (agents/research/pesquisa.py, hybrid mode) and prints each step of the LangGraph flow:
the queries the LLM writes, where each candidate came from (analyst's text or LLM queries), which incidents
the LLM chooses and why, and the root-cause and fix passages found inside them.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pesquisa  # noqa: E402
import pesquisa_ferramentas as pf  # noqa: E402
from langchain_core.messages import AIMessage, ToolMessage  # noqa: E402

EXEMPLOS = {
    "cauda": "Our service suddenly started failing on calls to a cloud provider's API, with no change on our side.",
    "mars": "The onboard computer keeps resetting itself every now and then, a few days after going into operation.",
}
FONTE = {"llm": "LLM query", "causa": "fixed: root cause", "correcao": "fixed: fix / prevention", "fixa": "fixed"}

console = Console(width=110)


def pausa(s: float) -> None:
    if s:
        time.sleep(s)


def passo(n: int, titulo: str, subtitulo: str) -> None:
    console.print()
    console.print(Rule(f"[bold cyan]STEP {n} · {titulo}[/]"))
    console.print(f"[dim]{subtitulo}[/]")


def mostrar_agente(delta: dict, chamada: int, pausa_s: float) -> None:
    for m in delta.get("messages", []):
        if not isinstance(m, AIMessage):
            continue
        seg = (delta.get("chamadas_llm") or [{}])[-1].get("segundos", "?")
        for c in m.tool_calls:
            if c["name"] == "find_similar_incidents":
                passo(1 if chamada == 1 else 3, "The LLM decides how to search",
                      f"LLM call {chamada} ({seg}s) → tool [bold]find_similar_incidents[/]")
                for q in c["args"].get("queries", []):
                    console.print(f"   🔎  [yellow]{q}[/]")
                console.print("   [dim]+ the code always adds the analyst's original text as one more search[/]")
            elif c["name"] == "search_inside_incidents":
                passo(3, "The LLM chooses which incidents to investigate",
                      f"LLM call {chamada} ({seg}s) → tool [bold]search_inside_incidents[/]")
                for s in c["args"].get("searches", []):
                    console.print(f"   ✅  [bold green]{s.get('incident_id')}[/]  query: [yellow]{s.get('query')}[/]")
                    if s.get("why"):
                        console.print(f"       [italic]why: {s.get('why')}[/]")
        if not m.tool_calls:
            passo(3, "The LLM stops searching", f"LLM call {chamada} ({seg}s): {str(m.content)[:200]}")
    pausa(pausa_s)


def mostrar_ferramentas(delta: dict, pausa_s: float) -> None:
    for m in delta.get("messages", []):
        if not isinstance(m, ToolMessage):
            continue
        art = m.artifact or {}
        if m.name == "find_similar_incidents":
            passo(2, "Vector search in pgvector (code, < 1 s)",
                  "Candidates from the analyst's text + extra candidates found only by the LLM queries")
            t = Table(show_lines=False, header_style="bold")
            t.add_column("#", justify="right")
            t.add_column("Incident")
            t.add_column("Company / title")
            t.add_column("Found by")
            t.add_column("Similarity", justify="right")
            for k, r in enumerate(art.get("incidentes", []), 1):
                origem = r.get("origem_incidente")
                found = "[magenta]LLM query (new)[/]" if origem == "consulta_llm" else "analyst's text"
                t.add_row(str(k), r["doc_id"], f"{r['company']} — {r['title']}"[:52], found, f"{r['similaridade']:.3f}")
            console.print(t)
        elif m.name == "search_inside_incidents":
            passo(4, "Search inside the chosen incidents (code, < 1 s)",
                  "LLM query + fixed 'root cause' query + fixed 'fix / prevention' query, inside each incident")
            for inc, trechos in art.get("resultados", {}).items():
                console.print(f"   [bold green]{inc}[/]")
                for d in trechos:
                    secao = d.get("secao") or "(no section title)"
                    texto = d["content"].replace("\n", " ")
                    if texto.startswith("#"):
                        texto = texto.split(" ", 1)[-1]
                    console.print(f"     • [cyan]{secao[:45]}[/]  [dim]({FONTE.get(d.get('fonte_consulta'), '')})[/]")
                    console.print(f"       [dim]{texto[len(secao):][:170].strip()}…[/]")
    pausa(pausa_s)


def mostrar_achados(delta: dict) -> None:
    passo(5, "Output for the Diagnosis Agent (code)", "Structured findings: deepened incidents first, with the reason and the passages")
    t = Table(header_style="bold")
    t.add_column("Incident")
    t.add_column("Company / title")
    t.add_column("Deepened", justify="center")
    t.add_column("Passages", justify="right")
    for r in delta["achados"]:
        t.add_row(r["doc_id"], f"{r['company']} — {r['title']}"[:58], "✅" if r["aprofundado"] else "",
                  str(len(r["detalhes"])))
    console.print(t)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("descricao", nargs="*", help="incident description (default: --exemplo)")
    ap.add_argument("--exemplo", choices=sorted(EXEMPLOS), default="cauda")
    ap.add_argument("--pausa", type=float, default=1.5, help="seconds between steps (for recording)")
    ap.add_argument("--why-pt", action="store_true", help="keep the LLM's reason (why) in Portuguese")
    a = ap.parse_args()
    descricao = " ".join(a.descricao) or EXEMPLOS[a.exemplo]

    pesquisa.ativar_modo_hibrido()
    if not a.why_pt:  # the presentation is in English: ask for the reason (why) in English
        pf.BuscaNoIncidente.model_fields["why"].description = (
            "one short sentence, in English, saying why you chose this incident: what matches the current incident "
            "and what does not")
        pf.BuscaNoIncidente.model_rebuild(force=True)
        pesquisa.pp.SISTEMA_AGENTICO = pesquisa.pp.SISTEMA_AGENTICO.replace(
            "com uma consulta e uma frase (why)", "com uma consulta e uma frase em inglês (why)")
    console.print(Panel.fit(
        "[bold]Incident Copilot · Research RAG Agent[/] (hybrid mode)\n"
        "LangGraph · LLM: NVIDIA NIM nemotron-3.5-super-vl · pgvector (2,494 passages, 212 post-mortems)\n\n"
        f"[bold]Analyst:[/] [white]{descricao}[/]", border_style="cyan"))
    console.print("[dim]loading the embedding model…[/]")
    pesquisa.busca.vetorizar("warm-up")

    t0, chamada = time.time(), 0
    entrada = {"descricao": descricao, "sintomas": [], "pedido_busca": "", "sem_llm": False}
    estado: dict = {}
    for parte in pesquisa.criar_grafo().stream(entrada, {"recursion_limit": 20}, stream_mode=["updates", "values"],
                                                version="v2"):
        if parte["type"] == "values":
            estado = parte["data"]
            continue
        for no, delta in parte["data"].items():
            delta = delta or {}
            if no == "agente":
                chamada += len(delta.get("chamadas_llm", [])) or 1
                mostrar_agente(delta, chamada, a.pausa)
            elif no == "ferramentas":
                mostrar_ferramentas(delta, a.pausa)
            elif no == "montar_achados":
                mostrar_achados(delta)

    console.print()
    console.print(Panel.fit(
        f"[bold]Total:[/] {time.time() - t0:.0f}s · {len(estado.get('chamadas_llm', []))} LLM calls · "
        f"{len(estado.get('buscas', []))} database searches", border_style="green"))


if __name__ == "__main__":
    main()
