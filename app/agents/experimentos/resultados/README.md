# Resultados dos testes do Agente Pesquisa RAG

Gerados por `app/agents/experimentos/avaliar_pesquisa.py`, no banco da ingestão da main. Cada rodada tem
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
