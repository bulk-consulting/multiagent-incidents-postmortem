# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q01 | DAN-164 | — | sim | sim | search | não | sim | 0 | 19 |
| q02 | DAN-104 | — | sim | sim | search | não | sim | 0 | 9 |
| q03 | DAN-090 | — | sim | sim | search | não | sim | 0 | 10 |
| q04 | DAN-071 | — | sim | sim | search | não | sim | 0 | 17 |
| q05 | DAN-084 | — | sim | sim | search | não | sim | 0 | 11 |
| q06 | DAN-236 | — | sim | sim | search | não | sim | 0 | 5 |
| q07 | DAN-088, DAN-089 | — | sim | sim | search | não | sim | 0 | 9 |
| q08 | DAN-145 | — | sim | sim | search | não | sim | 0 | 13 |
| q09 | DAN-122 | — | sim | sim | search | não | sim | 0 | 6 |
| q10 | DAN-017 | — | sim | sim | search | não | sim | 0 | 12 |
| q11 | DAN-086, DAN-090 | — | sim | sim | search | não | sim | 0 | 8 |
| q12 | (nenhum) | — | — | — | find → (texto) | — | — | 2 | 9 |

## q01 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-043, DAN-220, DAN-186, DAN-209, DAN-048, DAN-195, DAN-056, DAN-058, DAN-026
- justificativa: 
- aprofundar DAN-164: `tired admin wrong directory deletion root cause fix recovery` — Bate exatamente: administrador cansado deletou o diretório errado e perdeu seis horas de dados.
- aprofundar DAN-043: `accidental production database deletion data loss recovery fix` — Semelhança: exclusão acidental em produção com perda de horas de dados, embora envolva banco de dados, não diretório.
- aprofundar DAN-056: `accidental environment variable truncate production database fix` — Semelhança: erro humano acidental causou perda de dados em produção, mas gatilho é variável de ambiente, não exclusão de diretório.
  - DAN-164 (llm) [Root cause analysis] 0.594: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.514: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.709: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.683: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [What We Learned] 0.732: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.72: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q02 (esperado: DAN-104)

- busca inicial: DAN-104, DAN-105, DAN-230, DAN-064, DAN-073, DAN-125, DAN-106, DAN-164, DAN-060, DAN-048
- justificativa: 
- aprofundar DAN-104: `typo command removed too many servers S3 outage remediation fix` — O resumo descreve erro humano com comando digitado errado que removeu muitos servidores e derrubou o S3, exatamente como o incidente atual, incluindo impacto cascata e mudanças depois.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.65: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.627: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q03 (esperado: DAN-090)

- busca inicial: DAN-090, DAN-025, DAN-216, DAN-136, DAN-023, DAN-154, DAN-018, DAN-016, DAN-005, DAN-024
- justificativa: 
- aprofundar DAN-090: `expired certificate Firefox add-ons fix privileged add-on certificate store` — O DAN-090 descreve exatamente um certificado expirado que desativou todos os add-ons do Firefox e a correção por meio de um add-on privilegiado que injetou um certificado válido no certificate store, correspondendo ao incidente atual.
  - DAN-090 (llm) [Root Cause Analysis] 0.696: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.543: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q04 (esperado: DAN-071)

- busca inicial: DAN-067, DAN-068, DAN-071, DAN-231, DAN-048, DAN-209, DAN-064, DAN-191, DAN-062, DAN-070
- justificativa: 
- aprofundar DAN-071: `lightning strikes european datacenter power loss storage systems permanent data loss fix remediation` — Bate exatamente: raios sucessivos no datacenter europeu causaram perda de energia nos sistemas de armazenamento, erros de I/O em HDDs e perda permanente de dados; não se sabe se o incidente atual é o Google ou europe-west1-b.
- aprofundar DAN-062: `severe weather power loss datacenter instances backup power fix remediation` — Bate parcialmente: perda de energia em datacenter por evento climático severo com impacto em instâncias; não menciona raios nem perda permanente em discos.
- aprofundar DAN-070: `datacenter power disruption servers boot Redis clusters restore fix` — Bate parcialmente: interrupção de energia no datacenter primário com impacto em serviços e necessidade de restauração; não menciona raios nem discos especificamente.
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.689: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.65: # Google Compute Engine Incident #15056  However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk. This outage is wholly Google's responsib
  - DAN-071 (causa) [Google Compute Engine Incident #15056] 0.415: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.335: # Google Compute Engine Incident #15056  The service has been partially recovered. Meanwhile, affected customers can restore from snapshots as a workaround solution. We will provide another status upd
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.324: # Google Compute Engine Incident #15056  Please also feel free to proactively contact support for more information. We will conduct an internal investigation of this issue and make appropriate improve
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.693: ### Summary of the AWS Service Event in the Sydney Region  If utility power is interrupted, the DRUPS uses this stored energy to continue to provide power to the datacenter while the integrated genera
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.657: ### Summary of the AWS Service Event in the Sydney Region  We’d like to share more detail about the AWS service disruption that occurred this past weekend in the AWS Sydney Region. The service disrupt
  - DAN-062 (causa) [Summary of the AWS Service Event in the Sydney Region] 0.399: ### Summary of the AWS Service Event in the Sydney Region  A latent bug in our instance management software led to a slower than expected recovery of the remaining instances. The team worked over the 
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.388: ### Summary of the AWS Service Event in the Sydney Region  Additionally, we will be taking actions to improve our recovery systems. The first is to fix the latent issue that led to our recovery system
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.359: ### Summary of the AWS Service Event in the Sydney Region  During the initial part of this event, customers experienced errors when trying to launch new instances, or when trying to scale their auto-s
  - DAN-070 (llm) [The Event] 0.813: ## The Event  By this point, we had a fairly clear picture of what was required to restore service and began working towards that end. We needed to repair our servers that were not booting, and we nee
  - DAN-070 (llm) [The Event] 0.655: ## The Event  Initial notifications for unreachable servers and a spike in exceptions related to Redis connectivity directed our team to investigate a possible outage in our internal network. We also 
  - DAN-070 (causa) [Future Work] 0.507: ## Future Work  Complex systems are defined by the interaction of many discrete components working together to achieve an end result. Understanding the dependencies for each component in a complex sys
  - DAN-070 (correcao) [Future Work] 0.534: ## Future Work  A number of less technical improvements are also being implemented. Strengthening our cross-team communications would have shaved minutes off the recovery time. Predefining escalation 
  - DAN-070 (correcao) [In Conclusion] 0.461: ## In Conclusion  We realize how important GitHub is to the workflows that enable your projects and businesses to succeed. All of us at GitHub would like to apologize for the impact of this outage. We

## q05 (esperado: DAN-084)

- busca inicial: DAN-084, DAN-050, DAN-106, DAN-017, DAN-042, DAN-154, DAN-207, DAN-116, DAN-125, DAN-191
- justificativa: 
- aprofundar DAN-084: `conflicting deployed versions re-used bit root cause fix $460M loss` — O resumo cita exatamente versões conflitantes implantadas e perda de $460M, o mesmo cenário do incidente atual.
- aprofundar DAN-017: `deployment tool bug production staging build version routing 401` — Envolve deploy apontando para versão/build errada, mas não cita $460M nem versões conflitantes do código.
- aprofundar DAN-042: `incorrect deployment process config variables not used code required` — Trata de processo de deploy incorreto, mas não de versões conflitantes nem da perda de $460M.
  - DAN-084 (llm) [sem seção] 0.531: I was speaking at a conference last year on the topics of DevOps, Configuration as Code, and Continuous Delivery and used the following story to demonstrate the importance making deployments fully aut
  - DAN-084 (llm) [What Could Possibly Go Wrong? Indeed!] 0.528: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-084 (causa) [45 Minutes of Hell] 0.448: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (correcao) [A Lesson to Learn] 0.316: ## A Lesson to Learn  The events of August 1, 2012 should be a lesson to all development and operations teams. It is not enough to build great software and test it; you also have to ensure it is deliv
  - DAN-084 (correcao) [Attack of the Killer Code Zombies] 0.361: ## Attack of the Killer Code Zombies  Its important to understand what the “dead” Power Peg code was meant to do. This functionality was meant to count the shares bought/sold against a parent order as
  - DAN-017 (llm) [Analysis] 0.587: ### Analysis  Workers KV is a low-latency key-value store that allows users to store persistent data on Cloudflare's network, as close to the users as possible. This distributed key-value store is use
  - DAN-017 (llm) [Analysis] 0.564: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-042 (llm) [It was such a nice morning] 0.636: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Did I mess up?] 0.632: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So

## q06 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-059, DAN-154, DAN-226, DAN-216, DAN-126, DAN-142, DAN-104, DAN-173, DAN-116
- justificativa: 
- aprofundar DAN-236: `steam deleted files root cause fix rm -rf directory path` — Este incidente descreve exatamente o caso atual: o cliente Steam apagou todos os arquivos do usuário após mover ~/.local/share/steam. Os outros incidentes são sobre quedas de rede, memória, SQL Server ou outros serviços, não sobre perda de arquivos do usuário pelo Steam.
  - DAN-236 (llm) [Activity] 0.71: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [Activity] 0.692: ## Activity  Polezhaiev and Safin SinghReacted by Harry Newsome, pizzanfruit, Paul, Torbjørn Viem Ness, Jonas Stein, Rakin Rahman and VasiliiGeneralov 2. I agree, that line minimally requires an exist
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [doofy commentedon Jan 15, 2015] 0.293: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti

## q07 (esperado: DAN-088, DAN-089)

- busca inicial: DAN-088, DAN-103, DAN-087, DAN-089, DAN-129, DAN-209, DAN-116, DAN-205, DAN-146, DAN-154
- justificativa: 
- aprofundar DAN-088: `leap second xtime_lock deadlock printk timer interrupt fix` — Bate: Linux, leap second e servidores travando; não ocorre: é de 2008-2009 e envolve deadlock no xtime_lock, não o cenário exato atual.
- aprofundar DAN-089: `leap second CLOCK_REALTIME hrtimer futex fix patch` — Bate: Linux, leap second e alta carga/servidores fora do ar; não ocorre: causa é ajuste incorreto do hrtimer e futex, não travamento por deadlock.
- aprofundar DAN-087: `leap second Go time.Now negative rand.Int63n panic fix` — Bate: leap second causando falha em sistemas; não ocorre: é Cloudflare DNS em Go, não servidores Linux travando.
  - DAN-088 (llm) [sem seção] 0.831: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.776: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.83: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.782: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.661: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.621: ### A falsehood programmers believe about time  RRDNS doesn’t just keep a single measurement for each resolver, it takes many measurements and smoothes them. So, the single measurement wouldn’t cause 
  - DAN-087 (causa) [sem seção] 0.385: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (correcao) [The one character fix] 0.332: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (correcao) [Timeline] 0.444: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is

## q08 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-164, DAN-078, DAN-217, DAN-096, DAN-221
- justificativa: 
- aprofundar DAN-145: `redis primary failover cluster rebalance cascading connection failure fix` — É o mais parecido: Redis primário de um cluster HA caiu, o cluster rebalanceou e houve falha em cascata nas conexões dos usuários. Difere porque o gatilho foi migração automática da GCP.
- aprofundar DAN-234: `redis cluster master crash resynchronization read-only fix` — Envolve Redis cluster e master crash, mas no contexto de billing/auto-recharge, não conexões de usuários em tempo real.
- aprofundar DAN-217: `cascading connection failures database capacity reconnection fix` — Tem falha de conexão em cascata após desconexões em massa, mas envolve banco de dados, não Redis.
  - DAN-145 (llm) [Sequence of Events] 0.706: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.678: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-234 (llm) [What We’re Doing About It] 0.654: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.616: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn
  - DAN-217 (llm) [TUESDAY] 0.729: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [WEDNESDAY] 0.529: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou

## q09 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-157, DAN-177, DAN-136, DAN-142, DAN-124, DAN-215, DAN-233, DAN-203
- justificativa: 
- aprofundar DAN-152: `npm account compromise malicious package publication root cause fix` — Conta de mantenedor comprometida e pacotes maliciosos publicados no registry, igual ao atual; difere no ecossistema (npm vs outro).
- aprofundar DAN-122: `JCenter malicious Maven packages impersonation attack root cause remediation` — Pacotes maliciosos em repositório público com ataque de personificação, muito parecido; difere no ecossistema (Maven/JCenter).
- aprofundar DAN-157: `Gentoo GitHub organization compromise access removal commits root cause fix` — Comprometimento de identidade organizacional no GitHub, similar; difere porque envolve commits e não publicação de pacotes.
  - DAN-152 (llm) [Summary] 0.749: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.746: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.727: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.657: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-157 (llm) [Incident summary] 0.769: ## Incident summary  An unknown entity gained control of an admin account for the Gentoo GitHub Organization and removed all access to the organization (and its repositories) from Gentoo developers. T
  - DAN-157 (llm) [2018-06-28] 0.751: ### 2018-06-28  Force-push.   - Same history as *gentoo/gentoo* in a squashed commit. - 21:00 (approx) GitHub informal report that they are starting to look - 21:05 Infra's formal ticket to GitHub Sup
  - DAN-157 (causa) [What went badly] 0.426: ### What went badly  - Initial communications were unclear and lacking detail in two areas.   - How can users verify their tree to be sure they had a clean copy?   - Clearer guidelines that even if us
  - DAN-157 (correcao) [Lessons] 0.478: ## Lessons  ### What went well  - Gentoo responded quickly to reports of problems. - GitHub responded quickly and had a function to hide the impacted organization. - Gentoo quickly removed account acc
  - DAN-157 (correcao) [Action items] 0.381: ## Action items  - Note: During the access revocation, some hosts were missed. - action-item: prod gentoo-infra members to start using local password managers (pass, gopass, etc.)   - *In-Progress: Dr

## q10 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-066, DAN-008, DAN-067, DAN-050, DAN-020, DAN-042, DAN-129, DAN-102
- justificativa: 
- aprofundar DAN-017: `deployment staging build unauthorized endpoint 401 fix rollback` — É o mais parecido: deploy que faz produção referenciar build de staging, endpoint não autorizado retorna HTTP 401 e gera falha em cascata em serviços dependentes. Difere por ser específico do Cloudflare e envolver versão de build, não apenas credenciais.
- aprofundar DAN-050: `deployment bug download URL generation fix rollback` — Semelha por ser uma implantação com bug que quebra requisições em escala, mas não envolve 401 nem serviço central de autenticação, apenas URLs de download de crates.
- aprofundar DAN-042: `deployment process config variables not used fix` — Semelha por ser um processo de implantação incorreto que impede config necessária de ser aplicada, mas não menciona 401 nem falha em cascata em produtos dependentes.
  - DAN-017 (llm) [Analysis] 0.566: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Timeline] 0.555: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.
  - DAN-050 (llm) [Recovery] 0.733: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Response] 0.686: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-042 (llm) [It was such a nice morning] 0.645: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Houston, we have a problem] 0.617: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Did I mess up?] 0.334: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru

## q11 (esperado: DAN-086, DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-198, DAN-191, DAN-221, DAN-066, DAN-015, DAN-124, DAN-179, DAN-084
- justificativa: 
- aprofundar DAN-086: `certificate expiration date leap year invalid date fix library` — Envolve certificados com data de expiração inválida causada por erro no cálculo de um ano (ano bissexto). Não bate necessariamente com o gatilho atual, mas é diretamente sobre certificados.
- aprofundar DAN-090: `expired certificate add-ons certificate chain fix privileged add-on` — Envolve certificado expirado que quebrou a cadeia de certificados e desabilitou add-ons do Firefox. Não bate necessariamente com o gatilho atual, mas é diretamente sobre certificados.
  - DAN-086 (llm) [The Leap Day Bug] 0.602: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.491: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.591: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.504: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q12 (esperado: nenhum)

- busca inicial: DAN-066, DAN-134, DAN-155, DAN-009, DAN-216, DAN-209, DAN-210, DAN-056, DAN-029, DAN-092
- justificativa: Busquei na base de post-mortems incidentes sobre o Pix do Banco Central em março de 2025, primeiro revisando a lista fornecida (nenhum relacionado a sistemas de pagamento ou ao Banco Central do Brasil) e depois tentando novas buscas com termos como "Pix payment system outage Brazil March 2025" e "Banco Central Brazil payment disruption 2025", mas nenhum dos incidentes encontrados tem relação com o incidente em andamento.
- novos incidentes nos achados: DAN-221, DAN-191, DAN-234, DAN-154, DAN-193
