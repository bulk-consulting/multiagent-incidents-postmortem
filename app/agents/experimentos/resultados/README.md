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
| `2026-11-17_1522` | v3 (versão atual) | 12 da E3 | certo aprofundado em 11/11; q12 (fora do corpus) procurou e encerrou sem aprofundar; 0 malformadas |

Cuidados ao ler: cada versão rodou uma vez, e o modelo varia entre rodadas (temperatura 1,0). As
diferenças de 1 ou 2 perguntas são tendência, não prova.
