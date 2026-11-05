# E2.5 — Validação da Ingestão

Comandos executados no Git Bash a partir da raiz do projeto, com o ambiente virtual e o banco ativos (ver `E2_1_Ambiente_Desenvolvimento.md`).

## 1. Contagem de chunks

```bash
docker exec incident-copilot-db psql -U copilot -d incident_copilot -c "SELECT chunk_type, count(*) FROM chunk GROUP BY chunk_type;"
```

```text
 chunk_type | count
------------+-------
 text       |  2314
 summary    |   211
```

Os números batem com o chunking (E2.3): 2.525 chunks de 211 incidentes.

## 2. Amostra de embeddings

```bash
docker exec incident-copilot-db psql -U copilot -d incident_copilot -c "SELECT chunk_id, vector_dims(embedding) AS dimensoes, left(embedding::text, 60) AS inicio FROM chunk LIMIT 3;"
```

```text
  chunk_id   | dimensoes |                            inicio
-------------+-----------+--------------------------------------------------------------
 DAN-001-000 |       768 | [0.019335719,0.051959433,-0.029933127,0.0061120107,0.0414976
 DAN-001-001 |       768 | [0.003030334,0.06606757,-0.02289596,0.0016671887,0.055801146
 DAN-001-002 |       768 | [0.014872185,0.030314501,-0.010542229,-0.0067200484,0.015733
```

Cada chunk tem um vetor de 768 números, o tamanho gerado pelo modelo `multilingual-e5-base`.

## 3. Busca no pgvector

O script `search.py` recebe uma descrição em texto livre e mostra os 5 chunks mais parecidos:

```bash
python ./dataset_nela/danluu-ingestion/scripts/search.py "o banco de dados foi apagado por engano"
```

```text
1. DAN-164-000 | Gitlab | Postmortem of database outage of January 31
   similaridade 0.843 | https://about.gitlab.com/2017/02/10/postmortem-of-database-outage-of-january-31/
2. DAN-164-001 | Gitlab | Postmortem of database outage of January 31
...
```

O primeiro resultado é o incidente do GitLab de 2017, em que um administrador apagou o banco de produção por engano.

Para ver o texto de um chunk retornado:

```bash
docker exec incident-copilot-db psql -U copilot -d incident_copilot -c "SELECT content FROM chunk WHERE chunk_id = 'DAN-164-001';"
```

O texto confirma que o resultado é coerente com a busca: *"The outage was caused by an accidental removal of data from our primary database server."*

## 4. Como saber se os resultados estão certos

Em vez de ler cada resultado, usamos **incidentes conhecidos**: escrevemos, com palavras simples e em português, a descrição de um incidente que sabemos que está na base, e conferimos se ele aparece entre os 5 primeiros resultados.

```bash
python ./dataset_nela/danluu-ingestion/scripts/validate_rag.py
```

O script repete as verificações 1 e 2 e faz 6 buscas de teste:

| Descrição usada na busca | Incidente esperado |
|---|---|
| Um administrador cansado apagou o diretório errado e perdemos seis horas de dados | GitLab, 2017 (DAN-164) |
| Um comando digitado errado removeu servidores demais e derrubou o armazenamento S3 | Amazon S3, 2017 (DAN-104) |
| Um certificado expirou e os complementos do navegador Firefox pararam de funcionar | Mozilla, 2019 (DAN-090) |
| Raios atingiram o datacenter e causaram queda de energia nos discos | Google, 2015 (DAN-071) |
| Um deploy com versões diferentes do código causou prejuízo de 460 milhões de dólares | Knight Capital, 2012 (DAN-084) |
| O cliente do Steam apagou todos os arquivos do computador do usuário | Valve (DAN-236) |

**Resultado: 6 de 6.** Todos os incidentes esperados aparecem entre os 5 primeiros, e as buscas em português encontram documentos escritos em inglês.
