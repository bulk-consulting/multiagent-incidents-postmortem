# Conferência: RAG sobre a ingestão da Mari (2026-11-12)

Três rodadas com as 12 perguntas, GPT-OSS-20B, prompt v2, 5 incidentes × 4 trechos: os mesmos parâmetros das
rodadas v2 da entrega (`2026-11-11_1802`, `_1904`, `_1938`, feitas sobre o banco da `ingestion/`). Muda só a busca:
duas etapas (`rag/busca.py`) sobre as tabelas `incident`/`chunk` da ingestão da Mari.

| Rodada | Arquivo | Observação |
|---|---|---|
| a | `2026-11-12_1925` | |
| b | `2026-11-12_2004` + `2026-11-12_2030` | Na `2004`, a q09 falhou nas 4 tentativas (o modelo devolveu JSON com caractere de controle inválido). Rodada de novo sozinha na `2030`. |
| c | `2026-11-12_2017` | |

Conferido como na conferência da entrega: cada resposta lida junto com o contexto exato que o modelo recebeu
(reconstruído com a mesma busca; os IDs recuperados batem com os das rodadas), procurando no texto cada número,
data, nome e afirmação de causa ou correção.

## Recuperação (igual nas três rodadas)

| Pergunta | Entrega (3 rodadas v2) | Banco da Mari |
|---|---|---|
| q04 | esperado em 2º | em 3º |
| q07 | em 2º | em 1º |
| q10 | fora dos 5 (8º), resposta "insuficiente" | **em 1º, resposta "forte" e correta nas 3 rodadas** |
| q11 | DAN-090 em 1º, DAN-086 em 2º | ordem trocada |
| demais | iguais | iguais |

Nas três rodadas, as 11 perguntas com incidente esperado tiveram o esperado no contexto e citado, sem ID fora do
contexto. A q12 (fora do corpus) saiu "insuficiente" nas três.

## Invenções

| Rodada | Pergunta | Na resposta | No contexto |
|---|---|---|---|
| b | q09 | no [DAN-152] (ESLint), "adoção de 2-FA e a exigência de revisão de pull-request antes de permitir push direto ao master" | Essas medidas são do incidente do Homebrew, que também estava no contexto (*"enabled 2FA... require CI checks from a pull request to pass before changes can be pushed to master"*). O postmortem do ESLint só diz que o mantenedor não tinha 2FA. |

## Leituras erradas

| Rodada | Pergunta | Na resposta | No contexto |
|---|---|---|---|
| a | q11 | "como o Firefox **ignorava** a verificação de certificado em alguns cenários" | A equipe **achava** isso, e estava errada: *"thought (incorrectly) that Firefox ignored the expiration dates"*. |
| b | q03 | "equipe ignorou data de expiração devido a diretrizes pré-existentes" | A equipe sabia da expiração, mas achava que o Firefox a ignorava, por causa de um incidente anterior. "Diretrizes" não aparece no texto. |
| c | q01 | os dados "não eram recuperáveis a partir de backups existentes, pois os backups diários não eram automáticos nem bem documentados" | O que *"was not automated, nor was it documented properly"* era a reconstrução da réplica secundária, não os backups. |
| c | q11 | "a verificação de certificados de **nível intermediário** foi desativada" | Foi desativada a de *end-entity*, e isso *"led to confusion about the status of intermediate certificate checking"*. |

## Fronteira (não contadas como erro)

- **a, q07:** "loops que dependiam de `clock_nanosleep`". O contexto fala em *"sleep for less than one second in a loop"*, sem citar a função.
- **b, q01:** "a equipe automatizou a restauração e atualizou a documentação", no passado. O contexto diz que estão *"working on multiple improvements"*.
- **b, q05:** "gerando transações erradas pelas 8 máquinas". O código antigo só estava no 8º servidor.
- **c, q05:** "quando a equipe conseguiu parar o sistema e restaurar a implantação original". O contexto só diz *"Eventually they were able to stop the system"*.

## Formatação e português

- **a, q06:** resposta inteira em inglês, contra a regra 7. O conteúdo está correto (`rm -rf "$STEAMROOT/"*` no `steam.sh`).
- **a, q01:** copia "perdemos seis horas de dados" da pergunta, tem um trecho truncado ("passa-durante o pós-evento") e não cita o ID no texto (só no campo da ferramenta).
- **a, q03:** traduz *certificate store* como "nuvem de certificados".
- **a, q04** ("Dois adicionais eventos"), **a, q08** ("O incidenti"), **b, q03** ("expirões"), **b, q04** ("luzes de raios"), **c, q05** ("deploy trinta-hora").

## Comparação com a entrega

| | Entrega v2 (3 rodadas) | Banco da Mari (3 rodadas) |
|---|---|---|
| Invenções | 2 | 1 |
| Leituras erradas | 6 | 4 |
| q10 respondida com o incidente certo | 0 de 3 | 3 de 3 |
| q12 marcada "insuficiente" | 3 de 3 | 3 de 3 |

A diferença em invenções e leituras erradas é pequena e muda de pergunta a cada rodada (`temperature=1.0`), então
não indica que o texto melhorou. O ganho que se repete é o da busca: a q10 passou a receber a evidência e foi
respondida corretamente nas três rodadas. A única invenção misturou medidas de outro incidente presente no mesmo
contexto, um risco que existe nas duas bases.

## Correção

A primeira versão desta conferência, só com a rodada a, apontava 3 invenções (q04: "quatro raios" e "13 de agosto
de 2015"; q05: a reversão do deploy). Estava errada: o auxiliar de busca procurava os termos alternativos
("uninstall\|removed") como um texto literal único e não os encontrava. Os três fatos estão no contexto:
*"At 09:19 PDT on Thursday 13 August 2015, four successive lightning strikes..."* e *"they reacted by uninstalling
the new code from the servers it was deployed to correctly"*.
