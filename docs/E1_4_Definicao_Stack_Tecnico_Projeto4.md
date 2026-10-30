# E1.4 — Definição do Stack Técnico

**Projeto 4 — Incident Copilot (Assistente Inteligente de Incidentes e Post-Mortems)**  

## 1. Contexto

Este documento define o stack do MVP do Incident Copilot. A base de conhecimento do RAG é formada pelos datasets `danluu-ingestion` e `incident-postmortem-assistant`, definidos em [E1_3_Mapeamento_dos_Dados.md](E1_3_Mapeamento_dos_Dados.md).

## 2. Resumo das decisões

| Área | Decisão |
|---|---|
| Orquestração | **LangGraph** |
| Chunking | Por **seção**, com divisão adicional de **trechos** longos (máximo de 400 tokens e overlap de 60) |
| Embeddings | **`multilingual-e5-base`**, 768 dimensões |
| Armazenamento | **PostgreSQL + pgvector**, com as tabelas `documents` e `chunks` |
| Recuperação | Busca semântica no pgvector, que encontra os trechos com significado mais próximo da consulta |
| API | **FastAPI + Pydantic**, com endpoints de incidentes, complementos e alertas |

## 3. Orquestração: LangGraph versus CrewAI

**Decisão:** adotar **LangGraph**, principalmente pela **clareza para representar o processo de investigação**. No Incident Copilot, depois de analisar as evidências, o sistema pode gerar o relatório, voltar ao Agente 1 para refinar a busca ou pausar para pedir informações ao analista. No LangGraph, cada etapa é desenhada como um nó e cada decisão como um caminho entre os nós, o que corresponde diretamente a esse fluxo. Ele também salva o estado da investigação, permitindo pausar e retomar o mesmo `incident_id`.

O CrewAI também atenderia a esses requisitos, mas é mais centrado em equipes de agentes e tarefas. **Como nosso fluxo tem caminhos bem definidos, o LangGraph é a opção mais adequada.**

| Critério | LangGraph | CrewAI |
|---|---|---|
| Workflows definidos | Grafos de nós/arestas, inclusive condicionais | Flows com roteadores e listeners |
| Estado e retomada | Estado tipado, checkpointers, interrupção e retomada | Estado e persistência de Flows |
| Iteração RAG controlada | Loop explícito no grafo com limite de tentativas | Também viável por roteamento no Flow |
| Agentes especializados | Agentes podem ser encapsulados em nós | Abstração de crews/agentes e tarefas |
| Adequação à arquitetura adotada | Correspondência direta com o fluxo de estados e transições | Alternativa válida, com maior ênfase em abstrações de equipes |

## 4. Estratégia de chunking

O chunking seguirá a estrutura de cada dataset, para manter juntas as informações de uma mesma seção:

| Dataset | Regra |
|---|---|
| `incident-postmortem-assistant` | Dividir pelas cinco **seções** fixas: Summary, Timeline, Root Cause, Resolution e Prevention |
| `danluu-ingestion` | Dividir pelos **títulos** do texto; quando não houver títulos, dividir por **tamanho** |

Os trechos com mais de 400 tokens serão subdivididos, com overlap de 60 tokens. Esses valores são iniciais e poderão ser ajustados nos testes de recuperação.

## 5. Estratégia de embedding

O modelo escolhido é o **`multilingual-e5-base`**, pelos seguintes motivos:

- É executado localmente, sem custo por uso e sem chave de API.
- É multilíngue, o que permite consultas em português sobre documentos em inglês.
- Gera vetores de 768 dimensões e aceita até 512 tokens, acima do limite de 400 definido para os chunks.

O mesmo modelo será usado para gerar os vetores dos documentos e das consultas.

## 6. Modelo de dados do pgvector

```text
documents (1) ─── (N) chunks
```

**`documents`**: uma linha por documento.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | UUID, PK | Identificador interno |
| `dataset` | TEXT | Dataset de origem |
| `source_id` | TEXT | `catalog_id` ou `id` do dataset de origem |
| `title` | TEXT | Título |
| `company` | TEXT | Empresa |
| `url` | TEXT | Link da fonte |
| `incident_date` | DATE, opcional | Data do incidente |

**`chunks`**: uma linha por trecho de texto.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | UUID, PK | Identificador interno |
| `document_id` | UUID, FK | Documento de origem |
| `chunk_index` | INTEGER | Posição do trecho no documento |
| `section_title` | TEXT, opcional | Título da seção |
| `content` | TEXT | Texto do trecho |
| `embedding` | VECTOR(768) | Vetor do trecho |

## 7. Estrutura da API

### 7.1 Papel da API e organização em camadas

A API, em **FastAPI + Pydantic**, é a porta de entrada do sistema: recebe incidentes, alertas e complementos, valida a entrada e encaminha para a camada de serviços. **A API não executa lógica de investigação**: não chama LLM, não consulta o pgvector e não decide transições do grafo.

Regra de organização: **cada camada só conversa com a camada vizinha**: `api` → `services` → `agents` / `data sources`. 

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
  db/                   # acesso ao PostgreSQL + pgvector
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

**Sistema de alertas (Webhooks):**

| Método | Rota | Função | Resposta |
|---|---|---|---|
| `POST` | `/webhooks/alerts` | Recebe alerta em formato genérico; abre nova investigação ou associa a uma investigação existente | `202` com `incident_id` |


### 7.4 Validações

- **Entrada:** as classes Pydantic validam campos obrigatórios, tipos e tamanhos máximos (descrição, evidências, payload de alerta). Entradas inválidas retornam `422`.
- **Duplicidade:** o sistema não deve abrir várias investigações para o **mesmo incidente**, evitando tráfego e custo de LLM desnecessários. Para cada entrada é calculada uma impressão digital (*fingerprint*):
  - **alertas:** origem + identificador/fingerprint do alerta enviado pela ferramenta;
  - **incidentes manuais:** hash do conteúdo normalizado (título, descrição e evidências).

  Se já existir investigação **aberta** com o mesmo fingerprint, a API retorna o `incident_id` existente em vez de criar outro. A janela de tempo considerada para a duplicidade é um parâmetro a definir na implementação.

### 7.5 Observabilidade e segurança (MVP)

Por se tratar de um MVP, a proposta é manter o mínimo necessário:

- **Observabilidade**: Logs com `incident_id` em todas as etapas, para rastrear a investigação do início ao fim.
- **Segurança**: Implementaremos o mínimo necessário para este MVP.


## 8. Conclusão

O stack do MVP usa LangGraph na orquestração, chunking orientado às seções dos documentos, embeddings do `multilingual-e5-base`, PostgreSQL + pgvector no armazenamento e FastAPI na API. Essas definições ainda serão validadas durante a implementação.
