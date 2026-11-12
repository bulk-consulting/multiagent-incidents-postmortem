# E2.5 — Validação da Ingestão

Comandos executados no Git Bash a partir da raiz do projeto, com o ambiente virtual e o banco ativos (ver `E2_1_Ambiente_Desenvolvimento.md`).

## 1. Validação do banco

```bash
python ./dataset_nela/danluu-ingestion/scripts/validate_rag.py
```

O script faz quatro verificações:

1. **Contagem:** incidentes e chunks no banco, e quantos chunks do arquivo de chunking ficaram fora do banco.
2. **Integridade:** cada linha deve mostrar `OK` (zero problemas):
   - vetores com dimensão diferente de 1024;
   - vetores sem norma 1 (não normalizados);
   - chunks com texto vazio;
   - incidentes sem nenhum chunk ou sem o chunk de summary;
   - tipos de chunk desconhecidos;
   - chunks com o mesmo vetor de outro chunk.
3. **Amostra de embedding:** o primeiro chunk, com o número de dimensões e o início do vetor.
4. **Buscas de teste:** 6 descrições simples de incidentes conhecidos, em inglês; o incidente esperado deve aparecer entre os 5 primeiros resultados.

| Descrição usada na busca | Incidente esperado |
|---|---|
| a tired administrator deleted the wrong directory and we lost six hours of data | GitLab, 2017 (DAN-164) |
| a mistyped command removed too many servers and took down S3 storage | Amazon S3, 2017 (DAN-104) |
| a certificate expired and Firefox browser add-ons stopped working | Mozilla, 2019 (DAN-090) |
| lightning strikes hit the datacenter and caused power loss on the disks | Google, 2015 (DAN-071) |
| a deploy with different versions of the code caused a loss of 460 million dollars | Knight Capital, 2012 (DAN-084) |
| the Steam client deleted all files on the user's computer | Valve (DAN-236) |

### Resultado

```text
1. Contagem
   incidentes: 212
   chunks summary: 212
   chunks text: 2282
   chunks do arquivo de chunking: 2494 | fora do banco: 0

2. Integridade
   OK   vetores com outra dimensão: 0
   OK   vetores sem norma 1 (não normalizados): 0
   OK   chunks com texto vazio: 0
   OK   incidentes sem nenhum chunk: 0
   OK   incidentes sem chunk de summary: 0
   OK   tipos de chunk desconhecidos: 0
   OK   chunks com o mesmo vetor de outro chunk: 0
   tudo certo
```

**Busca: 6 de 6, todas em 1º lugar.**

A checagem de vetores repetidos achou, na primeira carga, 6 pares de chunks idênticos: texto repetido no corpus, não um erro da carga. Eram 5 pares no DAN-031 (a página de status do Google traz o relatório duas vezes) e 1 par entre DAN-031 e DAN-036 (o aviso padrão das páginas de status do Google, com o mesmo título genérico). As regras de chunks repetidos (E2.3), de plantilla do site e de títulos repetidos (E2.2) resolveram os dois casos.

## 2. Busca no pgvector

O script `search.py` recebe uma descrição em texto livre e mostra os 5 chunks mais parecidos:

```bash
python ./dataset_nela/danluu-ingestion/scripts/search.py "o banco de dados foi apagado por engano"
```

Para ver o texto de um chunk retornado:

```bash
docker exec incident-copilot-db psql -U copilot -d incident_copilot -c "SELECT content FROM chunk WHERE chunk_id = 'DAN-164-001';"
```

## 3. Medição da busca

As 6 buscas de teste mostram que a busca funciona, mas são poucas para medir uma mudança. Para isso há um conjunto de 295 perguntas em `dataset_nela/danluu-ingestion/evaluation/questions.json`, em português e inglês, cada uma com o incidente que deveria aparecer:

- **sintoma:** descreve só o que se vê durante o incidente ("os clientes recebem erro 502"), sem a causa;
- **causa:** descreve o que aconteceu;
- **geral:** perguntas livres;
- 5 perguntas não têm incidente parecido no corpus.

```bash
python ./dataset_nela/danluu-ingestion/scripts/evaluate.py
```

O script ordena os incidentes pela maior similaridade entre a pergunta e os seus chunks e anota a posição do incidente esperado. Ele lê os vetores de `data/embeddings/qwen3/` (não usa o banco) e grava a posição de cada pergunta em `evaluation/results.json`.

### Resultado

| Perguntas | Quantidade | 1º lugar | Top 5 | MRR |
|---|---|---|---|---|
| **Todas** | 290 | **80%** | **94%** | 0,86 |
| Sintoma | 137 | 74% | 91% | 0,81 |
| Causa | 137 | 83% | 96% | 0,89 |
| Geral | 16 | 94% | 100% | 0,96 |
| Português | 126 | 79% | 95% | 0,86 |
| Inglês | 164 | 80% | 93% | 0,86 |

- **1º lugar:** o incidente esperado veio em primeiro. **Top 5:** ele ficou entre os 5 primeiros, que são os que o agente recebe. **MRR:** média de 1/posição.
- Em 8 de cada 10 perguntas o incidente certo vem em primeiro, e em mais de 9 de cada 10 ele está entre os 5 primeiros.
- As perguntas de sintoma são as mais difíceis, e as perguntas em português funcionam tão bem quanto as em inglês, embora os documentos estejam em inglês.
- **"Não achei":** nas 5 perguntas sem incidente parecido, a maior similaridade ficou entre 0,456 e 0,652; nas perguntas com resposta, a mediana é 0,739 e 10% ficam abaixo de 0,638. Os valores se misturam, então a similaridade sozinha não serve para o sistema dizer "não encontrei um incidente parecido".

Para medir uma mudança no chunking, na limpeza ou no modelo: rodar o script antes e depois e comparar os números. Com 290 perguntas, diferenças de 2 a 4 pontos estão dentro do ruído.
