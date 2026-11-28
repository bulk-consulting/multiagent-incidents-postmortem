# E1.3 — Mapeamento dos Dados

## 1. Identificação dos datasets

Os datasets escolhidos para o projeto foram:

| Dataset | O que é | Papel no projeto |
|---|---|---|
| `danluu-ingestion` | Post-mortems públicos coletados a partir de um catálogo de 240 links, com base na lista [danluu/post-mortems](https://github.com/danluu/post-mortems) | Base principal |
| [`incident-postmortem-assistant`](https://github.com/kai2055/incident-postmortem-assistant) | 20 incidentes públicos em Markdown, organizados em resumo, linha do tempo, causa raiz, resolução e prevenção | Complemento |

Os dois foram escolhidos porque reúnem incidentes reais de tecnologia, descrevem o que causou cada falha e como ela foi resolvida, e permitem indicar a fonte original, o que é necessário para as citações do Incident Copilot.

## 2. Análise exploratória inicial


### 2.1 Volume e formato

| Métrica | `danluu-ingestion` | `incident-postmortem-assistant` |
|---|---|---|
| Documentos | 224 extraídos de 240 links | 20 |
| Empresas | 104 no catálogo | 10 |
| Total de palavras | 415.198 | 18.909 |
| Palavras por documento (mediana) | 1.304 | 970 |
| Palavras por documento (mín.–máx.) | 2–37.704 | 426–1.669 |
| Formato | JSON | Markdown |

### 2.2 Campos disponíveis

| Dataset | Preenchidos em 100% dos documentos | Parcialmente preenchidos | Ausentes |
|---|---|---|---|
| `danluu-ingestion` | `catalog_id`, `company`, `source_url`, `final_url`, `category`, `fetched_at`, `content_hash` | `title` (99,6%), `extracted_text` (95,1%) | Data do incidente |
| `incident-postmortem-assistant` | `id`, `title`, `company`, `date`, `severity`, `duration_minutes`, `affected_services`, `root_cause_category` | `url` (75%) | — |

Os documentos de `incident-postmortem-assistant` têm sempre as mesmas cinco seções: Summary, Timeline, Root Cause, Resolution e Prevention.

Os documentos de `danluu-ingestion` não seguem uma estrutura fixa.

### 2.3 Qualidade

Foram analisados 224 documentos de `danluu-ingestion` e 20 documentos de `incident-postmortem-assistant`.

A tabela abaixo mostra os problemas que reduzem a qualidade de cada dataset e o percentual afetado: quanto menor, melhor. Um documento pode ter mais de um problema.

| Problema | `danluu-ingestion` | `incident-postmortem-assistant` |
|---|---|---|
| Link não coletado: a página não foi baixada | 6,7% | 0% |
| Documento sem texto: a página foi baixada, mas nenhum texto foi extraído | 4,9% | 0% |
| Texto curto: menos de 300 palavras | 4,0% | 0% |
| Conteúdo duplicado: documentos com texto idêntico | 4,0% | 0% |
| Marcado para revisão | 32,6% | 0% |
| Sem link da fonte: não é possível citar o documento | 0% | 25% |

## 3. Definição dos dados que alimentarão o RAG

O RAG receberá o texto dos documentos e os campos necessários para identificar e citar cada fonte:

| Campo no RAG | `danluu-ingestion` | `incident-postmortem-assistant` |
|---|---|---|
| Identificador | `catalog_id` | `id` |
| Título | `title` | `title` |
| Empresa | `company` | `company` |
| Link da fonte | `source_url` | `url` |
| Data do incidente (opcional) | Extraída do texto, quando disponível | `date` |
| Texto | `extracted_text` | Corpo do Markdown |


## 4. Conclusão

Os dois datasets são uma base inicial para o RAG: `danluu-ingestion` oferece maior volume, e `incident-postmortem-assistant` oferece documentos com estrutura padronizada. Os problemas identificados, incluindo os alertas de revisão gerados na coleta de `danluu-ingestion`, serão tratados na limpeza dos dados. **No futuro, novos datasets poderão ser adicionados caso seja necessário ampliar a base de conhecimento.**
