# E2.4 — Geração e Armazenamento de Embeddings

O script `dataset_nela/danluu-ingestion/scripts/embed.py` gera um embedding para cada chunk de `data/chunks/danluu_chunks.jsonl`, guarda os vetores em `data/embeddings/qwen3/` e grava os incidentes e os chunks no PostgreSQL + pgvector.

## Modelo: Qwen3-Embedding-0.6B

| | |
|---|---|
| Modelo | `Qwen/Qwen3-Embedding-0.6B` (Apache 2.0, roda localmente) |
| Dimensões | 1024 |
| Chunks | codificados sem prefixo |
| Perguntas | codificadas com a instrução `Instruct: Given a description of a production incident, retrieve post-mortem passages about similar incidents` + `Query: <pergunta>` |

*Por quê:* os documentos estão em inglês e as perguntas podem vir em português. Nos testes de busca com perguntas nos dois idiomas, o Qwen3 encontrou o incidente certo com mais frequência que o `multilingual-e5-base` e o `bge-m3`, com a maior diferença nas perguntas em português.

No processador, o modelo é carregado em float32: o padrão dele (bfloat16) foi duas vezes mais lento neste notebook (10,3 s contra 5,3 s por chunk), com vetores praticamente iguais (similaridade de cosseno ≥ 0,998).

## Vetores guardados no git

Gerar os 2.494 vetores no processador levou **cerca de 2 horas** num notebook sem GPU (~3 s por chunk). Por isso os vetores ficam versionados em `data/embeddings/qwen3/`:

| Arquivo | Conteúdo |
|---|---|
| `vectors.npy` | Um vetor por linha, em float16 (~5 MB para todos os chunks) |
| `index.json` | O modelo e, na mesma ordem das linhas, o `chunk_id` e o hash do texto que virou vetor |

A cada execução, um vetor só é reaproveitado se o **`chunk_id` e o hash do texto** forem os mesmos. Se o texto de um chunk muda (por exemplo, por uma mudança no chunking), mesmo com o mesmo `chunk_id`, o vetor é gerado de novo. Só os vetores que faltam são gerados.

Os vetores são guardados a cada 64 chunks (~5 minutos no processador), e o script mostra quanto falta. Se a execução for interrompida (computador suspenso, terminal fechado, Ctrl+C), basta rodar de novo: ela reaproveita o que já foi gerado e continua de onde parou, perdendo no máximo o bloco em andamento.

Regra: quando os chunks mudarem, gerar os vetores e fazer o commit dos dois juntos.

## Tabelas

Definidas em `db/schema.sql`:

**`incident`**: um registro por post-mortem.

| Coluna | Conteúdo |
|---|---|
| `catalog_id` | Identificador (`DAN-011`), chave primária |
| `dataset` | De onde veio o incidente (`danluu`), para receber outras bases sem mudar o banco |
| `company` | Empresa |
| `title` | Título do post-mortem |
| `source_url` | Link da fonte original |
| `category` | Categoria da danluu (`Config Errors`, `Database`…) |
| `incident_date` | Data do incidente (vazia, ver abaixo) |

**`chunk`**: um registro por chunk.

| Coluna | Conteúdo |
|---|---|
| `chunk_id` | Identificador (`DAN-011-001`), chave primária |
| `catalog_id` | Incidente de origem |
| `chunk_type` | `summary` ou `text` |
| `content` | Texto do chunk (os de texto, com o cabeçalho) |
| `embedding` | Vetor de 1024 dimensões |

## Metadados

| Metadado | Onde fica |
|---|---|
| Fonte | `incident.source_url`, `incident.company` e `incident.dataset` |
| Tipo | `chunk.chunk_type` |
| Tags | `incident.category` |
| Data | `incident.incident_date` |

A data fica vazia: a danluu não tem um campo de data. Às vezes ela aparece no título ou no primeiro parágrafo, mas em formatos diferentes e difíceis de extrair automaticamente.

## Como executar

Com o banco ativo (ver `E2_1_Ambiente_Desenvolvimento.md`):

```bash
python ./dataset_nela/danluu-ingestion/scripts/embed.py
```

Para testar sem esperar horas, gerar no máximo um vetor novo (os chunks sem vetor ficam fora do banco):

```bash
python ./dataset_nela/danluu-ingestion/scripts/embed.py --limit 1
```

## Como funciona

1. Calcula o hash do texto de cada chunk e reaproveita os vetores guardados que batem.
2. Gera os vetores que faltam com o `Qwen3-Embedding-0.6B` (normalizados) e atualiza `data/embeddings/qwen3/`.
3. Apaga e recria as tabelas, porque o tamanho do vetor depende do modelo. Cada carga substitui a anterior, sem duplicados.
4. Grava os 212 incidentes e os chunks que têm vetor (2.494 com todos os vetores gerados).
