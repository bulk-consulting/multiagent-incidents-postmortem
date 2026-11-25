"""The answer when the problem is already being investigated (the Triage agent found a related open incident).

No LLM (as in docs/E5_Estado_e_Formatos.md): the answer is built in code from the Triage result, in the same shape
as the other reports (summary + message in Markdown for the chat), in the analyst's language (Portuguese or
English, guessed from the words of the message).

State keys it reads:    incident_id, description, triage_result
State keys it writes:   report

How to plug it into the main graph:
    build_graph(..., related_incident=related_incident_node)
"""
import re

# Common Portuguese words that do not exist in English. Two or more of them: the analyst writes in Portuguese.
PORTUGUESE_WORDS = {"não", "está", "estão", "nosso", "nossa", "com", "erro", "erros", "quando", "também", "desde",
                    "falha", "falhas", "serviço", "usuários", "para", "uma", "depois", "ainda", "hoje", "agora"}


def analyst_language(text):
    """'pt' or 'en', from the words of the analyst's message."""
    words = set(re.findall(r"[a-zà-ú]+", (text or "").lower()))
    return "pt" if len(words & PORTUGUESE_WORDS) >= 2 else "en"


TEXTS = {
    "en": {
        "summary": "This problem looks like one that is already being investigated: {id} ({title}).",
        "title": "Already under investigation: {id}",
        "intro": "Your report matches an open investigation, so a new one was not started.",
        "why": "**Why it looks like the same problem:** the same service ({service}) and the same symptoms ({symptoms}).",
        "next": "**What to do now**",
        "steps": ["Follow investigation {id} and add what you see there (time, scope, error messages).",
                  "If it is not the same problem (another symptom or another service), reply with what is different "
                  "and a new investigation will start."],
    },
    "pt": {
        "summary": "Este problema parece ser um que já está em investigação: {id} ({title}).",
        "title": "Já em investigação: {id}",
        "intro": "O seu relato corresponde a uma investigação aberta, então uma nova não foi iniciada.",
        "why": "**Por que parece o mesmo problema:** o mesmo serviço ({service}) e os mesmos sintomas ({symptoms}).",
        "next": "**O que fazer agora**",
        "steps": ["Acompanhe a investigação {id} e acrescente nela o que você está vendo (horário, alcance, mensagens "
                  "de erro).",
                  "Se não for o mesmo problema (outro sintoma ou outro serviço), responda dizendo o que é diferente "
                  "e uma nova investigação será iniciada."],
    },
}


def _get(obj, key, default=None):
    return getattr(obj, key, None) if not isinstance(obj, dict) else obj.get(key, default)


def related_incident_report(state):
    """The report for a problem that is already under investigation (a dict, like the code reports of the graph)."""
    triage = state.get("triage_result")
    related = _get(triage, "related_incident")
    rid, title = _get(related, "incident_id", ""), _get(related, "title", "")
    service = _get(triage, "affected_service") or "?"
    symptoms = ", ".join(_get(triage, "symptoms") or []) or "?"
    t = TEXTS[analyst_language(state.get("description", ""))]
    fill = {"id": rid, "title": title, "service": service, "symptoms": symptoms}
    message = "\n".join([f"### {t['title'].format(**fill)}", "", t["intro"], "", f"> {title}", "",
                         t["why"].format(**fill), "", t["next"]] + [f"- {s.format(**fill)}" for s in t["steps"]])
    return {"incident_id": state.get("incident_id", ""), "kind": "related_incident",
            "related_incident": {"incident_id": rid, "title": title},
            "summary": t["summary"].format(**fill), "message": message}


def related_incident_node(state):
    """LangGraph node: writes the report for a duplicate. Returns only the keys it updates."""
    return {"report": related_incident_report(state)}
