# E2.2 — Pipeline de Ingestão (danluu)

Scripts que transformam a lista de post-mortems da danluu em um arquivo de texto limpo, pronto para o RAG. Os comandos são executados no Git Bash a partir da raiz do projeto, com o ambiente virtual ativo (ver `E2_1_Ambiente_Desenvolvimento.md`). Os dados ficam em `dataset_nela/danluu-ingestion/data/`.

## Fluxo

```mermaid
flowchart LR
    R["README.md<br/>danluu/post-mortems"] -->|build_catalog.py| A
    A["catalog.csv<br/>240 links"] -->|collect.py| B["raw/<br/>HTML e PDF"]
    B -->|extract.py| C["extracted/<br/>1 JSON por post-mortem"]
    C -->|clean.py| D["processed/<br/>danluu_clean.jsonl"]

    classDef entrada fill:#E3F2FD,stroke:#64B5F6,color:#0D47A1
    classDef bruto fill:#FFF8E1,stroke:#FFB74D,color:#E65100
    classDef extraido fill:#F3E5F5,stroke:#BA68C8,color:#4A148C
    classDef limpo fill:#E8F5E9,stroke:#81C784,color:#1B5E20
    class R,A entrada
    class B bruto
    class C extraido
    class D limpo
```

## 0. Dependências (só na primeira vez)

```bash
pip install -r ./dataset_nela/danluu-ingestion/requirements.txt
```

## 1. Catálogo

Gera o arquivo CSV com os links dos post-mortems a partir do `README.md` do repositório [danluu/post-mortems](https://github.com/danluu/post-mortems).

```bash
python ./dataset_nela/danluu-ingestion/scripts/build_catalog.py
```

## 2. Coleta

Baixa as páginas (HTML e PDF) de cada link e grava na pasta `data/raw/`.

```bash
python ./dataset_nela/danluu-ingestion/scripts/collect.py
```

## 3. Extração

Extrai o texto das páginas e grava um JSON por post-mortem na pasta `data/extracted/`.

```bash
python ./dataset_nela/danluu-ingestion/scripts/extract.py
```

## 4. Limpeza

Remove os documentos sem texto útil e junta o resto em um único arquivo, `data/processed/danluu_clean.jsonl`.

```bash
python ./dataset_nela/danluu-ingestion/scripts/clean.py
```
