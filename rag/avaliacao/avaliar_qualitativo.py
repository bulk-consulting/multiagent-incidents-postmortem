"""
Avaliação qualitativa do RAG (entrega 3.5).

Roda cada pergunta de rag/avaliacao/perguntas.json no pipeline (rag/grafo.py) e gera:
    rag/avaliacao/resultados/<data-hora>.json   tudo o que o grafo produziu, para auditoria
    rag/avaliacao/resultados/<data-hora>.md     planilha de leitura com as checagens automáticas
                                                e colunas em branco para a nota humana

Checagens automáticas (não substituem a leitura):
    recuperação  posição do incidente esperado entre os recuperados (só os 5 primeiros vão ao prompt)
    citação      se a resposta cita o incidente esperado e se cita algum ID fora do contexto
    evidência    o nível que o modelo declarou (forte / parcial / insuficiente)

Notas humanas, de 0 a 2, por pergunta:
    correção     a resposta está certa segundo os documentos? (0 errada/inventada, 1 incompleta, 2 certa)
    relevância   o contexto recuperado serve para responder? (0 não, 1 em parte, 2 sim)
    citação      as fontes citadas sustentam o que foi dito? (0 não, 1 em parte, 2 sim)

Uso (a partir da raiz do repositório, com o pgvector no ar):
    multiagent_env/bin/python -I rag/avaliacao/avaliar_qualitativo.py [--paralelo 3] [--ids q01,q12]
                                                            [--trechos 4] [--prompt v1|v2]

O NIM gratuito leva uns 2 minutos por chamada; com 3 em paralelo, as 12 perguntas levam ~10 minutos.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
import grafo  # noqa: E402
import llm  # noqa: E402
import prompts  # noqa: E402


def rodar(caso: dict, n_docs: int, n_trechos: int, versao: str) -> dict:
    t = time.time()
    try:
        estado = grafo.perguntar(caso["pergunta"], n_docs, n_trechos, prompt_versao=versao)
        erro = None
    except Exception as e:  # registra e segue para as outras perguntas
        estado, erro = {}, f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=3)}"
    rec = [prompts._id_curto(r["doc_id"]) for r in estado.get("recuperados", [])]
    alvo = set(caso["esperado"]) | set(caso.get("aceitos", []))
    citados = estado.get("citados", [])
    pos = [rec.index(e) + 1 for e in caso["esperado"] if e in rec]
    print(f"  {caso['id']} terminou em {time.time() - t:.0f}s" + (f" (ERRO: {erro.splitlines()[0]})" if erro else ""), flush=True)
    return {
        **caso, "erro": erro, "segundos": round(time.time() - t, 1),
        "recuperados": [{"id": i, "similaridade": round(r["similaridade"], 3), "titulo": f"{r['company']} — {r['title']}"}
                        for i, r in zip(rec, estado.get("recuperados", []))],
        "resposta": estado.get("resposta"), "citados": citados, "invalidos": estado.get("invalidos", []),
        "tentativas": estado.get("tentativas"), "uso": estado.get("uso", []),
        "auto": {
            "posicoes_esperado": pos,
            "esperado_no_contexto": bool(alvo & set(rec)) if alvo else None,
            "cita_esperado": bool(alvo & set(citados)) if alvo else None,
            "cita_fora_do_contexto": bool(estado.get("invalidos")),
            "evidencia": (estado.get("resposta") or {}).get("evidencia"),
        },
    }


def _sim_nao(v) -> str:
    return "—" if v is None else ("sim" if v else "não")


def relatorio(res: list[dict], meta: dict) -> str:
    L = [f"# Avaliação qualitativa do RAG — {meta['quando']}", "",
         f"Modelo: `{meta['modelo']}` · prompt `{meta['prompt']}` · {meta['n_docs']} incidentes × {meta['n_trechos']} trechos no contexto", "",
         "## Resumo das checagens automáticas", "",
         "| id | tipo | esperado | posição na busca | no contexto | cita o esperado | cita ID fora | evidência | tempo |",
         "|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        a = r["auto"]
        L.append(f"| {r['id']} | {r['tipo']} | {', '.join(r['esperado']) or '(nenhum)'} | "
                 f"{', '.join(map(str, a['posicoes_esperado'])) or '—'} | {_sim_nao(a['esperado_no_contexto'])} | "
                 f"{_sim_nao(a['cita_esperado'])} | {_sim_nao(a['cita_fora_do_contexto'])} | {a['evidencia'] or 'erro'} | {r['segundos']:.0f}s |")
    L += ["", "## Notas humanas (0–2)", "",
          "Preencher depois de ler cada resposta abaixo. Critérios no início de `avaliar_qualitativo.py`.", "",
          "| id | correção | relevância do contexto | citação | comentário |", "|---|---|---|---|---|"]
    L += [f"| {r['id']} |  |  |  |  |" for r in res]
    L += ["", "## Respostas", ""]
    for r in res:
        L += [f"### {r['id']} ({r['tipo']})", "", f"**Pergunta:** {r['pergunta']}", "",
              f"**Esperado:** {', '.join(r['esperado']) or 'nenhum (fora do corpus)'}"
              + (f" · também aceito: {', '.join(r['aceitos'])}" if r.get("aceitos") else ""), ""]
        if r.get("observacao"):
            L += [f"*{r['observacao']}*", ""]
        L += ["**Recuperados:** " + "; ".join(f"{x['id']} ({x['similaridade']})" for x in r["recuperados"]), ""]
        if r["erro"]:
            L += ["**ERRO:**", "", "```", r["erro"].strip(), "```", ""]
            continue
        L += ["**Resposta:**", ""] + [f"> {linha}" if linha else ">" for linha in r["resposta"]["resposta"].splitlines()] + [""]
        L += [f"evidência declarada: **{r['resposta']['evidencia']}** · citados: {', '.join(r['citados']) or '—'}"
              + (f" · **fora do contexto: {', '.join(r['invalidos'])}**" if r["invalidos"] else "")
              + f" · tentativas: {r['tentativas']}", ""]
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paralelo", type=int, default=3)
    ap.add_argument("--ids", help="só estas perguntas, separadas por vírgula (ex.: q01,q12)")
    ap.add_argument("--docs", type=int, default=5)
    ap.add_argument("--trechos", type=int, default=2)
    ap.add_argument("--prompt", choices=sorted(prompts.SISTEMAS), default=prompts.VERSAO, help="versão do system prompt")
    a = ap.parse_args()

    casos = json.loads((PASTA / "perguntas.json").read_text())["perguntas"]
    if a.ids:
        casos = [c for c in casos if c["id"] in a.ids.split(",")]
    print(f"carregando o modelo de embedding e rodando {len(casos)} perguntas ({a.paralelo} em paralelo)...", flush=True)
    grafo.busca().vetorizar("aquecimento")  # carrega o modelo uma vez, antes das threads
    with ThreadPoolExecutor(a.paralelo) as ex:
        res = list(ex.map(lambda c: rodar(c, a.docs, a.trechos, a.prompt), casos))

    quando = datetime.now().strftime("%Y-%m-%d_%H%M")
    meta = {"quando": quando, "modelo": llm.MODELO, "prompt": a.prompt, "n_docs": a.docs, "n_trechos": a.trechos}
    saida = PASTA / "resultados"
    saida.mkdir(exist_ok=True)
    (saida / f"{quando}.json").write_text(json.dumps({"meta": meta, "resultados": res}, ensure_ascii=False, indent=1))
    (saida / f"{quando}.md").write_text(relatorio(res, meta))
    print(f"\nsalvo em {saida / quando}.json e .md")


if __name__ == "__main__":
    main()
