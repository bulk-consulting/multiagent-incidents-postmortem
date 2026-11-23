# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | não | sim | find → search | sim | sim | 2 | 10 |
| q-022 | DAN-104 | 4 | não | sim | find → search | sim | sim | 2 | 40 |
| q-170 | DAN-018 | 4 | não | sim | find → search | sim | sim | 2 | 47 |
| q-171 | DAN-018 | 4 | não | sim | find → search | sim | sim | 2 | 70 |
| q-222 | DAN-121 | 4 | não | não | find → search | não | não | 2 | 9 |
| q-240 | DAN-152 | 4 | não | sim | find → search | sim | sim | 2 | 48 |
| q-012 | DAN-211 | 5 | não | sim | find → search | sim | sim | 2 | 39 |
| q-263 | DAN-200 | 5 | não | sim | find → search | sim | sim | 2 | 67 |
| q-032 | DAN-104 | 7 | não | sim | find → find → search | sim | sim | 4 | 153 |
| q-219 | DAN-116 | 7 | não | não | find → search | não | não | 2 | 10 |
| q-223 | DAN-121 | 8 | não | sim | find → search | sim | sim | 2 | 76 |
| q-218 | DAN-116 | 9 | não | sim | find → search | sim | sim | 2 | 41 |
| q-229 | DAN-125 | 10 | não | sim | find → search | sim | sim | 2 | 98 |
| q-262 | DAN-200 | 10 | não | não | find → search | não | não | 2 | 11 |
| q-228 | DAN-125 | 11 | não | sim | find → search | sim | sim | 2 | 240 |
| q-034 | DAN-004 | 12 | não | sim | find → search | sim | sim | 2 | 39 |
| q-243 | DAN-154 | 12 | não | não | find → search | não | não | 2 | 67 |
| q-260 | DAN-197 | 19 | não | não | find → search | não | não | 3 | 9 |
| q-242 | DAN-154 | — | não | não | find → search | não | não | 2 | 101 |
| q-261 | DAN-197 | — | não | não | find → search | não | não | 2 | 10 |

## q-020 (esperado: DAN-164)

- busca inicial: 
- justificativa: 
- aprofundar DAN-043: `root cause fix accidental delete production database backups recovery` — É a correspondência mais direta: engenheiros deletaram o banco de produção por acidente, exatamente como o incidente atual.
- aprofundar DAN-164: `root cause fix admin deleted wrong directory data loss recovery` — Erro humano de admin apagando o alvo errado durante operação, com perda de dados; componente diferente (diretório), mas categoria de falha parecida.
- aprofundar DAN-056: `root cause fix accidental truncate production database environment variable` — Perda acidental de dados do banco de produção, embora o gatilho seja variável de ambiente e não manutenção; impacto semelhante.
- novos incidentes nos achados: DAN-043, DAN-146, DAN-164, DAN-056, DAN-094, DAN-048, DAN-102, DAN-208, DAN-058, DAN-186
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.706: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.617: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Root cause analysis] 0.62: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.52: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.737: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.687: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-022 (esperado: DAN-104)

- busca inicial: 
- justificativa: 
- aprofundar DAN-104: `root cause human error typo command remove servers S3 fix corrective action` — Bate fortemente: comando do operador para remover poucos servidores removeu mais do que o esperado, derrubou serviço de armazenamento (S3) e causou falha em cascata em sistemas dependentes — espelho do incidente atual.
- aprofundar DAN-189: `root cause operator tool lax input validation reboot all servers fix remediation` — Bate parcialmente: operador afetou mais servidores do que pretendia por falha de ferramenta/processo, mas é reboot não remoção, e não é específico a serviço de armazenamento.
- novos incidentes nos achados: DAN-073, DAN-104, DAN-209, DAN-109, DAN-230, DAN-164, DAN-222, DAN-103, DAN-146, DAN-189
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.563: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.551: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.606: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.597: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-170 (esperado: DAN-018)

- busca inicial: 
- justificativa: 
- aprofundar DAN-018: `React component dependency array excessive API calls Tenant Service root cause fix` — Bate muito: painel (dashboard) enviando enxurrada de chamadas para serviço interno após alteração no frontend, derrubando API e painel em cascata. Difere apenas no nome do serviço interno (Tenant Service).
- aprofundar DAN-144: `thundering herd reconnect frontend services out of memory internal queues fix` — Bate parcialmente: sobrecarga em cascata afetando frontend, mas o gatilho é um serviço flutuando, não um deploy do frontend nem chamadas vindas do painel para um serviço interno.
- novos incidentes nos achados: DAN-066, DAN-029, DAN-018, DAN-144, DAN-067, DAN-129, DAN-133, DAN-220, DAN-218, DAN-223
  - DAN-018 (llm) [What Happened] 0.704: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.638: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-144 (llm) [Summary] 0.57: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.535: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 

## q-171 (esperado: DAN-018)

- busca inicial: 
- justificativa: 
- aprofundar DAN-018: `React component dashboard excessive API calls dependency array root cause fix` — É o mais parecido: dashboard React causando excesso de chamadas a serviço interno (Tenant Service) após deploy frontend, derrubando API e dashboard. O sintoma bate com o incidente atual.
- aprofundar DAN-144: `thundering herd flapping service frontend services memory queues root cause fix` — Tem semelhança parcial: enxurrada de requisições afetando serviços frontend após instabilidade, mas não menciona deploy nem dashboard como origem das chamadas.
- novos incidentes nos achados: DAN-144, DAN-066, DAN-018, DAN-029, DAN-067, DAN-133, DAN-129, DAN-218, DAN-001, DAN-222
  - DAN-018 (llm) [What Happened] 0.656: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.646: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-144 (llm) [Summary] 0.549: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.538: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 

## q-222 (esperado: DAN-121)

- busca inicial: 
- justificativa: 
- aprofundar DAN-147: `database capacity request queue cascading failure fix` — Descreve falha em cascata por fila de requisições sobrecarregando capacidade insuficiente do banco, semelhante ao banco sobrecarregado afetando vários serviços.
- aprofundar DAN-101: `connection pool exhaustion app timeouts database overload fix` — Descreve timeouts de aplicação por exaustão do pool de conexões do banco, com múltiplos endpoints afetados, parecido com timeouts em vários serviços.
- aprofundar DAN-094: `MySQL cluster overload load-driven incident ProxySQL meltdown fix` — Aborda incidentes por carga no cluster MySQL afetando serviço, embora o gatilho seja query analítica no master, não exatamente sobrecarga geral.
- novos incidentes nos achados: DAN-147, DAN-148, DAN-219, DAN-134, DAN-101, DAN-144, DAN-129, DAN-094, DAN-016, DAN-220
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.59: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.58: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-101 (llm) [sem seção] 0.681: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (llm) [sem seção] 0.674: It wasn’t until a few days later that we realised this was the root of our problems. As the timeouts were intermittent and didn’t occur every day, it took a little while to confirm the issue. But, it’
  - DAN-101 (causa) [sem seção] 0.433: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (correcao) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-101 (correcao) [sem seção] 0.317: Originally, we would receive this event from Slack, and within the lifetime of that HTTP request, we’d perform any responses we needed to, e.g. offering to attach a GitHub link that a user has just po
  - DAN-094 (llm) [Timeline] 0.75: ## Timeline  ## 2020, February 19 15:17 UTC (lasting for 52 minutes)  At this time, an unexpectedly resource-intensive query began running against our mysql1 database cluster. The intent was to run th
  - DAN-094 (llm) [2020, February 25 16:36 UTC (lasting for two hours 12 minutes)] 0.739: ## 2020, February 25 16:36 UTC (lasting for two hours 12 minutes)  In this third incident involving ProxySQL, active database connections crossed a critical threshold that changed the behavior of this
  - DAN-094 (causa) [2020, February 20 21:31 UTC (lasting for 47 minutes)] 0.45: ## 2020, February 20 21:31 UTC (lasting for 47 minutes)  Two days later, as part of a planned master database promotion, we saw unexpectedly high load which triggered a similar ProxySQL failure. The i
  - DAN-094 (correcao) [Next steps] 0.365: ## Next steps  ## Immediate changes: Data partitioning  We shipped a sizable chunk of data partitioning efforts we’ve worked on for the past six months just days after these incidents for one of our m
  - DAN-094 (correcao) [In summary] 0.481: ## In summary  We know you depend on our platform to be reliable. With the immediate changes we’ve made and long-term plans in progress, we’ll continue to use what we’ve learned to make GitHub better 

## q-240 (esperado: DAN-152)

- busca inicial: 
- justificativa: 
- aprofundar DAN-152: `compromised npm account malicious packages published root cause fix remediation` — Bate com o cenário de pacote malicioso publicado por alguém que não é o mantenedor legítimo (conta comprometida), diferando apenas no fato de o resumo não mencionar exfiltração de tokens.
- aprofundar DAN-122: `malicious Maven packages impersonation attack JCenter root cause fix remediation` — Semelhança forte: pacotes maliciosos injetados em um repositório público por meio de ataque de personificação, sem relação com os publicadores originais; não menciona tokens no resumo.
- novos incidentes nos achados: DAN-152, DAN-131, DAN-140, DAN-122, DAN-177, DAN-175, DAN-216, DAN-009, DAN-141, DAN-015
  - DAN-152 (llm) [Summary] 0.761: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.745: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.73: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.68: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-012 (esperado: DAN-211)

- busca inicial: 
- justificativa: 
- aprofundar DAN-020: `service discovery config bad dependent client global outage root cause fix` — Menciona service discovery e cliente dependente derrubando a descoberta globalmente, bem parecido com discovery layer lenta afetando outros serviços.
- aprofundar DAN-211: `Consul streaming BoltDB issue root cause remediation` — Consul é uma camada de service discovery; o incidente trata de problemas no Consul que afetam o serviço.
- aprofundar DAN-220: `exponential backoff cascading failure microservice root cause fix` — Falha em cascata causada por microservice sem backoff, similar a outros serviços falhando devido à discovery lenta.
- novos incidentes nos achados: DAN-220, DAN-020, DAN-129, DAN-109, DAN-066, DAN-222, DAN-205, DAN-144, DAN-211, DAN-148
  - DAN-020 (llm) [The failure of a core system] 0.705: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [A thundering herd] 0.681: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Improve the resilience of service discovery] 0.401: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.725: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  But what was going on with the slow leaders? We did not figure this out during the incident, but HashiCorp engineers determined the root cause in the
  - DAN-211 (llm) [Outage Summary] 0.672: ### Outage Summary  The outage was unique in both duration and complexity. The team had to address a number of challenges in sequence to understand the root cause and bring the service back up.  - The
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-220 (llm) [First symptoms: two months before the outage] 0.651: ## First symptoms: two months before the outage  Two months before the big outage we had an incident connected with one of our smallest backend services: Popcount. Popcount (this is our internal name)
  - DAN-220 (llm) [Lessons learned] 0.648: ## Lessons learned  - We should have prioritized fixing the backoff bug in the client after the first Popcount incident, we did not assign the right severity. We thought having the fast fail mechanism
  - DAN-220 (causa) [The night of April 27th] 0.485: ## The night of April 27th  It was a rainy Saturday night in Stockholm. Some of our engineers were online on IRC, and discovered that Popcount was unhealthy again. We thought the fast fail logic we in
  - DAN-220 (correcao) [Remediations in place after the second incident] 0.641: ## Remediations in place after the second incident  After the outage (infamously known as OPS-6000 in our incident tracking system), we held a post-mortem meeting where we invited the entire Technolog
  - DAN-220 (correcao) [Remediations: why are they important?] 0.568: ## Remediations: why are they important?  For every incident we hold a post-mortem meeting. The goal of this meeting is producing a list of remediations that we need to put in place in order to preven

## q-263 (esperado: DAN-200)

- busca inicial: 
- justificativa: 
- aprofundar DAN-200: `priority inversion VxWorks system reset fix patch` — O incidente atual descreve reinicializações do computador de bordo dias depois de entrar em operação; DAN-200 descreve exatamente reinicializações do sistema da sonda Pathfinder dias depois da aterrissagem em Marte, com causa raiz prioridade inversão no VxWorks.
- aprofundar DAN-198: `rendezvous radar CPU load computer restart Apollo 11 fix` — Também envolve reinicialização do computador de bordo de uma nave espacial, mas ocorre durante a aterrissagem lunar e não dias depois de entrar em operação, então a semelhança é parcial.
- novos incidentes nos achados: DAN-198, DAN-189, DAN-146, DAN-103, DAN-066, DAN-191, DAN-073, DAN-154, DAN-200, DAN-116
  - DAN-200 (llm) [THE FAILURE] 0.611: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.593: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.736: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.704: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-032 (esperado: DAN-104)

- busca inicial: 
- justificativa: 
- aprofundar DAN-104: `human error command remove servers typo S3 outage root cause fix recovery` — Corresponde quase exatamente: operador executou comando de rotina para remover poucos servidores, removeu mais do que o pretendido, e o serviço de storage (S3) ficou completamente fora do ar exigindo reinicialização para recuperar.
- aprofundar DAN-189: `operator tool input validation reboot all servers outage fix` — Semelhança: erro de operador com comando destinado a poucos servidores afetou muitos e causou interrupção. Diferença: é reboot, não remoção, e não é especificamente serviço de storage.
- aprofundar DAN-112: `storage nodes lost power could not rejoin cluster handshake timeout recovery fix` — Semelhança: nós de storage caíram e não conseguiam recuperar/reentrar sozinhos. Diferença: gatilho foi perda de energia, não comando de operador para remover servidores.
- novos incidentes nos achados: DAN-219, DAN-073, DAN-109, DAN-222, DAN-029, DAN-070, DAN-210, DAN-139, DAN-146, DAN-067, DAN-112, DAN-208, DAN-104, DAN-026, DAN-148, DAN-209, DAN-189, DAN-127, DAN-143, DAN-145
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.646: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.629: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.653: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.641: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-112 (llm) [Summary of the Amazon SimpleDB Service Disruption] 0.563: ### Summary of the Amazon SimpleDB Service Disruption  Once the problem was identified, we had to manually increase the handshake timeout values and restart a subset of metadata nodes so that they cou
  - DAN-112 (llm) [Summary of the Amazon SimpleDB Service Disruption] 0.542: ### Summary of the Amazon SimpleDB Service Disruption  In this event, multiple storage nodes became unavailable simultaneously in a single data center (after power was lost to the servers on which the
  - DAN-112 (causa) [Summary of the Amazon SimpleDB Service Disruption] 0.33: ### Summary of the Amazon SimpleDB Service Disruption  We wanted to share what we've learned from our investigation of the June 13 SimpleDB disruption in the US East Region. The service was unavailabl

## q-219 (esperado: DAN-116)

- busca inicial: 
- justificativa: 
- aprofundar DAN-209: `migration critical backend system outage root cause fix` — Envolve migração de sistema crítico de backend causando queda simultânea, parecido com atualização de dados derrubando todos os servidores de um serviço crítico.
- aprofundar DAN-146: `scheduled OS upgrade machines wiped out databases outage` — Atualização agendada causou falha em múltiplas máquinas e bancos, semelhante a atualização derrubando servidores simultaneamente.
- aprofundar DAN-102: `Postgres upgrade migration deadlock outage fix` — Atualização seguida de migração gerou bloqueio generalizado e queda de serviço, parecido com atualização de dados precedendo queda simultânea.
- novos incidentes nos achados: DAN-209, DAN-164, DAN-146, DAN-043, DAN-096, DAN-048, DAN-066, DAN-154, DAN-102, DAN-106
  - DAN-209 (llm) [sem seção] 0.572: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.547: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 
  - DAN-146 (llm) [sem seção] 0.689: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [sem seção] 0.536: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri
  - DAN-102 (llm) [sem seção] 0.643: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [sem seção] 0.524: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily

## q-223 (esperado: DAN-121)

- busca inicial: 
- justificativa: 
- aprofundar DAN-121: `database overload throttle requests services timing out root cause fix` — Corresponde quase exatamente: banco de dados sobrecarregado throttling requisições de vários serviços, serviços sem cache começaram a dar timeout e falhar, incluindo o iPlayer (semelhante ao video player).
- aprofundar DAN-101: `connection pool exhaustion transaction timeout root cause fix` — Aborda timeouts de aplicação causados por esgotamento do pool de conexões do banco, com correções como materialized views, indexes e lock timeouts — relevante para o sintoma de timeout em serviços.
- aprofundar DAN-147: `database capacity overload cascading failure root cause remediation` — Falha em cascata por fila de requisições sobrecarregando capacidade insuficiente do banco — mesmo padrão de banco como gargalo afetando múltiplos serviços.
- novos incidentes nos achados: DAN-147, DAN-219, DAN-148, DAN-101, DAN-121, DAN-183, DAN-134, DAN-129, DAN-016, DAN-164
  - DAN-121 (llm) [sem seção] 0.512: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.49: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-101 (llm) [sem seção] 0.675: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (llm) [sem seção] 0.675: It wasn’t until a few days later that we realised this was the root of our problems. As the timeouts were intermittent and didn’t occur every day, it took a little while to confirm the issue. But, it’
  - DAN-101 (causa) [sem seção] 0.433: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (correcao) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-101 (correcao) [sem seção] 0.317: Originally, we would receive this event from Slack, and within the lifetime of that HTTP request, we’d perform any responses we needed to, e.g. offering to attach a GitHub link that a user has just po
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.574: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.519: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-218 (esperado: DAN-116)

- busca inicial: 
- justificativa: 
- aprofundar DAN-116: `database update double free crash all servers root cause fix` — Atualização de banco de dados fez todos os servidores caírem ao mesmo tempo, quase idêntico ao incidente atual.
- aprofundar DAN-209: `migration critical backend system outage root cause fix` — Erro durante migração de sistema crítico causou pane, similar à atualização de dados como gatilho.
- aprofundar DAN-154: `configuration change triggered software bug global outage fix` — Mudança de configuração disparou bug não descoberto e causou pane global, gatilho semelhante a atualização de dados.
- novos incidentes nos achados: DAN-146, DAN-116, DAN-209, DAN-205, DAN-189, DAN-154, DAN-208, DAN-222, DAN-073, DAN-026
  - DAN-116 (llm) [sem seção] 0.688: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.628: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-209 (llm) [sem seção] 0.572: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.547: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 
  - DAN-154 (llm) [sem seção] 0.718: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (llm) [**What happened?**] 0.711: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s

## q-229 (esperado: DAN-125)

- busca inicial: 
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade peak load cascading collapse root cause fix` — Bate exatamente: redução de capacidade do banco, carga no pico, colapso em cascata de servidores dependentes.
- aprofundar DAN-147: `insufficient database capacity cascading failure root cause remediation` — Bate parcialmente: falha em cascata por capacidade insuficiente do banco, mas não menciona redução recente.
- aprofundar DAN-219: `cache nodes removal high workload cluster outage root cause correction` — Bate parcialmente: remoção de nós causou sobrecarga e pane, análogo ao downsizing, mas componente é cache não banco.
- novos incidentes nos achados: DAN-147, DAN-156, DAN-125, DAN-164, DAN-130, DAN-194, DAN-094, DAN-096, DAN-209, DAN-219
  - DAN-125 (llm) [Database performance issues] 0.658: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.548: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.57: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.53: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-219 (llm) [What triggered the incident?] 0.602: ## What triggered the incident?  The PBR step on February 22 updated Consul on 25% of the fleet. It followed two previous 25% steps the prior week, both of which had occurred without any incident. How
  - DAN-219 (llm) [Cascading failure in the cache and datastore tiers] 0.6: ## Cascading failure in the cache and datastore tiers  Once the system is in either a healthy state or a cascading failure state it will tend to stay there, unless there is an external intervention th
  - DAN-219 (causa) [Learnings] 0.551: ## Learnings  The incident has also highlighted some other risks. A brief network outage or partition affecting the cache nodes might trigger the same kind of cascading failure scenario as the Consul 
  - DAN-219 (correcao) [Learnings] 0.467: ## Learnings  We see familiar patterns here which often arise in incidents: performance bottlenecks, cascading failures, dependency on a warm cache, and changes as triggering events. Reading an incide
  - DAN-219 (correcao) [What triggered the incident?] 0.408: ## What triggered the incident?  The Mcrib component is a relatively new piece of software. Prior to Mcrib, we used a distributed locking mechanism based on Consul locks to generate the Mcrouter hash 

## q-262 (esperado: DAN-200)

- busca inicial: 
- justificativa: 
- aprofundar DAN-198: `spacecraft computer restart excess CPU load design flaw root cause fix` — O incidente envolve computador de bordo (nave espacial) reiniciando por causa de falha de projeto, semelhante ao sintoma atual, embora o gatilho seja pouso lunar e não 'alguns dias após operação'.
- aprofundar DAN-182: `repeated crashes unhandled panic root cause mitigation fix` — Descreve falhas intermitentes e quedas repetidas de um sistema, mas em serviço web, não em computador de bordo, então a semelhança é apenas no sintoma de reinício/crash.
- novos incidentes nos achados: DAN-189, DAN-191, DAN-182, DAN-103, DAN-066, DAN-073, DAN-198, DAN-146, DAN-154, DAN-102
  - DAN-198 (llm) [sem seção] 0.649: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.616: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,
  - DAN-182 (llm) [sem seção] 0.658: Subsequent crashes increase the ‘cool off’ period, but it matters little to us: waiting 20m to restart our application would be an unacceptable amount of downtime.  From previous incidents, we’ve lear
  - DAN-182 (llm) [sem seção] 0.634: On Friday 18th November 2022 we experienced 13 minutes of downtime over a period of 32 minutes from 15:40 to 16:12 GMT.  At incident.io, our customers depend on us to be available even when everything
  - DAN-182 (causa) [See related articles] 0.439: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-182 (correcao) [sem seção] 0.518: In this instance, we took advantage of the opportunity to learn and socialise knowledge internally about:  - Heroku Dyno restart policies, and how to manually reboot if they go wrong, for those outsid
  - DAN-182 (correcao) [sem seção] 0.478: We conclude the original crash was probably the first time we processed this bad event, and start looking at all subscriptions with unacked messages from around the time we first went down. For all su

## q-228 (esperado: DAN-125)

- busca inicial: 
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade peak load cascading collapse dependent servers root cause fix` — Bate muito com o atual: banco de dados reduzido (downgrade) por corte de custos, incapaz de aguentar pico, causando colapso em cascata de servidores dependentes. É o mais parecido.
- aprofundar DAN-147: `cascading failure insufficient database capacity request queue root cause fix` — Bate na falha em cascata por capacidade insuficiente do banco de dados, mas não menciona redução explícita de tamanho; ainda assim é relevante.
- aprofundar DAN-096: `peak hour load mysql cluster connection exhaustion failover root cause fix` — Bate no sobrecarregamento do banco em horário de pico, embora a causa seja exaustão de conexões e não redução de capacidade.
- novos incidentes nos achados: DAN-129, DAN-147, DAN-156, DAN-094, DAN-219, DAN-164, DAN-096, DAN-125, DAN-130, DAN-146
  - DAN-125 (llm) [Database performance issues] 0.622: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.536: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.632: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.593: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.777: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.68: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev

## q-034 (esperado: DAN-004)

- busca inicial: 
- justificativa: 
- aprofundar DAN-004: `unrecorded WAF change blocked legitimate traffic Terraform drift detection` — Mudança fora do pipeline (não registrada/lembrada) no WAF bloqueou tráfego legítimo, semelhante ao firewall bloqueando tudo sem que ninguém lembre de ter alterado.
- aprofundar DAN-051: `bad firewall config blocked stackoverflow stackexchange root cause fix` — Firewall config ruim bloqueou todo o site, mesmo componente (firewall) e sintoma de bloqueio total de tráfego.
- novos incidentes nos achados: DAN-012, DAN-005, DAN-051, DAN-009, DAN-137, DAN-011, DAN-004, DAN-007, DAN-016, DAN-220
  - DAN-004 (llm) [**Root Cause Analysis**] 0.745: ## **Root Cause Analysis**  While we manage all our infrastructure, including WAF, almost entirely with Terraform, we discovered during this incident a misconfiguration in IAM controls that allowed a 
  - DAN-004 (llm) [What Happened] 0.675: ## What Happened  - **01:15:** Initial investigation revealed broad connectivity issues between the frontend and our backing APIs, including CORS (Cross-Origin Resource Sharing) errors. The team explo
  - DAN-004 (causa) [Summary] 0.416: ## Summary  On April 4, 2025, from 00:16 to 01:49 UTC (approximately 1 hour and 33 minutes), CircleCI experienced a service disruption affecting both our user interface and build capabilities. During 
  - DAN-004 (correcao) [Future Prevention and Process Improvement] 0.505: ## Future Prevention and Process Improvement  This incident highlighted the strength of our existing systems while identifying several areas where we can improve and make them even more robust:  1. We
  - DAN-004 (correcao) [What Happened] 0.435: ## What Happened  (all times UTC)  The WAF is a critical security component that sits in front of our services and protects them from malicious traffic, while allowing legitimate requests to pass thro
  - DAN-051 (llm) [sem seção] 0.684: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-051 (llm) [sem seção] 0.576: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f

## q-243 (esperado: DAN-154)

- busca inicial: 
- justificativa: 
- aprofundar DAN-005: `root cause router rule config fix edge routers crash` — Bate com o incidente atual: queda mundial do CDN causada por configuração ruim que derrubou todos os edge routers. Não bate: é específico do Cloudflare, não genérico.
- aprofundar DAN-011: `root cause database permissions file output systemwide outage fix` — Bate com o incidente atual: systemwide outage que se propagou pela rede inteira. Não bate: origem é banco de dados de bot-detection, não um problema direto de edge/CDN.
- aprofundar DAN-137: `root cause WAF regex CPU exhaustion global downtime fix rollback` — Bate com o incidente atual: downtime global causado por regra implantada em produção. Não bate: causa é regex/WAF e CPU, não configuração de roteador ou erro genérico de servidor.
- novos incidentes nos achados: DAN-011, DAN-008, DAN-005, DAN-137, DAN-184, DAN-209, DAN-067, DAN-106, DAN-016, DAN-007
  - DAN-005 (llm) [Bad Rule] 0.716: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.634: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-011 (llm) [The query behaviour change] 0.537: ### The query behaviour change  ``` SELECT   name,   type FROM system.columns WHERE   table = 'http_requests_features' order by name; ``` Note how the query does not filter for the database name. With
  - DAN-011 (llm) [sem seção] 0.535: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-137 (llm) [sem seção] 0.769: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (llm) [The events of July 2] 0.734: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [What happened] 0.441: ### What happened  Let’s begin with the sequence of events. All times in this blog are UTC.  At 13:42 an engineer working on the firewall team deployed a minor change to the rules for XSS detection vi
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-260 (esperado: DAN-197)

- busca inicial: 
- justificativa: 
- aprofundar DAN-066: `root cause fix Byzantine failure API availability` — O incidente envolve falha na disponibilidade de API devido a comportamento anômalo de switch, semelhante a chamadas de API para provedor de nuvem falhando sem mudança nossa.
- aprofundar DAN-205: `root cause fix cloud deployment connectivity network instability peering` — O incidente envolve problemas de conectividade entre implantações em nuvem e ponto de peering compartilhado com instabilidade de rede, parecido com falha súbita em chamadas de API de provedor externo.
- aprofundar DAN-184: `root cause fix AWS outage cascading third-party dependencies` — O incidente envolve interrupção na AWS afetando dependências de terceiros e causando degradação em plataforma externa, semelhante ao nosso cenário de API de nuvem falhando sem mudança nossa.
- novos incidentes nos achados: DAN-066, DAN-067, DAN-029, DAN-205, DAN-018, DAN-184, DAN-222, DAN-106, DAN-193, DAN-154
  - DAN-066 (llm) [sem seção] 0.633: *An analysis of the Cloudflare API availability incident on 2020-11-02*  When we review design documents at Cloudflare, we are always on the lookout for Single Points of Failure (SPOFs). Eliminating t
  - DAN-066 (llm) [The Dashboard] 0.623: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.463: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-205 (llm) [The Outage] 0.634: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.612: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-184 (llm) [Service disruption on October 20, 2025] 0.716: ## Service disruption on October 20, 2025  Pete Hamilton  October 22, 2025  —  15 min read  When the internet goes down, our primary job is to help everyone get back up, as fast as possible.  Of the a
  - DAN-184 (llm) [What we learned and next steps] 0.711: ## What we learned and next steps  For outages like this, where so many products and services end up having issues at once, there are always a lot of lessons to be learned.  One key theme we’re hearin
  - DAN-184 (causa) [Initial response] 0.441: ## Initial response  At 07:21 UTC, one of our on-call engineers was paged due to high error rates sending SMS messages and making phone calls. Shortly after, our provider confirmed the impact via thei
  - DAN-184 (correcao) [What we learned and next steps] 0.507: ## What we learned and next steps  - We split worker capacity for notification sending from the escalation worker system and segmented all notification senders by provider  - We reviewed capacity post
  - DAN-184 (correcao) [Scaling our Kubernetes deployments] 0.475: ## Scaling our Kubernetes deployments  We managed to combat acquisition cost by decreasing our autovacuum thresholds and changing our escalation acquisition logic to avoid this type of churn.  These f

## q-242 (esperado: DAN-154)

- busca inicial: 
- justificativa: 
- aprofundar DAN-005: `bad config router rule edge routers crash Cloudflare outage root cause fix` — É um CDN (Cloudflare) que caiu mundialmente devido a erro de configuração, igual ao incidente atual.
- aprofundar DAN-011: `bot detection database permission change file output systemwide outage root cause fix` — Outage sistêmico da Cloudflare (CDN) causado por mudança em sistema interno, afetando mundo todo.
- aprofundar DAN-023: `backbone router configuration changes global outage root cause fix` — Outage global causado por mudanças de configuração em roteadores de backbone, similar a falha de infraestrutura de rede em escala mundial.
- novos incidentes nos achados: DAN-011, DAN-008, DAN-026, DAN-007, DAN-005, DAN-023, DAN-067, DAN-016, DAN-006, DAN-109
  - DAN-005 (llm) [Incident Response] 0.745: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (llm) [Bad Rule] 0.742: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-011 (llm) [Remediation and follow-up steps] 0.625: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [sem seção] 0.57: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-023 (llm) [sem seção] 0.635: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.623: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-261 (esperado: DAN-197)

- busca inicial: 
- justificativa: 
- aprofundar DAN-193: `AWS outage root cause fix remediation API degradation` — O incidente envolve uma interrupção na AWS (provedor de nuvem) que degradou a API do serviço, similar ao problema atual de chamadas de API em nuvem falhando sem mudança interna.
- aprofundar DAN-205: `cloud connectivity network instability root cause fix outage` — O incidente envolve problemas de conectividade e instabilidade de rede em implantações de nuvem afetando a disponibilidade do serviço, semelhante a falhas repentinas em chamadas de API de provedor externo.
- novos incidentes nos achados: DAN-066, DAN-029, DAN-067, DAN-205, DAN-154, DAN-209, DAN-193, DAN-222, DAN-018, DAN-220
  - DAN-193 (llm) [What Happened and What Caused It] 0.704: ## What Happened and What Caused It  However, **a second phase** (between October 20, 11:40 AM and October 21, 12:05 AM) of disruption began shortly after. At 11:48 AM, while we were stabilizing our s
  - DAN-193 (llm) [What Happened and What Caused It] 0.702: ## What Happened and What Caused It  The incident unfolded in two phases.  The **first phase** (between October 19, 11:50 PM and October 20, 11:40 AM) began late on October 19, when AWS us-east-1 expe
  - DAN-193 (causa) [sem seção] 0.369: On October 20, 2025, LaunchDarkly experienced a widespread service disruption that impacted feature flag management, feature flag delivery, as well as our guarded releases, observability, experimentat
  - DAN-193 (correcao) [How We’re Improving] 0.441: ## How We’re Improving  We’ve already made substantial improvements to our systems, and more are underway. Our goal is clear: to help ensure that a regional cloud outage cannot cause the same kind of 
  - DAN-193 (correcao) [3. Strengthening Multi-region availability and Disaster Recovery] 0.336: #### 3. Strengthening Multi-region availability and Disaster Recovery  We are relocating all disaster recovery orchestration systems out of us-east-1.  We are investigating multi-region improvements a
  - DAN-205 (llm) [The Outage] 0.635: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.593: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
