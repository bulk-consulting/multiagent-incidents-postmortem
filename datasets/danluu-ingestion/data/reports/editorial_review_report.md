# E1.3 — Relatório de apoio à revisão editorial

Gerado exclusivamente a partir do registro editorial, dos JSONs extraídos e da shortlist local. As recomendações abaixo são triagem técnica: **não constituem aprovação editorial** e não alteram `editorial_decision=pending_review`.

## Resumo executivo

| Documento | Recomendação técnica | Limitação principal | Atenção humana |
|---|---|---|---|
| DAN-001 — Allegro | `recommend_approval` | Redirecionamento legítimo da fonte | Confirmar a proveniência do salto de domínio |
| DAN-009 — Cloudflare | `recommend_approval` | Formatação de exemplos de código | Conferir legibilidade dos exemplos |
| DAN-134 — CircleCI | `recommend_with_caveats` | Gráficos não extraídos | Verificar visualmente espera de jobs e filas |
| DAN-143 — Datadog | `recommend_approval` | Relato multirregional longo | Planejar granularidade sem separar a recuperação |
| DAN-183 — incident.io | `needs_deeper_review` | Causa exata não confirmada | Manter hipóteses e linguagem probabilística |
| DAN-164 — GitLab | `recommend_approval` | Vários fatores técnicos e humanos | Não reduzir a causa a erro individual |
| DAN-135 — CircleCI | `recommend_approval` | Incidentes subsequentes de RabbitMQ | Separar evento Kubernetes dos eventos de fila |
| DAN-109 — Amazon | `recommend_approval` | Muitos impactos dependentes | Preservar a ordem da cascata DynamoDB |
| DAN-169 — Google | `recommend_with_caveats` | Relatório final e updates no mesmo documento | Indexar as duas partes separadamente no futuro |
| DAN-188 — Joyent | `recommend_with_caveats` | Incerteza durante a investigação | Preservar a evolução das hipóteses |
| DAN-066 — Cloudflare | `recommend_with_caveats` | Classificação causal corrigida em postscript | Não chamar definitivamente de falha Byzantine |
| DAN-234 — Twilio | `recommend_approval` | URL histórica redirecionada | Manter separadas falha Redis e cobrança |
| DAN-026 — GitHub | `recommend_with_caveats` | Gráficos ausentes do texto | Conferir os gráficos de fileservers |
| DAN-115 — Amazon | `recommend_approval` | Muitos serviços downstream | Separar degradação Kinesis dos efeitos derivados |
| DAN-218 — Slack | `needs_deeper_review` | Causa AWS descrita com pouca profundidade | Não representar o texto como RCA completo da AWS |
| DAN-137 — Cloudflare | `recommend_approval` | Antigo falso positivo de bloqueio | Registrar que a auditoria do HTML o resolveu |
| DAN-118 — Atlassian | `recommend_with_caveats` | Diagramas não representados | Conferir visualmente arquitetura e recuperação |
| DAN-086 — Azure | `recommend_approval` | Arquitetura e termos antigos | Contextualizar Fabric Controller e Guest Agent |
| DAN-230 — Tarsnap | `recommend_with_caveats` | Origem dos erros S3 incerta | Não promover o fator precipitante a causa confirmada |
| DAN-050 — crates.io | `recommend_approval` | Incidente curto | Preservar a hierarquia dos Five Whys |

## DAN-001 — Allegro

- **Empresa, título e fonte:** Allegro — *Postmortem — why Allegro went down* — https://allegro.tech/2018/08/postmortem-why-allegro-went-down.html
- **Data identificável:** 18 de julho de 2018.
- **Resumo técnico:** Uma promoção gerou tráfego súbito, em grande parte automatizado. A configuração de escalabilidade reservava CPU e memória para instâncias existentes, impedindo novas instâncias de iniciar mesmo com capacidade física ociosa. Retries e limites de pools agravaram a saturação. O relatório combina cronologia, análise de reservas do cluster e mudanças técnicas e comerciais.
- **Sintomas e impacto:** Aumento de latência antes do meio-dia, falha de transações e indisponibilidade do site durante a oferta.
- **Causalidade:** Causa explícita: configuração incorreta das reservas de recursos. Tráfego de bots, retries e pools saturados foram contribuintes.
- **Evidências:** “prevented more instances from starting despite resources being there” — seção *Outage timeline* (~29%). “retries only increase the load” — seção *Analysis* (~54%).
- **Mitigação e recuperação:** Escala manual, estabilização após a pressão de tráfego e tratamento posterior das compras interrompidas.
- **Prevenção:** Alterar reservas do cluster, revisar pools e retries e melhorar o planejamento de promoções.
- **Limitações editoriais:** A fonte redireciona legitimamente de `allegro.tech` para `blog.allegro.tech`; o histórico deve permanecer documentado.
- **Recomendação técnica:** `recommend_approval` — cadeia causal explícita, evidência operacional e ações concretas; requer apenas conferência de proveniência.

## DAN-009 — Cloudflare

- **Empresa, título e fonte:** Cloudflare — *Cloudflare incident on January 24, 2023* — https://blog.cloudflare.com/cloudflare-incident-on-january-24th-2023/
- **Data identificável:** 24 de janeiro de 2023.
- **Resumo técnico:** Um release do Access sobrescreveu com strings vazias os secrets de service tokens. O rollout foi revertido rapidamente, mas valores já propagados invalidaram autenticação usada por WARP, Zero Trust, R2, Cache Reserve e purge. A recuperação exigiu restaurar metadados a partir do banco e aguardar propagação.
- **Sintomas e impacto:** Falhas de autenticação, uploads de postura zerados, políticas bloqueando tráfego e degradação de serviços internos da Cloudflare.
- **Causalidade:** Causa confirmada no release; a dependência de serviços internos nos tokens ampliou o impacto.
- **Evidências:** “overwrite service token metadata” — *Incident Timeline* (~27%). “tokens of impacted accounts invalid” — introdução (~6%).
- **Mitigação e recuperação:** Rollback interrompeu novas sobrescritas; secrets foram restaurados e redistribuídos pela rede.
- **Prevenção:** Testes específicos, proteção de campos, alertas e mudanças no processo de release descritos na seção final.
- **Limitações editoriais:** Exemplos de código dependem da formatação original e merecem inspeção humana.
- **Recomendação técnica:** `recommend_approval` — relato primário, causa explícita, timeline e remediações verificáveis.

## DAN-134 — CircleCI

- **Empresa, título e fonte:** CircleCI — *Postmortem: May 21, 2021 — Delay in starting Docker Jobs* — https://discuss.circleci.com/t/postmortem-may-21-2021-delay-in-starting-docker-jobs-machine-remote-docker-environments-blocked/40274
- **Data identificável:** 21 de maio de 2021, com evento contribuinte em 20 de maio.
- **Resumo técnico:** Após upgrade do RabbitMQ 3.8.9 para 3.8.16, um timeout de acknowledgment que se esperava restrito a quorum queues afetou outros tipos de fila. Canais de consumidores foram fechados, uma fila chegou a zero consumidores e VMs deixaram de ser removidas. Retries automáticos atingiram quotas do GCP e prolongaram a recuperação de jobs.
- **Sintomas e impacto:** Atraso no início de Docker jobs; ambientes machine e remote Docker bloqueados.
- **Causalidade:** Explicação explícita envolvendo mudança de timeout e fechamento de canais; quotas e retries contribuíram.
- **Evidências:** “eventually hitting zero consumers” — *Contributing Event* (~18%). “automated retries were the leading cause” — *What Happened* (~42%).
- **Mitigação e recuperação:** Bloqueio de novos machine jobs, redução de backlog e recuperação gradual das filas e quotas.
- **Prevenção:** Provisionamento mais robusto, independência entre VM e Docker jobs, observabilidade de RabbitMQ, batching e resposta a incidentes longos.
- **Limitações editoriais:** Os gráficos citados não foram extraídos; valores e contexto visual precisam de conferência.
- **Recomendação técnica:** `recommend_with_caveats` — texto forte, mas a validação editorial deve consultar os gráficos.

## DAN-143 — Datadog

- **Empresa, título e fonte:** Datadog — *2023-03-08 Incident: Infrastructure connectivity issue affecting multiple regions* — https://www.datadoghq.com/blog/2023-03-08-multiregion-infrastructure-connectivity-issue/
- **Data identificável:** 8 de março de 2023; recuperação continuou em 9 e 10 de março.
- **Resumo técnico:** Uma atualização de segurança do systemd reiniciou `systemd-networkd` em VMs Ubuntu 22.04. O processo removeu rotas administradas pelo Cilium, isolando nós Kubernetes em várias regiões. A recuperação foi sequenciada para telemetria em tempo real, dados históricos e serviços restantes.
- **Sintomas e impacto:** APIs e monitores indisponíveis, alertas ausentes e ingestão de dados afetada.
- **Causalidade:** Causa explicitamente identificada na interação systemd-networkd/Cilium; a amplitude multirregional agravou a restauração.
- **Evidências:** “forcibly deleted the routes managed by” Cilium — análise (~21%). “APIs and monitors were unavailable” — início (~3%).
- **Mitigação e recuperação:** Restauração priorizou ingestão e processamento em tempo real, depois histórico e demais serviços.
- **Prevenção:** Melhorias de rollout, proteção de rotas e preparação para recuperação multirregional.
- **Limitações editoriais:** O relato é longo; chunking futuro deve preservar a sequência entre regiões e fases.
- **Recomendação técnica:** `recommend_approval` — causa e recuperação são claras e tecnicamente relevantes.

## DAN-183 — incident.io

- **Empresa, título e fonte:** incident.io — *Clouds, caches and connection conundrums* — https://incident.io/blog/clouds-caches-and-connection-conundrums
- **Data identificável:** Não identificável com segurança no texto extraído.
- **Resumo técnico:** A investigação começou com timeouts esparsos de Memcached e passou por hipóteses sobre pools PostgreSQL, concorrência e chamadas externas. Traces e métricas apontaram rajadas de conexões, CPU elevada do `anetd` e drops de pacotes no GKE Dataplane V2. Keep-alives, pooling e limites de concorrência reduziram o problema, mas o texto não fecha um mecanismo causal único.
- **Sintomas e impacto:** Pequena fração de requests com timeouts; algumas falhas afetavam operações além de uma única requisição.
- **Causalidade:** Hipóteses sustentadas por evidência, não causa definitivamente confirmada.
- **Evidências:** “high volume of TCP connections being opened and closed” — investigação de `anetd` (~75%). “nothing obvious” nos logs — mesma seção.
- **Mitigação e recuperação:** Aumento do lifespan do pool, conexões estáticas, pooling/keep-alives e limitação de concorrência externa.
- **Prevenção:** Melhor instrumentação, investigação de traces e limites sensatos para chamadas externas.
- **Limitações editoriais:** Análise técnica, não RCA conclusiva; linguagem de incerteza é parte essencial do documento.
- **Recomendação técnica:** `needs_deeper_review` — excelente material de investigação, mas um editor deve confirmar se o corpus aceita casos sem causa final.

## DAN-164 — GitLab

- **Empresa, título e fonte:** GitLab — *Postmortem of database outage of January 31* — https://about.gitlab.com/2017/02/10/postmortem-of-database-outage-of-january-31/
- **Data identificável:** 31 de janeiro de 2017.
- **Resumo técnico:** Carga e locks produziram atraso de replicação; WAL necessário já havia sido removido e não existia arquivamento suficiente. Durante a ressincronização manual, o diretório de dados do primário foi apagado por engano. Procedimentos de backup e restore falharam ou estavam incompletos, prolongando a indisponibilidade e causando perda de dados.
- **Sintomas e impacto:** GitLab.com indisponível por aproximadamente 18 horas e perda de alterações entre 17:20 e 00:00 UTC.
- **Causalidade:** Cadeia multifatorial confirmada; não é apenas erro de operador.
- **Evidências:** “WAL segments needed by the secondary” já não estavam disponíveis — *Broken recovery procedures*. “primary database was removed by accident” — *Root cause analysis* (~65%).
- **Mitigação e recuperação:** Avaliação de snapshots e backups, restauração do banco e reativação gradual do GitLab.com.
- **Prevenção:** Testar restores, definir owner de durabilidade, melhorar WAL/backups e documentar procedimentos.
- **Limitações editoriais:** Deve preservar controles ausentes, falhas de backup e contexto humano sem culpabilização individual.
- **Recomendação técnica:** `recommend_approval` — caso primário excepcional sobre bancos, recuperação e fatores humanos.

## DAN-135 — CircleCI

- **Empresa, título e fonte:** CircleCI — *CircleCI Status — Jobs not starting* — https://status.circleci.com/incidents/dcqb3fykhgvg
- **Data identificável:** 14 de março de 2023, com efeitos até 15 de março.
- **Resumo técnico:** Um upgrade Kubernetes deixou kubelet e kube-proxy em versões incompatíveis. Falhas repetidas de `iptables-restore` corromperam a conectividade entre serviços do cluster de produção e impediram jobs de iniciar. A recuperação também desencadeou dois eventos posteriores em RabbitMQ, com atrasos de pipelines e checks do GitHub.
- **Sintomas e impacto:** Pipelines atrasados ou parados entre 18:00 e 01:27 UTC; incidentes posteriores de fila.
- **Causalidade:** Causa explícita para o evento principal; os eventos RabbitMQ são contribuintes posteriores distintos.
- **Evidências:** “version mismatch between kubelet and kubeproxy” — *Summary* (~4%). “Failed to execute iptables-restore” — análise (~54%).
- **Mitigação e recuperação:** Correção da incompatibilidade e restauração da rede; tratamento posterior das filas RabbitMQ.
- **Prevenção:** Melhorias no processo de upgrade, compatibilidade de versões, validação de rede e operação das filas.
- **Limitações editoriais:** Manter separados post-mortem principal e efeitos subsequentes de RabbitMQ.
- **Recomendação técnica:** `recommend_approval` — logs, cronologia e mecanismo Kubernetes estão preservados e claros.

## DAN-109 — Amazon

- **Empresa, título e fonte:** Amazon — *Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region* — https://aws.amazon.com/message/5467D2/
- **Data identificável:** 20 de setembro; o ano não aparece de forma inequívoca no texto extraído.
- **Resumo técnico:** Respostas lentas do serviço de metadados fizeram storage servers excederem timeout, retirarem-se temporariamente do atendimento e solicitarem novamente seus memberships. As retries mantiveram a carga elevada e bloquearam ações administrativas para adicionar capacidade. O evento afetou DynamoDB e serviços dependentes, incluindo Auto Scaling, SQS e CloudWatch.
- **Sintomas e impacto:** Erros elevados no DynamoDB US-East e backlog em serviços dependentes.
- **Causalidade:** Feedback loop explicitamente descrito; cascatas downstream são efeitos, não causas independentes.
- **Evidências:** Pausar requests “decreased retry activity” — corpo (~39%). Auto Scaling acumulou “a significant backlog” — *Impact on Other Services* (~73%).
- **Mitigação e recuperação:** Pausa de requests ao metadata service, adição de capacidade e reinserção de servidores no caminho de atendimento.
- **Prevenção:** Isolamento e capacidade do metadata service, controle de retries e mudanças corretivas descritas pela AWS.
- **Limitações editoriais:** Terminologia densa e vários serviços exigem preservar a ordem causal.
- **Recomendação técnica:** `recommend_approval` — exemplo forte de retry amplification e falha em cascata.

## DAN-169 — Google

- **Empresa, título e fonte:** Google — *Incident details — Google Cloud Service Health* — https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW
- **Data identificável:** 12 de junho de 2025; relatório final publicado em 13 de junho.
- **Resumo técnico:** Uma feature de quota do Service Control possuía caminho sem tratamento de erro e sem feature flag. Uma política com campos vazios foi replicada globalmente via Spanner, acionou null pointer e crash loops regionais. A recuperação com reinícios criou pressão adicional, descrita como thundering herd. O documento contém primeiro o relatório final e depois updates preliminares timestampados.
- **Sintomas e impacto:** Erros 503 em APIs de Google Cloud, Workspace e Security Operations, com impacto global.
- **Causalidade:** Causa confirmada no relatório final; updates preliminares devem ser tratados como observações temporais.
- **Evidências:** “policy data contained unintended blank fields” — relatório final (~13%). “null pointer caused the binary to crash” — análise da feature (~11%).
- **Mitigação e recuperação:** Uso do red-button para desabilitar o caminho, rollout regional e recuperação progressiva.
- **Prevenção:** Error handling, feature flags, testes do caminho com policy changes e infraestrutura independente de comunicação.
- **Limitações editoriais:** Separar `Final incident report` de `Status updates` em qualquer transformação futura.
- **Recomendação técnica:** `recommend_with_caveats` — excelente conteúdo, condicionado à preservação das duas camadas temporais.

## DAN-188 — Joyent

- **Empresa, título e fonte:** Joyent — *Postmortem for July 27 outage of the Manta service* — https://web.archive.org/web/20220528044329/https://www.joyent.com/blog/manta-postmortem-7-27-2015
- **Data identificável:** 27 de julho de 2015; publicação em 3 de agosto.
- **Resumo técnico:** Uma base PostgreSQL do metadata tier do Manta ficou bloqueada enquanto executava autovacuum anti-wraparound. A análise posterior identificou interação com uma query da aplicação que solicitava lock mais amplo que o necessário. O relato conserva as hipóteses iniciais, incidentes anteriores, tentativas de acelerar autovacuum e a conclusão posterior.
- **Sintomas e impacto:** Alta latência e erros 500 em cerca de 22% das operações, com pico próximo de 27%, até 20:45 UTC.
- **Causalidade:** Interação causal descrita na análise final, mas a equipe inicialmente não entendia o bloqueio.
- **Evidências:** “nearly all queries were waiting” — *The problem* (~14%). A equipe “did not understand why” autovacuum bloqueava queries — investigação.
- **Mitigação e recuperação:** Restart do PostgreSQL, preservação de dados diagnósticos e ações para concluir/otimizar vacuum.
- **Prevenção:** Ajustes de queries e locks, observabilidade do metadata tier e preparação para anti-wraparound.
- **Limitações editoriais:** Não apagar a diferença entre hipótese operacional e conclusão posterior.
- **Recomendação técnica:** `recommend_with_caveats` — tecnicamente rico, desde que a evolução da incerteza seja mantida.

## DAN-066 — Cloudflare

- **Empresa, título e fonte:** Cloudflare — *A Byzantine failure in the real world* — https://web.archive.org/web/20211015231917/https://blog.cloudflare.com/a-byzantine-failure-in-the-real-world/
- **Data identificável:** 2 de novembro de 2020.
- **Resumo técnico:** Um switch parcialmente defeituoso apresentou visões diferentes de conectividade aos membros de um cluster. Eleições Raft terminaram repetidamente empatadas e o datastore de control plane ficou sem líder alcançável, bloqueando writes. O título e o corpo chamam inicialmente o comportamento de Byzantine, mas o postscript o reclassifica como omission fault.
- **Sintomas e impacto:** Erros de etcd, cluster read-only e efeitos em sistemas dependentes e dashboard.
- **Causalidade:** Mecanismo explícito, com terminologia formal corrigida posteriormente.
- **Evidências:** “repeatedly initiated leader elections” — análise (~37%). Postscript: “better characterized as an omission fault” — (~96%).
- **Mitigação e recuperação:** Redução de carga, uso de redundância e reconstrução de réplica após recuperação do switch.
- **Prevenção:** Correção do cluster manager e aumento de resiliência a falhas parciais de dependências.
- **Limitações editoriais:** A reclassificação é obrigatória; não rotular definitivamente o caso como Byzantine.
- **Recomendação técnica:** `recommend_with_caveats` — apropriação depende de conservar título histórico e correção conceitual juntos.

## DAN-234 — Twilio

- **Empresa, título e fonte:** Twilio — *Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause* — https://www.twilio.com/blog/2013/07/billing-incident-post-mortem-breakdown-analysis-and-root-cause.html
- **Data identificável:** 18 de julho de 2013.
- **Resumo técnico:** Perda de conectividade fez slaves Redis solicitarem full sync simultaneamente, elevando a carga no master. Um restart com configuração errada tentou recuperar AOF inexistente, perdeu saldos e iniciou o master como slave de si próprio, em modo read-only. Retries de recharge cobraram cartões antes que o saldo pudesse ser atualizado.
- **Sintomas e impacto:** 1,4% dos clientes afetados; saldos atrasados, recargas repetidas e algumas contas suspensas. Voz e SMS continuaram operando.
- **Causalidade:** Cadeia confirmada de rede, sincronização, configuração de recuperação e falta de idempotência transacional.
- **Evidências:** “boot as a slave of itself” — análise (~64%). “recharge was attempted multiple times” — impacto inicial.
- **Mitigação e recuperação:** Correção da configuração Redis, restauração de saldos e reconciliação das cobranças.
- **Prevenção:** Configuração de recovery segura, controle de sincronizações e idempotência no fluxo de cobrança.
- **Limitações editoriais:** Preservar o redirecionamento histórico e não colapsar Redis e billing em uma causa única.
- **Recomendação técnica:** `recommend_approval` — compacto, concreto e relevante a recovery e idempotência.

## DAN-026 — GitHub

- **Empresa, título e fonte:** GitHub — *DNS Outage Post Mortem* — https://github.blog/news-insights/the-library/dns-outage-post-mortem/
- **Data identificável:** 8 de janeiro; o ano não é inequívoco no texto extraído.
- **Resumo técnico:** Uma mudança de IP deveria reiniciar nameservers autoritativo e de cache, mas um bug Puppet reiniciou apenas o autoritativo. O cache consultou um IP que já não servia DNS. Durante a recuperação, uma API interna dependente de DNS devolveu dados incompletos e corrompeu zone files, gerando NXDOMAIN; fileservers também sofreram pressão de processos e memória.
- **Sintomas e impacto:** 42 minutos de indisponibilidade geral e mais 1h35 em parte dos repositórios.
- **Causalidade:** Cadeia explícita: configuração Puppet, DNS timeout, dependência circular e corrupção de zonas.
- **Evidências:** “only the authoritative name server was restarted” — *What happened* (~32%). “zone files had become corrupted” — (~37%).
- **Mitigação e recuperação:** Reload de nameservers, execução manual e validação da API, restauração das zonas e recuperação de fileservers.
- **Prevenção:** Seis medidas numeradas: testes Puppet, revisão da dependência circular, validação, DNS e capacidade operacional.
- **Limitações editoriais:** Gráficos de processos e memória são mencionados, mas não estão representados no texto.
- **Recomendação técnica:** `recommend_with_caveats` — cadeia forte; recomenda-se consultar os gráficos antes da decisão humana.

## DAN-115 — Amazon

- **Empresa, título e fonte:** Amazon — *Summary of the Amazon Kinesis Data Streams Service Event in Northern Virginia* — https://aws.amazon.com/message/073024/
- **Data identificável:** 30 de julho de 2024.
- **Resumo técnico:** Distribuição desigual concentrou muitos shards de baixo throughput em poucos hosts de uma célula Kinesis. Status messages cresceram, chegaram atrasadas e fizeram o sistema de gerenciamento classificar hosts saudáveis como falhos. A redistribuição de shards gerou uma tempestade e pressionou provisionamento de conexões, afetando serviços AWS dependentes.
- **Sintomas e impacto:** Latência e erros entre 14:45 e 21:37 PDT em CloudWatch Logs, Firehose, eventos S3, ECS, Lambda, Redshift e Glue.
- **Causalidade:** Root cause explícita na nova arquitetura de gerenciamento; impactos downstream são derivados.
- **Evidências:** “incorrectly determined that the healthy hosts were unhealthy” — corpo (~37%). A célula degradada causou impacto “directly or indirectly” — *Issue Summary*.
- **Mitigação e recuperação:** Estabilização da célula, redistribuição controlada e recuperação dos serviços e backlogs dependentes.
- **Prevenção:** Limites e processamento de status messages, distribuição de shards, proteção contra storms e isolamento de dependências.
- **Limitações editoriais:** A quantidade de serviços exige separar causa, célula afetada e cascatas.
- **Recomendação técnica:** `recommend_approval` — caso claro de skew, detecção falsa e redistribuição amplificada.

## DAN-218 — Slack

- **Empresa, título e fonte:** Slack — *Slack’s Outage on January 4th 2021* — https://slack.engineering/slacks-outage-on-january-4th-2021/
- **Data identificável:** 4 de janeiro de 2021.
- **Resumo técnico:** Problemas na rede AWS elevaram packet loss e latência entre web tier e backends. Threads ficaram bloqueadas; CPU inicialmente caiu e induziu downscale, seguido por upscale intenso. Uma tentativa de adicionar 1.200 servidores expôs gargalos no `provision-service`. A AWS depois identificou saturação em parte da infraestrutura de rede, sem RCA detalhada no documento.
- **Sintomas e impacto:** Saturação do web tier, instâncias marcadas unhealthy e indisponibilidade do Slack.
- **Causalidade:** Mecanismo interno bem evidenciado; fator iniciador externo permanece descrito em nível limitado.
- **Evidências:** “increased packet loss led to much higher latency” — corpo (~23%). “attempted to add 1,200 servers” — (~39%).
- **Mitigação e recuperação:** Scale-up manual, entrada gradual de hosts saudáveis e uso do panic mode dos load balancers.
- **Prevenção:** Load tests do provision-service e revisão de health checks e autoscaling.
- **Limitações editoriais:** Não tratar como análise completa da causa na AWS.
- **Recomendação técnica:** `needs_deeper_review` — útil para recovery e autoscaling, mas a adequação causal depende do escopo editorial desejado.

## DAN-137 — Cloudflare

- **Empresa, título e fonte:** Cloudflare — *Details of the Cloudflare outage on July 2, 2019* — https://web.archive.org/web/20211006055154/https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/
- **Data identificável:** 2 de julho de 2019.
- **Resumo técnico:** Uma regra WAF global continha regex com backtracking catastrófico e consumiu CPU dos proxies HTTP/HTTPS em toda a rede. Uma proteção de CPU havia sido removida em refactoring, testes não capturavam custo e o processo permitia deploy global rápido. Timeline, WAF, Quicksilver, ações e apêndice técnico estão completos.
- **Sintomas e impacto:** CPU próxima de 100% e indisponibilidade mundial de tráfego HTTP/HTTPS.
- **Causalidade:** Cadeia confirmada com múltiplas vulnerabilidades, não uma única causa isolada.
- **Evidências:** “CPUs to become exhausted on every CPU core” — *The events of July 2* (~6%). “backtrack enormously” — análise (~58%).
- **Mitigação e recuperação:** Identificação e remoção da regra, rollback e restauração global.
- **Prevenção:** Testes de desempenho de regex, limites de CPU, rollout progressivo e revisão do pipeline de regras.
- **Limitações editoriais:** O alerta de login era falso positivo de “sign in” na explicação do autômato; HTML auditado sem bloqueio.
- **Recomendação técnica:** `recommend_approval` — relato canônico, completo e auditado.

## DAN-118 — Atlassian

- **Empresa, título e fonte:** Atlassian — *Post-Incident Review on the Atlassian April 2022 outage* — https://www.atlassian.com/engineering/post-incident-review-april-2022-outage
- **Data identificável:** 5 a 18 de abril de 2022.
- **Resumo técnico:** Uma equipe forneceu IDs de sites em vez de IDs do app Insight a um processo de remoção. A API aceitava ambos sem advertir sobre o tipo, e o script apagou 883 sites de 775 clientes. A restauração multi-site e multi-produto durou até 14 dias, exigindo automação nova, validação manual e reconstrução de contatos.
- **Sintomas e impacto:** Perda de acesso para 775 clientes; no máximo cinco minutos de dados perdidos, segundo o PIR.
- **Causalidade:** Gap de comunicação e controles insuficientes no processo/API são explicitamente documentados.
- **Evidências:** “IDs of the entire cloud site” — *What happened*. “restoring hundreds of customers with multiple products” — resposta inicial (~8%).
- **Mitigação e recuperação:** Dois workstreams de restauração, automação progressiva e validação por centenas de profissionais.
- **Prevenção:** Soft delete universal, rollout em etapas, rollback testado, DR em escala e playbook de comunicação.
- **Limitações editoriais:** Figuras e diagramas têm legendas, mas seu conteúdo visual não está no texto.
- **Recomendação técnica:** `recommend_with_caveats` — PIR excepcional; aprovação humana deve reconhecer a perda dos diagramas.

## DAN-086 — Azure

- **Empresa, título e fonte:** Azure — *Summary of Windows Azure Service Disruption on Feb 29th, 2012* — https://azure.microsoft.com/en-us/blog/summary-of-windows-azure-service-disruption-on-feb-29th-2012/
- **Data identificável:** 29 de fevereiro de 2012.
- **Resumo técnico:** Cálculo incorreto adicionou um ano à data de certificados de transferência e produziu 29 de fevereiro de 2013, data inexistente. Guest Agents rejeitaram certificados e perderam comunicação com Host Agents/Fabric Controllers, afetando deploys e gerenciamento. Uma ação posterior em sete clusters causou um outage secundário antes do pacote corrigido.
- **Sintomas e impacto:** Novos deploys falharam, operações de gerenciamento foram prejudicadas e houve indisponibilidade adicional em clusters.
- **Causalidade:** Leap-day bug confirmado, com erro secundário durante recuperação.
- **Evidências:** “February 29, 2013, an invalid date” — *The Leap Day Bug*. “GAs in new VMs tried to generate certificates” — *Bug in Action*.
- **Mitigação e recuperação:** Correção e teste do Guest Agent, rollout controlado e pacote HA corrigido.
- **Prevenção:** Testes de datas, isolamento de falhas, detecção, resposta e recuperação mais seguras.
- **Limitações editoriais:** Arquitetura de 2012 exige contextualização; `<sup>` de datas já foi normalizado sem perda.
- **Recomendação técnica:** `recommend_approval` — causalidade, timeline e lições de validação são claras.

## DAN-230 — Tarsnap

- **Empresa, título e fonte:** Tarsnap — *Tarsnap outage 2016-07-24 10:15:19–11:40:04* — https://mail.tarsnap.com/tarsnap-announce/msg00035.html
- **Data identificável:** 24 de julho de 2016.
- **Resumo técnico:** Falhas correlacionadas do S3 fizeram um job de limpeza abortar e reiniciar 142 vezes. Cada tentativa registrou novamente blocos no log até encher o filesystem; writes falharam e o serviço desligou defensivamente. O operador removeu o log regenerável e reiniciou o servidor. A mudança que provocou os erros S3 não foi diagnosticada.
- **Sintomas e impacto:** Serviço indisponível por 85 minutos; archives em criação falharam, sem perda de dados armazenados.
- **Causalidade:** Mecanismo Tarsnap confirmado; fator precipitante S3 permanece hipótese/incerteza.
- **Evidências:** “fills the filesystem” — timeline. “not yet clear what the root cause within Amazon S3 is” — *Footnotes*.
- **Mitigação e recuperação:** Diagnóstico do filesystem, remoção segura do log e restart às 11:40 UTC.
- **Prevenção:** Monitorar espaço livre, investigar anomalias e rever alertas humanos, ponderando riscos de segurança do monitoring interno.
- **Limitações editoriais:** Preservar incerteza S3 e manter assinatura/OpenPGP separadas do corpo técnico.
- **Recomendação técnica:** `recommend_with_caveats` — mecanismo interno e lições são fortes; causa externa não deve ser afirmada.

## DAN-050 — rust-lang / crates.io

- **Empresa, título e fonte:** rust-lang — *crates.io Postmortem: Broken Crate Downloads* — https://blog.rust-lang.org/inside-rust/2023/07/21/crates-io-postmortem.html
- **Data identificável:** 20 de julho de 2023, com lead-up em 19 de julho.
- **Resumo técnico:** Um deploy introduziu bug na geração de URLs após migração para `object_store`, concatenando host e caminho incorretamente. Todos os downloads falharam por 13 minutos; retries do Cargo amplificaram tráfego e cerca de 3,7 milhões de requests falharam. Rollback restaurou imediatamente as URLs, e o Five Whys liga cobertura de testes, revisão e smoke tests incompletos.
- **Sintomas e impacto:** Downloads de crates falharam entre 12:17 e 12:30 UTC; média de 4,71 mil requests/s.
- **Causalidade:** Causa explícita e análise causal hierárquica.
- **Evidências:** “system immediately recovered” após rollback — *Recovery* (~32%). “about 3.7M failed requests” — *Summary*.
- **Mitigação e recuperação:** Rollback, correção com testes realistas, validação em staging e novo deploy.
- **Prevenção:** Incluir downloads no smoke test, automatizá-lo e definir quando code review é obrigatório.
- **Limitações editoriais:** Relato curto; a hierarquia de perguntas e respostas dos Five Whys deve permanecer intacta.
- **Recomendação técnica:** `recommend_approval` — caso conciso, mensurável e com prevenção concreta.

## Síntese das recomendações

- `recommend_approval`: 11 documentos.
- `recommend_with_caveats`: 7 documentos.
- `needs_deeper_review`: 2 documentos — DAN-183 e DAN-218.
- Decisões editoriais registradas por este relatório: **nenhuma**.
