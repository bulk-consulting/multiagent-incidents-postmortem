"""
Roda o Agente Pesquisa RAG nas 12 perguntas da E3 (rag/avaliacao/perguntas.json), ou noutro arquivo
(--arquivo agents/research/experimentos/perguntas_dificeis.json), e registra,
para cada uma, o que precisa ser conferido:
    - o incidente esperado está na busca inicial? e nos achados?
    - o LLM aprofundou o esperado? descartou o esperado?
    - os trechos de aprofundamento (seção + início do texto, para conferir à mão se são causa/correção)

Uso (a partir da raiz do repositório, com o banco no ar):
    multiagent_env/bin/python -I agents/research/experimentos/avaliar_pesquisa.py [--perguntas q01,q10] [--sem-llm]
        [--paralelo 3]
Saída: agents/research/experimentos/resultados/pesquisa_<data>.json e .md
"""
from __future__ import annotations

import argparse
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROOT = AQUI.parents[2]
sys.path.insert(0, str(AQUI.parent))
import pesquisa  # noqa: E402


def avaliar(p: dict, sem_llm: bool) -> dict:
    t = time.time()
    try:
        est = pesquisa.pesquisar(p["pergunta"], sem_llm=sem_llm)
    except Exception as e:  # registra e segue para a próxima pergunta
        return {"id": p["id"], "erro": f"{type(e).__name__}: {str(e)[:300]}", "segundos": round(time.time() - t)}
    esperados = set(p.get("esperado", [])) | set(p.get("aceitos", []))
    iniciais = [r["doc_id"] for r in est["candidatos"]] if "candidatos" in est else []
    achados = [r["doc_id"] for r in est["achados"]]
    plano = est["plano"]
    aprof = [a["id"] for a in plano["aprofundar"]]
    trechos = {i: [{"secao": d["secao"], "similaridade": round(d["similaridade"], 3),
                    "fonte_consulta": d.get("fonte_consulta", "llm"),
                    "inicio": d["content"][:300].replace("\n", " ")} for d in ts]
               for i, ts in est.get("aprofundados", {}).items()}
    # trechos inteiros do incidente certo (para conferir à mão se trazem causa e correção)
    trechos_esperado = {r["doc_id"]: [{"fonte": d.get("fonte_consulta") or d.get("origem"), "secao": d.get("secao", ""),
                                        "titulo_de_correcao": pesquisa.pf._eh_correcao(d), "texto": d["content"]}
                                       for d in r["detalhes"]]
                        for r in est.get("achados", []) if r["doc_id"] in esperados}
    return {
        "id": p["id"], "tipo": p["tipo"], "esperado": sorted(esperados),
        "trechos_do_esperado": trechos_esperado,
        "posicao_busca_inicial": p.get("posicao_busca_inicial"),
        "esperado_em_novos": sorted(esperados & {r["doc_id"] for r in est.get("novos", [])}),

        "busca_inicial": iniciais, "achados": achados,
        "esperado_na_busca_inicial": sorted(esperados & set(iniciais)),
        "esperado_nos_achados": sorted(esperados & set(achados)),
        "esperado_aprofundado": sorted(esperados & set(aprof)),
        "esperado_descartado": sorted(esperados & set(plano["descartar"])),
        "plano": plano, "trechos_aprofundamento": trechos,
        "novos": [r["doc_id"] for r in est.get("novos", [])],
        "buscas": est.get("buscas", []),
        "chamadas_llm": [{"segundos": c.get("segundos"), "tokens": (c.get("uso") or {}).get("total_tokens"),
                          "ferramentas": [t["nome"] for t in c.get("tool_calls", [])],
                          "nomes_corrigidos": c.get("nomes_corrigidos", 0), "json_consertados": c.get("json_consertados", 0), "campos_completados": c.get("campos_completados", 0), "malformadas": len(c.get("invalidas", [])), "detalhe_malformadas": c.get("invalidas", []),
                          "texto": (c.get("texto") or "")[:300]} for c in est.get("chamadas_llm", [])],
        "segundos": round(time.time() - t),
    }


def _ferramentas(r: dict) -> str:
    """Ex.: 'find → search' por chamada ao LLM; '(texto)' quando respondeu sem ferramenta; avisos de nome/formato."""
    partes = []
    for c in r.get("chamadas_llm", []):
        nomes = [n.split("_")[0] for n in c["ferramentas"]] or ["(texto)"]
        extra = (f" [{c['nomes_corrigidos']} nome corrigido]" if c["nomes_corrigidos"] else "") + \
                (f" [{c['malformadas']} malformada]" if c["malformadas"] else "") + \
                (f" [{c.get('json_consertados', 0)} JSON consertado]" if c.get("json_consertados") else "")
        partes.append("+".join(nomes) + extra)
    return " → ".join(partes) or "—"


def md(resultados: list[dict], sem_llm: bool) -> str:
    L = [f"# Agente Pesquisa RAG ({'sem LLM' if sem_llm else 'com LLM'})", "",
         "| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in resultados:
        if "erro" in r:
            L.append(f"| {r['id']} | erro: {r["erro"][:80]} | | | | | | | | | {r["segundos"]} |"); continue
        sim = lambda k: ("—" if not r["esperado"] else ("sim" if r[k] else "não"))
        L.append(f"| {r['id']} | {', '.join(r['esperado']) or '(nenhum)'} | {r.get('posicao_busca_inicial') or '—'} | "
                 f"{sim('esperado_na_busca_inicial')} | "
                 f"{sim('esperado_aprofundado')} | {_ferramentas(r)} | "
                 f"{sim('esperado_em_novos')} | "
                 f"{sim('esperado_nos_achados')} | {len(r['plano']['novas_consultas'])} | {r['segundos']} |")
    L.append("")
    for r in resultados:
        if "erro" in r:
            continue
        p = r["plano"]
        L += [f"## {r['id']} (esperado: {', '.join(r['esperado']) or 'nenhum'})", "",
              f"- busca inicial: {', '.join(r['busca_inicial'])}",
              f"- justificativa: {p['justificativa']}"]
        L += [f"- aprofundar {a['id']}: `{a['consulta']}`" + (f" — {a['why']}" if a.get("why") else "")
              for a in p["aprofundar"]]
        L += [f"- nova consulta: `{b['consulta']}` → {', '.join(b['ids'])}" for b in r.get("buscas", [])
              if b["etapa"] == "nova_consulta"]
        if r["novos"]:
            L.append(f"- novos incidentes nos achados: {', '.join(r['novos'])}")
        if p["descartar"]:
            L.append(f"- descartou: {', '.join(p['descartar'])}")
        L += [f"- aviso: {a}" for a in p.get("avisos", [])]
        for i, ts in r["trechos_aprofundamento"].items():
            for d in ts:
                L.append(f"  - {i} ({d.get('fonte_consulta', 'llm')}) [{d['secao'] or 'sem seção'}] {d['similaridade']}: {d['inicio'][:200]}")
        L.append("")
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perguntas", help="ex.: q01,q10 (padrão: todas)")
    ap.add_argument("--sem-llm", action="store_true")
    ap.add_argument("--arquivo", type=Path, default=ROOT / "rag/avaliacao/perguntas.json",
                    help="JSON com {'perguntas': [...]} (padrão: as 12 da E3; ex.: perguntas_dificeis.json)")
    ap.add_argument("--paralelo", type=int, default=1, help="quantas perguntas ao mesmo tempo (padrão: 1)")
    ap.add_argument("--modelo", help="modelo do NIM só nesta rodada (padrão: LLM_MODEL do .env)")
    ap.add_argument("--agentico", action="store_true", help="experimento: o LLM faz a 1ª busca (pesquisa.ativar_modo_agentico)")
    ap.add_argument("--sem-raciocinio", action="store_true", help="enable_thinking=False no LLM (menos tokens)")
    ap.add_argument("--hibrido", action="store_true", help="experimento: modo agêntico + a descrição original na 1ª busca")
    ap.add_argument("--candidatos", type=int, help="candidatos da busca inicial que o LLM lê (padrão: pesquisa.N_DOCS)")
    a = ap.parse_args()
    todas = json.loads(a.arquivo.read_text())["perguntas"]
    alvo = set(a.perguntas.split(",")) if a.perguntas else None
    perguntas = [p for p in todas if not alvo or p["id"] in alvo]
    # Carrega o modelo de embedding e o cliente do LLM antes das threads (evita carregar duas vezes ao mesmo tempo).
    if a.modelo:
        pesquisa.MODELO_FORCADO = a.modelo
    if a.candidatos:
        pesquisa.N_DOCS = a.candidatos
    if a.sem_raciocinio:
        pesquisa.RACIOCINIO = False
    if a.hibrido:
        pesquisa.ativar_modo_hibrido()
    elif a.agentico:
        pesquisa.ativar_modo_agentico()
    pesquisa.busca.vetorizar("aquecimento")
    if not a.sem_llm:
        pesquisa.llm_com_ferramentas()

    sufixo = "" if a.arquivo.name == "perguntas.json" else "_" + a.arquivo.stem
    if a.modelo:
        sufixo += "_" + a.modelo.split("/")[-1].replace(".", "-")  # sem ponto: with_suffix cortaria o nome
    if a.candidatos:
        sufixo += f"_{a.candidatos}cand"
    if a.sem_raciocinio:
        sufixo += "_sem-raciocinio"
    if a.hibrido:
        sufixo += "_hibrido"
    elif a.agentico:
        sufixo += "_agentico"
    saida = AQUI / "resultados" / f"pesquisa_{datetime.now():%Y-%m-%d_%H%M}{sufixo}{'_semllm' if a.sem_llm else ''}"
    saida.parent.mkdir(exist_ok=True)
    parcial = saida.with_name(saida.name + "_parcial.json")

    # Progresso visível e salvamento parcial: depois de cada pergunta, uma linha "progresso:" com quantas
    # terminaram, o tempo e a estimativa do que falta; o que já terminou vai para *_parcial.json (se a rodada
    # for interrompida, nada do que rodou se perde).
    t0 = time.time()
    feitos: dict[str, dict] = {}
    trava = threading.Lock()

    def uma(p: dict) -> dict:
        r = avaliar(p, a.sem_llm)
        with trava:
            feitos[p["id"]] = r
            n, total = len(feitos), len(perguntas)
            dec = time.time() - t0
            resta = dec / n * (total - n)
            erros = sum("erro" in x for x in feitos.values())
            print(f"progresso: {n}/{total} perguntas ({erros} com erro) · {dec / 60:.1f} min · faltam ~{resta / 60:.0f} min"
                  f" · {p['id']}: " + (r.get("erro", "")[:60] or ("certo aprofundado" if r.get("esperado_aprofundado")
                                                                    else ("—" if not r.get("esperado") else "certo NÃO aprofundado"))),
                  flush=True)
            parcial.write_text(json.dumps([feitos[q["id"]] for q in perguntas if q["id"] in feitos], ensure_ascii=False))
        return r

    # As perguntas são independentes; pool.map devolve na ordem das perguntas.
    with ThreadPoolExecutor(max_workers=max(1, a.paralelo)) as pool:
        resultados = list(pool.map(uma, perguntas))
    print(f"total: {time.time() - t0:.0f}s com {a.paralelo} em paralelo", flush=True)
    saida.with_suffix(".json").write_text(json.dumps(resultados, ensure_ascii=False, indent=1))
    saida.with_suffix(".md").write_text(md(resultados, a.sem_llm))
    parcial.unlink(missing_ok=True)
    print(f"salvo em {saida}.md / .json")


if __name__ == "__main__":
    main()
