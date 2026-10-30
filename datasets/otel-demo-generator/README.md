# Avaliação — otel-demo-generator (Apify)

Avaliação feita em 30/10/2026 a partir da página do Actor
[michiganpublictech/otel-demo-generator](https://apify.com/michiganpublictech/otel-demo-generator)
(última modificação registrada: 13/10/2026). O código não é público; tudo abaixo vem da página.

## Veredito

**Não entra no RAG de post-mortems.** É um serviço pago que **gera telemetria sintética modelada** (não
captura de software em execução) e a envia para um backend de observabilidade.

**Uso opcional e secundário** para cenários de avaliação com causa conhecida. Para o requisito de
correlação de observabilidade, o **OpenTelemetry Demo** (`../opentelemetry-demo-dataset/`) é preferível:
é software real rodando, gratuito e local.

## O que é

| Item | Valor |
|---|---|
| Tipo | Actor da plataforma Apify (serviço executado na nuvem da Apify) |
| O que gera | Traces, métricas e logs OpenTelemetry correlacionados (`trace_id`/`span_id` nos logs) de um sistema de microsserviços simulado |
| Formato de saída | Envio OTLP/HTTP (protobuf ou JSON, gzip) para um backend; resumo da execução no dataset da Apify; em modo de teste (`dryRun`), amostras `SAMPLE_TRACES.json`, `SAMPLE_METRICS.json` e `SAMPLE_LOGS.json` |
| Topologias | E-commerce (padrão), fintech, SaaS e logística |
| Duração por execução | 1 a 120 minutos; modo ao vivo ou retroativo (`backfill`) |
| Dados | Sintéticos, marcados com `app.synthetic = true`; IPs de faixas de documentação e hosts `.example` |
| Preço | US$ 0,02 por minuto de telemetria aceito pelo backend (15 min = US$ 0,30; 120 min = US$ 2,40); execuções de teste (`dryRun`) gratuitas |
| Autor | Justin Hagerty (mantido pela comunidade) |
| Uso registrado na página | 2 usuários, 18 execuções, nenhuma avaliação |
| Licença | Não informada; vale o termo de uso da Apify |

## Cenários de incidente (9)

| Cenário | Causa simulada |
|---|---|
| `healthy-baseline` | Sem incidente (~0,5% de erros) |
| `checkout-latency-incident` | Provedor de pagamento externo ~10x mais lento, com timeouts e retries |
| `bad-deployment-rollback` | Nova versão do serviço de carrinho piora erros e latência, depois é revertida |
| `database-slow-queries` | Migração remove um índice; uma query fica 20–50x mais lenta e satura o pool de conexões |
| `memory-leak-oom` | Heap da JVM cresce até OOMKilled e reinícios; correção depois |
| `cache-stampede` | Redis esvaziado; taxa de acerto despenca e o banco é sobrecarregado |
| `third-party-outage` | Transportadora externa responde 503; circuit breaker abre e fallbacks são servidos |
| `traffic-surge` | Pico de 4–5x de tráfego; autoscaler adiciona pods e o lag do Kafka sobe |
| `security-anomaly` | Credential stuffing: muitos 401 de poucos IPs, seguidos de 429 |

## Pontos fortes

- Cenários com **causa raiz conhecida** que correspondem a padrões frequentes nos post-mortems reais da
  danluu (índice removido, cache esvaziado, vazamento de memória, deploy ruim, dependência externa, pico de
  tráfego).
- Sinais correlacionados entre logs, métricas e traces, com início, duração e severidade do incidente
  configuráveis e `seed` para repetir a geração.
- O modo `dryRun` gera amostras em JSON sem custo e sem precisar de backend.

## Limitações

- **Telemetria modelada, não capturada:** os sinais tendem a ser mais "limpos" que os de um incidente real.
- **Só envia para endpoints públicos** (bloqueia endereços privados e locais) e só por OTLP/HTTP. Um backend
  interno teria de ser exposto publicamente para receber os dados ao vivo.
- **Dependência de um serviço pago de terceiro**, sem código aberto e com pouquíssimo uso registrado.
- Exportação de métricas a cada minuto; retroativo limitado a 120 minutos.

## Como poderia ser usado no projeto

- Se for preciso, gerar amostras gratuitas (`dryRun`) dos 9 cenários e usá-las como **casos de teste
  rotulados** do diagnóstico: entrada = sintomas extraídos da telemetria; resposta esperada = causa do
  cenário e post-mortems parecidos do corpus.
- Para desenvolvimento contínuo da correlação, usar o OpenTelemetry Demo, que roda localmente e de graça.
