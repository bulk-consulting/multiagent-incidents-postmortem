# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | sim | sim | search | não | sim | 0 | 5 |
| q-022 | DAN-104 | 4 | sim | sim | search | não | sim | 0 | 6 |
| q-170 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 22 |
| q-171 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 12 |
| q-222 | DAN-121 | 4 | sim | sim | search | não | sim | 0 | 34 |
| q-240 | DAN-152 | 4 | sim | sim | search | não | sim | 0 | 10 |
| q-012 | DAN-211 | 5 | sim | sim | search | não | sim | 0 | 9 |
| q-263 | DAN-200 | 5 | sim | sim | search | não | sim | 0 | 22 |
| q-032 | DAN-104 | 7 | sim | sim | search | não | sim | 0 | 13 |
| q-219 | DAN-116 | 7 | sim | sim | (texto) → search | não | sim | 0 | 56 |
| q-223 | DAN-121 | 8 | sim | sim | search | não | sim | 0 | 24 |
| q-218 | DAN-116 | 9 | sim | sim | search | não | sim | 0 | 9 |
| q-229 | DAN-125 | 10 | sim | sim | search | não | sim | 0 | 9 |
| q-262 | DAN-200 | 10 | sim | sim | search | não | sim | 0 | 17 |
| q-228 | DAN-125 | 11 | não | não | search | não | não | 0 | 33 |
| q-034 | DAN-004 | 12 | não | não | search | não | não | 0 | 14 |
| q-243 | DAN-154 | 12 | não | não | search | não | não | 0 | 9 |
| q-260 | DAN-197 | 19 | não | não | search | não | não | 0 | 11 |
| q-242 | DAN-154 | — | não | não | search | não | não | 0 | 14 |
| q-261 | DAN-197 | — | não | não | search | não | não | 0 | 17 |

## q-020 (esperado: DAN-164)

- busca inicial: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-091, DAN-186, DAN-092, DAN-066, DAN-058
- justificativa: 
- aprofundar DAN-043: `accidental database deletion production backup restore` — Same accidental deletion during maintenance; managed DB with daily backups like current incident.
- aprofundar DAN-164: `admin deleted wrong directory database replication data loss` — Accidental deletion by admin, similar context of data loss during operations.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.741: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.675: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Root cause analysis] 0.648: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.618: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-022 (esperado: DAN-104)

- busca inicial: DAN-191, DAN-189, DAN-146, DAN-104, DAN-064, DAN-067, DAN-073, DAN-109, DAN-209, DAN-103
- justificativa: 
- aprofundar DAN-104: `typo command remove servers human error` — Incidente envolve operador remover servidores por erro de digitação, correspondente ao atual onde comando removeu servidores e derrubou serviço de armazenamento.
- aprofundar DAN-189: `operator forgot -n reboot all servers` — Operador utilizou ferramenta com validação laxa, esqueceu -n e reiniciou todos servidores, similar a comando de remoção de servidores que causou queda.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.401: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.368: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.648: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.565: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-170 (esperado: DAN-018)

- busca inicial: DAN-144, DAN-066, DAN-017, DAN-018, DAN-029, DAN-191, DAN-102, DAN-037, DAN-067, DAN-154
- justificativa: 
- aprofundar DAN-018: `React component bug dashboard excessive API calls dependency array fix` — Dashboard React component bug after deploy causes overwhelming API calls, similar to internal service flood after frontend deploy
- aprofundar DAN-144: `flapping service thundering herd reconnect memory queue` — Thundering herd after service recovery fills queues, analogous to enxurrada de chamadas after deploy
- aprofundar DAN-067: `thundering herd after power failure rate limit` — Post-failure request volume overwhelms services, similar to internal service receiving calls from dashboard after deploy
  - DAN-018 (llm) [What Happened] 0.679: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.647: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-144 (llm) [Summary] 0.568: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.515: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-067 (llm) [Disaster Recovery] 0.593: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.575: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (causa) [Lessons and Remediation] 0.574: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 

## q-171 (esperado: DAN-018)

- busca inicial: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-133, DAN-129, DAN-218, DAN-145, DAN-220
- justificativa: 
- aprofundar DAN-018: `dashboard react component dependency array excessive api calls` — Dashboard React component bug causing excessive API calls after frontend deploy matches current incident's flooding from dashboard after deploy; differs in target service (Tenant Service vs internal service).
- aprofundar DAN-144: `flapping service thundering herd frontend memory queues` — Flapping service leads to thundering herd similar to call flooding, but cause is service flapping not frontend deploy.
- aprofundar DAN-220: `lack exponential backoff microservice cascading failure` — Missing exponential backoff can cause call flooding, but incident involves network scaling, not dashboard deploy.
  - DAN-018 (llm) [What Happened] 0.631: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.615: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-144 (llm) [Summary] 0.515: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.467: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-220 (llm) [First symptoms: two months before the outage] 0.625: ## First symptoms: two months before the outage  Two months before the big outage we had an incident connected with one of our smallest backend services: Popcount. Popcount (this is our internal name)
  - DAN-220 (llm) [Lessons learned] 0.607: ## Lessons learned  - We should have prioritized fixing the backoff bug in the client after the first Popcount incident, we did not assign the right severity. We thought having the fast fail mechanism
  - DAN-220 (causa) [The night of April 27th] 0.485: ## The night of April 27th  It was a rainy Saturday night in Stockholm. Some of our engineers were online on IRC, and discovered that Popcount was unhealthy again. We thought the fast fail logic we in
  - DAN-220 (correcao) [Remediations in place after the second incident] 0.641: ## Remediations in place after the second incident  After the outage (infamously known as OPS-6000 in our incident tracking system), we held a post-mortem meeting where we invited the entire Technolog
  - DAN-220 (correcao) [Remediations: why are they important?] 0.568: ## Remediations: why are they important?  For every incident we hold a post-mortem meeting. The goal of this meeting is producing a list of remediations that we need to put in place in order to preven

## q-222 (esperado: DAN-121)

- busca inicial: DAN-129, DAN-144, DAN-147, DAN-121, DAN-016, DAN-137, DAN-134, DAN-209, DAN-148, DAN-220
- justificativa: 
- aprofundar DAN-121: `database overload throttling timeout fix` — Bate: backend database sobrecarregado limita requisições, fazendo serviços fazerem timeout. Não bate: contexto diferente (BBC Blogs vs player de vídeo), mas padrão de falha identico.
- aprofundar DAN-147: `database capacity request queue overload fix` — Bate: fila de requisições sobrecarregando capacidade insuficiente de DB, causando falhas em cascata e timeouts. Não bate: foco em planejamento de capacidade e monitoring ausente vs limite de requisições atuais.
- aprofundar DAN-129: `health check timeout latency fix` — Bate: aumento de latência e indisponibilidade intermitente. Não bate: causa raiz é timeout de health check versus sobrecarga direta do banco de dados.
  - DAN-121 (llm) [sem seção] 0.482: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.455: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.62: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.612: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-129 (llm) [Health Check Timeouts] 0.683: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [sem seção] 0.525: Approximately two hours after Supermarket became the official community site it started to experience increased latency and intermittent unresponsiveness. This made downloading cookbooks problematic a
  - DAN-129 (causa) [Conclusion] 0.457: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 

## q-240 (esperado: DAN-152)

- busca inicial: DAN-009, DAN-175, DAN-140, DAN-152, DAN-177, DAN-015, DAN-017, DAN-124, DAN-131, DAN-028
- justificativa: 
- aprofundar DAN-009: `service token release code error` — envolve falha de token ao liberar código, similar ao novo pacote enviando tokens
- aprofundar DAN-175: `private token leak Jenkins` — vazamento de token do sistema CI, similar a pacote novo filtrando tokens
- aprofundar DAN-152: `malicious package npm publish` — publicação acidental de pacote malicioso, scenario de comprometimento de pacote
  - DAN-009 (llm) [sem seção] 0.657: Several Cloudflare services became unavailable for 121 minutes on January 24, 2023 due to an error releasing code that manages service tokens. The incident degraded a wide range of Cloudflare products
  - DAN-009 (llm) [What went wrong?] 0.644: ### What went wrong?  As a result of the bug, any Cloudflare account that used a service token to authenticate during the 10 minutes “last seen at” release was out would have its “client secret” value
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [How did we fix the issue?] 0.483: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-175 (llm) [Incident Summary] 0.557: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (llm) [Incident Summary] 0.508: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro
  - DAN-152 (llm) [Timeline] 0.716: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Summary] 0.712: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-012 (esperado: DAN-211)

- busca inicial: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-066, DAN-222, DAN-113, DAN-101, DAN-133
- justificativa: 
- aprofundar DAN-020: `service discovery config misconfiguration cascading failure` — Incident involves service discovery layer outage due to bad config, matching current slow writes and service failures.
- aprofundar DAN-211: `Consul streaming BoltDB service discovery load health check` — Incident involves service discovery and health check load issues after iptables removal, similar to current writes timing out and other services failing.
- aprofundar DAN-220: `lack exponential backoff microservice cascading failure` — Cascading failure from missing backoff could relate to service discovery slowdown propagating failures.
  - DAN-020 (llm) [The failure of a core system] 0.735: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [A thundering herd] 0.723: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Improve the resilience of service discovery] 0.401: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-211 (llm) [Return to Service Attempt #1 (10/29 02:00 – 04:00)] 0.69: ### Return to Service Attempt #1 (10/29 02:00 – 04:00)  The reset went smoothly, and initially, the metrics looked good. When we removed the iptables block, the service discovery and health check load
  - DAN-211 (llm) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.669: ### Early Triage (10/28 13:37 – 10/29 02:00)  The initial investigation suggested that the Consul cluster that Vault and many other services depend on was unhealthy.  Specifically, the Consul cluster 
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-220 (llm) [First symptoms: two months before the outage] 0.625: ## First symptoms: two months before the outage  Two months before the big outage we had an incident connected with one of our smallest backend services: Popcount. Popcount (this is our internal name)
  - DAN-220 (llm) [Lessons learned] 0.607: ## Lessons learned  - We should have prioritized fixing the backoff bug in the client after the first Popcount incident, we did not assign the right severity. We thought having the fast fail mechanism
  - DAN-220 (causa) [The night of April 27th] 0.485: ## The night of April 27th  It was a rainy Saturday night in Stockholm. Some of our engineers were online on IRC, and discovered that Popcount was unhealthy again. We thought the fast fail logic we in
  - DAN-220 (correcao) [Remediations in place after the second incident] 0.641: ## Remediations in place after the second incident  After the outage (infamously known as OPS-6000 in our incident tracking system), we held a post-mortem meeting where we invited the entire Technolog
  - DAN-220 (correcao) [Remediations: why are they important?] 0.568: ## Remediations: why are they important?  For every incident we hold a post-mortem meeting. The goal of this meeting is producing a list of remediations that we need to put in place in order to preven

## q-263 (esperado: DAN-200)

- busca inicial: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-073, DAN-146, DAN-106, DAN-069, DAN-066
- justificativa: 
- aprofundar DAN-200: `priority inversion VxWorks task scheduler fix` — Sintoma de resets do sistema poucos dias após início de operação, parecido com o incidente atual; causa foi inversão de prioridade no sistema operacional VxWorks, mas contexto e hardware diferem.
- aprofundar DAN-198: `Apollo rendezvous radar CPU load design flaw fix` — Reinicialização de computador de bordo, mas ocorreu durante pouso lunar, não poucos dias após início de operação; causa foi carga excessiva de CPU pelo radar de acoplagem.
  - DAN-200 (llm) [THE FAILURE] 0.668: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.622: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.65: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.649: This phenomenon occurred whenever the RR mode was in SLEW or AUTO, regardless of whether the rendezvous radar itself was powered up. | | The CDU interface counters in the LGC were incremented or decre
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-032 (esperado: DAN-104)

- busca inicial: DAN-109, DAN-210, DAN-189, DAN-191, DAN-067, DAN-073, DAN-104, DAN-103, DAN-026, DAN-070
- justificativa: 
- aprofundar DAN-104: `typo server removal S3 outage cause fix` — Current incident involves operator removing servers via command; DAN-104 matches because human error typo caused mass server removal leading to S3 outage, but current incident is storage service down, not cascading to other services.
- aprofundar DAN-189: `operator reboot servers input validation mistake` — Operator command to reboot servers accidentally rebooted all due to missing -n flag; similar in that operator mistake caused widespread server impact, but current incident is removal not reboot, and storage service specifically.
- aprofundar DAN-067: `storage volume failure recovery` — Storage volume failure took down services; relevant because current incident is storage service down, but cause is volume failure not server removal; included for storage aspect.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.661: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.657: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.62: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.547: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-067 (llm) [Lessons and Remediation] 0.562: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Disaster Recovery] 0.562: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 

## q-219 (esperado: DAN-116)

- busca inicial: DAN-066, DAN-126, DAN-103, DAN-222, DAN-205, DAN-209, DAN-116, DAN-109, DAN-191, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update crash recovery` — Database update triggered simultaneous server crashes, matching current incident's timing; but double-free bug is specific to memory corruption, not general data update.
- aprofundar DAN-126: `bug fix wrong timestamps data loss server misconfiguration` — Involves data loss after a bug fix and hotfix misconfiguration, similar to post-update issues, but timestamps bug is different from general data update crash.
- aprofundar DAN-222: `Cassandra cluster crash data ingest message bus` — Cassandra crashed after data was ingested from message bus, similar to crash after data update, but cause is cluster-specific, not generic service crash.
  - DAN-116 (llm) [sem seção] 0.718: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.567: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-126 (llm) [Server Configurations] 0.647: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [Server Configurations] 0.595: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (causa) [Server Configurations] 0.378: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-222 (llm) [sem seção] 0.692: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (llm) [sem seção] 0.681: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (causa) [sem seção] 0.453: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl

## q-223 (esperado: DAN-121)

- busca inicial: DAN-147, DAN-148, DAN-101, DAN-129, DAN-134, DAN-219, DAN-164, DAN-121, DAN-144, DAN-094
- justificativa: 
- aprofundar DAN-121: `database throttling requests timeout fix` — Bate por descrever backend de banco de dados sobrecarregado fazendo throttle de requests e services timing out, similar ao incidente atual; não bate por detalhar outages de serviços específicos de vídeo, não a causa raiz de throttle.
- aprofundar DAN-147: `database capacity request queue cascading fix` — Bate por request queue overloading insuficiente capacidade de banco de dados, espelha o overloading do incidente atual; não bate por foco em cascading failure por fila, enquanto atual tem timeouts de serviços múltiplos.
- aprofundar DAN-164: `database influx requests overload replication fix` — Bate por influx de requests sobrecarregando banco de dados, core similarity; não bate por incluir replicação lag e erro de administração de diretórios, não presentes no incidente atual.
  - DAN-121 (llm) [sem seção] 0.466: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.455: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.593: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.566: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Timeline] 0.68: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.65: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-218 (esperado: DAN-116)

- busca inicial: DAN-126, DAN-146, DAN-103, DAN-066, DAN-209, DAN-106, DAN-048, DAN-191, DAN-116, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update crash impression bus` — Database update triggered a double free bug causing all impression bus servers to crash simultaneously, matching current incident after data update
- aprofundar DAN-106: `human error networking upgrade US East outage` — Networking upgrade by human error caused outage across all US East zones, but not directly after a data update
- aprofundar DAN-048: `RDS Multi-AZ failover data loss MySQL config` — RDS hardware failure and incorrect configuration caused data loss, not simultaneous server crash after update
  - DAN-116 (llm) [sem seção] 0.748: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.629: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.605: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.583: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Customers also experienced elevated error rates until Noon PDT on April 21st when attempting to launch new EBS-ba
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-048 (llm) [Final thoughts] 0.819: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (llm) [Incorrect configuration variable] 0.807: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m

## q-229 (esperado: DAN-125)

- busca inicial: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-129, DAN-091, DAN-125
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade peak load cascade` — Exact match: database capacity reduction caused inability to handle peak load and cascading server failures, similar to current incident downsizing.
- aprofundar DAN-147: `insufficient database capacity request queue cascading failure` — Cascading failure due to overloaded database capacity; current incident also involves DB capacity insufficiency at peak.
- aprofundar DAN-096: `ProxySQL connections exhausted peak load` — Load-related connection exhaustion leading to failures; relevant but differs in component (ProxySQL vs direct DB).
  - DAN-125 (llm) [Database performance issues] 0.656: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.512: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.584: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.579: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.639: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.633: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev

## q-262 (esperado: DAN-200)

- busca inicial: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073, DAN-189, DAN-146, DAN-210, DAN-043, DAN-200
- justificativa: 
- aprofundar DAN-200: `priority inversion VxWorks task scheduler patch system reset` — Both involve spontaneous system resets occurring days after initial operation; DAN-200 identifies a priority inversion OS bug causing resets, directly analogous to current incident's timing and symptom.
- aprofundar DAN-198: `Apollo 11 rendezvous radar CPU load spacecraft computer restart` — Both involve spacecraft computer restarts due to design flaws; however DAN-198 occurs during high-load lunar landing while current incident involves sporadic resets days after startup, so less direct but related in aerospace computing context.
  - DAN-200 (llm) [THE FAILURE] 0.658: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [THE SOFTWARE ARCHITECTURE] 0.598: ## THE SOFTWARE ARCHITECTURE  The bc_sched and bc_dist tasks check each cycle to be sure that the other had completed its execution. The bc_sched task is the highest priority task in the system (excep
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.728: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.702: This phenomenon occurred whenever the RR mode was in SLEW or AUTO, regardless of whether the rendezvous radar itself was powered up. | | The CDU interface counters in the LGC were incremented or decre
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-228 (esperado: DAN-125)

- busca inicial: DAN-164, DAN-147, DAN-156, DAN-048, DAN-096, DAN-043, DAN-094, DAN-209, DAN-134, DAN-109
- justificativa: 
- aprofundar DAN-147: `db capacity overload cascading failure` — Falha em cascata por capacidade DB insuficiente coincide com atual; falta redução recente de tamanho mas problema de capacidade se alinha.
- aprofundar DAN-096: `peak load mysql proxySQL connection exhaustion` — Sobrecarga pico de carga no cluster MySQL exaure conexões, similar a pico atual e efeito em servidores dependentes; throttling e failovers são diferenças.
- aprofundar DAN-094: `systemd limit NOFILE mysql cluster load` — Meltdowns por carga com limites de sistema (NOFILE) causando falhas em cascata em cluster MySQL, tema de limite de capacidade sob carga coincide com redução recente de tamanho; especificações de ProxySQL diferem.
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.521: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.475: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.683: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.66: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev
  - DAN-094 (llm) [2020, February 25 16:36 UTC (lasting for two hours 12 minutes)] 0.624: ## 2020, February 25 16:36 UTC (lasting for two hours 12 minutes)  In this third incident involving ProxySQL, active database connections crossed a critical threshold that changed the behavior of this
  - DAN-094 (llm) [Timeline] 0.586: ## Timeline  ## 2020, February 19 15:17 UTC (lasting for 52 minutes)  At this time, an unexpectedly resource-intensive query began running against our mysql1 database cluster. The intent was to run th
  - DAN-094 (causa) [2020, February 20 21:31 UTC (lasting for 47 minutes)] 0.45: ## 2020, February 20 21:31 UTC (lasting for 47 minutes)  Two days later, as part of a planned master database promotion, we saw unexpectedly high load which triggered a similar ProxySQL failure. The i
  - DAN-094 (correcao) [Next steps] 0.365: ## Next steps  ## Immediate changes: Data partitioning  We shipped a sizable chunk of data partitioning efforts we’ve worked on for the past six months just days after these incidents for one of our m
  - DAN-094 (correcao) [In summary] 0.481: ## In summary  We know you depend on our platform to be reliable. With the immediate changes we’ve made and long-term plans in progress, we’ll continue to use what we’ve learned to make GitHub better 

## q-034 (esperado: DAN-004)

- busca inicial: DAN-005, DAN-137, DAN-051, DAN-012, DAN-220, DAN-011, DAN-016, DAN-014, DAN-006, DAN-113
- justificativa: 
- aprofundar DAN-051: `firewall iptables HAProxy configuration change blocked all traffic` — Incorrect firewall config blocked network traffic, similar to current incident where a firewall rule blocks all traffic without remembered change.
- aprofundar DAN-006: `network configuration typo datacenter traffic routing` — Typo in network config redirected traffic, analogous to unintended firewall rule blocking all traffic.
- aprofundar DAN-005: `bad router rule config caused edge router crash` — Bad configuration led to outage, but differs as it crashed routers rather than blocking traffic.
  - DAN-051 (llm) [sem seção] 0.675: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-051 (llm) [sem seção] 0.626: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-006 (llm) [sem seção] 0.604: Today a configuration error in our backbone network caused an outage for Internet properties and Cloudflare services that lasted 27 minutes. We saw traffic drop by about 50% across our network. Becaus
  - DAN-006 (llm) [What happened and what we’re doing about it] 0.585: ### What happened and what we’re doing about it  As there was backbone congestion in Atlanta, the team had decided to remove some of Atlanta’s backbone traffic. But instead of removing the Atlanta rou
  - DAN-006 (causa) [Conclusion] 0.402: ### Conclusion  We’ve never experienced an outage on our backbone and our team responded quickly to restore service in the affected locations, but this was a very painful period for everyone involved.
  - DAN-006 (correcao) [What happened and what we’re doing about it] 0.372: ### What happened and what we’re doing about it  - Introduce a maximum-prefix limit on our backbone BGP sessions - this would have shut down the backbone in Atlanta, but our network is built to functi
  - DAN-006 (correcao) [Timeline] 0.323: ### Timeline  All timestamps are UTC.  First, an issue occurred on the backbone link between Newark and Chicago which led to backbone congestion in between Atlanta and Washington, DC.  In responding t
  - DAN-005 (llm) [Bad Rule] 0.733: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.602: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp

## q-243 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210, DAN-209, DAN-205, DAN-129, DAN-109, DAN-145
- justificativa: 
- aprofundar DAN-011: `database permission change bot-detection file overflow Cloudflare outage` — Incidente global CDN causado por mudança de permissão em banco de dados do bot-detection, semelhante a queda worldwide, mas causa específica de arquivo excessivo pode diferir.
- aprofundar DAN-008: `Tiered Cache change causing 530 errors Cloudflare` — Parcial outage Cloudflare por mudança no Tiered Cache, relevante para CDN mas impacto limitado e não worldwide.
- aprofundar DAN-067: `power failure data center Cloudflare control plane outage` — Queda global do control plane devido a falha de energia no data center, parecido em escopo mas causa diferente (energia vs configuração CDN).
  - DAN-011 (llm) [sem seção] 0.719: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (llm) [Remediation and follow-up steps] 0.696: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-008 (llm) [sem seção] 0.829: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Remediation and follow-up steps] 0.733: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Conclusion] 0.516: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-067 (llm) [Lessons and Remediation] 0.83: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.806: ### Flexential Data Center Power Failure  The largest of the three facilities in Oregon is run by Flexential. We refer to this facility as “PDX-DC04”. Cloudflare leases space in PDX-04 where we house 
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-260 (esperado: DAN-197)

- busca inicial: DAN-066, DAN-106, DAN-067, DAN-029, DAN-209, DAN-220, DAN-154, DAN-205, DAN-008, DAN-133
- justificativa: 
- aprofundar DAN-106: `Amazon EC2 RDS service disruption human error networking upgrade root cause fix` — Incident involves a cloud provider (AWS) outage due to human error, no client changes, sudden failure of services; relevant but focuses on resource crunch rather than API calls.
- aprofundar DAN-067: `Cloudflare power failure thundering herd API call rate limit` — External event (power failure) caused API call overwhelming and service degradation; similar sudden impact on API calls, but cause is data center power, not provider API.
- aprofundar DAN-154: `Fastly software bug customer config change outage root cause fix` — Provider‑side bug surfaced after a valid config change; sudden global outage; similar pattern of unexpected failure of downstream services, though our incident has no config change on our side.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.739: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.735: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.41: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-067 (llm) [Disaster Recovery] 0.702: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.643: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-154 (llm) [**What happened?**] 0.751: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (llm) [sem seção] 0.699: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s

## q-242 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-109, DAN-026, DAN-129, DAN-145, DAN-106, DAN-009, DAN-008, DAN-067, DAN-016
- justificativa: 
- aprofundar DAN-011: `permissions database bot-detection Cloudflare outage root cause fix` — Global CDN outage due to database permission change; matches worldwide impact but differs in component (bot-detection vs CDN config).
- aprofundar DAN-009: `service token code release Cloudflare incident root cause fix` — CDN-wide degradation after code release managing service tokens; matches code‑release trigger but tokens differ from cache config.
- aprofundar DAN-008: `Tiered Cache change Cloudflare 530 error root cause fix` — CDN configuration change causing 530 errors worldwide; directly about cache system and global impact.
  - DAN-011 (llm) [Remediation and follow-up steps] 0.723: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-011 (llm) [Remediation and follow-up steps] 0.721: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [How Cloudflare processes requests, and how this went wrong today] 0.393: ## How Cloudflare processes requests, and how this went wrong today  This feature file is refreshed every few minutes and published to our entire network and allows us to react to variations in traffi
  - DAN-009 (llm) [What went wrong?] 0.78: ### What went wrong?  As a result of the bug, any Cloudflare account that used a service token to authenticate during the 10 minutes “last seen at” release was out would have its “client secret” value
  - DAN-009 (llm) [sem seção] 0.778: Several Cloudflare services became unavailable for 121 minutes on January 24, 2023 due to an error releasing code that manages service tokens. The incident degraded a wide range of Cloudflare products
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [How did we fix the issue?] 0.483: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-008 (llm) [sem seção] 0.826: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Incident timeline and impact] 0.753: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Conclusion] 0.516: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i

## q-261 (esperado: DAN-197)

- busca inicial: DAN-067, DAN-066, DAN-220, DAN-154, DAN-029, DAN-008, DAN-133, DAN-106, DAN-205, DAN-209
- justificativa: 
- aprofundar DAN-067: `power failure thundering herd API rate limits` — Semelhança: falha de API do provedor de nuvem sem mudança nossa. Diferença: causa é falha de energia, não nosso cenário.
- aprofundar DAN-008: `Tiered Cache change 530 errors` — Semelhança: mudança no provedor causa erros na API. Diferença: nosso incidente não tem mudança nossa, mas mudança do provedor.
- aprofundar DAN-106: `human error networking upgrade EC2 RDS outage` — Semelhança: erro do provedor causa interrupção sem mudança nossa. Diferença: causa é erro humano em upgrade de rede.
  - DAN-067 (llm) [Disaster Recovery] 0.637: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.563: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-008 (llm) [sem seção] 0.766: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.675: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.689: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Customers also experienced elevated error rates until Noon PDT on April 21st when attempting to launch new EBS-ba
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.687: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
