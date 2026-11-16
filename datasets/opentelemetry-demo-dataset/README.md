# Avaliação — OpenTelemetry Demo Dataset

Avaliação feita em 30/10/2026 do repositório
[openobserve/opentelemetry-demo-dataset](https://github.com/openobserve/opentelemetry-demo-dataset),
commit `b5284987b6f8ba23ffcb826148fa5004ff47236b` (06/02/2026). Licença Apache-2.0.

## Veredito

**Não é um dataset: é um gerador.** O repositório não contém logs, métricas ou traces gravados. É uma cópia
adaptada pela OpenObserve do aplicativo de demonstração oficial do OpenTelemetry
([open-telemetry/opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo)): uma loja virtual
com microsserviços que, ao ser executada com Docker, produz telemetria em tempo real.

**Não entra no RAG de post-mortems.** Serve para outra parte do projeto: **testar a correlação de
observabilidade e montar cenários de avaliação com causa conhecida**, porque o aplicativo tem 14 falhas que
podem ser ligadas e desligadas.

## O que tem

| Item | Valor |
|---|---|
| Serviços | 16 microsserviços (frontend, cart, checkout, payment, shipping, product catalog, recommendation, email, ad, currency, fraud detection, accounting, product reviews, quote, image provider, load generator) em várias linguagens |
| Infraestrutura | Kafka, PostgreSQL, Valkey (Redis), serviço de LLM, OpenTelemetry Collector |
| Telemetria (segundo o README) | Logs de 20 fontes; métricas de host, contêiner, aplicação, banco, cache e servidor web; traces de 7 fluxos distribuídos |
| Observabilidade incluída | Jaeger, Prometheus, Grafana, OpenSearch |
| Implantação | `docker-compose.yml` e manifesto Kubernetes (`kubernetes/opentelemetry-demo.yaml`) |
| Requisitos | Docker e Docker Compose, 4 GB+ de memória livre |
| Adição desta cópia | Um `log-generator` em Python que emite logs, traces e métricas sintéticos, e configuração do Collector para enviar a qualquer backend OTLP |

## Falhas injetáveis (feature flags)

Configuradas em `src/flagd/demo.flagd.json`, todas desligadas por padrão:

| Flag | O que provoca |
|---|---|
| `kafkaQueueProblems` | Sobrecarga da fila Kafka com atraso no consumidor |
| `emailMemoryLeak` | Vazamento de memória no serviço de e-mail |
| `adHighCpu` | CPU alta no serviço de anúncios |
| `adManualGc` | Coletas de lixo completas forçadas no serviço de anúncios |
| `adFailure` | Falha do serviço de anúncios |
| `cartFailure` | Falha do serviço de carrinho |
| `paymentFailure` | Falha em n% das cobranças |
| `paymentUnreachable` | Serviço de pagamento indisponível |
| `productCatalogFailure` | Falha do catálogo para um produto específico |
| `recommendationCacheFailure` | Falha no cache do serviço de recomendação |
| `imageSlowLoad` | Imagens lentas no frontend |
| `loadGeneratorFloodHomepage` | Inundação de requisições no frontend |
| `llmRateLimitError` | Erro intermitente de rate limit no LLM |
| `llmInaccurateResponse` | Resposta incorreta do LLM para um produto |

## Como pode ser usado no projeto

- **Requisito de correlação de sinais:** gerar logs, métricas e traces reais de microsserviços para
  desenvolver e testar a parte do Copilot que consulta observabilidade (equivalente ao Datadog/Grafana,
  ELK/OpenSearch e Jaeger da Stratus).
- **Cenários de avaliação com causa conhecida:** ligar uma flag (ex.: `kafkaQueueProblems`), coletar os
  sintomas e verificar se o Copilot chega à causa certa e aos post-mortems parecidos do corpus (ex.: casos de
  fila e backlog da danluu).
- **Proximidade com a Stratus:** microsserviços, Kafka, PostgreSQL, Redis e implantação em Kubernetes.

## Limitações

- Não há dados prontos: é preciso executar o ambiente (Docker, 4 GB+) e gravar a telemetria.
- As falhas são simuladas e de um único aplicativo; não substituem incidentes reais.
- É uma cópia do projeto oficial, com atualizações até 02/2026; para uso prolongado, avaliar usar o
  repositório oficial do OpenTelemetry.
- O `log-generator` adicionado nesta cópia emite, a cada 2–5 segundos e ao acaso, eventos como
  "Database connection failed", "Payment processing failed" e "Slow query detected", **sem relação com
  nenhuma falha real**. Em cenários de avaliação, ele cria sinais falsos; o serviço deve ser desligado
  (removido do `docker-compose.yml`) ao gravar telemetria de teste.
