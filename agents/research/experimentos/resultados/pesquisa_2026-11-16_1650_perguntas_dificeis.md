# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | descartado | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | sim | sim | não | não | sim | 0 | 160 |
| q-022 | DAN-104 | 4 | sim | sim | não | não | sim | 0 | 142 |
| q-170 | DAN-018 | 4 | sim | sim | não | não | sim | 0 | 137 |
| q-171 | DAN-018 | 4 | sim | sim | não | não | sim | 0 | 138 |
| q-222 | DAN-121 | 4 | sim | sim | não | não | sim | 0 | 157 |
| q-240 | DAN-152 | 4 | sim | sim | não | não | sim | 0 | 206 |
| q-012 | DAN-211 | 5 | sim | sim | não | não | sim | 0 | 158 |
| q-263 | DAN-200 | 5 | sim | sim | não | não | sim | 0 | 149 |
| q-032 | DAN-104 | 7 | não | não | não | não | não | 0 | 161 |
| q-219 | DAN-116 | 7 | não | não | não | não | não | 0 | 167 |
| q-223 | DAN-121 | 8 | não | não | não | não | não | 0 | 183 |
| q-218 | DAN-116 | 9 | não | não | não | não | não | 0 | 165 |
| q-229 | DAN-125 | 10 | não | não | não | não | não | 0 | 174 |
| q-262 | DAN-200 | 10 | não | não | não | não | não | 0 | 174 |
| q-228 | DAN-125 | 11 | não | não | não | não | não | 0 | 156 |
| q-034 | DAN-004 | 12 | não | não | não | não | não | 0 | 155 |
| q-243 | DAN-154 | 12 | não | não | não | não | não | 0 | 170 |
| q-260 | DAN-197 | 19 | não | não | não | não | não | 0 | 470 |
| q-242 | DAN-154 | — | não | não | não | não | não | 0 | 178 |
| q-261 | DAN-197 | — | não | não | não | não | não | 0 | 161 |

## q-020 (esperado: DAN-164)

- busca inicial: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048
- justificativa: Selecionamos DAN‑043, que descreve exatamente a exclusão acidental do banco de produção e os passos de restauração de backup. DAN‑056 também traz lições sobre truncamento acidental via variável de ambiente, oferecendo práticas de isolamento e backup. DAN‑164 reflete a remoção acidental de diretório de dados primários, relevante para entender como evitar erros similares. Os outros incidentes não trazem cenário alinhado ao caso atual.
- aprofundar DAN-043: `accidentally deleted production database maintenance backup recovery fix`
- aprofundar DAN-056: `environment variable DATABASEURL test truncate production database recovery steps`
- aprofundar DAN-164: `accidental deletion primary database directory data lost recovery fix`
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.708: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.66: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (fixa) [Some perspective] 0.449: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-056 (llm) [Remediation] 0.751: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (llm) [What We Learned] 0.722: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (fixa) [Conclusion] 0.478: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-164 (llm) [Timeline] 0.675: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (llm) [Root cause analysis] 0.652: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (fixa) [Improving recovery procedures] 0.461: ## Improving recovery procedures  If you think there are additional measures we can take to prevent incidents like this please let us know in the comments.

## q-022 (esperado: DAN-104)

- busca inicial: DAN-191, DAN-189, DAN-146, DAN-104, DAN-064
- justificativa: DAN‑189 e DAN‑104 descrevem exatamente remoção de servidores por erro de operador, semelhante ao incidente atual. DAN‑191 envolve falha de firmware em hardware de storage, e DAN‑146 trata de um script de upgrade, não remoção de servidores; ambos são superficiais em relação ao contexto de remoção.
- aprofundar DAN-189: `operator typo all servers reboot root cause fix`
- aprofundar DAN-104: `operator removed servers typo root cause fix`
- descartou: DAN-191, DAN-146
  - DAN-189 (llm) [What Happened?] 0.644: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [What Happened?] 0.55: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (fixa) [Closing] 0.482: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.398: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.381: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper

## q-170 (esperado: DAN-018)

- busca inicial: DAN-144, DAN-066, DAN-017, DAN-018, DAN-029
- justificativa: Os incidentes selecionados apresentam falhas de front‑end ou rede que geram chamadas em massa (thundering herd) para a API/dashboards, similar ao que ocorre aqui, e fornecem detalhes de causa raiz e correções. Nenhuma busca adicional foi necessária.
- aprofundar DAN-018: `React dependency array misconfigured causing excessive API calls dashboard Thundering Herd fix`
- aprofundar DAN-144: `thundering herd reconnecting internal service memory exhaustion mitigation`
- aprofundar DAN-066: `partial switch misbehavior cascading API dashboard failure redundancy handling`
  - DAN-018 (llm) [What Happened] 0.687: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.681: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (fixa) [How we responded] 0.475: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (fixa) [Going forward] 0.459: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-144 (llm) [Summary] 0.581: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.552: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (fixa) [Action Items / Response] 0.484: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (fixa) [Investigation and Analysis] 0.463: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-066 (llm) [The Dashboard] 0.681: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [sem seção] 0.668: *An analysis of the Cloudflare API availability incident on 2020-11-02*  When we review design documents at Cloudflare, we are always on the lookout for Single Points of Failure (SPOFs). Eliminating t
  - DAN-066 (fixa) [Redundant Points of Failure] 0.512: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (fixa) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.484: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se

## q-171 (esperado: DAN-018)

- busca inicial: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067
- justificativa: DAN‑018 descreve exatamente um bug no dashboard que gerou chamadas repetidas ao serviço interno, causando falhas nos APIs e no painel; as demais incidências têm causas diferentes e são descartadas.
- aprofundar DAN-018: `Tenant Service API flood dashboard calls thundering herd bug`
- descartou: DAN-066, DAN-144, DAN-029
  - DAN-018 (llm) [What Happened] 0.741: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.711: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (fixa) [How we responded] 0.475: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (fixa) [Going forward] 0.459: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e

## q-222 (esperado: DAN-121)

- busca inicial: DAN-129, DAN-144, DAN-147, DAN-121, DAN-016
- justificativa: O incidente atual envolve sobresaturação do banco de dados e limitação de requisições, condição semelhante ao caso BBC (DAN-121) e aoenqueue de requisições “DUO1” (DAN-147). Os demais incidentes tratam de falhas de timeout de health check, thundering herd ou CPU loop, não correlacionando-se com a causa raiz descrita.
- aprofundar DAN-121: `BBC iPlayer database overload root cause steps`
- aprofundar DAN-147: `DUO1 request queue overload root cause database capacity`
- descartou: DAN-129, DAN-144, DAN-016
  - DAN-121 (llm) [sem seção] 0.715: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.659: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.733: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.686: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (fixa) [Authentication Latency on DUO1 Deployment] 0.456: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 

## q-240 (esperado: DAN-152)

- busca inicial: DAN-009, DAN-175, DAN-140, DAN-152, DAN-177
- justificativa: O incidente atual descreve um pacote que, apesar de não ter sido publicado, está enviando tokens de acesso. O caso mais semelhante na lista é o DAN‑152, onde um pacote malicioso exfiltra tokens de acesso do arquivo .npmrc. Os outros incidentes abordam vazamento interno ou rotinas de token, mas não a exfiltração de tokens por pacotes dependentes, então foram descartados.
- aprofundar DAN-152: `malicious package exfiltrate .npmrc token postinstall script`
- descartou: DAN-009, DAN-175, DAN-140, DAN-177
  - DAN-152 (llm) [Timeline] 0.722: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Summary] 0.671: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (fixa) [Attack Method] 0.306: ## Attack Method  Further details on the attack can be found here.

## q-012 (esperado: DAN-211)

- busca inicial: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211
- justificativa: DAN-020 e DAN-211 descrevem falhas no serviço de descoberta por carga excessiva e latência nas gravações, mirroring o cenário de baixa performance e timeouts. Os outros incidentes não abordam diretamente a descoberta e gravações lenta.
- aprofundar DAN-020: `service discovery thundering herd root cause recovery fix`
- aprofundar DAN-211: `Consul KV write latency root cause mitigation`
- descartou: DAN-220, DAN-109
  - DAN-020 (llm) [A thundering herd] 0.746: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.694: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (fixa) [How do we avoid it in the future?] 0.525: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (fixa) [Setting the stage] 0.492: ## Setting the stage  We traced the origin of the failure to a routine operation by an authorized engineer early that day, on a small-sized cluster, that is itself a dependency of a much larger data i
  - DAN-211 (llm) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.699: ### Early Triage (10/28 13:37 – 10/29 02:00)  At this point, the team developed a new theory about what was going wrong: increased traffic. Perhaps Consul was slow because our system reached a tipping
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.656: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  But what was going on with the slow leaders? We did not figure this out during the incident, but HashiCorp engineers determined the root cause in the
  - DAN-211 (fixa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.554: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 

## q-263 (esperado: DAN-200)

- busca inicial: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200
- justificativa: O incidente atual é semelhante ao reset por prioridade invertida do Pathfinder (DAN-200) e também pode ser causado por sobrecarga de CPU como no Apollo 11 (DAN-198).
- aprofundar DAN-200: `priority inversion reset VxWorks task scheduler`
- aprofundar DAN-198: `CPU load restart Apollo 11 computer radar fault`
  - DAN-200 (llm) [THE FAILURE] 0.689: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [THE SOFTWARE ARCHITECTURE] 0.619: ## THE SOFTWARE ARCHITECTURE  The bc_sched and bc_dist tasks check each cycle to be sure that the other had completed its execution. The bc_sched task is the highest priority task in the system (excep
  - DAN-200 (fixa) [HOW WE FOUND IT] 0.486: ## HOW WE FOUND IT  The software that flies on Mars Pathfinder has several debug features within it that are used in the lab but are not used on the flight spacecraft (not used because some of them pr
  - DAN-198 (llm) [sem seção] 0.697: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.647: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (fixa) [sem seção] 0.426: | Many explanations have been offered for why the RR was configured in this way for the lunar landing. For example, a fanciful scheme for monitoring the landing by comparing RR data to a chart of expe

## q-032 (esperado: DAN-104)

- busca inicial: DAN-109, DAN-210, DAN-189, DAN-191, DAN-067
- justificativa: O incidente atual envolve erro de operador que removeu servidores, semelhante ao DAN‑189, onde um comando mal‑digitado reiniciou todos os nós causando queda de armazenamento. O DAN‑109 descreve falha de servidores de armazenamento e sobrecarga do serviço de metadados, oferecendo lições sobre loops de retry e recuperação nesses cenários.
- aprofundar DAN-189: `operator rebooted all instances cause storage outage recovery`
- aprofundar DAN-109: `metadata service overload storage node failure retry loop cause recovery`
  - DAN-189 (llm) [What Happened?] 0.691: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.627: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (fixa) [Closing] 0.482: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.63: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.594: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (fixa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.417: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 

## q-219 (esperado: DAN-116)

- busca inicial: DAN-066, DAN-126, DAN-103, DAN-222, DAN-205
- justificativa: DAN-126 contém histórico de servidores que falharam após atualização; os outros dois incidentes podem oferecer exemplos de falha sóbrio quando dados são alterados e propagam falhas.

- aprofundar DAN-126: `crash after update all servers`
- aprofundar DAN-066: `data update caused server crash all servers`
- aprofundar DAN-222: `database update led to server crash all services`
  - DAN-126 (llm) [Server Configurations] 0.674: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (llm) [Server Configurations] 0.596: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (fixa) [sem seção] 0.479: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (fixa) [Server Configurations] 0.471: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.591: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (llm) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.585: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-066 (fixa) [Redundant Points of Failure] 0.512: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-222 (llm) [sem seção] 0.53: On Wednesday, October 23, around 9:45am ET, the Stackdriver Intelligent Monitoring application suffered an outage. We sincerely apologize for this incident. We know that you depend on Stackdriver to h
  - DAN-222 (llm) [sem seção] 0.525: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (fixa) [sem seção] 0.474: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (fixa) [sem seção] 0.453: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff

## q-223 (esperado: DAN-121)

- busca inicial: DAN-147, DAN-148, DAN-101, DAN-129, DAN-134
- justificativa: Asincidentes DAN‑147, DAN‑148 e DAN‑101 abordam sobrecarga do banco, fila de backlog ou esgotamento do pool de conexões, que se alinham diretamente com a sobrecarga e os timeouts relatados. DAN‑129 e DAN‑134 têm foco em timeout de saúde ou RabbitMQ e não refletem o mesmo tipo de falha do incidente atual.
- aprofundar DAN-147: `database overload queue backlog root cause and remediation`
- aprofundar DAN-148: `connection pool starvation DB throttling root cause fix`
- aprofundar DAN-101: `database connection pool exhaustion root cause and resolution`
- descartou: DAN-129, DAN-134
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.615: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.575: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (fixa) [Authentication Latency on DUO1 Deployment] 0.456: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-148 (llm) [Postmortem of Service Outage at 3.4M CCU] 0.734: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (llm) [**Cloud capacity limits and throttling**] 0.641: ### **Cloud capacity limits and throttling**  - **Identify and resolve the root cause of our DB performance issues.** We’ve flown Mongo experts on-site to analyze our DB and usage, as well as provide 
  - DAN-148 (fixa) [**Account Service outage**] 0.512: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (fixa) [**XMPP outage**] 0.512: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-101 (llm) [sem seção] 0.638: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (llm) [sem seção] 0.636: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (fixa) [sem seção] 0.463: It wasn’t until a few days later that we realised this was the root of our problems. As the timeouts were intermittent and didn’t occur every day, it took a little while to confirm the issue. But, it’

## q-218 (esperado: DAN-116)

- busca inicial: DAN-126, DAN-146, DAN-103, DAN-066, DAN-209
- justificativa: O incidente atual parece resultado de uma atualização de dados que deixou servidores em estado inconsistente ou mal configurado, causando falha simultânea. DAN-126 descreve exatamente essa situação. DAN‑146 pode indicar um bug na rotina de atualização que limpa máquinas em uso, e DAN‑209 mostra como migração parcial pode levar a desligamento coletivo de servidores. Todos são relevantes para verificar causa raiz e correções.
- aprofundar DAN-126: `server misconfig after data update crash root cause fix`
- aprofundar DAN-146: `upgrade script bug wiped machines data loss fix`
- aprofundar DAN-209: `autoscaler misread zookeeper migration shut down servers fix`
  - DAN-126 (llm) [Server Configurations] 0.65: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (llm) [Server Configurations] 0.638: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (fixa) [sem seção] 0.479: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (fixa) [Server Configurations] 0.471: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-146 (llm) [sem seção] 0.614: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [sem seção] 0.546: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri
  - DAN-209 (llm) [sem seção] 0.553: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.54: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 

## q-229 (esperado: DAN-125)

- busca inicial: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094
- justificativa: DAN‑147, 096 e 094 descrevem falhas por pico de carga que levaram a falhas em cascata de serviços dependentes e destacam mitigação ligada ao banco. DAN‑156 e 164 resolvem questões diferentes (memória e exclusão acidental).
- aprofundar DAN-147: `identify request queue overload root cause and mitigation steps`
- aprofundar DAN-096: `find peak hour load causing ProxySQL exhaustion and backup plan`
- aprofundar DAN-094: `locate load-driven incidents triggered ProxySQL meltdowns during peak hours`
- descartou: DAN-156, DAN-164
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.6: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.583: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (fixa) [Authentication Latency on DUO1 Deployment] 0.456: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.66: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.65: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (fixa) [Next steps] 0.456: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-094 (llm) [2020, February 20 21:31 UTC (lasting for 47 minutes)] 0.736: ## 2020, February 20 21:31 UTC (lasting for 47 minutes)  Two days later, as part of a planned master database promotion, we saw unexpectedly high load which triggered a similar ProxySQL failure. The i
  - DAN-094 (llm) [Timeline] 0.71: ## Timeline  ## 2020, February 19 15:17 UTC (lasting for 52 minutes)  At this time, an unexpectedly resource-intensive query began running against our mysql1 database cluster. The intent was to run th
  - DAN-094 (fixa) [Optimizing for stability] 0.474: ## Optimizing for stability  We decided to freeze production deployments for three days to address short-term hotspotting as a result of the final incident on February 27. This helped us stabilize Git

## q-262 (esperado: DAN-200)

- busca inicial: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073
- justificativa: O incidente envolve reboot espontâneo pós‑operação, semelhante ao de Apollo 11 que reiniciou por carga excessiva da CPU. Os demais incidentes tratam de falha de hardware, réplica de banco ou armazenamento, não relacionados ao reboot por sobrecarga do sistema.
- aprofundar DAN-198: `Apollo 11 radar excess CPU reboot`
- descartou: DAN-103, DAN-066, DAN-191, DAN-073
  - DAN-198 (llm) [sem seção] 0.667: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.666: This phenomenon occurred whenever the RR mode was in SLEW or AUTO, regardless of whether the rendezvous radar itself was powered up. | | The CDU interface counters in the LGC were incremented or decre
  - DAN-198 (fixa) [sem seção] 0.426: | Many explanations have been offered for why the RR was configured in this way for the lunar landing. For example, a fanciful scheme for monitoring the landing by comparing RR data to a chart of expe

## q-228 (esperado: DAN-125)

- busca inicial: DAN-164, DAN-147, DAN-156, DAN-048, DAN-096
- justificativa: Selecionamos incidentes que envolvem sobrecarga de banco de dados em horário de pico, falhas em cascata e insuficiência de capacidade — todos relevantes ao caso atual. Cada consulta busca a causa raiz e a correção especificamente citadas no postmortem. No momento não há necessidade de novas buscas.
- aprofundar DAN-147: `find root cause database overload queue max limit fix`
- aprofundar DAN-096: `identify peak load proxy memory profiling degrade connections mitigation`
- aprofundar DAN-164: `locate replication lag overload causes and recovery steps`
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.641: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.608: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (fixa) [Authentication Latency on DUO1 Deployment] 0.456: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.648: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.568: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (fixa) [Next steps] 0.456: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-164 (llm) [Timeline] 0.647: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.613: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (fixa) [Improving recovery procedures] 0.461: ## Improving recovery procedures  If you think there are additional measures we can take to prevent incidents like this please let us know in the comments.

## q-034 (esperado: DAN-004)

- busca inicial: DAN-005, DAN-137, DAN-051, DAN-012, DAN-220
- justificativa: DAN‑051 descreve exatamente uma regra de firewall errada bloqueando todo tráfego e a correção via revert. DAN‑005 mostra outro tipo de regra defeituosa em roteadores; investigar mudará de cenário. DAN‑012 tem falha interna de WAF; não pertence ao caso atual. Nenhuma nova pesquisa é necessária.
- aprofundar DAN-051: `iptables HAProxy blocking traffic revert times`
- aprofundar DAN-005: `router bad rule packet-length RAM crash mitigation`
- aprofundar DAN-012: `WAF Lua exception test rule disable rollback`
- descartou: DAN-137
  - DAN-051 (llm) [sem seção] 0.641: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-051 (llm) [sem seção] 0.604: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-005 (llm) [Bad Rule] 0.745: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Flowspec] 0.523: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-005 (fixa) [Incident Response] 0.445: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-012 (llm) [The runtime error] 0.636: ### The runtime error  Cloudflare’s rulesets system consists of sets of rules which are evaluated for each request entering our system. A rule consists of a filter, which selects some traffic, and an 
  - DAN-012 (llm) [What happened] 0.613: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (fixa) [What about the changes being made after the incident on November 18, 2025?] 0.466: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (fixa) [sem seção] 0.433: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf

## q-243 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210
- justificativa: Selecionamos incidentes que tratam especificamente de falhas globais no CDN por erro de configuração ou rollback de cache e excluímos aqueles que afetam apenas controle de plano ou DNS.
- aprofundar DAN-011: `ClickHouse permission change bad config file CDN outage issue resolution`
- aprofundar DAN-008: `Tiered Cache change 530 error CDN global outage rollback cause`
- aprofundar DAN-210: `Kubernetes upgrade network failure CDN edge DNS not working logs`
- descartou: DAN-067, DAN-026
  - DAN-011 (llm) [The outage] 0.657: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (llm) [The outage] 0.599: ## The outage  As well as returning HTTP 5xx errors, we observed significant increases in latency of responses from our CDN during the impact period. This was due to large amounts of CPU being consume
  - DAN-011 (fixa) [Remediation and follow-up steps] 0.483: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-008 (llm) [sem seção] 0.775: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Incident timeline and impact] 0.732: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-008 (fixa) [Conclusion] 0.497: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (fixa) [Incident timeline and impact] 0.473: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-210 (llm) [It Begins] 0.732: ## It Begins  All at once the site came to a screeching halt. We opened an incident immediately, and brought all hands on deck, trying to figure out what had happened. Hands were on deck and in the ca
  - DAN-210 (llm) [It Begins] 0.644: ## It Begins  It’s funny in an ironic sort of way. As a team, we had just finished up an internal postmortem for a previous Kubernetes upgrade that had gone poorly; but only mildly, and for an entirel
  - DAN-210 (fixa) [A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack] 0.494: ## A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack  The route reflectors were set up several years ago by the precursor to the current Compute team. Time passed, and with att
  - DAN-210 (fixa) [Get to the Point, Spock, If You Have One] 0.491: ## Get to the Point, Spock, If You Have One  How did it actually break? That’s one of the most unexpected things of all. In doing the research, we discovered that the way that the route reflectors wer

## q-260 (esperado: DAN-197)

- busca inicial: DAN-066, DAN-106, DAN-067, DAN-029, DAN-209
- justificativa: Selecionamos incidentes de falhas de APIs de provedores de nuvem (AWS, Cloudflare) que não envolvem mudanças internas. Descartamos incidentes internos (GoCardless, Reddit).
- aprofundar DAN-106: `Amazon EC2 EBS networking upgrade human error impact API outage cause root`
- aprofundar DAN-066: `Cloudflare control plane API failure switch misbehavior root cause`
- aprofundar DAN-067: `Cloudflare API outage thundering herd power failure root cause`
- descartou: DAN-029, DAN-209
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.743: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  By 5:30 AM PDT, error rates and latencies again increased for EBS API calls across the Region. When data for a vo
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.742: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  After the initial sequence of events described above, the degraded EBS cluster had an immediate impact on the EBS
  - DAN-106 (fixa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.426: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (fixa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.399: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-066 (llm) [sem seção] 0.713: *An analysis of the Cloudflare API availability incident on 2020-11-02*  When we review design documents at Cloudflare, we are always on the lookout for Single Points of Failure (SPOFs). Eliminating t
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.656: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (fixa) [Redundant Points of Failure] 0.512: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (fixa) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.484: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-067 (llm) [Lessons and Remediation] 0.737: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Disaster Recovery] 0.716: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (fixa) [Attempting to Restore Power] 0.453: ### Attempting to Restore Power  While we haven't gotten official confirmation, we have been told by employees that three things hampered getting the generators back online. First, they needed to be p

## q-242 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-109, DAN-026, DAN-129, DAN-145
- justificativa: O incidente DAN-011 descreve exatamente uma queda mundial de CDN causada por arquivos de configuração incorretos gerados por ClickHouse, semelhante ao cenário atual. Derivamos consultas específicas para localizar a causa raiz e a correção dentro desse post‑mortem.
- aprofundar DAN-011: `clickhouse query permissions change bad config file crash`
  - DAN-011 (llm) [The query behaviour change] 0.664: ### The query behaviour change  ``` SELECT   name,   type FROM system.columns WHERE   table = 'http_requests_features' order by name; ``` Note how the query does not filter for the database name. With
  - DAN-011 (llm) [The query behaviour change] 0.642: ### The query behaviour change  I mentioned above that a change in the underlying query behaviour resulted in the feature file containing a large number of duplicate rows. The database system in quest
  - DAN-011 (fixa) [Remediation and follow-up steps] 0.483: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (fixa) [The outage] 0.477: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T

## q-261 (esperado: DAN-197)

- busca inicial: DAN-067, DAN-066, DAN-220, DAN-154, DAN-029
- justificativa: DAN-067 e DAN-066 descrevem falhas no API de Cloudflare, semelhante ao nosso problema envolvendo chamadas a um provedor de nuvem. As consultas são focadas em encontrar a causa raiz e a correção nesses casos. Outros incidentes foram descartados por não terem relação direta.
- aprofundar DAN-067: `cloud provider API failure root cause fix Cloudflare`
- aprofundar DAN-066: `Cloudflare API outage cause root fix`
- descartou: DAN-154, DAN-029, DAN-220
  - DAN-067 (llm) [Lessons and Remediation] 0.732: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Disaster Recovery] 0.723: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (fixa) [Attempting to Restore Power] 0.453: ### Attempting to Restore Power  While we haven't gotten official confirmation, we have been told by employees that three things hampered getting the generators back online. First, they needed to be p
  - DAN-066 (llm) [sem seção] 0.691: *An analysis of the Cloudflare API availability incident on 2020-11-02*  When we review design documents at Cloudflare, we are always on the lookout for Single Points of Failure (SPOFs). Eliminating t
  - DAN-066 (llm) [The Dashboard] 0.645: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (fixa) [Redundant Points of Failure] 0.512: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (fixa) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.484: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
