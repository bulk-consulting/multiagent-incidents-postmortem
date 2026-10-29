# E1.2 — Proposta de Arquitetura de Agentes

**Projeto 4 — Incident Copilot / Resolução de Incidentes e Post-Mortems**  
**Entrega:** 1.2 — Proposta de arquitetura de agentes  
**Situação:** proposta de design; implementação e testes ainda não realizados

## 1. Visão geral

O sistema é um workflow condicional multi-agente: o código define os caminhos possíveis do fluxo, e os agentes decidem, a cada passo, qual caminho seguir com base no que encontraram. A investigação de cada incidente é identificada por um `incident_id`, o que permite retomá-la quando o analista envia novas informações ou refina a busca.

O desenho prioriza **orquestração definida (defined orchestration)**: os caminhos de execução são estabelecidos pela aplicação; o uso de LLM ajuda na interpretação e na seleção entre caminhos permitidos, sem controlar livremente toda a execução.


## 2. Diagrama de referência

Arquitetura do Incident Copilot

![Arquitetura do Incident Copiloto](/docs/desenho.png)


## 3. Como os agentes se comunicam
 
A troca de informações acontece pelo **estado compartilhado da investigação** e pelas **transições do workflow**, e não por uma conversa livre entre os agentes.
 
1. A API recebe uma nova descrição ou um complemento associado a um `incident_id` e valida a estrutura da entrada.
2. O módulo inicial a descrição em sintomas ou organiza as novas evidências enviadas.
3. O contexto é persistido, e o workflow encaminha ao Agente 1 os sintomas, termos, filtros e histórico relevante da investigação.
4. O Agente 1 devolve as referências recuperadas: IDs dos documentos e trechos, o conteúdo dos trechos, links das fontes, metadados e o score de relevância.
5. O Agente 2 recebe o contexto do incidente atual e as evidências históricas, propõe hipóteses ranqueadas e avalia se a evidência é suficiente, quais lacunas existem e qual é o próximo passo. Com base nessa avaliação, o workflow conclui o diagnóstico, refina a pesquisa, solicita informações adicionais ou encerra como inconclusivo.
6. O sistema envia ao usuário o relatório ou um pedido de informações. Se o usuário responder ou quiser refinar a busca, a nova mensagem entra como continuação da mesma investigação, e o processo volta ao passo 1.


## 4. Responsabilidade de cada agente

**Dois agentes especializados**, ambos no workflow condicional:

| Agente | Responsabilidade | Recebe | Entrega |
|---|---|---|---|
| **Agente 1 — Pesquisa RAG** | Buscar na base vetorial os post-mortems e runbooks mais parecidos com o incidente | Sintomas, termos e filtros da investigação | Post-mortems, runbooks e fontes encontrados |
| **Agente 2 — Análise e diagnóstico diferencial** | Analisar as evidências, ranquear as causas prováveis e avaliar se a evidência é suficiente. No fim da investigação, gerar o relatório | Evidências do Agente 1 | Hipóteses ranqueadas e avaliação estruturada; depois, o relatório |
 
O relatório traz, para cada causa provável: causa raiz histórica, passos de remediação, código ou configuração alterados, checklist de prevenção, link para o post-mortem original e nível de confiança.

## 5. Comunicação entre agentes e módulos

A troca de informações é **mediada pelo estado compartilhado da investigação e pelas transições do workflow**, e não por conversação irrestrita entre agentes.

1. A API recebe uma nova descrição ou um complemento associado a `incident_id` e valida a estrutura de entrada.
2. O módulo inicial sintetiza a descrição ou organiza as novas evidências.
3. O contexto é persistido; o workflow encaminha ao Agente 1 termos, sintomas, filtros e histórico relevante.
4. O Agente 1 devolve referências recuperadas: IDs de documentos/chunks, trechos, URLs, metadados editoriais e indicação de relevância.
5. O Agente 2 recebe o contexto da ocorrência atual e as evidências históricas; propõe hipóteses e indica suficiência, lacunas e próximos passos possíveis.
6. O roteador aplica regras de fluxo: concluir, refinar pesquisa, solicitar evidências adicionais ou encerrar como inconclusivo.
7. Quando o usuário complementa o incidente, a API recupera o estado pelo `incident_id`, incorpora as informações e retoma o workflow.

**Campos conceituais do estado** (não são um contrato de API nem esquema SQL definitivo): `incident_id`, `status`, `incident_context`, `evidence_received`, `search_terms`, `filters`, `retrieved_references`, `hypotheses`, `uncertainties`, `refinement_count`, `max_refinements`, `pending_questions` e `report`.

Os agentes **não devem tratar relatos históricos como prova de causalidade do incidente atual**. A resposta deve manter rastreabilidade das fontes e distinguir observação, hipótese, inferência e limitação.

## 6. Fluxo de orquestração

### 6.1 Entrada e preparação (sequencial)

**Alerta / interface / complemento → API FastAPI → autenticação e validação com Pydantic → identificar nova investigação ou retomada → estruturar contexto → persistir estado.**

- **Nova investigação:** o LLM sintetiza e decompõe sintomas antes de iniciar a pesquisa.
- **Complemento com novas evidências:** o estado anterior é carregado e um LLM estrutura as informações adicionadas.
- **Retomada para refinar:** termos e filtros são atualizados sem inventar evidências novas.

A validação deve impedir a mistura de informações entre incidentes diferentes. Detalhes de endpoints, contratos, autenticação e tratamento de erros são responsabilidade da **E1.4 — Estrutura da API (Mari)** e não são definidos aqui.

### 6.2 Investigação multiagente (sequencial e condicional)

O caminho principal é **Agente 1 → Agente 2 → decisão de suficiência**.

- Se há evidências suficientes, o Agente 2 prepara um diagnóstico **fundamentado e com ressalvas**.
- Se não há evidências suficientes e o limite foi alcançado, o Agente 2 prepara um relatório **inconclusivo**, explicitando lacunas.
- Se falta aprofundamento e ainda existe orçamento de investigação, o roteador escolhe entre **refinar a busca histórica** ou **solicitar evidências atuais ao usuário**.

### 6.3 Loops controlados

O ciclo **Agente 1 → Agente 2 → roteador → refinamento → Agente 1** só ocorre quando a busca histórica pode agregar informação e ainda há limite disponível. O limite de tentativas é um parâmetro **a definir na implementação**.

### 6.4 Paralelismo

O paralelismo acontece dentro do Agente 1, que faz as buscas nas fontes relevantes ao mesmo tempo e junta os resultados antes de entregá-los ao Agente 2.
 
As fontes do Agente 1 são organizadas em dois níveis. O **Tier 1** reúne as fontes mais rápidas, consultadas primeiro. O **Tier 2** reúne fontes menos estruturadas e, por isso, com mais ruído, consultadas apenas quando o Tier 1 não traz evidência suficiente.

---

**Conclusão:** a arquitetura proposta possui **dois agentes com responsabilidades complementares**, integrados por um **workflow definido, predominantemente sequencial, com decisões condicionais, refinamento limitado e pausa/retomada por incidente**. O desenho prevê geração de diagnóstico com fontes ou saída inconclusiva quando necessário, sem assumir integrações, ferramentas ou dados que ainda não foram implementados ou curados.
