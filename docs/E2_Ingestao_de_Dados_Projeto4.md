# E2 — Infraestrutura de Dados e Ingestão

Este documento mostra o que foi entregue na E2, onde está a evidência de cada entrega e por que cada
decisão foi tomada. Os detalhes técnicos de cada etapa estão em [`ingestion/README.md`](../ingestion/README.md).

**Resumo:** um comando leva os 240 postmortems do catálogo do danluu do dado bruto até o PostgreSQL +
pgvector. Ficam 211 documentos e 2.885 chunks com vetores de 1024 dimensões. Ao final, o próprio pipeline
valida a carga e faz perguntas de teste no banco. Tempo total: ~1 minuto com GPU, ~2,5 minutos sem GPU.

## 1. Entregas e evidências

| Entrega | O que foi feito | Evidência |
|---|---|---|
| **2.1** Ambiente | virtualenv `multiagent_env` (Python 3.12) com LangGraph, FastAPI, pgvector, psycopg e sentence-transformers; PostgreSQL 17 + pgvector 0.8.0 no Docker | `requirements.txt`, `ingestion/banco/docker-compose.yml` |
| **2.2** Pipeline de ingestão | 8 etapas: inventário → reextração → fichas → corpus → chunks → embeddings → banco → validação | `ingestion/pipeline.py` |
| **2.3** Chunking | dois tipos de chunk: por assunto da ficha (busca) e por seção do texto (detalhe) | seção 3 abaixo; etapa 5 do pipeline |
| **2.4** Embeddings + metadados | Qwen3-Embedding-0.6B; tabelas `documents` e `chunks` com fonte, tipo, data e tags | `ingestion/banco/schema.sql` |
| **2.5** Validação | contagens, 7 checagens de integridade, amostra de vetores, 4 perguntas de teste e resumo da avaliação | `ingestion/banco/validacao_ingestao.md` (gerado a cada execução) |

## 2. Os dados

**Só o `danluu-ingestion` entra no RAG.** Os outros 8 datasets foram avaliados um a um. Cada pasta em
`datasets/` tem um README com o veredito:

| Dataset | Veredito |
|---|---|
| `incident-postmortem-assistant` | não indexado: são reescritas feitas por LLM (o Claude, segundo a decisão ADR-010 do próprio repositório), 13 delas de incidentes que já temos no original pelo danluu, e com fonte incompleta. **As perguntas de avaliação dele foram reaproveitadas** (suíte IPA). |
| `incidentdb-statuspage` | não usado agora: os campos de causa e correção são gerados por template no crawler, iguais para todos os registros |
| `agent-postmortems` | fora do escopo: são falhas de agentes de IA, não de infraestrutura |
| `postmortem-intelligence` | descartado: registros fictícios, como o próprio repositório declara |
| `postmortem-templates` | não é dataset: só modelos vazios de postmortem |
| `opentelemetry-demo-dataset`, `otel-demo-generator`, `otel-incident-lab` | não são datasets: geradores ou laboratórios de telemetria, sem incidentes gravados |

A coluna `dataset` já existe nas tabelas, para receber outra base sem mudar o banco.

**Qualidade do danluu:** dos 240 links, o inventário marcou 44 que precisavam de reextração e 27
inutilizáveis (página fora do ar, vazia ou sem o postmortem). A reextração refez o texto de 49 documentos a
partir do HTML salvo, com regras para cada formato de página (blog, Statuspage, painel do Google Cloud,
Reddit antigo, Google Groups). Em 7 deles, a extração original tinha pegado outra coisa no lugar do artigo.

## 3. Decisões e justificativas

### Fichas: um resumo estruturado de cada incidente
Cada documento ganhou uma **ficha** em JSON com resumo, detecção, causa, mitigação e prevenção. **Cada
afirmação da ficha cita trechos literais do texto**, e um validador confere que esses trechos existem.
As fichas foram extraídas por LLM em lotes de 10 e conferidas por um segundo modelo (GPT). Os erros que se
repetiam viraram regras novas no prompt, que hoje está na versão 2.21.

*Por quê:* os postmortems são longos e cheios de ruído (linha do tempo minuto a minuto, rodapé de
marketing, comentários de leitores). A ficha diz em poucas linhas o que aconteceu e por quê. Ela é a
parte que mais se parece com a pergunta de quem está no meio de um incidente. Os trechos literais
garantem que o copiloto possa citar a fonte em vez de inventar.

### Busca em duas etapas
1. **Etapa 1:** a pergunta é comparada com os chunks das fichas, e os documentos são ranqueados pelo
   chunk mais parecido. Assim se acham os **incidentes parecidos**.
2. **Etapa 2:** dentro desses documentos, a pergunta é comparada com os chunks do texto completo. Assim
   se trazem os **detalhes e a evidência**.

*Por quê:* medido nas 278 perguntas de avaliação. Ranquear pelas fichas acerta o documento em 1º lugar
mais vezes do que ranquear pelo texto completo:

| Índice usado para ranquear (Qwen3) | 1º lugar | entre os 5 primeiros |
|---|---|---|
| **só fichas** | **72%** | 88% |
| só texto completo | 61% | 85% |
| fichas + texto juntos | 69% | 91% |

Nas perguntas de sintoma em português, que são o caso real de uso, a diferença no 1º lugar é de 67%
contra 47%.

### Chunking (entrega 2.3)
**Chunks de ficha (867):** um chunk por assunto: resumo com detecção, causa, mitigação e prevenção. A
causa é dividida em duas quando passa do limite (44 casos). Os trechos de evidência ficam guardados ao lado
do chunk, fora do vetor.
- *Por quê por assunto:* uma pergunta sobre a causa deve casar com o trecho que fala da causa, e não com
  uma média de tudo.
- *Por quê a evidência fora do vetor:* as citações são texto bruto em inglês, cheio de detalhes. Dentro do
  vetor, elas diluiriam o significado. Fora dele, ficam prontas para o agente mostrar.

**Chunks de texto (2.018):** por seção, usando os intertítulos do documento. Seções curtas (menos de
100 tokens) se juntam à seguinte. Seções longas se dividem entre parágrafos, nunca no meio de um.
- *Por quê por seção:* um postmortem já é organizado em partes com sentido ("What happened", "Root
  cause", "Remediation"). Cortar por tamanho fixo partiria essas ideias ao meio.

**Limite de 450 tokens**, contados com o tokenizador real (o do multilingual-e5-base, que entrou na
comparação de modelos).
- *Por quê:* o e5 lê no máximo 512 tokens. Com 450 de limite, sobra margem para o cabeçalho, e **os três
  modelos comparados liam cada chunk inteiro**, o que deixou a comparação justa. Na prática, a mediana dos
  chunks de texto é 318 tokens, e nenhum passou do limite.

**Sem sobreposição**, exceto quando um parágrafo sozinho passa do limite. Nesse caso, ele é dividido entre
frases, com uma frase repetida entre as partes.
- *Por quê:* como o corte cai sempre num ponto natural (intertítulo ou fim de parágrafo), não há frase
  cortada a recuperar. Sobreposição só duplicaria texto no índice.

**Cabeçalho no vetor:** cada chunk vira vetor com "empresa — título — assunto ou seção" na frente, e o
texto passa por uma normalização: tabelas, links e HTML simplificados. O texto original fica guardado sem
alteração, para ser mostrado ao usuário.
- *Por quê:* um trecho solto como "we rolled back the change" não diz de qual incidente é. O cabeçalho
  dá esse contexto ao vetor.

### Modelo de embedding: Qwen3-Embedding-0.6B
Comparamos três modelos gratuitos que rodam localmente, com as mesmas 278 perguntas, ranqueando pelas
fichas:

| Modelo | Licença | 1º lugar (todas) | sintoma em português: 1º lugar / top-5 |
|---|---|---|---|
| multilingual-e5-base | MIT | 49% | 28% / 48% |
| bge-m3 | MIT | 63% | 58% / 75% |
| **Qwen3-Embedding-0.6B** | Apache 2.0 | **72%** | **67% / 83%** |

*Por quê:*
- foi o melhor em todos os recortes;
- os documentos estão em inglês e as perguntas podem vir em português, e o e5 vai mal nessa mistura;
- roda localmente (1,6 GB de memória de vídeo, ou só processador), sem custo e sem mandar dados para fora.

### Banco: PostgreSQL + pgvector no Docker
- **Docker:** é o recomendado na entrega, e quem clona o repositório sobe o mesmo banco com um comando.
  Ele escuta só em `127.0.0.1:5433`, e a senha fica num `.env` fora do git.
- **Busca exata, sem índice vetorial (HNSW/IVFFlat):** com 2.885 chunks, a busca exata leva ~13 ms e
  sempre acha o mais parecido. Um índice aproximado só compensa com centenas de milhares de vetores, e
  troca precisão por velocidade.
- **Metadados (entrega 2.4)** ficam na tabela `documents`, e cada chunk aponta para o seu documento:

| Pedido na entrega | Coluna |
|---|---|
| fonte | `url`, `dataset`, `company`, `text_source` (texto original ou reextraído) |
| tipo | `tipo_documento`; no chunk, `tipo` (ficha/texto) e `assunto` |
| data | `incident_date` |
| tags | `categoria_causa`, `dominio`, `seguranca` |

### Reprodutibilidade
- **Repetível:** rodar o pipeline de novo produz os mesmos arquivos. A carga substitui o dataset em vez de
  duplicar, e nenhum script altera os dados brutos.
- **Com ou sem GPU:** o código usa a GPU se houver, e senão o processador.
- **Vetores no git:** os vetores do Qwen3 estão versionados. O pipeline só gera de novo se os chunks
  mudarem; no processador, isso levaria ~2 h.

## 4. Roteiro da demonstração (~5 minutos)

Antes de começar: abrir o Docker Desktop, abrir o terminal na raiz do repositório e ativar o ambiente
(`source multiagent_env/bin/activate`).

**1. Ambiente (2.1)**
```bash
docker ps --filter name=e2-pgvector-andre
pip list | grep -iE "langgraph|fastapi|pgvector|psycopg|sentence-transformers"
```
Mostrar: o container saudável e as bibliotecas instaladas.

**2. Pipeline completo (2.2, 2.3, 2.4, 2.5)**
```bash
python -I ingestion/pipeline.py --listar
python -I ingestion/pipeline.py
```
Apontar na tela:
- **etapa 2:** os 49 documentos reextraídos;
- **etapa 3:** 213 de 213 fichas válidas;
- **etapa 4:** a limpeza (comentários, parágrafos repetidos) e "trechos de fichas ausentes no corpus: 0";
- **etapa 5:** os chunks por assunto e por seção, com "acima do limite: 0";
- **etapa 6:** os vetores reaproveitados, porque os chunks não mudaram;
- **etapa 7:** 211 documentos e 2.885 chunks carregados;
- **etapa 8:** a integridade toda ✔, a amostra de vetores (1024 dimensões, norma 1) e as perguntas de
  teste com o incidente esperado no topo.

**3. Os dados no banco, com metadados (2.4)**
```bash
docker exec e2-pgvector-andre psql -U e2 -d incidentes -c "SELECT d.doc_id, d.company, d.incident_date, d.tipo_documento, d.categoria_causa, c.tipo, c.assunto, c.tokens, vector_dims(c.embedding) AS dims FROM chunks c JOIN documents d USING (doc_id) WHERE c.doc_id = 'danluu:DAN-189' ORDER BY c.tipo, c.chunk_id;"
```
Mostrar: um incidente com seus 4 chunks de ficha e 5 de texto, todos com vetor de 1024 dimensões e com os
metadados do documento.

**4. Query de teste ao vivo (2.5)**
```bash
python -I ingestion/banco/busca.py "depois de uma mudança de BGP, nossos datacenters sumiram da internet"
python -I ingestion/banco/busca.py "uma expressão regular passou a consumir 100% da CPU em todos os servidores"
```
Resultado esperado: o Facebook (outubro de 2021) e o Stack Exchange (julho de 2016) em 1º lugar.
Mostrar, para cada incidente achado:
- o chunk da ficha que casou;
- o trecho literal de evidência;
- os trechos do texto completo trazidos pela etapa 2.

Se sobrar tempo, peça uma pergunta para a plateia. Lembre que as perguntas de sintoma em português acertam o 1º lugar em 67% dos casos: se o incidente certo vier em 2º ou 3º, isso é esperado.

## 5. Perguntas prováveis

**Por que só um dataset?** Ver a seção 2: os outros são reescritas por LLM, registros fictícios, campos
gerados por template ou não contêm incidentes. Preferimos menos dados com fonte verificável, porque o
copiloto precisa citar a origem.

**As fichas foram geradas por LLM. Como sabem que estão certas?**
- cada afirmação tem trecho literal do texto, e o validador confere que o trecho existe (213 de 213 ok);
- um segundo modelo conferiu as fichas;
- cada crítica dele foi checada contra o texto antes de corrigir.

**Vocês descartaram o `incident-postmortem-assistant` por ser reescrito por LLM, mas as fichas também
foram feitas por LLM. Qual a diferença?**

O autor do repositório registra o processo na decisão ADR-010 do próprio projeto: o Claude baixava o
postmortem original e o reescrevia num formato fixo. Na conferência, achamos um resumo da Cloudflare citando
Spotify, ChatGPT, X e Canva fora do ar, o que não está no postmortem original. A diferença está no que fica
no banco e em como cada afirmação é checada:

| | `incident-postmortem-assistant` | nossas fichas |
|---|---|---|
| o que fica no banco | só a reescrita (o original não está no repositório) | **o texto original** do postmortem, que é o que a etapa 2 busca |
| como conferir uma afirmação | não dá: a reescrita não aponta o trecho de onde veio | cada afirmação cita um **trecho literal** do original, e um script confere que ele existe (213 de 213 ok) |
| link da fonte | fora do documento; ausente em 5 de 20 e errado em 1 | `url` em todo documento |
| papel do texto gerado | é o conteúdo | é um índice para achar o incidente; a evidência mostrada é sempre o texto original |

**Por que 450 tokens e não 512, 800 ou 1000?** Para os três modelos comparados lerem cada chunk inteiro (o
e5 lê no máximo 512). Com o Qwen3, que lê mais, daria para aumentar. Mas a mediana das seções já fica
abaixo disso, então pouca coisa mudaria.

**Como a qualidade da busca foi medida?**
- 278 perguntas com o documento certo conhecido: 38 da suíte do `incident-postmortem-assistant` e 240
  próprias;
- metade descreve o sintoma ("o que está acontecendo") e metade a causa;
- há perguntas em português e em inglês.

**Quais as limitações conhecidas?**
- **"Não achei":** a similaridade sozinha não separa bem a pergunta sem incidente parecido da pergunta com
  resposta. O agente vai precisar de outra regra para dizer "não achei".
- **Viés possível:** as perguntas próprias e as fichas foram escritas por modelos de linguagem, o que pode
  favorecer o índice de fichas. Perguntas escritas por pessoas são o próximo passo.
- **Etapa 2 não medida:** a escolha dos trechos do texto completo ainda não tem métrica própria.

**Precisa de GPU?** Não. Sem GPU, cada pergunta leva ~1 s a mais e o pipeline completo leva ~2,5 min, porque
os vetores já vêm prontos no git.
