# Research RAG agent (with LLM)

| q | expected | position in search | in initial search | deepened | tools called | found by new query | in findings | new queries | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | yes | yes | search | no | yes | 0 | 8 |
| q-022 | DAN-104 | 4 | no | no | search | no | no | 0 | 30 |
| q-170 | DAN-018 | 4 | yes | yes | search | no | yes | 0 | 7 |
| q-171 | DAN-018 | 4 | yes | yes | search | no | yes | 0 | 9 |
| q-222 | DAN-121 | 4 | no | no | search | no | no | 0 | 8 |
| q-012 | DAN-211 | 5 | no | no | search | no | no | 0 | 5 |
| q-263 | DAN-200 | 5 | yes | yes | search | no | yes | 0 | 8 |
| q-032 | DAN-104 | 7 | no | no | search | no | no | 0 | 12 |
| q-223 | DAN-121 | 8 | yes | yes | search | no | yes | 0 | 11 |
| q-229 | DAN-125 | 10 | yes | yes | search | no | yes | 0 | 12 |
| q-262 | DAN-200 | 10 | yes | yes | search | no | yes | 0 | 22 |
| q-228 | DAN-125 | 11 | no | no | search | no | no | 0 | 21 |
| q-243 | DAN-154 | 12 | no | no | search | no | no | 0 | 11 |
| q-242 | DAN-154 | — | no | no | search | no | no | 0 | 19 |

## q-020 (expected: DAN-164)

- initial search: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-091, DAN-186, DAN-092, DAN-066, DAN-058
- final note: 
- deepen DAN-043: `accidentally deleted production database recovery backup restoration fix` — Direct match: engineers deleted the production database by accident during operations, exactly like the current incident; it used DigitalOcean managed backups and restored in 30 minutes with data loss.
- deepen DAN-164: `admin deleted wrong directory database outage root cause fix` — Similar: a tired admin deleted the wrong directory causing database outage and data loss, though triggered by replication lag rather than pure maintenance mistake.
- deepen DAN-056: `accidental environment variable truncated production database recovery` — Related: accidental action caused production database data loss, but via test truncation rather than direct deletion during maintenance.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.712: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [no section] 0.657: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (cause) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (fix) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Root cause analysis] 0.699: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [no section] 0.588: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (cause) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (fix) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (fix) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.728: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.661: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (cause) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (fix) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (fix) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-022 (expected: DAN-104)

- initial search: DAN-073, DAN-109, DAN-209, DAN-222, DAN-191, DAN-139, DAN-067, DAN-205, DAN-071, DAN-230
- final note: 
- deepen DAN-109: `DynamoDB storage nodes down metadata timeout retry storm cause fix` — Storage service (DynamoDB) went down with related impacts; nodes took themselves down and cascaded, matching storage-plus-dependents down, though the trigger was a network disruption not an operator removal command.
- deepen DAN-073: `storage volume failure outage dependent services root cause fix` — A storage volume failure knocked down the site and dependent user programs, matching storage-plus-dependents down, but the trigger was a volume failure rather than an operator removing servers.
- deepen DAN-222: `Cassandra cluster crash producers blocked queue insert outage fix` — A Cassandra cluster crash cascaded to producers blocking on queue inserts and failed the whole application, matching a storage-cluster failure cascading to dependents, though not an operator server-removal trigger.
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.69: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.665: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (cause) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (fix) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (fix) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was
  - DAN-073 (llm) [The details¶] 0.709: ### The details¶  At 16:06 UTC on 7 July 2020, a storage volume failure on one of our storage servers caused a number of outages, starting with our own site and also with our users’ programs (includin
  - DAN-073 (llm) [17:04¶] 0.685: #### 17:04¶  By this point we had become sure that the system was getting blocked on storage IO, but the problem did not seem to be the machine itself like the original indications had suggested. Howe
  - DAN-073 (cause) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (fix) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (fix) [Next steps¶] 0.303: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-222 (llm) [no section] 0.682: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (llm) [no section] 0.67: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (cause) [no section] 0.457: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (fix) [no section] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (fix) [no section] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl

## q-170 (expected: DAN-018)

- initial search: DAN-029, DAN-066, DAN-144, DAN-018, DAN-210, DAN-129, DAN-017, DAN-182, DAN-133, DAN-191
- final note: 
- deepen DAN-018: `dashboard React component bug excessive API calls dependency array frontend deploy fix rollback` — The current incident is a dashboard flood of calls to an internal service after a frontend deploy, crashing API and dashboard; DAN-018 describes exactly a React dashboard bug causing excessive API calls after a frontend change, cascading into API/dashboard outages. What does not match: the specific component (Tenant Service vs generic internal service).
- deepen DAN-144: `flapping service thundering herd frontend memory queues internal service fix` — Both involve frontend services overwhelming internal services and cascading outages; however DAN-144 is a flapping service causing a reconnect thundering herd, not a dashboard-generated call flood after a frontend deploy.
- deepen DAN-017: `deployment tool bug staging build version traffic unauthorized endpoint fix` — Both involve a deploy triggering cascading failures; however DAN-017 is a deployment tool misrouting traffic to a staging endpoint, not a dashboard flooding an internal service after a frontend deploy.
  - DAN-018 (llm) [What Happened] 0.683: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.652: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (cause) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (fix) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (fix) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-144 (llm) [Summary] 0.521: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.502: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (cause) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (fix) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (fix) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-017 (llm) [Timeline] 0.585: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (llm) [Analysis] 0.574: ### Analysis  Workers KV is a low-latency key-value store that allows users to store persistent data on Cloudflare's network, as close to the users as possible. This distributed key-value store is use
  - DAN-017 (cause) [Analysis] 0.422: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (fix) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (fix) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 

## q-171 (expected: DAN-018)

- initial search: DAN-066, DAN-029, DAN-144, DAN-018, DAN-210, DAN-189, DAN-209, DAN-191, DAN-129, DAN-067
- final note: 
- deepen DAN-018: `React component bug dashboard excessive API calls Tenant Service dependency array root cause fix` — Matches current incident: dashboard flooding internal service with calls after frontend deploy, taking API and dashboard down
  - DAN-018 (llm) [What Happened] 0.776: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.696: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (cause) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (fix) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (fix) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T

## q-222 (expected: DAN-121)

- initial search: DAN-147, DAN-164, DAN-129, DAN-016, DAN-144, DAN-186, DAN-001, DAN-219, DAN-094, DAN-148
- final note: 
- deepen DAN-147: `database overload rate limiting capacity planning fix cascading failure` — Matches current incident: database overloaded and rate-limiting causing cascading timeouts. Duo describes request queue overloading insufficient database capacity with cascading failure.
- deepen DAN-164: `database overloaded influx requests replication lag outage recovery fix` — Matches current incident: influx of requests overloaded the database causing service issues. GitLab postmortem covers database outage and recovery.
- deepen DAN-186: `hosted database limits hit migration recovery outage cause` — Matches current incident: limits were hit for a hosted database causing outage. Instapaper describes database limit issues and migration to new database.
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.628: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.575: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Timeline] 0.714: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.699: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (cause) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (fix) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (fix) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-186 (llm) [**Prevention**] 0.687: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-186 (llm) [**Limited service restoration**] 0.675: # **Limited service restoration**  We didn’t have a good disaster recovery plan in the event our MySQL instance failed with a critical filesystem issue that all of our backups were also subject to.  A
  - DAN-186 (cause) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (fix) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (fix) [**Full service restoration**] 0.454: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma

## q-012 (expected: DAN-211)

- initial search: DAN-191, DAN-220, DAN-020, DAN-205, DAN-067, DAN-129, DAN-209, DAN-106, DAN-109, DAN-066
- final note: 
- deepen DAN-020: `service discovery config bad client brought down global discovery root cause fix` — Directly involves service discovery being brought down by a dependent client, matching the current incident's service discovery slowness and cascading impact.
- deepen DAN-220: `cascading failure microservice lack exponential backoff service degradation root cause fix` — Describes a cascading failure causing service degradation, similar to the current incident where other services start failing.
- deepen DAN-109: `network disruption metadata services timeout storage nodes retry cascading load root cause fix` — Involves timeouts exceeding values causing nodes to take themselves down and retry, increasing load—a timeout-driven cascade similar to current write timeouts.
  - DAN-020 (llm) [The failure of a core system] 0.677: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.668: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (cause) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (fix) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (fix) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-220 (llm) [First symptoms: two months before the outage] 0.654: ## First symptoms: two months before the outage  Two months before the big outage we had an incident connected with one of our smallest backend services: Popcount. Popcount (this is our internal name)
  - DAN-220 (llm) [Lessons learned] 0.637: ## Lessons learned  - We should have prioritized fixing the backoff bug in the client after the first Popcount incident, we did not assign the right severity. We thought having the fast fail mechanism
  - DAN-220 (cause) [The night of April 27th] 0.485: ## The night of April 27th  It was a rainy Saturday night in Stockholm. Some of our engineers were online on IRC, and discovered that Popcount was unhealthy again. We thought the fast fail logic we in
  - DAN-220 (fix) [Remediations in place after the second incident] 0.641: ## Remediations in place after the second incident  After the outage (infamously known as OPS-6000 in our incident tracking system), we held a post-mortem meeting where we invited the entire Technolog
  - DAN-220 (fix) [Remediations: why are they important?] 0.568: ## Remediations: why are they important?  For every incident we hold a post-mortem meeting. The goal of this meeting is producing a list of remediations that we need to put in place in order to preven
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.668: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.647: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (cause) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (fix) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (fix) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-263 (expected: DAN-200)

- initial search: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-146, DAN-073, DAN-106, DAN-069, DAN-066
- final note: 
- deepen DAN-200: `computer reset priority inversion VxWorks patch fix days after landing` — Mars Pathfinder resets a few days after landing matches the current incident's onboard computer resetting days after going into operation; both are spacecraft onboard computers.
- deepen DAN-198: `rendezvous radar CPU load restart fix Apollo 11` — Apollo 11 spacecraft computer restart matches the reset symptom, but it happened during landing due to radar load rather than days after operation, so it is less similar.
  - DAN-200 (llm) [THE FAILURE] 0.616: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [HOW WE FOUND IT] 0.601: ## HOW WE FOUND IT  The software that flies on Mars Pathfinder has several debug features within it that are used in the lab but are not used on the flight spacecraft (not used because some of them pr
  - DAN-200 (cause) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (fix) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (fix) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [no section] 0.735: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [no section] 0.708: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (cause) [no section] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (fix) [no section] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (fix) [no section] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-032 (expected: DAN-104)

- initial search: DAN-073, DAN-118, DAN-109, DAN-209, DAN-222, DAN-191, DAN-067, DAN-210, DAN-139, DAN-230
- final note: 
- deepen DAN-118: `routine script command deleted customer instances outage restoration backups root cause fix` — Matches the trigger (a routine command/script run by an operator caused the outage) and the slow, incomplete recovery; differs because it involved customer instance deletion rather than server removal from a storage service.
- deepen DAN-073: `storage volume failure storage server outage recovery root cause fix` — Matches the component (storage service/storage servers completely down) but the trigger was a volume failure rather than an operator command to remove servers.
- deepen DAN-109: `storage nodes took themselves down metadata load timeout not recovering retry root cause fix` — Matches the 'not recovering' symptom with storage nodes shutting themselves down under load, but the trigger was a network disruption, not a server-removal command.
  - DAN-118 (llm) [Workstream 2: Early recovery and the Restoration 1 approach] 0.618: #### Workstream 2: Early recovery and the Restoration 1 approach  **Timestamp: Days 1-4 (April 5th – 9th)**  We understood what caused the site deletion on April 5th at 08:53 UTC, within an hour after
  - DAN-118 (llm) [Workstream 1: Detection, starting the recovery & identifying our approach] 0.607: #### Workstream 1: Detection, starting the recovery & identifying our approach  **Timestamp: Days 1-2 (April 5th – 6th)**  At 08:53 UTC on April 5th, we identified that the Insight app script caused t
  - DAN-118 (cause) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (fix) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (fix) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si
  - DAN-073 (llm) [18:23¶] 0.705: #### 18:23¶  At this time, livefile1 had the new volumes attached, and we were logged in and checking everything out. The server needed to do a full filesystem check before the storage was available, 
  - DAN-073 (llm) [Speeding up recovery¶] 0.704: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (cause) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (fix) [Next steps¶] 0.303: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (fix) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.58: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.571: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (cause) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (fix) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (fix) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-223 (expected: DAN-121)

- initial search: DAN-147, DAN-219, DAN-148, DAN-164, DAN-101, DAN-129, DAN-134, DAN-121, DAN-144, DAN-156
- final note: 
- deepen DAN-121: `database overload throttling requests iPlayer video player timeout root cause fix` — This incident matches the current one almost exactly: database backend overloaded, started throttling requests from various services, and BBC iPlayer (video player) began timing out and failing completely.
- deepen DAN-147: `cascading failure request queue overloading database capacity root cause fix` — Similar pattern: cascading failure due to request queue overloading insufficient database capacity, though it doesn't specifically mention video player timeouts.
- deepen DAN-101: `connection pool exhaustion app timeouts root cause transaction wrapping fix` — Related: app timeouts from database connection pool issues, but the root cause was an unnecessary transaction wrapping every Slack modal submission rather than pure database overload/throttling.
  - DAN-121 (llm) [no section] 0.582: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [no section] 0.526: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (cause) [no section] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.617: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.599: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-101 (llm) [no section] 0.657: It wasn’t until a few days later that we realised this was the root of our problems. As the timeouts were intermittent and didn’t occur every day, it took a little while to confirm the issue. But, it’
  - DAN-101 (llm) [no section] 0.652: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (cause) [no section] 0.433: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (fix) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-101 (fix) [no section] 0.317: Originally, we would receive this event from Slack, and within the lifetime of that HTTP request, we’d perform any responses we needed to, e.g. offering to attach a GitHub link that a user has just po

## q-229 (expected: DAN-125)

- initial search: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-129, DAN-091, DAN-125
- final note: 
- deepen DAN-125: `database capacity downgrade peak load cascading collapse fix root cause` — Exact match: downsized database, peak load, cascading collapse of dependent servers
- deepen DAN-147: `cascading failure request queue insufficient database capacity fix root cause` — Strong match: cascading failure from overloaded insufficient database capacity, but no explicit downsizing
- deepen DAN-091: `peak load database queue backed up dependent servers fix root cause` — Good match: peak load saturating primary database queue with downstream effects, but no downsizing or explicit cascade
  - DAN-125 (llm) [Database performance issues] 0.659: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.549: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (cause) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (fix) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (fix) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.625: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.599: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-091 (llm) [Postmortem] 0.659: ## Postmortem  We've also moved over 50 percent of the data that was in our primary database onto its own deployment. The data was orthogonal and didn't need to be co-located, but its heavy use was ca
  - DAN-091 (llm) [Postmortem] 0.651: ## Postmortem  Getting back to the architecture, we've known for a while that our queue model needs to be rebuilt and we've been laying the foundation to get there with the items outlined above, but w
  - DAN-091 (cause) [Postmortem] 0.449: ## Postmortem  THURSDAY 09:00 UTC: We worked to bring up excess capacity to handle the backlog and push builds in as fast as we could. Then we learned that the throttles we had built into our build sc
  - DAN-091 (fix) [Resolved] 0.326: ## Resolved  We’re continuing to see builds running normally. We will be monitoring closely throughout the day. Please contact us in support if you’re seeing issues with your builds.  Posted Oct 15, 2
  - DAN-091 (fix) [Postmortem] 0.404: ## Postmortem  We identified a couple of changes that required additional work but had performed well in evaluation and rolled them back. Unfortunately, by that time the queued DB operations were back

## q-262 (expected: DAN-200)

- initial search: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073, DAN-189, DAN-146, DAN-210, DAN-043, DAN-200
- final note: 
- deepen DAN-200: `system resets days after landing priority inversion VxWorks patch priority inheritance` — matches spontaneous onboard computer restarts days after entering operation; differs in being a Mars lander with a known OS scheduler bug
- deepen DAN-198: `Apollo 11 rendezvous radar CPU load computer restart lunar landing cause fix` — matches computer restarts but triggered by radar CPU load during landing, not days after operation
- deepen DAN-103: `asynchronous task processing subsystem failure root cause fix` — distributed system failure, unrelated to spontaneous onboard computer restarts
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.635: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [THE FAILURE] 0.623: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (cause) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (fix) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (fix) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [no section] 0.745: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [no section] 0.709: | TALES FROM THE LUNAR MODULE GUIDANCE COMPUTER Don Eyles | | (A paper presented to the 27th annual Guidance and Control Conference of the American Astronautical Society (AAS), in Breckenridge, Colora
  - DAN-198 (cause) [no section] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (fix) [no section] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (fix) [no section] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,
  - DAN-103 (llm) [How did we respond? #] 0.704: ## How did we respond? #  Because the mechanism was poorly monitored, we had no idea about the problem until 8:40 AM. At 9:20 AM, we managed to start processing queued tasks. However, we could not ret
  - DAN-103 (llm) [Consequences of failure #] 0.682: ## Consequences of failure #  The failure caused several hours of delay in task processing. Some tasks that were submitted after 11th September 2014, but for some reason had not been correctly re-proc
  - DAN-103 (cause) [What happened? #] 0.567: ## What happened? #  On 23rd October, at 4:19 AM a wrong server was restarted by mistake. In fact, it was the wrong “half” of a blade server running in the active datacentre and hosting important comp
  - DAN-103 (fix) [Prevention? #] 0.483: ## Prevention? #  It is necessary to monitor the task processing subsystem. Currently, we do not notice most of the system problems. Each restart of any Allegro Platform server must be supervised by a
  - DAN-103 (fix) [How did we respond? #] 0.495: ## How did we respond? #  The third thing we needed to do, was finding the cause of this enormous number of tasks. For reasons which we still do not understand, after rebooting, daemons started to ret

## q-228 (expected: DAN-125)

- initial search: DAN-147, DAN-164, DAN-156, DAN-048, DAN-096, DAN-043, DAN-094, DAN-209, DAN-134, DAN-109
- final note: 
- deepen DAN-147: `cascading failure insufficient database capacity capacity planning remediation` — Matches cascading failure and insufficient database capacity after downsizing; differs as it involves a request queue rather than direct peak load.
- deepen DAN-096: `peak hour load ProxySQL connections exhaustion failover remediation` — Matches peak-hour database overload and dependent service failovers; differs as it centers on ProxySQL connection limits rather than instance size reduction.
- deepen DAN-094: `load driven ProxySQL meltdown LimitNOFILE fix remediation` — Matches load-driven database cluster meltdowns; differs as root cause is OS file descriptor cap, not capacity reduction.
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.597: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.571: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.711: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.708: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (cause) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (fix) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (fix) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev
  - DAN-094 (llm) [2020, February 25 16:36 UTC (lasting for two hours 12 minutes)] 0.715: ## 2020, February 25 16:36 UTC (lasting for two hours 12 minutes)  In this third incident involving ProxySQL, active database connections crossed a critical threshold that changed the behavior of this
  - DAN-094 (llm) [2020, February 20 21:31 UTC (lasting for 47 minutes)] 0.638: ## 2020, February 20 21:31 UTC (lasting for 47 minutes)  Two days later, as part of a planned master database promotion, we saw unexpectedly high load which triggered a similar ProxySQL failure. The i
  - DAN-094 (cause) [Background] 0.437: ## Background  Originally, all our MySQL data lived in a single database cluster. Over time, as mysql1 grew larger and busier, we split functionally grouped sets of tables into new clusters and create
  - DAN-094 (fix) [Next steps] 0.365: ## Next steps  ## Immediate changes: Data partitioning  We shipped a sizable chunk of data partitioning efforts we’ve worked on for the past six months just days after these incidents for one of our m
  - DAN-094 (fix) [In summary] 0.481: ## In summary  We know you depend on our platform to be reliable. With the immediate changes we’ve made and long-term plans in progress, we’ll continue to use what we’ve learned to make GitHub better 

## q-243 (expected: DAN-154)

- initial search: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210, DAN-103, DAN-209, DAN-205, DAN-129, DAN-109
- final note: 
- deepen DAN-011: `bot detection database permission file size limit network propagation systemwide outage fix rollback` — Cloudflare CDN systemwide outage matches the worldwide CDN down symptom; both involve a recent change breaking the network, unlike the other incidents.
- deepen DAN-008: `Tiered Cache change 530 errors rollback fix test blind spot` — Cloudflare cache change causing servers to return errors matches the error symptom, but the impact was only partial (~5% of requests), not worldwide.
- deepen DAN-067: `control plane analytics outage data center power failure remediation fix` — Cloudflare control plane outage matches a CDN control plane failure, but the trigger was a data center power failure rather than a software change.
  - DAN-011 (llm) [Remediation and follow-up steps] 0.643: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [no section] 0.61: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (cause) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (fix) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (fix) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-008 (llm) [no section] 0.737: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.685: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (cause) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (fix) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (fix) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-067 (llm) [Lessons and Remediation] 0.761: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.729: ### Flexential Data Center Power Failure  The largest of the three facilities in Oregon is run by Flexential. We refer to this facility as “PDX-DC04”. Cloudflare leases space in PDX-04 where we house 
  - DAN-067 (cause) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (fix) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (fix) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-242 (expected: DAN-154)

- initial search: DAN-011, DAN-103, DAN-109, DAN-026, DAN-129, DAN-145, DAN-106, DAN-009, DAN-073, DAN-008
- final note: 
- deepen DAN-011: `database permissions file output exceeded limits systemwide outage root cause fix rollback` — matches a worldwide systemwide Cloudflare/CDN-style outage; differs in trigger (database permissions and oversized file rather than CDN config).
- deepen DAN-009: `service tokens code release CDN control plane outage fix rollback` — explicitly involves CDN control plane degradation and service errors; differs in trigger (code release for service tokens).
- deepen DAN-008: `Tiered Cache change 530 errors root cause fix rollback` — involves CDN Tiered Cache causing request errors; differs in scope (partial, ~5% of requests, not worldwide).
  - DAN-011 (llm) [The query behaviour change] 0.56: ### The query behaviour change  ``` SELECT   name,   type FROM system.columns WHERE   table = 'http_requests_features' order by name; ``` Note how the query does not filter for the database name. With
  - DAN-011 (llm) [no section] 0.553: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (cause) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (fix) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (fix) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-009 (llm) [no section] 0.677: Several Cloudflare services became unavailable for 121 minutes on January 24, 2023 due to an error releasing code that manages service tokens. The incident degraded a wide range of Cloudflare products
  - DAN-009 (llm) [Incident Timeline] 0.664: ### Incident Timeline  *All Timestamps are UTC*  At 2023-01-24 16:55 the Access engineering team initiated the release that inadvertently began to overwrite service token metadata, causing the inciden
  - DAN-009 (cause) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (fix) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (fix) [How did we fix the issue?] 0.483: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-008 (llm) [no section] 0.768: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.703: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (cause) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (fix) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (fix) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
