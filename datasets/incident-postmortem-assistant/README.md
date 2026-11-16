# Avaliação — incident-postmortem-assistant

Avaliação feita em 30/10/2026 do repositório
[kai2055/incident-postmortem-assistant](https://github.com/kai2055/incident-postmortem-assistant),
commit `d9e70a5b802faf5c693e709f1a97c9b78bbd0a24` (02/10/2026).

## Veredito

**Não usar os 20 documentos do corpus como fonte do RAG.** São reescritas de post-mortems feitas por LLM,
13 delas de incidentes que já temos no texto original pela danluu, e a rastreabilidade da fonte é incompleta.

**Aproveitar duas coisas do repositório:** os conjuntos de teste de busca (`data/eval/`) e as decisões de
arquitetura (`decisions/`).

## O que é o repositório

Um projeto completo de assistente de post-mortems (RAG, agente de diagnóstico, avaliação e interface),
muito parecido com o Incident Copilot. Não é um dataset; o corpus é uma parte pequena dele.

| Item | Valor |
|---|---|
| Documentos do corpus | 20 arquivos Markdown em `corpus/raw/`, ~19 mil palavras no total (~1.000 por documento) |
| Formato | YAML (empresa, data, severidade, duração, serviços afetados, categoria de causa) + 5 seções fixas: Summary, Timeline, Root Cause, Resolution, Prevention |
| Como foi feito | Reescrito por LLM (Claude) a partir do post-mortem original, com verificação contra a fonte (ADR-010) |
| Índice de fontes | `data/incidents.csv`, com 15 entradas |
| Licença | O repositório não tem arquivo de licença; uso interno, com citação |

## O que foi conferido

### Fidelidade ao original

Dois documentos cobrem incidentes cujo texto original temos pela danluu e foram comparados fato a fato.
Foram verificados 2 dos 20 documentos.

- **Cloudflare, 18/11/2025 (DAN-011):** todos os horários e números técnicos batem (limite de 200
  features, uso de ~60, geração a cada 5 minutos, ClickHouse, banco `r0`, "pior outage desde 2019"). Mas o
  resumo afirma que Spotify, ChatGPT, X e Canva ficaram fora do ar, e **isso não está no post-mortem da
  Cloudflare**. A informação veio de fora da fonte, contrariando a regra do próprio projeto (ADR-010).
- **Roblox, 2021 (DAN-211):** os números batem com o original.

A reescrita é boa, mas não é o texto original, e pelo menos um caso inclui informação externa.

### Rastreabilidade da fonte

O link do post-mortem original não fica no documento (o YAML não tem campo de URL), só no índice
`data/incidents.csv`, e esse índice está incompleto:

- **5 dos 20 documentos não têm entrada no índice**, então não há link de fonte em lugar nenhum do
  repositório: `circleci-waf-2025-04-04`, `cloudflare-route-leak-2026-01-22`, `codecov-2021-04-01`,
  `github-auditlog-2026-04-01` e `github-pages-dns-2026-04-13`.
- **1 link está errado:** o de `cloudflare-2025-11-18` aponta para `...november-14th-2025`, que não é o
  post-mortem real (`https://blog.cloudflare.com/18-november-2025-outage/`).

Isso afeta diretamente o requisito do Incident Copilot de citar a fonte original.

### Sobreposição com a danluu

**13 dos 20 incidentes estão na danluu.** Em 12 deles temos o texto original extraído. A exceção é
`sentry-postgres-2015-07-20` (DAN-214): na danluu a coleta falhou (HTTP 404), então a reescrita desta
fonte é a única versão que temos.

Os **7 incidentes que só existem aqui**:

| Incidente | Tipo |
|---|---|
| Cloudflare / Verizon BGP, 2019 | Operação (vazamento de rota) |
| GitHub DNS no Pages, 2026 | Operação |
| GitHub audit log, 2026 | Operação |
| GitHub autenticação, 2026 | Operação (só status page, sem post-mortem completo) |
| Codecov, 2021 | Segurança / cadeia de suprimentos |
| TanStack npm, 2026 | Segurança / cadeia de suprimentos |
| Cloudflare Thanksgiving, 2023 | Segurança (credenciais roubadas) |

A correspondência dos 20 documentos com a danluu está em `mapeamento_corpus.csv`.

## O que vale aproveitar

**Conjuntos de teste** (o melhor ativo do repositório):

- `data/eval/layer2_suite.json`: 15 descrições de incidente em linguagem de sintoma, cada uma com o
  documento esperado. Exemplo: "colocamos uma regra nova no filtro de tráfego, os servidores bateram 100%
  de CPU e tudo começou a dar erro" → Cloudflare WAF 2019. É o formato de entrada do Incident Copilot.
- `data/eval/query_suite.json`: 39 perguntas com o documento e a seção esperados.

Como a maioria dos incidentes também está na danluu, dá para adaptar esses testes ao nosso corpus,
trocando o `doc_id` desta fonte pelo `id_danluu` de `mapeamento_corpus.csv`.

**Decisões de arquitetura** (`decisions/`): chunking, limite de relevância, citação numerada e "recusa
honesta" quando não há evidência suficiente. Referência para a E1.4.

**Taxonomia de causa** (`corpus/README.md`): 9 categorias com a regra "classificar pela origem, não pelo
efeito". Pode servir de base para o campo de categoria do nosso corpus.

## Encaminhamentos

1. Não indexar os documentos de `corpus/raw/`.
2. Para os 7 incidentes exclusivos: buscar os post-mortems originais e incluí-los na coleta. Quatro são de
   operação; os três de segurança dependem da decisão do time sobre esse tipo de incidente.
3. Para o Sentry 2015: tentar o original por outra via (ex.: web.archive.org); se não houver, decidir se a
   reescrita entra com marcação de "texto secundário".
4. Adaptar `layer2_suite.json` e `query_suite.json` como base da avaliação de busca.

## Limitações desta avaliação

- A fidelidade foi verificada em 2 dos 20 documentos.
- A sobreposição com a danluu foi feita pelo link de cada post-mortem; para `github-dns-2024-10-11` a
  correspondência é com o relatório mensal de outubro de 2024 do GitHub (DAN-162), não com um post-mortem
  dedicado.
- O código do projeto (pipeline, agente, interface) não foi avaliado; só o corpus e os dados de avaliação.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `README.md` | Este documento |
| `mapeamento_corpus.csv` | Os 20 documentos: empresa, data, categoria de causa, palavras, link de fonte no índice, ID correspondente na danluu, se é exclusivo desta fonte e observações |
| `snapshot/` | Cópia do repositório no commit avaliado (sem `.git` e imagens). Ver `snapshot/PROVENIENCIA.md`. **Não indexar `corpus/raw/`.** |
