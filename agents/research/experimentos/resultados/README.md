# Resultados dos testes do Agente Pesquisa RAG

Gerados por `agents/research/experimentos/avaliar_pesquisa.py`, no banco da ingestão da main. Cada rodada tem
um `.md` (tabela + decisões do LLM + trechos trazidos) e um `.json` (dados completos).

Perguntas:
- **12 da E3** (`rag/avaliacao/perguntas.json`): o incidente certo quase sempre vem em 1º na busca.
- **20 difíceis** (`perguntas_dificeis.json`): perguntas de sintoma da suíte da E2 em que a busca põe o
  incidente certo abaixo do 3º lugar (8 em 4º–5º, 6 em 6º–10º, 6 além do 10º).

| Rodada | Versão do agente | Perguntas | Resultado principal |
|---|---|---|---|
| `2026-11-16_1429` | v1: o LLM devolve um plano (`planejar_busca`), o código busca; 5 candidatos com trechos | 12 da E3 | certo achado em 11/11 |
| `2026-11-16_1511` | v1 + consulta fixa de causa e correção somada à do LLM | 12 da E3 | a consulta fixa trouxe causa/correção em 5 de 11 que a do LLM não trouxe |
| `2026-11-16_1539_semllm` | sem LLM: aprofunda os 3 primeiros com a consulta fixa | 12 da E3 | base de comparação: empate com o LLM nas perguntas fáceis |
| `2026-11-16_1551_perguntas_dificeis_semllm` | sem LLM | 20 difíceis | certo aprofundado em 0/20 (por construção) |
| `2026-11-16_1650_perguntas_dificeis` | v1 + consulta fixa | 20 difíceis | 4º–5º: 8/8; 6º ou abaixo: 0/12 (nunca fez consulta nova) |
| `2026-11-17_1216` | v2: o LLM chama as ferramentas (`search_inside_incidents`, `find_similar_incidents`); 5 candidatos com trechos | 12 da E3 | certo aprofundado em 9/11; 2 chamadas malformadas |
| `2026-11-17_1222` | v2 + nova tentativa em chamada malformada | q01 e q07 | as duas aprofundadas |
| `2026-11-17_1320_perguntas_dificeis` | v2 | 20 difíceis | 4º–5º: 8/8; 6º ou abaixo: 2/12 (as 2 por consulta nova) |
| `2026-11-17_1432_perguntas_dificeis` | v3: 10 candidatos, o LLM lê só título e resumo; conserto de JSON sem fechar | 12 difíceis (6º ou abaixo) | 6º–10º: 6/6; além do 10º: 0/6 |
| `2026-11-17_1522` | v3 | 12 da E3 | certo aprofundado em 11/11; q12 (fora do corpus) procurou e encerrou sem aprofundar; 0 malformadas |
| `2026-11-17_1719_perguntas_dificeis` | v3 + A (`match` strong/partial/weak) + B (`alternative_query` executada em código) | 6 difíceis (além do 10º) | B achou o certo em 1/6 (q-242); A marcou incidentes errados como `strong` nas 6 |
| `2026-11-17_1741` | v3 + A + B, 3 em paralelo | 12 da E3 | certo aprofundado em 11/11, todos `strong`; B trouxe 2 incidentes por pergunta, quase sempre ruído |
| `conferencia_causa_correcao_2026-11-17.md` | v3 + A + B → v4 | 20 incidentes certos aprofundados | leitura dos trechos inteiros: correção completa em 11/20; com a consulta fixa separada em causa + correção (v4), 17/20 |
| `2026-11-17_1759` | v4: sem `match` e sem `alternative_query` (ganho pequeno demais), com `why`; consultas fixas de causa e de correção | q01, q07, q10 | 3/3 aprofundados, chamadas válidas |
| `2026-11-17_1831` + `2026-11-17_1840_perguntas_dificeis` | **v4 (versão atual), teste completo**, trechos do certo salvos inteiros | 12 da E3 + 20 difíceis | certo aprofundado: 11/11, 8/8 (4º–5º), 6/6 (6º–10º), 0/6 (além do 10º); causa 24/27 e correção 23/27 completas (ver conferência) |

Cuidados ao ler: cada versão rodou uma vez, e o modelo varia entre rodadas (temperatura 1,0). As
diferenças de 1 ou 2 perguntas são tendência, não prova.

## Troca de modelo (2026-11-18: o `openai/gpt-oss-20b` saiu do NIM)

Branch `e5-troca-modelo`, opção `--modelo` (o `.env` não muda). Mesmo agente, só o modelo trocado.

| Rodada | Modelo | Perguntas | Resultado principal |
|---|---|---|---|
| `2026-11-18_1200` + `1202_perguntas_dificeis` e `1221` + `1222_perguntas_dificeis` | nemotron-3.5-super-vl-120b-a12b, 2 rodadas | 12 da E3 + 20 difíceis | igual ao GPT-OSS nas duas: 11/11, 8/8, 6/6, 0/6; 0 problemas de chamada; ~12 s por pergunta |
| `2026-11-18_1208` + `1210_perguntas_dificeis` e `1221` + `1223_perguntas_dificeis` | nemotron-3.5-lightning-30b-a3b, 2 rodadas | 12 da E3 + 20 difíceis | 10/11 e 11/11 na E3 (1 vez respondeu ao analista em vez de buscar); 8/8, 6/6, 0/6; respostas vazias ocasionais |
| `2026-11-18_1206` | mistral-large-4-1t-a52b | 12 da E3 | 11/11, ~10 vezes mais lento (as difíceis foram canceladas) |
| `2026-11-18_1157` + `1158_perguntas_dificeis` | nemotron-3.5-super-vl, antes das correções | 12 + 20 | 2 respostas vazias → limite de tokens 4096 e nova tentativa em resposta vazia |
| `2026-11-18_1314` e `2026-11-18_1334` | nemotron-3.5-super-vl, 2 rodadas | **137 de sintoma da suíte da E2** (`perguntas_sintoma_e2.json`) | até o 10º lugar: 130/131 e 131/131; além do 10º: 0/6 nas duas; a única falha (q-006, rodada 1) foi a lista de argumentos mandada como texto, agora convertida em código |
| `2026-11-18_1405_perguntas_sintoma_e2_..._20cand` | nemotron-3.5-super-vl, **20 candidatos** (`--candidatos 20`) | 137 de sintoma | 135/137: resolveu as 4 com o certo entre o 11º e o 20º, sem perder nenhuma das 131 até o 10º. O padrão continua em 10 (decisão do André: poucos casos se beneficiam) |
| `2026-11-18_1424_perguntas_e2_completa_...` | nemotron-3.5-super-vl, 10 candidatos | **suíte inteira da E2: 295** (`perguntas_e2_completa.json`) | certo aprofundado em 284/284 até o 10º lugar (sintoma 131/131, causa 137/137, geral 16/16); 0/6 além do 10º; das 5 fora do corpus, 3 procuraram outros incidentes e encerraram sem aprofundar e 2 aprofundaram incidentes parecidos, com o `why` dizendo o que não bate; 298 chamadas, 0 problemas; 13 min 26 s |

Uma rodada de 295 com 4 em paralelo falhou inteira no embedding (`float != BFloat16`, várias threads na GPU ao mesmo
tempo). Corrigido com uma trava em `rag/busca.py` (`vetorizar`); a rodada que falhou foi apagada.
