# E3.2 — Integração com a LLM

## Arquivo

`dataset_nela/danluu-ingestion/scripts/llm.py`

```bash
python dataset_nela/danluu-ingestion/scripts/llm.py "Em uma frase, o que é um post-mortem de incidente na área de SRE?"
```

## Chamadas de teste

| Pergunta | Resposta | Tempo |
|---|---|---|
| Responda apenas: OK | OK | 137,7 s |
| Em uma frase, o que é um post-mortem de incidente na área de SRE? | Um post‑mortem de incidente na área de SRE é uma análise estruturada e detalhada dos eventos, causas e lições aprendidas após um incidente, com o objetivo de melhorar a confiabilidade e prevenir recorrências. | 143,4 s |
| In one sentence, what is connection pool exhaustion in a database? | Connection pool exhaustion occurs when every connection in the database’s pool is occupied, leaving no free connections for new requests and causing connection‑request failures. | 132,2 s |
