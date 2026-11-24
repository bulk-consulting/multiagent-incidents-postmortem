# E5 — Testes da ligação Triagem → Pesquisa (2026-11-23)

Objetivo: decidir **o que o Agente Triagem entrega ao Agente Pesquisa** antes de montar o grafo da E5. Todos os
testes usam o código da Mari (`agents/triage`) sem alterações: as variantes do Triagem trocam o prompt e o
esquema só durante o experimento (`agents/orchestration/experiments/`).

## 1. Resumo

1. **Os sintomas do Triagem não servem como consulta de busca.** Eles descrevem o que falha, mas perdem o gatilho
   e as pistas de causa, que são o que distingue um incidente de outro. Usados como buscas separadas, derrubam o
   modo padrão do Pesquisa (17 → 13 de 20).
2. **O Triagem atual não pergunta o que mudou antes do problema.** Numa conversa em que o analista começa com uma
   mensagem vaga, o gatilho se perdeu em **15 de 15** conversas.
3. **Perguntando pelo gatilho uma vez, junto com a pergunta do serviço**, o gatilho foi capturado em **48 de 48**
   conversas com gatilho conhecido, **sem nenhuma volta a mais**. Com a regra ajustada (seção 5), ele também
   deixou de perguntar quando o analista já disse que não sabe o que mudou (36 de 36 execuções corretas).
4. **Com os casos reescritos sem o vocabulário do post-mortem (o teste mais realista), a conversa colada — o
   texto que o contrato da E5 já guarda em `description` — foi a melhor entrada para o Pesquisa**: post-mortem
   certo aprofundado em 32 de 36 execuções no modo híbrido, igual à mensagem completa de um analista (32 de 36) e
   acima do `search_text` resumido pelo Triagem (28 de 36). O resumo perde detalhes que ajudam a busca.
5. **O LLM do modo híbrido recupera boa parte do que a busca em código perde**: com a conversa colada, a busca em
   código punha o certo entre os 10 primeiros em 30 de 36; o híbrido o aprofundou em 32 de 36 (inclusive o
   DAN-018, que a busca em código não achava em nenhuma entrada).
6. Com os casos originais (que repetem as palavras do post-mortem), quase toda entrada punha o certo em 1º; esses
   números são otimistas (seção 6).

## 2. Testes com as 32 perguntas da E3/E2 (mensagens completas)

Arquivos: `results/triage_2026-11-23_1639.json`, `results/triage_v2_2026-11-23_1730.json`,
`results/retrieval_variants_2026-11-23_1825.json`, `results/analise_triagem_e_hibrido_2026-11-23.md` e as rodadas
`research_2026-11-23_*` em `agents/research/experiments/results/`.

**Triagem:** 21 seguiram para o Pesquisa e 11 foram barradas, todas por não dizer o nome do serviço (inclusive
mensagens bem descritas, como "nosso serviço falha nas chamadas à API de um provedor de nuvem"). Uma pergunta
sobre o histórico (q11) não tem caminho no fluxo.

**O que entra no Pesquisa** (incidente certo aprofundado, 20 perguntas com gabarito):

| Entrada | Padrão | Híbrido |
|---|---|---|
| mensagem original | 17 | 19 |
| mensagem + 1 busca por sintoma (como o código fazia) | 13 | 17 |
| resumo do incidente escrito pelo Triagem | 15 | 16 |
| mensagem + sintomas numa busca só (2 rodadas) | 17 / 17 | 17 / 18 |

Com mensagens completas, nenhuma entrada superou a mensagem original. O teste só da busca (sem LLM, determinístico)
explicou a queda do modo padrão: as buscas pelos sintomas curtos tiram o certo dos 10 candidatos.

## 3. Casos de post-mortem: mensagem completa × conversa

Para simular o uso real (o analista começa com pouco e o Triagem pergunta), 12 post-mortems do corpus foram
transformados por um LLM externo em: fatos visíveis durante o incidente, uma mensagem completa de analista, um
roteiro de conversa (a 1ª mensagem vaga e as respostas para serviço, gatilho, momento e sintomas) e o gabarito
descoberto depois (causa, correção, prevenção). Nomes anonimizados, sem datas.
Arquivos: `postmortems/DAN-xxx.json` (e o texto completo em `DAN-xxx.txt`).

| Casos | Gatilho conhecido durante o incidente |
|---|---|
| DAN-104, 145, 211, 125, 018, 017, 116, 164 | sim (comando, migração, recurso ligado, redução do banco, deploys, atualização de dados, reconstrução do standby) |
| DAN-004, 121, 154, 197 | não ("não sabemos o que mudou") |

Script: `run_triage_scenarios.py`. Cenário A: a mensagem completa, uma vez. Cenário B: a conversa; a cada pedido
do Triagem, um analista simulado responde com os itens do roteiro que casam com as perguntas (por palavras-chave,
reproduzível) e a resposta entra na descrição como no contrato ("Analyst answer: ...").

**Triagem atual + `trigger` e `search_text` (5 casos, 3 rodadas)** — `triage_scenarios_2026-11-23_1934.json`:

| | A: mensagem completa | B: conversa |
|---|---|---|
| seguiu para o Pesquisa | 15/15 | 15/15 (2 voltas; 1 vez sem perguntar nada) |
| gatilho capturado | 14/15 | **0/15** (nunca perguntou o que mudou) |

**Variante que pergunta pelo gatilho (12 casos, 3 rodadas)** — `triage_scenarios_2026-11-23_2024_ask-trigger.json`:

| | A | B |
|---|---|---|
| 8 casos com gatilho | gatilho 24/24 | gatilho **24/24**, 2 voltas (serviço e gatilho perguntados juntos) |
| 4 casos sem gatilho | **barrou 8 de 12** para perguntar o que mudou, embora a mensagem já dissesse "não sabemos" | aceitou "não sabemos" e seguiu com `trigger: null` (1 pergunta repetida no DAN-004) |

## 4. Busca com os textos da conversa (sem LLM)

Script: `retrieval_scenarios.py` — `retrieval_scenarios_2026-11-23_2048.json`. Posição do post-mortem certo entre
os 20 primeiros da busca:

| Texto | Entre os 10 primeiros | Observação |
|---|---|---|
| só a 1ª mensagem (vaga) | 6/12 | |
| conversa colada, sem pergunta do gatilho | 15/15 (5 casos) | DAN-104 em 9º, DAN-125 em 3º–7º |
| `search_text` sem gatilho | 12/15 (5 casos) | DAN-104 cai para 12º–16º |
| conversa colada, com pergunta do gatilho | 36/36 | quase tudo em 1º |
| **`search_text` com gatilho** | **36/36** | 1º em 34 de 36 (DAN-125 e DAN-121 em 2º uma vez cada) |
| mensagem completa (teto) | 12/12 | todas em 1º |

## 5. Ajuste da regra do gatilho

A primeira versão da regra fazia o Triagem perguntar pelo gatilho mesmo quando a mensagem já dizia "não sabemos o
que mudou" (8 de 12 no cenário A) e, uma vez, perguntar duas vezes. A regra passou a dar exemplos de frases que
já contam como resposta ("we haven't identified a trigger", "we don't know what changed", "nothing changed",
"we haven't changed it in months", "we are investigating recent deployments") e a dizer que uma resposta
incerta também é resposta. Texto final em `run_triage_scenarios.py` (`ASK_TRIGGER_RULE`).

Rodada com a regra ajustada — `triage_scenarios_2026-11-23_2101_ask-trigger.json` (6 casos, 3 rodadas, 36 execuções):

| Casos | A: mensagem completa | B: conversa |
|---|---|---|
| 4 sem gatilho (DAN-004, 121, 154, 197) | seguiu nas 12, sem perguntar (antes: barrou 8 de 12) | 2 voltas, perguntou o gatilho **uma vez**, `trigger: null` |
| 2 com gatilho (DAN-104, 125) | seguiu nas 6, gatilho capturado | 2 voltas, perguntou uma vez, gatilho capturado |

Nenhuma pergunta desnecessária, nenhuma repetida e nenhum gatilho perdido.

## 5b. Casos reescritos: Triagem, busca e Pesquisa híbrido

Os 12 casos foram reescritos pelo mesmo LLM externo, só com o JSON do caso (sem o post-mortem): mesmos fatos, sem
frases, números, mensagens de erro ou nomes internos do documento (`postmortems/DAN-xxx_rewrite.json`; pedidos em
`DAN-xxx_rewrite.txt`). Conferência manual: fatos e gatilhos mantidos, `discovered_later` idêntico.

**Triagem** (regra do gatilho ajustada, 3 rodadas) — `triage_scenarios_2026-11-23_2116_ask-trigger_rewrite.json`:
mensagem completa 36/36 seguiu sem perguntas desnecessárias, gatilho 24/24; conversa 36/36 seguiu (33 em 2 voltas,
3 em 3), gatilho 23/24 (no DAN-164 a reconstrução manual do banco não foi registrada como gatilho).

**Busca em código, sem LLM** — `retrieval_scenarios_2026-11-23_2147_rewrite.json` (post-mortem certo entre os 10
primeiros): 1ª mensagem 3/12; conversa colada **30/36**; `search_text` **25/36**; mensagem completa 10/12. O DAN-018
ficou fora dos 20 primeiros em todas as entradas e o DAN-125 em quase todas.

**Pesquisa híbrido com LLM** — `research_scenarios_2026-11-23_2156_hybrid_rewrite.json` (`run_research_scenarios.py`;
texto de cada rodada do Triagem, com os sintomas como contexto; 108 execuções, 230 chamadas, 0 erros):

| Entrada | Certo aprofundado | Certo encontrado |
|---|---|---|
| conversa colada | **32/36** | 34/36 |
| `search_text` | 28/36 | 31/36 |
| mensagem completa | **32/36** | 33/36 |

Por caso (D = aprofundado, f = encontrado sem aprofundar, - = não encontrado; uma letra por rodada):

| Caso | colada | `search_text` | completa |
|---|---|---|---|
| DAN-104, 145, 017, 116, 121 | DDD | DDD | DDD |
| DAN-211 | DDD | -DD | DDD |
| DAN-125 | D-- | D-D | DDD |
| DAN-018 | DDD | DDf | -D- |
| DAN-164 | DDD | DfD | DDD |
| DAN-004 | DDD | **---** | DDD |
| DAN-154 | DDD | DDD | DD- |
| DAN-197 | ffD | DfD | DfD |

O maior prejuízo do `search_text` foi o DAN-004 (0 de 3): o resumo perdeu os detalhes do relato (erros de
cross-origin, menos callbacks do repositório). O DAN-018, que a busca em código não achava, foi aprofundado em todas
as rodadas com a conversa colada: as consultas do LLM ("account backend revision", "access checks") o trouxeram.

## 5c. Agêntico puro e o bloco do Triagem no prompt (2026-11-24)

Pergunta: o modo agêntico puro (o LLM faz todas as buscas) melhora se receber a saída estruturada do Triagem
(serviço, gatilho, sintomas, categoria) e instruções de como usá-la nas consultas (`prompts.TRIAGE_GUIDANCE`:
consultas pelo tipo de gatilho + tipo de componente, pelo sintoma + alcance, depois pelo mecanismo provável; palavras
gerais, sem nomes internos; não inventar gatilho)? Opção `TRIAGE_CONTEXT` em `agents/research/agent.py`, desligada
por padrão. Entrada: a conversa colada dos 12 casos reescritos, 3 rodadas.

| Variante | Certo aprofundado | Encontrado | Chamadas ao LLM |
|---|---|---|---|
| híbrido, prompt atual (`2156_hybrid_rewrite`) | **32/36** | 34/36 | 77 |
| híbrido + bloco do Triagem (`0840_hybrid_triage-context`) | 30/36 | 34/36 | 78 |
| agêntico, prompt atual (`0823_agentic`) | 24/36 | 28/36 | 82 |
| agêntico + bloco do Triagem (`0832_agentic_triage-context`) | 24/36 | 27/36 | 80 |

Por caso (D aprofundado, f encontrado sem aprofundar, - não encontrado):

| Caso | híbrido | híbrido + Triagem | agêntico | agêntico + Triagem |
|---|---|---|---|---|
| DAN-104, 145, 017, 164 | DDD | DDD | DDD | DDD |
| DAN-211 | DDD | DDD | D-D | DDD |
| DAN-125 | D-- | D-- | DD- | DD- |
| DAN-018 | DDD | Dff | DDD | -fD |
| DAN-116 | DDD | DDD | DDD | -DD |
| DAN-004 (sem gatilho) | DDD | DDD | D-- | D-- |
| DAN-121 (sem gatilho) | DDD | DDD | --f | D-D |
| DAN-154 (sem gatilho) | DDD | DDD | -D- | --- |
| DAN-197 (sem gatilho) | ffD | Dff | fff | fDf |

**Conclusões:**
- O bloco do Triagem **não melhorou** nenhum dos modos (diferenças de 0 a 2, dentro do ruído de 3 rodadas). O LLM
  seguiu as instruções — as consultas passaram a começar pelo gatilho (DAN-104: "removing machines from billing
  infrastructure caused object store API failures") —, mas isso não trouxe mais acertos.
- O agêntico puro continua **bem abaixo do híbrido** (24 contra 32). As perdas se concentram nos **casos sem gatilho**
  (DAN-004, 121, 154: 4 de 18 no agêntico, 18 de 18 no híbrido): sem gatilho, as consultas do LLM ficam genéricas, e
  a busca garantida pela conversa colada do híbrido é o que encontra o caso.
- O DAN-197 é um problema de **escolha**, não de busca: o LLM encontra o caso em quase todas as rodadas e escolhe
  outros incidentes para aprofundar.
- **Decisão sugerida:** manter o híbrido com o prompt atual; a opção `TRIAGE_CONTEXT` fica no código, desligada.

## 6. Limitações

- **Vocabulário do próprio documento:** as mensagens dos casos foram escritas a partir do post-mortem e repetem
  frases, números e mensagens de erro dele ("One of the specified inputs is invalid", "pg_basebackup", "85% of
  the network"). O teste mede "encontrar o mesmo incidente descrito de novo", não "encontrar um incidente
  parecido". Por isso o teste com o LLM do Pesquisa não diferenciaria as entradas.
- **Contaminação:** os post-mortems são públicos; o LLM reconhece incidentes famosos (cap. 10 do livro do Dibia).
- **Amostra pequena:** 12 casos e 3 rodadas; diferenças de 1 ou 2 são tendência.
- **Analista simulado por palavras-chave:** quando uma pergunta casa com dois temas, ele responde os dois.

## 7. Proposta (para a Mari)

| # | Mudança no Triagem | Evidência |
|---|---|---|
| 1 | **Perguntar uma vez se algo mudou antes do problema**, junto com as outras perguntas, só quando o analista ainda não falou de mudanças (texto testado: `ASK_TRIGGER_RULE`) | gatilho 0/15 → 48/48 nas conversas, sem volta a mais; com a regra ajustada, 36/36 sem perguntas desnecessárias |
| 2 | **Campo `trigger`** com o gatilho dito pelo analista (de preferência uma lista, `triggers`: no DAN-018 o modelo guardou só o deploy mais próximo e perdeu o release do painel) | seções 3 e 4 |
| 3 | Campo `search_text` (resumo do incidente): **não usar como texto de busca** — nos casos reescritos, perdeu para a conversa colada (28 contra 32 de 36). Pode servir para exibição ou para o Relatório | seção 5b |
| 4 | Ajustes menores: sintomas sempre em inglês; usar o serviço identificado ao chamar a ferramenta | `analise_triagem_e_hibrido_2026-11-23.md` |
| 5 | Avaliar a rigidez com o nome do serviço (11 de 32 barradas por isso) | seção 2 |

**Para o contrato da E5:** o Pesquisa (modo híbrido) usa a **conversa colada** (`description`: a mensagem e as
respostas do analista, sem reescrita) como texto de busca; `symptoms`, `trigger`, `affected_service` e `category`
vão como contexto para o LLM do Pesquisa e para o Diagnóstico. A pergunta do gatilho continua essencial: é ela que
faz o gatilho aparecer na conversa colada.
