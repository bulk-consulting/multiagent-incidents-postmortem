# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | não | sim | find → search | sim | sim | 2 | 9 |
| q-022 | DAN-104 | 4 | não | não | find → search | não | não | 2 | 29 |
| q-170 | DAN-018 | 4 | não | sim | find → search | sim | sim | 2 | 42 |
| q-171 | DAN-018 | 4 | não | sim | find → search | sim | sim | 2 | 57 |
| q-222 | DAN-121 | 4 | não | sim | find → search | sim | sim | 2 | 72 |
| q-240 | DAN-152 | 4 | não | sim | find → search | sim | sim | 2 | 12 |
| q-012 | erro: Exception: [429] Too Many Requests
{'status': 429, 'title': 'Too Many Requests'} | | | | | | | | | 47 |
| q-263 | DAN-200 | 5 | não | não | find → search | não | não | 2 | 26 |
| q-032 | DAN-104 | 7 | não | não | find → search | não | não | 2 | 62 |
| q-219 | DAN-116 | 7 | não | sim | find → search | sim | sim | 2 | 15 |
| q-223 | DAN-121 | 8 | não | não | find → search | não | não | 3 | 24 |
| q-218 | DAN-116 | 9 | não | não | find → search | não | não | 2 | 11 |
| q-229 | DAN-125 | 10 | não | sim | find → search | sim | sim | 2 | 30 |
| q-262 | DAN-200 | 10 | não | não | find → find → search | não | não | 4 | 38 |
| q-228 | DAN-125 | 11 | não | sim | find → search | sim | sim | 2 | 25 |
| q-034 | erro: Exception: [429] Too Many Requests
{'status': 429, 'title': 'Too Many Requests'} | | | | | | | | | 47 |
| q-243 | DAN-154 | 12 | não | não | find → search | não | não | 2 | 28 |
| q-260 | DAN-197 | 19 | não | sim | find → search | sim | sim | 2 | 11 |
| q-242 | DAN-154 | — | não | sim | find → search | sim | sim | 2 | 59 |
| q-261 | DAN-197 | — | não | sim | find → search | sim | sim | 2 | 10 |

## q-020 (esperado: DAN-164)

- busca inicial: 
- justificativa: 
- aprofundar DAN-043: `root cause accidental production database deletion fix recovery backup` — Mais parecido: engenheiros deletaram o banco de produção por acidente, exatamente como o incidente atual, com impacto de perda de dados e restauração via backup.
- aprofundar DAN-056: `accidental truncate production database environment variable root cause fix` — Semelhança parcial: truncate acidental do banco de produção, mas causado por variável de ambiente em testes, não por exclusão direta durante manutenção.
- aprofundar DAN-164: `admin deleted wrong directory database outage root cause fix` — Semelhança parcial: admin deletou algo errado causando perda de dados no banco, mas foi um diretório durante sobrecarga, não exclusão direta do banco em manutenção.
- novos incidentes nos achados: DAN-043, DAN-186, DAN-056, DAN-146, DAN-164, DAN-118, DAN-048, DAN-066, DAN-094, DAN-091
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.728: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.639: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [What We Learned] 0.736: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.686: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a
  - DAN-164 (llm) [Root cause analysis] 0.699: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [sem seção] 0.588: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-022 (esperado: DAN-104)

- busca inicial: 
- justificativa: 
- aprofundar DAN-219: `cache nodes removal witness cluster outage root cause fix` — Menciona explicitamente remoção de nodes causando outage do serviço, igual ao incidente atual (comando para remover servidores derrubou o storage), embora o componente seja cache e não storage.
- aprofundar DAN-112: `storage nodes removed cluster handshake timeout recovery fix` — Envolve storage nodes sendo removidos do cluster e outage em dependentes, mas o gatilho foi perda de energia, não um comando de operador, então a semelhança é parcial.
- novos incidentes nos achados: DAN-222, DAN-219, DAN-029, DAN-109, DAN-112, DAN-073, DAN-210, DAN-067, DAN-209, DAN-191
  - DAN-219 (llm) [Learnings] 0.606: ## Learnings  The incident has also highlighted some other risks. A brief network outage or partition affecting the cache nodes might trigger the same kind of cascading failure scenario as the Consul 
  - DAN-219 (llm) [Learnings] 0.588: ## Learnings  We see familiar patterns here which often arise in incidents: performance bottlenecks, cascading failures, dependency on a warm cache, and changes as triggering events. Reading an incide
  - DAN-219 (causa) [Learnings] 0.519: ## Learnings  But all is not lost: what is left in Dr. Cook’s Pandora’s Box of Complex Systems Failure is not hope, but human expertise and adaptability. We at Slack Engineering share this story with 
  - DAN-219 (correcao) [What triggered the incident?] 0.429: ## What triggered the incident?  The PBR step on February 22 updated Consul on 25% of the fleet. It followed two previous 25% steps the prior week, both of which had occurred without any incident. How
  - DAN-219 (correcao) [What triggered the incident?] 0.408: ## What triggered the incident?  The Mcrib component is a relatively new piece of software. Prior to Mcrib, we used a distributed locking mechanism based on Consul locks to generate the Mcrouter hash 
  - DAN-112 (llm) [Summary of the Amazon SimpleDB Service Disruption] 0.593: ### Summary of the Amazon SimpleDB Service Disruption  Once the problem was identified, we had to manually increase the handshake timeout values and restart a subset of metadata nodes so that they cou
  - DAN-112 (llm) [Summary of the Amazon SimpleDB Service Disruption] 0.501: ### Summary of the Amazon SimpleDB Service Disruption  In this event, multiple storage nodes became unavailable simultaneously in a single data center (after power was lost to the servers on which the
  - DAN-112 (causa) [Summary of the Amazon SimpleDB Service Disruption] 0.33: ### Summary of the Amazon SimpleDB Service Disruption  We wanted to share what we've learned from our investigation of the June 13 SimpleDB disruption in the US East Region. The service was unavailabl

## q-170 (esperado: DAN-018)

- busca inicial: 
- justificativa: 
- aprofundar DAN-018: `root cause fix React component dependency array excessive API calls dashboard` — Corresponde exatamente: deploy do frontend introduziu bug no componente do painel que gerava chamadas excessivas a serviço interno, derrubando API e painel em cascata.
- aprofundar DAN-016: `root cause fix newly deployed rule infinite loop CPU rate limiting` — Também envolve um deploy novo que expôs bug causando loop infinito e consumo extremo, embora o gatilho seja uma regra e não o painel chamando serviço interno.
- aprofundar DAN-144: `root cause fix flapping service thundering herd frontend out of memory internal queues` — Tem cascata afetando serviços frontend por filas internas cheias, mas o gatilho é failover de serviço e não deploy do frontend.
- novos incidentes nos achados: DAN-144, DAN-066, DAN-018, DAN-029, DAN-133, DAN-182, DAN-129, DAN-016, DAN-145, DAN-067
  - DAN-018 (llm) [What Happened] 0.632: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.613: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.653: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.644: ## Technical description of the error and how it happened  ``` for (rule in active_mitigations) {    // ... (ignore other rule types)    if (rule.match_current_request()) {        if (!has_valid_cooki
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Remediation and follow-up steps] 0.472: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-144 (llm) [Summary] 0.513: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.51: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 

## q-171 (esperado: DAN-018)

- busca inicial: 
- justificativa: 
- aprofundar DAN-018: `root cause React component dependency array excessive API calls Tenant Service fix` — Corresponde quase exatamente: um componente React no dashboard gerou chamadas excessivas a um serviço interno (Tenant Service) após um deploy frontend, derrubando API e dashboard — mesmo gatilho e mesmo sintoma do incidente atual.
- aprofundar DAN-144: `root cause flapping service thundering herd frontend internal queues out of memory fix` — Semelhança parcial: serviço interno afetado pelo frontend com filas internas lotando, mas o gatilho é um serviço flapping, não um deploy frontend, então não é tão direto quanto o DAN-018.
- novos incidentes nos achados: DAN-029, DAN-066, DAN-018, DAN-144, DAN-220, DAN-218, DAN-209, DAN-001, DAN-067, DAN-129
  - DAN-018 (llm) [What Happened] 0.708: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.642: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-144 (llm) [Summary] 0.528: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.524: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 

## q-222 (esperado: DAN-121)

- busca inicial: 
- justificativa: 
- aprofundar DAN-121: `database backend overloaded throttle requests timeout iPlayer root cause fix` — Corresponde quase exatamente: banco de backend sobrecarregado, throttling de requisições de vários serviços, e o iPlayer (player de vídeo) com timeout/falha total. Diferença: é um incidente de 2014 da BBC, não do nosso ambiente.
- aprofundar DAN-096: `ProxySQL connection exhaustion throttle webhooks Actions root cause failover` — Semelhança: cluster de banco de dados sob carga de pico exaurindo conexões, com throttling proativo de serviços. Diferença: afetou webhooks e Actions do GitHub, não um player de vídeo.
- aprofundar DAN-147: `request queue overloading insufficient database capacity cascading failure fix capacity planning` — Semelhança: falha em cascata causada por fila de requisições sobrecarregando capacidade insuficiente do banco. Diferença: foco em autenticação (Duo), não player de vídeo.
- novos incidentes nos achados: DAN-220, DAN-101, DAN-183, DAN-147, DAN-129, DAN-148, DAN-144, DAN-096, DAN-016, DAN-121
  - DAN-121 (llm) [sem seção] 0.553: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.512: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.668: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (llm) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.656: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (causa) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.415: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.634: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.609: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-240 (esperado: DAN-152)

- busca inicial: 
- justificativa: 
- aprofundar DAN-152: `malicious package compromised npm account root cause fix published registry` — Pacote malicioso publicado em registry (ESLint) se assemelha ao pacote não publicado enviando tokens; difere porque lá a conta do mantenedor foi comprometida e o pacote foi publicado.
- aprofundar DAN-122: `malicious Maven package impersonation attack root cause fix JCenter` — Pacotes maliciosos em JCenter via ataque de personificação afetaram apps sem serem publicados pela vítima, bem parecido com o pacote não publicado enviando tokens.
- novos incidentes nos achados: DAN-152, DAN-131, DAN-140, DAN-141, DAN-122, DAN-084, DAN-124, DAN-017, DAN-136, DAN-216
  - DAN-152 (llm) [Summary] 0.741: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.723: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.739: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.664: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-263 (esperado: DAN-200)

- busca inicial: 
- justificativa: 
- aprofundar DAN-198: `computer restart root cause fix excess CPU load rendezvous radar` — É o único incidente sobre computador de bordo/espacial reiniciando; bate com 'onboard computer' e 'resetting', embora o gatilho (pouso lunar) e o padrão (alguns dias após operação) não sejam idênticos.
- novos incidentes nos achados: DAN-189, DAN-103, DAN-198, DAN-191, DAN-066, DAN-069, DAN-182, DAN-211, DAN-102, DAN-209
  - DAN-198 (llm) [sem seção] 0.551: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.529: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-032 (esperado: DAN-104)

- busca inicial: 
- justificativa: 
- aprofundar DAN-112: `storage nodes removed from cluster handshake timeout cannot rejoin manual recovery` — Envolve storage nodes sendo removidos/desregistrados do cluster e não conseguindo reentrar, exigindo recuperação manual — espelha o storage down e não recuperando após remoção de servidores.
- aprofundar DAN-219: `cache nodes removal caused workload outage witness cluster` — Envolve remoção de nodes causando outage de serviço, semelhante ao gatilho de comando de remoção, embora seja cache e não storage.
- aprofundar DAN-109: `storage nodes took themselves down retry loop metadata load` — Envolve storage nodes saindo do cluster e não conseguindo se recuperar sozinhos devido a loop de retry, semelhante ao sintoma de storage não se recuperar.
- novos incidentes nos achados: DAN-109, DAN-222, DAN-219, DAN-112, DAN-070, DAN-029, DAN-148, DAN-073, DAN-026, DAN-145
  - DAN-112 (llm) [Summary of the Amazon SimpleDB Service Disruption] 0.549: ### Summary of the Amazon SimpleDB Service Disruption  Once the problem was identified, we had to manually increase the handshake timeout values and restart a subset of metadata nodes so that they cou
  - DAN-112 (llm) [Summary of the Amazon SimpleDB Service Disruption] 0.503: ### Summary of the Amazon SimpleDB Service Disruption  In this event, multiple storage nodes became unavailable simultaneously in a single data center (after power was lost to the servers on which the
  - DAN-112 (causa) [Summary of the Amazon SimpleDB Service Disruption] 0.33: ### Summary of the Amazon SimpleDB Service Disruption  We wanted to share what we've learned from our investigation of the June 13 SimpleDB disruption in the US East Region. The service was unavailabl
  - DAN-219 (llm) [What triggered the incident?] 0.572: ## What triggered the incident?  The PBR step on February 22 updated Consul on 25% of the fleet. It followed two previous 25% steps the prior week, both of which had occurred without any incident. How
  - DAN-219 (llm) [Cascading failure in the cache and datastore tiers] 0.568: ## Cascading failure in the cache and datastore tiers  Early in the incident we had paused the Consul agent restart operation that had triggered the problem, even though at that point we had not suspe
  - DAN-219 (causa) [Learnings] 0.551: ## Learnings  The incident has also highlighted some other risks. A brief network outage or partition affecting the cache nodes might trigger the same kind of cascading failure scenario as the Consul 
  - DAN-219 (correcao) [Learnings] 0.467: ## Learnings  We see familiar patterns here which often arise in incidents: performance bottlenecks, cascading failures, dependency on a warm cache, and changes as triggering events. Reading an incide
  - DAN-219 (correcao) [What triggered the incident?] 0.408: ## What triggered the incident?  The Mcrib component is a relatively new piece of software. Prior to Mcrib, we used a distributed locking mechanism based on Consul locks to generate the Mcrouter hash 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.559: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.557: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-219 (esperado: DAN-116)

- busca inicial: 
- justificativa: 
- aprofundar DAN-116: `double free database update crash all impression bus servers root cause fix` — Bate com o incidente atual: uma atualização de banco de dados revelou um bug (double free) que derrubou todos os servidores de um serviço crítico ao mesmo tempo, com um atraso (time delay) necessário para disparar o problema.
- aprofundar DAN-209: `migration critical backend system outage root cause fix Reddit August 2016` — Erro durante migração de um sistema crítico causou um outage prolongado, semelhante a uma atualização de dados derrubando o serviço, embora o resumo não mencione crash simultâneo de todos os servidores.
- novos incidentes nos achados: DAN-189, DAN-146, DAN-209, DAN-164, DAN-066, DAN-106, DAN-103, DAN-154, DAN-116, DAN-092
  - DAN-116 (llm) [sem seção] 0.687: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.686: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-209 (llm) [sem seção] 0.673: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 
  - DAN-209 (llm) [sem seção] 0.658: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact

## q-223 (esperado: DAN-121)

- busca inicial: 
- justificativa: 
- aprofundar DAN-147: `database overload cascading failure insufficient capacity root cause fix` — Bate com o incidente atual: banco de dados sobrecarregado por fila de requisições causando falha em cascata nos serviços. Não menciona explicitamente video player, mas o padrão de sobrecarga de DB afetando múltiplos serviços é idêntico.
- aprofundar DAN-101: `database connection pool exhaustion app timeout root cause fix transaction` — Muito parecido: timeouts intermitentes de app devido a esgotamento do pool de conexões do banco (Go database/sql), afetando muitos endpoints. O sintoma de timeout de serviços devido a DB sobrecarregado é o mesmo do incidente atual.
- aprofundar DAN-164: `influx requests overloaded database replication lag root cause fix` — Semelhança: influxo de requisições sobrecarregou o banco causando lag de replicação. Diferente por envolver exclusão acidental de diretório e perda de dados, mas o gatilho de sobrecarga de DB por volume de requisições é equivalente.
- novos incidentes nos achados: DAN-147, DAN-219, DAN-148, DAN-101, DAN-134, DAN-129, DAN-094, DAN-164, DAN-144, DAN-183
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.602: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.531: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-101 (llm) [sem seção] 0.714: It wasn’t until a few days later that we realised this was the root of our problems. As the timeouts were intermittent and didn’t occur every day, it took a little while to confirm the issue. But, it’
  - DAN-101 (llm) [sem seção] 0.683: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (causa) [sem seção] 0.433: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (correcao) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-101 (correcao) [sem seção] 0.317: Originally, we would receive this event from Slack, and within the lifetime of that HTTP request, we’d perform any responses we needed to, e.g. offering to attach a GitHub link that a user has just po
  - DAN-164 (llm) [Root cause analysis] 0.703: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.684: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-218 (esperado: DAN-116)

- busca inicial: 
- justificativa: 
- aprofundar DAN-222: `Cassandra cluster crash data ingestion root cause fix` — Bate com o incidente atual: dados sendo ingestidos/aplicados no cluster causaram a queda do cluster e depois derrubaram toda a aplicação. Não confirma se foi 'todos os servidores ao mesmo tempo' nem detalhe da correção.
- aprofundar DAN-209: `backend migration error outage root cause fix` — Bate parcialmente: erro durante migração de sistema backend crítico causou outage. O resumo não diz se todos os servidores caíram simultaneamente nem detalha a causa raiz e correção.
- novos incidentes nos achados: DAN-222, DAN-209, DAN-103, DAN-189, DAN-146, DAN-205, DAN-066, DAN-164, DAN-208, DAN-026
  - DAN-222 (llm) [sem seção] 0.736: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (llm) [sem seção] 0.72: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (causa) [sem seção] 0.453: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl
  - DAN-209 (llm) [sem seção] 0.597: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.556: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 

## q-229 (esperado: DAN-125)

- busca inicial: 
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade peak load cascading collapse fix remediation` — Corresponde quase exatamente: banco reduzido recentemente, carga em pico, colapso em cascata de servidores dependentes.
- aprofundar DAN-147: `cascading failure insufficient database capacity request queue remediation capacity planning` — Bate em falha em cascata devido à capacidade insuficiente do banco, mas não menciona redução recente de capacidade.
- aprofundar DAN-096: `peak hour load mysql ProxySQL connections exhaustion failover remediation throttling` — Bate em carga de pico sobrecarregando banco de dados, mas não menciona downsizing nem servidores dependentes em cascata.
- novos incidentes nos achados: DAN-147, DAN-096, DAN-130, DAN-094, DAN-156, DAN-148, DAN-125, DAN-164, DAN-134, DAN-109
  - DAN-125 (llm) [Database performance issues] 0.651: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.571: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.632: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.619: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.696: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.692: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev

## q-262 (esperado: DAN-200)

- busca inicial: 
- justificativa: 
- aprofundar DAN-198: `root cause fix spacecraft computer restart excess CPU load radar` — É o único resultado que envolve um computador de bordo/espacial reiniciando sozinho (mesmo componente e sintoma), embora o gatilho (carga excessiva do radar durante pouso lunar) difira do incidente atual (reinício dias após entrar em operação).
- novos incidentes nos achados: DAN-198, DAN-189, DAN-146, DAN-103, DAN-191, DAN-069, DAN-066, DAN-073, DAN-102, DAN-154, DAN-182, DAN-211, DAN-067, DAN-209, DAN-070, DAN-210, DAN-230, DAN-129, DAN-072, DAN-208
  - DAN-198 (llm) [sem seção] 0.588: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.56: The landing radar provided this information. Despite the "reasonability check" performed by the software, radar data could not be incorporated into the state vector without crew (and ground) approval.
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-228 (esperado: DAN-125)

- busca inicial: 
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade peak cascading collapse dependent servers root cause fix` — É o mais parecido: redução de capacidade do banco, carga de pico e colapso em cascata de servidores dependentes.
- aprofundar DAN-147: `cascading failure insufficient database capacity request queue root cause remediation` — Também envolve falha em cascata por capacidade insuficiente do banco de dados, embora não mencione redução prévia do tamanho.
- aprofundar DAN-096: `peak hour load mysql cluster ProxySQL connections exhaustion failover remediation` — Carga de pico sobre o banco de dados causando falhas, mas não menciona redução de tamanho nem colapso de servidores dependentes.
- novos incidentes nos achados: DAN-147, DAN-156, DAN-194, DAN-096, DAN-219, DAN-164, DAN-148, DAN-094, DAN-130, DAN-125
  - DAN-125 (llm) [Database performance issues] 0.6: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.539: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.623: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.605: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.719: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.706: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev

## q-243 (esperado: DAN-154)

- busca inicial: 
- justificativa: 
- aprofundar DAN-005: `router rule config edge routers crash outage root cause fix rollback` — Bate: CDN (Cloudflare edge) caiu mundialmente devido a erro de configuração. Não bate: não menciona servidores retornando erros explicitamente, apenas roteadores.
- aprofundar DAN-011: `database permission change file limit systemwide outage root cause fix rollback` — Bate: pane sistêmica mundial na CDN causada por mudança que se espalhou pela rede. Não bate: causa é banco de dados/arquivo, não erro direto nos servidores.
- aprofundar DAN-016: `DDoS mitigation rule cookie validation CPU infinite loop data centers root cause fix` — Bate: pane que se propagou por data centers na CDN. Não bate: causa é regra de mitigação/CPU, não queda repentina global genérica.
- novos incidentes nos achados: DAN-011, DAN-008, DAN-184, DAN-007, DAN-016, DAN-023, DAN-129, DAN-005, DAN-137, DAN-106
  - DAN-005 (llm) [Bad Rule] 0.711: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.667: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-011 (llm) [sem seção] 0.562: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (llm) [The query behaviour change] 0.55: ### The query behaviour change  ``` SELECT   name,   type FROM system.columns WHERE   table = 'http_requests_features' order by name; ``` Note how the query does not filter for the database name. With
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.718: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.705: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi

## q-260 (esperado: DAN-197)

- busca inicial: 
- justificativa: 
- aprofundar DAN-197: `root cause Azure breaking change downstream systems fix recovery` — Mais parecido: provedor de nuvem (Azure) fez mudança não anunciada que quebrou sistemas downstream sem aviso, exatamente como nosso caso de chamadas à API de nuvem falhando sem mudanças nosso lado.
- aprofundar DAN-184: `root cause AWS outage third-party dependencies cascade fix` — Bastante parecido: falha na AWS (provedor de nuvem) cascateou para dependências de terceiros, afetando plataforma sem mudanças diretas nela.
- aprofundar DAN-066: `root cause Byzantine failure switch misbehavior API dashboard fix` — Parcialmente parecido: falha na infra do próprio provedor (Cloudflare) derrubou API e dashboard, mas causa é switch com comportamento bizantino, não mudança na API de nuvem consumida.
- novos incidentes nos achados: DAN-066, DAN-029, DAN-197, DAN-067, DAN-154, DAN-018, DAN-205, DAN-184, DAN-222, DAN-145
  - DAN-197 (llm) [sem seção] 0.722: Although APIs are the lifeblood of so many software applications today, the impact on their dependencies when they break can often be overlooked. And while full outages can have a more widespread and 
  - DAN-197 (llm) [Discovery of the Outage] 0.662: ## Discovery of the Outage  While this data was not the most helpful, it confirmed that there was something wrong with our request, despite no changes to how we made the request in months. Until seein
  - DAN-197 (causa) [Discovery of the Outage] 0.42: ## Discovery of the Outage  We first noticed the problem with the partial outage of our Azure CosmosDB service monitor September 14th at 18:42 UTC. We reported to our users that the product was not fu
  - DAN-197 (correcao) [Background] 0.362: ## Background  First, a bit of background on how we use Azure CosmosDB, and how we obtained the debugging data to determine that Azure published a breaking change without telling their customers. Metr
  - DAN-197 (correcao) [Conclusions] 0.356: ## Conclusions  All in all, this was a fairly simple fix, but because of the nature of the API, it could have been worse. The more deeply ingrained a given API is into one’s app, the bigger an effect 
  - DAN-184 (llm) [Service disruption on October 20, 2025] 0.714: ## Service disruption on October 20, 2025  Pete Hamilton  October 22, 2025  —  15 min read  When the internet goes down, our primary job is to help everyone get back up, as fast as possible.  Of the a
  - DAN-184 (llm) [What we learned and next steps] 0.691: ## What we learned and next steps  For outages like this, where so many products and services end up having issues at once, there are always a lot of lessons to be learned.  One key theme we’re hearin
  - DAN-184 (causa) [Initial response] 0.441: ## Initial response  At 07:21 UTC, one of our on-call engineers was paged due to high error rates sending SMS messages and making phone calls. Shortly after, our provider confirmed the impact via thei
  - DAN-184 (correcao) [What we learned and next steps] 0.507: ## What we learned and next steps  - We split worker capacity for notification sending from the escalation worker system and segmented all notification senders by provider  - We reviewed capacity post
  - DAN-184 (correcao) [Scaling our Kubernetes deployments] 0.475: ## Scaling our Kubernetes deployments  We managed to combat acquisition cost by decreasing our autovacuum thresholds and changing our escalation acquisition logic to avoid this type of churn.  These f
  - DAN-066 (llm) [The Dashboard] 0.623: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.59: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.463: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain

## q-242 (esperado: DAN-154)

- busca inicial: 
- justificativa: 
- aprofundar DAN-005: `bad config router rule edge routers crash root cause fix` — Bate: CDN (Cloudflare), queda global/total dos edge routers, causada por mudança de configuração. Não bate: sintoma detalhado (routers crashando vs servidores retornando erro genérico).
- aprofundar DAN-154: `Fastly June 8 global outage software bug customer configuration change root cause fix` — Bate: CDN (Fastly), pane global repentina desencadeada por mudança de configuração. Não bate: causa foi bug de software não descoberto, não erro nos servidores clientes.
- aprofundar DAN-011: `Cloudflare November 18 2025 bot detection database permission file limit systemwide outage root cause fix` — Bate: pane sistêmica da CDN (Cloudflare) originada por mudança de permissão/configuração. Não bate: componente específico (bot-detection) e não queda geral de edge servers.
- novos incidentes nos achados: DAN-011, DAN-008, DAN-005, DAN-154, DAN-067, DAN-007, DAN-023, DAN-006, DAN-109, DAN-205
  - DAN-005 (llm) [Bad Rule] 0.705: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.613: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-154 (llm) [**What happened?**] 0.848: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (llm) [sem seção] 0.836: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s
  - DAN-011 (llm) [sem seção] 0.76: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (llm) [Remediation and follow-up steps] 0.708: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic

## q-261 (esperado: DAN-197)

- busca inicial: 
- justificativa: 
- aprofundar DAN-197: `root cause Azure unannounced breaking change downstream API fix recovery` — Bate com o incidente atual: cloud provider (Azure) mudou algo sem avisar, afetando sistemas downstream sem mudança do cliente. Não bate: é específico do Azure e Metrist, não genérico.
- aprofundar DAN-018: `root cause dashboard API outage excessive API calls fix remediation` — Bate parcialmente: envolve falha de API e dashboard, mas a causa é um bug interno (React component) que gerou chamadas excessivas, não uma mudança do provedor externo sem aviso.
- aprofundar DAN-066: `root cause Byzantine failure API dashboard availability fix remediation` — Bate parcialmente: impacto na disponibilidade da API por falha de infraestrutura (switch), mas não envolve chamada a API de provedor externo nem mudança repentina sem aviso do cliente.
- novos incidentes nos achados: DAN-067, DAN-066, DAN-029, DAN-018, DAN-154, DAN-008, DAN-197, DAN-037, DAN-013, DAN-106
  - DAN-197 (llm) [sem seção] 0.754: Although APIs are the lifeblood of so many software applications today, the impact on their dependencies when they break can often be overlooked. And while full outages can have a more widespread and 
  - DAN-197 (llm) [Background] 0.688: ## Background  First, a bit of background on how we use Azure CosmosDB, and how we obtained the debugging data to determine that Azure published a breaking change without telling their customers. Metr
  - DAN-197 (causa) [Discovery of the Outage] 0.424: ## Discovery of the Outage  While this data was not the most helpful, it confirmed that there was something wrong with our request, despite no changes to how we made the request in months. Until seein
  - DAN-197 (correcao) [Conclusions] 0.356: ## Conclusions  All in all, this was a fairly simple fix, but because of the nature of the API, it could have been worse. The more deeply ingrained a given API is into one’s app, the bigger an effect 
  - DAN-197 (correcao) [Determining the Change] 0.347: ## Determining the Change  The next step was to figure out what actually changed. Our service monitor code hadn’t been touched in several months and is fairly straightforward, using the account and da
  - DAN-018 (llm) [Improving visibility] 0.741: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (llm) [What Happened] 0.703: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-066 (llm) [The Dashboard] 0.666: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.595: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
