# E1.3 — Mapeamento dos Dados
**Projeto 4 — Incident Copilot | Entrega 1.3 | 28/10/2026 | Versão final — caminhos revisados**

> **Escopo:** levantamento, exploração, avaliação de qualidade e seleção das fontes documentais que alimentarão o RAG do MVP. Este documento **não** implementa chunking, embeddings, pgvector, agentes nem API; essas decisões pertencem às etapas seguintes.

**Referência de caminhos:** todos os caminhos de arquivo deste documento são relativos à raiz `~/bulk_projetos/treinamento_dell/`. O documento está em `docs/E1_3_Mapeamento_dos_Dados.md`.

## 1. Objetivo e decisão executiva

O Incident Copilot apoiará a investigação de incidentes de infraestrutura e aplicações usando informações fornecidas pelo usuário ou pelo alerta, complementadas por conhecimento recuperado de incidentes históricos. Para o MVP, foi selecionado um corpus **textual de 20 relatórios públicos de incidentes**, provenientes de publicações originais referenciadas no catálogo `danluu/post-mortems`.

**Decisão E1.3:** os 20 documentos selecionados passaram por extração, revisão de qualidade, comparação com HTML, conferência de proveniência e aprovação editorial humana. **Todos os 20 estão elegíveis** como entrada documental da futura etapa RAG; nenhum índice foi criado. Não está previsto incorporar outros corpora nesta entrega. **Runbooks não foram selecionados para o corpus inicial** e permanecem uma fonte futura prevista na arquitetura.

## 2. Fonte, escopo e metodologia

- **Catálogo de descoberta:** https://github.com/danluu/post-mortems (lista de referências, não repositório de textos completos).
- **Origem dos textos:** páginas públicas das organizações autoras, inclusive capturas do Wayback Machine quando necessário. As URLs de cada documento estão no registro editorial.
- **Ambiente e ferramentas da exploração:** scripts Python no repositório `danluu-ingestion`, coleta de páginas HTTP, preservação de HTML, extração textual com `trafilatura`, metadados em JSON e relatórios/manifestos CSV.
- **Fluxo observado:** descoberta de URLs → coleta → extração → shortlist temática → revisão técnica de 20 documentos → auditoria HTML × texto extraído → registro de ressalvas → aprovação humana → validação de elegibilidade.
- **Critérios de seleção:** fonte rastreável, conteúdo técnico sobre sintomas e impacto, mecanismo causal confirmado ou incerteza expressa, investigação, recuperação e prevenção; diversidade de tecnologias relacionadas a operações cloud, redes, aplicações e sistemas distribuídos.

Os 20 casos foram aprovados em dois lotes por `andre morotti`: 11 em `2026-10-28T13:15:19Z` e 9 em `2026-10-28T13:33:51Z`. Os registros originais permanecem preservados; as aprovações estão centralizadas no CSV editorial.

## 3. Análise exploratória: volume e formatos

| Indicador | Resultado | Origem da evidência |
|---|---:|---|
| Referências processadas | 240 | `datasets/danluu-ingestion/data/reports/summary.json`; `datasets/danluu-ingestion/data/reports/documents.csv` |
| Coletas bem-sucedidas | 224 | `datasets/danluu-ingestion/data/reports/summary.json`; relatório final |
| Falhas de coleta | 14 | idem |
| Itens ignorados conforme política de coleta | 2 | relatório final |
| Textos extraídos | 224 | `datasets/danluu-ingestion/data/reports/summary.json` |
| Candidatos selecionados para curadoria | 20 | registro editorial e corpus selecionado |
| HTMLs originais no corpus final | 20 | `datasets/danluu-ingestion/data/exports/corpus_20_by_stage/raw/` |
| JSONs extraídos no corpus final | 20 | `datasets/danluu-ingestion/data/exports/corpus_20_by_stage/extracted/` |
| Aprovados / pendentes / rejeitados | **20 / 0 / 0** | `datasets/danluu-ingestion/data/reviews/editorial_reviews.csv` |
| Elegíveis ao RAG | **20** | validação editorial |

O corpus final tem **49.721 palavras reportadas nos metadados**, com **mínimo de 1.166**, **mediana de aproximadamente 1.991** e **máximo de 7.429 palavras por documento**. Os 20 textos extraídos somam aproximadamente **310.463 caracteres**. Essas métricas descrevem o texto disponível, não a quantidade futura de chunks ou tokens.

**Formatos e camadas de dados:** as referências de origem são páginas Web; o lote selecionado possui 20 arquivos `text/html` preservados como RAW e 20 JSONs textuais derivados. O CSV editorial complementa os JSONs com decisões de revisão humana e ressalvas. No conjunto de 240 entradas, houve referências a HTML, PDF e tipos não identificados, mas o corpus final selecionado é HTML → JSON.

O arquivo `datasets/danluu-ingestion/data/reports/summary.json` conserva `rag_candidates=0`, campo técnico legado calculado antes do fluxo editorial. **Isso não significa zero documentos aprovados**: a elegibilidade vigente deve ser determinada exclusivamente a partir do CSV editorial validado.

## 4. Estrutura e campos disponíveis

| Camada | Arquivos | Campos / conteúdo relevantes | Papel |
|---|---|---|---|
| HTML original | `datasets/danluu-ingestion/data/raw/DAN-xxx.html` | texto e estrutura da publicação, listas, referências e marcação de imagens | Auditoria e rastreabilidade |
| JSON extraído | `datasets/danluu-ingestion/data/extracted/DAN-xxx.json` | `catalog_id`, `title`, `company`, `category`, `source_url`, `final_url`, `extracted_text`, `word_count`, `content_hash`, `completeness`, `status`, `review_reason`, `extraction_method`, `fetched_at` | Texto de entrada e metadados técnicos |
| Registro editorial | `datasets/danluu-ingestion/data/reviews/editorial_reviews.csv` | 11 campos: `catalog_id`, `company`, `source_url`, `document_type`, `technical_topics`, `causal_status`, `evidence_notes`, `quality_limitations`, `editorial_decision`, `reviewed_by`, `reviewed_at` | **Fonte de verdade** de aprovação, proveniência e ressalvas |
| Inventário geral | `datasets/danluu-ingestion/data/reports/documents.csv` (manifesto fornecido como `documents.csv`) | status de coleta/extração, domínio, `word_count`, alertas técnicos e possíveis duplicatas | EDA do processo de seleção |
| Shortlist | `datasets/danluu-ingestion/data/reports/shortlist_candidates.csv` | tema, mecanismo, evidência da escolha, limitações, justificativa | Histórico da triagem de 15 candidatos adicionais |

A presença de campos `completeness` em um JSON indica **sinalização heurística de seções**, não validação definitiva de exatidão. Os 20 JSONs preservam `editorial_approved=false` como campo legado: **não usar esse atributo para filtrar o corpus aprovado**, pois o controle válido está no CSV de revisão.

## 5. Inventário definitivo dos 20 documentos

| ID | Organização | Tema técnico predominante | Palavras | Situação editorial |
|---|---|---|---:|---|
| DAN-001 | Allegro | Autoscaling, reservas de recursos e picos de tráfego | 2015 | Aprovado |
| DAN-009 | Cloudflare | Autenticação, tokens de serviço e rollout | 2534 | Aprovado |
| DAN-026 | GitHub | DNS, Puppet e dependência circular | 1410 | Aprovado |
| DAN-050 | rust-lang | Deploy, CDN e formação de URLs | 1635 | Aprovado |
| DAN-066 | Cloudflare | Switch, etcd, eleições Raft e falha parcial | 1955 | Aprovado |
| DAN-086 | Azure | Certificados, leap-day e controle de VMs | 3128 | Aprovado |
| DAN-109 | Amazon | DynamoDB, metadados, retries e cascatas | 2181 | Aprovado |
| DAN-115 | Amazon | Kinesis, shards e redistribuição em cascata | 2014 | Aprovado |
| DAN-118 | Atlassian | Exclusão acidental de sites e disaster recovery | 7429 | Aprovado |
| DAN-134 | CircleCI | RabbitMQ, consumidores, retries e quotas de nuvem | 1838 | Aprovado |
| DAN-135 | CircleCI | Kubernetes, kube-proxy e iptables | 1304 | Aprovado |
| DAN-137 | Cloudflare | WAF, regex e consumo de CPU | 4647 | Aprovado |
| DAN-143 | Datadog | systemd-networkd, Cilium e rede Kubernetes | 1939 | Aprovado |
| DAN-164 | Gitlab | PostgreSQL, WAL, replicação, backup e recuperação | 3946 | Aprovado |
| DAN-169 | Google | Quota, Spanner, null pointer e falha global | 2758 | Aprovado |
| DAN-183 | incident.io | Conexões PostgreSQL, Memcached e GKE | 1967 | Aprovado |
| DAN-188 | Joyent | PostgreSQL, autovacuum e locks | 2943 | Aprovado |
| DAN-218 | Slack | Transit Gateway, rede AWS e autoscaling | 1672 | Aprovado |
| DAN-230 | Tarsnap | S3, retries, logs e esgotamento de disco | 1240 | Aprovado |
| DAN-234 | Twilio | Redis, recuperação e inconsistência em cobranças | 1166 | Aprovado |

A seleção **não pretende ser representativa estatisticamente** de todos os incidentes de produção. É uma amostra intencional de diferentes mecanismos de falha para o MVP. A aprovação se refere à **adequação editorial do documento**, não à confirmação irrestrita de todas as hipóteses do relato.

## 6. Qualidade, proveniência e controles editoriais

### 6.1 Validação aplicada

- **Fidelidade:** comparação dos 20 JSONs com os HTMLs disponíveis para localizar perdas textuais, mudanças de estrutura, resíduos de página e referências visuais ausentes.
- **Proveniência:** correspondência de `source_url` em **20/20** registros editoriais com o JSON correspondente; preservação de snapshots históricos e redirecionamentos válidos. Houve correções de URLs no CSV de DAN-066, DAN-115, DAN-137, DAN-169 e DAN-188.
- **Revisão humana:** 20 decisões `approved`, com revisor e timestamp UTC, registradas em dois lotes sem sobrescrever decisões anteriores.
- **Integridade:** HTMLs RAW e JSONs não foram modificados nas rodadas de aprovação; verificações de checksum relatadas pela validação final.
- **Testes:** validação final reportou **62 testes aprovados em 1,42 s**, juntamente com 20 registros únicos, 20 aprovados e 20 elegíveis.

### 6.2 Perfil verificado do registro editorial final

O arquivo `datasets/danluu-ingestion/data/reviews/editorial_reviews.csv` final foi conferido como um **registro único de 20 linhas de dados e 11 colunas**, com **20 IDs distintos**, **20 decisões `approved`**, **nenhum campo editorial vazio**, e o mesmo identificador de revisor (`andre morotti`) em todas as linhas. Os timestamps de aprovação distribuem-se em dois lotes: **11 em `2026-10-28T13:15:19Z`** e **9 em `2026-10-28T13:33:51Z`**.

**Distribuição dos tipos documentais (`document_type`):**

| Tipo registrado | Quantidade |
|---|---:|
| `postmortem` | 10 |
| `incident_report` | 7 |
| `technical_incident_analysis` | 2 |
| `post_incident_review` | 1 |
| **Total** | **20** |

**Distribuição das classificações de causalidade (`causal_status`):**

| Classificação editorial | Quantidade | Interpretação para o MVP |
|---|---:|---|
| `explicit_causal_explanation` | 8 | Relato apresenta explicação causal explícita. |
| `causal_chain_with_contributors` | 7 | Vários mecanismos ou fatores contribuintes devem ser preservados. |
| `causal_uncertainty_preserved` | 2 | Incertezas da investigação não podem ser convertidas em afirmações definitivas. |
| `causal_chain_with_investigative_uncertainty` | 1 | Distinguir hipóteses intermediárias e conclusões posteriores. |
| `explicit_causal_explanation_with_reclassification` | 1 | Manter a correção posterior da terminologia causal. |
| `documented_mechanism_with_external_uncertainty` | 1 | Mecanismo interno documentado; fator externo permanece incerto. |
| **Total** | **20** | |

Os campos `technical_topics`, `evidence_notes` e `quality_limitations` estão preenchidos em todos os registros. `technical_topics` usa termos separados por ponto e vírgula; trata-se de descrição editorial temática, **não de uma taxonomia padronizada e comprovadamente exaustiva**. Os campos `evidence_notes` e `quality_limitations` fornecem contexto para interpretação, mas não substituem o texto original, especialmente quando existem trechos visuais não extraídos.

O CSV é associado aos JSONs por `catalog_id`. A aprovação não deve ser inferida da mera existência do JSON, do status de extração ou de `editorial_approved=false` (legado). A regra vigente de elegibilidade exige simultaneamente **`editorial_decision=approved`**, **`reviewed_by` não vazio** e **`reviewed_at` UTC válido**.

### 6.3 Incerteza causal que deve ser preservada

| Documento | Cuidados documentados |
|---|---|
| DAN-066 | Postscript corrige a classificação inicial *Byzantine fault* para *omission fault*. |
| DAN-169 | Separar o relatório final dos status updates preliminares. |
| DAN-183 | Investigação rica em evidências, mas sem cadeia causal única definitivamente comprovada. |
| DAN-188 | Distinguir hipóteses operacionais iniciais de conclusões posteriores. |
| DAN-218 | Mecanismo interno do Slack bem descrito; não atribuir RCA detalhado ao componente AWS. |
| DAN-230 | Falha interna da Tarsnap documentada; causa subjacente dos erros S3 não confirmada. |
| DAN-109, DAN-115, DAN-137, DAN-164 | Evitar reduzir incidentes multifatoriais a explicações monocausais. |

### 6.4 Limitações de material visual

O texto extraído não representa integralmente gráficos, screenshots e diagramas de **oito documentos**: DAN-001, DAN-009, DAN-026, DAN-118, DAN-134, DAN-135, DAN-137 e DAN-183. A auditoria identificou essas lacunas, **mas não interpretou valores ausentes das figuras**. O sistema não deve alegar que esses dados visuais foram examinados.

### 6.5 Distinção entre alertas técnicos e aprovação

`status=needs_review` ou `review_reason` no JSON (por exemplo, redirecionamento de domínio) é um **sinal do pipeline**, não uma decisão editorial de rejeição. A elegibilidade deve exigir `editorial_decision=approved`, `reviewed_by` preenchido e `reviewed_at` UTC válido no registro editorial. Os campos técnicos legados não devem sobrescrever essa decisão.

## 7. Outras fontes exploradas e justificativa de não inclusão no MVP

A etapa de descoberta avaliou fontes com finalidades e níveis distintos de evidência. **Não selecionar uma fonte nesta versão não significa que ela seja inútil ou incorreta**: a decisão considera principalmente a autenticidade dos incidentes, a integridade do conteúdo, a adequação temática e o esforço de validação exigido. O corpus final permanece restrito aos **20 relatórios públicos selecionados a partir de `danluu/post-mortems`**.

| Fonte e referência | Material encontrado na exploração | Motivo para não incorporar ao RAG inicial | Possível uso posterior |
|---|---|---|---|
| [Incident Post-Mortem Assistant](https://github.com/kai2055/incident-postmortem-assistant) | 20 Markdown com frontmatter YAML e seções padronizadas; catálogo CSV com 15 entradas. | Cinco documentos não constam no catálogo; foram observadas divergências de classificação e durações com definições diferentes. A auditoria estrutural foi positiva, mas **não houve confronto factual integral dos 20 textos com suas fontes primárias**. Embora a avaliação preliminar o considerasse candidato preferencial, optou-se ao final pelo corpus danluu já auditado e aprovado. | Referência de estrutura, testes e eventual expansão após reconciliação de metadados e proveniência. |
| [IncidentDB](https://github.com/trobasuj-cpu/incidentdb) | 448 registros JSONL e 468 Markdown em `rag_vault` no inventário inspecionado. | O código e os registros mostraram configurações, remediações e checklists produzidos por **templates**; há também cortes de atualizações e explicações causais genéricas. A quantidade de registros não compensa o risco de tratar conteúdos derivados como evidência histórica completa. | Testes de parsing ou recuperação de sintomas, mantendo identificação explícita das limitações. |
| [postmortem-intelligence](https://github.com/akashhalgekar/postmortem-intelligence) | CSV principal com 36 registros e script gerador. | Os 36 registros principais são **explicitamente fictícios**; não podem fundamentar afirmações sobre falhas reais de empresas e serviços. | Testes sintéticos de ingestão e avaliação, separados do conhecimento factual. |
| [agent-postmortems](https://github.com/swarmproof/agent-postmortems) | 63 YAML, dos quais 34 classificados como incidentes e 29 como riscos demonstrados (*hazards*). | Foco em falhas, riscos e segurança de **agentes de IA**, não em incidentes de infraestrutura cloud/SRE. A verificação individual das referências não foi realizada na exploração. | Inspiração para metadados de confiança, taxonomia e governança; extensão futura para incidentes envolvendo agentes. |
| [postmortem-templates](https://github.com/dastergon/postmortem-templates) | Sete templates Markdown de post-mortem. | São **modelos vazios**, e não relatos históricos com sintomas, evidências e causas verificáveis. | Padronização documental e referência para campos como gatilho, impacto, detecção, recuperação e prevenção. |
| [OpenTelemetry Demo Dataset](https://github.com/openobserve/opentelemetry-demo-dataset) | Aplicação demonstrativa instrumentada, com microsserviços e 14 flags de falha identificadas no código; README declara logs, métricas e traces. | É um ambiente para **gerar telemetria dinâmica**, não um corpus pré-coletado de post-mortems. A exploração foi estática: execução e entrega dos sinais não foram verificadas. | Cenários de testes controlados de observabilidade, fora da coleção RAG de relatos históricos. |
| [otel-incident-lab](https://github.com/hrmse/otel-incident-lab) | Laboratório local com API FastAPI, instrumentação e runbook de investigação de falha HTTP 503 sintética. | O runbook descreve **um exercício controlado**, não procedimentos comprovados para incidentes reais. A execução e a correlação fim a fim não foram validadas. | Testes de correlação e de resposta a evidências insuficientes, caso o escopo futuro inclua laboratório de telemetria. |
| [OTel Demo Generator](https://apify.com/michiganpublictech/otel-demo-generator) | Serviço anunciado para emissão de logs, métricas e traces sintéticos via OTLP/HTTP, com cenários roteirizados. | Não contém post-mortems históricos. A avaliação examinou a descrição do serviço, **sem executar cenários nem validar os sinais produzidos**; há ainda dependências externas de execução e integração. | Testes opcionais com falhas controladas, após validação técnica e operacional. |

### 7.1 Justificativa da escolha final

O catálogo [danluu/post-mortems](https://github.com/danluu/post-mortems) foi utilizado **como índice de descoberta**; não se presumiu que suas descrições curtas fossem os próprios relatos. A partir dele foram coletadas as publicações originais, preservados os HTMLs, extraídos os textos, selecionados 20 documentos de interesse técnico e conduzidas auditorias de proveniência, qualidade e aprovação humana. Essa cadeia rastreável fundamenta a decisão de usar **apenas esses 20 documentos** na versão inicial.

As fontes de **telemetria sintética**, **templates** e **riscos de agentes** atendem a propósitos diferentes de um corpus factual de post-mortems. Também não foi selecionada nesta E1.3 uma coleção de **runbooks operacionais reais**; o runbook do `otel-incident-lab` é restrito a um cenário de laboratório. A arquitetura pode prever busca de runbooks no futuro, mas não deve apresentá-los como dados já curados ou disponíveis no MVP.

As avaliações dessas alternativas foram majoritariamente exploratórias ou estáticas. Seus volumes e características são aqueles observados/documentados nos relatórios de 27/10/2026, **não métricas de operação nem novas validações independentes realizadas para esta consolidação**.

## 8. Definição dos dados que alimentarão o RAG

**Inclusão no MVP:** exclusivamente os `extracted_text` dos 20 JSONs aprovados localizados em `datasets/danluu-ingestion/data/exports/corpus_20_by_stage/extracted/`, com metadados do documento e seu registro correspondente no **`datasets/danluu-ingestion/data/reviews/editorial_reviews.csv` final**. A seleção é uma junção por `catalog_id` condicionada à elegibilidade editorial, não um filtro pelo campo legado presente nos JSONs. O HTML original é preservado para conferência e eventual reprocessamento, mas não será tratado como uma segunda cópia de conhecimento a indexar.

**Exclusões nesta entrega:** entradas do catálogo não aprovadas, outros repositórios e datasets exploratórios, coleções sintéticas de incidentes, e runbooks ainda não curados. Informações disponíveis apenas em figuras não serão inventadas nem convertidas automaticamente em fatos textuais.

**Relação com o fluxo dos agentes:** o RAG fornecerá **referências históricas** para comparação com sintomas e informações recebidas da ocorrência atual. O relato histórico não constitui prova de que a causa se repete no incidente sob análise. A arquitetura atual não requer integração direta com sistemas de coleta de logs ou métricas; tais dados podem ser informados pelo usuário/alerta.

## 9. Requisitos que a E1.3 entrega à E1.4 (ainda sem implementação)

| Evidência encontrada na E1.3 | Requisito para decisão na E1.4 |
|---|---|
| Seções, timelines, listas e Five Whys | Definir chunking que preserve unidades semânticas e hierarquia de seções. |
| Relatos longos e incidentes com recuperação em fases | Evitar fragmentação que rompa a sequência causal ou temporal. |
| Relatório final e atualizações no mesmo documento (DAN-169) | Representar as duas camadas com metadados distintos. |
| Graus diferentes de certeza causal | Propagar `causal_status`, `evidence_notes` e `quality_limitations` aos metadados recuperáveis. |
| 20 fontes com URLs auditadas | Manter identificador, URL e referência a documento/seção em cada unidade indexada. |
| Corpus pequeno, mas com vocabulário técnico variado | Justificar escolha de embeddings, chunk size, overlap e estratégia de recuperação com teste, não por estimativas assumidas. |
| Fonte de verdade da elegibilidade no CSV | Ingestão futura deve permitir apenas documentos formalmente aprovados, vinculando JSON e CSV por `catalog_id`. |
| Seis classificações causais registradas | Definir se os rótulos serão preservados como metadados descritivos e como evitar que o classificador substitua evidências da fonte. |

A definição de **tamanho de chunk, overlap, modelo de embeddings e esquema de tabelas/índices pgvector** é escopo da E1.4. A E1.3 **não afirma** que tais escolhas foram implementadas, medidas ou validadas.

## 10. Limitações e riscos remanescentes

1. **Escala/cobertura:** 20 publicações são suficientes para iniciar testes do MVP, mas não garantem cobertura ampla de incidentes reais, tecnologias ou serviços específicos.
2. **Fidelidade de mídia:** figuras não interpretadas; referências visuais devem permanecer sinalizadas.
3. **Causalidade:** alguns relatos preservam incerteza genuína, não uma causa raiz única confirmada.
4. **Temporalidade:** relatos de diferentes anos refletem tecnologias e arquiteturas da época; recomendações históricas não são runbooks universalmente seguros.
5. **Direitos de reutilização:** a seleção validou qualidade e proveniência, mas não equivale a uma auditoria jurídica de licenças ou redistribuição de cada publicação.
6. **Avaliação futura:** ainda não existem resultados medidos de Recall@K, MRR, precisão de diagnóstico, latência ou custo de embeddings para esse corpus.

## 11. Critérios de aceite e conclusão

| Critério da entrega 1.3 | Evidência | Status |
|---|---|---|
| Datasets/fonte identificados | Catálogo e URLs individuais | Atendido |
| Volume da coleta e extração medido | `datasets/danluu-ingestion/data/reports/summary.json`, `datasets/danluu-ingestion/data/reports/documents.csv` | Atendido |
| Formato e campos inventariados | HTML, JSON e CSV editorial | Atendido |
| Qualidade e limitações avaliadas | Relatório de revisão e comparação RAW × JSON | Atendido |
| Dados para o RAG definidos | 20 post-mortems aprovados | Atendido |
| Elegibilidade e proveniência verificadas | 20/20, CSV editorial e validação final | Atendido |

**Conclusão:** a E1.3 identifica e valida um conjunto inicial de **20 post-mortems públicos** para alimentar o futuro RAG do Incident Copilot. O conjunto está qualificado editorialmente, com limitações técnicas e causais documentadas, e fornece os requisitos para as decisões de chunking, embeddings e modelo pgvector na E1.4. Não foi executado chunking, embedding ou indexação nesta entrega.

## 12. Evidências e artefatos de referência

| Artefato | Finalidade |
|---|---|
| `datasets/danluu-ingestion/data/exports/corpus_20_by_stage/extracted/` | 20 JSONs do corpus RAG aprovado (entrada planejada para a E1.4) |
| `datasets/danluu-ingestion/data/exports/corpus_20_by_stage/raw/` | 20 HTMLs do corpus aprovado, para auditoria |
| `datasets/danluu-ingestion/data/reviews/editorial_reviews.csv` | **Fonte de verdade:** 20 decisões, origem, temas, notas de evidência, classificação de causalidade, limitações e auditoria humana |
| `datasets/danluu-ingestion/data/reports/e13_final_validation.md` | Critérios e resultados finais da curadoria |
| `datasets/danluu-ingestion/data/reports/editorial_review_report.md` | Parecer técnico individual de cada candidato; recomendações anteriores à aprovação |
| `datasets/danluu-ingestion/data/reports/summary.json` | Métricas agregadas da coleta/extração; campos legados |
| `datasets/danluu-ingestion/data/reports/documents.csv` | Inventário dos 240 registros |
| `datasets/danluu-ingestion/data/reports/shortlist_candidates.csv` | Triagem de 15 candidatos adicionais |
| `datasets/danluu-ingestion/data/raw/DAN-xxx.html` | Fonte HTML local para auditoria da coleta completa |
| `datasets/danluu-ingestion/data/extracted/DAN-xxx.json` | Conteúdo textual da coleta completa e metadados técnicos |
| `datasets/danluu-ingestion/tests/test_reviews.py` | Testes de validação editorial e elegibilidade |
| Relatórios exploratórios de fontes alternativas (arquivos `.docx` citados na análise anterior) | **Não constam na árvore atual do projeto**; confirmar sua existência no backup antes de apresentá-los como artefatos disponíveis. A síntese das alternativas permanece na seção 7. |

> **Observação de rastreabilidade:** os caminhos informados são relativos à raiz `~/bulk_projetos/treinamento_dell/`, conforme a árvore `estrutura_projeto_atual.txt` enviada em 28/10/2026. O registro editorial vigente é `datasets/danluu-ingestion/data/reviews/editorial_reviews.csv`; não usar backups ou nomes temporários de uploads como referência. A verificação desta revisão foi **estrutural (nomes e caminhos)**, com base na árvore enviada, e não incluiu abertura local dos arquivos do WSL, reexecução de testes ou comparação de hashes.
