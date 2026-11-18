# Agente Pesquisa RAG nas perguntas da E3 (sem LLM)

| q | esperado | na busca inicial | aprofundado | descartado | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|
| q01 | DAN-164 | sim | sim | não | sim | 0 | 15 |
| q02 | DAN-104 | sim | sim | não | sim | 0 | 0 |
| q03 | DAN-090 | sim | sim | não | sim | 0 | 0 |
| q04 | DAN-071 | sim | sim | não | sim | 0 | 0 |
| q05 | DAN-084 | sim | sim | não | sim | 0 | 0 |
| q06 | DAN-236 | sim | sim | não | sim | 0 | 0 |
| q07 | DAN-088, DAN-089 | sim | sim | não | sim | 0 | 0 |
| q08 | DAN-145 | sim | sim | não | sim | 0 | 0 |
| q09 | DAN-122 | sim | sim | não | sim | 0 | 0 |
| q10 | DAN-017 | sim | sim | não | sim | 0 | 0 |
| q11 | DAN-086, DAN-090 | sim | sim | não | sim | 0 | 0 |
| q12 | (nenhum) | — | — | não | — | 0 | 0 |

## q01 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-043, DAN-220, DAN-186, DAN-209
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-164: `what was the root cause and how was the problem fixed`
- aprofundar DAN-043: `what was the root cause and how was the problem fixed`
- aprofundar DAN-220: `what was the root cause and how was the problem fixed`
  - DAN-164 (llm) [Root cause analysis] 0.614: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Improving recovery procedures] 0.461: ## Improving recovery procedures  If you think there are additional measures we can take to prevent incidents like this please let us know in the comments.
  - DAN-043 (llm) [Some perspective] 0.449: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (llm) [sem seção] 0.427: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-220 (llm) [Remediations in place after the second incident] 0.542: ## Remediations in place after the second incident  After the outage (infamously known as OPS-6000 in our incident tracking system), we held a post-mortem meeting where we invited the entire Technolog
  - DAN-220 (llm) [Lessons learned] 0.523: ## Lessons learned  - We should have prioritized fixing the backoff bug in the client after the first Popcount incident, we did not assign the right severity. We thought having the fast fail mechanism

## q02 (esperado: DAN-104)

- busca inicial: DAN-104, DAN-105, DAN-230, DAN-064, DAN-073
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-104: `what was the root cause and how was the problem fixed`
- aprofundar DAN-105: `what was the root cause and how was the problem fixed`
- aprofundar DAN-230: `what was the root cause and how was the problem fixed`
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.355: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.308: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-105 (llm) [sem seção] 0.458: We've now determined that message corruption was the cause of the server-to-server communication problems. More specifically, we found that there were a handful of messages on Sunday morning that had 
  - DAN-105 (llm) [sem seção] 0.407: We wanted to provide some additional detail about the problem we experienced on Sunday, July 20th.  At 8:40am PDT, error rates in all Amazon S3 datacenters began to quickly climb and our alarms went o
  - DAN-230 (llm) [Lessons learned] 0.46: ## Lessons learned  1\. I am apparently able to sleep through my phone ringing, at least once. I had assumed this couldn't happen, so I set the Tarsnap monitoring system to phone once an hour since I 
  - DAN-230 (llm) [Final words] 0.437: ## Final words  While the ultimate precipitating factor seems to have be an as yet still undiagnosed change in Amazon S3 behaviour, the majority of the fault here lies in Tarsnap: Inappropriate handli

## q03 (esperado: DAN-090)

- busca inicial: DAN-090, DAN-025, DAN-216, DAN-136, DAN-023
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-090: `what was the root cause and how was the problem fixed`
- aprofundar DAN-025: `what was the root cause and how was the problem fixed`
- aprofundar DAN-216: `what was the root cause and how was the problem fixed`
  - DAN-090 (llm) [Root Cause Analysis] 0.54: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.5: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-025 (llm) [The Infinite Loop] 0.492: ## The Infinite Loop  With the load balancer change in place, and a special code path in a new Rust service now active, the necessary final ingredient to trigger the problem for users was deep in Neck
  - DAN-025 (llm) [Lessons Learned] 0.486: ## Lessons Learned  As so often is the case, the issue was a lot more complex than it appeared at first glance and there were many contributing factors working together. Some of the key factors we hav
  - DAN-216 (llm) [Post-mortem: Outages on 1/19/17 and 1/23/17] 0.504: ## Post-mortem: Outages on 1/19/17 and 1/23/17  Analysis of the heap dump identified an unbounded, non-evicting, strongly-referencing cache (clojure.core/memoize) in a third-party library (Amazonica) 
  - DAN-216 (llm) [Post-mortem: Outages on 1/19/17 and 1/23/17] 0.501: ## Post-mortem: Outages on 1/19/17 and 1/23/17  Coda Hale  Follow  Jan 27, 2017  ·  3  min read  Skyliner was unavailable from 00:59 to 01:26 PST on January 19th and from 12:49 PST to 12:56 PST on Jan

## q04 (esperado: DAN-071)

- busca inicial: DAN-067, DAN-068, DAN-071, DAN-231, DAN-048
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-067: `what was the root cause and how was the problem fixed`
- aprofundar DAN-068: `what was the root cause and how was the problem fixed`
- aprofundar DAN-071: `what was the root cause and how was the problem fixed`
  - DAN-067 (llm) [Lessons and Remediation] 0.536: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Attempting to Restore Power] 0.453: ### Attempting to Restore Power  While we haven't gotten official confirmation, we have been told by employees that three things hampered getting the generators back online. First, they needed to be p
  - DAN-068 (llm) [What happened to the power in the data center?] 0.483: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [How did we get here?] 0.449: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.399: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.386: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog

## q05 (esperado: DAN-084)

- busca inicial: DAN-084, DAN-050, DAN-106, DAN-017, DAN-042
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-084: `what was the root cause and how was the problem fixed`
- aprofundar DAN-050: `what was the root cause and how was the problem fixed`
- aprofundar DAN-106: `what was the root cause and how was the problem fixed`
  - DAN-084 (llm) [45 Minutes of Hell] 0.497: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (llm) [What Could Possibly Go Wrong? Indeed!] 0.422: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-050 (llm) [Root cause identification: The Five Whys] 0.528: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (llm) [Recovery] 0.523: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.426: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.399: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro

## q06 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-059, DAN-154, DAN-226, DAN-216
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-236: `what was the root cause and how was the problem fixed`
- aprofundar DAN-059: `what was the root cause and how was the problem fixed`
- aprofundar DAN-154: `what was the root cause and how was the problem fixed`
  - DAN-236 (llm) [kisak-valve commentedon Apr 30, 2021] 0.386: ## kisak-valve commentedon Apr 30, 2021  Hello @nicklleite, the investigation of the issue in this issue report concluded several years ago. Please open a new issue report.
  - DAN-236 (llm) [Activity] 0.336: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.42: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [A (Nearly) Global Outage] 0.339: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-154 (llm) [**Where do we go from here?**] 0.486: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (llm) [**What happened?**] 0.477: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust

## q07 (esperado: DAN-088, DAN-089)

- busca inicial: DAN-088, DAN-103, DAN-087, DAN-089, DAN-129
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-088: `what was the root cause and how was the problem fixed`
- aprofundar DAN-103: `what was the root cause and how was the problem fixed`
- aprofundar DAN-087: `what was the root cause and how was the problem fixed`
  - DAN-088 (llm) [sem seção] 0.395: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.389: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-103 (llm) [What happened? #] 0.552: ## What happened? #  On 23rd October, at 4:19 AM a wrong server was restarted by mistake. In fact, it was the wrong “half” of a blade server running in the active datacentre and hosting important comp
  - DAN-103 (llm) [How did we respond? #] 0.539: ## How did we respond? #  The third thing we needed to do, was finding the cause of this enormous number of tasks. For reasons which we still do not understand, after rebooting, daemons started to ret
  - DAN-087 (llm) [sem seção] 0.48: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (llm) [Timeline] 0.471: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is

## q08 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-145: `what was the root cause and how was the problem fixed`
- aprofundar DAN-234: `what was the root cause and how was the problem fixed`
- aprofundar DAN-066: `what was the root cause and how was the problem fixed`
  - DAN-145 (llm) [Update] 0.493: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-145 (llm) [Investigation and Analysis] 0.475: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-234 (llm) [What We’re Doing About It] 0.558: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.555: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-066 (llm) [Redundant Points of Failure] 0.512: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.484: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se

## q09 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-157, DAN-177, DAN-136
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-122: `what was the root cause and how was the problem fixed`
- aprofundar DAN-152: `what was the root cause and how was the problem fixed`
- aprofundar DAN-157: `what was the root cause and how was the problem fixed`
  - DAN-122 (llm) [Remediation] 0.382: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.356: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-152 (llm) [Timeline] 0.393: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Attack Method] 0.306: ## Attack Method  Further details on the attack can be found here.
  - DAN-157 (llm) [What went badly] 0.438: ### What went badly  - Initial communications were unclear and lacking detail in two areas.   - How can users verify their tree to be sure they had a clean copy?   - Clearer guidelines that even if us
  - DAN-157 (llm) [Lessons] 0.421: ## Lessons  ### What went well  - Gentoo responded quickly to reports of problems. - GitHub responded quickly and had a function to hide the impacted organization. - Gentoo quickly removed account acc

## q10 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-066, DAN-008, DAN-067
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-017: `what was the root cause and how was the problem fixed`
- aprofundar DAN-220: `what was the root cause and how was the problem fixed`
- aprofundar DAN-066: `what was the root cause and how was the problem fixed`
  - DAN-017 (llm) [Resolution] 0.501: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (llm) [Timeline] 0.458: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-220 (llm) [Remediations in place after the second incident] 0.542: ## Remediations in place after the second incident  After the outage (infamously known as OPS-6000 in our incident tracking system), we held a post-mortem meeting where we invited the entire Technolog
  - DAN-220 (llm) [Lessons learned] 0.523: ## Lessons learned  - We should have prioritized fixing the backoff bug in the client after the first Popcount incident, we did not assign the right severity. We thought having the fast fail mechanism
  - DAN-066 (llm) [Redundant Points of Failure] 0.512: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.484: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se

## q11 (esperado: DAN-086, DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-198, DAN-191, DAN-221
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-086: `what was the root cause and how was the problem fixed`
- aprofundar DAN-090: `what was the root cause and how was the problem fixed`
- aprofundar DAN-198: `what was the root cause and how was the problem fixed`
  - DAN-086 (llm) [Prevention] 0.511: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (llm) [Introduction] 0.458: ## Introduction  As a follow-up to my March 1 posting, I want to share the findings of our root cause analysis of the service disruption of February 29th. We know that many of our customers were impac
  - DAN-090 (llm) [Root Cause Analysis] 0.54: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.5: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-198 (llm) [sem seção] 0.494: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.426: | Many explanations have been offered for why the RR was configured in this way for the lunar landing. For example, a fanciful scheme for monitoring the landing by comparing RR data to a chart of expe

## q12 (esperado: nenhum)

- busca inicial: DAN-066, DAN-134, DAN-155, DAN-009, DAN-216
- justificativa: modo --sem-llm: plano fixo
- aprofundar DAN-066: `what was the root cause and how was the problem fixed`
- aprofundar DAN-134: `what was the root cause and how was the problem fixed`
- aprofundar DAN-155: `what was the root cause and how was the problem fixed`
  - DAN-066 (llm) [Redundant Points of Failure] 0.512: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.484: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-134 (llm) [What Happened] 0.503: ## What Happened  At 16:25, engineers determined that the queues which account for destroying old VMs had no consumers. In an effort to re-establish connectivity to the queues we reset the VM services
  - DAN-134 (llm) [What Happened] 0.492: ## What Happened  The system had become “wedged” and we had found ourselves in a vicious cycle of creating VMs and then not being able to remove them due to hitting our GCP quotas. In order to break o
  - DAN-155 (llm) [sem seção] 0.452: 1. Flowdock went down and was restarted (April 21, ~13:30 UTC)        ●  The application database was hung due to high CPU usage caused by a sudden               surge in user activities from multiple
  - DAN-155 (llm) [sem seção] 0.418: Impact Analysis   ●  The application was unavailable for its users for ~22 hrs   ●  The fact that only recently defined user ID’s were accidentally affected, suggests a very        limited exposure of
