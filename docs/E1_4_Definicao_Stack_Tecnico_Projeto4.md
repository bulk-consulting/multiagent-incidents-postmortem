# E1.4 — Definição do Stack Técnico

**Projeto 4 — Incident Copilot (Assistente Inteligente de Incidentes e Post-Mortems)**  
**Data:** 28/10/2026  
**Status:** proposta técnica consolidada para planejamento; API pendente de contribuição da Mari  
**Escopo:** decisões de arquitetura e modelagem. **Não foram executados nesta etapa** chunking, geração de embeddings, criação do banco, indexação, benchmark ou implementação dos agentes/API.

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
| API | Contratos e endpoints **pendentes** | **Responsável: Mari** |

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

## 7. Estrutura da API — PENDENTE (Mari)

**Responsável:** Mari. **Status:** aguardando definição e integração ao documento. Esta seção é uma reserva de escopo; **nenhum endpoint, payload, contrato, autenticação ou comportamento foi aprovado aqui**.

Pontos a detalhar pela responsável, em alinhamento com a arquitetura:

- Framework e limites da API; proposta de uso de FastAPI/Pydantic a confirmar.
- Contratos de entrada de incidente e evidências; validações e formato das respostas.
- Identificação e consulta de investigações; envio de evidências adicionais e retomada por identificador.
- Integração com o grafo, tratamento de estados (em andamento, aguardando evidências, concluído, falhou) e erros.
- Segurança, autenticação, limites de acesso e observabilidade da aplicação.

**Não preencher com endpoints inventados sem a contribuição da Mari.**

## 8. Riscos, dependências e validações pendentes

| Item | Risco ou dependência | Próxima verificação |
|---|---|---|
| Extração textual | Perda de cabeçalhos ou dependências entre linhas | Inspecionar amostras reais antes do chunking |
| Fidelidade causal | Hipótese histórica recuperada como se fosse causa provada | Testes com casos de incerteza e referências de origem |
| Multilinguismo | Consulta em português contra texto em inglês | Avaliar buscas nos dois idiomas |
| Modelo de embedding | Acesso/custo ou impossibilidade de enviar dados à API | Confirmar condições de uso; comparar com alternativa local |
| Dimensão do vetor | Divergência entre encoder e schema físico | Escolher esquema compatível com modelo/configuração |
| Persistência | Retomada de fluxo pode repetir operações | Definir checkpoints e idempotência de ações |
| Corpus | Apenas 20 documentos aprovados | Medir cobertura sem confundir similaridade com diagnóstico |
| API | Especificação ainda não recebida | Integrar proposta da Mari |

## 9. Critérios de aceite da E1.4

| Critério | Situação |
|---|---|
| LangGraph vs. CrewAI — decisão justificada | **Proposto / documentado** |
| Chunking — estratégia, parâmetros e plano de validação | **Proposto / documentado** |
| Embeddings — modelo, alternativa e condicionantes | **Provisório / documentado** |
| PostgreSQL + pgvector — modelo lógico e decisões físicas pendentes | **Proposto / documentado** |
| Estrutura da API — contratos e endpoints | **Pendente — Mari** |
| Testes, indexação, integração e implementação | **Fora do escopo desta etapa de planejamento** |

## 10. Referências técnicas para verificação na implementação

- LangGraph — documentação: https://docs.langchain.com/oss/python/langgraph/overview
- LangGraph — persistência: https://docs.langchain.com/oss/python/langgraph/persistence
- LangGraph — interrupções: https://docs.langchain.com/oss/python/langgraph/interrupts
- CrewAI — Flows: https://docs.crewai.com/en/concepts/flows
- pgvector — documentação: https://github.com/pgvector/pgvector
- OpenAI — embeddings: https://platform.openai.com/docs/guides/embeddings
- Hugging Face — multilingual-e5-base: https://huggingface.co/intfloat/multilingual-e5-base

**Conclusão:** a E1.4 estabelece LangGraph como proposta de orquestração, chunking estrutural como estratégia-base, parâmetros iniciais de segmentação e embeddings sujeitos a avaliação, e um modelo lógico PostgreSQL + pgvector para o corpus documental. **A entrega continua parcial até a inclusão da especificação da API pela Mari.** Nenhuma dessas definições equivale a uma implementação já validada.
