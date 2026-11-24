# Research RAG agent (with LLM)

| q | expected | position in search | in initial search | deepened | tools called | found by new query | in findings | new queries | s |
|---|---|---|---|---|---|---|---|---|---|
| q-022 | DAN-104 | 4 | yes | yes | search | no | yes | 0 | 11 |
| q-170 | DAN-018 | 4 | yes | yes | search | no | yes | 0 | 6 |
| q-171 | DAN-018 | 4 | yes | yes | search | no | yes | 0 | 22 |
| q-222 | DAN-121 | 4 | yes | yes | search | no | yes | 0 | 9 |
| q-012 | DAN-211 | 5 | yes | yes | search | no | yes | 0 | 7 |
| q-263 | DAN-200 | 5 | yes | yes | search | no | yes | 0 | 7 |
| q-032 | DAN-104 | 7 | no | no | search | no | no | 0 | 16 |
| q-223 | DAN-121 | 8 | yes | yes | search | no | yes | 0 | 9 |
| q-229 | DAN-125 | 10 | yes | yes | search | no | yes | 0 | 15 |
| q-262 | DAN-200 | 10 | no | no | search | no | no | 0 | 8 |
| q-228 | DAN-125 | 11 | no | no | search | no | no | 0 | 25 |
| q-243 | DAN-154 | 12 | no | no | search | no | no | 0 | 19 |
| q-242 | DAN-154 | — | no | no | search | no | no | 0 | 7 |

## q-022 (expected: DAN-104)

- initial search: DAN-189, DAN-191, DAN-146, DAN-104, DAN-109, DAN-064, DAN-073, DAN-209, DAN-067, DAN-103
- final note: 
- deepen DAN-104: `command remove servers typo larger set removed S3 outage fix` — Matches: operator command meant to remove a few servers removed a larger set and took down storage (S3) plus dependents; differs: it was a typo rather than a removal command going wrong.
- deepen DAN-189: `operator reboot few servers rebooted all datacenter missing flag fix` — Matches: operator meant to affect a few servers but the command hit all servers in the datacenter; differs: reboot instead of removal, and it hit compute/PXE boot rather than storage.
- deepen DAN-146: `OS upgrade machines wiped out databases outage fix` — Partial match: maintenance wiped out machines and took out dependent databases; differs: trigger is an OS upgrade, not a removal command, and the postmortem is thin.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.671: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.66: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (cause) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (fix) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (fix) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.619: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [What Happened?] 0.597: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (cause) [Next Steps] 0.434: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (fix) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (fix) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-146 (llm) [no section] 0.684: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [no section] 0.565: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri

## q-170 (expected: DAN-018)

- initial search: DAN-144, DAN-066, DAN-018, DAN-029, DAN-067, DAN-133, DAN-129, DAN-182, DAN-220, DAN-218
- final note: 
- deepen DAN-018: `React component bug dashboard excessive API calls Tenant Service dependency array root cause fix` — DAN-018 matches the current incident closely: a dashboard/frontend change caused a flood of calls to an internal service, overwhelming the API and dashboard. It differs in that the summary mentions a React dependency array bug specifically, whereas the current incident describes a frontend deploy more generally.
  - DAN-018 (llm) [What Happened] 0.776: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.696: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (cause) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (fix) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (fix) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T

## q-171 (expected: DAN-018)

- initial search: DAN-066, DAN-029, DAN-144, DAN-018, DAN-067, DAN-133, DAN-218, DAN-129, DAN-155, DAN-145
- final note: 
- deepen DAN-018: `React component dashboard excessive API calls Tenant Service dependency array fix` — Closest match: a frontend/dashboard deploy caused the dashboard to flood an internal service with API calls, cascading into API and dashboard outage—same pattern as the current incident; differs only in the specific internal service name.
  - DAN-018 (llm) [What Happened] 0.745: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.678: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (cause) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (fix) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (fix) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T

## q-222 (expected: DAN-121)

- initial search: DAN-147, DAN-164, DAN-129, DAN-016, DAN-186, DAN-101, DAN-148, DAN-134, DAN-094, DAN-121
- final note: 
- deepen DAN-121: `database overloaded throttle requests timeout fix mitigation` — Closest match: database backend overloaded, throttled requests from services, iPlayer video service timed out — mirrors current incident closely
- deepen DAN-147: `cascading failure request queue database capacity overload fix` — Strong match: request queue overloaded insufficient database capacity causing cascading failure; differs in lacking explicit rate limiting and video player impact
- deepen DAN-164: `influx requests overload database replication lag fix` — Good match: influx of requests overloaded database; differs in having data loss from wrong directory deletion not present in current incident
  - DAN-121 (llm) [no section] 0.472: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [no section] 0.455: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (cause) [no section] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.613: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.601: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Timeline] 0.693: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.664: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (cause) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (fix) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (fix) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-012 (expected: DAN-211)

- initial search: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-066, DAN-101, DAN-222, DAN-113, DAN-144
- final note: 
- deepen DAN-020: `bad service discovery config dependent client global outage root cause fix rollback` — Matches current incident: service discovery layer impacted globally due to a dependent client issue, causing cascading failures to other services.
- deepen DAN-211: `Consul streaming BoltDB service discovery health check load degradation root cause fix` — Matches current incident: Consul is a service discovery tool; passage mentions service discovery and health check load degrading, similar to slow service discovery with write timeouts.
- deepen DAN-109: `network disruption metadata service response time timeout storage node retry cascading failure fix` — Partially matches: involves timeouts exceeding thresholds and cascading retries causing load, but not specifically service discovery layer.
  - DAN-020 (llm) [The failure of a core system] 0.685: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.667: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (cause) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (fix) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (fix) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-211 (llm) [Return to Service Attempt #1 (10/29 02:00 – 04:00)] 0.696: ### Return to Service Attempt #1 (10/29 02:00 – 04:00)  The reset went smoothly, and initially, the metrics looked good. When we removed the iptables block, the service discovery and health check load
  - DAN-211 (llm) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.676: ### Early Triage (10/28 13:37 – 10/29 02:00)  The initial investigation suggested that the Consul cluster that Vault and many other services depend on was unhealthy.  Specifically, the Consul cluster 
  - DAN-211 (cause) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (fix) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (fix) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.643: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.634: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (cause) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (fix) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (fix) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-263 (expected: DAN-200)

- initial search: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-073, DAN-146, DAN-106, DAN-069, DAN-066
- final note: 
- deepen DAN-200: `Mars Pathfinder system resets priority inversion VxWorks root cause fix priority inheritance patch` — The current incident describes an onboard computer resetting itself a few days after going into operation, which closely matches Mars Pathfinder's system resets a few days after landing; both involve an onboard spacecraft computer and remote software patching.
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.662: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [THE FAILURE] 0.655: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (cause) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (fix) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (fix) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac

## q-032 (expected: DAN-104)

- initial search: DAN-189, DAN-109, DAN-067, DAN-064, DAN-191, DAN-210, DAN-146, DAN-073, DAN-070, DAN-209
- final note: 
- deepen DAN-189: `operator reboot all servers lax input validation manual intervention fix` — Matches an operator routine command affecting far more servers than intended and requiring manual recovery; differs because it rebooted rather than removed servers and was not specifically a storage service.
- deepen DAN-073: `storage volume failure storage server outage recovery fix` — Matches a storage service going down because of a storage server problem; differs because the trigger was a volume failure, not an operator command to remove servers.
- deepen DAN-191: `3PAR controller failure storage system not recovering process fix` — Matches a storage system outage that did not recover after a maintenance action; differs because the trigger was hardware replacement, not an operator command to remove servers.
  - DAN-189 (llm) [What Happened?] 0.621: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.594: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (cause) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (fix) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (fix) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-073 (llm) [18:23¶] 0.715: #### 18:23¶  At this time, livefile1 had the new volumes attached, and we were logged in and checking everything out. The server needed to do a full filesystem check before the storage was available, 
  - DAN-073 (llm) [Speeding up recovery¶] 0.702: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (cause) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (fix) [Next steps¶] 0.303: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (fix) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi
  - DAN-191 (llm) [no section] 0.629: On the 17th October 2016 one of the four controllers within the principal HP storage system located in the Strand Data Centre failed. There was no user impact. HP hardware engineers then arrived on si
  - DAN-191 (llm) [no section] 0.599: Controllers                                                                                       4. Legacy workload (eg., oracle database, Solaris hosts,    4                      for adaptive       
  - DAN-191 (cause) [no section] 0.483: IT INFRASTRUCTURE RESILIENCY REVIEW  23 February 2017  Introduction  Objective of the review:                                      Structure of the report:  This report presents the findings of the IT
  - DAN-191 (fix) [no section] 0.456: The incident timeline presented overleaf is a high level  depiction of the incident from the start on Monday 17th Oct until  the BCP Silver team handed over the recovery and restoration  work to the r
  - DAN-191 (fix) [no section] 0.446: It was later established, in an assessment of the incident by HP, that the inability of the storage system to return to service after the defective hardware was replaced was due to a flaw in the firmw

## q-223 (expected: DAN-121)

- initial search: DAN-147, DAN-148, DAN-219, DAN-164, DAN-121, DAN-101, DAN-134, DAN-129, DAN-220, DAN-144
- final note: 
- deepen DAN-121: `database overloaded throttle requests services timing out video player root cause fix` — Closest match: database backend overloaded, throttling requests, services including iPlayer timing out — same pattern as current incident
- deepen DAN-147: `request queue overloading database capacity cascading failure root cause fix` — Strong match: cascading failure from request queue overloading insufficient database capacity — same core mechanism
- deepen DAN-164: `influx of requests overloaded database replication lag root cause fix` — Relevant: influx of requests overloaded the database — similar trigger but includes admin error which differs from current incident
  - DAN-121 (llm) [no section] 0.556: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [no section] 0.515: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (cause) [no section] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.598: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.584: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Root cause analysis] 0.715: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.678: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (cause) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (fix) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (fix) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-229 (expected: DAN-125)

- initial search: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-181, DAN-043, DAN-125
- final note: 
- deepen DAN-125: `database downgrade insufficient capacity peak cascading collapse dependent servers fix` — Matches the downsizing trigger, peak-time overload, and cascading collapse of dependent servers exactly.
- deepen DAN-147: `cascading failure insufficient database capacity request queue root cause fix` — Matches cascading failure from insufficient database capacity, but lacks explicit downsizing trigger.
  - DAN-125 (llm) [Database performance issues] 0.627: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.558: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (cause) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (fix) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (fix) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.632: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.593: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-262 (expected: DAN-200)

- initial search: DAN-198, DAN-103, DAN-189, DAN-191, DAN-073, DAN-146, DAN-066, DAN-102, DAN-230, DAN-210
- final note: 
- deepen DAN-198: `rendezvous radar CPU load computer restart cause fix` — Apollo 11 computer restarted due to excess CPU load from a design flaw — matches the restart symptom, though the trigger differs (landing vs days after operation).
- deepen DAN-191: `firmware flaw hardware controller restart fix outage` — 3PAR storage controllers failed due to a firmware flaw — involves onboard hardware controllers, but not spontaneous restarts days after operation.
- deepen DAN-102: `database restart deadlock PGAudit fix` — Postgres was restarted to break a deadlock — involves a restart as fix, but the cause is a lock bug, not a time-delayed onboard computer restart.
  - DAN-198 (llm) [no section] 0.59: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [no section] 0.57: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (cause) [no section] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (fix) [no section] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (fix) [no section] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,
  - DAN-191 (llm) [no section] 0.656: It was later established, in an assessment of the incident by HP, that the inability of the storage system to return to service after the defective hardware was replaced was due to a flaw in the firmw
  - DAN-191 (llm) [no section] 0.487: On the 17th October 2016 one of the four controllers within the principal HP storage system located in the Strand Data Centre failed. There was no user impact. HP hardware engineers then arrived on si
  - DAN-191 (cause) [no section] 0.483: IT INFRASTRUCTURE RESILIENCY REVIEW  23 February 2017  Introduction  Objective of the review:                                      Structure of the report:  This report presents the findings of the IT
  - DAN-191 (fix) [no section] 0.456: The incident timeline presented overleaf is a high level  depiction of the incident from the start on Monday 17th Oct until  the BCP Silver team handed over the recovery and restoration  work to the r
  - DAN-191 (fix) [no section] 0.388: Is there a strategic roadmap to     No – there are a number of solutions currently being considered to eliminate   ensure that the College gets the      the need for the Strand Data Centre which is no
  - DAN-102 (llm) [no section] 0.647: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [no section] 0.606: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily

## q-228 (expected: DAN-125)

- initial search: DAN-147, DAN-164, DAN-156, DAN-096, DAN-094, DAN-130, DAN-194, DAN-181, DAN-091, DAN-134
- final note: 
- deepen DAN-147: `cascading failure database capacity insufficient peak load root cause fix` — Matches cascading failure and insufficient database capacity; current incident also mentions database size recently reduced
- deepen DAN-091: `peak load database queued operations cascading failure root cause fix` — Matches peak hour database overload and cascading queue effects; current incident has peak hours and cascading server failures
- deepen DAN-164: `database overloaded influx requests replication lag root cause fix` — Matches database overload under influx of requests; differs because it includes admin error deleting wrong directory
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.621: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.547: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (cause) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (fix) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (fix) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-091 (llm) [Postmortem] 0.662: ## Postmortem  We identified a couple of changes that required additional work but had performed well in evaluation and rolled them back. Unfortunately, by that time the queued DB operations were back
  - DAN-091 (llm) [Postmortem] 0.636: ## Postmortem  THURSDAY 09:00 UTC: We worked to bring up excess capacity to handle the backlog and push builds in as fast as we could. Then we learned that the throttles we had built into our build sc
  - DAN-091 (cause) [Postmortem] 0.464: ## Postmortem  We've also moved over 50 percent of the data that was in our primary database onto its own deployment. The data was orthogonal and didn't need to be co-located, but its heavy use was ca
  - DAN-091 (fix) [Resolved] 0.326: ## Resolved  We’re continuing to see builds running normally. We will be monitoring closely throughout the day. Please contact us in support if you’re seeing issues with your builds.  Posted Oct 15, 2
  - DAN-091 (fix) [Postmortem] 0.423: ## Postmortem  Getting back to the architecture, we've known for a while that our queue model needs to be rebuilt and we've been laying the foundation to get there with the items outlined above, but w
  - DAN-164 (llm) [Root cause analysis] 0.711: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.688: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (cause) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (fix) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (fix) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-243 (expected: DAN-154)

- initial search: DAN-011, DAN-008, DAN-026, DAN-067, DAN-205, DAN-209, DAN-109, DAN-129, DAN-145, DAN-210
- final note: 
- deepen DAN-011: `bot detection database permission file limit network propagation outage fix` — Matches worldwide CDN outage and systemwide propagation, but differs in root cause being bot-detection database permissions rather than general CDN config.
- deepen DAN-008: `Tiered Cache change 530 error test blind spot fix rollback` — Matches Cloudflare CDN cache change causing server errors, but differs as it was partial (5% requests) not worldwide.
- deepen DAN-067: `Flexential data center power failure control plane analytics outage remediation` — Matches Cloudflare control plane outage with broad impact, but differs as cause was data center power failure, not a CDN software change.
  - DAN-011 (llm) [Remediation and follow-up steps] 0.65: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [no section] 0.603: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (cause) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (fix) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (fix) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-008 (llm) [no section] 0.734: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.685: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (cause) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (fix) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (fix) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.758: ### Flexential Data Center Power Failure  The largest of the three facilities in Oregon is run by Flexential. We refer to this facility as “PDX-DC04”. Cloudflare leases space in PDX-04 where we house 
  - DAN-067 (llm) [Lessons and Remediation] 0.745: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (cause) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (fix) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (fix) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-242 (expected: DAN-154)

- initial search: DAN-011, DAN-067, DAN-008, DAN-026, DAN-109, DAN-145, DAN-129, DAN-210, DAN-066, DAN-205
- final note: 
- deepen DAN-011: `root cause database permissions bot detection file exceeded limits systemwide outage fix rollback` — Cloudflare is a CDN; this was a systemwide/global outage matching the current incident's sudden global CDN failure, though the trigger was a database permission change rather than a CDN-specific component.
- deepen DAN-008: `Tiered Cache change 530 error root cause fix rollback blind spot tests` — Cloudflare Tiered Cache is a CDN component causing request failures, but the outage was partial (5% of requests, six hours) not global like the current incident.
- deepen DAN-066: `Byzantine failure switch misbehavior cascading root cause fix API dashboard availability` — Cloudflare cascading failure impacted API/dashboard availability, but it was partial (six hours) and triggered by switch misbehavior rather than a global CDN down event.
  - DAN-011 (llm) [Remediation and follow-up steps] 0.605: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [Remediation and follow-up steps] 0.567: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-011 (cause) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (fix) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (fix) [How Cloudflare processes requests, and how this went wrong today] 0.393: ## How Cloudflare processes requests, and how this went wrong today  This feature file is refreshed every few minutes and published to our entire network and allows us to react to variations in traffi
  - DAN-008 (llm) [no section] 0.737: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.68: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (cause) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (fix) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (fix) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-066 (llm) [The Dashboard] 0.628: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.605: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (cause) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (fix) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.463: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (fix) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
