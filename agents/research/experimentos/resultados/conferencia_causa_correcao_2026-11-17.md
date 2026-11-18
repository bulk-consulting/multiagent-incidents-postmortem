# Conferência: o aprofundamento traz causa e correção?

Data: 2026-11-17. Versão do agente: v3 + melhorias A/B (rodadas `2026-11-17_1741`, `1432_perguntas_dificeis`
e `1719_perguntas_dificeis`).

**Pergunta:** quando o Agente Pesquisa RAG aprofunda o incidente certo (`search_inside_incidents`), os trechos
que chegam dizem **por que** o incidente aconteceu (causa) e **o que foi feito** para resolver ou prevenir
(correção)?

**Como foi feito:** para cada incidente certo aprofundado, os trechos foram reproduzidos com as mesmas consultas
da rodada (a do LLM + a consulta fixa; a busca é determinística) e lidos inteiros. Em seguida, a lista de seções
do post-mortem completo foi conferida para separar dois casos:
- **falha da busca:** a causa ou a correção está no documento, mas o trecho não veio;
- **limite do corpus:** o documento não descreve a causa ou a correção.

A classificação é leitura humana (como na 3.5), não métrica automática.

## Resultado

20 incidentes: 13 das 12 perguntas da E3 (q07 e q11 têm dois) e 7 das perguntas difíceis.

| q | Incidente | Causa | Correção | Se faltou: por quê |
|---|---|---|---|---|
| q01 | DAN-164 GitLab | sim (*Root cause analysis*, os "5 porquês") | **não** | busca: *Improving recovery procedures* existe (3 trechos), ficou em 12º |
| q02 | DAN-104 S3 | sim (comando com erro de digitação) | sim (*"We are making several changes… safeguards"*) | |
| q03 | DAN-090 Firefox | sim (*Root Cause Analysis*) | parcial (*Incomplete Fixes*) | busca: *Code Delivery*, com a entrega da correção, ficou em 5º |
| q04 | DAN-071 Google (raios) | sim (*ROOT CAUSE* dentro do trecho) | **não** | busca: a remediação está em trechos de 4º e 8º |
| q05 | DAN-084 Knight Capital | sim (servidor sem a versão nova + flag reaproveitada) | parcial (o que tentaram durante o incidente) | busca: *A Lesson to Learn* ficou em 7º |
| q06 | DAN-236 Steam | parcial (um comentário aponta `rm -rf "$STEAMROOT/"*` sem checar a variável) | **não** | corpus: é uma issue do GitHub, sem correção descrita |
| q07 | DAN-088 kernel | sim (deadlock no `xtime_lock` via `printk`) | parcial (sugestão de correção na thread) | corpus: thread de e-mail |
| q07 | DAN-089 kernel | sim (diagnóstico do `hrtimer base.offset`) | sim (*"my fix to call clock_was_set"*) | |
| q08 | DAN-145 Discord | sim (*Investigation and Analysis*) | sim (*Update*: correção de biblioteca); *Action Items* (6º) não veio | |
| q09 | DAN-122 JCenter | sim (revisão não detectou a impersonação) | sim (*Remediation*) | |
| q10 | DAN-017 Cloudflare | sim (*Timeline*: a API devolve o build de staging) | sim (*Resolution*); prevenção (*Next steps*, 7º) não veio | |
| q11 | DAN-086 Azure | sim (*The Leap Day Bug*) | sim (*Prevention*) | |
| q11 | DAN-090 Firefox | sim | parcial | busca (igual à q03) |
| q-032 | DAN-104 S3 | sim | sim | |
| q-219 | DAN-116 AppNexus | sim (double free) | sim (correção testada + próximos passos) | |
| q-218 | DAN-116 AppNexus | sim | sim | |
| q-223 | DAN-121 BBC | parcial (sobrecarga no banco; o próprio texto diz que a análise não terminou) | parcial (restaurar o cache) | corpus: documento curto (3 trechos) |
| q-229 | DAN-125 Buildkite | sim (downgrade do banco para economizar) | sim (upgrade do banco, volta do pgbouncer por host) | |
| q-262 | DAN-200 Mars Pathfinder | sim (inversão de prioridade) | **não** | busca: *HOW WAS THE PROBLEM CORRECTED* existe, ficou em 6º e 8º |
| q-242 | DAN-154 (pela consulta alternativa) | sim (*What happened?*) | sim (*Where do we go from here?*) | |

| | sim | parcial | não |
|---|---|---|---|
| **causa** | 18 | 2 | 0 |
| **correção** | 11 | 5 | 4 |

Das 9 correções parciais ou ausentes, **6 são falha da busca** (a seção existe no documento) e **3 são limite
do corpus** (issue do GitHub, thread de e-mail, documento curto).

## Conclusões

1. **A causa chega quase sempre.** É o que a consulta do LLM e a busca inicial mais trazem.
2. **A correção é o ponto fraco**, e na maioria das vezes por causa da busca, não do corpus. A seção de correção
   existe, mas fica entre o 4º e o 12º lugar dentro do incidente, e o aprofundamento pega 2 trechos por consulta.
3. A consulta fixa atual mistura causa e correção (*"what was the root cause and how was the problem fixed"*) e
   tende a puxar a narrativa e a causa. Uma consulta só de correção (*"how the problem was corrected,
   remediation, action items, prevention, next steps"*) melhora parte dos casos (DAN-164: de 12º para 2º;
   DAN-017: de 7º para 1º), mas não todos (DAN-200 continua em 6º).

## Depois da mudança (mesmo dia)

Mudança em `pesquisa_ferramentas.py` (`trechos_do_incidente`), só código:
- a consulta fixa virou duas: **causa** (*"what was the root cause of the failure"*, 1 trecho) e **correção**
  (*"how the problem was corrected, remediation, action items, prevention, next steps"*, 2 trechos);
- na correção, trechos cujo título de seção (ou rótulo em maiúsculas, como *REMEDIATION AND PREVENTION:*) indica
  correção ou prevenção vêm antes dos demais;
- trechos que começam igual (os chunks da ingestão se sobrepõem) entram uma vez só.

A consulta do LLM não muda, e a entrada do LLM também não. Por isso, a conferência foi refeita sem o NIM, com as
mesmas consultas do LLM salvas nas rodadas.

| q | Incidente | Correção antes | Correção depois | O que passou a vir |
|---|---|---|---|---|
| q01 | DAN-164 | não | **sim** | *Improving recovery procedures* (2 trechos) |
| q03 / q11 | DAN-090 | parcial | **sim** | *Code Delivery* (como a correção foi entregue) |
| q04 | DAN-071 | não | **sim** | *REMEDIATION AND PREVENTION* |
| q05 | DAN-084 | parcial | **sim** (lições/prevenção) | *A Lesson to Learn* |
| q08 | DAN-145 | sim, sem *Action Items* | sim | *Action Items / Response* |
| q10 | DAN-017 | sim, sem prevenção | sim | *Next steps* |
| q-262 | DAN-200 | não | **sim** | *HOW WAS THE PROBLEM CORRECTED* + *ANALYSIS AND LESSONS* |
| q06, q07 (DAN-088), q-223 | | não / parcial | igual | limite do corpus |
| demais | | sim | sim | |

| | sim | parcial | não |
|---|---|---|---|
| **correção, antes** | 11 | 5 | 4 |
| **correção, depois** | **17** | 2 | 1 |
| causa (antes e depois) | 18 | 2 | 0 |

As 6 falhas da busca foram resolvidas. O que sobra (q06, q07/DAN-088, q-223) é limite do corpus: o documento
não descreve a correção. Ainda aparece ruído em alguns trechos de correção (lista de arquivos no DAN-122,
*Where to Learn More* no DAN-090, o pedido de desculpas em *Moving forward* no DAN-125): o título bate, ou a
similaridade puxa, mas o conteúdo não ajuda.

## Teste completo da versão v4 (rodadas `2026-11-17_1831` e `2026-11-17_1840_perguntas_dificeis`)

Execução real (com o LLM), 12 da E3 e 20 difíceis rodando ao mesmo tempo, 2 em paralelo em cada. Os trechos do
incidente certo ficaram salvos inteiros no resultado e foram lidos para esta conferência.

**Busca:** certo aprofundado em 11/11 (E3), 8/8 (difíceis, 4º–5º), 6/6 (6º–10º) e 0/6 (além do 10º: fora da lista).

**Causa e correção** nos 27 incidentes certos aprofundados:

| | sim | parcial | não |
|---|---|---|---|
| causa | 24 | 3 | 0 |
| correção | 23 | 3 | 1 |

Os parciais e o "não" são os mesmos casos de limite do corpus: DAN-236 (Steam, issue do GitHub), DAN-088 (thread
de e-mail do kernel) e DAN-121 (BBC, post curto, em q-222 e q-223). Exemplos de correção que chegaram:
*HOW WAS THE PROBLEM CORRECTED* (Mars Pathfinder, q-262 e q-263), *Improving recovery procedures* (GitLab, q01 e
q-020), *Recent Improvements and Future Steps* (Roblox, q-012), *Going forward* (Cloudflare, q-170/q-171),
*Recommendations* (ESLint, q-240), *Action Items / Response* (Discord, q08).

**Chamadas de ferramenta:** 33 chamadas ao LLM, todas executadas; 2 com JSON sem fechar, consertadas em código
(sem nova chamada); 0 nomes vazados; 0 campos esquecidos.

**q12 (fora do corpus):** chamou `find_similar_incidents` duas vezes (4 consultas sobre o Pix) e encerrou sem
aprofundar nada; os incidentes trazidos não têm relação, o que cabe ao Diagnóstico marcar como insuficiente.

**Tempo:** 12 da E3 em ~28 min e 20 difíceis em ~37 min, ao mesmo tempo (uma de cada vez seriam ~90 min).
Três perguntas passaram de 8 min por estouro de tempo na fila do NIM, resolvido pela nova tentativa.
