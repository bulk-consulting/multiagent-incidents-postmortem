# Status pages públicos (recoleta própria) + avaliação da IncidentDB

Corpus de incidentes reais publicados nos status pages públicos de provedores de cloud e SaaS.
Substitui o uso direto da IncidentDB (`trobasuj-cpu/incidentdb`), que foi avaliada e **não** será usada como está.

## Veredito

- **IncidentDB original: não usar no RAG.** Os campos `breaking_config_code`, `remediation_patch` e
  `prevention_checklist` são gerados por template no crawler (um único texto para os 448 registros,
  trocando só o nome da empresa). `root_cause_analysis` é a timeline colada e cortada em 450 caracteres.
  Parte do `service_stack` é preenchida com uma lista fixa por empresa.
- **Status pages (fonte por trás da IncidentDB): usar como corpus complementar de sintomas**,
  coletado com o nosso próprio script, indexando só o que os provedores publicaram.

## Conteúdo da pasta

| Caminho | O que é |
|---|---|
| `recoleta_statuspage.py` | Script de coleta (só biblioteca padrão do Python). Baixa `/api/v2/incidents.json` de 14 provedores. |
| `raw/` | Resposta bruta da API por provedor. Prova de proveniência; não editar. |
| `timelines.jsonl` | Saída do script: um incidente por linha, timeline completa em ordem cronológica. |
| `processed/base_incidentes_v2.jsonl` | Base combinada classificada (722 incidentes), com `timeline_text`. Entrada do RAG. |
| `processed/base_incidentes_v2.csv` | Mesma base sem a timeline, para leitura e filtros. |
| `incidentdb_avaliacao/explore.py` | Script de profiling usado para avaliar a IncidentDB original. |
| `incidentdb_avaliacao/classificacao_causas_v1.csv` | Classificação dos 448 incidentes da IncidentDB original (evidência do veredito). |
| `incidentdb_avaliacao/incidentdb_snapshot/` | Cópia do repositório original da IncidentDB (commit `925ac05a`), sem `.git`, `rag_vault/` e `notebook/`. Proveniência e checksums em `PROVENIENCIA.md`. |

## Como os dados foram gerados

1. **Coleta** (30/10/2026): `python recoleta_statuspage.py`. 13 de 14 provedores responderam;
   o Datadog retornou HTTP 403. Ele foi deixado de fora porque, na base original, teve 0 causas
   concretas em 50 incidentes.
2. **Junção**: os 448 incidentes da IncidentDB original (só os campos reais) foram combinados com os
   274 incidentes novos da recoleta, casando por `incident_id`. 10 incidentes já existentes ganharam
   timelines mais completas.
3. **Classificação de causa**: feita por leitura de LLM (Claude), incidente por incidente, em lotes
   de 100, **não** por palavras-chave. Um filtro de palavras-chave testado antes errava muito:
   dos 124 que marcou, 44 não tinham causa e 46 eram vagos.

## Campos da base processada

| Campo | Descrição |
|---|---|
| `incident_id`, `company`, `date`, `title` | Identificação do incidente (originais do status page). |
| `severity_ou_impact` | Severidade da IncidentDB ou `impact` da API (none/minor/major/critical). |
| `nivel_causa` | `CONCRETA` (diz o que falhou e por quê), `VAGA` (só a categoria) ou `SEM_CAUSA`. |
| `origem_causa` | `interna`, `externa` (provedor ou dependência upstream) ou `indefinida`. |
| `causa_resumo` | Resumo da causa em português, escrito na classificação. |
| `mitigacao_real` | Ação de mitigação descrita pelo provedor, quando há. |
| `tem_mitigacao_real` | Booleano derivado do campo acima. |
| `fonte` | `base_original`, `recoleta` ou `base_original+recoleta`. |
| `has_postmortem` | Se a timeline tem uma atualização de post-mortem. |
| `source_url` | Link oficial do incidente (citação). |
| `timeline_text` | Texto completo das atualizações (só no JSONL). |

## Números

| | Total | Concreta | Vaga | Sem causa |
|---|---|---|---|---|
| IncidentDB original | 448 | 45 | 66 | 337 |
| Base combinada v2 | 722 | 70 | 127 | 525 |

- 171 incidentes descrevem alguma mitigação real.
- Causas concretas concentradas em GitHub (39) e CircleCI (11, quase todas de post-mortems).
- OpenAI, Datadog, npm, Reddit e Supabase: 0 causas concretas.
- Cerca de 65 eventos distintos entre os 70 concretos (há recorrências e incidentes com o mesmo post-mortem).

## Limitações

- A API devolve só os **50 incidentes mais recentes** por provedor. Para acumular histórico, a coleta
  precisa ser repetida periodicamente.
- Fonte de provedores **SaaS**, não de operação de infraestrutura. Quase não há casos de disco, kernel,
  rede física ou nó de Kubernetes.
- Status pages **não publicam código/config alterado** e raramente trazem checklist de prevenção.
  Esses requisitos do Copilot precisam vir de outras fontes (ex.: danluu/post-mortems).
- A Atlassian devolve incidentes de 2019–2025; os demais provedores são quase todos de 2026.
- Termos de uso: o conteúdo é texto publicado pelos provedores. Uso interno, sempre com `source_url`.

## Uso no RAG

- **Indexar:** `title` + `timeline_text`, com metadados `company`, `date`, `nivel_causa`,
  `origem_causa`, `has_postmortem`, `source_url`.
- **Não indexar:** nenhum campo de template da IncidentDB, nem os Markdown do `rag_vault/`.
- `nivel_causa` serve para o Copilot distinguir quando tem só evidência de sintoma e quando tem causa
  documentada (nível de confiança e loop de evidência insuficiente).
