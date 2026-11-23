# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q01 | DAN-164 | — | sim | sim | search | não | sim | 0 | 6 |
| q02 | DAN-104 | — | sim | sim | search | não | sim | 0 | 5 |
| q03 | DAN-090 | — | sim | sim | search | não | sim | 0 | 5 |
| q04 | DAN-071 | — | sim | sim | search | não | sim | 0 | 15 |
| q05 | DAN-084 | — | sim | sim | search | não | sim | 0 | 10 |
| q06 | DAN-236 | — | sim | sim | search | não | sim | 0 | 3 |
| q07 | DAN-088, DAN-089 | — | sim | sim | search | não | sim | 0 | 25 |
| q08 | DAN-145 | — | sim | sim | search | não | sim | 0 | 17 |
| q09 | DAN-122 | — | sim | sim | search | não | sim | 0 | 12 |
| q10 | DAN-017 | — | sim | sim | search | não | sim | 0 | 12 |
| q11 | DAN-086, DAN-090 | — | sim | sim | search | não | sim | 0 | 17 |
| q12 | (nenhum) | — | — | — | find → (texto) | — | — | 2 | 13 |

## q01 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-043, DAN-220, DAN-186, DAN-209, DAN-048, DAN-195, DAN-056, DAN-058, DAN-026
- justificativa: 
- aprofundar DAN-164: `root cause fix wrong directory deletion data loss recovery` — É o único que corresponde exatamente ao incidente atual: administrador cansado apagou o diretório errado e se perderam seis horas de dados. Os demais são falhas de banco, migração ou configuração, não exclusão de diretório por erro humano.
  - DAN-164 (llm) [Root cause analysis] 0.634: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.571: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q02 (esperado: DAN-104)

- busca inicial: DAN-104, DAN-105, DAN-230, DAN-064, DAN-073, DAN-125, DAN-106, DAN-164, DAN-060, DAN-048
- justificativa: 
- aprofundar DAN-104: `human error typo command remove servers S3 outage remediation fix` — Corresponde exatamente: comando com erro de digitação removeu servidores além do previsto e derrubou o armazenamento S3; o resto da lista trata de falhas de hardware, corrupção, log ou energia, sem relação com o comando errado.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.63: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.623: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q03 (esperado: DAN-090)

- busca inicial: DAN-090, DAN-025, DAN-216, DAN-136, DAN-023, DAN-154, DAN-018, DAN-016, DAN-005, DAN-024
- justificativa: 
- aprofundar DAN-090: `expired certificate add-ons outage fix privileged add-on certificate store` — É o único incidente da lista que envolve certificado expirado fazendo add-ons do Firefox pararem, exatamente como o incidente atual; os outros são falhas de rede, configuração ou memory leak em serviços diferentes.
  - DAN-090 (llm) [Root Cause Analysis] 0.612: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.573: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q04 (esperado: DAN-071)

- busca inicial: DAN-067, DAN-068, DAN-071, DAN-231, DAN-048, DAN-209, DAN-064, DAN-191, DAN-062, DAN-070
- justificativa: 
- aprofundar DAN-071: `lightning datacenter power loss disk I/O errors permanent data loss root cause fix` — É o único incidente que menciona raios atingindo o datacenter e perda de energia em discos, correspondendo ao incidente atual; ainda não se sabe se detalha correção além da perda de dados.
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.672: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.643: # Google Compute Engine Incident #15056  | |  | SUMMARY: From Thursday 13 August 2015 to Monday 17 August 2015, errors occurred on a small proportion of Google Compute Engine persistent disks in the e
  - DAN-071 (causa) [Google Compute Engine Incident #15056] 0.415: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.358: # Google Compute Engine Incident #15056  However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk. This outage is wholly Google's responsib
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.335: # Google Compute Engine Incident #15056  The service has been partially recovered. Meanwhile, affected customers can restore from snapshots as a workaround solution. We will provide another status upd

## q05 (esperado: DAN-084)

- busca inicial: DAN-084, DAN-050, DAN-106, DAN-017, DAN-042, DAN-154, DAN-207, DAN-116, DAN-125, DAN-191
- justificativa: 
- aprofundar DAN-084: `conflicting deployed versions re-used bit 460 million loss root cause fix` — Mesmo cenário de deploy com versões conflitantes e prejuízo de 460M, bate exatamente com o incidente atual.
- aprofundar DAN-017: `deployment tool bug staging build version production unauthorized endpoint fix` — Envolve deploy que direcionou produção para versão de staging, mas não cita versões conflitantes nem 460M de prejuízo.
- aprofundar DAN-042: `incorrect deployment process config variables not used code required fix` — Trata de processo de implantação incorreto, mas sem versões conflitantes nem prejuízo de 460M.
  - DAN-084 (llm) [What Could Possibly Go Wrong? Indeed!] 0.542: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-084 (llm) [45 Minutes of Hell] 0.528: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (causa) [sem seção] 0.424: I was speaking at a conference last year on the topics of DevOps, Configuration as Code, and Continuous Delivery and used the following story to demonstrate the importance making deployments fully aut
  - DAN-084 (correcao) [A Lesson to Learn] 0.316: ## A Lesson to Learn  The events of August 1, 2012 should be a lesson to all development and operations teams. It is not enough to build great software and test it; you also have to ensure it is deliv
  - DAN-084 (correcao) [Attack of the Killer Code Zombies] 0.361: ## Attack of the Killer Code Zombies  Its important to understand what the “dead” Power Peg code was meant to do. This functionality was meant to count the shares bought/sold against a parent order as
  - DAN-017 (llm) [Analysis] 0.566: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Analysis] 0.561: ### Analysis  Workers KV is a low-latency key-value store that allows users to store persistent data on Cloudflare's network, as close to the users as possible. This distributed key-value store is use
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-042 (llm) [Did I mess up?] 0.639: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (llm) [It was such a nice morning] 0.631: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So

## q06 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-059, DAN-154, DAN-226, DAN-216, DAN-126, DAN-142, DAN-104, DAN-173, DAN-116
- justificativa: 
- aprofundar DAN-236: `steam deleted files root cause fix rm -rf` — Este incidente é exatamente o descrito no caso atual: o cliente Steam apagou todos os arquivos do usuário após mover ~/.local/share/steam. É o mais relevante da lista.
  - DAN-236 (llm) [Activity] 0.699: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [jthill commentedon Jan 15, 2015] 0.696: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [doofy commentedon Jan 15, 2015] 0.293: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 

## q07 (esperado: DAN-088, DAN-089)

- busca inicial: DAN-088, DAN-103, DAN-087, DAN-089, DAN-129, DAN-209, DAN-116, DAN-205, DAN-146, DAN-154
- justificativa: 
- aprofundar DAN-088: `leap second deadlock xtime_lock printk klogd kernel fix patch` — Bate: Linux, leap second, servidores travando ao mesmo tempo; não bate: travamento por deadlock de impressão de log, não necessariamente todos os servidores.
- aprofundar DAN-089: `leap second futex CLOCK_REALTIME hrtimer offset high load fix patch` — Bate: Linux, leap second, múltiplos sistemas afetados simultaneamente; não bate: causa é timers expirando cedo e carga alta, não travamento total descrito no incidente atual.
- aprofundar DAN-087: `leap second backwards time Go time.Now monotonic rand Int63n panic fix` — Bate: leap second afetando sistemas em produção; não bate: é DNS da Cloudflare e linguagem Go, não servidores Linux travando pelo kernel.
  - DAN-088 (llm) [sem seção] 0.798: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.78: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.81: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.699: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.239: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.692: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe
  - DAN-087 (llm) [The one character fix] 0.601: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (causa) [sem seção] 0.385: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (correcao) [Timeline] 0.444: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is
  - DAN-087 (correcao) [A little bit about Cloudflare DNS] 0.318: ### A little bit about Cloudflare DNS  Cloudflare customers use our DNS service to serve the authoritative answers for DNS queries for their domains. They need to tell us the IP address of their origi

## q08 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-164, DAN-078, DAN-217, DAN-096, DAN-221
- justificativa: 
- aprofundar DAN-145: `Redis primary failover cluster rebalance cascading failure fix` — Redis primária em cluster de alta disponibilidade caiu, forçou rebalance e gerou falha em cascata, igual ao incidente atual
- aprofundar DAN-234: `Redis network partition master crash read-only retry cascade fix` — Redis cluster com partição de rede, master caiu e causou retry em cascata, embora seja de faturamento e não de conexões de usuário
- aprofundar DAN-217: `massive reconnection cascading connection failures database capacity fix` — Falha em cascata de conexões após desconexões em massa, mas sem envolvimento de queda de Redis primária
  - DAN-145 (llm) [Sequence of Events] 0.699: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.683: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-234 (llm) [What We’re Doing About It] 0.603: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.596: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn
  - DAN-217 (llm) [TUESDAY] 0.732: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [WEDNESDAY] 0.537: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou

## q09 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-157, DAN-177, DAN-136, DAN-142, DAN-124, DAN-215, DAN-233, DAN-203
- justificativa: 
- aprofundar DAN-122: `malicious packages JCenter impersonation attack root cause fix removal` — Bate: pacotes maliciosos em repositório público via ataque de personificação de desenvolvedor. Não bate: é Maven/JCenter e Android, não necessariamente o mesmo ecossistema do atual.
- aprofundar DAN-152: `compromised npm account malicious packages published root cause fix` — Bate: conta de desenvolvedor conhecido comprometida e pacotes maliciosos publicados em seu nome no registro público. Não bate: é npm/JavaScript, pode ser ecossistema diferente.
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.774: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.701: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.759: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.741: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q10 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-066, DAN-008, DAN-067, DAN-050, DAN-020, DAN-042, DAN-129, DAN-102
- justificativa: 
- aprofundar DAN-017: `deployment staging build unauthorized endpoint 401 fix rollback` — Bate com deploy + HTTP 401 + falhas em cascata em produtos dependentes; difere no componente específico (Cloudflare Workers KV, Pages, Access).
- aprofundar DAN-050: `deployment bug download URL generation broken fix rollback` — Bate com deploy que quebrou serviço central; não envolve erro 401 nem autorização.
- aprofundar DAN-042: `incorrect deployment config variables not used fix rollback` — Bate com processo de deploy incorreto após release; não envolve 401 nem falha em cascata de dependentes.
  - DAN-017 (llm) [Analysis] 0.566: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Timeline] 0.555: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.
  - DAN-050 (llm) [Recovery] 0.758: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Response] 0.7: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-042 (llm) [It was such a nice morning] 0.653: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Houston, we have a problem] 0.641: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Did I mess up?] 0.334: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru

## q11 (esperado: DAN-086, DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-198, DAN-191, DAN-221, DAN-066, DAN-015, DAN-124, DAN-179, DAN-084
- justificativa: 
- aprofundar DAN-086: `certificate expiration leap year invalid date root cause fix` — O resumo já cita certificados com expiração inválida em 29 de fevereiro devido a cálculo incorreto de um ano, diretamente relacionado a certificados.
- aprofundar DAN-090: `add-on certificate expired Firefox root cause fix renewal` — O resumo cita expiração de certificado que parou os add-ons do Firefox, claramente um incidente de certificado.
  - DAN-086 (llm) [The Leap Day Bug] 0.624: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.537: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.732: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.551: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q12 (esperado: nenhum)

- busca inicial: DAN-066, DAN-134, DAN-155, DAN-009, DAN-216, DAN-209, DAN-210, DAN-056, DAN-029, DAN-092
- justificativa: Busquei por incidentes de queda do Pix do Banco Central em março de 2025 e de pane no sistema de pagamentos instantâneo do Brasil, mas nenhum dos post-mortems encontrados (atualmente nem nos resultados adicionais) trata do Pix ou do Banco Central — todos são sobre outros serviços (Cloudflare, CircleCI, Fastly, Twilio, etc.). Portanto, não há evidência histórica disponível nesta base sobre causa raiz e duração desse incidente específico.
- novos incidentes nos achados: DAN-154, DAN-191, DAN-221, DAN-234, DAN-186
