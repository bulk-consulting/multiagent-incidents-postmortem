# E2.3 — Estratégia de Chunking

O script `dataset_nela/danluu-ingestion/scripts/chunk.py` divide os 212 post-mortems de `data/processed/danluu_clean.jsonl` em chunks e grava o resultado em `data/chunks/danluu_chunks.jsonl`: **2.494 chunks** (212 de summary e 2.282 de texto).

## Como funciona

1. **Parágrafos.** O texto é separado em parágrafos pelo `\n\n`. Assim, nenhuma ideia é cortada no meio.

2. **Summary.** O primeiro chunk de cada documento é o `summary` (o resumo do catálogo da danluu). Ele descreve o incidente inteiro em poucas palavras e ajuda a busca a encontrar o documento certo. Vai **sem cabeçalho**: só o texto do resumo. Com o cabeçalho na frente (título longo, categoria), o vetor ficava menos parecido com as perguntas; sem ele, o incidente certo em 1º lugar subiu de 70% para 80% (ver `E2_5_Validacao_Ingestao.md`).

3. **Juntar parágrafos.** Parágrafos seguidos são somados até chegar a no máximo **450 tokens, contando o cabeçalho**. Um parágrafo sozinho costuma ser curto demais para ter sentido (a mediana é de 17 tokens).

4. **Títulos.** Quando aparece um título, o chunk atual termina e um novo chunk começa a partir dele.

5. **Seções longas.** Quando uma seção não cabe em um chunk, cada chunk que a continua começa **repetindo o título da seção** (`## Root cause`). Assim, um trecho do meio da seção não fica sem contexto. Só ficam sem título os chunks da introdução, antes do primeiro título do documento (151 de 2.109 nos documentos que têm títulos).

6. **Overlap.** Quando um parágrafo sozinho não cabe:
   - Ele é dividido em partes de tamanho parecido.
   - O corte é sempre no fim de uma frase.
   - Cada parte repete as últimas frases da anterior (até **60 tokens**).

7. **Chunks repetidos.** Um chunk idêntico a outro do mesmo documento é descartado. Acontece em páginas de status que trazem o mesmo relatório duas vezes (5 chunks no DAN-031).

Além disso, todo chunk de texto começa com um **cabeçalho** com a empresa, o título e a categoria do documento. Assim, cada trecho carrega o contexto de onde veio:

```text
Company: Cloudflare | Title: Cloudflare outage on November 18, 2025 | Cloudflare Blog | Category: Config Errors
```

## Por que 450 tokens

- O limite conta o chunk inteiro, com o cabeçalho: nenhum chunk passa de 450 (mediana de 310 nos de texto).
- Cabe nos 512 tokens do `multilingual-e5-base`, caso seja preciso comparar modelos de novo.
- O modelo usado (Qwen3-Embedding-0.6B) lê bem mais que isso, mas chunks maiores misturam mais assuntos num vetor só. Aumentar o limite só vale com uma medição.

Os tokens são contados com o tokenizer do `multilingual-e5-base`. O Qwen3 tem outro tokenizer; a contagem do e5 serve como aproximação do tamanho.

Exemplo: incidente DAN-004 — [chunks_DAN-004.html](../dataset_nela/danluu-ingestion/data/exports/chunks_DAN-004.html)

## Como executar

```bash
python ./dataset_nela/danluu-ingestion/scripts/chunk.py
```

Para gerar a visualização de um documento (grava em `data/exports/`):

```bash
python ./dataset_nela/danluu-ingestion/scripts/visualize_chunks.py DAN-004
```
