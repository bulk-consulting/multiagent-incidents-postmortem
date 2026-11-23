# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q01 | DAN-164 | — | sim | sim | search | não | sim | 0 | 72 |
| q02 | DAN-104 | — | sim | sim | search | não | sim | 0 | 41 |
| q03 | DAN-090 | — | sim | sim | search | não | sim | 0 | 4 |
| q04 | DAN-071 | — | sim | sim | search | não | sim | 0 | 8 |
| q05 | DAN-084 | — | sim | sim | search | não | sim | 0 | 7 |
| q06 | DAN-236 | — | sim | sim | search | não | sim | 0 | 20 |
| q07 | DAN-088, DAN-089 | — | sim | sim | search | não | sim | 0 | 10 |
| q08 | DAN-145 | — | sim | sim | search | não | sim | 0 | 7 |
| q09 | DAN-122 | — | sim | sim | search | não | sim | 0 | 8 |
| q10 | DAN-017 | — | sim | sim | search | não | sim | 0 | 10 |
| q11 | DAN-086, DAN-090 | — | sim | não | (texto) | não | sim | 0 | 38 |
| q12 | (nenhum) | — | — | — | find → find | — | — | 4 | 8 |

## q01 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-043, DAN-220, DAN-186, DAN-209, DAN-048, DAN-195, DAN-056, DAN-058, DAN-026
- justificativa: 
- aprofundar DAN-164: `directory deletion data loss six hours` — Admin tired, deleted wrong directory, six hours data lost, matches current incident type and scale
- aprofundar DAN-043: `accidental database deletion backup` — Production database deleted by accident, 7 hours data lost, similar accidental deletion by admin
- aprofundar DAN-056: `environment variable database truncation` — Accidental env variable caused production database truncation, different trigger but similar data loss scenario
  - DAN-164 (llm) [sem seção] 0.529: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (llm) [Data loss impact] 0.516: ## Data loss impact  Database data such as projects, issues, snippets, etc. created between January 31st 17:20 UTC and 23:30 UTC has been lost. Git repositories and Wikis were not removed as they are 
  - DAN-164 (causa) [Root cause analysis] 0.567: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.731: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.677: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [What We Learned] 0.723: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.689: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q02 (esperado: DAN-104)

- busca inicial: DAN-104, DAN-105, DAN-230, DAN-064, DAN-073, DAN-125, DAN-106, DAN-164, DAN-060, DAN-048
- justificativa: 
- aprofundar DAN-104: `Amazon S3 2017 command typo remove servers root cause fix` — Comando com typo removeu mais servidores que o planejado e derrubou S3, mesma causa humana e componente S3, mas escala e playbook de recuperação diferem.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.667: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.608: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q03 (esperado: DAN-090)

- busca inicial: DAN-090, DAN-025, DAN-216, DAN-136, DAN-023, DAN-154, DAN-018, DAN-016, DAN-005, DAN-024
- justificativa: 
- aprofundar DAN-090: `certificate expiration Firefox add-on outage root cause fix` — Certificate expired caused add-ons to stop working, matching current incident; resolution involved pushing privileged add-on with valid certificate.
  - DAN-090 (llm) [Root Cause Analysis] 0.78: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.623: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q04 (esperado: DAN-071)

- busca inicial: DAN-067, DAN-068, DAN-071, DAN-231, DAN-048, DAN-209, DAN-064, DAN-191, DAN-062, DAN-070
- justificativa: 
- aprofundar DAN-071: `lightning strike power loss disk data loss` — Lightning strikes caused power loss to disks matching current incident
- aprofundar DAN-062: `severe weather power loss AWS Sydney disk` — Power loss due to severe weather affecting AWS region, similar external cause
- aprofundar DAN-067: `data center power failure cascading outage` — Power failure at data center provider, though cause differs
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.658: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.572: # Google Compute Engine Incident #15056  | |  | SUMMARY: From Thursday 13 August 2015 to Monday 17 August 2015, errors occurred on a small proportion of Google Compute Engine persistent disks in the e
  - DAN-071 (causa) [Google Compute Engine Incident #15056] 0.415: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.358: # Google Compute Engine Incident #15056  However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk. This outage is wholly Google's responsib
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.335: # Google Compute Engine Incident #15056  The service has been partially recovered. Meanwhile, affected customers can restore from snapshots as a workaround solution. We will provide another status upd
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.762: ### Summary of the AWS Service Event in the Sydney Region  We’d like to share more detail about the AWS service disruption that occurred this past weekend in the AWS Sydney Region. The service disrupt
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.754: ### Summary of the AWS Service Event in the Sydney Region  If utility power is interrupted, the DRUPS uses this stored energy to continue to provide power to the datacenter while the integrated genera
  - DAN-062 (causa) [Summary of the AWS Service Event in the Sydney Region] 0.399: ### Summary of the AWS Service Event in the Sydney Region  A latent bug in our instance management software led to a slower than expected recovery of the remaining instances. The team worked over the 
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.388: ### Summary of the AWS Service Event in the Sydney Region  Additionally, we will be taking actions to improve our recovery systems. The first is to fix the latent issue that led to our recovery system
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.359: ### Summary of the AWS Service Event in the Sydney Region  During the initial part of this event, customers experienced errors when trying to launch new instances, or when trying to scale their auto-s
  - DAN-067 (llm) [Lessons and Remediation] 0.689: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.687: ### Flexential Data Center Power Failure  The largest of the three facilities in Oregon is run by Flexential. We refer to this facility as “PDX-DC04”. Cloudflare leases space in PDX-04 where we house 
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q05 (esperado: DAN-084)

- busca inicial: DAN-084, DAN-050, DAN-106, DAN-017, DAN-042, DAN-154, DAN-207, DAN-116, DAN-125, DAN-191
- justificativa: 
- aprofundar DAN-084: `conflicting deployed versions bit reuse $460M loss cause correction` — Exact $460M loss from different deployed versions and reused bit, matches current incident's financial impact and root cause.
  - DAN-084 (llm) [45 Minutes of Hell] 0.515: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (llm) [What Could Possibly Go Wrong? Indeed!] 0.514: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-084 (causa) [sem seção] 0.424: I was speaking at a conference last year on the topics of DevOps, Configuration as Code, and Continuous Delivery and used the following story to demonstrate the importance making deployments fully aut
  - DAN-084 (correcao) [A Lesson to Learn] 0.316: ## A Lesson to Learn  The events of August 1, 2012 should be a lesson to all development and operations teams. It is not enough to build great software and test it; you also have to ensure it is deliv
  - DAN-084 (correcao) [Attack of the Killer Code Zombies] 0.361: ## Attack of the Killer Code Zombies  Its important to understand what the “dead” Power Peg code was meant to do. This functionality was meant to count the shares bought/sold against a parent order as

## q06 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-059, DAN-154, DAN-226, DAN-216, DAN-126, DAN-142, DAN-104, DAN-173, DAN-116
- justificativa: 
- aprofundar DAN-236: `steam client user file deletion bug fix` — Incidente atual descreve Steam apagando todos os arquivos do usuário; DAN-236 descreve exatamente o cliente Steam excluindo tudo do sistema do usuário, mesma causa provável.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.649: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (llm) [Activity] 0.649: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 

## q07 (esperado: DAN-088, DAN-089)

- busca inicial: DAN-088, DAN-103, DAN-087, DAN-089, DAN-129, DAN-209, DAN-116, DAN-205, DAN-146, DAN-154
- justificativa: 
- aprofundar DAN-088: `leap second deadlock xtime_lock printk` — Incidente trata de crash Linux na virada de leap second causado por deadlock no xtime_lock ao imprimir log, similar ao incidente atual de servidores Linux travando; porém envolve printk e klogd, não o mesmo mecanismo de rewind de clock.
- aprofundar DAN-089: `leap second CLOCK_REALTIME timer early expiry spinwait` — Incidente descreve rewind de CLOCK_REALTIME na virada de leap second causando temporizers expirados cedo e spinwait, levando a alta carga e quedas de serviço Linux, diretamente relacionado ao incidente atual de servidores travando na mesma circunstância.
  - DAN-088 (llm) [sem seção] 0.811: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.76: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.714: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.678: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti

## q08 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-164, DAN-078, DAN-217, DAN-096, DAN-221
- justificativa: 
- aprofundar DAN-145: `Redis primary migration cluster rebalance cascading fail` — Redis primary migration caused cluster rebalance and cascading user connection failures, matching current incident's Redis primary crash and cascade.
- aprofundar DAN-217: `Slack cascading disconnect reconnection database capacity` — Slack's cascading disconnection after database capacity exceeded parallels current user connection failures after Redis crash.
- aprofundar DAN-078: `MySQL master failover network partition latency` — Network partition causing failover provides insight into failover dynamics, though incident involves Redis not MySQL.
  - DAN-145 (llm) [Sequence of Events] 0.688: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Summary] 0.644: ## Summary  At approximately 14:01, a Redis instance acting as the primary for a highly-available cluster used by our API services was migrated automatically by Google’s Cloud Platform. This migration
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Action Items / Response] 0.404: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-217 (llm) [TUESDAY] 0.834: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [WEDNESDAY] 0.615: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou
  - DAN-078 (llm) [Incident timeline] 0.663: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.605: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa

## q09 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-157, DAN-177, DAN-136, DAN-142, DAN-124, DAN-215, DAN-233, DAN-203
- justificativa: 
- aprofundar DAN-122: `malicious packages JCenter impersonation attack` — Packages impersonating a legitimate developer in a public repository, similar to current incident; lived over a year and affected Android apps.
- aprofundar DAN-152: `compromised npm account malicious packages published` — Attacker compromised a maintainer's npm account and published malicious packages to the registry, matching the pattern of impersonation and malicious distribution.
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.792: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.659: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.762: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.736: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q10 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-066, DAN-008, DAN-067, DAN-050, DAN-020, DAN-042, DAN-129, DAN-102
- justificativa: 
- aprofundar DAN-017: `deployment staging build version 401 error routing traffic` — Deployment after release caused production to reference staging build, resulting in 401 errors, matching current incident's description of service central returning 401 for all requests after a deploy.
  - DAN-017 (llm) [Timeline] 0.575: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (llm) [Resolution] 0.559: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (causa) [Analysis] 0.422: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.

## q11 (esperado: DAN-086, DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-198, DAN-191, DAN-221, DAN-066, DAN-015, DAN-124, DAN-179, DAN-084
- justificativa: Encontrei 2 incidentes históricos envolvendo certificados: **DAN-086**, onde o código calculou erroneamente "um ano" como data atual mais 12 meses, gerando certificados com data de expiração 29/fev/2013 em 29/fev/2012 (ano bissexto), o que causou rejeição e uma interrupção global da Azure; e **DAN-090**, onde um certificado expirado em 04/mai/2019 quebrou a cadeia de certificados do Firefox, bloqueando ~15.000 add-ons e exigindo a implantação de um certificado válido por uma add-on privilegiado para restauração, com resolução em 15–21 horas e perda de alguns dados de usuário.

## q12 (esperado: nenhum)

- busca inicial: DAN-066, DAN-134, DAN-155, DAN-009, DAN-216, DAN-209, DAN-210, DAN-056, DAN-029, DAN-092
- justificativa: 
- novos incidentes nos achados: DAN-191, DAN-181, DAN-068, DAN-204, DAN-154, DAN-073, DAN-193, DAN-059, DAN-186, DAN-195
