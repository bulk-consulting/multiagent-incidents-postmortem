# E2.4 — Geração e Armazenamento de Embeddings

O script `dataset_nela/danluu-ingestion/scripts/embed.py` gera um embedding para cada chunk de `data/chunks/danluu_chunks.jsonl` e grava os incidentes e os chunks no PostgreSQL + pgvector.

## Tabelas

Definidas em `db/schema.sql`:

**`incident`**: um registro por post-mortem.

| Coluna | Conteúdo |
|---|---|
| `catalog_id` | Identificador (`DAN-011`), chave primária |
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
| `content` | Texto do chunk, com o cabeçalho |
| `embedding` | Vetor de 768 dimensões |

## Metadados

| Metadado | Onde fica |
|---|---|
| Fonte | `incident.source_url` e `incident.company` |
| Tipo | `chunk.chunk_type` |
| Tags | `incident.category` |
| Data | `incident.incident_date` |

A data fica vazia: a danluu não tem um campo de data. Às vezes ela aparece no título ou no primeiro parágrafo, mas em formatos diferentes e difíceis de extrair automaticamente.

## Como executar

Com o banco ativo (ver `E2_1_Ambiente_Desenvolvimento.md`):

```bash
python ./dataset_nela/danluu-ingestion/scripts/embed.py
```

Leva cerca de 20 minutos em CPU.

## Como funciona

1. Cria as tabelas, se não existirem.
2. A cada nova execução, as tabelas são esvaziadas e carregadas de novo, sem duplicados.
3. Gera os embeddings com o modelo `multilingual-e5-base`
4. Grava os 211 incidentes e os 2.525 chunks.
