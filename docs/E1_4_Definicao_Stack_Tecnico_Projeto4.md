# E1.4 — Definição do Stack Técnico

**Projeto 4 — Incident Copilot (Assistente Inteligente de Incidentes e Post-Mortems)**  

## 1. Objetivo e contexto

Definir o stack do MVP para recuperar conhecimento de incidentes históricos, apoiar a análise de ocorrências atuais e permitir investigação controlada, rastreável e retomável. O conhecimento documental do MVP é composto exclusivamente por **20 post-mortems aprovados na E1.3**, provenientes de publicações originais identificadas pelo catálogo `danluu/post-mortems`.

O sistema recebe a descrição do incidente e evidências fornecidas pelo usuário/alerta. No MVP **não existe integração obrigatória com observabilidade em tempo real**, e **runbooks ainda não foram curados** para o RAG. Trechos históricos são evidências de casos anteriores, **não prova automática da causa do incidente atual**.

**Referências locais (relativas à raiz `~/bulk_projetos/treinamento_dell/`):**

- Documento-base: `docs/E1_3_Mapeamento_dos_Dados.md`.
- Corpus selecionado: `datasets/danluu-ingestion/data/exports/corpus_20_by_stage/extracted/` (20 JSONs) e `datasets/danluu-ingestion/data/exports/corpus_20_by_stage/raw/` (20 HTMLs).
- Aprovação editorial: `datasets/danluu-ingestion/data/reviews/editorial_reviews.csv`.
- Manifesto e relatórios: `datasets/danluu-ingestion/data/reports/`.

O filtro de elegibilidade consulta o registro editorial, associado ao JSON por `catalog_id`, e requer `editorial_decision=approved`, `reviewed_by` preenchido e `reviewed_at` UTC válido. Campos legados como `editorial_approved=false` nos JSONs ou `rag_candidates=0` no resumo **não substituem** o registro editorial.

## 2. Resumo executivo das decisões

| Área | Decisão / proposta | Maturidade |
|---|---|---|
| Orquestração | **LangGraph**; workflow explícito com estado, transições condicionais e pausa/retomada | Escolha arquitetural |
| Organização de agentes | **Dois agentes especializados:** Pesquisador RAG e Analista; síntese de entrada por LLM não autônomo | Escolha arquitetural |
| Chunking | **Hierárquico/estrutural**, priorizando seções e unidades semânticas; fallback recursivo por tokens | Estratégia proposta |
| Parâmetros iniciais | **400 tokens**, **60 tokens de overlap** quando subdividir blocos longos | Hipótese a testar |
| Embeddings | **`text-embedding-3-small`**, dimensão padrão **1.536**; alternativa local **`multilingual-e5-base`**, 768 dimensões | Provisório; sujeito a acesso/custo/avaliação |
| Armazenamento | **PostgreSQL + pgvector** | Escolha arquitetural |
| Modelo lógico de RAG | `documents` → `chunks` → `chunk_embeddings` | Proposta, não DDL final |
| Recuperação | Busca por similaridade cosseno; começar por busca vetorial exata | Proposta de baseline |
| API | **FastAPI + Pydantic**; endpoints de incidentes, complementos e webhook de alertas; deduplicação de entradas | Proposta inicial (Mari) |

## 3. Orquestração: LangGraph versus CrewAI

### 3.1 Requisitos do fluxo

1. Receber descrição do incidente e evidências disponíveis.
2. Estruturar a entrada por uma **chamada LLM comum**, sem convertê-la em agente autônomo.
3. Acionar o **Agente 1 — Pesquisador RAG**, que recupera e, quando necessário, refina referências a post-mortems históricos.
4. Passar por um **supervisor/roteador**, que avalia suficiência e seleciona somente transições autorizadas.
5. Prosseguir ao **Agente 2 — Analista**, responsável por hipóteses, diagnósticos preliminares, evidências favoráveis/contrárias, incertezas e recomendações.
6. Quando faltarem evidências atuais, solicitar informações adicionais e permitir a **retomada da investigação** com estado persistente.
7. Produzir relatório estruturado, com origem das evidências e distinção entre hipótese e confirmação.

O supervisor é uma **função/nó lógico de decisão**, não um terceiro agente especializado obrigatório. Sua decisão pode ser apoiada por LLM, mas o sistema valida o resultado e impõe limites operacionais.

### 3.2 Comparativo

| Critério | LangGraph | CrewAI |
|---|---|---|
| Workflows definidos | Grafos de nós/arestas, inclusive condicionais | Flows com roteadores e listeners |
| Estado e retomada | Estado tipado, checkpointers, interrupção e retomada | Estado e persistência de Flows |
| Iteração RAG controlada | Loop explícito no grafo com limite de tentativas | Também viável por roteamento no Flow |
| Agentes especializados | Agentes podem ser encapsulados em nós | Abstração de crews/agentes e tarefas |
| Adequação à arquitetura adotada | Correspondência direta com o fluxo de estados e transições | Alternativa válida, com maior ênfase em abstrações de equipes |

**Decisão:** adotar **LangGraph**, principalmente pela clareza para representar o processo de investigação como estados, nós, bifurcações e pontos de interrupção. **CrewAI não foi descartado por falta de funcionalidades**; seus Flows oferecem alternativas para esses requisitos. A escolha é de adequação e legibilidade arquitetural, não resultado de benchmark comparativo.

### 3.3 Transições controladas

- `REFINE_SEARCH`: voltar ao pesquisador RAG, com limite de tentativas.
- `REQUEST_EVIDENCE`: interromper o fluxo, solicitar novos dados do incidente atual e aguardar retomada.
- `PROCEED`: avançar à análise com evidências disponíveis.

**Restrições:** nenhuma execução arbitrária de ferramentas, nenhum loop ilimitado, nenhuma conclusão causal categórica sem evidência suficiente. O plano de persistência deverá especificar identificador de investigação e cuidados contra repetição de efeitos colaterais na retomada. O mecanismo concreto de checkpoint ainda não foi configurado.

## 4. Estratégia de chunking

### 4.1 Justificativa

Os 20 relatos aprovados têm comprimentos e formatos variados, incluindo timelines, listas, etapas de recuperação, análises de causa raiz, hipóteses preliminares posteriormente revisadas e informações apenas visuais não extraídas. Divisões de tamanho fixo podem romper a sequência temporal ou uma cadeia causal. O chunking semântico automático isolado também não garante respeitar cabeçalhos e a relação entre evidência e conclusão.

**Proposta:** chunking **hierárquico orientado à estrutura**, com divisões adicionais por tokens somente quando a unidade estrutural exceder o orçamento.

### 4.2 Processo lógico proposto

1. Ler apenas os 20 JSONs do corpus aprovado e validar a correspondência com `editorial_reviews.csv` por `catalog_id`.
2. Identificar unidades efetivamente presentes em `extracted_text`: títulos, seções, parágrafos, itens, timelines e sequências causais. **Não presumir Markdown ou cabeçalhos intactos:** a fonte é texto extraído de HTML.
3. Manter juntas unidades curtas com sentido próprio, sem forçar preenchimento exato do limite.
4. Subdividir unidades longas em fronteiras naturais, usando segmentação recursiva e overlap controlado.
5. Registrar origem, seção, ordem, offsets, versão do chunking e referência ao documento-pai.
6. Preservar seções com hipóteses descartadas, atualizações preliminares ou correções posteriores, sem transformar essas passagens em conclusões confirmadas.

**Parâmetros candidatos para avaliação:**

| Configuração | Máximo nominal | Overlap nominal | Finalidade |
|---|---:|---:|---|
| A | 250 tokens | 40 tokens | Recuperação mais granular |
| **B — baseline proposta** | **400 tokens** | **60 tokens** | Equilíbrio inicial entre detalhe e contexto |
| C | 700 tokens | 100 tokens | Contexto mais longo; verificar limites do encoder |

Overlap não é obrigatório entre seções independentes; deve ser aplicado sobretudo a subdivisões internas. O limite é em **tokens do tokenizer compatível com o modelo**, não caracteres ou palavras. Os números acima **não foram testados neste corpus**.

### 4.3 Rastreabilidade e qualidade

Cada chunk deverá preservar pelo menos: `catalog_id`, `chunk_id`, `chunk_index`, `section_title` quando identificável, `start_offset`, `end_offset`, `token_count`, `source_url`, `chunking_version` e vínculo ao documento-pai. `technical_topics`, `causal_status`, `evidence_notes` e `quality_limitations` são metadados documentais provenientes do CSV editorial; sua propagação não implica que *cada trecho* possua o mesmo grau de certeza causal do documento completo.

O RAG recuperará somente o texto do corpus e a proveniência associada. **HTML não será indexado como segunda cópia**; ele fica preservado para auditoria e possível reprocessamento. Elementos visuais não extraídos não podem ser inferidos como fatos.

## 5. Estratégia de embeddings

### 5.1 Critérios

- Adequação a vocabulário técnico de cloud, Kubernetes, redes e bancos de dados.
- Consultas em português contra documentos predominantemente em inglês.
- Custo, disponibilidade de API, requisitos de execução local e privacidade.
- Compatibilidade com PostgreSQL/pgvector e com o orçamento de tokens do encoder.
- Capacidade de versionamento, avaliação e regeneração segura dos vetores.

### 5.2 Modelos considerados

| Modelo | Modo | Dimensões típicas | Considerações |
|---|---|---:|---|
| **`text-embedding-3-small`** | API OpenAI | **1.536** (padrão) | Integração simples; depende de acesso/credenciais, custo e autorização de envio dos textos à API |
| **`multilingual-e5-base`** | Execução local | **768** | Alternativa multilíngue aberta; requer prefixos `query:`/`passage:` e respeitar limite de entrada de 512 tokens |

**Escolha provisória:** `text-embedding-3-small`, condicionada à disponibilidade/autorização. O modelo de embeddings é **independente** do LLM que executará síntese e análise. Se os recursos da API não estiverem disponíveis, avaliar `multilingual-e5-base` e ajustar os limites de segmentação. Em especial, a configuração de **700 tokens não é diretamente compatível** com um encoder limitado a 512 tokens, sem tratamento adicional.

### 5.3 Consulta e avaliação futura

Vetorização das consultas com o **mesmo modelo e configuração** usados nos documentos; similaridade por cosseno como baseline. A proposta de avaliação é preparar questões com trechos relevantes previamente identificados (ground truth), cobrindo acertos temáticos e casos de incerteza causal, e comparar as configurações por **Recall@5**, **MRR**, preservação de contexto, latência e custo. **Não existem métricas medidas nesta fase.**

## 6. Modelo lógico de dados: PostgreSQL + pgvector

### 6.1 Entidades propostas

```text
documents (1) ─── (N) chunks (1) ─── (N) chunk_embeddings
```

**`documents`**: uma linha por post-mortem curado. Campos principais: `id` (UUID, PK), `catalog_id` (único), `title`, `company`, `source_url`, `technical_topics`, `causal_status`, `evidence_notes`, `quality_limitations`, `editorial_decision`, `reviewed_by`, `reviewed_at`, hash/versão da fonte. A importação deve preservar evidência de proveniência e não deduzir aprovação a partir de flags legadas.

**`chunks`**: uma linha por fragmento de texto, com `id` (UUID, PK), `document_id` (FK), `chunk_index`, `content`, `section_title` quando disponível, offsets, `token_count`, `chunking_version` e hash do conteúdo. É importante impedir duplicações por documento e versão de processamento.

**`chunk_embeddings`**: uma linha por representação vetorial de chunk e modelo/configuração, com `id` (UUID, PK), `chunk_id` (FK), `model_name`, `model_version/configuration`, `dimensions`, `embedding` e referência ao hash do chunk. Unicidade por chunk/modelo/configuração, para permitir reprocessamento e comparação.

### 6.2 Decisões e ressalvas

- **Separar embeddings de chunks** permite trocar modelo sem duplicar os textos nem perder rastreabilidade. Isso custa um JOIN adicional, aceitável como proposta lógica para corpus pequeno.
- Com `text-embedding-3-small` na dimensão padrão, uma coluna `vector(1536)` é adequada **para aquela configuração**. Um modelo com **768 dimensões** não cabe nessa mesma tipagem; para suportar tamanhos heterogêneos, definir tabelas/colunas por dimensão ou solução com `vector` sem dimensão fixa e restrições/índices adequados. **A estratégia física final permanece em aberto** até escolher os modelos reais.
- **Busca exata por similaridade cosseno** é o baseline proposto. Considerar HNSW/IVFFlat somente após verificar contagem de chunks, volume, performance e necessidade; não há benchmark ou índice criado.
- Aplicar chave estrangeira, unicidade e validação de elegibilidade editorial na ingestão; tratar atualizações de chunking/modelo com versionamento e possibilidade de reindexação.
- O modelo acima cobre o **repositório documental RAG**, não o estado dos incidentes atuais, sessões, registros de interação ou checkpoints do LangGraph. Essas estruturas serão definidas em design próprio, conforme necessidade do workflow e da API.

**Estado:** modelo **lógico** proposto; sem DDL físico aprovado, sem banco criado e sem carga executada.

## 7. Estrutura da API

### 7.1 Papel da API e organização em camadas

A API, em **FastAPI + Pydantic**, é a porta de entrada do sistema: recebe incidentes, alertas e complementos, valida a entrada e encaminha para a camada de serviços. **A API não executa lógica de investigação**: não chama LLM, não consulta o pgvector e não decide transições do grafo.

Regra de organização: **cada camada só conversa com a camada vizinha**: `api` → `services` → `agents` / `db`. 

### 7.2 Estrutura de pastas proposta

```text
app/
  main.py               # cria a aplicação FastAPI e registra os routers
  api/                  # routers FastAPI (somente entrada/saída HTTP)
    incidents.py        # criação, consulta e complementos de incidentes
    webhooks.py         # recebimento de alertas do sistema de alertas
  schemas/              # modelos/classes Pydantic de entrada e saída
  services/             # lógica de aplicação
    incident_service.py # validação e envio de incidentes aos agentes
    alert_service.py    # validação e envio dos alertas aos agentes
    dedup.py            # detecção de incidentes/alertas repetidos
  agents/               # grafo LangGraph: Agente 1 (RAG), Agente 2 (análise)
  core/                 # configuração, logging
```

### 7.3 Endpoints

Todos sob o prefixo `/api/v1`.

**Incidentes (usuário / interface web):**

| Método | Rota | Função | Resposta |
|---|---|---|---|
| `POST` | `/incidents` | Cria nova investigação e inicia o grafo | `202` com `incident_id` e `status` |
| `GET` | `/incidents/{incident_id}` | Consulta estado, perguntas pendentes e relatório (quando houver) | `200` / `404` |
| `POST` | `/incidents/{incident_id}` | Envia complemento: novas evidências ou pedido de refinamento; retoma a investigação | `202` / `404` |

Como a investigação pode levar tempo, os `POST` respondem imediatamente com `202` e a interface consulta o progresso via `GET /incidents/{incident_id}` (polling). O `incident_id` é usado como identificador da execução no grafo, permitindo pausar e retomar a mesma investigação.

**Webhooks (sistema de alertas):**

| Método | Rota | Função | Resposta |
|---|---|---|---|
| `POST` | `/webhooks/alerts` | Recebe alerta em formato genérico; abre nova investigação ou associa a uma investigação existente | `202` com `incident_id` |

Comportamento do webhook:

- Alerta **novo** → cria investigação, como `POST /incidents`.
- Alerta **repetido** de um incidente ainda aberto → não cria nova investigação; retorna o `incident_id` existente (ver 7.4).
- O sistema de alertas não aguarda o resultado da investigação; a resposta `202` apenas confirma o recebimento.

### 7.4 Validações

- **Entrada:** as classes Pydantic validam campos obrigatórios, tipos e tamanhos máximos (descrição, evidências, payload de alerta). Entradas inválidas retornam `422`.
- **Duplicidade:** o sistema não deve abrir várias investigações para o **mesmo incidente**, evitando tráfego e custo de LLM desnecessários. Para cada entrada é calculada uma impressão digital (*fingerprint*):
  - **alertas:** origem + identificador/fingerprint do alerta enviado pela ferramenta;
  - **incidentes manuais:** hash do conteúdo normalizado (título, descrição e evidências).

  Se já existir investigação **aberta** com o mesmo fingerprint, a API retorna o `incident_id` existente em vez de criar outro. A janela de tempo considerada para a duplicidade é um parâmetro a definir na implementação.

### 7.5 Observabilidade e segurança (MVP)

Por se tratar de um MVP, a proposta é manter o mínimo necessário:

- Token simples em header para o endpoint de webhook, para que apenas o sistema de alertas configurado consiga enviar alertas.
- Logs com `incident_id` em todas as etapas, para rastrear a investigação do início ao fim.

Autenticação de usuários e controle de acesso por perfil ficam fora do escopo do MVP.

**Conclusão:** a E1.4 estabelece LangGraph como proposta de orquestração, chunking estrutural como estratégia-base, parâmetros iniciais de segmentação e embeddings sujeitos a avaliação, e um modelo lógico PostgreSQL + pgvector para o corpus documental, além de uma estrutura de API em FastAPI com endpoints para incidentes, complementos e alertas. Nenhuma dessas definições equivale a uma implementação já validada.
