"""
Builds an animated replay of one recorded investigation: the graph drawn on the page, the active node lit, the edge
the flow goes through animated, a panel with what happens inside each agent and the shared state filling up.

Input: a recording made by agents/orchestration/experiments/capture_walkthrough.py (results/walkthrough_*.json).
Output: one self-contained HTML file (the data goes inside it): open it in a browser, no server, no internet.

Usage (from the repository root):
    multiagent_env/bin/python -I agents/orchestration/visual/build_replay.py \
        agents/orchestration/experiments/results/walkthrough_dan104_2026-11-25_1621.json
Output: agents/orchestration/visual/replay_<case>.html
    add --detail for the replay that also opens the inside of each agent: replay_<case>_detalhe.html
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

NODE_KIND = {"triage": "agent", "research": "agent", "diagnosis": "agent", "report": "agent",
             "ask_analyst": "pause", "related_incident": "code"}
NODE_NAME = {"triage": "Triagem", "research": "Pesquisa", "diagnosis": "Diagnóstico", "report": "Relatório",
             "ask_analyst": "Pergunta ao analista", "related_incident": "Já em investigação", "start": "Início",
             "end": "Fim"}
RULES = {"triage": "route_after_triage", "research": "route_after_research", "diagnosis": "route_after_diagnosis",
         "ask_analyst": "aresta fixa ask_analyst → triage", "report": "aresta fixa report → END"}


def short(text, n=220):
    text = " ".join(str(text or "").split())
    return text if len(text) <= n else text[:n].rsplit(" ", 1)[0] + " …"


def frame(node, title, lines=(), state=(), edge=None, kind=None, seconds=None, rule=None, table=None, wait=1.0,
          sub=None, subcount=None):
    """One moment of the animation. wait = relative time on screen (multiplied by the speed).
    sub = the step inside the agent (the detailed replay lights it); subcount = a counter shown beside it."""
    return {"node": node, "kind": kind or NODE_KIND.get(node, "code"), "title": title, "lines": list(lines),
            "state": list(state), "edge": edge, "seconds": seconds, "rule": rule, "table": table, "wait": wait,
            "sub": sub, "subcount": subcount}


def triage_frames(step, inside, edge):
    out = []
    i = inside[0]
    first = i["messages"][0]["content"] if i["messages"] else ""
    out.append(frame("triage", "A Triagem lê o que o analista escreveu",
                     [f"“{short(first, 260)}”", "1 chamada ao modelo, com o prompt de agents/triage/prompts.py"],
                     edge=edge, seconds=i["seconds"], wait=1.2, sub="read"))
    for m in i["messages"]:
        for c in m.get("tool_calls") or []:
            out.append(frame("triage", f"Chama a ferramenta {c['name']}",
                             [f"argumentos: {c['arguments']}",
                              "procura investigações abertas do mesmo serviço (duplicado?)"], wait=1.0, sub="tool"))
        if m["role"] == "tool":
            try:
                data = json.loads(m["content"].rstrip(" …"))
                inv = data.get("investigations", [])
                lines = [f"{x['incident_id']} · {x['service']} · {x['status']}" for x in inv[:5]]
            except (ValueError, AttributeError):
                lines = [short(m["content"], 200)]
            out.append(frame("triage", "A ferramenta devolve as investigações", lines, kind="code", wait=1.0,
                             sub="compare"))
    r = i["result"]
    lines = [f"informação suficiente: {'sim' if r['enough_information'] else 'não'}",
             f"serviço: {r.get('affected_service') or '—'}",
             "sintomas: " + ("; ".join(r.get("symptoms") or []) or "—"),
             "mudanças citadas: " + ("; ".join(r.get("triggers") or []) or "nenhuma")]
    if r.get("missing_information"):
        lines += [f"pergunta: {q}" for q in r["missing_information"]]
    if r.get("related_incident"):
        lines.append(f"mesmo problema que {r['related_incident']['incident_id']}")
    out.append(frame("triage", "Resultado da Triagem", lines, state=list(step["update"].keys()),
                     rule=RULES["triage"], wait=1.6, sub="out"))
    return out


def research_frames(step, inside, edge):
    i = inside[0]
    rnd = step["update"].get("research_rounds")
    req = i["input"].get("request")
    head = [f"rodada {rnd} de 3"]
    if req:
        head.append(f"pedido do Diagnóstico: “{short(req, 160)}”")
        head.append(f"deixa de fora {len(i['input'].get('previous_ids') or [])} incidentes já vistos")
    out = [frame("research", "O Pesquisa procura post-mortems parecidos", head, edge=edge, seconds=i["seconds"],
                 wait=1.2, sub="code")]
    out[0]["round"] = rnd  # the round of this search (back to 1 when the investigation starts again)
    code_searches = [s for s in i["searches"] if s["step"].startswith("initial") or "description" in s["step"]]
    if code_searches:
        out.append(frame("research", "Busca em código (rede de segurança)",
                         [f"{short(s['query'], 90)} → {', '.join((s['ids'] or [])[:6])}" for s in code_searches[:3]],
                         kind="code", wait=1.2, sub="code"))
    for k, c in enumerate(i["llm_calls"], 1):
        for t in c.get("tool_calls") or []:
            if t["name"] == "find_similar_incidents":
                qs = t["args"].get("queries", [])
                out.append(frame("research", f"Modelo, chamada {k}: busca com outras palavras",
                                 [f"“{short(q, 120)}”" for q in qs], wait=1.0, sub="find", subcount=f"chamada {k}"))
            elif t["name"] == "search_inside_incidents":
                out.append(frame("research", f"Modelo, chamada {k}: aprofunda os melhores",
                                 [f"{s.get('post_mortem_id') or s.get('incident_id')}: {short(s.get('why'), 150)}" for s in t["args"].get("searches", [])],
                                 wait=1.4, sub="inside", subcount=f"chamada {k}"))
    deep = [f for f in i["findings"] if f["deepened"]]
    lines = [f"{f['id']} · {short(f['title'], 70)} · aprofundado" for f in deep]
    lines += [f"{f['id']} · {short(f['title'], 70)}" for f in i["findings"] if not f["deepened"]][:4]
    if not deep:
        lines.insert(0, "nenhum incidente aprofundado nesta rodada")
    out.append(frame("research", f"Achados: {len(i['findings'])} incidentes, {len(deep)} aprofundados", lines,
                     state=list(step["update"].keys()), rule=RULES["research"], wait=1.6, sub="build"))
    return out


def diagnosis_frames(step, inside, edge):
    i = inside[0]
    inp = i["input"]
    out = [frame("diagnosis", "O Diagnóstico compara o incidente com os casos passados",
                 [f"rodada {inp['research_round']} de 3",
                  f"{len(inp['findings'])} achados, {sum(1 for _, d in inp['findings'] if d)} com trechos",
                  "mudanças citadas: " + ("; ".join((inp.get('triage') or {}).get('triggers') or []) or "nenhuma")]
                 + ([f"pedido anterior: “{short(inp['previous_requests'][0], 120)}”"] if inp.get("previous_requests") else []),
                 edge=edge, seconds=i["seconds"], wait=1.2, sub="text")]
    draft, final = i["model_draft"], i["decided_by_code"]
    rows = []
    for h, fh in zip(draft["hypotheses"], final["hypotheses"]):
        rows.append({"cause": short(h["cause"], 110), "based_on": ", ".join(h["based_on"]),
                     "t": h["same_trigger"], "c": h["same_component"], "m": h["same_mechanism"],
                     "model": h["confidence"], "code": fh["confidence"]})
    out.append(frame("diagnosis", "O modelo escreve hipóteses e responde 3 perguntas",
                     ["mesmo tipo de gatilho? mesmo componente? mesmo mecanismo?"] if rows else
                     ["nenhuma hipótese: nada nos achados explica o incidente"], table=rows or None, wait=2.2,
                     sub="llm", subcount=f"{i['turns']} tentativas" if i.get("turns", 1) > 1 else None))
    out.append(frame("diagnosis", "Validação da resposta do modelo",
                     ["o JSON tem o formato do DiagnosisDraft (Pydantic)",
                      "cada hipótese se apoia em incidentes que estão nos achados",
                      f"tentativas até ficar válido: {i.get('turns', 1)}"], kind="code", wait=1.0, sub="check"))
    nxt = {"report": "relatório", "refine_search": "nova busca", "ask_analyst": "perguntar ao analista"}[final["next_step"]]
    lines = [f"evidência suficiente: {'sim' if final['evidence_sufficient'] else 'não'}", f"próximo passo: {nxt}"]
    if final.get("search_request"):
        lines.append(f"pedido de busca: “{short(final['search_request'], 140)}”")
    for q in final.get("questions_for_analyst") or []:
        lines.append(f"pergunta: {q}")
    out.append(frame("diagnosis", "O código decide (schema.py → decide)", lines, kind="code",
                     state=list(step["update"].keys()), rule=RULES["diagnosis"], wait=1.8, sub="decide"))
    return out


def report_frames(step, inside, edge):
    i = inside[0]
    rep = i["report"]
    out = [frame("report", "O Relatório escreve a resposta final",
                 ["no idioma do analista, com causa, correção, prevenção e fonte",
                  f"tentativas até ficar válido: {i['attempts']}"], edge=edge, seconds=i["seconds"], wait=1.2,
                 sub="llm", subcount=f"tentativa {i['attempts']}" if i["attempts"] > 1 else None),
           frame("report", "A conferência em código",
                 ["tipo de acordo com o Diagnóstico", "cada fonte existe nos achados, com o mesmo link",
                  "causas = hipóteses, na mesma ordem e confiança",
                  "resultado: " + ("válido" if not i["problems"] else "problemas: " + "; ".join(i["problems"])[:160])],
                 kind="code", wait=1.4, sub="check")]
    lines = [short(rep["summary"], 300)]
    for c in rep.get("causes", []):
        # recordings made before the rename use incident_id for the post-mortem
        src = ", ".join(s.get("post_mortem_id") or s.get("incident_id") for s in c["sources"])
        lines.append(f"[{c['confidence']}] {short(c['root_cause'], 140)} ({src})")
    out.append(frame("report", f"Relatório: {rep['kind']}", lines, state=list(step["update"].keys()),
                     rule=RULES["report"], wait=2.4, sub="out"))
    return out


def build_frames(rec):
    frames = [frame("start", "Início: o analista escreve", [f"“{short(rec['first_message'], 260)}”"], kind="code")]
    prev = "start"
    for step in rec["steps"]:
        node = step["node"]
        if node == "pause":
            q = step["interrupt"].get("questions", [])
            frames.append(frame("ask_analyst", "Pausa: o grafo espera o analista",
                                [f"pergunta: {x}" for x in q] + ["o estado fica salvo (no run.py, no Postgres)"],
                                edge=[prev, "ask_analyst"], kind="pause", state=["pending_questions"], wait=1.8))
            prev = "ask_analyst"
            continue
        if node == "analyst":
            frames.append(frame("ask_analyst", "O analista responde", [f"“{short(step['answer'], 320)}”"],
                                kind="pause", wait=1.8))
            continue
        edge = [prev, node] if prev != node else None
        inside = step.get("inside") or []
        if node == "triage" and inside:
            frames += triage_frames(step, inside, edge)
        elif node == "research" and inside:
            frames += research_frames(step, inside, edge)
        elif node == "diagnosis" and inside:
            frames += diagnosis_frames(step, inside, edge)
        elif node == "report" and inside:
            frames += report_frames(step, inside, edge)
        elif node == "ask_analyst":
            frames.append(frame("ask_analyst", "A resposta entra na investigação",
                                ["junta “Analyst answer: …” à descrição", "zera as rodadas e os achados: busca do zero"],
                                state=list(step["update"].keys()), edge=None, rule=RULES["ask_analyst"], kind="code"))
        else:
            summary = (step.get("trace") or [{}])[0].get("summary", "")
            frames.append(frame(node, NODE_NAME.get(node, node), [summary], edge=edge,
                                state=list((step.get("update") or {}).keys())))
        prev = node
    last = rec["steps"][-1]["node"]
    if last == "report" or last == "related_incident":
        frames.append(frame("end", "Fim: o relatório vai para o analista", [], edge=[prev, "end"], kind="code"))
    elif last == "pause":
        frames.append(frame("ask_analyst", "A gravação termina aqui",
                            ["o Diagnóstico pediu dados ao analista; a investigação espera a resposta"], kind="pause"))
    return frames


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    detail = "--detail" in sys.argv  # the replay that also opens the inside of each agent (layout A)
    src = Path(args[0])
    rec = json.loads(src.read_text())
    case = re.search(r"walkthrough_([a-z0-9]+)_", src.name)
    case = case.group(1) if case else "case"
    data = {"case": case.upper().replace("DAN", "DAN-"), "source": src.name, "frames": build_frames(rec)}
    html = (HERE / ("replay_detail_template.html" if detail else "replay_template.html")).read_text()
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = HERE / f"replay_{case}{'_detalhe' if detail else ''}.html"
    out.write_text(html.replace("/*__DATA__*/null", payload))
    print(f"{len(data['frames'])} frames → {out}")


if __name__ == "__main__":
    main()
