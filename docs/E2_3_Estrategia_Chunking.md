# E2.3 — Estratégia de Chunking

O script `dataset_nela/danluu-ingestion/scripts/chunk.py` divide os 211 post-mortems de `data/processed/danluu_clean.jsonl` em chunks e grava o resultado em `data/chunks/danluu_chunks.jsonl`.

## Como funciona

1. **Parágrafos.** O texto é separado em parágrafos pelo `\n\n`. Assim, nenhuma ideia é cortada no meio.

2. **Juntar parágrafos.** Parágrafos seguidos são somados até chegar a no máximo **400 tokens**. Um parágrafo sozinho costuma ser curto demais para ter sentido (a mediana é de 17 tokens).

3. **Summary.** O primeiro chunk de cada documento é o `summary` (o resumo do catálogo da danluu). Ele descreve o incidente inteiro em poucas palavras e ajuda a busca a encontrar o documento certo.

4. **Overlap.** Um parágrafo com mais de 400 tokens é dividido em partes de 400 tokens. Cada parte repete os últimos **60 tokens** da anterior, para que uma ideia cortada na divisão apareça inteira em pelo menos uma delas.

5. **Títulos.** Um título (linha que começa com `#`) nunca fica sozinho: ele vai junto com o parágrafo seguinte.

Além disso, todo chunk começa com um **cabeçalho** com a empresa, o título e a categoria do documento. Assim, cada trecho carrega o contexto de onde veio:

```text
Company: Cloudflare | Title: Cloudflare outage on November 18, 2025 | Category: Config Errors
```

Os tokens são contados com o tokenizer do modelo de embeddings (`multilingual-e5-base`), que aceita no máximo 512 tokens por trecho.

## Como executar

```bash
python ./dataset_nela/danluu-ingestion/scripts/chunk.py
```
