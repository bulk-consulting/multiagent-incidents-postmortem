# Avaliação — otel-incident-lab

Avaliação feita em 30/10/2026 do repositório
[hrmse/otel-incident-lab](https://github.com/hrmse/otel-incident-lab),
commit `398d6b9d35329e65aaa8c43135cbae4f86e98403` (15/09/2026). O repositório não tem arquivo de licença.

## Veredito

**Não é um dataset e não entra no RAG.** É um laboratório mínimo: uma API de checkout de 38 linhas com uma
única falha simulada (um 503 disparado por um cabeçalho HTTP), mais uma pilha local de observabilidade.

**Serve apenas como referência de montagem** da pilha OpenTelemetry Collector → Tempo (traces),
Prometheus (métricas) e Loki (logs), consultada pelo Grafana, já configurada para rodar com Docker Compose.
Essa pilha pode receber a telemetria do OpenTelemetry Demo (`../opentelemetry-demo-dataset/`) quando o
ambiente de testes de correlação for montado.

## O que tem

| Item | Valor |
|---|---|
| Aplicação | Uma API de checkout em Python (FastAPI), sem estado e sem dependências externas |
| Falha | Uma só: requisição com `X-Debug-Fail: true` devolve 503 e grava um log de erro, se `LAB_ALLOW_DEBUG_FAILURES=true` |
| Observabilidade | OpenTelemetry Collector, Tempo, Prometheus, Loki e Grafana (com um dashboard de investigação) |
| Documentação | Runbook do exercício (`docs/incident-runbook.md`) e modelo de ameaças (`docs/threat-model.md`) |
| Tamanho | 20 arquivos, 148 KB, 2 commits |

## Por que não serve como fonte de dados

- Não há telemetria gravada; é preciso executar o laboratório.
- A única falha é artificial e trivial: não tem causa raiz a investigar. O próprio runbook diz que o
  laboratório não permite estabelecer causa raiz de um sistema real.
- O OpenTelemetry Demo cobre o mesmo propósito com 16 serviços e 14 falhas injetáveis.

## O que vale aproveitar

- **Configurações prontas** em `deploy/` (Collector, Tempo, Prometheus, Loki, provisionamento do Grafana)
  como ponto de partida para o backend local de observabilidade dos testes.
- **Roteiro de investigação entre os três sinais** (métrica → trace → log pelo contexto do trace), útil
  como referência para o agente do Copilot que consulta observabilidade.
- **Boas práticas de segurança do ambiente** (contêineres sem root, sistema de arquivos somente leitura,
  falha só habilitada localmente).
