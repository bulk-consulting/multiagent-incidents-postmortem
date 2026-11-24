# Research RAG agent (with LLM)

| q | expected | position in search | in initial search | deepened | tools called | found by new query | in findings | new queries | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | no | yes | find → search | yes | yes | 2 | 6 |
| q-022 | DAN-104 | 4 | no | yes | find → search | yes | yes | 2 | 11 |
| q-170 | DAN-018 | 4 | no | yes | find → search | yes | yes | 3 | 6 |
| q-171 | DAN-018 | 4 | no | yes | find → search | yes | yes | 3 | 6 |
| q-222 | DAN-121 | 4 | no | yes | find → search | yes | yes | 3 | 57 |
| q-012 | DAN-211 | 5 | no | yes | find → search | yes | yes | 2 | 52 |
| q-263 | DAN-200 | 5 | no | yes | find → search | yes | yes | 2 | 9 |
| q-032 | DAN-104 | 7 | no | yes | find → search | yes | yes | 2 | 9 |
| q-223 | DAN-121 | 8 | no | yes | find → search | yes | yes | 2 | 10 |
| q-229 | DAN-125 | 10 | no | yes | find → search | yes | yes | 2 | 12 |
| q-262 | DAN-200 | 10 | no | yes | find → search | yes | yes | 2 | 53 |
| q-228 | DAN-125 | 11 | no | yes | find → search | yes | yes | 2 | 53 |
| q-243 | DAN-154 | 12 | no | no | find → search | no | no | 2 | 12 |
| q-242 | DAN-154 | — | no | no | find → search | no | no | 2 | 13 |

## q-020 (expected: DAN-164)

- initial search: 
- final note: 
- deepen DAN-043: `root cause accidental database deletion fix recovery backup restoration` — Directly matches: engineers deleted the production database by accident during operations; same symptom as current incident
- deepen DAN-164: `root cause admin deleted wrong directory database outage fix data loss recovery` — Very similar: tired admin deleted the wrong directory causing database outage and six hours of data lost; matches accidental deletion during maintenance context
- new query: `We just accidentally deleted a production database during maintenance. production database accidentally deleted` → DAN-043, DAN-056, DAN-146, DAN-164, DAN-091, DAN-048, DAN-186, DAN-066, DAN-092, DAN-058
- new query: `production database accidentally deleted during maintenance` → DAN-043, DAN-146, DAN-056, DAN-164, DAN-048, DAN-091, DAN-186, DAN-058, DAN-092, DAN-066
- new query: `database deletion maintenance incident recovery` → DAN-043, DAN-186, DAN-164, DAN-146, DAN-056, DAN-066, DAN-091, DAN-094, DAN-048, DAN-058
- new incidents in the findings: DAN-043, DAN-056, DAN-146, DAN-164, DAN-091, DAN-048, DAN-186, DAN-066, DAN-092, DAN-058, DAN-094
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.696: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [no section] 0.602: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (cause) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (fix) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Root cause analysis] 0.71: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [no section] 0.626: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (cause) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (fix) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (fix) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-022 (expected: DAN-104)

- initial search: 
- final note: 
- deepen DAN-104: `root cause typo command remove servers S3 outage fix dependent systems restart` — Operator command to remove a small number of servers removed too many, taking down storage (S3) and causing dependent/cascading failures — matches current incident closely
- deepen DAN-219: `cache nodes removal caused workload witness cluster service outage root cause fix` — Removal of nodes triggered a service outage with dependent impact, similar removal-trigger theme though component is cache rather than storage
- new query: `Our storage service and everything that depends on it went down right after an operator ran a command to remove a few servers. storage service went down; services depending on storage went down` → DAN-073, DAN-109, DAN-191, DAN-209, DAN-104, DAN-125, DAN-222, DAN-067, DAN-064, DAN-139
- new query: `storage service outage after removing servers operator command` → DAN-073, DAN-209, DAN-104, DAN-230, DAN-189, DAN-191, DAN-109, DAN-067, DAN-146, DAN-222
- new query: `storage dependency cascade failure server removal` → DAN-073, DAN-107, DAN-222, DAN-125, DAN-104, DAN-048, DAN-109, DAN-191, DAN-219, DAN-067
- new incidents in the findings: DAN-073, DAN-109, DAN-191, DAN-209, DAN-104, DAN-125, DAN-222, DAN-067, DAN-064, DAN-139, DAN-107, DAN-230, DAN-189, DAN-048, DAN-219
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.637: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.619: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (cause) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (fix) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (fix) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-219 (llm) [What triggered the incident?] 0.577: ## What triggered the incident?  The PBR step on February 22 updated Consul on 25% of the fleet. It followed two previous 25% steps the prior week, both of which had occurred without any incident. How
  - DAN-219 (llm) [What triggered the incident?] 0.576: ## What triggered the incident?  What caused us to go from a stable serving state to a state of overload? The answer turned out to lie in complex interactions between our application, the Vitess datas
  - DAN-219 (cause) [Learnings] 0.551: ## Learnings  The incident has also highlighted some other risks. A brief network outage or partition affecting the cache nodes might trigger the same kind of cascading failure scenario as the Consul 
  - DAN-219 (fix) [Learnings] 0.467: ## Learnings  We see familiar patterns here which often arise in incidents: performance bottlenecks, cascading failures, dependency on a warm cache, and changes as triggering events. Reading an incide
  - DAN-219 (fix) [What triggered the incident?] 0.408: ## What triggered the incident?  The Mcrib component is a relatively new piece of software. Prior to Mcrib, we used a distributed locking mechanism based on Consul locks to generate the Mcrouter hash 

## q-170 (expected: DAN-018)

- initial search: 
- final note: 
- deepen DAN-018: `React component bug dependency array excessive API calls Tenant Service root cause fix` — This incident matches closely: a dashboard React component bug caused excessive calls to an internal service (Tenant Service), overwhelming the system and cascading into API and dashboard failures - similar to the current incident where the dashboard floods an internal service after a frontend deploy.
- new query: `A API e o painel estão caindo; um serviço interno está recebendo uma enxurrada de chamadas vindas do próprio painel, logo depois de um deploy do frontend. API and dashboard are crashing; internal service receiving flood of calls from dashboard` → DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-102, DAN-129, DAN-037, DAN-182, DAN-218
- new query: `dashboard flood calls internal service after frontend deploy` → DAN-144, DAN-018, DAN-066, DAN-029, DAN-208, DAN-067, DAN-155, DAN-218, DAN-137, DAN-102
- new query: `API dashboard crashing internal service request loop` → DAN-066, DAN-018, DAN-029, DAN-144, DAN-133, DAN-067, DAN-182, DAN-210, DAN-129, DAN-222
- new incidents in the findings: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-102, DAN-129, DAN-037, DAN-182, DAN-218, DAN-133, DAN-210, DAN-222, DAN-208, DAN-155
  - DAN-018 (llm) [What Happened] 0.735: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.656: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (cause) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (fix) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (fix) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T

## q-171 (expected: DAN-018)

- initial search: 
- final note: 
- deepen DAN-018: `root cause React component dependency array excessive API calls fix` — This incident matches closely: a React component bug in the dashboard caused excessive API calls to an internal service after a frontend deploy, cascading into API and dashboard outages — same symptoms as current incident.
- new query: `The API and the dashboard are going down; an internal service is getting flooded with calls coming from the dashboard itself, right after a frontend deploy. API going down; Dashboard going down; Internal service flooded with calls from dashboard` → DAN-066, DAN-029, DAN-018, DAN-144, DAN-067, DAN-133, DAN-155, DAN-218, DAN-129, DAN-145
- new query: `dashboard frontend deploy causes retry storm internal service overload` → DAN-018, DAN-144, DAN-220, DAN-067, DAN-221, DAN-219, DAN-066, DAN-129, DAN-133, DAN-211
- new query: `frontend deploy dashboard infinite request loop API outage cascading failure` → DAN-066, DAN-018, DAN-029, DAN-144, DAN-129, DAN-133, DAN-220, DAN-001, DAN-067, DAN-218
- new incidents in the findings: DAN-066, DAN-029, DAN-018, DAN-144, DAN-067, DAN-133, DAN-155, DAN-218, DAN-129, DAN-145, DAN-220, DAN-001, DAN-221, DAN-219, DAN-211
  - DAN-018 (llm) [What Happened] 0.604: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.581: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (cause) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (fix) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (fix) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 

## q-222 (expected: DAN-121)

- initial search: 
- final note: 
- deepen DAN-121: `database backend overloaded throttle requests iPlayer timeout root cause fix` — This incident matches closely: database backend overloaded, throttling requests from various services, and BBC iPlayer (video player) timing out - same pattern as current incident
- new query: `O banco de backend está sobrecarregado e limitando requisições, e vários serviços, inclusive o player de vídeo, estão dando timeout. backend database overloaded and rate-limiting requests; video player timeouts` → DAN-147, DAN-129, DAN-016, DAN-121, DAN-144, DAN-186, DAN-164, DAN-148, DAN-101, DAN-134
- new query: `backend database overloaded rate limiting requests service timeouts` → DAN-147, DAN-129, DAN-001, DAN-164, DAN-016, DAN-094, DAN-101, DAN-148, DAN-134, DAN-219
- new query: `database overload rate limiting causing video player timeouts` → DAN-147, DAN-219, DAN-016, DAN-186, DAN-148, DAN-121, DAN-101, DAN-134, DAN-223, DAN-164
- new incidents in the findings: DAN-147, DAN-129, DAN-016, DAN-121, DAN-144, DAN-186, DAN-164, DAN-148, DAN-101, DAN-134, DAN-001, DAN-094, DAN-219, DAN-223
  - DAN-121 (llm) [no section] 0.55: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [no section] 0.504: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (cause) [no section] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim

## q-012 (expected: DAN-211)

- initial search: 
- final note: 
- deepen DAN-020: `service discovery config root cause fix dependent client cascading failure` — Directly mentions service discovery being brought down globally by a dependent client, matching the current incident's service discovery slowness and cascading service failures.
- deepen DAN-211: `Consul streaming BoltDB issue root cause fix service discovery` — Mentions Consul (a service discovery tool) issues and outage, which matches the affected component (service discovery layer) in the current incident.
- deepen DAN-109: `metadata services load timeout response times storage nodes cascading failure root cause fix` — Describes metadata services exceeding timeout values and cascading node failures, which parallels service discovery slow writes timing out and other services failing.
- new query: `Our service discovery layer is slow and writes are timing out, and other services are starting to fail. service discovery layer is slow; writes are timing out; other services are starting to fail` → DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-101, DAN-066, DAN-222, DAN-113, DAN-144
- new query: `service discovery slow writes timing out cascading service failures` → DAN-220, DAN-020, DAN-129, DAN-066, DAN-109, DAN-211, DAN-222, DAN-219, DAN-101, DAN-221
- new query: `service discovery layer write timeout dependency failure other services failing` → DAN-020, DAN-220, DAN-066, DAN-109, DAN-222, DAN-129, DAN-205, DAN-211, DAN-151, DAN-113
- new incidents in the findings: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-101, DAN-066, DAN-222, DAN-113, DAN-144, DAN-219, DAN-205, DAN-221, DAN-151
  - DAN-020 (llm) [A thundering herd] 0.697: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (llm) [The failure of a core system] 0.694: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (cause) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (fix) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (fix) [Improve the resilience of service discovery] 0.401: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.688: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  But what was going on with the slow leaders? We did not figure this out during the incident, but HashiCorp engineers determined the root cause in the
  - DAN-211 (llm) [Outage Summary] 0.667: ### Outage Summary  The outage was unique in both duration and complexity. The team had to address a number of challenges in sequence to understand the root cause and bring the service back up.  - The
  - DAN-211 (cause) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (fix) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (fix) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.626: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.625: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (cause) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (fix) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (fix) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-263 (expected: DAN-200)

- initial search: 
- final note: 
- deepen DAN-200: `priority inversion VxWorks system reset root cause fix priority inheritance patch` — Mars Pathfinder onboard computer reset a few days after landing — matches current incident's onboard computer resetting days after going into operation; same spacecraft/onboard-computer failure pattern.
- deepen DAN-198: `Apollo 11 rendezvous radar CPU load computer restart root cause fix` — Apollo 11 spacecraft computer restarted — similar onboard-computer reset symptom, but triggered by radar during landing rather than days after operation, so a weaker match.
- new query: `The onboard computer keeps resetting itself every now and then, a few days after going into operation. onboard computer resets itself` → DAN-198, DAN-191, DAN-189, DAN-103, DAN-200, DAN-073, DAN-106, DAN-154, DAN-146, DAN-066
- new query: `onboard computer reset itself after days in operation` → DAN-198, DAN-146, DAN-103, DAN-191, DAN-189, DAN-073, DAN-200, DAN-210, DAN-069, DAN-211
- new query: `onboard computer spontaneous reboot reset production` → DAN-189, DAN-198, DAN-146, DAN-191, DAN-103, DAN-073, DAN-069, DAN-066, DAN-067, DAN-043
- new incidents in the findings: DAN-198, DAN-191, DAN-189, DAN-103, DAN-200, DAN-073, DAN-106, DAN-154, DAN-146, DAN-066, DAN-210, DAN-069, DAN-211, DAN-067, DAN-043
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.669: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.63: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-200 (cause) [THE FAILURE] 0.577: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (fix) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (fix) [HUMAN NATURE, DEADLINE PRESSURES] 0.436: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-198 (llm) [no section] 0.724: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [no section] 0.68: This phenomenon occurred whenever the RR mode was in SLEW or AUTO, regardless of whether the rendezvous radar itself was powered up. | | The CDU interface counters in the LGC were incremented or decre
  - DAN-198 (cause) [no section] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (fix) [no section] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (fix) [no section] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-032 (expected: DAN-104)

- initial search: 
- final note: 
- deepen DAN-104: `root cause typo command remove servers fix recovery S3 storage service down` — Matches current incident: operator ran a routine command to remove a small number of servers but it removed a larger set, taking down a storage service (S3) that did not recover on its own.
- new query: `An operator just ran a routine command to remove a few servers and now our storage service is completely down and not recovering. storage service completely down; storage service not recovering` → DAN-109, DAN-067, DAN-191, DAN-210, DAN-073, DAN-189, DAN-146, DAN-070, DAN-103, DAN-064
- new query: `storage service down after operator removed servers routine command` → DAN-104, DAN-146, DAN-189, DAN-103, DAN-109, DAN-073, DAN-209, DAN-191, DAN-230, DAN-064
- new query: `storage service not recovering after node removal deletion` → DAN-109, DAN-112, DAN-143, DAN-219, DAN-210, DAN-026, DAN-118, DAN-029, DAN-073, DAN-145
- new incidents in the findings: DAN-109, DAN-067, DAN-191, DAN-210, DAN-073, DAN-189, DAN-146, DAN-070, DAN-103, DAN-064, DAN-112, DAN-143, DAN-219, DAN-104, DAN-209
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.635: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.617: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (cause) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (fix) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (fix) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q-223 (expected: DAN-121)

- initial search: 
- final note: 
- deepen DAN-121: `database backend overloaded throttle requests iPlayer video timeout root cause fix` — This incident matches closely: database backend overloaded, throttling requests from services, and BBC iPlayer (video player) timing out — same symptoms as the current incident.
- new query: `The backend database is overloaded and throttling requests, and several services, including the video player, are timing out. backend database overloaded and throttling requests; video player timing out` → DAN-147, DAN-148, DAN-101, DAN-219, DAN-164, DAN-121, DAN-134, DAN-129, DAN-156, DAN-220
- new query: `backend database overloaded throttling requests video player timeout` → DAN-147, DAN-219, DAN-148, DAN-121, DAN-101, DAN-134, DAN-129, DAN-164, DAN-094, DAN-186
- new query: `database connection pool exhaustion service timeout video streaming` → DAN-101, DAN-148, DAN-134, DAN-183, DAN-096, DAN-144, DAN-129, DAN-217, DAN-147, DAN-220
- new incidents in the findings: DAN-147, DAN-148, DAN-101, DAN-219, DAN-164, DAN-121, DAN-134, DAN-129, DAN-156, DAN-220, DAN-183, DAN-094, DAN-186, DAN-096, DAN-144
  - DAN-121 (llm) [no section] 0.546: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [no section] 0.503: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (cause) [no section] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim

## q-229 (expected: DAN-125)

- initial search: 
- final note: 
- deepen DAN-125: `database capacity downgrade downsizing peak load cascading collapse dependent servers root cause fix` — Directly matches: database downgrade/downsizing caused lack of capacity at peak, leading to cascading collapse of dependent servers — same trigger and failure mode as current incident.
- deepen DAN-147: `cascading failure insufficient database capacity request queue root cause fix capacity planning monitoring` — Strong match: cascading failure due to insufficient database capacity under load, with inadequate capacity planning — same component and symptom pattern.
- new query: `At peak time the database cannot handle the load and the servers that depend on it are failing in a cascade; we downsized it recently. database cannot handle peak load; dependent servers failing in cascade` → DAN-147, DAN-156, DAN-194, DAN-094, DAN-164, DAN-096, DAN-130, DAN-125, DAN-129, DAN-066
- new query: `database cannot handle peak load cascading failures dependent servers downsized` → DAN-147, DAN-156, DAN-219, DAN-094, DAN-130, DAN-096, DAN-194, DAN-129, DAN-125, DAN-164
- new query: `database overloaded peak time cascading server failures after downsizing` → DAN-147, DAN-156, DAN-164, DAN-130, DAN-194, DAN-125, DAN-219, DAN-209, DAN-094, DAN-096
- new incidents in the findings: DAN-147, DAN-156, DAN-194, DAN-094, DAN-164, DAN-096, DAN-130, DAN-125, DAN-129, DAN-066, DAN-219, DAN-209
  - DAN-125 (llm) [Database performance issues] 0.633: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.541: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (cause) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (fix) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (fix) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.642: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.592: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-262 (expected: DAN-200)

- initial search: 
- final note: 
- deepen DAN-200: `priority inversion VxWorks system reset root cause fix priority inheritance` — Mars Pathfinder spacecraft had system resets a few days after landing, matching onboard computer restarting days after entering operation
- deepen DAN-198: `Apollo 11 rendezvous radar CPU load spacecraft computer restart root cause fix` — Apollo 11 spacecraft computer restarted due to excess CPU load, matching spontaneous onboard computer restart but timing is during landing not days after
- deepen DAN-116: `double free database update crash time delay staging root cause fix` — Crash triggered by a time delay not present in staging, loosely matches days-after-operation timing but component is servers not onboard computer
- new query: `O computador de bordo está reiniciando sozinho de tempos em tempos, alguns dias depois de entrar em operação. onboard computer restarts spontaneously` → DAN-073, DAN-103, DAN-198, DAN-189, DAN-191, DAN-066, DAN-146, DAN-210, DAN-200, DAN-043
- new query: `onboard computer spontaneous restart reboot embedded avionics` → DAN-198, DAN-189, DAN-103, DAN-073, DAN-191, DAN-069, DAN-066, DAN-076, DAN-072, DAN-064
- new query: `computer restarts automatically after days operation watchdog memory leak` → DAN-107, DAN-103, DAN-188, DAN-116, DAN-180, DAN-216, DAN-189, DAN-016, DAN-088, DAN-144
- new incidents in the findings: DAN-073, DAN-103, DAN-198, DAN-189, DAN-191, DAN-066, DAN-146, DAN-210, DAN-200, DAN-043, DAN-107, DAN-188, DAN-116, DAN-180, DAN-216
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.673: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [THE FAILURE] 0.651: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (cause) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (fix) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (fix) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [no section] 0.737: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [no section] 0.694: | TALES FROM THE LUNAR MODULE GUIDANCE COMPUTER Don Eyles | | (A paper presented to the 27th annual Guidance and Control Conference of the American Astronautical Society (AAS), in Breckenridge, Colora
  - DAN-198 (cause) [no section] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (fix) [no section] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (fix) [no section] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,
  - DAN-116 (llm) [no section] 0.734: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [no section] 0.668: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (cause) [no section] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (fix) [no section] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (fix) [no section] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-228 (expected: DAN-125)

- initial search: 
- final note: 
- deepen DAN-125: `database capacity downgrade peak load cascading collapse dependent servers fix` — Matches the current incident closely: database size was reduced (downgrade to save spend), then at peak the database could not handle load and dependent servers collapsed in cascade.
- deepen DAN-147: `cascading failure insufficient database capacity request queue fix` — Matches the cascading failure caused by insufficient/overloaded database capacity, though it does not explicitly mention a recent size reduction.
- deepen DAN-096: `peak hour load mysql cluster connection exhaustion primary failover fix` — Matches peak-hour database overload causing repeated failures, but does not involve downsizing the database.
- new query: `No horário de pico, o banco de dados não está aguentando a carga e os servidores que dependem dele estão caindo em cascata; reduzimos o tamanho dele há pouco tempo. database cannot handle peak load; dependent servers crashing in cascade` → DAN-147, DAN-156, DAN-164, DAN-096, DAN-194, DAN-094, DAN-148, DAN-129, DAN-125, DAN-048
- new query: `database cannot handle peak load dependent servers crashing cascade reduced size` → DAN-147, DAN-156, DAN-164, DAN-094, DAN-194, DAN-096, DAN-129, DAN-125, DAN-186, DAN-130
- new query: `database downsizing cascade failure dependent servers peak load` → DAN-147, DAN-156, DAN-125, DAN-094, DAN-164, DAN-146, DAN-130, DAN-096, DAN-194, DAN-129
- new incidents in the findings: DAN-147, DAN-156, DAN-164, DAN-096, DAN-194, DAN-094, DAN-148, DAN-129, DAN-125, DAN-048, DAN-146, DAN-130, DAN-186
  - DAN-125 (llm) [Database performance issues] 0.633: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.551: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (cause) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (fix) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (fix) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.627: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.591: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.777: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.685: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (cause) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (fix) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (fix) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev

## q-243 (expected: DAN-154)

- initial search: 
- final note: 
- deepen DAN-005: `root cause bad config router rule edge routers crash fix rollback` — Worldwide CDN outage where all edge routers crashed, taking down all of Cloudflare — closely matches 'CDN went down worldwide and most servers returning errors'.
- deepen DAN-011: `root cause bot detection system permission change file exceeded limits systemwide outage fix` — Systemwide Cloudflare outage caused by a software change propagating through the network — matches worldwide CDN failure.
- deepen DAN-016: `root cause DDoS mitigation rule rate-limiting bug cookie validation infinite loop CPU fix rollback` — CDN incident causing HTTP request handler processes to consume 100% CPU across data centers — could explain most servers returning errors.
- new query: `The CDN suddenly went down worldwide and most of our servers are returning errors. CDN went down worldwide; most servers returning errors` → DAN-011, DAN-008, DAN-026, DAN-205, DAN-129, DAN-067, DAN-109, DAN-145, DAN-209, DAN-007
- new query: `CDN outage worldwide servers returning errors` → DAN-011, DAN-008, DAN-023, DAN-067, DAN-005, DAN-007, DAN-006, DAN-016, DAN-026, DAN-205
- new query: `CDN edge server failure global error responses` → DAN-011, DAN-008, DAN-005, DAN-016, DAN-010, DAN-007, DAN-184, DAN-129, DAN-193, DAN-067
- new incidents in the findings: DAN-011, DAN-008, DAN-026, DAN-205, DAN-129, DAN-067, DAN-109, DAN-145, DAN-209, DAN-007, DAN-023, DAN-005, DAN-006, DAN-016, DAN-010
  - DAN-005 (llm) [Bad Rule] 0.682: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.623: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (cause) [no section] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (fix) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (fix) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-011 (llm) [Remediation and follow-up steps] 0.623: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [Memory preallocation] 0.577: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (cause) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (fix) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (fix) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.716: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.704: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (cause) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (fix) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (fix) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi

## q-242 (expected: DAN-154)

- initial search: 
- final note: 
- deepen DAN-011: `bot detection database permissions file limit systemwide outage root cause fix` — Cloudflare is a CDN; this was a systemwide worldwide outage matching the current incident's worldwide CDN down symptom
- deepen DAN-005: `router rule config edge routers crash taking down all Cloudflare root cause fix` — All edge routers crashed taking down the entire CDN worldwide, matching worldwide CDN outage and servers returning errors
- deepen DAN-016: `DDoS mitigation rule rate limiting cookie validation infinite loop CPU propagating data centers root cause fix` — Cloudflare CDN issue that propagated across data centers causing widespread failures, similar to worldwide CDN impact
- new query: `A CDN caiu no mundo todo de repente e a maioria dos nossos servidores está devolvendo erro. CDN down worldwide; servers returning errors` → DAN-011, DAN-109, DAN-145, DAN-008, DAN-026, DAN-009, DAN-106, DAN-129, DAN-067, DAN-066
- new query: `CDN worldwide outage servers returning errors` → DAN-011, DAN-008, DAN-005, DAN-023, DAN-067, DAN-016, DAN-006, DAN-007, DAN-026, DAN-205
- new query: `CDN edge server failure global downtime origin server errors` → DAN-011, DAN-008, DAN-005, DAN-007, DAN-026, DAN-209, DAN-016, DAN-129, DAN-137, DAN-154
- new incidents in the findings: DAN-011, DAN-109, DAN-145, DAN-008, DAN-026, DAN-009, DAN-106, DAN-129, DAN-067, DAN-066, DAN-005, DAN-023, DAN-016, DAN-006, DAN-007
  - DAN-011 (llm) [Remediation and follow-up steps] 0.618: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [Memory preallocation] 0.58: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (cause) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (fix) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (fix) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-005 (llm) [Bad Rule] 0.741: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.733: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (cause) [no section] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (fix) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (fix) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.741: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.715: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (cause) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (fix) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (fix) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
