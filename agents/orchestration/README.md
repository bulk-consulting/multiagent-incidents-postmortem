# Orquestração (E5)

O grafo principal que liga os agentes: **Triagem → Pesquisa → Diagnóstico → Relatório**, com o laço de nova busca,
a pausa para perguntar ao analista e a validação do relatório. O contrato (o que cada agente recebe e entrega) está
em [`docs/E5_Estado_e_Formatos.md`](../../docs/E5_Estado_e_Formatos.md).

![Grafo principal](../../docs/e5_grafo_principal.svg)

## Arquivos

| Arquivo | O que é |
|---|---|
| `state.py` | o estado compartilhado (`InvestigationState`), os limites (`MAX_RESEARCH_ROUNDS = 3`, `MAX_REPORT_FIXES = 2`) e o serializador do checkpointer (`STATE_CLASSES`) |
| `graph.py` | os nós, o roteamento e `build_graph()` |
| `run.py` | a demonstração no terminal, com o estado salvo no Postgres |
| `tests/test_state.py` | o estado passa pelo checkpointer (pausa, retomada, classes Pydantic) |
| `tests/test_graph.py` | os 8 cenários do contrato com agentes falsos (sem modelo, sem banco) e o Relatório da Mari com um modelo falso |
| `experiments/` | testes com o modelo real (Triagem → Pesquisa → Diagnóstico) e os relatórios em `experiments/results/` |

## Como o grafo funciona

```
START → triage ─┬─ falta informação ───► ask_analyst (pausa) ──► triage
                ├─ já existe ──────────► related_incident ──► END
                ├─ erro ───────────────► report (inconclusivo)
                └─ problema novo ──────► research ──► diagnosis ─┬─ evidência basta ──────────► report
                                            ▲                    ├─ nova busca (até 3 rodadas) ► research
                                            └────────────────────┤
                                                                 ├─ faltam dados ─────────────► ask_analyst
                                                                 └─ limite ou erro ───────────► report (inconclusivo)
report ──► END   (o Relatório valida e corrige o próprio texto)
```

- **Os agentes não conversam entre si.** Cada nó lê o que precisa do estado, chama o seu agente e escreve o resultado
  de volta. Quem decide o próximo passo é o roteamento, em código.
- **Pausa (`interrupt()`):** quando o Triagem ou o Diagnóstico precisa de dados do incidente, o grafo pausa com as
  perguntas e salva o estado no Postgres (`thread_id = incident_id`). A resposta pode vir na mesma execução ou depois,
  em outra.
- **Depois da resposta, a investigação recomeça** com a descrição enriquecida (Triagem de novo, busca do zero). No
  máximo 3 respostas por investigação (`MAX_ANALYST_ROUNDS`); depois disso, relatório inconclusivo.
- **Erros:** se um agente falhar depois das próprias tentativas (NIM fora do ar, respostas inválidas), o erro vai para
  `errors` e o grafo termina com relatório inconclusivo. Uma investigação sempre termina com uma resposta.
- **Passo a passo:** cada nó escreve uma linha em `trace` (nó, segundos, resumo), que a demo mostra.

## Rodar a demonstração

Da raiz do repositório, com o Docker ligado (o Postgres guarda o RAG e os checkpoints) e o `.env` com a chave do NIM:

```bash
# nova investigação (se houver perguntas, elas aparecem no terminal)
multiagent_env/bin/python -I agents/orchestration/run.py "Requests are failing across an entire region." --incident DEMO-1

# responder depois, em outra execução
multiagent_env/bin/python -I agents/orchestration/run.py --resume DEMO-1 "It is our cloud object store. An engineer took a handful of machines out..."

# ver onde uma investigação parou (passo a passo e perguntas pendentes, ou o relatório)
multiagent_env/bin/python -I agents/orchestration/run.py --show DEMO-1

# sem Postgres (o estado só existe enquanto o programa roda)
multiagent_env/bin/python -I agents/orchestration/run.py "..." --memory
```

Na primeira execução, o `run.py` cria as tabelas do checkpointer no banco. Tempo típico com o NIM gratuito: 2 a 3
minutos para um caso conhecido; uns 6 minutos para um caso fora do corpus (3 rodadas de busca). Os avisos
`429 (limite do NIM)` são normais: o `rag/limite_llm.py` espera e tenta de novo.

Exemplos (25/11):
- `DEMO-104`: mensagem vaga → o Triagem pergunta o serviço → pausa → retomada em outra execução → o Pesquisa
  aprofunda o post-mortem certo (DAN-104) → Diagnóstico `high` → relatório com a fonte e o link.
- `DEMO-NEW` (incidente inventado: pagamentos em dobro depois do horário de verão): 3 rodadas de busca sem caso
  parecido → pergunta ao analista ("o agendador trata 01:30 como um horário que acontece duas vezes?").

## Rodar os testes

```bash
PYTHONPATH=. multiagent_env/bin/python -m agents.orchestration.tests.test_graph   # 40 verificações, segundos
PYTHONPATH=. multiagent_env/bin/python -m agents.orchestration.tests.test_state   # 10 verificações
```

Os agentes são chamados pelas variáveis `graph.run_triage`, `graph.run_research`, `graph.run_diagnosis` e
`graph.run_reporting`; os testes
trocam essas variáveis por agentes falsos com respostas prontas.

## O Relatório (agente da Mari)

O nó `report` chama o `reporting_node` da Mari (`agents/reporting/node.py`), que escreve o relatório com o LLM,
**valida o próprio relatório** (tipo segundo o Diagnóstico, fontes e links nos `findings`, causas = hipóteses do
Diagnóstico, links da mensagem) e corrige até 3 vezes; se não conseguir, monta um relatório inconclusivo em código.
Por isso o fluxo padrão é `report → END`, sem o nó separado `validate_report` do primeiro desenho do contrato.

- **Quando não há diagnóstico** (o Triagem, o Pesquisa ou o Diagnóstico falhou), o grafo usa o relatório
  inconclusivo em código (`code_report_node`), porque o agente da Mari precisa do diagnóstico.
- **Validação separada (opcional):** `build_graph(checkpointer, validate_report=validate_report_node)` acrescenta o
  nó de validação depois do relatório, com até `MAX_REPORT_FIXES` voltas (usado no cenário 8 dos testes).
- **Incidente duplicado:** também da Mari (`agents/reporting/related.py`), sem LLM, com a mensagem no idioma do
  analista; para trocar, `build_graph(..., related_incident=outro_no)`.
- As classes do relatório (`Report`, `ReportCause`, `Source`) estão em `STATE_CLASSES` (`state.py`).

Exemplos com o Relatório de verdade (25/11):
- `DEMO-104B` (conversa completa do DAN-104): diagnóstico `high`, relatório válido na 1ª tentativa, com correção,
  checklist de prevenção e o link do post-mortem; ~1min30.
- `DEMO-NEW` retomado com a resposta do analista: 3 rodadas sem caso parecido → relatório inconclusivo explicando por
  que o caso mais próximo não serve e o que verificar agora.
