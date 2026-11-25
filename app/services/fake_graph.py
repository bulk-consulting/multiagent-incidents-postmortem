"""A fake LangGraph graph, used while the real one (Triage → Research → Diagnosis → Report) is not ready.

It is a real LangGraph graph with a single fake node: it does not call any LLM or the database.
It only returns what the Reporting agent would return (agents/reporting/schema.py, Report), so the API
and the frontend can be built and tested against the real output format.

The demo scenario (the analyst sees the symptom, not the cause):
  "Since 21:40 every upload to our object storage fails: PUT /objects returns 401 Unauthorized
   with {"error": "invalid_credentials"} and about a third of the reads fail too. No deploy today."
The fake answer is based on a real post-mortem with the same symptoms: Cloudflare R2, March 2025
(DAN-015), where a credential rotation was deployed to the wrong environment. Every fact in the
answer comes from that post-mortem.

The rule of the fake node (only to show both kinds of answer in the demo):
  - few words in the conversation -> "inconclusive" report asking the analyst for more information;
  - enough words                  -> "diagnosis" report based on DAN-015.

When the real graph is ready, it must accept the same input ({"incident_id", "description"}) and write
the same output key ("report"). Then only app/services/incident_service.py changes.
"""
from __future__ import annotations

import time
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from agents.reporting.schema import Report, ReportCause, Source

MIN_WORDS = 12        # below this, the fake answer asks for more information
FAKE_SECONDS = 2      # a small wait, so the loading indicator of the frontend can be seen


class FakeState(TypedDict, total=False):
    incident_id: str
    description: str
    report: Report


def _inconclusive(incident_id: str) -> Report:
    gaps = [
        "Qual erro aparece? Se possível, o código HTTP e o corpo da resposta.",
        "Desde quando acontece? Afeta todas as requisições ou só algumas (escrita, leitura)?",
        "Houve alguma mudança recente: deploy, configuração, segredos?",
    ]
    message = (
        "Ainda não tenho informação suficiente para investigar este incidente.\n\n"
        "**Pode me contar um pouco mais?**\n\n" + "\n".join(f"- {g}" for g in gaps)
    )
    return Report(
        incident_id=incident_id,
        kind="inconclusive",
        summary="A descrição é curta demais para buscar incidentes parecidos.",
        message=message,
        gaps=gaps,
        suggested_checks=["Verificar nos logs do serviço afetado o código e a mensagem dos erros."],
    )


def _diagnosis(incident_id: str) -> Report:
    source = Source(
        incident_id="DAN-015",
        title="Cloudflare incident on March 21, 2025",
        url="https://blog.cloudflare.com/cloudflare-incident-march-21-2025/",
    )
    cause = ReportCause(
        root_cause=(
            "Credenciais rotacionadas e publicadas no ambiente errado. No incidente do R2 da Cloudflare, "
            "a equipe trocou as credenciais que o gateway usa para se autenticar no armazenamento, mas "
            "publicou as novas no ambiente padrão em vez de produção (faltou o parâmetro --env production). "
            "Quando as credenciais antigas foram apagadas, o gateway de produção passou a falhar na "
            "autenticação: 100% das escritas e cerca de 35% das leituras falharam, sem nenhum deploy da "
            "aplicação. É o mesmo padrão descrito aqui: erros de autenticação de repente, escritas "
            "falhando por completo e leituras só em parte."
        ),
        remediation_steps=[
            "Confirmar qual credencial o serviço de produção está usando de fato.",
            "Publicar a credencial nova no ambiente de produção. No caso da Cloudflare, isso resolveu o incidente na hora.",
        ],
        changes="Os comandos `wrangler secret put` e `wrangler deploy` foram executados sem `--env production`.",
        prevention_checklist=[
            "Registrar nos logs o sufixo do ID da credencial em uso, para saber qual credencial cada serviço usa.",
            "Antes de apagar a credencial antiga, confirmar nos logs do armazenamento que a nova já está em uso.",
        ],
        sources=[source],
        confidence="medium",
    )
    message = (
        "### Causa provável\n"
        f"{cause.root_cause}\n\n"
        "### O que fazer agora\n" + "\n".join(f"1. {s}" for s in cause.remediation_steps) + "\n\n"
        "### Para não acontecer de novo\n" + "\n".join(f"- {s}" for s in cause.prevention_checklist) + "\n\n"
        f"**Fonte:** [{source.incident_id} — {source.title}]({source.url})\n\n"
        "_Resposta simulada (grafo fake): ainda não usa os agentes reais._"
    )
    return Report(
        incident_id=incident_id,
        kind="diagnosis",
        summary="O incidente se parece com a falha do R2 da Cloudflare em março de 2025: credenciais rotacionadas e publicadas no ambiente errado (confiança média).",
        message=message,
        causes=[cause],
        suggested_checks=[
            "Verificar se alguém rotacionou credenciais ou segredos do armazenamento nas últimas horas.",
            "Comparar a credencial configurada em produção com a que o armazenamento aceita hoje.",
        ],
    )


def fake_report_node(state: FakeState) -> dict:
    time.sleep(FAKE_SECONDS)
    incident_id = state.get("incident_id", "")
    if len(state.get("description", "").split()) < MIN_WORDS:
        return {"report": _inconclusive(incident_id)}
    return {"report": _diagnosis(incident_id)}


def build_graph():
    builder = StateGraph(FakeState)
    builder.add_node("report", fake_report_node)
    builder.add_edge(START, "report")
    builder.add_edge("report", END)
    return builder.compile()
