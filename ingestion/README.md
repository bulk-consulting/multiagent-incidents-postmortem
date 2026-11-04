# Ingestão de dados — E2 (danluu)

Pipeline que leva os postmortems do catálogo do danluu do dado bruto até o PostgreSQL + pgvector,
pronto para a busca do agente. Um comando roda tudo, do inventário à query de teste no banco.

```text
datasets/danluu-ingestion/data/            (bruto: catálogo, HTML e texto extraído — só leitura)
        │
        ├─ 1 inventario ──── classifica a qualidade de cada documento (240)
        ├─ 2 reextracao ──── refaz o texto dos 49 documentos que a extração original estragou
        │
        │   fichas/saida/    213 fichas (resumo, causa, detecção, mitigação, prevenção, com trechos
        │                    literais), produzidas no processo curado descrito abaixo
        ├─ 3 fichas ──────── valida as fichas (schema e trechos que existem no texto)
        │
        ├─ 4 corpus ──────── 211 documentos: texto escolhido (reextraído ou original) e limpo
        ├─ 5 chunks ──────── 867 chunks de ficha (etapa 1 da busca) + 2.018 de texto (etapa 2)
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

**Para a apresentação:** `--desde banco` (~1 minuto) mostra a carga no banco e a validação com as
perguntas de teste; o pipeline completo mostra todas as etapas rodando. Uma pergunta avulsa:

```bash
multiagent_env/bin/python -I ingestion/banco/busca.py "usuários estão vendo dados de outros usuários"
```

## Etapas

| # | Etapa | Script | Lê | Grava |
|---|---|---|---|---|
| 1 | inventario | `triagem/01_inventario.py` | catálogo e HTML do danluu | `triagem/saida/inventario.csv` |
| 2 | reextracao | `reextracao/reextrair.py` | HTML salvo do danluu e `reextracao/baixados/` | `reextracao/extraidos/`, `checagem.csv` |
| 3 | fichas | `fichas/validar_fichas.py` | `fichas/saida/DAN-*.json` | `fichas/saida/validacao.csv` |
| 4 | corpus | `corpus/montar_corpus.py` | texto (reextraído ou original) e fichas | `corpus/corpus.jsonl`, `limpeza.csv` |
| 5 | chunks | `corpus/chunk_fichas.py`, `corpus/chunk_texto.py` | `corpus.jsonl` e fichas | `corpus/chunks_fichas.jsonl`, `chunks_texto.jsonl` |
| 6 | embeddings | `corpus/gerar_embeddings.py qwen3` | chunks | `corpus/embeddings/qwen3/` (no git; pulada se os vetores batem com os chunks) |
| 7 | banco | `banco/carregar.py` | corpus, fichas, chunks e vetores | tabelas `documents`, `chunks`, `cargas` |
| 8 | validacao | `banco/validar_ingestao.py` | banco | `banco/validacao_ingestao.md` |

Todas as etapas são repetíveis: rodar de novo produz os mesmos arquivos, e a carga no banco
substitui o dataset em vez de duplicar. Nenhum script altera nada em `datasets/`.

## O que não é automático (processo curado)

**Fichas.** Uma ficha por documento, em JSON, com cada afirmação provada por trechos literais do
texto. Foram feitas em lotes de 10, ao longo de vários dias:

1. `fichas/montar_prompts.py` monta o prompt de cada documento (`fichas/prompt_extracao.md`, hoje na v2.21);
2. uma sessão nova do Claude Code extrai as fichas às cegas e faz a autorrevisão (`fichas/autorrevisao.md`);
3. `fichas/validar_fichas.py` confere o schema e se todo trecho existe no texto;
4. `fichas/montar_revisao.py` gera os pacotes que o GPT confere (todas as fichas nos primeiros lotes, depois uma amostra);
5. cada crítica do GPT é verificada contra o texto e as regras antes de corrigir; erros que se repetem viram nova versão do prompt.

Histórico, regras e taxas de erro por lote: `fichas/FICHA.md` e `fichas/PLANO_LOTES.md`.

**Reextração.** As regras do `reextrair.py` foram ajustadas à mão para cada formato de página
(blog, Statuspage, painel do Google Cloud, Reddit antigo, Google Groups). As 6 páginas que precisaram
de download novo vieram da Wayback Machine e estão salvas em `reextracao/baixados/` (origem e sha256 em
`manifesto.csv`). Cortes de comentários de leitores e títulos corrigidos ficam em tabelas manuais no
`corpus/montar_corpus.py`.

## Decisões principais

- **Busca em duas etapas.** Etapa 1: a pergunta é comparada com os chunks das fichas para achar
  incidentes parecidos. Etapa 2: nos documentos achados, é comparada com os chunks do texto completo
  para trazer detalhes e evidência. Na avaliação, as fichas ranqueiam melhor que o texto completo.
- **Chunks das fichas:** um por assunto (resumo com detecção, causa, mitigação, prevenção), com os
  trechos de evidência guardados ao lado e fora do vetor.
- **Chunks do texto:** por seção (intertítulos) e, sem intertítulos, por parágrafos; seções curtas se
  juntam e longas se dividem entre parágrafos; até 450 tokens reais, sem sobreposição (o corte cai
  sempre num ponto natural).
- **Modelo de embedding:** Qwen3-Embedding-0.6B (Apache 2.0, local). Venceu multilingual-e5-base e
  bge-m3 na avaliação: com perguntas de sintoma em português, o incidente certo vem em 1º em 67% dos
  casos e entre os 5 primeiros em 83%. Detalhes em `avaliacao/RESULTADOS.md`.
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
| `avaliacao/` | suítes de perguntas (IPA adaptada e própria), avaliador e resultados |
