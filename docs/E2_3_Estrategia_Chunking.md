# E2.3 — Estratégia de Chunking

O script `dataset_nela/danluu-ingestion/scripts/chunk.py` divide os 211 post-mortems de `data/processed/danluu_clean.jsonl` em chunks e grava o resultado em `data/chunks/danluu_chunks.jsonl`.

## Como funciona

1. **Parágrafos.** O texto é separado em parágrafos pelo `\n\n`. Assim, nenhuma ideia é cortada no meio.

2. **Summary.** O primeiro chunk de cada documento é o `summary` (o resumo do catálogo da danluu). Ele descreve o incidente inteiro em poucas palavras e ajuda a busca a encontrar o documento certo.

3. **Juntar parágrafos.** Parágrafos seguidos são somados até chegar a no máximo **400 tokens**. Um parágrafo sozinho costuma ser curto demais para ter sentido (a mediana é de 17 tokens).

4. **Overlap.** Quando um parágrafo passa de 400 tokens:
   - Ele é dividido em partes de tamanho parecido.
   - O corte é sempre no fim de uma frase.
   - Cada parte repete as últimas frases da anterior (até **60 tokens**).

5. **Títulos.** Quando aparece um título, o chunk atual termina e um novo chunk começa a partir dele.

Além disso, todo chunk começa com um **cabeçalho** com a empresa, o título e a categoria do documento. Assim, cada trecho carrega o contexto de onde veio:

```text
Company: Cloudflare | Title: Cloudflare outage on November 18, 2025 | Category: Config Errors
```

Os tokens são contados com o tokenizer do modelo de embeddings (`multilingual-e5-base`), que aceita no máximo 512 tokens por trecho.

Exemplo: incidente DAN-004 — [chunks_DAN-004.html](../dataset_nela/danluu-ingestion/data/exports/chunks_DAN-004.html)

## Como executar

```bash
python ./dataset_nela/danluu-ingestion/scripts/chunk.py
```
