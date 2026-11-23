# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | sim | sim | search | não | sim | 0 | 12 |
| q-022 | DAN-104 | 4 | sim | sim | search | não | sim | 0 | 50 |
| q-170 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 54 |
| q-171 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 10 |
| q-222 | DAN-121 | 4 | sim | sim | search | não | sim | 0 | 107 |
| q-240 | DAN-152 | 4 | sim | sim | search | não | sim | 0 | 40 |
| q-012 | DAN-211 | 5 | sim | sim | search | não | sim | 0 | 15 |
| q-263 | DAN-200 | 5 | sim | sim | search | não | sim | 0 | 7 |
| q-032 | DAN-104 | 7 | sim | sim | search | não | sim | 0 | 45 |
| q-219 | DAN-116 | 7 | sim | sim | search | não | sim | 0 | 17 |
| q-223 | DAN-121 | 8 | sim | sim | search | não | sim | 0 | 43 |
| q-218 | DAN-116 | 9 | sim | sim | search | não | sim | 0 | 34 |
| q-229 | DAN-125 | 10 | sim | sim | search | não | sim | 0 | 103 |
| q-262 | DAN-200 | 10 | sim | sim | search | não | sim | 0 | 39 |
| q-228 | DAN-125 | 11 | não | não | search | não | não | 0 | 35 |
| q-034 | DAN-004 | 12 | não | não | search | não | não | 0 | 11 |
| q-243 | DAN-154 | 12 | não | não | search | não | não | 0 | 12 |
| q-260 | DAN-197 | 19 | não | não | search | não | não | 0 | 89 |
| q-242 | DAN-154 | — | não | não | search | não | não | 0 | 14 |
| q-261 | DAN-197 | — | não | não | search | não | não | 0 | 12 |

## q-020 (esperado: DAN-164)

- busca inicial: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-091, DAN-186, DAN-092, DAN-066, DAN-058
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup restoration recovery` — Corresponde exatamente: banco de produção deletado por acidente durante manutenção, com backup e restauração
- aprofundar DAN-056: `production database truncate accidental environment variable fix prevention` — Semelhança: banco de produção afetado por ação acidental, mas gatilho diferente (variável de ambiente em testes)
- aprofundar DAN-164: `admin deleted wrong directory database data loss recovery postmortem` — Semelhança: erro humano excluiu dados do banco, mas contexto diferente (replication lag, diretório errado)
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.714: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.651: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [What We Learned] 0.747: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.738: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a
  - DAN-164 (llm) [Root cause analysis] 0.642: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [sem seção] 0.618: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-022 (esperado: DAN-104)

- busca inicial: DAN-191, DAN-189, DAN-146, DAN-104, DAN-064, DAN-067, DAN-073, DAN-109, DAN-209, DAN-103
- justificativa: 
- aprofundar DAN-104: `S3 typo command remove servers root cause fix playbook` — Bate quase exatamente: operador digitou comando para remover poucos servidores, erro digitado removeu muito mais, derrubou o serviço de armazenamento (S3) e tudo que dependia dele (EC2, EBS e clientes externos). Não bate no detalhe do typo, mas o gatilho e a cascata são idênticos.
- aprofundar DAN-189: `operator reboot all servers input validation fix tool` — Bate no padrão de erro humano com comando de operador que afetou muito mais do que o pretendido e derrubou ambiente inteiro. Não bate porque a ação foi reiniciar servidores, não removê-los, e não se tratava especificamente de serviço de armazenamento.
- aprofundar DAN-073: `storage volume failure outage root cause remediation` — Bate porque falha em serviço de armazenamento derruba sites e programas dependentes, espelhando a cascata do incidente atual. Não bate porque o gatilho foi falha de volume, não comando do operador para remover servidores.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.568: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.544: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.576: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.567: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-073 (llm) [Next steps¶] 0.693: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (llm) [17:04¶] 0.689: #### 17:04¶  By this point we had become sure that the system was getting blocked on storage IO, but the problem did not seem to be the machine itself like the original indications had suggested. Howe
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi

## q-170 (esperado: DAN-018)

- busca inicial: DAN-144, DAN-066, DAN-017, DAN-018, DAN-029, DAN-191, DAN-102, DAN-037, DAN-067, DAN-154
- justificativa: 
- aprofundar DAN-018: `React dashboard excessive API calls dependency array fix` — Bate: dashboard (painel) gerando excessivas chamadas de API para serviço interno após alteração no frontend, com cascata para API e painel. Não bate: causa é bug de dependência array em serviço Tenant Service, não necessariamente deploy geral.
- aprofundar DAN-144: `thundering herd reconnect frontend services memory queues fix` — Bate: enxurrada (thundering herd) afetando serviços frontend com filas internas lotando e memória esgotada. Não bate: origem é serviço flapping que volta, não chamadas do painel disparadas por deploy do frontend.
- aprofundar DAN-067: `thundering herd API calls overwhelming services rate limit fix` — Bate: volume excessivo de chamadas de API sobrecarregando serviços com uso de rate limits. Não bate: origem é falha de energia em data center, não deploy do frontend nem painel como fonte das chamadas.
  - DAN-018 (llm) [Improving visibility] 0.651: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (llm) [What Happened] 0.646: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-144 (llm) [Summary] 0.545: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.529: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-067 (llm) [Disaster Recovery] 0.638: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.501: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 

## q-171 (esperado: DAN-018)

- busca inicial: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-133, DAN-129, DAN-218, DAN-145, DAN-220
- justificativa: 
- aprofundar DAN-018: `dashboard React component excessive API calls dependency array fix` — O resumo descreve exatamente o painel (dashboard) gerando chamadas excessivas a um serviço interno (Tenant Service) após alteração no frontend (bug React/dependency array), com cascata que derruba API e painel — igual ao incidente atual.
- aprofundar DAN-144: `thundering herd reconnect frontend memory queues fix` — Semelhança parcial: reenvio em massa (thundering herd) sobrecarregando serviços frontend e filas internas, mas não envolve o próprio painel disparando chamadas após deploy.
  - DAN-018 (llm) [What Happened] 0.648: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.608: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-144 (llm) [Summary] 0.501: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Action Items / Response] 0.5: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-144 (correcao) [Connectivity Issues] 0.428: ## Connectivity Issues  ## Postmortem  At Discord, one of our primary concerns is the uptime and reliability of our service. We’ve all experienced the frustration and annoyance that comes along with t

## q-222 (esperado: DAN-121)

- busca inicial: DAN-129, DAN-144, DAN-147, DAN-121, DAN-016, DAN-137, DAN-134, DAN-209, DAN-148, DAN-220
- justificativa: 
- aprofundar DAN-121: `database overloaded throttle requests services timeout fix mitigation` — Bate exatamente: banco de backend sobrecarregado fazendo throttling de requisições e serviços (incluindo player de vídeo, iPlayer) dando timeout; não bate no componente específico (blogs/iPlayer).
- aprofundar DAN-147: `request queue overloading database capacity cascading failure fix` — Bate com banco sobrecarregado por filas de requisições e falha em cascata; não menciona throttling explícito nem player de vídeo.
- aprofundar DAN-148: `extreme load concurrent users service disruptions mitigation fix` — Bate com sobrecarga geral do sistema causando disrupções; não é específico de banco de dados nem throttling.
  - DAN-121 (llm) [sem seção] 0.479: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.471: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.593: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.582: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-148 (llm) [**Account Service outage**] 0.663: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [**XMPP outage**] 0.659: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme

## q-240 (esperado: DAN-152)

- busca inicial: DAN-009, DAN-175, DAN-140, DAN-152, DAN-177, DAN-015, DAN-017, DAN-124, DAN-131, DAN-028
- justificativa: 
- aprofundar DAN-152: `malicious package published npm registry compromised maintainer account fix` — O DAN-152 envolve pacotes maliciosos publicados em registro público (npm) após comprometimento de conta de mantenedor, o mesmo tipo de falha do incidente atual de pacote não publicado por nós enviando tokens para fora; a diferença é que não sabemos se a origem foi conta comprometida ou outro mecanismo.
  - DAN-152 (llm) [Summary] 0.742: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.741: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-012 (esperado: DAN-211)

- busca inicial: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-066, DAN-222, DAN-113, DAN-101, DAN-133
- justificativa: 
- aprofundar DAN-020: `service discovery config bad client outage root cause fix` — Bate porque menciona service discovery diretamente e falha em cascata; não bate porque causa foi config ruim, não lentidão de escrita.
- aprofundar DAN-211: `Consul service discovery performance degradation root cause fix` — Bate porque Consul é service discovery e houve degradação de performance; não bate porque causa específica é Consul streaming/BoltDB.
- aprofundar DAN-109: `metadata service timeout retry storm root cause fix` — Bate porque envolve timeouts e falha em cascata em serviços dependentes; não bate porque componente é metadata do DynamoDB, não service discovery.
  - DAN-020 (llm) [The failure of a core system] 0.697: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.693: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-211 (llm) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.69: ### Early Triage (10/28 13:37 – 10/29 02:00)  The initial investigation suggested that the Consul cluster that Vault and many other services depend on was unhealthy.  Specifically, the Consul cluster 
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.684: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (causa) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.489: ### Early Triage (10/28 13:37 – 10/29 02:00)  At this point, the team developed a new theory about what was going wrong: increased traffic. Perhaps Consul was slow because our system reached a tipping
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.627: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.573: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-263 (esperado: DAN-200)

- busca inicial: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-073, DAN-146, DAN-106, DAN-069, DAN-066
- justificativa: 
- aprofundar DAN-200: `Mars Pathfinder system reset priority inversion VxWorks patch fix` — O incidente atual descreve reinícios de computador de bordo dias após começar a operar, igual ao Pathfinder em Marte; difere pelo contexto específico da missão marciana.
- aprofundar DAN-198: `Apollo 11 computer restart rendezvous radar CPU load fix` — O computador da Apollo 11 reiniciou durante a pousa lunar, semelhante ao reinício do computador de bordo, mas a causa foi carga excessiva de CPU e não ocorreu dias depois.
  - DAN-200 (llm) [HOW WE FOUND IT] 0.668: ## HOW WE FOUND IT  The software that flies on Mars Pathfinder has several debug features within it that are used in the lab but are not used on the flight spacecraft (not used because some of them pr
  - DAN-200 (llm) [THE FAILURE] 0.634: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.729: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.691: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-032 (esperado: DAN-104)

- busca inicial: DAN-109, DAN-210, DAN-189, DAN-191, DAN-067, DAN-073, DAN-104, DAN-103, DAN-026, DAN-070
- justificativa: 
- aprofundar DAN-104: `human error typo command remove servers S3 outage recovery restart fix` — Bate exatamente: operador executou comando para remover poucos servidores e, por erro/tipo, removeu mais, derrubando serviço de storage (S3) com impacto em cascata. Não bate: é ambiente AWS S3, não storage genérico.
- aprofundar DAN-189: `operator reboot all servers lax input validation outage fix` — Bate parcialmente: comando de operador destinado a poucos servidores afetou muitos mais por falha na ferramenta. Não bate: é reboot, não remoção, e não envolve serviço de storage específico.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.63: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.622: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.654: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.591: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-219 (esperado: DAN-116)

- busca inicial: DAN-066, DAN-126, DAN-103, DAN-222, DAN-205, DAN-209, DAN-116, DAN-109, DAN-191, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update crash root cause fix` — Todos os servidores caíram ao mesmo tempo após uma atualização de banco de dados, com atraso para desencadear o bug, igual ao incidente atual.
  - DAN-116 (llm) [sem seção] 0.739: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.618: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-223 (esperado: DAN-121)

- busca inicial: DAN-147, DAN-148, DAN-101, DAN-129, DAN-134, DAN-219, DAN-164, DAN-121, DAN-144, DAN-094
- justificativa: 
- aprofundar DAN-121: `database overload throttling requests services timing out fix` — Bate exatamente: banco de dados sobrecarregado fazendo throttling de requisições e vários serviços, incluindo player, entrando em timeout.
- aprofundar DAN-147: `database capacity overload cascading failure request queue fix` — Semelhança forte: fila de requisições sobrecarregando capacidade insuficiente do banco, causando falha em cascata.
- aprofundar DAN-101: `connection pool exhaustion database timeouts root cause fix` — Semelhança parcial: timeouts intermitentes de aplicação por esgotamento de pool de conexões do banco, embora a causa raiz seja diferente.
  - DAN-121 (llm) [sem seção] 0.506: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.476: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.61: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.597: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-101 (llm) [sem seção] 0.684: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (llm) [sem seção] 0.683: It wasn’t until a few days later that we realised this was the root of our problems. As the timeouts were intermittent and didn’t occur every day, it took a little while to confirm the issue. But, it’
  - DAN-101 (causa) [sem seção] 0.405: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (correcao) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-101 (correcao) [sem seção] 0.317: Originally, we would receive this event from Slack, and within the lifetime of that HTTP request, we’d perform any responses we needed to, e.g. offering to attach a GitHub link that a user has just po

## q-218 (esperado: DAN-116)

- busca inicial: DAN-126, DAN-146, DAN-103, DAN-066, DAN-209, DAN-106, DAN-048, DAN-191, DAN-116, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update crash all servers root cause fix` — Bate: atualização de banco de dados revelou um bug que fez todos os servidores 'impression bus' caírem simultaneamente, com atraso de tempo para disparar o bug — espelha o incidente atual (servidores caíram após atualização de dados). Não bate: componente específico é 'impression bus', não genérico.
  - DAN-116 (llm) [sem seção] 0.702: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.622: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-229 (esperado: DAN-125)

- busca inicial: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-129, DAN-091, DAN-125
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade peak load cascading collapse fix` — Bate exatamente: banco reduzido recentemente, carga em pico, incapacidade de atender carga e colapso em cascata de servidores dependentes; não especifica o componente de banco usado.
- aprofundar DAN-147: `cascading failure insufficient database capacity request queue fix` — Bate em falha em cascata causada por fila sobrecarregando capacidade insuficiente do banco; não menciona downsizing recente.
- aprofundar DAN-096: `peak hour load mysql cluster ProxySQL connection exhaustion fix` — Bate em carga de pico sobre cluster de banco de dados compartilhado; não menciona redução de capacidade nem falha em cascata direta de servidores dependentes.
  - DAN-125 (llm) [Database performance issues] 0.652: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.555: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.627: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.591: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.708: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.685: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev

## q-262 (esperado: DAN-200)

- busca inicial: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073, DAN-189, DAN-146, DAN-210, DAN-043, DAN-200
- justificativa: 
- aprofundar DAN-200: `priority inversion VxWorks system reset patch priority inheritance root cause fix` — Bate: computador de bordo reiniciando sozinho dias após entrar em operação (Mars Pathfinder, poucos dias após pouso). Não bate: causa foi inversão de prioridade no VxWorks, ainda não confirmada no incidente atual.
- aprofundar DAN-198: `rendezvous radar CPU load spacecraft computer restart root cause fix Apollo 11` — Bate: computador espacial reiniciando por sobrecarga. Não bate: gatilho foi radar durante pouso lunar, não dias após início da operação.
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.654: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [THE FAILURE] 0.632: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.741: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.711: | TALES FROM THE LUNAR MODULE GUIDANCE COMPUTER Don Eyles | | (A paper presented to the 27th annual Guidance and Control Conference of the American Astronautical Society (AAS), in Breckenridge, Colora
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-228 (esperado: DAN-125)

- busca inicial: DAN-164, DAN-147, DAN-156, DAN-048, DAN-096, DAN-043, DAN-094, DAN-209, DAN-134, DAN-109
- justificativa: 
- aprofundar DAN-147: `database capacity insufficient cascading failure root cause fix remediation` — Bate: falha em cascata devido a capacidade insuficiente do banco de dados sob carga. Não bate: não menciona redução recente do tamanho do banco.
- aprofundar DAN-096: `peak hour load mysql cluster ProxySQL connections exhausted failover fix` — Bate: carga de pico sobrecarregando cluster de banco de dados com impacto em servidores dependentes. Não bate: foco em ProxySQL e conexões, não em redução de tamanho.
- aprofundar DAN-164: `influx requests overloaded database replication lag root cause fix` — Bate: influxo de requisições sobrecarregando o banco de dados. Não bate: inclui erro humano excluindo diretório, que não está no incidente atual.
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.579: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.528: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.718: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.691: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev
  - DAN-164 (llm) [Root cause analysis] 0.703: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.684: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-034 (esperado: DAN-004)

- busca inicial: DAN-005, DAN-137, DAN-051, DAN-012, DAN-220, DAN-011, DAN-016, DAN-014, DAN-006, DAN-113
- justificativa: 
- aprofundar DAN-051: `iptables firewall configuration blocked traffic root cause fix rollback` — é o único que cita firewall bloqueando todo tráfego por mudança incorreta de configuração, igual ao incidente atual.
- aprofundar DAN-006: `typo network configuration traffic datacenter root cause fix` — envolve mudança acidental de configuração de rede que afeta tráfego, mas não cita especificamente regra de firewall.
- aprofundar DAN-014: `human error disabled service admin tooling root cause fix` — envolve erro humano em ferramenta administrativa que desativou serviço, sem relação direta com firewall.
  - DAN-051 (llm) [sem seção] 0.61: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-051 (llm) [sem seção] 0.603: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-006 (llm) [sem seção] 0.585: Today a configuration error in our backbone network caused an outage for Internet properties and Cloudflare services that lasted 27 minutes. We saw traffic drop by about 50% across our network. Becaus
  - DAN-006 (llm) [Conclusion] 0.574: ### Conclusion  We’ve never experienced an outage on our backbone and our team responded quickly to restore service in the affected locations, but this was a very painful period for everyone involved.
  - DAN-006 (causa) [Timeline] 0.391: ### Timeline  All timestamps are UTC.  First, an issue occurred on the backbone link between Newark and Chicago which led to backbone congestion in between Atlanta and Washington, DC.  In responding t
  - DAN-006 (correcao) [What happened and what we’re doing about it] 0.372: ### What happened and what we’re doing about it  - Introduce a maximum-prefix limit on our backbone BGP sessions - this would have shut down the backbone in Atlanta, but our network is built to functi
  - DAN-006 (correcao) [What happened and what we’re doing about it] 0.314: ### What happened and what we’re doing about it  As there was backbone congestion in Atlanta, the team had decided to remove some of Atlanta’s backbone traffic. But instead of removing the Atlanta rou
  - DAN-014 (llm) [Deep dive] 0.624: ## Deep dive  **Due to human error and insufficient validation safeguards in our admin tooling, the R2 Gateway service was taken down as part of a routine remediation for a phishing URL.**  During a r
  - DAN-014 (llm) [Incident timeline and impact] 0.582: ## Incident timeline and impact  | | 2025-02-06 08:42 | Root cause identified as R2 team reviews service deployment history and configuration, which surfaces the action and the validation gap that all
  - DAN-014 (causa) [Incident timeline and impact] 0.428: ## Incident timeline and impact  The incident timeline, including the initial impact, investigation, root cause, and remediation, are detailed below.  **All timestamps referenced are in Coordinated Un
  - DAN-014 (correcao) [Remediation and follow-up steps] 0.593: ## Remediation and follow-up steps  We’re continuing to discuss & review additional steps and effort that can continue to reduce the blast radius of any system- or human- action that could result in d
  - DAN-014 (correcao) [Remediation and follow-up steps] 0.539: ## Remediation and follow-up steps  We have taken immediate steps to resolve the validation gaps in our tooling to prevent this specific failure from occurring in the future.  We are prioritizing seve

## q-243 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210, DAN-209, DAN-205, DAN-129, DAN-109, DAN-145
- justificativa: 
- aprofundar DAN-011: `root cause fix permissions database bot detection outage` — É um CDN (Cloudflare) com pane mundial/sistêmica, igual ao incidente atual, embora o gatilho descrito (permissão/arquivo) seja diferente.
- aprofundar DAN-008: `root cause fix Tiered Cache 530 error change` — É um CDN (Cloudflare) com erros em requisições, bate no componente, mas difere no escopo (parcial, não mundial).
- aprofundar DAN-026: `root cause fix DNS Puppet nameserver zone file outage` — Semelha no sintoma de servidores retornando erro, mas difere no componente (DNS, não CDN).
  - DAN-011 (llm) [Remediation and follow-up steps] 0.623: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [Remediation and follow-up steps] 0.583: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [How Cloudflare processes requests, and how this went wrong today] 0.393: ## How Cloudflare processes requests, and how this went wrong today  This feature file is refreshed every few minutes and published to our entire network and allows us to react to variations in traffi
  - DAN-008 (llm) [sem seção] 0.734: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.673: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-026 (llm) [What happened…] 0.734: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.721: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto

## q-260 (esperado: DAN-197)

- busca inicial: DAN-066, DAN-106, DAN-067, DAN-029, DAN-209, DAN-220, DAN-154, DAN-205, DAN-008, DAN-133
- justificativa: 
- aprofundar DAN-106: `EC2 RDS disruption human error networking upgrade root cause fix remediation` — Bate: é uma interrupção de provedor de nuvem (Amazon) sem mudança do cliente, afetando APIs. Não bate: envolve erro humano em upgrade de rede, não uma falha súbita sem causa aparente.
- aprofundar DAN-066: `Byzantine failure partial switch misbehavior cascading API outage root cause fix` — Bate: falha súbita na disponibilidade de API sem mudança do cliente. Não bate: é infraestrutura própria do Cloudflare, não um provedor de nuvem externo chamado por nós.
- aprofundar DAN-067: `Control Plane Analytics outage power failure thundering herd API root cause fix` — Bate: chamadas de API falhando inesperadamente, sem mudança do cliente. Não bate: causado por falha de energia em data center, não por problema no provedor de nuvem chamado.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.672: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.67: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.644: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.616: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-067 (llm) [Lessons and Remediation] 0.724: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Disaster Recovery] 0.699: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 

## q-242 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-109, DAN-026, DAN-129, DAN-145, DAN-106, DAN-009, DAN-008, DAN-067, DAN-016
- justificativa: 
- aprofundar DAN-011: `root cause fix permission database bot detection file size limit network outage` — Cloudflare é uma CDN e a mudança de configuração provocou um outage sistêmico propagado pela rede, igual a uma CDN caindo de repente no mundo todo; difere porque a causa é um arquivo de bot-detection, não erro genérico de servidores.
- aprofundar DAN-016: `root cause fix DDoS mitigation rule rate limiting infinite loop CPU data centers` — Falha após deploy em Cloudflare que se espalhou por data centers com loops de CPU, semelhante a uma queda repentina de CDN distribuída; difere porque o sintoma é CPU a 100%, não servidores devolvendo erro.
- aprofundar DAN-009: `root cause fix service tokens code release Cloudflare CDN control plane outage` — Erro ao lançar código que gerencia service tokens degradou a CDN globalmente da Cloudflare, batendo com CDN afetada por mudança; difere porque o escopo incluiu Workers e Zero Trust, não apenas CDN.
  - DAN-011 (llm) [sem seção] 0.635: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (llm) [Remediation and follow-up steps] 0.602: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.665: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.655: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-009 (llm) [sem seção] 0.732: Several Cloudflare services became unavailable for 121 minutes on January 24, 2023 due to an error releasing code that manages service tokens. The incident degraded a wide range of Cloudflare products
  - DAN-009 (llm) [Incident Timeline] 0.714: ### Incident Timeline  *All Timestamps are UTC*  At 2023-01-24 16:55 the Access engineering team initiated the release that inadvertently began to overwrite service token metadata, causing the inciden
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [How did we fix the issue?] 0.483: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i

## q-261 (esperado: DAN-197)

- busca inicial: DAN-067, DAN-066, DAN-220, DAN-154, DAN-029, DAN-008, DAN-133, DAN-106, DAN-205, DAN-209
- justificativa: 
- aprofundar DAN-066: `Byzantine switch failure API outage cause remediation` — API de provedor cloud (Cloudflare) falhou sem mudança do cliente, semelhante ao incidente atual; difere por afetar também o dashboard e envolver comportamento bizantino de switch.
- aprofundar DAN-106: `networking upgrade human error EC2 outage cause fix` — interrupção de provedor cloud (Amazon EC2/RDS) afetando clientes externamente, mas causada por erro humano e upgrade interno da provedora.
- aprofundar DAN-067: `data center power failure API outage cause fix` — chamadas de API falharam por falha de infraestrutura do provedor cloud (Cloudflare), embora envolva falha de energia e problema de thundering herd na recuperação.
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.639: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.629: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.68: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Customers also experienced elevated error rates until Noon PDT on April 21st when attempting to launch new EBS-ba
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.674: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-067 (llm) [Attempting to Restore Power] 0.717: ### Attempting to Restore Power  While we haven't gotten official confirmation, we have been told by employees that three things hampered getting the generators back online. First, they needed to be p
  - DAN-067 (llm) [Lessons and Remediation] 0.688: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
