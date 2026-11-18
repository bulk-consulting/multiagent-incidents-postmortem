# Conferência: RAG da E3 com o Nemotron 3.5 super-vl

Data: 2026-11-18. Rodada: `2026-11-18_1439` (12 perguntas, prompt v2, 5 incidentes × 4 trechos, modelo
`nvidia/nemotron-3.5-super-vl-120b-a12b`, `max_tokens=8192`).

**Motivo:** o `openai/gpt-oss-20b` saiu do NVIDIA NIM em 18/11/2026 e a equipe adotou o Nemotron 3.5 super-vl.
Esta conferência repete, com o modelo novo, a leitura manual feita na entrega 3.5
(`conferencia_prompt_v1_v2_2026-11-11.md` e `conferencia_banco_mari_2026-11-12.md`).

**Rodada anterior, com `max_tokens=2048`** (`2026-11-18_1437_nemotron_2048tokens`): 6 de 12 respostas pararam por
limite de tokens antes de chamar a ferramenta (`finish_reason=length`), e a q01 falhou depois de 3 tentativas. O
modelo raciocina antes de responder. Com 8192, as 12 saíram na primeira tentativa.

**Como foi conferido:** o contexto de cada pergunta foi reconstruído com a mesma busca (determinística; os IDs
batem com os recuperados salvos). Cada número, data, nome e causa das respostas foi procurado literalmente no
contexto. A classificação é leitura humana.

## Checagens automáticas

| | Resultado |
|---|---|
| perguntas respondidas | 12/12 |
| cita o incidente esperado | 11/11 |
| cita ID fora do contexto | 0 |
| q12 (fora do corpus) | "insuficiente", sem inventar causa nem duração |
| tempo por pergunta | 5 a 52 s |

## Erros encontrados

| q | Tipo | O que foi escrito | O que o contexto diz |
|---|---|---|---|
| q07 | **invenção** (fronteira) | o relógio foi atrasado "sem que `clock_was_set()` fosse chamada" | o resumo do DAN-089 só diz "not done via a mechanism that would update `hrtimer base.offset`". O nome da função está no post-mortem completo, mas não nos trechos enviados: veio do conhecimento do modelo |
| q01 | **leitura errada** (leve) | "a restauração levou mais de 18 horas" | "GitLab.com was down for about 18 hours" |
| q09 | formatação | "exfililtrava" (erro de digitação) | — |

Tudo o mais foi encontrado no contexto, por exemplo:
- q02: os horários de recuperação (12:26PM, 1:18PM, 1:54PM PST), o placement subsystem, a auditoria das ferramentas
  e a repriorização do particionamento do index subsystem;
- q04: as quatro descargas, 09:19 PDT, os 5% dos discos, os 0,000001% e os discos não afetados;
- q09: as versões `eslint-config-eslint@5.0.2`, `eslint-scope@3.7.2` e `3.7.3`, o `postinstall`, o `.npmrc`, o
  pastebin e a revogação dos tokens anteriores a 12:30 UTC;
- q11: o *valid-to* calculado somando um ao ano, o timeout de 25 minutos do HA (que o Nemotron 3.5 tinha atribuído
  ao Fabric Controller no teste de 11/11) e os três timeouts seguidos.

Nas q08, q11 e q12, os IDs a mais citados são de incidentes que a resposta diz explicitamente **não** terem relação
("não mencionam certificados", "nenhum deles se refere ao Pix").

## Comparação

| | GPT-OSS-20B, v2 (média por rodada, E3) | Nemotron 3.5 super-vl, v2 (1 rodada) |
|---|---|---|
| invenções | ~0,7 | 1 (fato verdadeiro, mas fora do contexto) |
| leituras erradas | ~2 | 1 (leve) |
| português | fraco (concordância, palavras estranhas) | bom |
| tempo por pergunta | ~150 s | ~15 s |

Uma rodada só: é tendência, não prova. As respostas do Nemotron são mais longas e detalhadas, o que significa
mais afirmações para conferir; mesmo assim, apareceram menos erros de leitura.
