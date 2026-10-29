# E1.1 — Documento de entendimento do problema

**Projeto 4 — Incident Copilot: Assistente Inteligente de Incidentes e Post-Mortems**  
**Entrega:** 1.1 — Entendimento do problema de negócio  


## 1. Resumo

O **Incident Copilot** é uma proposta de assistente para **apoiar, e não substituir, a investigação humana**. É um sistema multi-agente que recebe a descrição de um incidente em andamento (texto livre ou alerta estruturado), busca post-mortems e runbooks de incidentes parecidos e devolve um **diagnóstico diferencial ranqueado.** Cada causa provável vem com a remediação, a fonte original e o nível de confiança.

O objetivo é **reduzir o tempo de diagnóstico** dos incidentes, que hoje é a maior parte do MTTR, e assim contribuir para as metas de SLA da Stratus.

## 2. Contexto e problema

### 2.1 Situação atual (hipótese de negócio)

Em um processo tradicional de investigação, a pessoa responsável pode precisar:

1. Interpretar alertas, relatos e sinais disponíveis sobre a ocorrência atual.
2. Buscar manualmente incidentes parecidos e materiais de referência.
3. Distinguir semelhança superficial de mecanismo de falha efetivamente sustentado por evidências.
4. Registrar hipóteses concorrentes, lacunas de informação e próximos passos.
5. Retomar a investigação conforme chegam novas evidências e preparar uma comunicação clara.

Essas atividades podem ser demoradas, sobretudo quando post-mortems não possuem uma forma consistente de pesquisa ou quando o contexto do incidente está incompleto.

> **Limite da evidência:** o projeto ainda não dispõe de medições reais do tempo gasto pelas equipes, taxa de erros ou volume de incidentes em uma organização específica. Portanto, os pontos acima descrevem o problema a validar, e não um diagnóstico quantitativo de uma operação real da Dell.

### 2.2 Dor central

**Encontrar, interpretar e aplicar conhecimento histórico confiável durante a investigação de um incidente, sem confundir incidentes similares com prova da causa raiz atual.**

### 2.3 Consequências potenciais

- Maior tempo para localizar casos históricos relevantes.
- Perda de contexto ao alternar entre documentos e atualizações da investigação.
- Hipóteses sem indicação explícita de evidências favoráveis, contrárias ou ausentes.
- Repetição de trabalho quando uma análise precisa ser retomada.
- Relatórios preliminares inconsistentes ou excessivamente conclusivos.

## 3. Quem são os usuários

| Perfil | Papel no processo | Necessidade principal |
|---|---|---|
| **Usuário primário — analista de operações, SRE ou engenheiro de suporte/infraestrutura** | Investiga incidentes e avalia hipóteses | Localizar rapidamente referências históricas, entender possíveis mecanismos e decidir o que investigar a seguir |
| **Usuário secundário — responsável pelo incidente / liderança técnica** | Acompanha andamento, riscos e comunicação | Receber uma síntese rastreável do que se sabe, do que ainda é incerto e das ações sugeridas |
| **Usuário eventual — engenheiro de desenvolvimento ou especialista de plataforma** | Contribui com informações técnicas e valida interpretações | Acrescentar evidências, contestar hipóteses e consultar as fontes recuperadas |

**Premissa de uso:** um profissional humano continua responsável por validar o diagnóstico e decidir qualquer ação operacional. Os perfis são propostos para o MVP e ainda devem ser confirmados com usuários reais.

## 4. Objetivo e resultados esperados

### 4.1 Objetivo principal

Apoiar a **triagem investigativa e a elaboração de diagnósticos preliminares** de incidentes de infraestrutura e aplicações com recuperação de conhecimento histórico, rastreabilidade das fontes e comunicação explícita da incerteza.

### 4.2 Resultados funcionais esperados

- Receber uma descrição de incidente ou alerta e validar os dados de entrada.
- Estruturar o contexto atual (sintomas, ambiente, impacto e informações fornecidas), sem inventar observações.
- Recuperar trechos pertinentes de post-mortems aprovados.
- Produzir hipóteses priorizadas, distinguindo observações atuais, paralelos históricos e inferências.
- Explicar a relação entre hipóteses e evidências; indicar limitações e perguntas ainda abertas.
- Refinar a busca dentro de um limite definido quando a primeira recuperação for insuficiente.
- Solicitar informações adicionais e retomar uma investigação por `incident_id`.
- Produzir um relatório que possa ser revisado pelo profissional responsável.

### 4.3 O que constitui sucesso para o usuário

Uma resposta útil não precisa necessariamente fornecer uma causa raiz definitiva. Ela deve permitir que o usuário **avance com segurança**: conhecendo hipóteses plausíveis, suas evidências, o que falta verificar e os documentos usados como referência. Uma conclusão **inconclusiva e fundamentada** é preferível a uma conclusão assertiva sem suporte.

## 5. Escopo do MVP e restrições

### 5.1 Incluído

- Entrada do incidente por interface/API, conforme contrato a ser definido na E1.4.
- Síntese inicial por LLM, sem tratá-la como agente independente.
- **Dois agentes:** (1) pesquisador RAG e (2) analista de diagnóstico.
- Orquestração predefinida com condições, refinamento limitado e possibilidade de pausa/retomada.
- Recuperação documental sobre **20 post-mortems públicos aprovados editorialmente** na E1.3.
- Relatório com fontes, hipóteses e incertezas.

### 5.2 Fora do escopo inicial

- Consulta automática em tempo real a logs, métricas, traces ou sistemas de observabilidade.
- Runbooks reais como fonte RAG já disponível: **não foram curados no corpus inicial**.
- Execução automática de comandos de remediação, mudanças em infraestrutura ou fechamento automático de incidentes.
- Garantia de diagnóstico correto ou descoberta da causa raiz em todos os casos.
- Substituição de políticas de incident management, escalonamento e revisão humana.

As informações atuais sobre o incidente são fornecidas pelo alerta ou usuário. Os post-mortems históricos servem para apoiar a investigação, **não para provar** que o mesmo mecanismo causal ocorre novamente.

## 6. Jornada do usuário — cenário representativo

1. Um alerta ou usuário informa sintomas e contexto de um incidente.
2. O sistema valida e normaliza a entrada; uma síntese por LLM organiza os fatos recebidos.
3. O pesquisador RAG busca ocorrências históricas relacionadas.
4. O analista compara referências e contexto atual, elaborando hipóteses fundamentadas.
5. A lógica de decisão verifica suficiência, necessidade de refinamento e limites da investigação.
6. Se faltarem dados do incidente atual, o sistema faz perguntas específicas e persiste a investigação para retomada.
7. Quando houver informação suficiente para uma avaliação — ou quando o limite for atingido — o sistema entrega relatório fundamentado, inclusive com resultado inconclusivo quando necessário.
8. O profissional consulta as fontes, valida as hipóteses e decide os próximos passos.

## 7. Métricas de sucesso e metodologia de avaliação

As métricas abaixo são **propostas de avaliação**, não valores observados. Os limiares numéricos devem ser definidos após obter uma linha de base, montar cenários de teste e acordar critérios com responsáveis pela capacitação.

| Dimensão | Indicador proposto | Como medir | Meta nesta fase |
|---|---|---|---|
| **Eficiência** | Tempo para encontrar referências históricas úteis | Comparar a execução assistida e a busca manual em cenários equivalentes | Definir baseline e buscar redução demonstrável |
| **Qualidade da recuperação** | Recall@K / MRR em conjunto de perguntas rotuladas | Comparar resultados do RAG com trechos relevantes identificados manualmente | Estabelecer patamar após piloto |
| **Rastreabilidade** | Percentual de afirmações sobre históricos sustentadas por referências verificáveis | Auditoria amostral de relatórios e trechos citados | Buscar cobertura integral das afirmações factuais sobre fontes |
| **Fidelidade e segurança** | Taxa de afirmações causais sem suporte ou de incerteza convertida em certeza | Revisão humana de casos de teste e respostas | Minimizar; tratar falhas graves como bloqueadoras |
| **Utilidade diagnóstica** | Avaliação humana de clareza, relevância e próximos passos | Rubrica aplicada por avaliadores técnicos | Definir critério de aprovação antes do teste |
| **Gestão de lacunas** | Percentual de cenários incompletos em que o sistema solicita dado útil ou responde inconclusivamente | Cenários com evidências deliberadamente insuficientes | Medir adequação, sem premiar perguntas desnecessárias |
| **Continuidade** | Sucesso da retomada via `incident_id` sem perda de contexto relevante | Teste de pausa, complementação e retomada | Critério funcional a validar |
| **Desempenho e custo** | Latência por investigação, número de chamadas LLM, tokens e custo estimado | Telemetria do protótipo | Estabelecer baseline e orçamento após implementação |

### 7.1 Desenho mínimo da avaliação

- Preparar um conjunto pequeno e documentado de cenários, incluindo casos com similaridade histórica clara, casos ambíguos e casos sem evidência suficiente.
- Definir respostas ou trechos de referência por revisão humana **antes** de comparar configurações.
- Executar os mesmos cenários manualmente (quando possível) e com o assistente, registrando duração e utilidade.
- Verificar se cada referência aponta para o documento correto e se o sistema preserva ressalvas editoriais.
- Registrar falhas, custo, limitações e critérios de aprovação; evitar generalizar resultados de uma amostra pequena.

**Nota metodológica:** encontrar um post-mortem semelhante não prova melhora de MTTR real. MTTR pode ser uma métrica futura em um piloto operacional com incidentes reais, mas não é um resultado atribuível ao MVP documental sem estudo controlado.

## 8. Riscos, premissas e mitigação

| Risco ou premissa | Consequência | Mitigação proposta |
|---|---|---|
| Corpus inicial pequeno (20 documentos) | Baixa cobertura de tecnologias ou tipos de falha | Expor ausência de evidências relevantes; avaliar expansão futura com curadoria |
| Semelhança sem equivalência causal | Diagnóstico equivocado | Separar fatos atuais, hipóteses e histórico; exigir fonte e revisão humana |
| Lacunas no conteúdo visual de oito documentos | Informações ausentes em gráficos/diagramas | Manter ressalvas editoriais; não inferir dados de figuras não extraídas |
| Certeza causal variável entre post-mortems | Afirmações indevidamente conclusivas | Preservar `causal_status`, notas e limitações na recuperação |
| Dados atuais insuficientes | Recomendações especulativas | Perguntar pelos dados faltantes; permitir relatório inconclusivo |
| Exposição de informações sensíveis em incidentes reais | Risco de confidencialidade | Definir autenticação, sanitização, acesso e política de retenção antes de uso real |
| Dependência de LLM/embeddings externos | Custos e requisitos de privacidade | Validar provedores e políticas; manter alternativa local se necessário |
| Ausência de integração com observabilidade no MVP | Diagnóstico baseado apenas no que foi informado | Comunicar explicitamente a origem e limitação das evidências |

## 9. Relação com as demais entregas da E1

| Entrega | Como contribui para a E1.1 |
|---|---|
| **E1.2 — Arquitetura de agentes** | Define dois agentes, fluxo predefinido, refinamento, pausa e retomada |
| **E1.3 — Mapeamento dos dados** | Valida o corpus inicial de 20 post-mortems e documenta limites e proveniência |
| **E1.4 — Definição do stack técnico** | Propõe LangGraph, chunking hierárquico, embeddings e PostgreSQL/pgvector; API ainda sob definição da Mari |
| **E1.5 — Organização do repositório** | Estrutura artefatos e documentação, ainda sujeita ao fechamento da entrega |

## 10. Critérios de aceite da E1.1

| Critério | Evidência no documento | Situação |
|---|---|---|
| Problema de negócio explicitado | Seções 1 e 2 | Atendido em nível de proposta |
| Público-alvo identificado | Seção 3 | Atendido; perfis a validar |
| Dor principal definida | Seção 2.2 | Atendido |
| Resultado esperado descrito | Seção 4 | Atendido |
| Escopo e limites definidos | Seção 5 | Atendido |
| Métricas de sucesso propostas | Seção 7 | Atendido; metas e baselines pendentes |
| Riscos e premissas descritos | Seção 8 | Atendido |

## 11. Conclusão

O problema de negócio escolhido é a **dificuldade de transformar o conhecimento de incidentes anteriores em apoio rápido, rastreável e responsável à investigação de incidentes atuais**. O Incident Copilot pretende ajudar profissionais de operações a organizar evidências, recuperar relatos históricos relevantes, formular hipóteses e identificar próximos passos, sem confundir similaridade documental com comprovação de causa raiz.

A E1.1 estabelece usuários, dores, resultados e indicadores de sucesso **como hipóteses de produto a validar**. O protótipo ainda não apresentou métricas de eficácia, redução de tempo ou impacto operacional. A arquitetura E1.2 e o corpus curado da E1.3 dão suporte técnico ao planejamento; as metas de negócio deverão ser aferidas em testes posteriores.
