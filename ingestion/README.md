# Ingestão de dados — E2 (danluu)

Pipeline que leva os postmortems do catálogo do danluu do dado bruto até o PostgreSQL + pgvector,
pronto para a busca do agente. Um comando roda tudo, do inventário à query de teste no banco.

```text
datasets/danluu-ingestion/data/            (bruto: catálogo, HTML e texto extraído — só leitura)
        │
        ├─ 1 inventario ──── classifica a qualidade de cada documento (240)
        ├─ 2 reextracao ──── refaz o texto dos 50 documentos que a extração original estragou ou não baixou
        │
        │   fichas/saida/    213 fichas (opcionais: enriquecimento para os agentes), produzidas no
        │                    processo curado descrito abaixo; não entram na busca
        ├─ 3 fichas ──────── valida as fichas, se houver (schema e trechos que existem no texto)
        │
        ├─ 4 corpus ──────── 212 documentos: texto escolhido (reextraído ou original), limpo, + resumo do danluu
        ├─ 5 chunks ──────── 212 de resumo + 2.024 de texto (busca) + 867 de ficha (opcionais)
        ├─ 6 embeddings ──── vetores de 1024 dimensões com Qwen3-Embedding-0.6B
        ├─ 7 banco ───────── carrega no PostgreSQL + pgvector (Docker)
        └─ 8 validacao ───── contagens, integridade e perguntas de teste no banco
```

## Como rodar

**Primeira vez** (a partir da raiz do repositório):

```bash
python3 -m venv multiagent_env
multiagent_env/bin/pip install -r requirements.txt   # sem GPU NVIDIA: veja o comentário no arquivo
```

O Docker Desktop precisa estar aberto, com a integração com o WSL ligada (Settings → Resources →
WSL Integration). O pipeline cria o `ingestion/banco/.env` com uma senha aleatória e sobe o container
sozinho.

**Pipeline completo** (~1,5 minuto com GPU, ~2,5 minutos sem GPU):

```bash
multiagent_env/bin/python -I ingestion/pipeline.py
multiagent_env/bin/python -I ingestion/pipeline.py --listar          # etapas
multiagent_env/bin/python -I ingestion/pipeline.py --desde chunks    # da etapa 'chunks' em diante
multiagent_env/bin/python -I ingestion/pipeline.py --so validacao    # só a validação
multiagent_env/bin/python -I ingestion/pipeline.py --forcar-embeddings   # gera os vetores de novo
```

**GPU ou processador.** Tudo funciona nos dois: o código usa a GPU NVIDIA se houver e o processador
se não houver. A única etapa pesada é gerar os vetores (~3,5 min na GPU, ~2 h no processador), e ela
só roda quando os chunks mudam: os vetores do Qwen3 estão no git, e o pipeline confere se eles batem
com os chunks atuais antes de gerar de novo. Sem GPU, cada pergunta leva ~1 s a mais para virar vetor.

**Para a apresentação:** roteiro em `docs/E2_Ingestao_de_Dados_Projeto4.md`. Uma pergunta avulsa:

```bash
multiagent_env/bin/python -I ingestion/banco/busca.py "depois de uma mudança de BGP, nossos datacenters sumiram da internet"
```

## Etapas

| # | Etapa | Script | Lê | Grava |
|---|---|---|---|---|
| 1 | inventario | `triagem/01_inventario.py` | catálogo e HTML do danluu | `triagem/saida/inventario.csv` |
| 2 | reextracao | `reextracao/reextrair.py` | HTML salvo do danluu e `reextracao/baixados/` | `reextracao/extraidos/`, `checagem.csv` |
| 3 | fichas | `fichas/validar_fichas.py` | `fichas/saida/DAN-*.json` | `fichas/saida/validacao.csv` |
| 4 | corpus | `corpus/montar_corpus.py` | texto (reextraído ou original), catálogo (resumo) e fichas, se houver | `corpus/corpus.jsonl`, `limpeza.csv` |
| 5 | chunks | `corpus/chunk_resumo.py`, `corpus/chunk_texto.py`, `corpus/chunk_fichas.py` | `corpus.jsonl` (e fichas, se houver) | `corpus/chunks_resumo.jsonl`, `chunks_texto.jsonl`, `chunks_fichas.jsonl` |
| 6 | embeddings | `corpus/gerar_embeddings.py qwen3` | chunks | `corpus/embeddings/qwen3/` (no git; pulada se os vetores batem com os chunks) |
| 7 | banco | `banco/carregar.py` | corpus, fichas (se houver), chunks e vetores | tabelas `documents`, `chunks`, `cargas` |
| 8 | validacao | `banco/validar_ingestao.py` | banco | `banco/validacao_ingestao.md` |

Todas as etapas são repetíveis: rodar de novo produz os mesmos arquivos, e a carga no banco
substitui o dataset em vez de duplicar. Nenhum script altera nada em `datasets/`.

## O que não é automático (processo curado)

**Fichas (opcionais).** Uma ficha por documento, em JSON, com cada afirmação provada por trechos literais do
texto. Não entram na busca desde que a etapa 1 passou a usar o resumo do danluu (mesmo resultado, sem
precisar de ficha para cada incidente novo); ficam como enriquecimento para os agentes. Sem fichas, o
pipeline pula a etapa 3 e os chunks de ficha. Foram feitas em lotes de 10, ao longo de vários dias:

1. `fichas/montar_prompts.py` monta o prompt de cada documento (`fichas/prompt_extracao.md`, hoje na v2.21);
2. uma sessão nova do Claude Code extrai as fichas às cegas e faz a autorrevisão (`fichas/autorrevisao.md`);
3. `fichas/validar_fichas.py` confere o schema e se todo trecho existe no texto;
4. `fichas/montar_revisao.py` gera os pacotes que o GPT confere (todas as fichas nos primeiros lotes, depois uma amostra);
5. cada crítica do GPT é verificada contra o texto e as regras antes de corrigir; erros que se repetem viram nova versão do prompt.

Histórico, regras e taxas de erro por lote: `fichas/FICHA.md` e `fichas/PLANO_LOTES.md`.

**Reextração.** As regras do `reextrair.py` foram ajustadas à mão para cada formato de página
(blog, Statuspage, painel do Google Cloud, Reddit antigo, Google Groups). As páginas que precisaram
de download novo estão salvas em `reextracao/baixados/` (origem e sha256 em `manifesto.csv`): 6 da
Wayback Machine e o DAN-084 (Knight Capital), da coleta da Mari, porque na coleta original o site devolveu 403. Cortes de comentários de leitores e títulos corrigidos ficam em tabelas manuais no
`corpus/montar_corpus.py`.

## Decisões principais

- **Busca em duas etapas.** Etapa 1: a pergunta é comparada com o chunk de resumo de cada incidente
  (resumo do catálogo do danluu, escrito por pessoas) e com os chunks do texto completo; cada documento
  vale o seu melhor chunk. Etapa 2: nos 5 documentos achados, é comparada com os chunks do texto completo
  para trazer detalhes e evidência literal. Na avaliação: 73% em 1º lugar e 92% entre os 5 primeiros,
  contra 72% / 88% com as fichas (detalhes em `avaliacao/RESULTADOS.md`).
- **Chunk de resumo:** um por incidente, "empresa — título" + resumo, sem divisão.
- **Chunks do texto:** por seção (intertítulos) e, sem intertítulos, por parágrafos; seções curtas se
  juntam e longas se dividem entre parágrafos; até 450 tokens reais, sem sobreposição (o corte cai
  sempre num ponto natural, e ~60 tokens de sobreposição foram testados sem ganho).
- **Chunks das fichas (opcionais):** um por assunto (resumo com detecção, causa, mitigação, prevenção),
  com os trechos de evidência guardados ao lado e fora do vetor; não entram na busca.
- **Modelo de embedding:** Qwen3-Embedding-0.6B (Apache 2.0, local). Venceu multilingual-e5-base e
  bge-m3 na avaliação (as três com o mesmo índice), principalmente nas perguntas de sintoma em português.
  Detalhes em `avaliacao/RESULTADOS.md`.
- **Banco:** PostgreSQL 17 + pgvector 0.8.0 em Docker, coluna `dataset` desde já (só `danluu` por
  enquanto), busca exata sem índice vetorial (alguns milhares de chunks, ~13 ms por consulta).

## Pastas

| Pasta | Conteúdo |
|---|---|
| `triagem/` | inventário e régua de qualidade dos documentos |
| `reextracao/` | reextração, lista dos documentos refeitos, downloads da Wayback |
| `fichas/` | prompt, schema, validador, lotes, fichas aceitas (`saida/`) |
| `corpus/` | corpus limpo, chunkers, normalização para o vetor, vetores |
| `banco/` | Docker, schema, carga, busca e validação |
| `avaliacao/` | suítes de perguntas (IPA adaptada, própria e as 6 da Mari), avaliador, teste de sobreposição e resultados |
