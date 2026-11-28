# E5 — Esboço do estado compartilhado e dos formatos dos agentes

**Situação (25/11):** estado, Diagnóstico e grafo implementados (`agents/orchestration/graph.py`, com demo e testes
de integração — ver `agents/orchestration/README.md`); o Relatório da Mari (`agents/reporting`) está ligado ao grafo
e faz a própria validação; o incidente duplicado também é dela (`agents/reporting/related.py`). Começou como proposta para a equipe revisar. Os nomes de código estão
em inglês, como nos agentes Triagem e Pesquisa; o texto do documento, em português.

**Objetivo:** fixar o que cada agente lê e escreve, para que o Diagnóstico, o Relatório e o grafo possam ser
feitos em paralelo sem um esperar o outro.

## 1. Decisões já tomadas

| Tema | Decisão |
|---|---|
| Fluxo | o da E1.2: Triagem → Pesquisa → Diagnóstico → roteamento → Relatório, com laço de refinamento e validação do relatório |
| Agentes no grafo | cada agente entra como nó, sem ser reescrito (como o `agents/triage/node.py`) |
| Memória de curto prazo | o estado da investigação, salvo pelo checkpointer do LangGraph com `thread_id = incident_id` |
| Checkpointer | Postgres (`langgraph-checkpoint-postgres`, no mesmo banco do Docker) na demonstração e no uso normal; `InMemorySaver` nos testes automáticos |
| Memória de longo prazo | o RAG dos post-mortems (já existe) |
| Pedido de dados ao analista | `interrupt()`: o grafo pausa, salva o estado e retoma com a resposta (`Command(resume=...)`) no mesmo `incident_id` |
| Contexto entre agentes | o estado guarda só resultados estruturados; o histórico de mensagens de cada agente fica dentro dele |
| Limite de chamadas | todas as chamadas ao LLM passam pelo `rag/limite_llm.py`, inclusive as do Triagem |
| Divisão | André: Diagnóstico, estado e grafo. Mari: Relatório e validação, Triagem no grafo. Juntos: testes de integração e demonstração |

## 2. O grafo

```
START → triage ─┬─ ask_user ──────────────► ask_analyst (interrupt) ──► triage
                ├─ tell_related_incident ─► related_incident (código) ──► END
                ├─ erro no Triagem ───────► report (inconclusivo)
                └─ go_to_research ────────► research ──► diagnosis ─┬─ evidência suficiente ─────────► report
                                               │ (falhou, nada encontrado ──► report inconclusivo)
                                               ▲                    ├─ refinar e ainda há tentativa ─► research
                                               └────────────────────┤
                                                                    ├─ faltam dados do incidente ────► ask_analyst
                                                                    └─ refinar, sem tentativa ───────► report (inconclusivo)
report ──► END   (desde 25/11: o agente da Mari valida e corrige o próprio relatório, até 3 tentativas;
                 o nó validate_report separado é opcional)
```

![Grafo principal da E5](e5_grafo_principal.svg)

Como ler o desenho: roxo são os agentes (usam o LLM), cinza é código Python, laranja é a pausa para o
analista e verde é o estado compartilhado. As setas tracejadas são as voltas: a resposta do analista volta ao
Triagem, o pedido de nova busca volta ao Pesquisa e o relatório inválido volta ao Relatório. Todos os nós leem
e escrevem o mesmo estado, salvo por `incident_id`.

| Nó | Tipo | Dono | O que faz |
|---|---|---|---|
| `triage` | agente | Mari | o `triage_node` (`agents/triage/node.py`), com os nomes do estado; desde 25/11 devolve todas as mudanças citadas em `triggers` e, quando já precisa perguntar o sintoma ou o serviço, pergunta junto se algo mudou antes do problema (política B; a A, perguntar sempre, ficou guardada para testes) |
| `related_incident` | código | Mari | `agents/reporting/related.py`: a resposta "já existe a investigação X", sem LLM, com a `message` em Markdown no idioma do analista |
| `research` | agente | André | chama o subgrafo do Agente Pesquisa com `description`, `symptoms` e, no refinamento, `search_request` e os achados anteriores |
| `diagnosis` | agente | André | lê os achados e escreve o `DiagnosisResult` |
| `ask_analyst` | código + `interrupt()` | André | pausa com as perguntas pendentes; ao retomar, junta a resposta à descrição e volta ao `triage` |
| `report` | agente | Mari | `agents/reporting/node.py`: escreve o `Report` (diagnóstico ou inconclusivo, com a `message` em Markdown para o chat) e o valida por dentro, corrigindo até 3 vezes; sem diagnóstico (agente anterior falhou), o grafo usa o relatório inconclusivo em código |
| `validate_report` | código | — | **opcional** desde 25/11: a validação ficou dentro do agente da Mari (`agents/reporting/validation.py`); o nó separado continua disponível em `build_graph(validate_report=...)` |

**Quem escreve as perguntas ao analista:** o agente que percebeu a falta.
- **Triagem** (falta informação para começar: o serviço, o gatilho): já é assim hoje. O agente da Mari escreve as
  perguntas em `missing_information`, no idioma do analista, e o caminho `ask_user` as devolve. A E1.2 não previa
  esse caso; ele nasceu na construção do Triagem.
- **Diagnóstico** (falta evidência do incidente atual para concluir, por exemplo o código de erro): **mudança em
  relação à E1.2**. Na E1.2, o Agente Relatório redigia esse pedido de dados. A proposta é o próprio Diagnóstico
  escrever as perguntas (`questions_for_analyst`), porque é ele que sabe o que falta; o Relatório só reescreveria a
  lista, com uma chamada ao LLM a mais e mais espera para o analista (limite de 10 chamadas por minuto).

Nos dois casos, as perguntas vão direto para o `ask_analyst` (código + `interrupt()`), que pode acrescentar um texto
fixo ("Para continuar a investigação, preciso de:"). O Relatório fica com o diagnóstico e o relatório inconclusivo.
**A confirmar com a Mari** (muda o que o Relatório faz).

## 3. O estado compartilhado (`InvestigationState`)

```python
class InvestigationState(TypedDict, total=False):
    # identificação e entrada
    incident_id: str                     # = thread_id do checkpointer
    description: str                     # mensagem do analista + respostas dele, juntas (entrada do Triagem e do Pesquisa)
    analyst_answers: Annotated[list[str], operator.add]  # respostas dadas aos pedidos de dados

    # Triagem
    triage_result: TriageResult          # o resultado completo (agents/triage/schema.py)
    symptoms: list[str]                  # = triage_result.symptoms (entrada do Pesquisa)

    # Pesquisa
    findings: list[dict]                 # saída do Agente Pesquisa (formato na seção 4)
    seen_ids: list[str]                  # incidentes já vistos (o refinamento não os traz de novo)
    search_request: str                  # pedido do Diagnóstico para a próxima busca; vazio na 1ª
    research_rounds: int                 # quantas vezes o Pesquisa rodou (limite: MAX_RESEARCH_ROUNDS = 3)

    # Diagnóstico
    diagnosis: DiagnosisResult

    # pedido de dados
    pending_questions: list[str]         # perguntas enviadas ao analista no interrupt()

    # Relatório
    report: Report
    report_problems: list[str]           # erros da validação, que voltam ao Relatório
    report_attempts: int                 # limite: 2 correções

    # controle
    route: str                           # última decisão do roteamento (para o registro e a demonstração)
    errors: Annotated[list[dict], operator.add]  # {"node": ..., "error": ...}: o que falhou e onde
    trace: Annotated[list[dict], operator.add]   # {"node": ..., "seconds": ..., "summary": ...}: passo a passo
```

O código está em `agents/orchestration/state.py`. As classes Pydantic que entram no estado (`TriageResult`,
`DiagnosisResult`, `Report`...) precisam estar na lista `STATE_CLASSES` desse arquivo: o checkpointer só lê de
volta os tipos registrados (sem a lista, o LangGraph avisa que vai bloquear numa versão futura).

**Quem lê e quem escreve:**

| Campo | Escreve | Lê |
|---|---|---|
| `incident_id`, `description` | entrada / `ask_analyst` | todos |
| `triage_result`, `symptoms` | `triage` | roteamento, `research`, `diagnosis`, `report` |
| `findings`, `seen_ids`, `research_rounds` | `research` | `diagnosis`, `report`, `validate_report` |
| `search_request` | `diagnosis` | `research` |
| `diagnosis` | `diagnosis` | roteamento, `report` |
| `pending_questions` | `triage` / `diagnosis` (via roteamento) | `ask_analyst` |
| `report`, `report_problems`, `report_attempts` | `report` / `validate_report` | `validate_report`, saída final |
| `errors`, `trace` | todos | roteamento, `report`, demonstração |

## 4. Saída do Agente Pesquisa (já existe)

Cada item de `findings` (até 8, os aprofundados primeiro):

```python
{
    "incident_id": "DAN-197", "company": "Metrist", "title": "...", "url": "https://...",
    "summary": "...", "similarity": 0.66,
    "deepened": True,                    # o LLM buscou causa e correção dentro dele
    "why": "...",                        # por que o LLM o escolheu (o que bate e o que não bate)
    "passages": [                        # até 7
        {"section": "Root cause", "content": "...", "similarity": 0.61,
         "origin": "deep_search",        # ou "similar" (busca inicial)
         "query_source": "fix"},         # "llm", "cause" ou "fix" (só em deep_search)
    ],
}
```

Para o Diagnóstico, o nó `diagnosis` monta um texto mais enxuto: os incidentes aprofundados com todos os
trechos, os demais só com título e resumo (a lista completa pode passar de 60 mil caracteres).

## 5. Saída do Agente Diagnóstico (`DiagnosisResult`)

```python
class Hypothesis(BaseModel):
    cause: str                           # causa provável do incidente atual, em 1 ou 2 frases
    based_on: list[str]                  # incident_ids dos achados que sustentam a hipótese (pelo menos 1)
    matches: str                         # o que bate entre o incidente atual e os passados
    differs: str                         # o que não bate
    same_trigger: Literal["yes", "no", "unknown"]  # o gatilho do caso passado é do mesmo TIPO? (unknown: gatilho atual desconhecido)
    same_component: Literal["yes", "no"]           # o componente que falhou é do mesmo TIPO?
    same_mechanism: Literal["yes", "no"]           # o que quebrou, e como se espalhou, explica os sintomas atuais?
    confidence: Literal["high", "medium", "low"]   # já com o teto aplicado pelo código

class DiagnosisResult(BaseModel):
    hypotheses: list[Hypothesis]         # até 3, da mais à menos provável
    evidence_sufficient: bool            # decidido pelo código
    gaps: list[str]                      # o que falta para ter certeza
    next_step: Literal["report", "refine_search", "ask_analyst"]  # decidido pelo código
    search_request: str = ""             # preenchido só se next_step == "refine_search"
    questions_for_analyst: list[str] = []  # preenchido só se next_step == "ask_analyst" (idioma do analista)
```

**Quem decide o quê (mudança de 24/11).** O modelo escreve um rascunho (`DiagnosisDraft`): as hipóteses, com as
três comparações (`same_trigger`, `same_component`, `same_mechanism`), as lacunas, uma busca sugerida (sempre, em inglês) e até 3
perguntas ao analista (opcional). O **código** (`decide()` em `agents/diagnosis/schema.py`) transforma o rascunho
no `DiagnosisResult`:

1. **Teto da confiança:** `high` só com mesmo tipo de gatilho, de componente **e** mesmo mecanismo; senão, no
   máximo `medium`; com gatilho e componente diferentes, `low`.
2. **Evidência suficiente:** alguma hipótese `high` ou `medium`, com o mesmo tipo de componente, o mesmo mecanismo,
   baseada em pelo menos um incidente **aprofundado** (com trechos) e com o gatilho igual — ou desconhecido, a
   partir da 2ª rodada (com gatilho desconhecido, na 1ª rodada qualquer caso do mesmo tipo de componente passava;
   uma nova busca é tentada antes).
3. **Próximo passo:** basta → `report`; não basta → `refine_search` enquanto houver rodadas (e uma busca
   sugerida); senão `ask_analyst`, se houver perguntas; senão `report` (inconclusivo).

**Por quê:** nos testes, quando o modelo decidia sozinho, ele disse "a evidência basta" em 24 de 24 respostas,
mesmo quando o próprio campo `differs` dizia que o caso passado era outro tipo de falha (por exemplo, MySQL com
proxy contra Postgres reduzido); `refine_search` nunca foi escolhido. Pedir um aviso mais rígido no prompt não
resolveu. Com as duas comparações e a decisão no código, nos casos em que o Pesquisa não trouxe o incidente certo,
o Diagnóstico passou a pedir nova busca, e os casos que acertavam continuaram certos (resultados em
`agents/orchestration/experiments/results/diagnosis_cases_2026-11-24_*.json`; análise completa em
`results/E5_testes_diagnostico_2026-11-24.md`).

**Modelo do Diagnóstico:** raciocínio desligado e temperatura 0 (`agents/diagnosis/agent.py`). Num teste de 7
configurações × 6 casos × 3 repetições sobre os mesmos achados, foi a mais rápida das estáveis (29 s por chamada
contra 52–74 s), sem respostas inválidas, e a única que não aceitou uma causa errada no caso mais difícil. Com o
raciocínio ligado e 4096 tokens, o raciocínio às vezes gastava o limite e a resposta vinha vazia.

**Várias mudanças e pedidos repetidos (25/11):** o Diagnóstico recebe todas as mudanças citadas (`triggers` do
Triagem) e escreve uma hipótese por mudança quando os casos passados apoiam mudanças diferentes, sem supor que a mais
recente é a causa. Ele também recebe o pedido de busca anterior e não deve repeti-lo; se repetir, recebe uma chance de
reescrever (se insistir, o pedido é aceito: o Pesquisa já exclui os incidentes vistos).

**Refinamento no Pesquisa:** numa nova rodada, o código busca com o `search_request` e com a `description`,
**excluindo todos os incidentes já vistos** (`seen_ids`); o LLM do Pesquisa escolhe só entre os novos; os
incidentes aprofundados nas rodadas anteriores voltam aos `findings`, depois dos novos aprofundados. Antes, o LLM
recebia os achados antigos como lista principal e o refinamento trazia os mesmos 8 incidentes.

**Regras de consistência** (no esquema, como no `TriageResult`):
- `evidence_sufficient` verdadeiro → `next_step == "report"` e pelo menos 1 hipótese;
- `refine_search` → `search_request` não vazio; `ask_analyst` → `questions_for_analyst` não vazio.

**Regras em código** (no agente, como no `agents/triage/agent.py`): todo `incident_id` de `based_on` tem de estar
nos `findings`; se não estiver, o erro volta ao modelo e ele corrige.

Sem confiança numérica (0–1): o livro do Dibia recomenda categorias com justificativa, porque o número
gerado pelo LLM não é calibrado.

**Ferramenta: começar sem, acrescentar se os testes mostrarem necessidade.** A primeira versão do Diagnóstico
não tem ferramenta: quando a evidência não basta, ele pede uma nova busca (`refine_search`). Se nos testes
aparecerem diagnósticos travados por falta de um detalhe de um incidente que já está nos achados, entra a
ferramenta `check_incident`:

- **O que faz:** lê mais trechos de **um incidente que já está nos `findings`**, procurando por uma pergunta.
  Exemplo: `check_incident("DAN-197", "how did they detect that Azure changed the API?")`.
- **Como:** reaproveita a busca dentro de um incidente do Pesquisa (`search_in_incident` em
  `agents/research/tools.py`): compara a pergunta com os chunks daquele post-mortem e devolve os 2 ou 3 mais
  parecidos, sem repetir os que o Diagnóstico já recebeu. Não chama o LLM; é uma consulta ao banco.
- **Limites:** só aceita incidentes dos `findings` e até 2 chamadas por diagnóstico.
- **Diferença para o `refine_search`:** a ferramenta olha **dentro** de um incidente já encontrado, para
  confirmar um detalhe (versão, gatilho, configuração alterada); o `refine_search` volta ao Pesquisa para
  achar **outros** incidentes, e custa uma rodada inteira (1 ou 2 chamadas ao LLM e um novo diagnóstico).

**E o texto completo?** O banco não guarda o post-mortem inteiro numa coluna só, mas ele pode ser remontado:
os chunks de cada incidente estão numerados na ordem do documento (`DAN-001-001`, `DAN-001-002`...), e juntá-los
devolve o texto, com pequenas repetições (o título da seção repetido no começo dos chunks de uma seção longa e
até 60 tokens de sobreposição quando um parágrafo foi dividido). O tamanho é o problema: a mediana é de ~10 mil
caracteres por incidente, 10% passam de 23 mil, e o maior tem 150 mil. Mandar o texto inteiro ao LLM gastaria
muito contexto e pesaria no limite do NIM. Por isso a ferramenta devolve trechos escolhidos pela pergunta; uma
variante "texto completo" só faria sentido com um teto de tamanho (por exemplo, até 15 mil caracteres).

**Roteamento depois do Diagnóstico (código):**

| Condição | Próximo nó |
|---|---|
| `evidence_sufficient` | `report` (diagnóstico) |
| `next_step == "ask_analyst"` | `ask_analyst` |
| `next_step == "refine_search"` e `research_rounds < MAX_RESEARCH_ROUNDS` | `research` |
| qualquer outro caso, ou erro no Diagnóstico | `report` (inconclusivo) |

## 6. Saída do Agente Relatório (`Report`)

O que a E1 pede para cada causa provável: causa raiz histórica, passos de correção, código ou configuração
alterados, checklist de prevenção, link para o post-mortem e nível de confiança.

```python
class Source(BaseModel):
    incident_id: str
    title: str
    url: str

class ReportCause(BaseModel):
    root_cause: str                      # a causa no incidente histórico e por que se aplica ao atual
    remediation_steps: list[str]         # o que foi feito para corrigir
    changes: str | None = None           # código ou configuração alterados, se o post-mortem disser
    prevention_checklist: list[str]
    sources: list[Source]                # pelo menos 1
    confidence: Literal["high", "medium", "low"]

class Report(BaseModel):
    incident_id: str
    kind: Literal["diagnosis", "inconclusive"]
    summary: str                         # 2 a 3 frases para o analista
    causes: list[ReportCause]            # pelo menos 1 em "diagnosis"; pode ser vazio em "inconclusive"
    gaps: list[str]                      # obrigatório em "inconclusive"
    suggested_checks: list[str]          # o que o analista pode verificar agora
```

O relatório sai no idioma do analista, como as perguntas do Triagem.

**Validação em código (`validate_report`):**
- todo `incident_id` das fontes existe nos `findings`, e o `url` é o mesmo dos `findings` (o modelo não
  inventa link);
- `diagnosis` tem pelo menos 1 causa, e cada causa tem pelo menos 1 fonte;
- `inconclusive` tem pelo menos 1 lacuna.

Se falhar, os problemas vão para `report_problems` e o Relatório tenta de novo (até 2 vezes). Se ainda falhar,
o código monta um relatório inconclusivo com os achados e as lacunas, para o fluxo nunca terminar sem resposta.

## 7. Pausa e retomada (`interrupt()`)

```python
def ask_analyst(state):
    answer = interrupt({"incident_id": state["incident_id"], "questions": state["pending_questions"]})
    return {"description": state["description"] + "\n\nAnalyst answer: " + answer,
            "analyst_answers": [answer], "pending_questions": []}
```

- O nó **roda de novo do começo** quando o grafo é retomado, por isso não há nada caro (chamada ao LLM) antes
  do `interrupt()`.
- Retomar: `graph.invoke(Command(resume=resposta), {"configurable": {"thread_id": incident_id}})`.
- **Depois da resposta, a investigação recomeça** com a descrição enriquecida: o Triagem lê de novo e o Pesquisa
  busca do zero (`research_rounds`, `findings`, `seen_ids` e `search_request` zerados). Assim, uma pergunta feita
  pelo Diagnóstico na última rodada ainda leva a uma busca nova.
- **No máximo `MAX_ANALYST_ROUNDS = 3` respostas** por investigação (contadas em `analyst_answers`, perguntas do
  Triagem e do Diagnóstico juntas); depois disso, o relatório sai inconclusivo em vez de outra pergunta.
- Com o Postgres, a pausa sobrevive ao fim do programa: o analista pode responder depois, em outra execução.

## 8. Tratamento de erros

| Situação | O que acontece |
|---|---|
| erro passageiro do NIM (tempo esgotado, 429, 5xx) | `limite_llm` espera e tenta de novo; o nó tem `RetryPolicy` |
| agente esgota as tentativas | o nó grava o erro em `errors` e o roteamento segue para o `report` inconclusivo |
| Pesquisa falha na 1ª rodada (nada encontrado) | vai direto ao `report` inconclusivo, sem chamar o Diagnóstico |
| Pesquisa falha num refinamento | a rodada conta; o Diagnóstico segue com os achados anteriores |
| resposta fora do formato | o erro volta ao modelo dentro do agente (como no Triagem e no Pesquisa) |
| relatório inválido | volta ao `report` até 2 vezes; depois, relatório inconclusivo montado em código |
| laço de refinamento | no máximo `MAX_RESEARCH_ROUNDS = 3` rodadas do Pesquisa (1ª + 2 refinamentos) |

## 9. Onde fica o código

```
agents/
  triage/          (existe)  node.py com os nomes do estado (description, symptoms)
  research/        (existe)  o subgrafo; o nó research fica em orchestration/graph.py
  diagnosis/       (feito)   agent.py, prompts.py, schema.py, tests/ (o nó diagnosis fica em graph.py)
  reporting/       (Mari)    agent.py, prompts.py, schema.py, validation.py, node.py, tests/, README.md
  orchestration/   (feito)   state.py, graph.py, run.py (demonstração), tests/ (estado e integração),
                             experiments/ (testes com o modelo real), README.md
```

## 10. Testes de integração (5.5)

Com `InMemorySaver` e, quando possível, agentes falsos (como o `agents/triage/tests/test_node.py`), além de
algumas rodadas com o modelo real. **Situação (25/11):** os 8 cenários estão em
`agents/orchestration/tests/test_graph.py` com agentes falsos (33 verificações, todas passando; o 6 com o mesmo
`InMemorySaver` e um grafo novo); com o modelo real e o Postgres, a demo rodou o 2 + 6 (pausa e retomada em outra
execução) e o 4 (fora do corpus → 3 rodadas → pergunta ao analista → retomada → relatório inconclusivo); com o
Relatório da Mari, o 1 (DAN-104 → relatório de diagnóstico válido na 1ª tentativa). O 8 é coberto pelos testes do
próprio agente (`agents/reporting/tests/test_validation.py`) e, no grafo, com o nó de validação opcional.

1. problema novo com caso parecido no corpus → relatório de diagnóstico com fontes válidas;
2. mensagem vaga → pausa com perguntas; retomada com a resposta → segue até o relatório;
3. duplicado → resposta com o `incident_id`, sem chamar o Pesquisa;
4. problema fora do corpus → refinamento até o limite → relatório inconclusivo;
5. refinamento que melhora a evidência: o incidente certo aparece na 2ª busca;
6. retomada em outra execução (Postgres), com o mesmo `incident_id`;
7. falha do LLM ou resposta inválida → o fluxo não quebra e termina com relatório inconclusivo;
8. relatório com link inventado → a validação rejeita e o Relatório corrige.

## 11. Pontos para a equipe confirmar

**Decididos (23/11):**
- o Diagnóstico começa sem ferramenta; a `check_incident` entra só se os testes mostrarem necessidade (seção 5);
- `MAX_RESEARCH_ROUNDS = 3` e até 2 correções do relatório;
- o relatório sai no idioma do analista.

**Para a Mari confirmar:**
1. O Diagnóstico escreve as próprias perguntas ao analista, sem passar pelo Relatório, como o Triagem já faz
   (seção 2; mudança em relação à E1.2).
2. Os nomes do estado (seção 3): o `node.py` do Triagem passa a usar `description` e `symptoms`.
3. A hipótese do Diagnóstico ganhou `same_trigger`, `same_component` e `same_mechanism`, e `evidence_sufficient` e
   `next_step` passaram a ser decididos pelo código (seção 5). O formato do `DiagnosisResult` é o mesmo; o
   Relatório pode ignorar os campos novos ou usá-los para explicar a confiança.
4. `chat()` em `agents/triage/llm.py` ganhou `temperature` e opções extras para o NIM (usadas pelo Diagnóstico); sem
   elas o comportamento é o de antes, e o Triagem não mudou.

## 12. Resumo simples

**O que é este documento:** um contrato entre as partes. Ele combina o que cada agente recebe e o que entrega,
para que cada um possa construir a sua parte sem esperar a do outro. Como cada agente funciona por dentro
(prompt, ferramentas, número de chamadas) fica a critério de quem o faz.

**Como os agentes se comunicam:** eles não conversam entre si. Existe uma "pasta da investigação" (o estado
compartilhado) que passa de mão em mão. Cada agente lê dela o que precisa, faz o seu trabalho e escreve o
resultado de volta. Depois de cada agente, um trecho de código olha a pasta e decide quem trabalha em seguida.
A pasta fica salva no banco, identificada pelo número do incidente; por isso a investigação pode parar e
continuar depois.

**O caminho de uma investigação:**
1. O analista descreve o problema.
2. O **Triagem** separa os sintomas. Se falta informação, o sistema pausa e pergunta ao analista; quando ele
   responde, o Triagem lê de novo. Se o problema já está sendo investigado, o sistema avisa e termina.
3. O **Pesquisa** encontra incidentes passados parecidos e os trechos de causa e correção.
4. O **Diagnóstico** propõe as causas mais prováveis e compara cada uma com o caso passado (mesmo tipo de
   gatilho? mesmo tipo de componente?). A partir dessas comparações, um código decide se a evidência basta. Se
   não basta, pede uma nova busca (no máximo 3 rodadas) ou pergunta ao analista.
5. O **Relatório** escreve a resposta final: o diagnóstico, com causa, correção, prevenção e links dos
   post-mortems, ou um relatório inconclusivo, explicando o que faltou.
6. Um código confere o relatório (os links existem? cada causa tem fonte?). Se algo estiver errado, o
   Relatório corrige.

**Se algo der errado:** o erro fica registrado, e o sistema termina com um relatório inconclusivo. Ele nunca
fica sem resposta.

**Quem faz o quê:** André faz o Diagnóstico, o estado e o grafo; Mari faz o Relatório com a validação e liga o
Triagem ao grafo; os dois fazem juntos os testes de integração e a demonstração.

**O que falta combinar:** os 4 pontos da seção 11 que dependem da Mari.
