# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q01 | DAN-164 | — | sim | sim | search | não | sim | 0 | 5 |
| q02 | DAN-104 | — | sim | sim | search | não | sim | 0 | 21 |
| q03 | DAN-090 | — | sim | sim | search | não | sim | 0 | 19 |
| q04 | DAN-071 | — | sim | sim | search | não | sim | 0 | 6 |
| q05 | DAN-084 | — | sim | sim | search | não | sim | 0 | 5 |
| q06 | DAN-236 | — | sim | sim | search | não | sim | 0 | 31 |
| q07 | DAN-088, DAN-089 | — | sim | sim | search | não | sim | 0 | 9 |
| q08 | DAN-145 | — | sim | sim | search | não | sim | 0 | 7 |
| q09 | DAN-122 | — | sim | sim | search | não | sim | 0 | 4 |
| q10 | DAN-017 | — | sim | sim | search | não | sim | 0 | 7 |
| q11 | DAN-086, DAN-090 | — | sim | sim | search | não | sim | 0 | 6 |
| q12 | (nenhum) | — | — | — | (texto) → find | — | — | 3 | 38 |

## q01 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-043, DAN-220, DAN-186, DAN-209, DAN-048, DAN-195, DAN-056, DAN-058, DAN-026
- justificativa: 
- aprofundar DAN-164: `directory deletion data loss cause recovery` — O incidente atual envolve administrador cansado apagando diretório errado e perda de seis horas de dados; o DAN-164 descreve exatamente esse cenário com admin cansado excluindo diretório errado e perda de seis horas.
  - DAN-164 (llm) [Root cause analysis] 0.548: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [sem seção] 0.542: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q02 (esperado: DAN-104)

- busca inicial: DAN-104, DAN-105, DAN-230, DAN-064, DAN-073, DAN-125, DAN-106, DAN-164, DAN-060, DAN-048
- justificativa: 
- aprofundar DAN-104: `S3 service disruption human error typo command remove servers root cause correction` — Comando com tipografia removeu servidores demais e derrubou S3, idêntico ao incidente atual em causa e efeito; diferente apenas em data e região.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.621: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.593: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q03 (esperado: DAN-090)

- busca inicial: DAN-090, DAN-025, DAN-216, DAN-136, DAN-023, DAN-154, DAN-018, DAN-016, DAN-005, DAN-024
- justificativa: 
- aprofundar DAN-090: `certificate expired Firefox add-ons outage fix` — Certificate expiry caused Firefox add-on outage matching current incident exactly; resolution involved injecting valid certificate via privileged add-on to restore chain.
  - DAN-090 (llm) [Root Cause Analysis] 0.723: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.668: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q04 (esperado: DAN-071)

- busca inicial: DAN-067, DAN-068, DAN-071, DAN-231, DAN-048, DAN-209, DAN-064, DAN-191, DAN-062, DAN-070
- justificativa: 
- aprofundar DAN-071: `lightning strike power loss disk data loss` — Lightning strikes caused power loss to disks and some permanent data loss, matching the current incident of lightning-caused power loss to disks.
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.658: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.572: # Google Compute Engine Incident #15056  | |  | SUMMARY: From Thursday 13 August 2015 to Monday 17 August 2015, errors occurred on a small proportion of Google Compute Engine persistent disks in the e
  - DAN-071 (causa) [Google Compute Engine Incident #15056] 0.415: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.358: # Google Compute Engine Incident #15056  However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk. This outage is wholly Google's responsib
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.335: # Google Compute Engine Incident #15056  The service has been partially recovered. Meanwhile, affected customers can restore from snapshots as a workaround solution. We will provide another status upd

## q05 (esperado: DAN-084)

- busca inicial: DAN-084, DAN-050, DAN-106, DAN-017, DAN-042, DAN-154, DAN-207, DAN-116, DAN-125, DAN-191
- justificativa: 
- aprofundar DAN-084: `conflicting deployed versions bit reuse cause fix` — Incidente atual envolve deploy com versões diferentes causando perda de $460M; DAN-084 descreve exatamente esse cenário com Knight Capital.
  - DAN-084 (llm) [What Could Possibly Go Wrong? Indeed!] 0.501: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-084 (llm) [45 Minutes of Hell] 0.465: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (causa) [sem seção] 0.424: I was speaking at a conference last year on the topics of DevOps, Configuration as Code, and Continuous Delivery and used the following story to demonstrate the importance making deployments fully aut
  - DAN-084 (correcao) [A Lesson to Learn] 0.316: ## A Lesson to Learn  The events of August 1, 2012 should be a lesson to all development and operations teams. It is not enough to build great software and test it; you also have to ensure it is deliv
  - DAN-084 (correcao) [Attack of the Killer Code Zombies] 0.361: ## Attack of the Killer Code Zombies  Its important to understand what the “dead” Power Peg code was meant to do. This functionality was meant to count the shares bought/sold against a parent order as

## q06 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-059, DAN-154, DAN-226, DAN-216, DAN-126, DAN-142, DAN-104, DAN-173, DAN-116
- justificativa: 
- aprofundar DAN-236: `steam desktop client file deletion cause fix` — Corresponde ao cliente Steam apagando todos os arquivos do usuário; mesma falha e componente. Diferenças apenas em detalhes de contexto ou versão.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.673: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (llm) [Activity] 0.656: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 

## q07 (esperado: DAN-088, DAN-089)

- busca inicial: DAN-088, DAN-103, DAN-087, DAN-089, DAN-129, DAN-209, DAN-116, DAN-205, DAN-146, DAN-154
- justificativa: 
- aprofundar DAN-088: `leap second deadlock xtime_lock printk klogd` — Linux leap second crash due to deadlock in timer interrupt handler, matches current incident of Linux servers crashing at leap second; differs in that klogd wakeup is involved.
- aprofundar DAN-089: `leap second futex hrtimer CLOCK_REALTIME rewound` — Linux timer rewind without hrtimer update causing spinwait and high load, matches Linux servers crash at leap second but different mechanism.
- aprofundar DAN-087: `leap second Cloudflare DNS Go time.Now monotonic` — Cloudflare DNS incident, not Linux servers; included for completeness but relevance low.
  - DAN-088 (llm) [sem seção] 0.802: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.76: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (causa) [sem seção] 0.328: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.82: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.734: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.8: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe
  - DAN-087 (llm) [sem seção] 0.758: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (causa) [Timeline] 0.373: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is
  - DAN-087 (correcao) [The one character fix] 0.332: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (correcao) [A little bit about Cloudflare DNS] 0.318: ### A little bit about Cloudflare DNS  Cloudflare customers use our DNS service to serve the authoritative answers for DNS queries for their domains. They need to tell us the IP address of their origi

## q08 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-164, DAN-078, DAN-217, DAN-096, DAN-221
- justificativa: 
- aprofundar DAN-145: `Redis primary failover cluster rebalance cascading failure` — Redis primary migration caused node to drop, forcing cluster rebalance and cascading user connection failures, matching current incident.
- aprofundar DAN-217: `Slack cascading connection failures disconnection reconnection database capacity` — Massive disconnection‑reconnection process exceeded database capacity causing cascading connection failures, similar downstream impact.
- aprofundar DAN-029: `bad config database cluster outage cascading failure` — Misconfiguration led to database cluster outage affecting API and dashboard, analogous to cascading effects after Redis failover.
  - DAN-145 (llm) [Sequence of Events] 0.679: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.646: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-217 (llm) [TUESDAY] 0.843: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [sem seção] 0.644: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [WEDNESDAY] 0.429: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou
  - DAN-029 (llm) [Incident timeline] 0.69: ## Incident timeline  So, how did all this go wrong?  All times in this section are in British Summer Time (UTC+1).  - 15:09: Our monitoring detects the total outage of our API and Dashboard; engineer
  - DAN-029 (llm) [The following weeks] 0.685: ## The following weeks  The day after the incident, the whole team sat down to discuss two issues:  - Why did our Pacemaker cluster fail to elect a new primary database node? - How do we move back to 
  - DAN-029 (causa) [Reproducing the failure] 0.515: ### Reproducing the failure  To be confident in a new cluster, we needed to understand why the existing one didn't promote a new primary, and make changes to fix that issue.  For the most part, we did
  - DAN-029 (correcao) [Wrapping up the incident] 0.496: ## Wrapping up the incident  With a plan in place, and the confidence that we'd understood and fixed the issue which stopped our cluster from failing over on 10 October, we were ready to go. Even with
  - DAN-029 (correcao) [What's next?] 0.486: ## What's next?  There's no getting away from the size of this incident.  We feel an immense duty to everyone who trusts GoCardless as their payments provider. We took some time to think through what 

## q09 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-157, DAN-177, DAN-136, DAN-142, DAN-124, DAN-215, DAN-233, DAN-203
- justificativa: 
- aprofundar DAN-122: `malicious Maven packages JCenter impersonation attack` — Similarity: malicious packages in public repo using impersonation; Difference: JCenter is a Maven repository, not npm, but same class of attack.
- aprofundar DAN-152: `malicious npm packages attacker compromised maintainer account` — Direct parallel: attacker compromised npm account and published malicious packages under known developer name; same scenario as current incident.
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.753: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [From a process and organizational perspective:] 0.628: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (causa) [Remediation] 0.279: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.729: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.723: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q10 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-066, DAN-008, DAN-067, DAN-050, DAN-020, DAN-042, DAN-129, DAN-102
- justificativa: 
- aprofundar DAN-017: `deployment staging build 401 unauthorized` — Deploy after release caused production to reference staging build, returning 401 errors, matches current incident's post-deploy 401 symptom.
- aprofundar DAN-042: `deploy config variables git push heroku` — Incorrect deployment process caused config variables not to be used, could result in auth failures; less direct 401 match but relevant deployment issue.
- aprofundar DAN-020: `service discovery config outage` — Bad service discovery config brought down discovery globally; different root cause but also post-deploy connectivity issue.
  - DAN-017 (llm) [Analysis] 0.5: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Analysis] 0.487: ### Analysis  Workers KV is a low-latency key-value store that allows users to store persistent data on Cloudflare's network, as close to the users as possible. This distributed key-value store is use
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-042 (llm) [It was such a nice morning] 0.825: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Did I mess up?] 0.798: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-020 (llm) [The failure of a core system] 0.743: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.724: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter

## q11 (esperado: DAN-086, DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-198, DAN-191, DAN-221, DAN-066, DAN-015, DAN-124, DAN-179, DAN-084
- justificativa: 
- aprofundar DAN-086: `certificate expiration leap year 2012` — Involves certificate creation bug due to leap year, causing outage, similar to certificate-related outage in current incident.
- aprofundar DAN-090: `certificate expired Firefox add-ons outage May 2019` — Certificate expiration led to add-on outage, directly related to certificate validity issues.
  - DAN-086 (llm) [The Leap Day Bug] 0.613: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.538: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.691: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.644: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q12 (esperado: nenhum)

- busca inicial: DAN-066, DAN-134, DAN-155, DAN-009, DAN-216, DAN-209, DAN-210, DAN-056, DAN-029, DAN-092
- justificativa: 
- novos incidentes nos achados: DAN-191, DAN-181, DAN-068, DAN-204, DAN-073
