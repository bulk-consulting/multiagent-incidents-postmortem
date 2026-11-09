# E2 — Infraestrutura de Dados e Ingestão

Este documento mostra o que foi entregue na E2, onde está a evidência de cada entrega e por que cada
decisão foi tomada. Os detalhes técnicos de cada etapa estão em [`ingestion/README.md`](../ingestion/README.md).

**Resumo:** um comando leva os 240 postmortems do catálogo do danluu do dado bruto até o PostgreSQL +
pgvector. Ficam 212 documentos e 2.236 chunks de busca (212 de resumo + 2.024 de texto) com vetores de 1024
dimensões, mais 867 chunks de ficha opcionais. Ao final, o próprio pipeline valida a carga e faz perguntas
de teste no banco. Tempo total: ~1 minuto com GPU, ~2,5 minutos sem GPU (os vetores vêm prontos no git).

## 1. Entregas e evidências

| Entrega | O que foi feito | Evidência |
|---|---|---|
| **2.1** Ambiente | virtualenv `multiagent_env` (Python 3.12) com LangGraph, FastAPI, pgvector, psycopg e sentence-transformers; PostgreSQL 17 + pgvector 0.8.0 no Docker | `requirements.txt`, `ingestion/banco/docker-compose.yml` |
| **2.2** Pipeline de ingestão | 8 etapas: inventário → reextração → fichas (opcional) → corpus → chunks → embeddings → banco → validação | `ingestion/pipeline.py` |
| **2.3** Chunking | um chunk de resumo por incidente (resumo do danluu) e chunks do texto por seção, sem sobreposição | seção 3 abaixo; etapa 5 do pipeline |
| **2.4** Embeddings + metadados | Qwen3-Embedding-0.6B; tabelas `documents` e `chunks` com fonte, tipo, data e tags | `ingestion/banco/schema.sql` |
| **2.5** Validação | contagens, 8 checagens de integridade, amostra de vetores, 4 perguntas de teste e resumo da avaliação | `ingestion/banco/validacao_ingestao.md` (gerado a cada execução) |

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
O Knight Capital (DAN-084), que a coleta original não conseguiu baixar (o site devolveu 403), entrou com o
HTML da coleta da Mari, passado pela mesma reextração.

## 3. Decisões e justificativas

### Busca em duas etapas
1. **Etapa 1:** a pergunta é comparada com o **chunk de resumo** de cada incidente e com os **chunks do
   texto completo**. Cada documento recebe a nota do seu chunk mais parecido, e os 5 melhores são os
   **incidentes parecidos**.
2. **Etapa 2:** dentro desses 5 documentos, a pergunta é comparada com os chunks do texto completo. Assim
   se trazem os **detalhes e a evidência**, sempre em texto literal do postmortem.

O **resumo** é o do próprio catálogo do danluu: uma a três frases escritas por pessoas para cada
incidente ("An operator used a tool with lax input validation to reboot a small number of servers…").

*Por quê:* medido nas 278 perguntas de avaliação, com o Qwen3:

| Índice usado na etapa 1 | 1º lugar | entre os 5 primeiros | sintoma em português (1º / top-5) | suíte do IPA (1º / top-5) |
|---|---|---|---|---|
| **resumo + texto (o usado)** | **73%** | **92%** | 62% / **92%** | 50% / 82% |
| fichas (a versão anterior) | 72% | 88% | **67%** / 83% | **61%** / 84% |
| só o resumo | 68% | 92% | 58% / 92% | 39% / 79% |
| só o texto completo | 61% | 85% | 45% / 80% | 47% / 79% |

> **Como ler as porcentagens (aqui e na tabela dos modelos):** para cada uma das 278 perguntas de teste,
> sabemos qual documento é a resposta certa. A busca ordena os documentos do mais parecido para o menos
> parecido, e anotamos em que posição o certo apareceu.
> - **1º lugar** é a fração das perguntas em que o documento certo veio em primeiro: 73% são ~200 das 278
>   perguntas.
> - **Entre os 5 primeiros** é a fração em que ele apareceu em qualquer posição do 1º ao 5º. Importa porque
>   o agente recebe os 5 primeiros incidentes, e não só o primeiro.
>
> Em resumo: a resposta certa vem em primeiro em 7 de cada 10 perguntas e está entre os 5 primeiros em 9
> de cada 10. Diferenças de 2 a 4 pontos estão dentro do ruído com 278 perguntas.

**Por que o resumo e não as fichas.** Até a versão anterior, a etapa 1 usava **fichas**: um resumo
estruturado de cada incidente (causa, mitigação, prevenção) extraído por LLM, com trechos literais
conferidos por um validador. As fichas funcionam bem, mas **cada incidente novo precisaria de uma ficha**,
e fazê-las exigiu um processo curado de vários dias (prompt na versão 2.21, conferência por um segundo
modelo). O resumo do danluu dá o mesmo resultado no geral (73% contra 72% em 1º lugar) e é melhor entre os
5 primeiros (92% contra 88%), sem LLM nenhum.

O custo da troca aparece no 1º lugar de dois recortes: as perguntas de sintoma em português (62% contra 67%)
e a suíte do IPA (50% contra 61%; são 38 perguntas, então 11 pontos são 4 perguntas). Entre os 5
primeiros, a diferença diminui ou se inverte: 92% contra 83% no português e 82% contra 84% no IPA (uma
pergunta). Como o agente recebe os 5, a troca compensa.

**As fichas continuam no banco**, como enriquecimento opcional para os agentes: as 213 já feitas trazem
causa, mitigação e prevenção separadas, com evidência. Elas só saíram do caminho obrigatório da ingestão.

**Incidentes novos**, que não estão no catálogo do danluu, vão precisar de um resumo. A ideia é gerá-lo
com um LLM (duas ou três frases no estilo do danluu, marcadas como `gerado` na coluna `resumo_origem`), o
que é bem mais simples que uma ficha. Sem resumo, o incidente ainda é achado pelos chunks de texto.

### Chunking (entrega 2.3)
**Chunk de resumo (212, um por incidente):** "empresa — título" + o resumo do danluu, sem os links. Não é
dividido: o maior tem 216 tokens.
- *Por quê:* o resumo descreve o incidente inteiro em poucas frases, que é o que mais se parece com a
  pergunta de quem está no meio de um incidente. Sozinho, ele já põe o certo entre os 5 primeiros em 92%
  das perguntas.

**Chunks de texto (2.024):** por seção, usando os intertítulos do documento. Seções curtas (menos de
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
  cortada a recuperar. E foi medido: três variantes com ~60 tokens de sobreposição deram praticamente o
  mesmo resultado na busca usada (resumo + texto: 73–76% em 1º lugar e 91–92% entre os 5 primeiros,
  contra 73% / 92% sem sobreposição), e criam até 12% mais chunks. Sobreposição ajudou um pouco mais
  quando o texto é buscado sozinho, sem o resumo (61% → 65% em 1º lugar).
  Detalhes em `ingestion/avaliacao/RESULTADOS.md`.

**Chunks de ficha (867, opcionais):** um por assunto (resumo com detecção, causa, mitigação, prevenção),
com os trechos de evidência guardados ao lado, fora do vetor. Não entram na busca; ficam para os agentes.

**Cabeçalho no vetor:** cada chunk vira vetor com "empresa — título — assunto ou seção" na frente, e o
texto passa por uma normalização: tabelas, links e HTML simplificados. O texto original fica guardado sem
alteração, para ser mostrado ao usuário.
- *Por quê:* um trecho solto como "we rolled back the change" não diz de qual incidente é. O cabeçalho
  dá esse contexto ao vetor.

### Modelo de embedding: Qwen3-Embedding-0.6B
Comparamos três modelos gratuitos que rodam localmente, com as mesmas 278 perguntas, ranqueando pelas
fichas (o índice da época; ranqueando só pelo texto, a ordem dos modelos é a mesma):

| Modelo | Licença | 1º lugar (todas) | sintoma em português: 1º lugar / top-5 |
|---|---|---|---|
| multilingual-e5-base | MIT | 49% | 28% / 48% |
| bge-m3 | MIT | 63% | 58% / 75% |
| **Qwen3-Embedding-0.6B** | Apache 2.0 | **72%** | **67% / 83%** |

"Sintoma em português" são as 60 perguntas mais próximas do uso real: alguém descrevendo em português o
que está acontecendo ("os certificados estão sendo rejeitados desde a meia-noite"), sem saber a causa,
enquanto os documentos estão em inglês. É onde os modelos mais se separam.

*Por quê:*
- foi o melhor em todos os recortes;
- os documentos estão em inglês e as perguntas podem vir em português, e o e5 vai mal nessa mistura;
- roda localmente (1,6 GB de memória de vídeo, ou só processador), sem custo e sem mandar dados para fora.

### Banco: PostgreSQL + pgvector no Docker
- **Docker:** é o recomendado na entrega, e quem clona o repositório sobe o mesmo banco com um comando.
  Ele escuta só em `127.0.0.1:5433`, e a senha fica num `.env` fora do git.
- **Busca exata, sem índice vetorial (HNSW/IVFFlat):** com ~3.100 chunks, a busca exata leva ~13 ms e
  sempre acha o mais parecido. Um índice aproximado só compensa com centenas de milhares de vetores, e
  troca precisão por velocidade.
- **Metadados (entrega 2.4)** ficam na tabela `documents`, e cada chunk aponta para o seu documento:

| Pedido na entrega | Coluna |
|---|---|
| fonte | `url`, `dataset`, `company`, `text_source` (texto original ou reextraído) |
| tipo | `tipo_documento`; no chunk, `tipo` (resumo/texto/ficha), `secao` e `assunto` |
| data | `incident_date` |
| tags | `categoria_causa`, `dominio`, `seguranca` (das fichas, quando houver) |
| resumo | `resumo` e `resumo_origem` (danluu ou gerado) |

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
- **etapa 3:** as fichas (opcionais) validadas, 213 de 213;
- **etapa 4:** 212 documentos, todos com resumo do danluu; a limpeza (comentários, parágrafos repetidos);
- **etapa 5:** 212 chunks de resumo e 2.024 de texto, com "acima do limite: 0";
- **etapa 6:** os vetores reaproveitados, porque os chunks não mudaram;
- **etapa 7:** 212 documentos e 3.103 chunks carregados (resumo, texto e ficha);
- **etapa 8:** a integridade toda ✔, a amostra de vetores (1024 dimensões, norma 1) e as perguntas de
  teste (3 de 4 com o incidente esperado no top-3; a 4ª é a do Cloudflare de 2023, que vem em 8º:
  é uma limitação real, ver a seção 5).

**3. Os dados no banco, com metadados (2.4)**
```bash
docker exec e2-pgvector-andre psql -U e2 -d incidentes -c "SELECT d.doc_id, d.company, d.incident_date, d.resumo_origem, c.tipo, c.secao, c.tokens, vector_dims(c.embedding) AS dims FROM chunks c JOIN documents d USING (doc_id) WHERE c.doc_id = 'danluu:DAN-189' ORDER BY c.tipo, c.chunk_id;"
```
Mostrar: um incidente com seu chunk de resumo, 5 de texto e 4 de ficha, todos com vetor de 1024 dimensões e
com os metadados do documento.

**4. Query de teste ao vivo (2.5)**
```bash
python -I ingestion/banco/busca.py "depois de uma mudança de BGP, nossos datacenters sumiram da internet"
python -I ingestion/banco/busca.py "uma expressão regular passou a consumir 100% da CPU em todos os servidores"
```
Resultado esperado:
- BGP: o Facebook (outubro de 2021) em 1º e, em 2º, o Cloudflare de junho de 2022, também de BGP;
- regex: o Cloudflare de julho de 2019 em 1º e o Stack Exchange de julho de 2016 em 3º. Os dois estão
  certos: nos dois casos, uma expressão regular travou a CPU dos servidores.

Mostrar, para cada incidente achado:
- o resumo do incidente e se ele foi achado pelo resumo ou por um trecho do texto;
- os trechos do texto completo trazidos pela etapa 2, que são a evidência literal.

Se sobrar tempo, peça uma pergunta para a plateia. As perguntas de sintoma em português põem o certo em 1º
em 62% dos casos e entre os 5 primeiros em 92%: se o incidente certo vier em 2º ou 3º, isso é esperado.

## 5. Perguntas prováveis

**Por que só um dataset?** Ver a seção 2: os outros são reescritas por LLM, registros fictícios, campos
gerados por template ou não contêm incidentes. Preferimos menos dados com fonte verificável, porque o
copiloto precisa citar a origem.

**Por que trocaram as fichas pelo resumo do danluu?** Ver "Por que o resumo e não as fichas" na seção 3:
o resultado da busca é equivalente (melhor entre os 5 primeiros, um pouco pior no 1º lugar em dois
recortes), e o resumo não exige LLM nem processo curado para cada incidente.

**E os incidentes novos, que não têm resumo do danluu?** Um LLM gera um resumo curto, marcado como
`gerado`. Sem resumo, o incidente ainda é achado pelo texto, com menos precisão (61% em 1º lugar contra
73%).

**Por que não usar sobreposição entre chunks, como é comum?** Foi medido: com o resumo junto, três
variantes com ~60 tokens de sobreposição ganharam de 1 a 3 pontos no 1º lugar, dentro do ruído, e nada
entre os 5 primeiros. Ver "Chunking" na seção 3.

**As fichas foram geradas por LLM. Como sabem que estão certas?**
- cada afirmação tem trecho literal do texto, e o validador confere que o trecho existe (213 de 213 ok);
- um segundo modelo conferiu as fichas;
- cada crítica dele foi checada contra o texto antes de corrigir.
Hoje elas não entram na busca; ficam como enriquecimento para os agentes.

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
| papel do texto gerado | é o conteúdo | enriquecimento opcional para os agentes; a busca usa o resumo do danluu e o texto original |

**Por que 450 tokens e não 512, 800 ou 1000?** Para os três modelos comparados lerem cada chunk inteiro (o
e5 lê no máximo 512). Com o Qwen3, que lê mais, daria para aumentar. Mas a mediana das seções já fica
abaixo disso, então pouca coisa mudaria.

**Como a qualidade da busca foi medida?**
- 278 perguntas com o documento certo conhecido: 38 da suíte do `incident-postmortem-assistant` e 240
  próprias;
- metade descreve o sintoma ("o que está acontecendo") e metade a causa;
- há perguntas em português e em inglês;
- à parte, as 6 perguntas de validação da Mari, escritas sem olhar as fichas, em português e em inglês:
  o certo vem entre os 5 primeiros em 12 de 12 e em 1º em 10 de 12.

**Quais as limitações conhecidas?**
- **"Não achei":** a similaridade sozinha não separa bem a pergunta sem incidente parecido da pergunta com
  resposta. O agente vai precisar de outra regra para dizer "não achei".
- **Viés possível:** as perguntas próprias foram escritas por modelos de linguagem, a partir das fichas.
  A suíte do IPA e as perguntas da Mari são independentes, mas são poucas (38 e 12). Mais perguntas
  escritas por pessoas são o próximo passo.
- **Sintomas que o resumo não cobre:** quando o resumo do danluu fala só da causa, uma pergunta de sintoma
  pode não achar o incidente no topo. Exemplo: "um serviço central passou a responder 401 para todas as
  requisições" acha o Cloudflare de 2023 (DAN-017) só em 8º.
- **Etapa 2 não medida:** a escolha dos trechos do texto completo ainda não tem métrica própria.

**Precisa de GPU?** Não. Sem GPU, cada pergunta leva ~1 s a mais e o pipeline completo leva ~2,5 min, porque
os vetores já vêm prontos no git.
