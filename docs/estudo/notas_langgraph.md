# Notas de estudo: LangGraph (Python)

Leitura completa da documentação oficial do LangGraph para Python (https://docs.langchain.com/oss/python/langgraph/), feita em 2026-11-09. São 37 páginas: overview, quickstart, capacidades, Graph API, padrões, deploy, frontend, Functional API, runtime e os dois tutoriais (RAG agêntico e agente SQL).

Premissa destas notas: **usar o LangGraph sem o pacote `langchain`**. Os nós chamam o SDK do provedor do LLM diretamente. As notas do LangChain v1 ([notas_langchain_langgraph.md](notas_langchain_langgraph.md)) ficam como referência, caso se decida usá-lo depois.

Os pontos marcados como **[verificado]** foram conferidos no código instalado (`multiagent_env`, langgraph 1.2.20). Os marcados como **[a conferir]** são lacunas ou inconsistências da documentação.

---

## 1. Dá para usar sem o LangChain?

Sim, com uma ressalva.

- **[verificado]** `langgraph` 1.2.20 depende de `langchain-core`, `langgraph-checkpoint`, `langgraph-prebuilt`, `langgraph-sdk`, `pydantic` e `xxhash`. O `langchain-core` é instalado junto de qualquer forma. O pacote **`langchain` não está instalado** e não é necessário.
- O `langchain-core` é a base: tipos de mensagem, `RunnableConfig` e a interface Runnable que os nós implementam por baixo. Não traz agentes, middleware nem integrações com provedores.
- Funciona só com `langgraph`:
  - `StateGraph`, arestas e roteamento, `Command`, `Send`;
  - `interrupt`, checkpointers e stores;
  - `RetryPolicy`, timeouts, `error_handler`, cache;
  - streaming e `Runtime`;
  - `MessagesState` e `add_messages`, importados de `langgraph.graph`;
  - **[verificado]** `RemoveMessage` e `REMOVE_ALL_MESSAGES` em `langgraph.graph.message`.
- O que os exemplos da documentação usam do `langchain` e o que colocamos no lugar:

| Nos exemplos | O que usar no lugar |
|---|---|
| `init_chat_model`, `ChatAnthropic`, `ChatOpenAI` | o SDK do provedor (`anthropic`, `openai` ou um cliente HTTP para o NIM/Ollama), chamado dentro do nó |
| `@tool` e `ToolRuntime` (`langchain.tools`) | uma função Python comum. No workflow, o nó chama a busca direto, sem o LLM decidir |
| `with_structured_output(Schema)` | saída estruturada do próprio provedor (JSON schema ou tool use) e validação com Pydantic no nó |
| `langchain.messages` | dicts `{"role", "content"}`, ou campos tipados no estado (o nosso caso, porque não é um chat) |
| stream de tokens via modo `messages` | `stream_mode="custom"`: o nó repassa cada pedaço do SDK com `get_stream_writer()`. A documentação recomenda isso para LLM sem integração LangChain |
| `create_agent` e middleware | não é necessário num workflow. Se precisarmos de um laço de agente, ele cabe em poucas linhas (ver §8.7) |
| `trim_messages`, `count_tokens_approximately` | ficam no `langchain-core`, que já está instalado. Só fazem falta se houver histórico de chat |

- Como o nosso fluxo é um **workflow** (busca, hipótese, aprovação, postmortem) e não um chat, o estado nem precisa de `messages`. Campos tipados bastam.

## 2. Modelo mental: o runtime Pregel

- Compilar um `StateGraph` (ou decorar um `@entrypoint`) gera uma instância de `Pregel`.
- A execução acontece em **super-steps**, cada um com três fases:
  1. **Plan**: escolhe os nós cujos canais de entrada mudaram.
  2. **Execution**: roda esses nós em paralelo. Uma escrita feita num passo **não é vista** pelos outros nós do mesmo passo.
  3. **Update**: aplica as escritas aos canais.
- Cada chave do estado é um **canal**:
  - `LastValue` (padrão): sobrescreve. Duas escritas no mesmo passo dão erro.
  - `BinaryOperatorAggregate`: é o reducer, como em `Annotated[list, operator.add]`.
  - `Topic`.
  - `EphemeralValue`: canais internos.
  - `DeltaChannel`: beta, guarda só os deltas. Ver o aviso em §5.6.
- O grafo termina quando nenhum nó fica ativo.
- O checkpoint é gravado na **fronteira de cada super-step**. O nó é a unidade de checkpoint e de retry.
- O limite de recursão conta super-steps (`GraphRecursionError`):
  - padrão de 10.007 a partir da versão 1.1.4;
  - configurado com `{"recursion_limit": N}` no **nível de cima** da config, não dentro de `configurable`;
  - para encerrar antes do erro, declare `remaining_steps: RemainingSteps` no estado (`langgraph.managed.is_last_step`) e saia antes de esgotar.

## 3. Método de desenho ("Thinking in the Graph API")

1. **Mapear o processo em passos discretos.** Cada passo vira um nó com uma única função. Desenhe o fluxo antes de escrever código.
2. **Classificar cada passo pelo tipo de trabalho:**
   - **LLM:** prompt estático, contexto vindo do estado, saída estruturada que decide a rota.
   - **Dados:** retry com backoff, cache possível.
   - **Ação externa:** retry, nunca cache, sempre idempotente.
   - **Humano:** `interrupt()`.
3. **Desenhar o estado.**
   - Guarde o que não dá para reconstruir (a entrada original), o que é caro de refazer (resultados de busca) e o que precisa persistir (rascunhos, decisões).
   - **Guarde dados brutos, não prompts formatados.** O prompt é montado dentro do nó.
   - Não guarde o que pode ser derivado.
4. **Escrever os nós.** O nó lê o estado e devolve um dict parcial, ou um `Command(update=..., goto=...)` quando também decide a rota. Tratamento de erro por tipo:

| Erro | Tratamento |
|---|---|
| transitório (rede, rate limit) | `RetryPolicy` no nó |
| corrigível pelo LLM (parse, ferramenta) | grava o erro no estado e volta ao nó do LLM |
| precisa de informação do humano | `interrupt()` |
| falhou depois dos retries | `error_handler` (compensação) |
| inesperado | deixa falhar, sem capturar |

5. **Ligar tudo.** Poucas arestas fixas e compilação com checkpointer.

**Regra prática:** um passo merece um nó próprio quando, depois dele, pode haver bifurcação, interrupt, retomada ou time travel. Se for só uma sequência determinística, pode ficar como função dentro de outro nó.

## 4. Graph API

### 4.1 Estado
- O schema do estado pode ser:
  - **TypedDict:** recomendado, junto com dataclass, pelo desempenho.
  - **dataclass:** quando o estado precisa de valores padrão.
  - **Pydantic:** valida **só a entrada do primeiro nó**, a saída do grafo vem como dict e a validação recursiva é lenta.
- **Reducer:** `campo: Annotated[list[X], operator.add]`. Sem reducer, o valor é sobrescrito.
- **Pegadinha:** com reducer de acumulação, devolver `[]` **não limpa** o campo. Use `Overwrite([])` (`langgraph.types`).
  - Só um nó por super-step pode dar `Overwrite` na mesma chave (senão dá `InvalidUpdateError`).
  - O `Overwrite` descarta as outras escritas na chave naquele passo.
- **Schemas de entrada e saída:** `StateGraph(S, input_schema=I, output_schema=O)`. Também existe estado privado entre dois nós.
  - Isso **não esconde canais no streaming**: `stream_mode="values"` mostra tudo.
  - Para filtrar, use `output_keys=[...]` ou `stream_mode="updates"`.
- **Contexto de runtime:** `StateGraph(S, context_schema=Ctx)` e depois `graph.invoke(x, config, context=Ctx(...))`. O nó lê `runtime.context`.
  - É o lugar das dependências que não devem ir para o estado nem para o checkpoint: cliente do banco, nome do modelo, `dataset`.

### 4.2 Nós
- Assinatura `def no(state, config?, runtime?)`, síncrona ou `async`.
- O `runtime: Runtime[Ctx]` dá acesso a:
  - `context`, `store`, `stream_writer`;
  - `execution_info`: `thread_id`, `run_id`, `checkpoint_id`, `task_id`, `node_attempt` (começa em 1) e `node_first_attempt_time`;
  - `heartbeat()`, `drain_requested`;
  - `server_info`, que só existe no Agent Server.
- `add_node(fn)` usa `fn.__name__` como nome do nó.
- `add_sequence([a, b, c])` cria uma sequência.
- **O nó é reexecutado do início** depois de um interrupt ou de um retry. Tudo o que vem antes do ponto de pausa precisa ser idempotente.

### 4.3 Arestas e controle de fluxo
- `add_edge(START, "a")`, `add_edge("a", END)`.
- `add_conditional_edges("a", rota, {"x": "no_x", ...})`. A função de rota devolve um nome, `END`, uma lista ou objetos `Send`.
  - Anote o retorno com `Literal[...]` e **sempre inclua um `else`**: a rota que devolve `None` quebra o grafo.
- **Num mesmo nó, use arestas fixas ou roteamento dinâmico, nunca os dois.** Se misturar, os dois caminhos rodam.
- **Fan-out e fan-in:**
  - várias arestas saindo do mesmo nó rodam em paralelo no mesmo passo;
  - o nó de junção precisa de reducer;
  - a ordem das escritas não é garantida;
  - se um ramo levantar exceção, **nenhuma** escrita daquele passo é aplicada (é transacional);
  - limite de paralelismo: `{"max_concurrency": N}` no nível de cima da config.
- **Formas de juntar ramos:**
  - `add_edge(["b", "c"], "d")`: `d` roda uma vez, depois que todos terminam. Se um dos ramos não rodar, `d` nunca roda, e não aparece erro.
  - Arestas separadas: `d` roda uma vez a cada passo em que algum ramo termina.
  - `add_node("d", fn, defer=True)`: `d` roda uma vez, quando não houver mais nada pendente **no grafo inteiro**.
- Loops precisam de condição de parada e de um contador no estado.

### 4.4 Send e Command
- **`Send("worker", {...})`** é o map-reduce.
  - O worker recebe **só** o payload do `Send`, não o estado.
  - A saída volta por um reducer.
  - Use quando o número de itens só é conhecido em execução, por exemplo "investigar cada um dos 3 incidentes similares".
- **`Command(update=..., goto=...)`**: o nó atualiza o estado e escolhe a rota na mesma resposta.
  - Anote como `-> Command[Literal["a", "b"]]`. Sem isso, o grafo e o desenho não conhecem as rotas.
  - `graph=Command.PARENT` navega de um subgrafo para o grafo pai. A chave atualizada precisa de reducer no pai.
- **Pegadinha:** como **entrada** de `invoke`/`stream`, só `Command(resume=...)` é válido.
  - `Command(update=...)` retoma do último checkpoint, não do `START`.
  - Um turno novo começa com um dict.

### 4.5 Configuração de nó (1.2+, versão instalada)
- **`retry_policy=RetryPolicy(...)`**: `max_attempts=3`, `initial_interval=0.5`, `backoff_factor=2.0`, `max_interval=128` e `jitter=True`.
  - `retry_on` aceita uma exceção, uma tupla de exceções ou uma função.
- **[verificado] `default_retry_on`:**
  - retenta `ConnectionError` e erros HTTP 5xx de `httpx`/`requests`;
  - **não** retenta `ValueError`, `TypeError`, `LookupError`, `RuntimeError`, `OSError` e semelhantes;
  - **pegadinha:** `TimeoutError` herda de `OSError`, então **não é retentado** (`default_retry_on(TimeoutError())` dá `False`). Os erros de timeout e rate limit do SDK do LLM precisam ir explicitamente no `retry_on`.
- **`timeout=`** aceita segundos, um `timedelta` ou `TimeoutPolicy(run_timeout, idle_timeout)`.
  - Funciona **só em nó async**. Num nó síncrono, a compilação falha.
  - O limite vale por tentativa.
  - Levanta `NodeTimeoutError`, que o retry padrão trata como retentável.
  - O `idle_timeout` reinicia a cada sinal de progresso (stream, writer, `runtime.heartbeat()`).
- **`error_handler=fn(state, error: NodeError) -> Command`** roda depois que os retries se esgotam.
  - É o padrão de compensação.
  - É um handler por nó. Se o handler falhar, o erro sobe.
  - O `NodeError` é checkpointado: se o processo cair, a retomada vê o mesmo erro.
- **`cache_policy=CachePolicy(ttl=..., key_func=...)`** junto com `compile(cache=InMemoryCache())`.
  - Útil para embeddings e buscas.
  - **Nunca** use em nós com ação externa.
- **`StateGraph(S).set_node_defaults(retry_policy=..., timeout=..., error_handler=..., cache_policy=...)`**
  - O valor passado no próprio nó vence o default.
  - Os defaults **não** passam para subgrafos.
- **Desligamento gracioso:**
  - `RunControl()` + `control.request_drain("sigterm")`, com `graph.invoke(..., control=control)`;
  - o grafo levanta `GraphDrained` e salva um checkpoint retomável;
  - depois, retome com `invoke(None, config)`.

### 4.6 Visualização
- `graph.get_graph().draw_mermaid()` gera texto Mermaid sem nenhuma dependência extra. Serve para documentação e PR.
- `draw_mermaid_png()` usa o serviço mermaid.ink, então **manda o grafo para fora**. `draw_png()` exige graphviz.

## 5. Persistência

### 5.1 Checkpointer e threads
- `compile(checkpointer=...)` grava um snapshot por super-step, agrupado por `thread_id` em `config["configurable"]`.
- Sem `thread_id`, não há persistência nem retomada.
- **No PostgresSaver, o `thread_id` precisa ter menos de 255 caracteres.**
- Quatro formas de chamar uma thread:

| Chamada | Efeito |
|---|---|
| `invoke(entrada, config)` | aplica a entrada sobre o estado salvo (passando pelos reducers) e começa do `START`. Não limpa a thread |
| `invoke(None, config)` | retoma depois de um erro e refaz o trabalho pendente |
| `invoke(Command(resume=v), config)` | responde ao `interrupt()`. O nó interrompido roda de novo do início |
| `invoke(None, snapshot.config)` | replay a partir de um checkpoint antigo |

- O `checkpoint_ns` identifica a origem: `""` para a raiz, `"no:uuid"` para um subgrafo, separados por `|` quando aninhados.
- **Pending writes:** num passo paralelo, as escritas dos nós que terminaram já ficam duráveis. Se outro ramo falhar, essas escritas não são refeitas.

### 5.2 Inspeção
- **`graph.get_state(config)`** devolve um `StateSnapshot` com:
  - `values` e `next` (tupla vazia significa que o grafo terminou);
  - `config`, com `thread_id`, `checkpoint_ns` e `checkpoint_id`;
  - `metadata`: `source` (`input`/`loop`/`update`), `writes` e `step`, que começa em -1;
  - `created_at`, `parent_config`;
  - `tasks`: `PregelTask` com `id`, `name`, `error`, `interrupts` e `state`, este último quando se passa `subgraphs=True`;
  - `interrupts`.
- **`get_state_history(config)`** lista os checkpoints do mais recente para o mais antigo. Para achar o checkpoint pausado num interrupt:
  ```python
  next(s for s in hist if any(t.interrupts for t in s.tasks))
  ```
- **`checkpointer.list(None)`** lista todas as threads, com uma linha **por checkpoint**. É preciso agrupar por `thread_id`, e o argumento é `None`, não `{}`.
  - O LangGraph não tem índice de threads. A tela "incidentes aguardando aprovação" vai depender de uma consulta nossa ou de uma tabela nossa.
- **`update_state(config, valores, as_node="no")`** cria um checkpoint novo, passando pelos reducers.
  - O `as_node` decide qual nó roda em seguida.
  - É obrigatório quando houve escrita paralela ou quando a thread ainda não tem histórico.
- **`checkpointer.delete_thread(thread_id)`** apaga uma thread.
  - Os checkpoints **crescem sem limite** e não existe API pública de poda. Vai precisar de um job de limpeza.

### 5.3 Modos de durabilidade (`durability=` em invoke/stream)
- `"exit"`: grava só no fim (com sucesso, erro ou interrupt). É o mais rápido, mas um crash perde tudo.
- `"async"`: grava em paralelo com o passo seguinte. Pode perder o último checkpoint.
- `"sync"`: grava antes do passo seguinte. É o mais seguro.
- Se o processo cair antes do primeiro checkpoint durável, a thread parece nunca ter existido: `get_tuple` devolve `None` e `invoke(None)` levanta `EmptyInputError`.
  - Para diferenciar "aceito e perdido" de "nunca recebido", **registre a admissão fora do checkpointer**, numa tabela de incidentes nossa, antes do `invoke`.
- **Para nós:** `durability="sync"` em qualquer thread que chegue à aprovação humana.

### 5.4 Postgres
- **Instalação:** `pip install "psycopg[binary,pool]" langgraph-checkpoint-postgres`. Ainda **não está instalado** no ambiente: **[verificado]** `langgraph.checkpoint.postgres` não existe no `multiagent_env`.
- Uso síncrono:
  ```python
  from langgraph.checkpoint.postgres import PostgresSaver
  with PostgresSaver.from_conn_string(DB_URI) as cp:
      cp.setup()            # cria/migra as tabelas; rodar na primeira vez
      graph = builder.compile(checkpointer=cp)
  ```
- Uso assíncrono, que é o que o FastAPI vai usar:
  ```python
  from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
  async with AsyncPostgresSaver.from_conn_string(DB_URI) as cp:
      await cp.setup()
  ```
- Rode o `setup()` como **etapa de migração** (no deploy ou na subida do app). Os exemplos da documentação deixam essa linha comentada.
- **[a conferir na referência do pacote]** As 6 páginas não falam de `autocommit`, `row_factory` nem pool. De memória: ao passar uma conexão ou pool próprios em vez de `from_conn_string`, ela precisa de `autocommit=True` e `row_factory=dict_row`, e com pgbouncer também `prepare_threshold=0`. Conferir antes de implementar.
- **Store** (memória entre threads): `PostgresStore` / `AsyncPostgresStore` (`langgraph.store.postgres`), com `.setup()`.
- **Serialização:**
  - O padrão é `JsonPlusSerializer` (msgpack), que cobre Pydantic v2, dataclass e datetime.
  - `pickle_fallback=True` existe, mas é inseguro.
  - Criptografia: `EncryptedSerializer.from_pycryptodome_aes()`, com a chave em `LANGGRAPH_AES_KEY`. Fora do LangSmith, precisa ser configurada explicitamente.

### 5.5 Stores
- API:
  - `store.put(ns, key, value_dict, index=None|False|[campos])`;
  - `get(ns, key)`;
  - `search(ns_prefix, query=None, filter=None, limit=10, offset=0)`;
  - `list_namespaces(prefix=..., max_depth=...)`;
  - versões async com o prefixo `a`.
- O namespace é uma tupla de strings, por exemplo `("time-sre", "licoes")`.
- Pegadinhas:
  - O `search` casa **por prefixo**: `("a",)` também traz `("a","b")`.
  - O resultado é cortado no `limit` sem nenhum aviso.
  - A ordem muda conforme o backend: o Postgres traz o mais recente primeiro, o InMemory traz por ordem de inserção.
- Busca semântica: `index={"embed": ..., "dims": N, "fields": [...]}`.
  - Os exemplos usam `init_embeddings`, do `langchain`.
  - **[a conferir]** A documentação não deixa claro se `embed` aceita uma função comum `list[str] -> list[list[float]]` no Postgres. No exemplo do MongoDB, aceita.
  - Não precisamos disso para a busca de incidentes, que continua sendo a nossa `busca.py`.
- Acesso no nó: `runtime.store`.

### 5.6 DeltaChannel (beta) e versões
- O `DeltaChannel` guarda deltas em vez do valor inteiro.
- Checkpoints gravados nesse formato **não são lidos por versões antigas**.
- **Fixar a versão do `langgraph`** no requirements.

## 6. Interrupts (human-in-the-loop)

- **Pré-requisitos:** um checkpointer durável, `thread_id` e um payload JSON-serializável.
- `valor = interrupt(payload, response_schema=None)`:
  - por baixo, levanta uma exceção especial que pausa o grafo;
  - a pausa dura indefinidamente;
  - a retomada é `Command(resume=valor)` com o **mesmo `thread_id`**;
  - **o nó roda de novo desde o começo**.
- **[verificado]** O `response_schema` (≥1.2.12) existe na versão instalada.
  - Com Pydantic, TypedDict ou dataclass, o `interrupt()` devolve o objeto validado. Uma resposta inválida levanta `ValidationError`, e dá para mandar outro `resume` na mesma thread.
  - Um JSON Schema em dict só é exposto, sem validação.
- **Onde aparece o interrupt:**
  - no `invoke` com `version="v2"`: em `result.interrupts`. O acesso `result["__interrupt__"]` está deprecated;
  - no event streaming: em `stream.interrupted` e `stream.interrupts`, uma tupla de `Interrupt` com `.value` e `.id`.
- **Interrupts paralelos** (vários ramos no mesmo passo) se retomam com um mapa: `Command(resume={intr.id: valor, ...})`.
- **Regras:**
  1. **Não envolver `interrupt()` num `try/except Exception`.** O except engole a pausa.
  2. **A ordem dos interrupts dentro de um nó é casada por índice.** Não pule interrupts condicionalmente e não faça laços com quantidade variável de interrupts.
  3. O payload deve ser simples: str, int, bool, dict e listas desses tipos.
  4. **Efeitos colaterais antes do `interrupt` se repetem na retomada.** Coloque-os depois do interrupt, ou num nó separado, sempre de forma idempotente.
  5. **Validar a resposta humana com um interrupt por execução do nó**, voltando ao mesmo nó por uma aresta condicional se for inválida. Nada de `while True` dentro do nó.
- **Padrões:**
  - aprovar ou rejeitar: `Command[Literal["seguir", "cancelar"]]`;
  - revisar e editar: o humano devolve o texto editado;
  - interrupt dentro de uma ferramenta.
  - O tutorial SQL usa três respostas: `accept`, `edit` e `response`, em que um feedback em texto volta para o LLM.
  - **Pegadinha da própria documentação:** no tutorial, o handler do `edit` lê `response["args"]["args"]`, mas o exemplo de retomada manda `{"args": {...}}`. Não copie esse trecho como está.
- **Breakpoints estáticos** (`interrupt_before`/`interrupt_after`, no compile ou no invoke) servem para debug e testes, não para human-in-the-loop. A retomada é `invoke(None, config)`.

## 7. Streaming

### 7.1 Stream modes (`graph.stream` / `astream`)

| Modo | O que sai |
|---|---|
| `values` | estado completo depois de cada passo |
| `updates` | `{no: delta}` de cada nó |
| `messages` | tokens `(chunk, metadata)`. **Só funciona com chat model do LangChain** |
| `custom` | o que o nó escreve com `get_stream_writer()` (`langgraph.config`) |
| `checkpoints`, `tasks`, `debug` | eventos do checkpointer (exigem checkpointer) |

- **`version="v2"`** (≥1.1): todo chunk vem como `{"type", "ns", "data"}`, e o `invoke` devolve `GraphOutput(.value, .interrupts)`.
  - Sem `version`, vale o formato v1, que usa tuplas.
  - Use v2 em código novo.
- **`subgraphs=True`** inclui eventos dos subgrafos, com o caminho em `ns`.
- **Para nós:** os tokens do LLM saem pelo modo `custom`, com o nó repassando cada pedaço do SDK. O progresso das etapas sai pelo modo `updates`.

### 7.2 Event streaming (`stream_events`, `version="v3"`, 1.2+)
- É a camada que a documentação recomenda para aplicações novas. Um único run expõe várias projeções ao mesmo tempo:
  - `stream.values`, `stream.messages`, `stream.subgraphs`;
  - `stream.interrupts` e `stream.interrupted`;
  - `stream.output`, que espera o fim;
  - `stream.extensions`.
- No modo síncrono, `stream.interleave("values", "messages")` devolve os eventos na ordem de chegada.
- **[verificado]** O `version` padrão dos dois métodos é `"v2"`, então é preciso passar `version="v3"` explicitamente.
  - `astream_events` devolve um `Awaitable` no v3, por isso a documentação usa `stream = await graph.astream_events(..., version="v3")`. Não é erro.
- **Eventos brutos** (`ProtocolEvent`):
  - campos `seq`, `method` e `params{namespace, timestamp, data}`;
  - ordene pelo `seq`, nunca pelo `timestamp`;
  - canais: `values`, `updates`, `messages`, `tools`, `lifecycle`, `checkpoints`, `tasks`, `custom:<nome>`.
- **`StreamTransformer`** (com `init`, `process`, `finalize` e `fail`, mais `StreamChannel("nome")`) cria projeções próprias.
  - O exemplo da documentação **remove PII dos eventos antes de chegarem ao navegador**, o que pode servir para logs de incidente.
  - Registro: `compile(transformers=[...])` ou na própria chamada.
- **No FastAPI**, isso vira um endpoint SSE que repassa as projeções. Quando `stream.interrupted` for verdadeiro, ele devolve os interrupts e o `thread_id`, e um segundo endpoint faz a retomada. *(Isto é inferência minha; a documentação não fala de FastAPI.)*
- **Python 3.11 ou superior:** abaixo disso, `get_stream_writer()` não funciona em nós async. **[verificado]** O `multiagent_env` usa Python 3.12.3, então isso não nos afeta.

## 8. Padrões (workflows-agents) e o que cada um serve para nós

1. **Prompt chaining com gate:** extrair sintomas, buscar, gerar a hipótese e verificar se a hipótese cita evidência real.
2. **Paralelização:** buscar ao mesmo tempo no histórico (pgvector), em runbooks e em deploys recentes, com um nó agregador no fim.
3. **Roteamento:** classificar o incidente (rede, banco, deploy...) e seguir para um fluxo específico. Lembre do `else`.
4. **Orchestrator-worker com `Send`:** uma investigação por incidente similar encontrado, e o resultado volta por um reducer.
5. **Evaluator-optimizer:** um crítico avalia a hipótese. **Ponha limite de iterações**: os exemplos da documentação não têm e podem rodar para sempre. O humano pode fazer o papel do avaliador.
6. **Laço de agente:** `llm → (tool_calls?) → tools → llm`. Sem LangChain, é um nó que chama o SDK com tools e um nó que despacha `tools_by_name[nome](**args)` e devolve o resultado.
   - O `ToolNode` (`langgraph.prebuilt`) espera mensagens do `langchain-core`.
   - **[a conferir]** se vale usar o `ToolNode` ou um despachante nosso.

**Lições do tutorial de RAG agêntico** (nós: `generate_query_or_respond`, `retrieve`, `grade_documents`, `rewrite_question`, `generate_answer`):
- A ferramenta devolve **só o texto** e perde os ids. A nossa precisa devolver `doc_id`, título e score para a hipótese poder citar.
- O tutorial usa `messages[0]` como a pergunta, o que quebra com várias trocas. Guarde a pergunta num campo próprio do estado.
- A reescrita da pergunta não tem limite. Ponha um contador e uma saída do tipo "evidência insuficiente".
- O prompt de avaliação trata o documento como **dado, não como instrução**. É mitigação de prompt injection vinda do corpus, e precisamos dela porque os postmortems vêm da web.

**Lições do tutorial do agente SQL:**
- As regras de segurança ficam **só no prompt**: o `check_query` é feito por LLM e não é controle de verdade.
- O controle de verdade é: usuário de banco somente leitura, allowlist, validação determinística, timeout e limite de linhas no código, e aprovação humana. É a Regra dos Dois do livro, na configuração [AB].

## 9. Functional API

- `@entrypoint(checkpointer=...)` recebe **um argumento posicional**. Pode receber também `previous`, `config`, `runtime`, `store` e `writer`.
- `@task` devolve um future (`.result()` ou `await`). O resultado é checkpointado e não é refeito na retomada.
- Na retomada, o entrypoint roda de novo desde o início, e as tasks já concluídas vêm do checkpoint.
- Regras:
  - efeitos colaterais e valores não determinísticos (tempo, aleatoriedade) **só dentro de task**;
  - entradas e saídas precisam ser JSON-serializáveis;
  - a ordem dos interrupts é fixa.
- **Não tem desenho do grafo.** A documentação recomenda a Graph API para agentes novos.
- **Para nós:** Graph API, por causa do desenho, do estado explícito e dos ramos claros.

## 10. Subgrafos

- **Duas formas de usar:**
  - **Como nó** (`add_node("x", subgrafo_compilado)`), quando compartilha chaves com o pai.
  - **Chamado dentro de um nó** (`sub.invoke(mapeado)`), quando os schemas são diferentes.
- **Persistência** pelo `compile(checkpointer=...)` do subgrafo:
  - `None` (padrão): **por invocação**. Herda o checkpointer do pai, suporta interrupt e começa do zero a cada chamada. É o recomendado.
  - `True`: **por thread**. Acumula estado entre chamadas, mas **não aceita duas chamadas paralelas ao mesmo subgrafo**.
  - `False`: sem estado e sem interrupt.
- **Inspeção:** `get_state(config, subgraphs=True).tasks[0].state`.
  - Não funciona se o subgrafo for chamado de dentro de uma ferramenta.
  - Mesmo assim, os interrupts sempre sobem até o grafo de cima.
- **Time travel:** por padrão, o subgrafo conta como um único passo do pai. Para voltar a um ponto no meio dele, ele precisa de `checkpointer=True`.

## 11. Time travel

- **Replay:** `invoke(None, snapshot.config)`. Os nós depois do checkpoint **rodam de novo**, incluindo chamadas ao LLM e interrupts. Não há cache.
- **Fork:** `cfg = update_state(snapshot.config, {...})` e depois `invoke(None, cfg)`. Cria um ramo novo e o histórico original continua intacto.
- **Para nós:** serve para reproduzir uma triagem com outro prompt ou modelo a partir do mesmo ponto. É o "replay de trajetória" que o livro recomenda para avaliação.

## 12. Testes

- Monte o grafo numa função `criar_grafo()` e compile **em cada teste** com um `InMemorySaver()` novo e um `thread_id` próprio.
- **Nó isolado:** `compilado.nodes["no"].invoke(estado)`. Ignora o checkpointer.
- **Trecho do grafo:** `update_state(config, valores, as_node="no_anterior")` e depois `invoke(None, config, interrupt_after="ultimo_no")`.
- **LLM falso:** sem LangChain, basta injetar um cliente fake pelo `context_schema`. É mais simples que o `GenericFakeChatModel`.
- **Para nós:** os testes de fluxo rodam sem LLM e sem rede. A avaliação de qualidade (hipótese contra ficha) é outra suíte, com o LLM real.

## 13. Compatibilidade de versões do grafo (threads pausadas)

O código novo vale para **todas** as threads, inclusive as pausadas. Não há pinagem de versão por execução.

- **O que quebra:**
  - renomear ou remover um nó em que uma thread esteja pausada, ou para onde ela vá em seguida;
  - renomear uma chave do estado: o valor salvo some;
  - tornar um campo obrigatório ou com tipo mais estreito.
- **O que é seguro:**
  - mudar arestas entre nós que continuam existindo, porque a topologia não é persistida;
  - adicionar nós;
  - adicionar campos como `NotRequired`.
- **Padrões recomendados:**
  - renomear em duas etapas: adiciona o novo, escreve nos dois e depois remove o antigo;
  - gravar `flow_version` no estado logo no primeiro nó e rotear com `state.get("flow_version", 1)`.
- **Para nós:** escolher bem os nomes dos nós e das chaves desde o início e gravar `flow_version` desde a primeira versão.

## 14. Deploy, Studio e observabilidade (o que precisa de LangSmith)

| Item | Precisa de conta ou serviço pago? | Decisão |
|---|---|---|
| biblioteca `langgraph` + checkpointer/store Postgres | não (open source) | **usar** dentro do nosso FastAPI |
| `langgraph dev` (servidor local, `langgraph-cli[inmem]`) | a documentação pede API key do LangSmith; o estado fica em memória e serve só para desenvolvimento | dispensável |
| LangSmith Studio | conta e API key; a interface é servida de smith.langchain.com. Com `LANGSMITH_TRACING=false`, a documentação diz que nenhum dado sai | opcional, só para depurar com dados sintéticos |
| Agent Server / LangSmith Deployment (cloud, hybrid, self-hosted) | plataforma LangSmith; licença e preço não aparecem nas páginas | **não usar** |
| Agent Chat UI e hooks `useStream` (React/Vue/Svelte/Angular) | falam o protocolo do Agent Server | não servem para um FastAPI nosso sem reimplementar o protocolo |
| Observabilidade | a documentação só cobre LangSmith (tracing, anonymizer por regex). **Não fala de OpenTelemetry** | nossos próprios logs: trajetória por `thread_id` a partir de `get_state_history` + modo `updates`/`tasks` |

- O `langgraph.json` (com `dependencies`, `graphs`, `env` e `dockerfile_lines`) só serve para o CLI e o Agent Server. Não precisamos dele.

## 15. Como fica o nosso desenho (sem LangChain)

```
START → registrar_incidente → buscar_historico → gerar_hipotese → verificar_citacoes
          ┌──────────── (citação inválida, tentativas < 2) ───────┘
          ▼                                                        │ ok
     gerar_hipotese                                                ▼
                                                    aprovar (interrupt) ─ rejeitar ─▶ END
                                                          │ aprovar/editar
                                                          ▼
                                                  redigir_postmortem → END
```

- **Estado** (TypedDict):
  - `flow_version`, `incidente_id`, `sintoma`;
  - `similares: list[dict]` com `doc_id`, título, score e trecho;
  - `hipotese: dict`, validada com Pydantic e com citações de `doc_id`;
  - `tentativas: int`;
  - `decisao: dict | None`;
  - `postmortem: str | None`.
- **Contexto (`context_schema`):** conexão do banco, cliente do LLM, nome do modelo e `dataset`. Nada disso vai para o checkpoint.
- **`registrar_incidente`:** grava o incidente numa tabela nossa, por upsert, **antes** de qualquer outra coisa. Cumpre ao mesmo tempo o papel do outbox da §5.3 e do índice de threads da §5.2.
- **`buscar_historico`:** chama a `busca.py` da E2 diretamente, sem `@tool`, porque é um passo fixo do workflow.
  - Configuração: `RetryPolicy` e `CachePolicy` opcional.
- **`gerar_hipotese`:** chama o SDK do provedor com saída estruturada e valida com Pydantic.
  - Faz streaming dos tokens pelo writer (modo `custom`).
  - Configuração: `RetryPolicy(retry_on=(erros de rate limit/timeout do SDK, ConnectionError))` e `timeout` (o nó é async).
- **`verificar_citacoes`:** sem LLM. Confere que cada `doc_id` citado está entre os `similares`. Se não estiver, volta ao `gerar_hipotese`, com limite de 2 tentativas.
- **`aprovar`:** `interrupt({...}, response_schema=Decisao)`, sem nenhum efeito colateral antes. Devolve `Command[Literal["redigir_postmortem", "__end__"]]`.
- **Compilação e execução:**
  - `AsyncPostgresSaver` no banco `incidentes` que já existe;
  - `durability="sync"`;
  - `stream_events(version="v3")` no FastAPI.
- **Nenhum nó executa ação em sistemas externos.** Sugere, não executa: é a configuração [AB] da Regra dos Dois.

### Dependências a adicionar quando for implementar
- `langgraph-checkpoint-postgres` e `psycopg[pool]`. O `psycopg` 3.3.8 já está instalado.
- O cliente do LLM. Escolha atual: `openai/gpt-oss-20b` no NVIDIA NIM (API no formato da OpenAI, chave em `.env`). Dá para chamar com `httpx`, que já está instalado, ou com o pacote `openai`.

### Testes do gpt-oss-20b no NIM (2026-11-09)
- **Resposta simples, chamada de ferramenta e streaming:** funcionam. O raciocínio do modelo vem em `message.reasoning_content` e não deve ser mostrado ao usuário final.
- **Resposta estruturada:**
  - **Funciona com uma chamada de ferramenta obrigatória** (`tools` = schema + `tool_choice` apontando para a função): o modelo devolveu JSON válido, com as citações certas, em 208 tokens.
  - **Não funcionam:** o `response_format` com `json_schema` devolveu JSON quebrado seguido de linhas em branco até o limite de tokens; o `guided_json` (dentro de `nvext` ou no topo do corpo) foi ignorado e voltou texto livre.
  - Mesmo com a ferramenta obrigatória, validar com Pydantic e tentar de novo se falhar.
- **Latência:** de 2 a 2,5 minutos por chamada, porque o plano gratuito tem fila. Na primeira tentativa, três chamadas estouraram 90–120 s sem resposta.
  - No grafo: `timeout` alto (cerca de 300 s), `retry_on` com o timeout do httpx e `durability="sync"`.
  - Com essa espera, uma suíte de avaliação de centenas de chamadas fica inviável.
- No mesmo NIM, o `gpt-oss-120b` e o `llama-3.3-70b` já respondem 410 (desativados). A página do modelo o chama de "trial service", sem data de fim.
- Fixar `langgraph==1.2.20` (ou a versão do momento) no requirements.

## 16. Lacunas desta leitura

- O `autocommit`, o `row_factory` e o pool do `PostgresSaver` não estão nas páginas do LangGraph. Precisam ser conferidos na referência do `langgraph-checkpoint-postgres` ou no código do pacote depois de instalado.
- Não fica claro se `PostgresStore(index={"embed": função})` aceita uma função comum. Não precisamos disso agora.
- A licença e o custo do Agent Server self-hosted não aparecem nas páginas. Não vamos usar.
- OpenTelemetry não é coberto na documentação do LangGraph.
- O formato exato do campo `interrupts` nas parts `values` do v2 não aparece na documentação. Conferir no protótipo.
- Os IDs de interrupt são gerados pelo runtime, e a documentação não diz se são estáveis entre execuções. Conferir no protótipo.
