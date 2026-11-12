# E1.3 — Validação final da curadoria editorial

Data da validação: 2026-10-28 (UTC)

## Resultado executivo

A E1.3 terminou com 20 post-mortems tecnicamente qualificados e formalmente aprovados no registro editorial. Os 20 são elegíveis ao futuro corpus RAG segundo a fonte de verdade `data/reviews/editorial_reviews.csv`. Nenhum chunk, embedding ou índice foi criado.

| Etapa | Resultado comprovado |
|---|---:|
| Referências processadas do catálogo | 240 |
| Coletas bem-sucedidas | 224 |
| Falhas de coleta registradas | 14 |
| Itens ignorados conforme política | 2 |
| Documentos extraídos | 224 |
| Candidatos selecionados para curadoria | 20 |
| Documentos editorialmente aprovados | 20 |
| Documentos pendentes | 0 |
| Documentos rejeitados | 0 |
| Documentos elegíveis ao RAG | 20 |

Os totais de coleta e extração foram conferidos nos manifestos locais. O campo legado `rag_candidates` de `data/reports/summary.json` antecede o registro editorial independente e não é usado para determinar elegibilidade.

## Escopo da curadoria

O trabalho incluiu seleção de cinco candidatos iniciais e quinze candidatos adicionais, comparação de conteúdo extraído com HTML local, correções localizadas de extração, registro causal, limitações editoriais, auditoria de proveniência e duas rodadas explícitas de aprovação humana.

- Primeiro lote: 11 documentos aprovados por `andre morotti` em `2026-10-28T13:15:19Z`.
- Lote final: 9 documentos aprovados por `andre morotti` em `2026-10-28T13:33:51Z`.
- As decisões foram registradas pela CLI editorial, sem `--revise-existing`.
- Cada alteração preservou um backup do CSV e foi gravada atomicamente.

## Critérios de qualidade e elegibilidade

Foram priorizados relatos primários de incidentes com sintomas, impacto, evidência técnica, causa ou hipóteses, recuperação e prevenção. A seleção cobre mecanismos de Kubernetes, bancos de dados, redes, DNS, filas, cache, deploy, configuração, autenticação e sistemas distribuídos.

Um documento somente é elegível quando:

1. `editorial_decision=approved`;
2. `reviewed_by` é não vazio;
3. `reviewed_at` é um timestamp ISO-8601 válido em UTC.

Pendentes e rejeitados não são elegíveis. A consulta `scripts/editorial_review.py eligible` retornou exatamente os 20 IDs do registro.

## Proveniência

Os 20 valores de `source_url` do CSV foram comparados com os respectivos JSONs extraídos e coincidem integralmente. URLs históricas e redirecionamentos legítimos foram preservados, incluindo capturas do Wayback Machine e destinos finais registrados no histórico de coleta.

As correções finais de proveniência abrangeram DAN-066, DAN-169 e DAN-188. Correções anteriores abrangeram DAN-115 e DAN-137. Nenhum HTML RAW ou JSON extraído foi alterado durante as aprovações.

## Preservação de causalidade

As decisões editoriais não transformam hipóteses em causas confirmadas. Permanecem obrigatórias as seguintes interpretações:

- DAN-066: o postscript reclassifica a falha inicialmente chamada Byzantine como *omission fault*.
- DAN-169: relatório final e atualizações preliminares timestampadas devem permanecer distinguíveis.
- DAN-183: investigação técnica sem cadeia causal única definitivamente comprovada.
- DAN-188: preservar a evolução das hipóteses durante a investigação do autovacuum e locking.
- DAN-218: o mecanismo interno é documentado, mas a causa externa na AWS tem profundidade limitada.
- DAN-230: a origem dos erros S3 permaneceu sem confirmação.
- Incidentes multifatoriais, como DAN-109, DAN-115, DAN-137 e DAN-164, não devem ser reduzidos a uma causa única ou a culpa individual.

## Limitações conhecidas

A extração textual não interpreta valores presentes somente em imagens. As limitações registradas incluem:

- DAN-001: gráficos de tráfego, response time e threads não representados no texto.
- DAN-009: figuras incorporadas não representadas nem validadas visualmente.
- DAN-026: gráficos de processos e memória ausentes do texto extraído.
- DAN-118: diagramas de arquitetura, restauração e comunicação não representados visualmente.
- DAN-134: gráficos de filas, espera e provisionamento não extraídos.
- DAN-135: gráfico de erros iniciais de sincronização não representado.
- DAN-137: gráficos e diagramas de estados de regex não representados visualmente; descrições e números textuais foram preservados.
- DAN-183: figuras e screenshots de métricas não representados nem validados visualmente.

Nenhum número ou interpretação visual ausente foi inferido. Essas limitações permanecem anexadas aos registros aprovados e devem acompanhar metadados futuros.

## Integridade e testes

Resultados comprovados na validação final:

- Registro editorial válido: 20 registros únicos.
- Decisões: 20 aprovados, 0 pendentes e 0 rejeitados.
- Metadados: 20 registros com revisor e timestamp UTC válidos.
- Elegibilidade: 20 documentos retornados pela CLI.
- Proveniência: 20 de 20 `source_url` correspondentes aos JSONs.
- Suíte automatizada: 62 testes aprovados em 1,42 s.
- Checksums de `data/raw/` e `data/extracted/`: inalterados durante a operação final.
- Campo legado `editorial_approved` nos JSONs: permanece `false` em 20 de 20 candidatos.
- Coleta, downloads, requisições HTTP, chunking, embeddings e indexação: não executados nesta etapa.

## Estado final do corpus

O conjunto editorial aprovado contém 20 post-mortems e está pronto como entrada controlada para o desenho da E1.4. A aprovação representa aceitação editorial com as ressalvas registradas; não significa que imagens foram interpretadas nem que incertezas causais foram resolvidas.

## Pendências para a E1.4

As atividades abaixo ainda não foram executadas e permanecem pendentes:

1. Definir estratégia de chunking que preserve seções, timelines, listas e relações causais.
2. Propagar proveniência, causalidade e limitações visuais para metadados de cada chunk.
3. Separar corretamente relatório final e updates no DAN-169.
4. Impedir que hipóteses dos DAN-183, DAN-188, DAN-218 e DAN-230 sejam apresentadas como fatos confirmados.
5. Definir tratamento de referências a imagens e diagramas ausentes, sem inferir seu conteúdo.
6. Criar e validar embeddings e índice somente após decisão arquitetural específica da E1.4.
7. Desenvolver avaliação de recuperação, fidelidade causal e citações antes de disponibilizar o corpus ao Incident Copilot.

Estas pendências são planejamento futuro; nenhuma delas foi iniciada como parte da E1.3.
