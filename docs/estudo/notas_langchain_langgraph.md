# Notas de estudo: LangChain v1 e LangGraph (documentação oficial, nov./2026)

Base técnica para implementar o Incident Copilot. São notas em português, com minhas palavras. As fontes
são as páginas em docs.langchain.com/oss/python/ (LangChain e LangGraph), lidas em 2026-11-09, mais a
documentação do CrewAI v1.15.39 para a comparação. Alguns trechos longos de páginas vieram como resumo
do leitor e não verbatim; eles estão marcados com *(resumo)* e devem ser conferidos na página antes de
virarem código.

Complementa [notas_designing_multi_agent_systems.md](notas_designing_multi_agent_systems.md), que traz
os conceitos. Este arquivo traz as APIs.

---

## 1. O mapa dos produtos

| Peça | O que é | Licença |
|---|---|---|
| **LangGraph** | camada de orquestração de baixo nível: grafo de estado, checkpoints, interrupts, streaming | código aberto (desde 2024-02) |
| **LangChain v1** | o "harness" de agente em cima do LangGraph: `create_agent` = modelo + ferramentas + prompt + **middleware** | código aberto (1.0 lançado em 2025-10-20) |
| **Deep Agents** (`deepagents`) | harness completo: planejamento, sistema de arquivos, subagentes | código aberto, **ainda antes da 1.0** (a API pode quebrar entre versões menores) |
| **LangSmith** | rastreamento, avaliação, Studio, deploy gerenciado | **código fechado**. Tem conta gratuita; o deploy gerenciado é pago (plano Plus ou superior) |

- **Estabilidade:** LangChain 1.0 e LangGraph 1.0 são LTS, mantidas ativamente até a 2.0 e com pelo menos
  1 ano de manutenção depois. O que for descontinuado continua funcionando em toda a série 1.x e só sai na
  2.0. Rótulos de estabilidade: *beta* (pode mudar um pouco), *alpha* (pode mudar muito), nomes com `_` são
  internos.
- **Python:** 3.10+ para LangChain e LangGraph. O CLI, o Studio e o `langgraph dev` pedem 3.11+.
- **Ambiente do projeto (verificado):** `langgraph 1.2.20`, `langgraph-checkpoint 4.3.1`,
  `langgraph-prebuilt 1.1.1`, `langchain-core 1.7.6`, `psycopg 3.3.8`. **Faltam** o `langchain`, o pacote
  do provedor do LLM e o `langgraph-checkpoint-postgres`.

## 2. LangGraph: o núcleo (Graph API)

- **Montagem:** `StateGraph(State)` → `add_node` / `add_edge` / `add_conditional_edges` → `.compile()`.
  Importar `StateGraph, START, END` de `langgraph.graph`.
- **Estado:** TypedDict, dataclass ou Pydantic (a documentação prefere TypedDict ou dataclass, por
  desempenho). **Redutores:** `Annotated[list, operator.add]` acumula; sem redutor, o valor é
  sobrescrito. `add_messages` serve para listas de mensagens.
- **Nós** recebem `state` (e, opcionalmente, `config` ou `runtime`). O contexto de execução é imutável por
  rodada e vai por `context_schema` + `invoke(..., context=...)`.
- **`Send`:** devolvido por uma aresta condicional, faz *fan-out* sobre um número de itens decidido em
  tempo de execução.
- **`Command`:** atualiza o estado e roteia (`goto`) num retorno só, e também serve para retomar
  (`resume`). **Não misturar** roteamento por `Command` (ou aresta condicional) com `add_edge` fixa saindo
  do mesmo nó.
- **Limite de recursão:** ~10 mil passos por padrão; estourar gera `GraphRecursionError`.
- **Nós recomeçam do início quando são retomados ou repetidos.** Efeitos colaterais precisam ser
  idempotentes.
- **Compatibilidade de código com execuções salvas:** acrescentar ou redirecionar arestas é seguro.
  **Renomear ou remover um nó em que uma execução pausada vai entrar quebra a retomada.** Renomear um campo
  do estado perde o valor salvo.
- **Subgrafos:** um nó pode chamar outro grafo (com esquemas diferentes, via um adaptador) ou receber o
  grafo compilado direto (campos em comum). A persistência do subgrafo vai por `compile(checkpointer=...)`:
  - `None`, o padrão: herda do pai a cada chamada, e interrupts funcionam;
  - `True`: acumula estado por conversa, mas não aceita chamadas paralelas;
  - `False`: sem estado, sem interrupts.

## 3. Persistência (checkpointers)

- **Backends:** `InMemorySaver` (vem junto, para desenvolvimento) e pacotes separados:
  `langgraph-checkpoint-sqlite`, **`langgraph-checkpoint-postgres`** (`PostgresSaver` / `AsyncPostgresSaver`,
  que a documentação chama de "ideal para produção"), MongoDB, Redis, Cosmos DB, AWS e outros. Todos de
  código aberto.
- **Postgres:** criar com `PostgresSaver.from_conn_string("postgresql://...")` como gerenciador de
  contexto e chamar `.setup()` **uma vez** para criar as tabelas. O `thread_id` precisa ter menos de 255
  caracteres.
- **`thread_id` é obrigatório** com checkpointer (vai em `config={"configurable": {"thread_id": ...}}`).
  Formas de chamar:
  - `invoke(input, config)` → nova entrada sobre o estado salvo;
  - `invoke(None, config)` → continua depois de um erro;
  - `invoke(Command(resume=...), config)` → responde a um interrupt;
  - *replay* a partir de um snapshot de `get_state_history()`.
- O checkpoint é salvo a cada passo do grafo, e as gravações pendentes de outros nós do mesmo passo
  sobrevivem a uma falha. `get_state`, `get_state_history` e `update_state` permitem inspecionar e
  corrigir.
- **Serialização:** JSON estendido por padrão. Há criptografia AES (`EncryptedSerializer`, chave em
  `LANGGRAPH_AES_KEY`).
- **Os checkpoints crescem sem limite.** Não há configuração de retenção, e a documentação sugere limpeza
  periódica (por exemplo, com cron).
- **Durabilidade** (`durability=` em qualquer chamada): `"exit"`, `"async"` ou `"sync"`. O padrão não
  aparece nas páginas lidas.

## 4. Interrupts (humano no ciclo, no nível do LangGraph)

- `interrupt(payload)` (de `langgraph.types`) dentro de um nó ou de uma ferramenta pausa a execução. O
  valor de `Command(resume=valor)` vira o retorno do `interrupt()`.
- **Requisitos:** checkpointer, `thread_id` e um payload serializável em JSON.
- **Regras:**
  - o nó recomeça do topo na retomada, então o código antes do `interrupt()` roda de novo;
  - **não envolver** o `interrupt()` num `try/except` genérico;
  - manter a ordem das pausas fixa (a correspondência é por posição);
  - para repetir uma validação, usar uma aresta condicional, não `while True`.
- Vários interrupts em paralelo são retomados com um dicionário de ID → valor.
- **Aprovar uma ferramenta:** o `interrupt()` dentro da ferramenta permite aprovar ou **editar os
  argumentos** antes de executar. A resposta humana pode ser validada com `response_schema`
  (langgraph ≥ 1.2.12).
- `interrupt_before`/`interrupt_after` (estáticos) existem, mas **não são recomendados** para humano no
  ciclo.

## 5. Streaming

- **Modos:** `values`, `updates`, `messages` (tokens com metadados do nó), `custom` (eventos nossos via
  `get_stream_writer()`), `checkpoints`, `tasks`, `debug`. Pode-se combinar vários numa lista.
- **`version="v2"`** (LangGraph 1.1+) devolve partes uniformes (`type`, `ns`, `data`). A API nova
  recomendada é **`stream_events(..., version="v3")`**, com projeções (`messages`, `values`, `interrupts`,
  `output`…).
- `subgraphs=True` para ver os subgrafos. Os argumentos das chamadas de ferramenta chegam em pedaços e
  precisam ser montados.

## 6. Memória de longo prazo (stores)

- **Checkpointer** = estado de *uma* conversa. **Store** = dados entre conversas, em namespaces
  (tuplas) + chave.
- `InMemoryStore` para desenvolvimento. Em produção, **`PostgresStore`** (mesmo pacote
  `langgraph-checkpoint-postgres`, com `.setup()`), MongoDB, Redis.
- **API:** `put` / `get` / `search(namespace_prefix, query=..., filter=..., limit=10)`. Busca semântica
  com um índice (`embed`, `dims`, `fields`).
- Nos nós e ferramentas, acessível via `runtime.store`.

## 7. LangChain v1: `create_agent`

- `from langchain.agents import create_agent`. **Devolve um grafo LangGraph compilado**, que pode virar
  um nó ou subgrafo de um `StateGraph` maior.
- **Parâmetros principais:**
  - `model`: uma string `"provedor:modelo"` ou uma instância. **Não aceita modelo com `bind_tools`
    aplicado antes**;
  - `tools`;
  - `system_prompt`;
  - `middleware`: uma lista, executada na ordem;
  - `response_format`: saída estruturada;
  - `state_schema`: subclasse de `AgentState`, **só TypedDict**;
  - `context_schema`;
  - `checkpointer`;
  - `store`;
  - `name`.
- **Resultado:** um dicionário com `messages` e, com `response_format`, também `structured_response`.
- **Substitui o `create_react_agent` do `langgraph.prebuilt`**, que foi descontinuado sem data de
  remoção. Na migração:
  - `prompt=` → `system_prompt=`;
  - `pre_model_hook`/`post_model_hook` → middleware;
  - `ToolNode` não entra mais em `tools=`;
  - nos eventos de streaming, o nó `"agent"` passou a se chamar `"model"`;
  - o que era legado (chains, retrievers antigos, parsers que consertam a saída, hub) foi para o pacote
    `langchain-classic`.
- **Pegadinha:** dentro de um grafo pai, o agente é um subgrafo. O streaming de tokens do pai só mostra os
  tokens internos com `subgraphs=True`.

## 8. Modelos

- **`init_chat_model("provedor:modelo", temperature=..., timeout=..., max_tokens=..., max_retries=...,
  base_url=..., rate_limiter=...)`.** Novos nomes de modelo funcionam sem atualizar o LangChain.
- **`max_retries` padrão = 6**, com espera exponencial e variação aleatória. Repete em falhas de rede, 429
  e 5xx; não repete em 401 e 404. A documentação sugere 10 a 15 para agentes longos.
- **Provedores (pacote próprio de cada um):**
  - `langchain-anthropic` (`ChatAnthropic`);
  - `langchain-openai` (`ChatOpenAI`, que só segue a especificação oficial da OpenAI; para vLLM,
    OpenRouter, DeepSeek e LiteLLM, use o pacote específico de cada um);
  - `langchain-nvidia-ai-endpoints` (`ChatNVIDIA`, NIM hospedado ou local, compatível com a API da
    OpenAI via `base_url`, chave `NVIDIA_API_KEY`);
  - `langchain-ollama` (`ChatOllama`, local, sem chave; **não informa o uso de tokens**);
  - Google, Bedrock, Azure e outros.
- **Ferramentas no modelo:** `bind_tools(...)`, `tool_choice`, `parallel_tool_calls=False`. Fora de um
  agente, é você quem executa as ferramentas e devolve as `ToolMessage`.
- **Saída estruturada direto no modelo:** `with_structured_output(Schema, method="json_schema" |
  "function_calling" | "json_mode", include_raw=...)`. Uma recusa gera `ModelRefusalError`.
- **Raciocínio:** `reasoning_effort` padronizado entre provedores; os blocos de `reasoning` aparecem no
  conteúdo da resposta.
- **Perfis de modelo** (beta): `model.profile` traz limite de contexto, suporte a ferramentas e a saída
  estruturada. Os dados vêm do models.dev e são usados para escolher automaticamente a estratégia de saída
  estruturada.
- **Limite de taxa:** `InMemoryRateLimiter` limita o número de requisições por segundo, não o tamanho, e
  vale só dentro de um processo.
- **Uso de tokens:** `usage_metadata` na `AIMessage` e callbacks agregadores. No streaming da OpenAI é
  preciso ativar (`stream_usage=True`).
- **Erros tipados** (`langchain_core.exceptions`): autenticação, permissão, requisição inválida, modelo
  inexistente, limite de taxa, erro da API, conexão, timeout e `ContextOverflowError`, cada um com
  `is_retryable`.
- **Anthropic, pegadinha:** os modelos Claude mais novos **recusam `temperature`/`top_p`/`top_k` fora do
  padrão** (erro 400). Isso afeta testes que tentariam usar `temperature=0`.

## 9. Mensagens e ferramentas

- **Mensagens** (`langchain.messages`): System, Human, AI (com `tool_calls`, `usage_metadata`,
  `content_blocks`) e Tool. A `ToolMessage` exige `tool_call_id` igual ao da chamada; o campo `artifact`
  não vai para o modelo.
- **Blocos de conteúdo padronizados** (texto, reasoning, imagem, arquivo, chamadas de ferramenta…) dão uma
  visão igual entre provedores.
- **Segurança:** `langchain_core.load.load()` instancia objetos e **nunca deve ser usado com dados não
  confiáveis**.
- **Ferramentas:** `@tool` de `langchain.tools`. A docstring vira a descrição e as anotações de tipo viram
  o schema (são obrigatórias). Nomes em snake_case. `config` e `runtime` são nomes reservados.
  - O parâmetro **`runtime: ToolRuntime`** fica escondido do modelo e dá acesso a `state`, `context`,
    `store`, `stream_writer`, `tool_call_id` e `execution_info`.
  - Para atualizar o estado, devolver `Command(update=...)` **com uma `ToolMessage` correspondente**;
    sem ela, dá erro.
  - `return_direct=True` encerra o ciclo com a saída da ferramenta, mas só se todas as chamadas daquele
    passo tiverem essa opção.
  - Erros de ferramenta são tratados via middleware.

## 10. Saída estruturada no agente

- **`response_format=`** em `create_agent`; o resultado validado fica em `result["structured_response"]`.
- **`ProviderStrategy(Schema, strict=...)`:** usa o recurso nativo do provedor (OpenAI, Anthropic, xAI).
  **`ToolStrategy(Schema, handle_errors=True, ...)`:** usa chamada de ferramenta e aceita `Union`.
  Passando só o schema, o LangChain escolhe sozinho pelo perfil do modelo. Um dicionário de JSON Schema
  precisa vir dentro de uma estratégia explícita.
- **`handle_errors`** (padrão `True`): em caso de erro de validação, devolve o erro ao modelo e pede
  correção. Também aceita uma mensagem fixa, tipos de exceção, uma função ou `False` (propaga o erro).
- **Recusa:** com ProviderStrategy, gera erro de validação; com ToolStrategy, o agente termina sem
  `structured_response`. O `ModelRefusalMiddleware` uniformiza isso.
- **Requisito:** se houver ferramentas, o modelo precisa suportar ferramentas e saída estruturada ao mesmo
  tempo.

## 11. Middleware (o recurso central da v1)

**Ganchos:**
- `before_agent` / `after_agent`: uma vez por chamada;
- `before_model` / `after_model`: a cada chamada ao modelo;
- `wrap_model_call` / `wrap_tool_call`: envolvem a chamada e podem pular, repetir ou trocar o modelo, as
  ferramentas, o prompt ou o formato de saída via `request.override(...)`;
- `@dynamic_prompt`.

Ordem: os `before_*` rodam do primeiro ao último, os `after_*` do último ao primeiro, e os `wrap_*` se
aninham (o primeiro fica por fora). `jump_to` permite pular para `end`, `tools` ou `model`.

**Prontos** (de `langchain.agents.middleware`), com os padrões:

| Middleware | Para quê | Padrões e cuidados |
|---|---|---|
| `HumanInTheLoopMiddleware(interrupt_on={...})` | aprovar chamadas de ferramenta | ver §12 |
| `ModelCallLimitMiddleware` | limitar chamadas ao modelo | `thread_limit` (precisa de checkpointer), `run_limit`; ao estourar, termina por padrão (`"end"`) |
| `ToolCallLimitMiddleware` | limitar chamadas de ferramenta (todas ou uma específica) | ao estourar, continua por padrão (`"continue"`); `"error"` lança exceção |
| `ToolRetryMiddleware` / `ModelRetryMiddleware` | repetir em falha | 2 repetições, espera ×2 a partir de 1 s, máximo 60 s, com variação; na falha final, devolve o erro ao modelo (`"continue"`) |
| `ToolErrorMiddleware` | transformar exceções de ferramenta em mensagens de erro | não repete; combinar com o de repetição por dentro |
| `ModelFallbackMiddleware(m1, m2, ...)` | modelos reserva, em ordem | — |
| `ModelRefusalMiddleware` | transformar recusa em exceção | só detecta blocos de recusa formais, não recusa em texto livre |
| `SummarizationMiddleware(model, trigger, keep)` | resumir o histórico | **sem `trigger`, não resume nada**; `keep` padrão = 20 mensagens |
| `ContextEditingMiddleware` *(resumo)* | limpar saídas antigas de ferramentas | gatilho em ~100 mil tokens, mantém as 3 últimas |
| `PIIMiddleware` | dados pessoais | tipos prontos: e-mail, cartão, IP, MAC, URL; estratégias block, redact (padrão), mask, hash. **Por padrão só olha a entrada**: saída e resultados de ferramenta precisam ser ativados |
| `LLMToolSelectorMiddleware` | escolher as ferramentas relevantes com um LLM | uma chamada extra |
| `TodoListMiddleware` | lista de tarefas para o agente | — |
| `ShellToolMiddleware` | shell persistente | **por padrão roda direto no host**. Não usar no copiloto |
| Filesystem/SubAgent/Rubric | vêm do `deepagents` | — |

## 12. Humano no ciclo com `create_agent`

- **`HumanInTheLoopMiddleware(interrupt_on={"ferramenta": True | False | InterruptOnConfig(...)})`.**
  O `InterruptOnConfig` permite escolher as decisões permitidas, uma descrição e uma condição (`when`).
- **Decisões:**
  - **approve**;
  - **edit**: muda o nome e os argumentos antes de executar;
  - **reject**: com mensagem opcional;
  - **respond**: devolve um texto como se a ferramenta tivesse dado certo. **Não usar para negar.**
- **Modos:** `"batched"` (o padrão, um interrupt por turno do modelo, com as decisões em ordem) e
  `"per_call"` (um interrupt por chamada, com chave por ID). O `per_call` é o recomendado para agentes
  novos e deve virar o padrão na próxima versão principal.
- **Chamar com** `thread_id` + `version="v2"`; o resultado traz `.interrupts`. **Retomar com**
  `Command(resume={"decisions": [...]})`.
- **Exige checkpointer.** Os exemplos de produção usam `AsyncPostgresSaver`.
- **Pegadinhas:**
  - a condição `when` **roda de novo na retomada** e precisa ser determinística. Se ela mudar para
    falso, a ferramenta executa e a decisão humana (até um *reject*) é ignorada;
  - no modo `per_call`, colocar o HITL **antes** dos middlewares de repetição e de erro.

## 13. Runtime, contexto e memória curta

- **`Runtime`/`ToolRuntime`:** `context` (configuração imutável por rodada, como usuário ou permissões),
  `store`, `stream_writer` e `execution_info` (thread_id, run_id, tentativa).
- **Engenharia de contexto:** mudar o prompt, as mensagens ou as ferramentas só para uma chamada, via
  `wrap_model_call` (não persiste), ou de forma persistente, via ganchos de ciclo ou `Command`.
- **Memória curta** = histórico no estado + checkpointer. Formas de controlar:
  - **cortar** com `before_model` + `RemoveMessage(REMOVE_ALL_MESSAGES)` mantendo as N últimas;
  - **resumir** com `SummarizationMiddleware`.
  - **Cuidado:** o histórico precisa continuar válido (alguns provedores exigem começar por uma mensagem
    do usuário, e toda chamada de ferramenta precisa da resposta correspondente).

## 14. Multiagente (padrões da documentação)

| Padrão | Como funciona | Quando |
|---|---|---|
| **Subagentes** | o agente principal chama outros agentes como ferramentas (`@tool` que chama `invoke` e devolve a última mensagem) | delegar com contexto isolado. Sem estado por padrão. `get_state(subgraphs=True)` não enxerga o estado deles |
| **Handoffs** | uma ferramenta muda uma variável do estado (`Command(update=...)`); um middleware troca o prompt e as ferramentas conforme o passo. Entre subgrafos: `Command(goto=..., graph=Command.PARENT)` | fluxos por etapas. A versão com um agente só e middleware é a recomendada |
| **Router** | um classificador manda para um ou vários agentes (`Command(goto)` ou `Send`) e depois sintetiza | entrada com tipos distintos. Sem estado por padrão |
| **Skills** | um agente carrega prompts sob demanda | não impõe restrições (é só prompt) |
| **Workflow próprio** | um `StateGraph` com nós que são funções, LLMs ou agentes | **o nosso caso** |

## 15. RAG e vetores no Postgres

- **`langchain-postgres`** tem dois vetores sobre pgvector:
  - **`PGVector`:** só psycopg3 (`postgresql+psycopg://`). IDs informados sobrescrevem os existentes. **Não
    há migração de schema: mudou o schema, recria a tabela.** Filtros `$eq … $ilike $and $or`, e MMR via
    `as_retriever`.
  - **`PGVectorStore`:** API nova, assíncrona primeiro (`PGEngine`, `PGVectorStore.create`). **Consegue
    usar uma tabela existente** mapeando as colunas de id, conteúdo, embedding e metadados. Tem índices
    HNSW e IVFFlat e busca híbrida.
- Formas de RAG descritas: em 2 passos, **agêntico** (o agente chama a ferramenta de busca) e híbrido (com
  reescrita da consulta e validação).

## 16. MCP

- **`langchain[mcp]>=1.4.0`** (beta, substitui o `langchain-mcp-adapters`). Uso: `MCPAdapter(alvo)`, que
  conecta por HTTP, stdio ou servidor FastMCP no mesmo processo, e `list_tools()` → `create_agent`.
- As anotações de cada ferramenta (destrutiva, só leitura) servem para montar o HITL. Pedidos de dados do
  servidor (*elicitation*) viram interrupts. *Sampling* não é suportado.
- **Pegadinha:** a retomada roda a ferramenta MCP do começo, então efeitos colaterais podem se repetir.

## 17. Testes e avaliação

- **Testes unitários:** `GenericFakeChatModel(messages=iter([...]))` ou `FakeListChatModel(responses=[...])`.
  - **Pegadinha:** o `GenericFakeChatModel` não implementa `bind_tools`; é preciso criar uma subclasse que
    devolva `self`.
  - O iterador se esgota, então use fixtures com escopo de função.
  - `InMemorySaver` para simular várias rodadas.
- **Testes de integração:** marcar com `@pytest.mark.integration` e excluir por padrão. Pular quando não há
  chave. **Verificar a estrutura** (quais ferramentas, quantas mensagens), não o texto exato. Gravar e
  reproduzir respostas com `vcrpy` + `pytest-recording`, filtrando as chaves; as gravações ficam velhas
  quando o prompt ou as ferramentas mudam.
- **Avaliação de trajetória** com `agentevals` (código aberto):
  - `create_trajectory_match_evaluator(trajectory_match_mode="strict"|"unordered"|"subset"|"superset")`:
    determinístico e sem custo;
  - `create_trajectory_llm_as_judge(...)`: com juiz LLM;
  - o LangSmith é opcional, para acompanhar experimentos.

## 18. Observabilidade, Studio, interface e deploy

- **Rastreamento:** LangSmith (`LANGSMITH_TRACING=true`, `LANGSMITH_API_KEY`), com `tags` e `metadata` por
  chamada e liga/desliga seletivo (`tracing_context`). Middlewares têm `TracePolicy` para omitir payloads.
  **OpenTelemetry não aparece** nas páginas lidas.
- **Studio:** interface visual gratuita (exige conta e chave do LangSmith). Roda com `langgraph dev`
  (servidor local em memória, só para desenvolvimento) e `langgraph.json`. **Com `LANGSMITH_TRACING=false`,
  nenhum dado sai da máquina.**
- **Agent Chat UI:** app Next.js de código aberto (streaming, ferramentas, interrupts, *time travel*). Há
  SDKs de frontend `useStream` para React, Vue, Svelte e Angular.
- **Deploy:** o caminho da documentação é o LangSmith Cloud (pago) ou servidores próprios com licença do
  LangSmith. **Nada disso é necessário:** o grafo compilado roda dentro do nosso FastAPI, com o
  checkpointer no nosso Postgres.

## 19. CrewAI (para registro da comparação)

- **Flows** (`@start`, `@listen`, `@router`, `and_`/`or_`, estado em Pydantic) dão um workflow controlado,
  e as *Crews* são passos dentro deles. **`@human_feedback`** pausa e retoma (`from_pending().resume()`).
- **Persistência padrão em SQLite.** Dá para criar um backend próprio, mas a interface **não está
  documentada**. **Não há Postgres.**
- A retomada por `inputs.id` está descontinuada; o substituto cria um *ramo novo*.
- **A API `/resume` e o rastreamento nativo dependem da plataforma paga (AMP).** O rastreamento nativo pode
  pedir para enviar os rastros à CrewAI. O RAG nativo usa ChromaDB ou Qdrant, sem pgvector.
- **Conclusão:** viável, mas o LangGraph atende melhor ao que precisamos: Postgres oficial, interrupts
  estáveis e observabilidade sob nosso controle.

---

## → No nosso projeto: como montar o Incident Copilot com essas peças

**Estrutura:** um `StateGraph` próprio (padrão "workflow próprio", §14) como orquestrador. Dentro dele,
um único nó autônomo, o de investigação, feito com `create_agent` (que vira um subgrafo).

```
StateGraph(EstadoIncidente)                       ← checkpointer: PostgresSaver (banco "incidentes")
 ├─ roteador (aresta condicional por tipo de pedido)
 ├─ buscar_historico      ← chama o busca.py da E2 (sem LLM)
 ├─ investigar            ← create_agent(model, tools=[buscar_incidentes, ler_incidente],
 │                            response_format=ToolStrategy(Hipotese),
 │                            middleware=[ModelCallLimit, ToolCallLimit, ToolRetry, ...])
 ├─ aprovar_mitigacao     ← interrupt() com a sugestão; Command(resume=decisão)
 └─ redigir_postmortem    ← saída estruturada (template) + verificação de citações
```

**Decisões práticas:**
1. **Pacotes:** `langchain`, `langgraph-checkpoint-postgres` e o provedor do LLM escolhido
   (`langchain-anthropic`, `langchain-nvidia-ai-endpoints` ou `langchain-ollama`).
2. **Checkpointer e store no mesmo Postgres** do pgvector (de preferência num schema separado), com um
   `setup()` único no pipeline e limpeza periódica dos checkpoints.
3. **A busca continua sendo a nossa** (`busca.py`, com o SQL em duas etapas). Embrulhar como `@tool` com
   saída estruturada, em vez de migrar para o `PGVectorStore`: a nossa busca agrupa por incidente e
   combina resumo + texto, o que o vetor genérico não faz. O `PGVectorStore` aceitaria a tabela existente,
   mas não ganharíamos nada.
4. **Saída estruturada:** `ToolStrategy(Hipotese)` com `handle_errors=True` e um schema com `sustentada:
   bool`, `justificativa`, `citacoes: list[Citacao]` e **sem "confiança 0–1"**, como manda o livro.
5. **Limites e robustez via middleware:** `ModelCallLimitMiddleware` + `ToolCallLimitMiddleware` (a
   parada composta do livro), `ToolRetryMiddleware` e `ToolErrorMiddleware`.
6. **Aprovação humana:** no workflow principal, um `interrupt()` no nó `aprovar_mitigacao`. Se no futuro o
   agente ganhar alguma ferramenta de ação, usar `HumanInTheLoopMiddleware` no modo `per_call`. **Nós
   idempotentes antes de cada pausa.**
7. **PII:** `PIIMiddleware` com `apply_to_tool_results=True` quando entrarem logs reais.
8. **Testes:** `GenericFakeChatModel` (com a subclasse do `bind_tools`) para o grafo; `agentevals` em modo
   `subset`/`superset` para conferir que o agente chamou a busca antes de afirmar algo; as perguntas da E2
   como base dos cenários.
9. **Observabilidade:** o Studio (`langgraph dev`) com `LANGSMITH_TRACING=false` para depurar
   localmente sem mandar dados para fora; decidir depois se os rastros podem ir para o LangSmith.
10. **Nomes estáveis desde o início** (nós e campos do estado), porque renomear quebra execuções pausadas.
