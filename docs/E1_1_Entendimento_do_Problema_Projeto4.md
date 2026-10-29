# E1.1 — Entendimento do problema

**Projeto 4 — Incident Copilot: Assistente Inteligente de Incidentes e Post-Mortems**  
**Entrega:** 1.1 — Entendimento do problema de negócio  


## 1. Contexto do problema
 
A Stratus Cloud Services é um provedor de nuvem (MSP) que opera 12.000+ servidores, 800+ clusters Kubernetes e 200+ microsserviços para 350 clientes corporativos. Com esse tamanho, incidentes são frequentes, e o NOC funciona 24/7 com 35 analistas de SRE em 3 turnos.
 
Hoje, quando um incidente acontece, o analista de plantão recebe o alerta e precisa descobrir a causa raiz antes de corrigir. Para isso, procura manualmente se algo parecido já aconteceu: abre wikis, runbooks, post-mortems antigos e threads de Slack, e cruza com o que vê nas ferramentas de monitoramento. Só depois de encontrar a causa ele começa a remediação.
 
Essa busca manual é o gargalo: num incidente P1, o diagnóstico consome a maior parte do tempo total de resolução. O conhecimento para acelerar essa etapa já existe na empresa, mas está espalhado e difícil de encontrar no momento em que é necessário. 

 
## 2. Solução proposta: Incident Copilot
 
O **Incident Copilot** é um sistema multi-agente que recebe a descrição de um incidente em andamento (texto livre ou alerta estruturado), busca post-mortems e runbooks de incidentes parecidos e devolve um **diagnóstico diferencial ranqueado**. Cada causa provável vem com a remediação, a fonte original e o nível de confiança.
 
O objetivo é **reduzir o tempo de diagnóstico** dos incidentes, que hoje é a maior parte do MTTR, e assim contribuir para as metas de SLA da Stratus.


## 3. Quem é o usuário

| Persona | Quem é | O que precisa do sistema |
|---|---|---|
| **Analista SRE/NOC de plantão** (usuário principal) | Um dos 35 analistas; recebe o alerta e precisa encontrar a causa raiz | Causas prováveis em minutos, com passos de remediação e link da fonte |
| **SRE júnior / recém-contratado** | Em onboarding de 3 meses, sem o conhecimento tácito dos seniores | Acesso ao histórico de incidentes parecidos, explicado e citado |
| **Gestor de SRE** | Responde por SLA e penalidades contratuais | Redução do MTTR e da recorrência de incidentes |

**Premissa de uso:** um profissional humano continua responsável por validar o diagnóstico e decidir qualquer ação operacional. Os perfis são propostos para o MVP e ainda devem ser confirmados com usuários reais.

## 4. Qual é a dor
 
- **Diagnóstico lento:** dos 72 minutos de um P1, **47 são gastos só para encontrar a causa raiz**, buscando manualmente em wikis, Slack, runbooks e post-mortems.
- **Conhecimento fragmentado:** existem **500+ post-mortems** de 3 anos e centenas de runbooks espalhados em Confluence, Google Docs, repositórios Git e threads de Slack.
- **Problemas repetidos:** cerca de **35% dos incidentes** dos últimos 12 meses eram variações de problemas já resolvidos, mas o post-mortem certo não foi encontrado a tempo.
- **Perda de conhecimento tácito:** quando um SRE sênior sai da empresa, os novos analistas repetem os mesmos erros de diagnóstico.
- **Sinais de observabilidade espalhados:** os analistas alternam entre Zabbix, Datadog/Grafana, ELK/OpenSearch e Jaeger/OpenTelemetry sem uma visão consolidada.
- **Pressão de SLA:** o contrato exige MTTR < 30 min para P1 e < 2 h para P2. Hoje há **4,2 violações de SLA P1 por mês**.
**Impacto no negócio:** cada minuto de indisponibilidade custa cerca de **R$ 8.500** em penalidades e perda de receita. Reduzir o MTTR em 50% representa uma economia estimada de **R$ 2,1 milhões por ano**.


## 5. Resultado esperado
 
Dado um incidente em andamento, o sistema deve:
 
1. **Receber** a descrição em texto livre (web chat) ou um alerta estruturado (sistema de alertas).
2. **Decompor** o incidente em sintomas distintos e pesquisáveis.
3. **Buscar** na base de post-mortems e runbooks os incidentes passados mais parecidos.
4. **Avaliar** se a evidência encontrada é suficiente. Se não for, **refinar a busca** (novos termos e filtros, com limite de tentativas) ou **pedir informações adicionais** ao analista.
5. **Entregar um diagnóstico diferencial ranqueado**, com cada causa provável acompanhada de:
   - causa raiz histórica;
   - passos de remediação;
   - código ou configuração alterados;
   - checklist de prevenção;
   - link para o post-mortem original;
   - nível de confiança.
6. **Permitir interação iterativa:** o analista pode responder perguntas ou refinar a busca (ex.: "descarte incidentes de rede", "busque também por DNS") dentro da mesma investigação.
7. **Registrar** todas as buscas realizadas e as evidências consultadas, garantindo rastreabilidade.

Quando não houver evidência suficiente, o sistema deve dizer isso de forma explícita, em vez de inventar uma causa.


## 6. Métricas de sucesso e metodologia de avaliação

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

### 6.1 Desenho mínimo da avaliação

- Preparar um conjunto pequeno e documentado de cenários, incluindo casos com similaridade histórica clara, casos ambíguos e casos sem evidência suficiente.
- Definir respostas ou trechos de referência por revisão humana **antes** de comparar configurações.
- Executar os mesmos cenários manualmente (quando possível) e com o assistente, registrando duração e utilidade.
- Verificar se cada referência aponta para o documento correto e se o sistema preserva ressalvas editoriais.
- Registrar falhas, custo, limitações e critérios de aprovação; evitar generalizar resultados de uma amostra pequena.


## 7. Riscos, premissas e mitigação

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


## 8. Conclusão

O problema de negócio escolhido é a **dificuldade de transformar o conhecimento de incidentes anteriores em apoio rápido, rastreável e responsável à investigação de incidentes atuais**. O Incident Copilot pretende ajudar profissionais de operações a organizar evidências, recuperar relatos históricos relevantes, formular hipóteses e identificar próximos passos, sem confundir similaridade documental com comprovação de causa raiz.

A E1.1 estabelece usuários, dores, resultados e indicadores de sucesso **como hipóteses de produto a validar**. O protótipo ainda não apresentou métricas de eficácia, redução de tempo ou impacto operacional. A arquitetura E1.2 e o corpus curado da E1.3 dão suporte técnico ao planejamento; as metas de negócio deverão ser aferidas em testes posteriores.
