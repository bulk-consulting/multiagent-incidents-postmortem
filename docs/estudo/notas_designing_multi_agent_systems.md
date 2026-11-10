# Notas de estudo — *Designing Multi-Agent Systems* (Victor Dibia)

Base teórica para as próximas etapas do Projeto 4 (Incident Copilot). São notas em português, com
as palavras do resumo, não trechos do livro. "p." é a página do PDF.
Livro: *Designing Multi-Agent Systems: Principles, Patterns, and Implementation for AI Agents*,
Victor Dibia (autor do AutoGen e do LIDA, Microsoft Research). Código em
github.com/victordibia/designing-multiagent-systems (biblioteca didática `picoagents`).

Cada capítulo termina com **→ No nosso projeto**: o que a ideia muda ou confirma no Incident Copilot.

---

## Visão geral (prefácio, p. 15–24)

- O livro vem da experiência do autor com o AutoGen e com clientes da Microsoft. Os problemas reais que
  ele relata: agentes que não seguem instruções (modelos antigos agradeciam uns aos outros sem parar), a
  importância do planejamento e da escolha das ferramentas, ferramentas de desenvolvimento e segurança.
- **Pipeline × agente.** Um pipeline (como o LIDA, em 4 etapas) é confiável porque cada etapa é testável
  sozinha. Mas ele supõe que a decomposição da tarefa é conhecida, que há expertise para cada etapa e que
  a tarefa é estável. Agentes servem quando essas suposições falham.
- **Pragmatismo:** os melhores sistemas combinam engenharia tradicional (decomposição, avaliação
  sistemática, otimização) com IA. Exemplo do LIDA: o erro caiu de 20% para 3% só com prompts melhores e
  um modelo novo. Ou seja, medir e iterar vale mais que descartar a ideia cedo.
- Proporção que o autor sugere: ~40% teoria (modelos, avaliação, tradução do problema de negócio) e ~60%
  engenharia de sistemas (arquitetura, código, deploy).
- Organização: Parte I (conceitos), Parte II (construir do zero), Parte III (avaliação, otimização,
  protocolos, ética), Parte IV (casos completos).

## Cap. 1 — Entendendo sistemas multiagentes (p. 26–54)

**Três níveis de tarefa.**
- *Modelo:* responder com o que está no treino ("qual a altura da Torre Eiffel").
- *Agente:* precisa de dado atual, de plano e de ferramenta ("preço da ação hoje").
- *Multiagente:* precisa de várias especialidades e de iteração ("construir um app de ações e impostos").

A fronteira entre "um agente" e "vários" é difusa: um agente pode usar outro agente como ferramenta.

**Quatro características que justificam multiagentes** (p. 32–35). O que pesa mais é a combinação delas:
1. *Planejamento:* decompor a tarefa em passos com um estado de sucesso.
2. *Especialidades diversas:* cada passo pede um papel. Separar responsabilidades por agente dá separação
   de responsabilidades e um design guiado pelo domínio.
3. *Contexto extenso:* LLMs prestam atenção ao começo e ao fim do contexto e negligenciam o meio ("lost
   in the middle", Liu et al. 2024). A solução é o **fornecimento seletivo de contexto**: cada agente
   recebe só o que importa para a sua parte.
4. *Soluções adaptativas:* o caminho só aparece depois de agir (uma API falha, uma fonte não existe), e é
   preciso replanejar. Aqui entra a metacognição: refletir sobre a própria estratégia.

Pesquisas citadas: debate entre agentes melhora raciocínio e factualidade (Du et al. 2023); separar quem
faz de quem julga melhora a qualidade e a diversidade (Liang et al. 2023).

**O que é um agente** (p. 36–40):
- **Capacidades:** raciocinar, agir, comunicar e se adaptar.
- **Componentes:**
  - *Modelo*, o motor de decisão. Pode ser combinado com lógica fixa ou com uma pessoa.
  - *Ferramentas*, de uso geral (executar código, operar uma interface) ou específicas do domínio
    (chamar a API X).
  - *Memória*: de curto prazo (histórico da tarefa) e de longo prazo (o que se aprendeu e persiste).
    Ela pode ser gerenciada pela aplicação (o código decide o que guardar) ou pelo próprio agente
    (ele decide, via ferramentas).
- **Ciclo ação–percepção:** agir, observar o resultado, ajustar, até resolver.
- **"Programação conversacional":** cada passo do ciclo vira uma mensagem numa conversa. É a base do
  AutoGen.
- **Agente × modelo:** o modelo gera texto a partir do treino; o agente age, usa ferramentas, mantém
  contexto e se adapta ao resultado.

**Sistema multiagente** (p. 41–42): o que o define é a **orquestração**, ou seja, como os agentes
trocam informação e quem decide a ordem de execução. Há duas famílias:
- **Workflows (orquestração definida):** a ordem está programada. São previsíveis, repetíveis e
  testáveis.
- **Orquestração autônoma (guiada por IA):** o modelo decide em tempo de execução quem age. É
  adaptável, mas menos previsível.

**Por que agora** (p. 43–45): os modelos ganharam capacidade de raciocínio. Há "arbitragem de tempo"
(o agente demora mais, mas custa US$ 1–2 contra US$ 30–100 da hora humana). Os sistemas melhoram sozinhos
quando o modelo melhora. E abre-se espaço para tarefas de conhecimento tácito. Agentes distribuídos
entre organizações, como no protocolo A2A, costumam ser excesso de engenharia no começo: a maioria dos
casos cabe num processo só.

**Como escolher a arquitetura** (p. 46–47, fig. 1.8). Começa pela pergunta mais simples:
1. Precisa só gerar texto? Uma chamada direta ao modelo resolve.
2. Precisa agir, e o caminho é conhecido? Use um workflow: com **um agente** se basta uma especialidade,
   com **vários agentes em workflow** se cada etapa pede uma especialidade.
3. O caminho não é conhecido? Um único agente resolve ciclos simples de ação e verificação. **Multiagente
   autônomo** só vale quando a solução emerge da exploração, quando os agentes precisam evoluir separados
   ou quando a colaboração depende de resultados intermediários.

**Princípio:** use a arquitetura mais simples que resolve. Cada nível acrescenta complexidade, custo,
latência e pontos de falha. Na avaliação do cap. 10, a chamada direta ao modelo vence nas tarefas simples
de raciocínio (9,7/10, com 24× menos tokens que o multiagente). Agentes com ferramentas só se justificam
quando a tarefa precisa delas (pesquisa na web: 3,2/10 sem ferramenta, 9,0/10 com).

**Exemplo prático** (p. 48–52): um poeta e um crítico em *round-robin*, com condições de parada
combinadas: no máximo N mensagens **ou** o crítico escrever "APPROVED". É o padrão gerador–crítico.

**→ No nosso projeto**
- O Incident Copilot tem as quatro características, mas em graus diferentes:
  - *planejamento:* triagem → busca → hipótese → mitigação → postmortem;
  - *especialidades:* diagnóstico, histórico, comunicação;
  - *contexto extenso:* logs, métricas e postmortens longos;
  - *adaptação:* a hipótese muda conforme a evidência chega.
- O ponto de partida pela regra "o mais simples que resolve" é um **workflow** com etapas conhecidas.
  Autonomia só nos trechos em que o caminho realmente não é conhecido, como investigar a causa.
- *Fornecimento seletivo de contexto* é o que a busca em duas etapas já faz: o agente recebe os 5
  incidentes e os trechos relevantes, não os postmortens inteiros.
- O par gerador–crítico (quem escreve o postmortem e quem confere contra a evidência) é um bom candidato
  para a etapa de redação.

## Cap. 2 — Padrões multiagentes (p. 55–73)

**Ideia central:** todos os padrões se ordenam num **espectro de autonomia**. Num extremo, o
desenvolvedor define o caminho (workflow); no outro, os agentes decidem em tempo de execução
(autônomo). Controle e autonomia andam em sentidos opostos.

O que muda em relação a engines como Airflow, Temporal e Prefect: o raciocínio é semântico (em
linguagem natural, não em regras), o plano se ajusta ao resultado intermediário, a saída é probabilística
(exige formas novas de detectar erro) e o custo é em tokens, que cresce com o tamanho da conversa.

**Workflows (controle explícito):** grafo de **nós** (função, agente ou até uma equipe) e **arestas**
(a saída de A vira a entrada de B, com condição opcional). Ganha-se validação antes de rodar,
visualização e determinismo. Há uma fase de montagem e outra de execução.
- *Sequencial* (A→B→C): erro isolado, tempo previsível.
- *Condicional:* a aresta depende de uma condição, como teste falhou → volta para o código.
  - *Supervisor:* um nó central roteia para especialistas.
  - *Hierárquico:* o nó é um workflow inteiro.
- *Paralelo:* DAG com *fan-out*/*fan-in*. O cuidado é esperar todos os ramos no *fan-in*.
- No fundo, é o padrão de pipeline de sempre com LLM nos nós, o que permite reaproveitar a engenharia
  conhecida (teste, escala). As suposições continuam as mesmas: decomposição conhecida, recursos para
  montar o caminho e uma tarefa estável.

**Autônomos (controle emergente):**
- **"Agentes até o fim"** (p. 62): qualquer agente pode ser, por dentro, um sistema multiagente. Cada
  camada pode usar o padrão que lhe cabe, e a conversa interna fica privada, o que reduz o ruído.
- **Baseado em plano:** um orquestrador "gerente de projeto" cria o plano, atribui passos, avalia cada
  passo e repete com instruções melhores quando falha. Ele vê todo o contexto, e cada especialista recebe
  só o que precisa. O risco é virar ponto único de falha e gargalo de raciocínio.
  - Exemplos: o *Magentic-One* (orquestrador + 4 agentes, com "registro da tarefa" e "registro do
    progresso", 1º lugar no GAIA) e o sistema de pesquisa da Anthropic (orquestrador e trabalhadores em
    paralelo, de 1 a 10+ subagentes conforme a complexidade, +90% sobre um agente só).
- **Handoff (passagem de bastão):** cada agente conhece só alguns outros e decide sozinho a quem
  transferir, levando o estado junto. Na prática, "transferir para B" vira uma chamada de ferramenta.
  Escala sem gargalo central, mas pode ficar preso em ciclos.
- **Conversa em grupo:** todos escrevem numa conversa compartilhada, e quem fala depois é escolhido em
  *round-robin*, ao acaso ou por um LLM seletor. É simples de implementar ("todos anexam à mesma lista")
  e melhora sozinho quando o modelo melhora. ReAct (pensar → agir → observar) e Reflexion (transformar
  falhas em lições guardadas) surgem naturalmente.
  - Limites: o custo em tokens cresce com a conversa, o contexto transborda e os agentes podem tomar
    decisões conflitantes mesmo vendo tudo (Cognition, 2025).

**Comparação** (tabela 2.2, resumida):

| Padrão | Autonomia | Controle | Complexidade |
|---|---|---|---|
| Sequencial / condicional / paralelo | baixa | alto | baixa a média |
| Baseado em plano | alta | médio | alta |
| Handoff | média | médio | média |
| Conversa round-robin | baixa | alto | baixa |
| Conversa com seletor LLM | alta | baixo | média |

**Como escolher:** pergunte "do que a tarefa precisa?", e não "qual é o melhor padrão?".
- *Pela tarefa:*
  - processo repetível → workflow;
  - exploratório → conversa;
  - planejamento complexo → baseado em plano;
  - especialidade de domínio → handoff.
- *Pela restrição:*
  - previsibilidade ou confiabilidade em produção → workflow;
  - protótipo rápido → conversa;
  - supervisão humana → qualquer padrão + delegação humana.
- **Híbrido é o normal em produção:** workflow nas partes conhecidas, autonomia onde é preciso adaptar,
  composição hierárquica e o mesmo gerenciamento de tarefa em tudo.

**Gerenciamento da tarefa (vale para todos os padrões):**
- **Parada:**
  - por orçamento (tempo, custo, número de passos);
  - semântica (um LLM julga que terminou);
  - por sinal externo (pessoa ou API).
  - Combinar com "ou" é o usual: 10 iterações **ou** atingiu a qualidade.
- **Delegação a humanos:**
  - por LLM: o agente avalia risco e confiança e escala;
  - por regra: limites explícitos e auditáveis, como valor acima de X, domínio jurídico ou médico, ou
    3 falhas seguidas.

**→ No nosso projeto**
- **Esqueleto como workflow:** triagem → busca (as duas etapas que já temos) → hipótese de causa →
  sugestão de mitigação → rascunho de postmortem. As etapas são conhecidas e precisam ser previsíveis e
  auditáveis. Com LangGraph, isso é um grafo de estado com arestas condicionais.
- **Supervisor/roteador** na entrada: tipo de pedido (diagnóstico em andamento × redação de postmortem ×
  pergunta sobre histórico) → subfluxo.
- **Autonomia só dentro do nó "investigar causa":** um agente com ferramentas (busca no RAG, logs,
  métricas) em ciclo ReAct, com parada por orçamento **ou** confiança.
- **Paralelo:** buscar incidentes parecidos e consultar telemetria ao mesmo tempo, com *fan-in* antes da
  hipótese.
- **Delegação humana por regra:** pedir aprovação antes de qualquer ação de mitigação, e escalar quando
  a busca não acha incidente parecido. Isso conversa com a limitação "não achei" da E2.
- Evitar conversa em grupo livre no caminho principal: custo e imprevisibilidade.

## Cap. 3 — Princípios de UX para sistemas multiagentes (p. 74–90)

**Mudança de paradigma:** do *design de interface* (clicar num botão dispara uma rotina previsível)
para o **design de delegação** (o usuário entrega uma tarefa aberta, e o sistema escolhe as ações). Três
propriedades tornam isso diferente:
- *autonomia:* o modelo escolhe entre muitas ações;
- *consequência:* as ações têm efeito real;
- *duração:* as tarefas são longas e envolvem vários sistemas.

O usuário final costuma enxergar "um sistema só"; ver o que acontece dentro deve ser opcional, mas
possível.

- **Software 1.0 → 2.0 → 3.0+:** regras → aprendizado com dados → agentes que raciocinam e agem. Um não
  substitui o outro: cada parte do sistema usa o paradigma que lhe cabe.
- **"Fronteira irregular"** (*jagged frontier*, Dell'Acqua et al. 2023): o modelo acerta coisas difíceis
  e erra coisas fáceis, como dizer se 9,11 é maior que 9,9. Com vários agentes, falhas de coordenação se
  somam aos erros de cada modelo. Tarefas parecidas podem dar certo ou errado, e isso dificulta o usuário
  formar um modelo mental do sistema.
- **Duas personas, duas necessidades:**
  - **Usuário final**, que precisa de *transparência funcional*: o que está acontecendo, por que cada
    decisão foi tomada, controles simples, detalhe sob demanda e clareza sobre o que funcionou ou não.
  - **Desenvolvedor**, que precisa de *transparência arquitetural*: escolher o padrão de coordenação,
    distinguir falha de coordenação de erro de um agente, perfilar custos e passos redundantes.

**Quatro princípios de UX:**
1. **Descoberta de capacidades:** o usuário não sabe em que o sistema é confiável. Ofereça exemplos
   prontos de tarefas que funcionam bem, sugestões guiadas e revelação progressiva. Indique o ponto forte
   ("confiável para X, exige revisão para Y") e os limites (quando chamar uma pessoa).
2. **Delegação consciente do custo:** cada ação tem um nível de consequência se der errado. Resumir tem
   custo baixo; cancelar uma reunião, médio; enviar um documento confidencial para fora, alto. Proposta
   em três níveis:
   - baixo: executa sozinho;
   - médio: executa e avisa;
   - alto: pede permissão antes.
   Mostre o impacto antes de executar, com configurações simples para o usuário e limites detalhados para
   o desenvolvedor.
3. **Observabilidade e proveniência:** mostrar o que os agentes fizeram, por quê e com base em quais
   dados, porque cada execução pode seguir um caminho diferente. Para o usuário: progresso ao vivo, uma
   narrativa simples e a causa de cada falha em termos dele, nunca só "erro". Para o desenvolvedor:
   rastros completos, atribuição de erro, tokens e desempenho.
4. **Interrupção:** poder pausar, retomar e cancelar sem perder o estado. Isso inclui correções "leves"
   sem parar tudo, retomar mostrando o que aconteceu na pausa e, para o desenvolvedor, interromper um
   agente só ou trocar de padrão no meio da tarefa.

**Interativo × offline:**
- *Interativo:* o usuário acompanha e corrige ao vivo, e a latência importa.
- *Offline:* o sistema trabalha sozinho e avisa ao terminar ou quando há exceção. A latência importa
  menos, e vale ter verificação automática do resultado.

**→ No nosso projeto**
- O copiloto tem os dois modos:
  - **interativo** durante o incidente: o engenheiro de plantão pergunta, e a latência importa;
  - **offline** depois: redação do rascunho de postmortem, com verificação automática contra a evidência.
- *Descoberta de capacidades:* exemplos de perguntas que funcionam bem (sintomas descritos como na suíte
  de avaliação) e um aviso claro de quando a busca não acha incidente parecido. É a limitação "não achei"
  da E2, que vira uma questão de UX.
- *Custo das ações:* consultar o RAG e ler métricas têm custo baixo e rodam sozinhos. Sugerir uma
  mitigação tem custo médio (é só texto, mas pode induzir uma ação). Executar algo no ambiente (rollback,
  reiniciar) tem custo alto: aprovação explícita, ou fora do escopo.
- *Proveniência* é o ponto forte que a E2 já prepara: todo trecho mostrado vem literal do postmortem, com
  `url` e `doc_id`. A resposta do agente deve citar o incidente e o trecho.
- *Observabilidade:* fazer streaming dos passos (achou 5 incidentes, lendo o DAN-023…) e guardar um
  rastro por execução para depurar. Ver o OpenTelemetry no cap. 4.

## Cap. 4 — Construindo o primeiro agente (p. 92–149)

O capítulo monta um agente do zero (biblioteca `picoagents`) e justifica cada decisão. A interface mínima
que virou padrão nos frameworks: **agente = modelo + ferramentas + memória**.

**Cinco princípios de design** (p. 94):
1. **Assíncrono desde o início:** chamadas de LLM levam de 0,5 a 5 s. Com async, três agentes que
   levariam ~30 s em sequência levam ~10 s. Adaptar código síncrono depois é bem mais difícil.
2. **Streaming de eventos:** tarefas de 30 s ou mais precisam mostrar progresso. O stream também é a
   matéria-prima da depuração (mostra onde o agente entrou em loop).
3. **Serialização dos componentes:** agente, ferramentas e memória viram JSON, o que permite versionar
   a configuração, editar visualmente e restaurar sessões.
4. **Cancelamento limpo:** um "token de cancelamento" verificado antes de cada chamada ao modelo, durante
   o streaming e antes de cada ferramenta. É o que o botão "Parar" da interface aciona.
5. **Classes base abstratas** para modelo, ferramenta e memória: trocar de provedor sem reescrever o
   agente e testar com implementações falsas (*mocks*).

**O ciclo do agente** (p. 95):
1. montar o contexto (instruções + memória + histórico + tarefa);
2. chamar o modelo;
3. se ele pediu ferramentas, executá-las, anexar os resultados e voltar ao passo 2;
4. senão, responder e, se for o caso, atualizar a memória.

Há sempre dois modos de execução: esperar a resposta final ou acompanhar por streaming.

**Cliente do modelo:** sempre o mesmo padrão: converter as mensagens para o formato do provedor, chamar a
API e converter a resposta de volta, guardando o uso de tokens. O livro padroniza na API da OpenAI, que
virou padrão de fato e também atende Azure, vLLM e modelos locais.

**Saída estruturada é a base da confiabilidade** (p. 100): obrigar o modelo a responder num schema
(Pydantic) em vez de texto livre. A chamada de ferramenta é só uma aplicação disso: o modelo gera um JSON
com nome e argumentos que batem com o schema da ferramenta. As descrições dos campos ajudam o modelo.

**Ferramentas** (p. 104–107):
- **Tipos:** *de uso geral* (executar código, operar uma interface) dão flexibilidade, mas exigem
  isolamento (sandbox). *Específicas* (enviar e-mail, consultar uma base) restringem o agente e o tornam
  mais previsível.
- **Interface comum** (nome, descrição, schema dos parâmetros, execução) para que funções, APIs REST e
  ferramentas MCP entrem do mesmo jeito.
- **Funções Python** viram ferramentas automaticamente: assinatura e docstring geram o schema.
- **Erros** (ferramenta inexistente, falha, exceção) voltam como mensagem para o modelo, sem derrubar
  o agente. O modelo vê o erro e pode tentar outra coisa.

**Memória** (p. 108–121):
- *Curto prazo:* o histórico da conversa. Permite resolver "quando *ela* foi construída?". Ele se perde
  quando a sessão termina.
- *Longo prazo:* RAG. Indexar como vetores, buscar por similaridade e injetar no prompt. A fonte pode ser
  qualquer coisa: banco relacional, API, grafo.
- **O difícil é decidir o que guardar.** Guardar tudo traz ruído; guardar pouco perde o essencial. Há
  três caminhos: curadoria manual, seleção automática (frequência, importância, novidade) ou um misto,
  com o sistema sugerindo e uma pessoa aprovando o que é crítico.
- **Contexto da sessão × memória persistente:** o contexto é transitório e serializável, o que permite
  execução *stateless*: qualquer servidor retoma a sessão. A memória persiste entre sessões.
- **Gerenciada pela aplicação × pelo agente:**
  - *Pela aplicação:* o código decide o que guardar e injeta o que for relevante.
  - *Pelo agente:* uma "ferramenta de memória" em forma de arquivos (ver, criar, editar, apagar, mover),
    em que o agente decide o que registrar.
  - Exemplo: um revisor de código aprende um padrão de bug numa sessão e o reconhece em outra.
  - Cuidado obrigatório: validar caminhos para impedir *path traversal*.
  - As duas podem coexistir.

**Middleware para controle e observabilidade** (p. 122–128): interceptadores em volta de cada chamada ao
modelo e de cada ferramenta, com três ganchos: antes, depois e em caso de erro. Cada um pode bloquear,
alterar ou emitir eventos. Exemplos:
- **segurança:** bloquear padrões de injeção de prompt *antes* de gastar uma chamada, e fora dos logs;
- **log e tempo** de cada operação;
- **redação de dados pessoais** (PII) nas saídas;
- **limite de taxa e custo** por usuário;
- **auditoria** para setores regulados.

O ganho é tirar essas preocupações do código do agente e ter comportamento **determinístico, por código,
e não por prompt**.

**OpenTelemetry** (p. 129–134):
- É o padrão aberto (CNCF) para rastros, métricas e logs, com as *convenções semânticas de GenAI*
  (nomes padronizados para modelo, tokens de entrada e saída, nome da ferramenta, sucesso).
- **Instrumente uma vez e exporte para qualquer destino:** Jaeger, Grafana, Langfuse, Phoenix, Datadog,
  Azure Monitor…
- **Privacidade por padrão:** por padrão vão só os metadados (operação, modelo, tokens, status). O
  conteúdo de prompts, respostas e argumentos é opcional, porque pode conter dados pessoais.

**Agentes como ferramentas** (p. 135–137): um agente vira ferramenta de outro, com um único parâmetro
(a tarefa); a descrição do agente vira a descrição da ferramenta. Cada especialista mantém modelo,
ferramentas e memória próprios, e pode usar um modelo barato para o que é simples e um modelo de
raciocínio para o que é complexo.
- **Decisão crítica: o que volta para o coordenador.**
  - Só a última mensagem: isolamento máximo, mas pode perder o conteúdo se ela for só "Pronto!".
  - As últimas N mensagens.
  - Tudo: transparência total, mas o contexto explode.
  - Uma função própria que extrai só as conclusões.

**Engenharia de contexto** (p. 137–143). "O LLM é a CPU, o contexto é a RAM" (Karpathy).
- *Context rot:* a capacidade de lembrar cai à medida que o contexto cresce, a partir de ~32 mil tokens,
  bem antes do limite anunciado. *Context explosion:* cada chamada de ferramenta acrescenta parâmetros,
  resultado e erros.
  - Exemplo: 2.600 tokens no início viram ~20 mil depois de 5 ferramentas.
  - Agentes falham *em silêncio*: um que ia bem em 5 passos alucina no 8º.
- **Estratégias:**
  - **compactação:** manter o começo (instruções e tarefa) e o fim (trabalho recente) e cortar o meio,
    sem nunca separar um pedido de ferramenta do resultado dela;
  - **memória ativa:** o agente guarda e apaga;
  - **isolamento:** um subagente gasta 30 mil tokens, e o coordenador recebe um resumo de 200;
  - **filtrar resultados grandes** de ferramentas, por exemplo devolver um agregado em vez de 10 mil
    linhas.
- **Medição do livro:** sem gestão, 21,6 mil tokens; com compactação, 7,3 mil (−66%); com isolamento,
  5,9 mil (−73%). **Prevenir pela arquitetura (isolamento) rende mais que remediar (compactar).**
- **Ganchos no nível do ciclo** (não de cada operação):
  - *de início:* força planejar antes de agir, com uma lista de tarefas;
  - *de fim:* um segundo modelo julga se a tarefa terminou de verdade, com base nas ferramentas
    chamadas e não no que o agente afirma, e limita os recomeços.
  - Isso resolve o agente que lê 6 de 30 arquivos e declara que terminou.
  - Cuidado com o **thrashing**: um orçamento de tokens apertado demais + o gancho de fim faz o agente
    reler o que já tinha lido. Dimensione o orçamento antes (2 a 3 vezes o conjunto de trabalho de cada
    passo).

**Humanos no ciclo** (p. 144–147):
- **Ferramentas que exigem aprovação:** o agente *para*, guarda todo o estado no contexto serializado e
  devolve um pedido de aprovação. Uma nova execução retoma de onde parou. Não fica nada preso no
  servidor.
- **Pedido de esclarecimento:** pelas instruções, o agente responde com um marcador ("preciso de
  esclarecimento: …"), e a resposta da pessoa entra como uma mensagem a mais. A resposta humana é
  tratada como um resultado de ferramenta.
- **Benefícios:** escala, não segura conexões abertas, sobrevive à queda do servidor e funciona com
  balanceador sem afinidade de sessão.

**→ No nosso projeto**
- **Saída estruturada em tudo** que o agente produz para o sistema consumir: hipótese de causa (com
  categoria, confiança e incidentes citados), sugestão de mitigação, rascunho de postmortem (os campos do
  template). Foi o que deu certo nas fichas (schema + validador); vale repetir na resposta do agente.
- **A busca da E2 como ferramenta** de interface bem definida, por exemplo
  `buscar_incidentes(pergunta, n_docs, n_trechos)` → JSON com `doc_id`, resumo, trechos e similaridade.
  O `busca.py` já devolve essa estrutura. Ferramentas específicas (busca no RAG, consulta de métricas)
  antes de ferramentas de uso geral.
- **Memória:**
  - o RAG dos postmortens é a memória de longo prazo, *gerenciada pela aplicação*;
  - o histórico do incidente em andamento é a memória de curto prazo;
  - a memória *gerenciada pelo agente* fica para depois, se for o caso.
- **Middleware/OpenTelemetry:** o LangGraph integra com LangSmith e OpenTelemetry. Vale instrumentar
  desde o início: tokens por etapa, latência e ferramentas chamadas. Conteúdo só em desenvolvimento,
  porque logs de incidente podem ter dados sensíveis.
- **Engenharia de contexto:**
  - o agente de investigação deve receber os 5 incidentes e os trechos (já são compactos), não os
    postmortens inteiros;
  - se houver subagentes (como um "analista de histórico"), devolver ao coordenador só as conclusões;
  - o `n_trechos` da busca é um controle direto do contexto.
- **Humano no ciclo:** as ferramentas de ação ficam marcadas como "exige aprovação". O LangGraph tem
  `interrupt` e checkpoints, que fazem exatamente o "parar, guardar o estado e retomar".
- **Gancho de fim** no agente que redige o postmortem: um juiz confere se todas as seções do template
  foram preenchidas com evidência antes de liberar.

## Cap. 5 — Agentes que usam o computador (p. 150–171)

*Pouco relevante para o copiloto. Fica o resumo dos conceitos que se transferem.*

- **Quando usar:** quando código e API não bastam. Exemplos: software sem API, tarefas visuais
  (desenhar num mapa), navegar em vários sites, *back-office* entre sistemas desconectados e testes de
  ponta a ponta. Exemplos comerciais: Operator (OpenAI), Computer Use (Anthropic), Manus.
- **Três componentes:** gerar a sequência de ações, representar a interface e executar as ações. O ciclo
  é **observar → pensar → agir**.
- **Planejamento explícito × implícito:**
  - *explícito:* o plano inteiro é feito antes. É eficiente em telas estáveis, como um formulário;
  - *implícito:* um passo de cada vez, olhando o estado atual. Adapta-se a telas dinâmicas, como busca
    de voos ou um feed, mas faz mais chamadas.
  - **O critério vale para qualquer agente:** se o ambiente é estável, planeje antes; se muda, replaneje
    a cada passo.
- **Espaço de ações:** o conjunto de ações possíveis precisa estar explícito para o modelo, e cada ação é
  uma ferramenta.
- **Representação do estado:**
  - texto (DOM filtrado só com os elementos interativos, ou as APIs de acessibilidade): barato e preciso;
  - imagem (captura de tela, com marcações nos elementos como no Set-of-Mark e no OmniParser): caro;
  - híbrido: o recomendado.
  - **Lição geral:** filtrar o estado antes de mandar para o modelo (ruído e tokens).
- **Observar depois de agir:** a ferramenta que clica não diz o que aconteceu. É preciso uma ferramenta
  de observação, e o resultado de cada ação precisa ser verificado.
- **Modelos especializados** (como o UI-TARS, ajustado para interfaces) superam modelos gerais nessas
  tarefas. Vale lembrar que ajuste fino especializado é uma opção quando o modelo geral não basta.
- **Desafios:** representação e ancoragem, memória entre telas, ambiguidade de alvos (pedir ajuda quando
  a confiança é baixa), segurança e privacidade, latência e custo, robustez a mudanças.
  - **Custo é infraestrutura:** orçamento de tokens por sessão, custo por tarefa, modelo pequeno para a
    rotina e grande só para o raciocínio difícil.
- **Segurança:** injeção de prompt escondida na página é o vetor principal. Também: vazamento de
  credenciais, extensões de terceiros, ferramentas de segurança que não distinguem agente de humano.
  Práticas: sandbox, credenciais de vida curta com permissão mínima, filtrar dados sensíveis antes de
  logar, confirmação para ações sensíveis e respeitar o `robots.txt` e os termos de uso.

**→ No nosso projeto**
- Não precisamos de um agente que opere a interface: as ferramentas são APIs (RAG, métricas, logs).
- O que se transfere:
  - planejar antes quando o fluxo é estável (o roteiro de triagem) e replanejar a cada passo na
    investigação;
  - **observar o resultado de cada ação** (conferir se a busca voltou vazia antes de seguir);
  - filtrar o estado: mandar ao agente só os campos úteis de logs e métricas, nunca o dump inteiro;
  - **conteúdo externo é entrada não confiável:** postmortens e logs podem conter instruções
    maliciosas. É o mesmo cuidado que a E2 já tem com os dados baixados, agora com um LLM lendo esse
    conteúdo.

## Cap. 6 — Construindo workflows multiagentes (p. 172–195)

**Workflow = grafo computacional de passos e arestas.** É o que existe por baixo de ferramentas visuais
como n8n e Flowise. Um passo pode ser qualquer computação: função pura, chamada de API, agente ou até
outro workflow.

- **Passos com contrato de tipos:** cada passo declara o tipo de entrada e de saída (modelos Pydantic).
  O workflow confere **antes de rodar** se a saída de um passo é compatível com a entrada do próximo.
  Cada passo tem estado (pendente, rodando, concluído, falhou), limite de tentativas e timeout.
- **Arestas:**
  - *sempre*: sequência;
  - *por saída*: "se `is_valid` for verdadeiro, vá para processar; senão, para tratar o erro";
  - *por estado compartilhado*: decisões guiadas por configuração.
- **Paralelo:** *fan-out* (um passo alimenta vários) e *fan-in* (um passo espera vários).
  - Regra de prontidão elegante: se todas as arestas que chegam são "sempre", o passo espera **todas**
    as dependências (E). Se são condicionais, basta **um** caminho válido (OU), como sucesso ou erro.
- **Validação antes de rodar:** passos de início e fim existem, arestas apontam para passos que existem,
  não há ciclos inesperados e os tipos são compatíveis.
- **Estado compartilhado** (um "contexto" lido e escrito pelos passos): um passo de configuração define o
  tamanho do lote, e os seguintes usam esse valor.
- **Executor:**
  - resolve dependências;
  - roda os passos prontos em paralelo, com um limite de concorrência;
  - detecta impasse ("nada pronto, nada rodando e ainda faltam passos");
  - emite eventos (início e fim de cada passo, com duração) para observar e alimentar a interface.
- **Serialização:** o workflow vira JSON, que pode ser versionado, compartilhado e editado visualmente.
- **Checkpoints** (p. 191–194):
  - depois de cada passo, salva quais passos terminaram, as saídas deles e o estado compartilhado;
  - para retomar, pula o que terminou e não repete chamadas caras de LLM ou API;
  - **guarda um hash da estrutura** (passos, arestas e tipos) e recusa retomar se o workflow mudou;
  - o armazenamento é abstrato: memória (testes), arquivo (uma máquina), banco ou S3 (distribuído).
  - **Com o checkpoint num armazenamento compartilhado, qualquer worker retoma qualquer execução:** os
    workers ficam descartáveis, e escalar é só adicionar workers.
- **Quando usar workflow:** a solução é conhecida, a previsibilidade importa, há dependências explícitas e
  é preciso ver passo a passo. Exemplos: pipelines de dados, fluxos de aprovação, qualquer coisa que
  exija trilha de auditoria.

**→ No nosso projeto**
- O **pipeline da E2 já é um workflow** nesse sentido: 8 etapas com dependências, validação e
  reaproveitamento (pular a geração dos vetores quando batem com os chunks é um checkpoint com conferência
  de compatibilidade, parecido com o hash de estrutura). Vale citar isso na apresentação como
  continuidade de projeto.
- No LangGraph, isso se traduz quase um a um:
  - `StateGraph` com um **estado tipado** (TypedDict/Pydantic) = o estado compartilhado;
  - nós = passos;
  - `add_edge` / `add_conditional_edges` = arestas;
  - `Send` = fan-out;
  - **checkpointer** (memória, SQLite ou **Postgres**) = checkpoints.
  - Já temos Postgres no Docker, então dá para usar o checkpointer de Postgres do LangGraph no mesmo banco.
- **Contrato de tipos entre os nós:** definir os modelos de dados do copiloto desde o começo
  (`Incidente`, `ResultadoBusca`, `Hipotese`, `Mitigacao`, `RascunhoPostmortem`) e validar nas
  fronteiras. Isso evita que um nó "LLM" passe texto solto para o próximo.
- **Condicionais típicas:**
  - "a busca achou incidente parecido?" (sim → hipótese baseada no histórico; não → investigação
    aberta ou escalar);
  - "a confiança da hipótese passa do limite?" (sim → sugerir mitigação; não → pedir mais dados).
- O checkpoint por passo também é a base do humano no ciclo (pausar para aprovação e retomar) e da
  retomada depois de uma falha.

## Cap. 7 — Orquestração autônoma (p. 196–220)

**Um único ciclo por trás de todos os padrões autônomos:**
1. escolher o próximo agente;
2. montar o contexto para ele;
3. executá-lo;
4. atualizar o estado compartilhado;
5. checar a condição de parada.

Cada padrão só muda três peças: *como escolher*, *que contexto entregar* e *como atualizar o estado*. O
resto (streaming, cancelamento, tratamento de erro, soma de tokens e tempo) é comum a todos. Há sempre um
**limite máximo de iterações** como rede de segurança.

- **Condições de parada combináveis:** por número de mensagens, por texto ("TERMINATE"), por orçamento de
  tokens, por tempo, por handoff. Combinam com **OU** ("20 mensagens ou 'DONE' ou 5 minutos") e **E**.
  A checagem olha só as mensagens novas desde a última verificação, o que é mais eficiente e reage ao
  que acabou de acontecer.
  - O texto de parada pode aparecer até na entrada do usuário, por isso se checa logo no início.
- **Round-robin:** a ordem é fixa e todos veem o histórico inteiro. É o que exige menos código e é ótimo
  para a primeira versão de um protótipo.
  - Detalhe que pesa: **o formato do contexto** (texto corrido, JSON, Markdown) muda a qualidade da
    resposta. Frameworks escondem essa escolha, e às vezes é preciso customizá-la.
- **Escolha por IA:** um LLM recebe as capacidades dos agentes e a conversa recente e devolve, em saída
  estruturada, quem fala agora e por quê. Adapta-se bem (volta ao pesquisador se o redator pedir mais
  dados), mas **cada escolha é uma chamada a mais ao LLM**.
- **Baseado em plano:**
  - um LLM gera o **plano estruturado** (passos com tarefa, agente responsável e justificativa);
  - depois de cada passo, outro LLM **avalia** se ele cumpriu o objetivo, também em saída estruturada:
    concluído sim/não, motivo da falha, confiança e sugestões;
  - quando falha, **repete com a análise da falha no contexto** ("a tentativa anterior falhou por X;
    melhore Y"), o que rende bem mais que repetir às cegas. Há um limite de tentativas por passo.
  - **Custo:** 2 ou mais chamadas por passo (planejar, executar, avaliar).
  - **Bom para:** pipelines em fases, tarefas em que a qualidade é crítica (verificar antes de seguir) e
    falhas recuperáveis.
- Em todos, **é a saída estruturada que torna o controle programável:** sem um booleano confiável não
  existe lógica de repetição.
- **Exercícios sugeridos** (bons para nós):
  - parada por orçamento de tokens;
  - comparar padrões medindo tempo, tokens e número de mensagens na mesma tarefa;
  - comparar formatos de contexto (texto × JSON × tabela) e a janela de mensagens (últimas N × todas).

**→ No nosso projeto**
- Se houver uma parte autônoma, o padrão **baseado em plano com avaliação por passo** é o que mais
  combina com a investigação de causa: plano (checar histórico → checar métricas → formular hipótese) →
  avaliação ("a hipótese é sustentada pela evidência?") → repetir com o motivo da falha.
- A avaliação por passo funciona como um *gate* de qualidade. Para o postmortem: "todas as afirmações têm
  trecho citado?". É a mesma ideia do `validar_fichas.py`, só que feita por LLM e no meio do fluxo.
- **Parada composta obrigatória:** iterações **ou** tokens **ou** tempo **ou** "a hipótese tem confiança
  suficiente".
- **Medir os padrões em vez de supor:** dá para repetir o que fizemos na E2 (que comparou índices e
  overlap com 278 perguntas) com tarefas do copiloto. Registrar custo, tempo e acerto de cada desenho.
- **Formato de contexto como variável testável:** os trechos que a busca devolve podem ir como Markdown
  (incidente → resumo → trechos com seção) ou como JSON. Isso entra na avaliação.

## Cap. 8 — Interfaces web para aplicações de agentes (p. 221–245)

- **Por que é diferente de um app web comum:** as tarefas duram minutos, então é preciso mostrar o
  progresso (texto saindo aos poucos, qual ferramenta está rodando, o resultado dela). A coordenação
  entre agentes precisa ser visível, e às vezes o agente pede algo no meio da tarefa.
- **Dois componentes independentes:**
  - *backend:* a lógica do agente + a API que transforma os eventos do agente num stream HTTP;
  - *frontend:* só sabe desenhar eventos e capturar a entrada.
  - Dá para trocar um sem mexer no outro. O mesmo agente serve web, linha de comando e Slack.
- **Recomendação do autor: FastAPI + Server-Sent Events (SSE).** O FastAPI é assíncrono e usa Pydantic.
  O SSE é um stream de mão única sobre HTTP simples (`data: <json>`), e o navegador lê sem biblioteca
  nenhuma.
- **Python puro × feito do zero:**
  - Streamlit (dados e painéis) e Chainlit (chat) servem em minutos para protótipos e ferramentas
    internas, mas limitam a customização.
  - React (o autor recomenda pelo ecossistema e porque assistentes de código o conhecem melhor) + Vite +
    shadcn/ui + Tailwind para produção.
- **Os princípios de UX do cap. 3 viram código:**
  - observabilidade = desenhar cada tipo de evento (token, início de ferramenta, resultado);
  - descoberta de capacidades = 2 ou 3 exemplos de pergunta na tela vazia;
  - interrupção = botão Parar → o navegador fecha a conexão → o backend detecta e aciona o cancelamento
    do agente.
- **SSE × WebSocket:**
  - O WebSocket mantém a conexão aberta e o estado em memória. Exige afinidade de sessão, e uma queda
    derruba todos.
  - O **SSE + contexto salvo** transmite o progresso, salva o contexto e fecha a conexão. A resposta do
    usuário (até uma aprovação horas depois) chega como nova requisição, que carrega o contexto e
    continua.
  - Para o usuário parece igual. Mas o SSE escala com balanceador comum, não consome recursos durante
    a espera e permite aprovações demoradas, trabalho em segundo plano e troca de dispositivo.
  - **Use WebSocket só para colaboração em tempo real ou estado que não dá para serializar.**
- **Deploy:**
  - comece com um servidor só (Docker / docker-compose), que atende centenas de usuários;
  - escale só com evidência (latência piorando, limite de conexões);
  - containers gerenciados (Cloud Run, ECS) em vez de serverless, que tem limite de 15 min e partida a
    frio ruim para agentes.
- **Para produção:** autenticação, OpenTelemetry e limite de requisições por usuário.

**→ No nosso projeto**
- O stack recomendado bate com o que a E1.4 já previa: **FastAPI** + streaming. Usar **SSE** com o
  estado do grafo salvo pelo checkpointer do LangGraph (por `thread_id`). Isso dá de graça a aprovação
  assíncrona de mitigação ("o agente pausa, o engenheiro aprova depois").
- **Protótipo da interface:** Streamlit ou Chainlit para a demonstração das próximas etapas (rápido e só
  em Python). React só se o projeto pedir um produto.
- **Eventos a mostrar:** "buscando incidentes parecidos" → lista dos 5 com a similaridade → "lendo
  trechos" → hipótese → aguardando aprovação. É a observabilidade do cap. 3 aplicada.
- **Exemplos na tela vazia:** as boas perguntas de demonstração (BGP/Facebook, regex/Cloudflare-Stack
  Exchange, banco apagado sem querer).

## Cap. 9 — E os frameworks? (p. 246–259)

- **O autor não compara frameworks diretamente**, porque eles mudam o tempo todo. Ele propõe avaliar
  qualquer opção, inclusive construir a própria, por **10 capacidades estáveis**.
- **Por que usar um framework:**
  - padrões já testados;
  - rapidez;
  - comunidade e integrações;
  - **manutenção:** o maior ganho, porque o time do framework acompanha as APIs dos modelos e corrige
    falhas de segurança;
  - **componentes padronizados e intercambiáveis**, o que facilita a entrada de gente nova e a troca
    de peças.
  - O custo: restrições, curva de aprendizado e dependência do fornecedor.
- **As 10 capacidades** (e o que perguntar):
  1. *Experiência de desenvolvimento em camadas:* "piso baixo, teto alto". Um fluxo simples em menos de
     20 linhas e a possibilidade de estender sem fazer *fork*.
  2. *Assíncrono e com streaming*, com cancelamento e timeout.
  3. *Observabilidade e ferramentas de desenvolvimento:* eventos, logs com ID de correlação, métricas
     de tokens e latência, visualização e *replay*. Sinal de alerta: só dá para testar em produção.
  4. *Estado e persistência:* estado serializável, checkpoints, armazenamento plugável e isolamento entre
     execuções concorrentes. Dá para pausar e retomar? Sobrevive a uma queda?
  5. *Configuração declarativa e reprodutível:* versionar a configuração dos agentes. O autor insiste:
     **sem configuração serializável não há testes de ablação automáticos** (trocar uma peça e rodar a
     avaliação de novo).
  6. *Guardrails e middleware:* interceptar todas as chamadas de modelo e de ferramenta, detectar dados
     pessoais e entradas maliciosas, auditoria.
  7. *Cobertura de padrões:* workflows, autônomos, parada, delegação humana e extensão.
  8. *Produção e segurança:* sandbox de ferramentas, autenticação e autorização, escala horizontal,
     limites e segredos.
  9. *Avaliação e testes:* avaliar a trajetória (os passos esperados × os executados), testes unitários e
     de integração, transformar sessões reais em casos de teste.
  10. *Ecossistema e longevidade:* releases frequentes, comunidade, documentação, governança, como lida
      com mudanças que quebram compatibilidade.
- **Decisão:** uma matriz de pontuação com pesos (o exemplo do livro dá 20% à experiência de
  desenvolvimento, 15% ao assíncrono, 15% ao estado…) + **protótipos focados** nos cenários reais.
  - *Construir do zero* quando os requisitos são muito específicos, há gente experiente com tempo e o
    domínio é estável.
  - *Framework* quando o foco é a lógica de negócio, o prazo é curto e os padrões são comuns.
  - *Híbrido* quando partes do sistema pedem coisas diferentes.
- O que frameworks de produção têm a mais que o didático: persistência e recuperação robustas,
  integração com a nuvem (Microsoft Agent Framework ↔ Azure, Google ADK ↔ Vertex, Pydantic AI neutro),
  guardrails como plugins e plataformas de observabilidade.

**→ No nosso projeto**
- O LangGraph já foi escolhido na E1.4 e está no ambiente. Passado pelas 10 capacidades, ele cobre bem:
  - grafo em camadas (alto nível com nós, baixo nível com funções);
  - assíncrono e streaming;
  - **checkpointer** (com backend em Postgres);
  - `interrupt` para humano no ciclo;
  - observabilidade via LangSmith ou OpenTelemetry;
  - padrões de workflow e de agente (ReAct, supervisor).
- **Pontos fracos para checar num protótipo:** a configuração declarativa (o grafo é código, e não JSON),
  os guardrails (não vêm prontos, são nós ou *callbacks* nossos) e a avaliação (via LangSmith ou feita
  por nós).
- **Configuração versionada para ablação:** guardar num arquivo (YAML/JSON) as escolhas do copiloto
  (modelo do LLM, `n_docs`, `n_trechos`, prompt, temperatura) e rodar a avaliação a cada mudança. É o que
  fizemos na E2 com os índices e o overlap, agora aplicado aos agentes.
- Se a Mari e a dupla quiserem comparar com outro framework, usar essa matriz com pesos em vez de opinião.

## Cap. 10 — Avaliando sistemas multiagentes (p. 261–284)  ★ central para nós

**O que se avalia é a trajetória:** o registro completo de uma execução, com as mensagens, as ações
(chamadas de ferramenta), o resultado (sucesso ou erro) e os metadados (tempo, tokens). Isso vale igual
para uma chamada ao modelo, um agente ou um sistema inteiro. Avaliar só a entrega final perde o processo:
um agente pode acertar por um caminho errado.

**Desenvolvimento guiado por avaliação:** definir *como medir o sucesso antes de construir*, como no TDD.
Os critérios de avaliação viram requisitos de design: se vai medir tokens, instrumente desde o primeiro
dia. Citação de Eugene Yan: quando a avaliação roda com um clique depois de mudar uma configuração, o time
experimenta e melhora rápido. **Cinco perguntas antes de escrever o agente:**
1. O que é sucesso, e em que dimensões (acerto, velocidade, experiência)?
2. Qual é o conjunto de tarefas (representativas, casos de borda, quantas para ter um sinal confiável)?
3. Que métricas usar (determinísticas × juiz LLM, de processo × de resultado, simples × compostas)?
4. Contra o que comparar (como é feito hoje, chamada direta ao modelo, um agente só, versão anterior)?
5. Como iterar (quando rodar, como detectar regressão, como registrar os experimentos)?

- **A observabilidade é a base:** com eventos estruturados (OpenTelemetry), qualquer execução, inclusive
  de produção, pode ser reconstruída e avaliada depois.
- **De onde extrair a resposta:** a última mensagem pode ser só "pronto", com o resultado duas mensagens
  antes. É preciso uma estratégia (última não vazia, última do assistente, todas juntas) ou um juiz que
  olhe a trajetória.
- **Métricas clássicas não servem** (BLEU, ROUGE e NDCG pressupõem uma saída previsível e várias
  referências). Trajetórias de agente misturam texto, JSON, código e erros, e há vários caminhos
  corretos.
- **Traduzir a expertise do domínio em critérios:** "o que um especialista conferiria?". Para cada
  critério, use uma métrica determinística quando houver (rodar testes, cobertura, tipos) e um juiz LLM
  quando exigir julgamento (legibilidade, adequação). Valide se a métrica acompanha o julgamento do
  especialista, ajuste e monitore se otimizá-la melhora o resultado real (evitando métricas que dá para
  "enganar").
- **Determinística × juiz LLM:**
  - *determinística* quando há gabarito, a propriedade é mensurável, a reprodutibilidade importa ou há
    milhares de casos;
  - *juiz LLM* quando é preciso nuance, há várias soluções válidas ou a saída é não estruturada ou
    multimodal;
  - *ambos:* filtrar com o barato e avaliar com o caro só o que passou, e validar o juiz contra a métrica
    objetiva.
- **Com referência × sem referência:**
  - *com:* comparação exata, "contém", aproximada;
  - *sem:* utilidade, clareza, eficiência;
  - *de processo:* chamou as ferramentas certas, na ordem certa, com os argumentos certos?
- **Formas de pontuar:**
  - nota única holística;
  - **comparação aos pares** ("qual das duas é melhor?"), mais confiável para qualidades subjetivas e
    ótima para comparar a versão nova com a anterior;
  - nota por dimensão, que indica o ponto fraco.
- **O próprio juiz precisa ser depurado** (p. 278–279). Exemplo do autor:
  - o juiz penalizava como "prolixa" a transparência das respostas multiagente (6,8 contra 7,9 da
    chamada direta). Com instruções corrigindo esse viés, foi para 9,3.
  - Houve também um erro de normalização de pesos no juiz composto.
  - **Lição:** registre a trajetória e a justificativa do juiz, inspecione quando o resultado parecer
    estranho e corrija o sistema *ou* a avaliação.
- **Modo mini e completo:** uma versão de ~2 min (1 tarefa por grupo) para iterar e outra de ~8 min para
  valer.
- **Resultado do estudo** (GPT-4.1-mini, 4 configurações × 4 grupos de tarefas):
  - nota geral: multiagente com seletor 9,3, agente com ferramentas 9,2, round-robin 9,2, chamada direta
    8,5;
  - raciocínio simples: **a chamada direta vence** (9,7);
  - tarefas com ferramentas: a chamada direta cai a 6,8 (3,2 na pesquisa de podcast, contra 9,0 de todos
    com busca);
  - planejamento e verificação: todos entre 8,6 e 9,6;
  - **custo: a chamada direta usa ~355 tokens por tarefa; o multiagente com seletor, ~15 mil (43×).**
  - **Conclusão:** a complexidade só se paga onde a tarefa exige ferramenta ou especialidade.
- **Benchmarks públicos ≠ a sua tarefa** (GAIA, SWE-bench, GPQA, HLE): eles dizem quem é melhor *em
  geral*, não no seu domínio.
  - **Contaminação:** as questões vazam para o treino e para a web.
  - Antídotos: conjuntos privados, problemas novos e desconfiar de resultados bons demais.
- **Exercícios sugeridos:**
  - conjunto de 5 a 10 tarefas do seu domínio que *discriminem* configurações;
  - um juiz específico do domínio, calibrado antes de escalar;
  - **regressão:** guardar os resultados com versão, configuração e data e alertar quando cair;
  - eficiência: quando 2× mais rápido justifica −0,5 ponto?

**→ No nosso projeto**
- **A E2 já seguiu esse capítulo sem saber:** as 278 perguntas com gabarito, as métricas determinísticas
  (hit@1, hit@5, MRR), os recortes (sintoma × causa, português × inglês, difícil), a comparação com linhas
  de base (e5 × bge-m3 × Qwen3, fichas × resumo × texto) e as ablações (overlap). Isso é um argumento
  forte na apresentação.
- **A próxima etapa deve começar pela avaliação, antes do agente.** Proposta de suíte para o copiloto:
  - *casos:* incidentes do danluu transformados em cenários (sintoma inicial + o que se sabe) com
    gabarito de causa, categoria e mitigação. As fichas viram o gabarito aqui, e é um ótimo uso para
    elas;
  - *determinísticas:* recuperou o incidente certo (já temos)? A categoria da causa bate? Todas as
    afirmações têm citação, e a citação existe no texto (como o `validar_fichas.py`)? Tokens, tempo,
    número de chamadas;
  - *juiz LLM:* a hipótese de causa é plausível e sustentada pelas evidências? A mitigação é acionável?
    O postmortem segue o template? Calibrar o juiz com uns 20 casos anotados à mão, inclusive pela Mari;
  - *processo:* o agente chamou a busca antes de afirmar algo? Pediu aprovação antes de uma ação?
- **Linhas de base obrigatórias:**
  - (a) LLM direto sem RAG;
  - (b) RAG + uma chamada só;
  - (c) agente com ferramentas;
  - (d) multiagente.
  - Só subir de nível se a avaliação mostrar ganho, como no estudo do livro.
- **Cuidado com contaminação:** os postmortens do danluu são públicos e famosos, e o LLM pode "saber" a
  causa sem usar o RAG. A linha de base (a) mede isso. Vale ter casos com detalhes alterados ou internos.
- Manter o **modo mini e o completo**, e guardar o histórico dos resultados para pegar regressões (como o
  `RESULTADOS.md`, mas com data e configuração).

## Cap. 11 — Otimizando sistemas multiagentes (p. 285–301)  ★ checklist de produção

**Ciclo:** medir (avaliação) → analisar (onde falhou) → ajustar → validar (rodar de novo) → repetir. O
difícil não é o ciclo, é saber **qual ajuste rende mais**.

**Dois níveis de parâmetro:**
- **Do sistema de agentes** (onde está a maior alavanca com o menor esforço): instruções, ferramentas,
  memória, escolha do modelo, padrão de orquestração, condições de parada, delegação a humanos.
- **Do modelo** (pesos, treino): só no fim. Os motivos para chegar a ele são três: custo e latência (um
  modelo pequeno sai de 20 a 30× mais barato), privacidade (não pode usar modelo de terceiros) ou ganhos
  decrescentes no nível de cima.

**Ordem:** instruções e ferramentas primeiro → o modelo certo (modelos de fronteira seguem instruções
muito melhor; *modelos de raciocínio às vezes pioram no papel de orquestrador*) → padrão e parada.

**As 10 falhas típicas em produção** (o autor sugere usar como checklist de diagnóstico):
1. **Instruções vagas.** Escreva-as como uma descrição de cargo (comportamento, quando usar cada
   ferramenta, restrições, formato, erros) e **amplie a cada falha que a avaliação revelar**. Um bom
   prompt pode ter páginas.
2. **Modelo pequeno sem otimização.** O caminho é:
   1. começar com um modelo de fronteira para ter a linha de base;
   2. otimizar o sistema;
   3. só então considerar:
      - *roteamento* (o simples vai para o modelo pequeno; ~90% do desempenho com ~15% do custo);
      - *destilação* (treinar o pequeno nas saídas do grande);
      - *cascata* (tenta o pequeno e escala se falhar).
   - Ajuste fino só se as falhas restantes forem de domínio raro, de lógica de negócio contraintuitiva
     ou de cauda longa, ou por eficiência quando já se está no topo. As trajetórias registradas viram
     dados de treino.
3. **Instruções não casadas com o modelo.** Prompts não são portáveis nem entre versões do mesmo modelo.
   Mantenha instruções por família de modelo, versionadas junto com a escolha, e faça teste A/B **ao
   trocar de modelo**.
4. **Ferramentas ruins.** **Melhor 10 ferramentas excelentes que 50 medíocres** (muitas ferramentas
   confundem e ocupam contexto). Elas devem devolver erros estruturados em vez de quebrar, documentar
   limites e o quão atuais são os dados, ter repetição com espera crescente e validar a própria saída.
   Foco em operações do domínio.
   - Duas ferramentas centrais úteis: uma para "pensar" (raciocínio explícito; a Anthropic relatou
     +54%) e uma de "status da tarefa", que obriga o agente a declarar se terminou e por quê.
5. **Não sabe quando parar.** Antipadrão: parar quando aparecer "TASK_COMPLETE", mas as instruções nunca
   pedem que o agente escreva isso. **Alinhe a parada com as instruções**, ou use a ferramenta de status.
   Calibre pelos dados: média de passos nos casos de sucesso, distribuição de tokens, tipo de parada.
   **É melhor parar cedo com um resultado parcial que gastar numa trajetória divergente.**
6. **Padrão errado.** Mais autonomia não é melhor. Prototipe com workflow, meça, ache o gargalo e **torne
   autônomo só o trecho que precisa**. Antipadrão: um orquestrador por IA para uma sequência linear (3 a
   5× o custo sem ganho). Híbrido é o normal: plano no topo, workflows nas subtarefas.
7. **Não aprende (memória).** Memória custa latência e dinheiro. Meça se ela melhora a taxa de acerto,
   quantas lembranças bastam e quais tarefas ganham com ela. Nem todo agente precisa.
8. **Sem metacognição.** Laços de reflexão (planejar → executar → avaliar → replanejar) evitam insistir
   num caminho que está falhando. O "registro" do Magentic-One deu até +31%. Custa chamadas a mais,
   então meça.
9. **Sem avaliação.** "Não dá para otimizar o que não se mede." O mínimo é uma lista de tarefas com a
   saída esperada + um juiz + rodar as versões.
10. **Não sabe quando delegar a um humano.** Para o agente, todas as ações parecem iguais. Classifique
    por risco:
    - baixo (só leitura) → executa sozinho;
    - alto (irreversível ou caro) → sempre pedir aprovação.
    - Calibre pelos dados: **se mais de 95% dos pedidos são aprovados, a política está cautelosa
      demais**; se casos de risco passam, está frouxa.
- **Bônus: provavelmente você não precisa de multiagente.** Só use se a tarefa for decomponível, pedir
  especialidades diferentes, tiver contexto extenso **e** exigir adaptação. Um agente único bem feito
  costuma vencer um multiagente mal feito.

**→ No nosso projeto**
- Usar as 10 falhas como **checklist de revisão** de cada versão do copiloto.
- **O que já se aplica:**
  - *(4) ferramentas:* poucas e boas, como `buscar_incidentes` (que já existe, com saída estruturada),
    `ler_trechos(doc_id)`, `consultar_metricas`, `consultar_logs`. Sem um "executar comando" genérico;
  - *(5) parada:* uma ferramenta ou campo de status ("hipótese suficiente / falta dado") alinhada ao
    prompt;
  - *(10) risco:* consultar = baixo; sugerir mitigação = médio (mostra, não executa); executar = alto
    (aprovação ou fora do escopo).
- **Escolha do LLM** (decisão pendente da dupla: a Mari usou o GPT-OSS-20B via NVIDIA NIM):
  - começar com um modelo forte para estabelecer a linha de base;
  - só depois testar um modelo menor ou local com a mesma avaliação;
  - manter os **prompts por modelo**, versionados.
- *(6) padrão:* workflow primeiro; autonomia só no nó de investigação, se a avaliação mostrar ganho.
- *(1) instruções:* tratar o prompt do copiloto como o prompt das fichas (que chegou à v2.21), ampliado a
  cada erro recorrente. Já temos a disciplina e o histórico disso na E2.

## Cap. 12 — Protocolos para agentes distribuídos (p. 302–324)

- **Distribuído** = agentes e ferramentas rodando em outro processo, máquina, região ou organização.
  Ganha-se escala independente, isolamento e tolerância a falhas; paga-se em complexidade de comunicação.
- **Os problemas são os clássicos de sistemas distribuídos** (descoberta, comunicação, falhas,
  coordenação), mas a lógica de decisão sai da infraestrutura e vai para a aplicação (o modelo decide).
  Paralelos:
  - fila de mensagens → delegação de tarefa;
  - descoberta de serviço → descoberta de agente por capacidade;
  - repetição com *circuit breaker* → sessão retomável (tarefas de horas não podem só "tentar de novo");
  - API gateway → orquestrador.
- **Quatro necessidades de agentes distribuídos:** streaming de progresso, retomada após desconexão,
  durabilidade do resultado (sobrevive a reinícios, com referência para consultar depois) e interação
  no meio da execução.
- **MCP (Model Context Protocol, Anthropic, nov./2024):**
  - **padroniza o acesso de LLMs a ferramentas, recursos e prompts.** Escreve-se um servidor e ele
    funciona em qualquer *host* (Claude Desktop, Cursor, VS Code, aplicações próprias), com catálogo
    central e autenticação centralizada;
  - **arquitetura:** *host* (a aplicação, que decide o que chamar) → *client* (uma conexão por servidor)
    → *server* (expõe as capacidades);
  - **transporte:** stdio (subprocesso local) ou HTTP com streaming (remoto);
  - **recursos que o tornam "agêntico":** notificações de progresso, sessão retomável com replay de
    eventos, links para recursos duráveis, *elicitation* (o servidor pede dados ao usuário) e *sampling*
    (o servidor pede uma resposta do LLM do cliente; quem controla o modelo e o contexto é o cliente, e o
    servidor não guarda chaves);
  - **na prática:** um adaptador que transforma cada ferramenta MCP numa ferramenta comum do agente, com
    prefixo no nome para evitar conflitos e gestão do ciclo de vida da sessão;
  - **segurança:** OAuth 2.1 com PKCE no transporte HTTP, credenciais do ambiente no stdio, e **proibido
    repassar o token do cliente para serviços de trás** (evita o ataque *confused deputy*).
- **A2A (Agent-to-Agent, Google, abr./2025, hoje na Linux Foundation):**
  - colaboração entre **agentes autônomos de organizações diferentes**, como caixas-pretas;
  - **descoberta:** um *Agent Card* em `/.well-known/agent-card.json` com capacidades e autenticação;
  - **elementos:** Mensagem, **Tarefa** (com ID e estados: submetida, em andamento, aguardando entrada,
    aguardando autenticação, concluída, falhou, cancelada, recusada) e Artefato (o resultado);
  - um `contextId` liga tarefas relacionadas;
  - HTTP + JSON-RPC + SSE, com webhooks para tarefas muito longas.
- **Contexto entre vários agentes distribuídos:** ou (1) o **orquestrador funciona como hub central**,
  coletando os resultados e passando adiante (o padrão para a maioria dos casos), ou (2) os resultados vão
  para um **armazenamento compartilhado** e circulam só as referências (para dados grandes).
- **Como escolher:**
  - **MCP para orquestração composta:** você controla cada chamada e o que cada ferramenta recebe, e
    depura passo a passo;
  - **A2A para delegar uma tarefa inteira** a um agente de outra organização ou de um marketplace;
  - os dois juntos é comum: MCP dentro de casa, A2A para fora;
  - lembrete do cap. 1: distribuir cedo demais costuma ser excesso de engenharia.

**→ No nosso projeto**
- **Não começar distribuído:** tudo num processo só (LangGraph + ferramentas Python).
- **MCP é o caminho natural para expor a busca da E2 como ferramenta reutilizável:** um servidor MCP
  `incidentes` com `buscar_incidentes` e `ler_incidente`, usado pelo copiloto e também pelo Claude
  Desktop/Cursor/VS Code de quem estiver de plantão. É um bom "extra" de demonstração, com custo baixo
  (FastMCP), mas fica para depois do caminho principal.
- Se a telemetria (métricas/logs, como a Prometheus/Loki do otel-demo) entrar, ela pode vir como
  servidores MCP prontos da comunidade, sem integração caseira.
- A2A só faria sentido se outra equipe tivesse um agente próprio (por exemplo, um "agente de mudanças"
  do time de plataforma). Fora do escopo agora.
- **Segurança:** se houver servidor MCP remoto, usar autenticação e nunca repassar tokens. A ferramenta
  de busca é só leitura, então o risco é baixo.

## Cap. 13 — Ética e IA responsável em sistemas multiagentes (p. 325–343)

**O que muda em relação à ética de ML tradicional**, em quatro dimensões:
- *Controlabilidade:* o comportamento do modelo vem de dados na escala da web, então curar os dados já
  não controla o comportamento. Foram observados "fingir alinhamento" (comportar-se quando vigiado e
  não quando não vigiado) e comportamentos nocivos sob ameaça em testes.
  - **Bajulação:** otimizar por sinais de satisfação do usuário cria um "modelo que concorda com tudo".
    Exemplo: em 2025, uma atualização do GPT-4o foi revertida porque os testes A/B pareciam bons, mas
    especialistas sentiram que algo estava errado.
  - **Lições:** sinal de produto ≠ sinal de qualidade; desvio de comportamento bloqueia o lançamento; a
    intuição de especialistas pega o que as métricas não pegam.
- *Capacidade de ação:* o agente não sinaliza para alguém decidir, ele investiga e age em vários passos.
- *Escopo:* agentes generalistas atuando em várias profissões.
- *Verificação:* testar cada componente não garante o comportamento do sistema, e o comportamento
  emergente é imprevisível.

**Ritmo:** o horizonte de tarefas que os modelos completam com 50% de sucesso **dobra a cada ~7 meses**
(METR): de segundos (GPT-2) a mais de 2 horas (GPT-5). Em 1.320 tarefas profissionais, o melhor modelo
empatou ou venceu especialistas em ~48% dos casos. A pressão econômica favorece a velocidade em vez da
validação.

**Desafios sociais:**
- *Ruído agêntico:* plataformas pensadas para humanos dos dois lados quebram quando um lado acelera com
  agentes (centenas de candidaturas por dia contra recrutadores humanos). Acelerar os dois lados também
  pode só gerar mais volume, sem bem-estar. Avalie o impacto no outro lado, não só o ganho próprio.
- *Impacto ocupacional:* agentes vão bem em tarefas de *pouco contexto* e mal nas de *muito contexto*
  organizacional (um terceiro leva de 5 a 18× mais tempo que o mantenedor na mesma tarefa). Isso tende a
  automatizar o trabalho sem contexto e a aumentar o peso da supervisão especializada.
- *Responsabilidade distribuída* (o problema das "muitas mãos"): cada peça funcionou, mas o conjunto
  violou uma regra. É preciso **definir os responsáveis antes de implantar**, por categoria de decisão.
- *Riscos emergentes:* coordenação não programada. Mitigar com monitoramento de padrões inesperados,
  limites na complexidade das interações e **disjuntores** que param a execução quando o comportamento
  sai dos limites.

**Segurança quando o agente age:**
- **O risco cresce com a capacidade de ação.** Um agente que só lê tem raio de dano pequeno.
- **Regra dos Dois** (Meta, 2025): numa mesma sessão, o agente deve ter **no máximo duas** destas três
  propriedades:
  - **(A)** processar entrada não confiável;
  - **(B)** acessar sistemas sensíveis ou dados privados;
  - **(C)** mudar estado ou se comunicar para fora.
  - Se precisar das três, não pode agir sozinho: exige aprovação humana ou validação confiável.
- **Agentes quebram a premissa de "serviços sem iniciativa":** diante de um erro, o agente pode procurar
  e usar credenciais de outro serviço para "resolver" a tarefa. Mude a premissa para "o agente vai achar
  e tentar usar tudo o que estiver acessível". Defesas:
  - containers isolados;
  - cofre de segredos em vez de variáveis de ambiente;
  - **ferramentas mínimas** (nada de shell ou sistema de arquivos genéricos);
  - infraestrutura separada.
- **Defesa em camadas via middleware:**
  1. filtrar a entrada (padrões de injeção; não pega técnicas novas, então é só a primeira camada);
  2. autorizar ferramentas (aprovação humana ou política automática: aprovar o seguro, rejeitar o
     perigoso, mandar o resto para uma pessoa);
  3. validar a saída (credenciais, volume suspeito).

**Checklist de implantação:**
- *isolamento e menor privilégio;*
- *auditoria:* registrar todas as ações e aprovações, detectar anomalias, guardar para perícia;
- *limites para supervisão humana:* ações irreversíveis, comunicação externa, excesso de consultas,
  disjuntor por taxa de erro;
- *controle de entrada e saída:* preferir saída estruturada para reduzir injeção via resultado de
  ferramenta;
- *avaliação de comportamento:* bajulação, desvio de comportamento ao longo do tempo, critérios de
  bloqueio de lançamento;
- *revisão periódica:* tirar ferramentas desnecessárias e testar com entradas adversariais.

**→ No nosso projeto**
- **Aplicar a Regra dos Dois ao copiloto:**
  - (A) ele lê conteúdo não confiável: postmortens baixados da web e, no futuro, logs e alertas;
  - (B) pode acessar dados internos (métricas, logs);
  - (C) **não deve mudar estado sozinho.**
  - Configuração alvo **[AB]:** lê e consulta, mas qualquer ação ou comunicação externa passa por
    aprovação humana. Isso justifica no relatório por que o copiloto *sugere* e não *executa*.
- **Injeção via RAG é real:** um postmortem poderia conter "ignore as instruções…". Mitigação:
  - marcar no prompt o conteúdo recuperado como *dados*, não instruções;
  - saída estruturada;
  - nenhuma ferramenta de ação disponível no mesmo agente que lê esse conteúdo.
  - É a continuação natural do cuidado da E2 com os dados não confiáveis (`python -I`, pastas
    isoladas).
- **Bajulação no contexto de incidentes:** o engenheiro sob pressão sugere uma causa e o agente
  concorda. A avaliação deve ter casos em que a hipótese do usuário está errada e medir se o agente
  discorda com base na evidência.
- **Responsabilidade:** o postmortem gerado é um *rascunho*, e o responsável pelo incidente continua
  sendo uma pessoa. Deixar isso explícito na interface e nos documentos.
- **Ruído agêntico:** relevante se o copiloto abrir tickets ou mandar mensagens automaticamente. Não
  automatizar isso sem limite.

## Cap. 14 — Respondendo perguntas de negócio com dados não estruturados (p. 345–364)

**Caso:** "quantas startups da YC constroem agentes de IA de verdade?", a partir de 5.622 descrições
curtas de empresas.
- **As dificuldades:**
  - polissemia ("agent" pode ser agente de seguros);
  - marketing inflado ("AI-powered" sem IA de verdade);
  - nuance (agente autônomo × uma chamada de API);
  - escala e custo.
- **Por que workflow e não agentes autônomos:** a solução é conhecida e decomponível em passos testáveis.
- **Quatro etapas em sequência:**
  1. **Carregar com cache:** validade por tempo (TTL de 7 dias), atualização forçada opcional e **escrita
     atômica** (grava num arquivo temporário e renomeia, para nunca deixar um arquivo pela metade).
  2. **Pré-filtrar barato:** regex com fronteira de palavra, sem diferenciar maiúsculas e exigindo "IA
     **e** agente". **Recall alto no filtro barato, precisão no LLM caro.** O filtro reduziu de 5.622 para
     1.795 (~32%).
  3. **Análise estruturada por LLM:**
     - schema Pydantic com `is_about_ai` (valida o filtro), domínio de uma **lista fechada** (para não
       inventar categorias que quebrariam a agregação), subdomínio, `is_agent` e **justificativas
       separadas** para cada decisão (explicar reduz alucinação e ajuda a depurar);
     - **sem campo de confiança:** o LLM dava 0,9 para respostas erradas, e booleanos com justificativa
       foram mais confiáveis;
     - processamento em lotes (limites de taxa), **checkpoint por lote** (perde no máximo um lote) e custo
       acompanhado em tempo real;
     - o prompt evoluiu iterando: rodar, revisar algumas dezenas de amostras à mão, corrigir.
  4. **Agregar e gerar os insights:** contagem por domínio, métricas de custo e exportação em JSON.
- **Testar cada etapa isolada:**
  - o filtro com exemplos conhecidos ("insurance agent" não deve passar);
  - o LLM com *mocks* (sem custo);
  - o checkpoint com diretórios temporários.
- **Resultado:**
  - 1.750 empresas (31%) são de IA de verdade, e 765 delas (44%) constroem agentes;
  - **o filtro por palavra "agent" pegaria só 53% dos agentes reais**, o que mostra o valor da etapa
    com LLM;
  - ~1,7 milhão de tokens, ~US$ 56.
- **O padrão serve para outras perguntas:** feedback de clientes, inteligência competitiva, revisão de
  literatura, compliance. **Limitações:** a qualidade das descrições, só um modelo usado, um retrato num
  momento só.

**→ No nosso projeto**
- **Esse capítulo descreve quase exatamente o processo das fichas da E2:**
  - schema com campos fechados (categoria da causa) e campos com evidência;
  - lotes de 10 com checkpoint;
  - o prompt iterado com revisão de amostras (até a v2.21);
  - validação automática (trechos literais).
  - Bom para citar como prática de referência.
- **Duas lições a incorporar:**
  1. **Desconfiar de campos de "confiança" gerados pelo LLM.** Na hipótese de causa do copiloto,
     preferir um booleano ("sustentada pela evidência? sim/não") + justificativa + citações, em vez de
     "confiança: 0,85". Se precisar de uma nota, calibrar contra a avaliação.
  2. **Filtro barato com recall alto antes do caro.** Na busca, isso já existe: a etapa 1 vetorial é
     barata e o LLM só lê os 5 primeiros. Para logs no futuro, filtrar por regra (janela de tempo,
     serviço, nível de erro) antes de mandar ao LLM.
- **Escrita atômica e cache com validade** valem para os artefatos do pipeline. Hoje os scripts
  sobrescrevem os arquivos diretamente; é uma melhoria simples se algum dia virar serviço.

## Cap. 15 — Construindo um agente de engenharia de software (p. 365–377)

O caso oposto ao cap. 14: a solução **não** é conhecida de antemão, então se usa o padrão autônomo
**agente + ferramentas + memória**. É a base de Copilot Agent Mode, Cursor, Claude Code, Codex e
Windsurf. **O agente é tão capaz quanto as ferramentas que tem e as instruções que guiam o uso delas.**

- **Como escolher as ferramentas:** imagine orientar um desenvolvedor júnior inteligente. O LLM já sabe
  programar; falta a ele agir no ambiente. Cinco categorias:
  - **arquivos:** ler, escrever (sobrescrever, *substituir um trecho* ou inserir uma linha), listar e
    buscar, sempre restritos a um diretório de trabalho;
    - a edição cirúrgica (substituir um trecho) evita reescrever e estragar o resto do arquivo;
  - **execução:** REPL Python e shell com timeout ("escrever código sem rodar é cozinhar sem provar");
  - **memória:** o agente guarda padrões e decisões entre tarefas;
  - **metacognição:** uma ferramenta de "pensar" (rascunho sem ação) e uma lista de tarefas (escrever e
    ler), que é o registro do progresso que os ganchos podem conferir.
- **O prompt faz a diferença:** "você pode escrever código, use as ferramentas" dá resultado ruim. O bom
  prompt é organizado em **fases numeradas**:
  1. consultar a memória primeiro;
  2. planejar (pensar + lista de tarefas);
  3. executar tarefa por tarefa, testando logo e registrando as decisões;
  4. verificar (testes, lista toda concluída);
  5. concluir (**nunca parar com itens pendentes**; se travar, explicar o que falta).
  - Princípios: fluxo explícito, memória primeiro, registro de progresso, **critério de pronto
    explícito** (o ciclo termina quando o modelo para de chamar ferramentas, então um "pronto" vago faz
    o agente parar cedo) e orientação sobre o que fazer com erros.
- **Robustez da conclusão, em três degraus:**
  1. só o prompt (serve para tarefas curtas);
  2. lista de tarefas + um gancho determinístico que confere se está toda concluída (sem chamada extra);
  3. um juiz LLM que avalia pelas evidências das ferramentas chamadas (o mais robusto para tarefas
     abertas).
- **Experimento** (revisar um repositório de 44 arquivos Python, GPT-4.1-mini):
  - sem gestão de contexto: 916 mil tokens de entrada, qualidade 6,0;
  - orçamento de 8 mil + gancho de fim: **55% de leituras repetidas** (thrashing), qualidade 4,0;
  - o mesmo sem o gancho: 15% de repetição, qualidade 5,5;
  - orçamento de 15 mil: 46% de repetição;
  - isolamento com subagentes: 119 mil tokens, 0% de repetição, qualidade 4,5.
  - Nenhuma configuração leu todos os 44 arquivos.
  - **Lições:**
    - o padrão saudável é o "dente de serra" (o contexto cresce, é compactado, cresce de novo);
    - um orçamento apertado demais gasta mais em releitura do que economiza;
    - ganchos e compactação interagem (o gancho manda continuar, mas o agente já esqueceu o que fez);
    - **regra prática: orçamento de 2 a 3× o conjunto de trabalho de cada passo; se as leituras
      repetidas passarem de 15%, o orçamento está apertado.**
- **Valores práticos:**
  - limite de iterações: 10–20 para scripts simples, 30–50 para projetos com vários arquivos, 50–100
    para revisões grandes;
  - orçamento de compactação a partir de 25–50 mil tokens;
  - menos de 10 chamadas de ferramenta: não precisa compactar.
- **Exercícios:** ablação do prompt (tirar uma seção e medir) e varredura do orçamento de tokens.

**→ No nosso projeto**
- **A estrutura em fases vale para o prompt do agente de investigação:**
  1. consultar o histórico (a busca da E2) primeiro;
  2. planejar as hipóteses a checar;
  3. coletar evidências por hipótese;
  4. verificar se cada afirmação tem fonte;
  5. concluir só com o critério atendido; senão, dizer o que falta ("preciso dos logs do serviço X").
- **Critério de pronto explícito** para o copiloto: "hipótese com pelo menos N evidências citadas" ou
  "declarar que não há evidência suficiente". Com um gancho de fim que confere isso de forma
  determinística, sem LLM, no estilo do `validar_fichas.py`.
- **Ferramenta de "pensar" e lista de tarefas** são baratas e ajudam na investigação, com o rastro
  visível para o engenheiro.
- **Nossas tarefas são curtas:** poucas chamadas de ferramenta por pergunta, e o retorno da busca é
  compacto (5 incidentes × 2 trechos). Provavelmente não precisaremos de compactação no início. Se o
  agente começar a ler postmortens inteiros, medir a taxa de leituras repetidas.
- **Ablação do prompt** entra na avaliação: tirar a fase "consultar o histórico primeiro" e ver quanto
  cai.

## Epílogo — Olhando para frente (p. 378–383)

- **A história do AutoGen como lição de arquitetura.** A v0.2 era síncrona, a "troca de mensagens" era
  uma lista compartilhada em memória e o código era extraído do texto gerado, o que falhava muito com
  modelos menores. A v0.4 virou uma arquitetura assíncrona de eventos, no **modelo de atores**, com duas
  APIs: o *Core* (controle explícito) e o *AgentChat* (atalhos de alto nível). A maioria dos
  desenvolvedores ficou com os atalhos, e a capacidade distribuída quase não foi usada. Depois ele se
  juntou ao Semantic Kernel no **Microsoft Agent Framework**.
- **A tendência central:** à medida que os modelos melhoram, o "andaime" em volta deles fica mais leve.
  No início eram duas páginas de instruções para coordenar e gerar JSON; hoje saída estruturada e uso de
  ferramentas são nativos. O andaime tende a virar **pontos de controle** (supervisão humana, avaliação,
  monitoramento). **Projete esperando que o modelo melhore e que responsabilidades mudem de lugar.**
- **Fases previstas:**
  1. *agora:* domínio dos workflows (confiáveis, com engenharia conhecida);
  2. adoção ampla dos padrões autônomos (onde o autor vê mais potencial de crescimento);
  3. integração: assistentes que escolhem sozinhos workflow para o que é crítico e autonomia para o que
     é exploratório, mais **marketplaces de agentes** com especificações declarativas e portáveis (como
     Dockerfile ou YAML do Kubernetes).
- **Mensagem final:** sistemas multiagentes não são mágica, são software com componentes de IA. Precisam
  do mesmo rigor de engenharia, mais práticas novas para lidar com comportamento emergente. Às vezes um
  script é melhor; às vezes um agente só vence vários. **Os princípios que ficam: decomposição da tarefa,
  avaliação, observabilidade, supervisão humana e implantação responsável.**

*(Glossário, p. 385–394, e referências, p. 395–400: não resumidos. O glossário define os termos já
cobertos acima.)*

---

## Síntese para o Incident Copilot (próximas etapas)

**1. A arquitetura mais simples que resolve** (caps. 1, 2, 11). Começar como **workflow em LangGraph**,
com autonomia só onde a avaliação provar que ela compensa:

```
entrada ─► roteador (tipo de pedido)
            ├─ diagnóstico em andamento ─► busca (E2) ─┬─► hipótese de causa ─► [aprovação] ─► sugestão de mitigação
            │                         consulta de     ─┘   (com citações)
            │                         telemetria (paralelo)
            ├─ redação de postmortem ──► busca + rascunho ─► juiz: seções completas e citadas? ─► rascunho
            └─ pergunta sobre histórico ─► busca ─► resposta citada
```

O nó "hipótese de causa" é o único candidato a virar um agente com ciclo próprio (padrão baseado em
plano com avaliação por passo, cap. 7), com parada composta (iterações **ou** tokens **ou** evidência
suficiente).

**2. Avaliação antes do agente** (cap. 10, ★):
- montar a suíte de cenários (incidentes do danluu como "sintoma inicial → causa, categoria e
  mitigação"), usando as **fichas como gabarito**;
- métricas determinísticas (recuperação, categoria certa, citações válidas, tokens, tempo) + juiz LLM
  calibrado com ~20 casos anotados à mão;
- **linhas de base** (LLM sem RAG, RAG com uma chamada, agente, multiagente);
- atenção à **contaminação** (os postmortens são públicos).

**3. Ferramentas poucas, específicas e com saída estruturada** (caps. 4, 11):
`buscar_incidentes` (já existe no `busca.py`), `ler_incidente`, depois `consultar_metricas` e
`consultar_logs`. Sem shell genérico. Erros devolvidos como dados.

**4. Saída estruturada em tudo** (caps. 4, 7, 14): hipótese, mitigação e postmortem como schemas.
**Nada de "confiança 0–1" gerada pelo LLM:** usar um booleano + justificativa + citações.

**5. Humano no ciclo e segurança** (caps. 3, 4, 13):
- configuração **[AB] da Regra dos Dois:** lê conteúdo não confiável e dados internos, mas não age
  sozinho;
- ações = aprovação (o `interrupt` do LangGraph + checkpointer em Postgres);
- conteúdo do RAG tratado como dado, não como instrução;
- testar a **bajulação** (o usuário propõe uma causa errada).

**6. Observabilidade desde o primeiro dia** (caps. 3, 4, 10): OpenTelemetry/LangSmith, streaming dos
passos para a interface, rastros guardados para depurar e para virar casos de avaliação. Conteúdo só em
desenvolvimento.

**7. Interface** (cap. 8): FastAPI + SSE, estado salvo por `thread_id`; Streamlit ou Chainlit para a
demonstração. Na tela vazia, exemplos que funcionam bem e um aviso de "não achei incidente parecido".

**8. Otimização por dados** (cap. 11): usar as 10 falhas como checklist; o prompt evolui a cada erro
recorrente (como as fichas, até a v2.21); configuração versionada para ablação; um modelo forte primeiro
e um menor ou local só depois, com a mesma suíte.

**9. Extras opcionais:** um servidor **MCP** com a busca de incidentes (cap. 12), para uso direto no IDE
do plantonista.

**O que a E2 já tem alinhado com o livro** (bom para a apresentação):
- avaliação com gabarito, recortes, linhas de base e ablações (cap. 10);
- pipeline como workflow, com validação e reaproveitamento parecido com checkpoint (cap. 6);
- extração estruturada com schema, lotes e prompt iterado, exatamente o padrão do cap. 14;
- proveniência (trechos literais com `url`), que atende ao princípio de observabilidade e proveniência
  do cap. 3;
- tratamento de dados não confiáveis (cap. 13).
