# E5 — Testes do Agente Diagnóstico (24/11)

Testes do Agente Diagnóstico ligado ao Pesquisa (modo híbrido), com a saída do Triagem já salva, nos 12 casos de
post-mortem reescritos (sem o vocabulário do documento). Para cada caso, o Diagnóstico é comparado com a causa real
do post-mortem (`discovered_later.root_cause` em `postmortems/DAN-xxx_rewrite.json`), conferida à mão.

Scripts:
- `run_diagnosis_cases.py`: Pesquisa → Diagnóstico; `--hide-right` esconde o post-mortem certo de todas as buscas
  (problema novo, fora do corpus); `--loop` faz o laço de refinamento como o grafo vai fazer (até
  `MAX_RESEARCH_ROUNDS = 3`).
- `run_diagnosis_config.py`: o Pesquisa roda uma vez por caso e os achados ficam salvos; o Diagnóstico roda várias
  vezes sobre os mesmos achados com cada configuração do modelo.

## Resumo

| Etapa | O que mudou | Resultado |
|---|---|---|
| 1. Primeira versão | o modelo decide tudo (confiança, se basta, próximo passo) | hipótese principal certa em 10/12; **disse "basta" em 24/24** respostas, mesmo sem o caso certo; nunca pediu nova busca |
| 2. Prompt mais rígido | critérios de `high` e de "basta" mais duros | não resolveu: continuou "basta" em 12/12 |
| 3. Decisão em código | o modelo compara (mesmo tipo de gatilho? de componente?) e `decide()` aplica as regras | passou a pedir nova busca quando o certo não vinha; acertos mantidos |
| 4. Certo escondido (12 casos) | — | 6/12 nova busca, 2/12 resposta aceitável, **4/12 causa errada com "basta"** |
| 5. Laço de refinamento | Pesquisa de novo com o pedido do Diagnóstico | o laço funciona, mas o refinamento trazia os **mesmos 8 incidentes** |
| 6. Quatro ajustes | refinamento busca excluindo os já vistos; `same_mechanism`; gatilho desconhecido não basta na 1ª rodada; `temperature` 0 | refinamento passou a trazer incidentes novos; **temperatura 0 com raciocínio: 4/8 respostas vazias** |
| 7. Configuração do modelo | 7 configurações × 6 casos × 3 repetições | escolhida: **raciocínio desligado + temperatura 0** (seção 7) |
| 8. Laço sem esconder (12 casos) | configuração final | seção 8 |
| 9. Laço com o certo escondido (12 casos) | configuração final | seção 9 |

## 1–3. Da primeira versão à decisão em código

Resultados: `diagnosis_cases_2026-11-24_1036.json` (primeira versão), `_1202.json` e `_1215.json` (prompt mais
rígido), `_1254.json` e `_1305.json` (decisão em código).

- Quando o Pesquisa traz o incidente certo com trechos, o Diagnóstico acerta a causa em praticamente todos os casos,
  com confiança calibrada (`medium` quando o gatilho é desconhecido, como no DAN-154 e no DAN-121).
- Pedido como julgamento geral ("a evidência basta?"), o modelo quase sempre responde que sim. Mas ele compara bem
  ponto a ponto: o campo `differs` dizia corretamente que o caso passado era outro tipo de falha.
- Por isso a decisão foi para o código (`decide()` em `agents/diagnosis/schema.py`): o modelo escreve um rascunho
  (`DiagnosisDraft`) com as comparações por hipótese, e o código aplica o teto da confiança, decide se basta e o
  próximo passo. Contrato atualizado (`docs/E5_Estado_e_Formatos.md`, seção 5).

## 4. Certo escondido (problema novo)

Resultado: `diagnosis_cases_2026-11-24_1508_hidden.json` (com as 2 comparações, sem laço).

| Decisão | Casos |
|---|---|
| nova busca (certo) | DAN-104, 145, 211, 125, 164, 197 |
| "basta" com resposta aceitável | DAN-017 (deploy no ambiente errado), DAN-121 (cache + banco) |
| "basta" com causa errada ou só parecida | DAN-154 (`medium`), DAN-004 (`medium`), DAN-018 (`high`), DAN-116 (`high`) |

Dois pontos fracos: o modelo marca "mesmo gatilho" e "mesmo componente" com generosidade quando o tipo geral bate; e,
com gatilho desconhecido, qualquer caso do mesmo tipo de componente passava.

## 5. Laço de refinamento

Resultados: `diagnosis_cases_2026-11-24_1543_hidden_loop.json` e `_1610_hidden_loop.json`.

- O laço funciona (vai até 3 rodadas e termina perguntando ao analista no DAN-164).
- O refinamento do Pesquisa trazia os mesmos 8 incidentes: o LLM recebia os achados antigos como lista principal e
  os novos que ele não aprofundava eram cortados pelo limite de 8.
- As comparações do modelo mudavam entre execuções: o mesmo caso passado recebia "gatilho igual" numa e "diferente"
  na outra.
- 2 falhas por respostas inválidas, que não se repetiram (causa descoberta na seção 7).

## 6. Quatro ajustes

1. **Refinamento do Pesquisa** (`agents/research/agent.py`): numa nova rodada, o código busca com o pedido do
   Diagnóstico e com a descrição, **excluindo todos os incidentes já vistos**; o LLM escolhe só entre os novos; os
   aprofundados das rodadas anteriores voltam aos achados, depois dos novos aprofundados.
2. **`same_mechanism`**: terceira comparação ("o que quebrou e como se espalhou explica os sintomas atuais?"),
   exigida para `high` e para "basta".
3. **Gatilho desconhecido** não conta como "basta" na 1ª rodada (a partir da 2ª, sim).
4. **`temperature`** configurável (`chat()` em `agents/triage/llm.py` aceita `temperature` e opções extras para o
   NIM; o Triagem continua com o padrão do modelo).

Resultados: `diagnosis_cases_2026-11-24_1646_hidden_loop.json`, `_1725_hidden_loop.json`,
`_1736_hidden_loop.json`.

- O refinamento passou a trazer incidentes novos de verdade (as buscas das rodadas 2 e 3 excluem os já vistos).
- Nos 6 primeiros casos escondidos, nenhum afirmou causa errada (DAN-145, 211 e 125 terminaram com a causa certa,
  vinda de um caso parecido; DAN-164 e 197 perguntaram ao analista).
- Nos 8 seguintes, **4 falharam com respostas vazias** (temperatura 0 com o raciocínio ligado) e o `same_mechanism`
  não segurou DAN-018 e DAN-116.
- O NIM ficou instável em parte da tarde (HTTP 503 "content safety screening is temporarily unavailable" e 502):
  quando o Pesquisa não consegue aprofundar nada, o Diagnóstico nunca diz "basta" (a regra exige um incidente com
  trechos) e o caso termina perguntando ao analista.

## 7. Configuração do modelo do Diagnóstico

Resultado: `diagnosis_config_2026-11-24_1824.json`; achados salvos em `diagnosis_config_findings/`. Casos: DAN-145,
211, 018 e 116 com o certo escondido; DAN-104 e 154 normais. 3 repetições sobre os mesmos achados.

| Config | Raciocínio | Temperatura | Tokens | Erros | Tempo médio | Próximo passo igual nas 3 repetições | Comparações iguais | DAN-018 (escondido; causa proposta errada) |
|---|---|---|---|---|---|---|---|---|
| A (anterior) | ligado | padrão | 4096 | **1** | 74 s | 6/6 | 11/15 | "basta" 3/3 |
| B | ligado | padrão | 8192 | 0 | 60 s | 5/6 | 6/15 | "basta" 3/3 |
| C | ligado | 0 | 8192 | 0 | 52 s | 5/6 | 9/15 | "basta" 3/3 |
| D | ligado | 0.3 (`top_p` 0.95) | 8192 | 0 | 52 s | **6/6** | **12/17** | "basta" 3/3 |
| E | ligado | 0.6 (`top_p` 0.95) | 8192 | 0 | 44 s | 5/6 | 9/16 | "basta" 3/3 |
| **F (escolhida)** | **desligado** | **0** | 4096 | 0 | **29 s** | 5/6 | 11/17 | **nova busca 3/3** |
| G | desligado | 0.3 | 4096 | 0 | 20 s | 3/6 | 7/17 | nova busca 2/3 |

- **A causa das respostas vazias** era o raciocínio do modelo gastando todo o limite de 4096 tokens antes da
  resposta (a resposta rejeitada tinha 0 caracteres ou só `{`). Com 8192 tokens, nenhuma configuração com raciocínio
  falhou — nem a temperatura 0 (C).
- **Por que a F:** foi a única que não aceitou a causa errada no DAN-018 (marcou "mecanismo: não" nas 3 repetições);
  nos outros casos decide igual às demais (DAN-104 e DAN-154 normais; causas certas de DAN-116, 145 e 211); é a mais
  rápida das estáveis (29 s contra 52 s da D); nenhum erro. A D é um pouco mais estável no próximo passo (6/6 contra
  5/6), mas aceitou o DAN-018 nas 3.
- **O que continua variando:** o DAN-145 (certo escondido; o caso usado é parecido, mas o gatilho é outro) oscila entre
  "basta" e "nova busca" em todas as configurações. É um caso de fronteira.
- Configuração fixada em `agents/diagnosis/agent.py` (`TEMPERATURE = 0`, `LLM_OPTIONS` com
  `enable_thinking: False`).

## 8. Laço sem esconder (12 casos, configuração final)

Resultado: `diagnosis_cases_2026-11-24_2011_loop.json`. Nenhuma falha do NIM; a execução inteira levou 13 minutos
(o Diagnóstico sem raciocínio responde em 30–60 s por caso).

| Caso | Pesquisa aprofundou o certo? | Rodadas | Hipótese principal final | Bate com a causa real? |
|---|---|---|---|---|
| DAN-104 | sim | 1 | [high] o comando de rotina removeu servidores demais (índice e alocação) | sim |
| DAN-145 | sim | 1 | [high] a relocação do Redis derrubou o primário e disparou o failover | sim |
| DAN-211 | sim | 1 | [high] o streaming do Consul ligado + frota 50% maior sobrecarregaram a coordenação | sim |
| DAN-125 | **não** | 1 | [high] o Postgres reduzido + um único host de pool esgotaram as conexões (casos parecidos) | em parte |
| DAN-018 | sim | 2 | [high] a revisão do backend de contas sobrecarregou o serviço (DAN-221) | **não** — a certa ("o console fez chamadas excessivas ao backend", DAN-018) ficou em 2º |
| DAN-017 | sim | 1 | [high] o deploy em estágios apontou a produção para o destino errado | sim |
| DAN-116 | sim | 1 | [high] a atualização de dados disparou um bug latente (cita double free) | sim |
| DAN-164 | sim | 1 | [high] a reconstrução manual do replica durante o pico quebrou a replicação | em parte (não diz que os dados do primário foram apagados por engano) |
| DAN-004 | sim | 2 | [medium] uma regra de WAF/borda mudada fora do pipeline bloqueou o tráfego | sim |
| DAN-121 | sim | 2 | [medium] pico de demanda no banco de metadados + cache fora | sim (causa não fechada no post-mortem) |
| DAN-154 | sim | 2 | [medium] mudança de configuração válida disparou um bug latente na borda | sim |
| DAN-197 | sim | 1 | [high] mudança não anunciada na API do provedor tornou um parâmetro obrigatório | sim |

- **Hipótese principal certa em 10/12** (mais 2 em parte); o DAN-018 tem a certa em 2º lugar.
- **Custo da regra do gatilho desconhecido:** 3 casos (DAN-004, 121, 154) gastaram uma rodada a mais e terminaram
  com a mesma resposta da 1ª rodada. É o preço de não aceitar qualquer caso parecido quando o gatilho não é conhecido
  (seção 9 mostra o ganho).
- **DAN-018:** na 1ª rodada a hipótese principal já vinha do DAN-018, mas com "mecanismo: não" (o analista fala da
  revisão do backend, e o post-mortem culpa o painel); a nova busca trouxe o DAN-221, que passou à frente. O modelo
  continua guiado pelo gatilho mais próximo citado pelo analista — o mesmo problema que o Triagem tinha (ver
  `E5_testes_triagem_pesquisa_2026-11-23.md`, seção 7: guardar todos os gatilhos, não só o mais próximo).

## 9. Laço com o certo escondido (12 casos, configuração final)

Resultado: `diagnosis_cases_2026-11-24_2025_hidden_loop.json`. O NIM falhou 8 vezes no LLM do Pesquisa (503); em
DAN-211 e DAN-197 nenhuma rodada conseguiu aprofundar incidentes (repetidos na seção 11).

| Caso | Rodadas | Final | Avaliação |
|---|---|---|---|
| DAN-104 | 3 | pergunta ao analista ("que mensagens de erro as APIs devolvem?") | ✅ não afirmou causa |
| DAN-211 | 3 | pergunta ao analista | ✅ (mas o Pesquisa não aprofundou nada: falhas do NIM) |
| DAN-018 | 3 | pergunta ao analista | ✅ não afirmou causa (antes: `high` com causa errada) |
| DAN-164 | 3 | pergunta ao analista | ✅ |
| DAN-154 | 3 | pergunta ao analista | ✅ (antes: "basta" com causa só parecida) |
| DAN-197 | 3 | pergunta ao analista ("qual parâmetro o provedor rejeita?") | ✅ (o Pesquisa não aprofundou nada: falhas do NIM) |
| DAN-145 | 1 | basta, `high` (DAN-144/217: failover + reconexão em massa) | ✅ a causa bate com a real, vinda de casos parecidos |
| DAN-125 | 1 | basta, `high` (Postgres reduzido + pool único esgotado) | ✅ em parte |
| DAN-017 | 1 | basta, `high` (DAN-015: deploy no ambiente errado) | ✅ quase a causa real |
| DAN-116 | 1 | basta, `high` (DAN-154: push global disparou bug latente) | ✅ mesmo mecanismo da causa real |
| DAN-121 | 2 | basta, `medium` (falha de vários hosts de cache → banco) | ✅ (causa não fechada no post-mortem) |
| DAN-004 | 2 | basta, `medium` (DAN-092: estatísticas do banco após mudança) | ❌ a causa real é uma regra de WAF |

**Comparação com a seção 4** (certo escondido, antes do laço e dos ajustes):

| | Seção 4 (sem laço, 2 comparações) | Seção 9 (laço + ajustes + config F) |
|---|---|---|
| não afirmou causa (nova busca / pergunta ao analista) | 6/12 | 6/12 (todos terminando em pergunta ao analista depois de 3 rodadas) |
| "basta" com resposta aceitável | 2/12 | **5/12** |
| "basta" com causa errada ou só parecida | **4/12** | **1/12** |

- Os casos que antes afirmavam causa errada (DAN-018, DAN-154) agora gastam as rodadas e terminam perguntando ao
  analista; DAN-116 passou a acertar o mecanismo usando um caso parecido de verdade.
- `high` com o caso certo ausente aparece em 4 casos (DAN-145, 125, 017, 116), todos com a causa certa ou quase. A
  confiança fica exagerada (a fonte é um caso parecido, não o mesmo), mas a resposta serve ao analista.
- As perguntas ao analista no fim do laço são boas e concretas (mensagem de erro exata, parâmetro rejeitado).

## 10. Repetição do laço sem esconder (variação entre execuções)

Resultado: `diagnosis_cases_2026-11-24_2107_loop.json` (mesma configuração da seção 8).

- DAN-104 falhou por erro do NIM (HTTP 503 três vezes na chamada do Diagnóstico; no grafo vira relatório
  inconclusivo). Repetido na seção 11.
- Nos outros 11: hipótese principal certa em 10 (+ DAN-164 em parte).
- **O Diagnóstico decidiu igual à seção 8** em todos os casos em que os achados foram parecidos: os mesmos casos
  pararam na 1ª rodada (DAN-145, 211, 017, 116, 164, 197) e na 2ª (DAN-004, 121, 154 — regra do gatilho desconhecido).
- **O que mudou foi o Pesquisa:** DAN-125 desta vez trouxe o post-mortem certo (`high`, causa certa); DAN-018 desta vez
  não trouxe e, depois de 3 rodadas, o Diagnóstico aceitou "bug na revisão do backend" (DAN-017/009) com `high` —
  errado; a hipótese certa ("o console mudou a forma de chamar o backend", DAN-097) ficou em 2º.
- **DAN-018 é o caso que mais falha** (seções 8, 9 e 10): o analista cita duas mudanças (o console e a revisão do
  backend) e o modelo sempre segue a mais próxima do início do problema. Melhoraria com o Triagem guardando todos os
  gatilhos e com uma comparação de mecanismo mais exigente — fica para depois.

## 11. Casos repetidos por falha do NIM

Resultados: `diagnosis_cases_2026-11-24_2137_hidden_loop.json` (DAN-211 e DAN-197 escondidos) e
`diagnosis_cases_2026-11-24_2149_loop.json` (DAN-104 normal).

| Caso | Final | Avaliação |
|---|---|---|
| DAN-104 (normal) | 1 rodada, `high`, o comando de rotina removeu capacidade demais | ✅ causa certa |
| DAN-211 (escondido) | 1 rodada, `medium` com base no DAN-098 (GitHub: mudança de TTL + pico de leitura) | ✅ a causa proposta é a certa (streaming + frota maior sobrecarregaram a coordenação), mas a fonte é um caso pouco parecido |
| DAN-197 (escondido) | 3 rodadas → pergunta ao analista ("qual parâmetro é rejeitado e qual o código de erro?") | ✅ não afirmou causa (o NIM falhou de novo na 1ª rodada; nas seguintes, os casos novos tinham mecanismo diferente) |

**Placar final com o certo escondido** (seção 9 com DAN-211 e DAN-197 desta seção): 5/12 terminaram perguntando ao
analista, 6/12 deram "basta" com resposta aceitável, 1/12 (DAN-004) deu "basta" com causa errada.

## 12. Conclusões

1. **Caso conhecido** (o post-mortem certo existe): a hipótese principal bate com a causa real em ~10 de 12 casos,
   e as decisões do Diagnóstico se repetem entre execuções. O que varia é o Pesquisa (DAN-125 e DAN-018 trazem o certo
   numa execução e não na outra).
2. **Problema novo** (certo escondido): de 4/12 causas erradas afirmadas (seção 4) para 1/12. Os casos sem evidência
   boa usam as 3 rodadas e terminam com perguntas concretas ao analista.
3. **O que fez a diferença:** decisão no código a partir de comparações simples; refinamento do Pesquisa excluindo
   o que já foi visto; gatilho desconhecido não basta na 1ª rodada; modelo do Diagnóstico sem raciocínio e com
   temperatura 0.
4. **Custos:** a regra do gatilho desconhecido gasta 1 rodada a mais em 3 de 12 casos normais (DAN-004, 121, 154),
   sem mudar a resposta. Com o Diagnóstico sem raciocínio, uma execução dos 12 casos com laço leva 13–30 minutos,
   dependendo do NIM.
5. **Limites que continuam:** DAN-018 (duas mudanças citadas pelo analista; o modelo segue a mais próxima); `high`
   quando a fonte é um caso parecido, não o mesmo; o NIM gratuito falha em rajadas (503/502) — quando o Pesquisa não
   aprofunda nada, o Diagnóstico não diz "basta" e o caso termina perguntando ao analista; quando o próprio
   Diagnóstico falha, o grafo deve terminar com relatório inconclusivo (cenário 7).

## 13. O que mudou no código (sem commit)

| Arquivo | Mudança |
|---|---|
| `agents/diagnosis/schema.py` | `same_mechanism`; `decide()` exige mesmo mecanismo para `high` e para "basta"; gatilho desconhecido só basta a partir da 2ª rodada |
| `agents/diagnosis/prompts.py` | terceira comparação no prompt e no exemplo |
| `agents/diagnosis/agent.py` | configuração do modelo (`TEMPERATURE = 0`, raciocínio desligado); o erro de 3 respostas inválidas leva as mensagens junto (`error.messages`) |
| `agents/diagnosis/tests/` | testes novos de `decide()` (30/30) e do laço (12/12) |
| `agents/research/agent.py`, `prompts.py` | refinamento: busca em código com o pedido e a descrição, excluindo os já vistos; o LLM vê só os novos ("NEW INCIDENTS FOUND"); os aprofundados antigos voltam no fim |
| `agents/research/tools.py` | `HIDDEN_IDS` (experimentos: incidentes tratados como fora do corpus) |
| `agents/triage/llm.py` (arquivo da Mari) | `chat()` aceita `temperature` e opções extras para o NIM; sem elas, igual a antes (testes do Triagem passando) |
| `experiments/run_diagnosis_cases.py` | `--hide-right`, `--loop`, log de buscas e avisos por rodada, respostas rejeitadas quando há erro |
| `experiments/run_diagnosis_config.py` | novo: teste de configurações do modelo sobre achados fixos |
| `docs/E5_Estado_e_Formatos.md` | seção 5 (regras, modelo, refinamento) e seção 11 (pontos 3 e 4 para a Mari) |

Os resultados avulsos das conferências (duas execuções isoladas do DAN-104 e uma da opção `--hide-right`) foram
apagados em 25/11.

## 14. Acabamentos (25/11, branch `e5-acabamentos`)

**Pergunta do gatilho no Triagem de verdade** (`run_triage_trigger_check.py`,
`triage_trigger_check_2026-11-25_0903.json`): com só a primeira mensagem, o Triagem perguntou se algo mudou antes do
problema em 12/12 casos (junto com a pergunta do serviço); com a conversa completa, não perguntou de novo em 12/12 —
inclusive nos 4 casos em que o analista diz não saber o que mudou (DAN-004, 121, 154, 197: `triggers` vazio). O
campo `triggers` trouxe todas as mudanças citadas: DAN-018 com as duas (o console e a revisão do backend), DAN-211,
125 e 164 com duas ou três.

**Várias mudanças e pedidos de busca** (`diagnosis_cases_2026-11-25_0909_loop_livetriage.json`, Triagem novo ao
vivo + laço):

| Execução | Final | Avaliação |
|---|---|---|
| DAN-018 nº 1 | 3 rodadas (a 3ª busca explorou a outra mudança: "console frontend update caused excessive backend API calls") → pergunta ao analista | ✅ não afirmou causa errada |
| DAN-018 nº 2 | basta, `high` na revisão do backend; a do console em 2º | ❌ |
| DAN-018 nº 3 | basta, `high` na revisão do backend; a do console em 2º | ❌ |
| DAN-104, 211, 164, 197 | 1 rodada, `high`, causa certa | ✅ |
| DAN-154 | 2 rodadas, `medium`, causa certa | ✅ |

- A hipótese certa do DAN-018 ("o console fez chamadas demais ao backend") agora aparece nas 3 execuções (antes,
  às vezes nem aparecia), mas o modelo ainda prefere a mudança mais recente. Melhorou, não resolveu.
- Os pedidos de busca das rodadas 2 e 3 vieram diferentes; nenhuma regressão nos outros casos.

## 15. Quando perguntar sobre mudanças: política A × B (25/11)

O Triagem com a pergunta do gatilho (seção 14) quebrou 3 cenários da Mari: mensagens que já dizem o que falha e onde,
mas não falam de mudanças, passaram a gerar a pergunta. Duas políticas, pelo grafo inteiro (Triagem → Pesquisa →
Diagnóstico com o laço; relatório em código), nos 12 casos, com uma 1ª mensagem que diz o que falha e onde, sem
mudança, e um analista simulado (`run_trigger_policy.py`, `trigger_policy_<A|B>_2026-11-25_*.json`):

- **A:** perguntar uma vez sempre que nenhuma mensagem fala de mudanças;
- **B:** perguntar sobre mudanças só junto com outra pergunta (falta o sintoma ou o serviço).

| | A | B |
|---|---|---|
| Hipótese principal veio do post-mortem certo (3 repetições) | 28/35 (80%) | 28/36 (78%) |
| Perguntas ao analista | 16 | 11 |
| Rodadas de busca | 75 | 96 |
| Tempo médio por investigação | ~1min40 | ~1min40 |
| Cenários do Triagem da Mari | 12/18 | 18/18 |

- **Mesma qualidade.** Os erros mudam de caso a cada repetição (o Pesquisa varia); nenhum caso favoreceu sempre a
  mesma política (o DAN-125, que parecia favorecer a A nas 2 primeiras repetições, errou na A na 3ª).
- **A A é aplicada de forma inconsistente:** com a mensagem que já diz o que falha e onde, o modelo perguntou em só
  3 a 6 dos 12 casos.
- **Na B, quem pergunta é o Diagnóstico**, quando a busca não acha evidência boa (DAN-164, 154, 197): o analista só é
  interrompido quando falta informação de verdade.
- Uma execução da A caiu por falha do NIM no Triagem (DAN-116, 3ª repetição) e ficou fora da conta.

**Decisão:** política B como padrão (`TRIGGER_POLICY = "B"` em `agents/triage/prompts.py`); a A ficou guardada
(`TRIGGER_RULES["A"]`, `set_trigger_policy("A")` em `agents/triage/agent.py`) para testar de novo.


## 16. Os 12 casos com o Relatório da Mari e o Postgres (25/11)

Resultado: `trigger_policy_B_report_pg_2026-11-25_1239.json` (`run_trigger_policy.py --policy B --real-report
--postgres`): o grafo inteiro com o modelo real, a política B, o Relatório da Mari (`agents/reporting`) e o
PostgresSaver; 1ª mensagem com o que falha e onde, analista simulado. Os 12 relatórios foram lidos à mão.

- **Diagnóstico:** a hipótese principal veio do post-mortem certo em 11/12.
- **Relatório:** válido na 1ª tentativa em 3 (DAN-017, 121, 197), na 2ª em 4 (DAN-145, 211, 116, 004), na 3ª em 2
  (DAN-104, 164); **falhou nas 3 tentativas em 3 (DAN-125, 018, 154)** e caiu no relatório de reserva
  (inconclusivo), embora o Diagnóstico tivesse dito que a evidência bastava — no DAN-018 e no DAN-154 o diagnóstico
  estava certo e se perdeu.
- **Causa das falhas: limite de tokens.** JSON cortado no meio (DAN-125, 154) ou resposta vazia (DAN-018): o modelo
  raciocina antes de responder (8192 tokens), e com 3 hipóteses a regra "causas = hipóteses" pede 3 causas completas
  (correção, mudanças, prevenção, fontes), inclusive as `low`. O mesmo problema que o Diagnóstico tinha com o
  raciocínio ligado (seção 7).
- **Qualidade dos 9 válidos:** fiéis aos post-mortems (double free no DAN-116, build de staging no DAN-017, regra de
  WAF fora do Terraform no DAN-004, mudança não anunciada da Azure no DAN-197); dizem quando o post-mortem não
  descreve a correção, sem inventar; links corretos em todos; "o que verificar agora" concreto. Problemas menores:
  muito longos (a causa `low` ocupa o mesmo espaço da principal); no DAN-164, um trecho do incidente aparece como
  "como foi corrigido"; no DAN-121, o texto de um link traz o resumo colado ao título (vem dos achados).

**Sugestões para a Mari** (em ordem): (1) desligar o raciocínio do modelo no Relatório, como no Diagnóstico
(temperatura 0, `enable_thinking: False`); (2) quando o Diagnóstico disse que basta, o relatório de reserva deve ser
um diagnóstico montado em código com as hipóteses e as fontes, não um inconclusivo; (3) encurtar as causas `low`
(causa + fonte), o que pede afrouxar a regra "causas = hipóteses"; (4) guardar os problemas de cada tentativa, não só
os da última.

## 17. Relatório com o raciocínio desligado (25/11)

Resultado: `trigger_policy_B_report_nothink_pg_2026-11-25_1422.json` (`run_trigger_policy.py --policy B --real-report
--report-no-thinking --postgres`), nos 3 casos que caíram no relatório de reserva na seção 16 e em 3 que passaram
(2 deles só na 3ª tentativa). O modelo do Relatório foi chamado com temperatura 0 e `enable_thinking: False`.

| Caso | Seção 16 (raciocínio ligado) | Raciocínio desligado |
|---|---|---|
| DAN-125 | falhou nas 3 → reserva | válido na 1ª |
| DAN-018 | falhou nas 3 → reserva | válido na 1ª |
| DAN-154 | falhou nas 3 → reserva | válido na 1ª |
| DAN-104 | válido na 3ª | válido na 1ª |
| DAN-164 | válido na 3ª | válido na 1ª |
| DAN-197 | válido na 1ª | válido na 1ª (inconclusivo) |

- **6 de 6 válidos na 1ª tentativa**, nenhum relatório de reserva. Lidos à mão: a mesma qualidade (fiéis aos
  post-mortems, dizem quando o post-mortem não descreve a correção ou a prevenção, links corretos), um pouco mais
  curtos (2.500 a 4.800 caracteres). Continua o detalhe do DAN-164 (um passo do incidente aparece como correção).
- **DAN-197 levou 26 minutos:** com 429 do NIM o Pesquisa não aprofundou o post-mortem certo, o Diagnóstico perguntou
  ao analista 3 vezes e cada resposta recomeçou a investigação (9 rodadas de busca no total); o relatório
  inconclusivo saiu honesto. O pior caso do desenho (3 respostas × 3 rodadas) é longo; limitar o total de rodadas por
  investigação fica como ideia para depois.

**Decisão:** o Relatório passa a chamar o modelo com o raciocínio desligado e temperatura 0
(`agents/reporting/agent.py`, `TEMPERATURE` e `LLM_OPTIONS`), na branch `e5-acabamentos`, para a Mari revisar.

