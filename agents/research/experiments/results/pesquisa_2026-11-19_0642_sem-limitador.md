# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q01 | DAN-164 | — | sim | sim | search | não | sim | 0 | 15 |
| q02 | DAN-104 | — | sim | sim | search | não | sim | 0 | 17 |
| q03 | DAN-090 | — | sim | sim | search | não | sim | 0 | 11 |
| q04 | DAN-071 | — | sim | sim | search | não | sim | 0 | 6 |
| q05 | DAN-084 | — | sim | sim | search | não | sim | 0 | 19 |
| q06 | DAN-236 | — | sim | sim | search | não | sim | 0 | 17 |
| q07 | DAN-088, DAN-089 | — | sim | sim | search | não | sim | 0 | 32 |
| q08 | DAN-145 | — | sim | sim | search | não | sim | 0 | 55 |
| q09 | DAN-122 | — | sim | sim | search | não | sim | 0 | 11 |
| q10 | erro: Exception: [429] Too Many Requests
{'status': 429, 'title': 'Too Many Requests'} | | | | | | | | | 45 |
| q11 | DAN-086, DAN-090 | — | sim | sim | search | não | sim | 0 | 6 |
| q12 | (nenhum) | — | — | — | find → (texto) | — | — | 2 | 40 |

## q01 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-043, DAN-220, DAN-186, DAN-209, DAN-048, DAN-195, DAN-056, DAN-058, DAN-026
- justificativa: 
- aprofundar DAN-164: `wrong directory deleted tired admin data loss recovery fix` — Corresponde exatamente ao incidente atual: administrador cansado apagou o diretório errado e se perderam seis horas de dados; mesmo componente (GitLab/database) e mesmo gatilho humano de exclusão acidental.
- aprofundar DAN-043: `accidental production database deletion recovery backups fix` — Também envolve exclusão acidental do banco de produção com perda de cerca de sete horas de dados, embora o gatilho seja engenheiros e não um administrador cansado apagando um diretório específico.
  - DAN-164 (llm) [Timeline] 0.541: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (llm) [Root cause analysis] 0.54: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.741: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.665: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo

## q02 (esperado: DAN-104)

- busca inicial: DAN-104, DAN-105, DAN-230, DAN-064, DAN-073, DAN-125, DAN-106, DAN-164, DAN-060, DAN-048
- justificativa: 
- aprofundar DAN-104: `typo command removed too many servers S3 outage root cause fix` — O resumo descreve exatamente um comando digitado errado que removeu mais servidores do que o previsto e derrubou o S3, igual ao incidente atual; não há diferença relevante no gatilho.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.646: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.636: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q03 (esperado: DAN-090)

- busca inicial: DAN-090, DAN-025, DAN-216, DAN-136, DAN-023, DAN-154, DAN-018, DAN-016, DAN-005, DAN-024
- justificativa: 
- aprofundar DAN-090: `expired certificate add-ons outage root cause fix` — O incidente DAN-090 descreve exatamente um certificado expirado que fez todos os add-ons do Firefox pararem de funcionar em maio de 2019, correspondendo diretamente ao incidente atual. Não há outros incidentes na lista relacionados a certificado expirado do Firefox.
  - DAN-090 (llm) [Root Cause Analysis] 0.699: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.6: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q04 (esperado: DAN-071)

- busca inicial: DAN-067, DAN-068, DAN-071, DAN-231, DAN-048, DAN-209, DAN-064, DAN-191, DAN-062, DAN-070
- justificativa: 
- aprofundar DAN-071: `lightning strikes datacenter power loss persistent disks data loss recovery` — Bate exatamente: raios no datacenter europeu causaram perda de energia em sistemas de armazenamento, com erros de I/O e perda permanente de dados em HDDs. Não bate porque é o Google Cloud, não o datacenter do analista.
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.706: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.665: # Google Compute Engine Incident #15056  However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk. This outage is wholly Google's responsib
  - DAN-071 (causa) [Google Compute Engine Incident #15056] 0.415: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.335: # Google Compute Engine Incident #15056  The service has been partially recovered. Meanwhile, affected customers can restore from snapshots as a workaround solution. We will provide another status upd
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.324: # Google Compute Engine Incident #15056  Please also feel free to proactively contact support for more information. We will conduct an internal investigation of this issue and make appropriate improve

## q05 (esperado: DAN-084)

- busca inicial: DAN-084, DAN-050, DAN-106, DAN-017, DAN-042, DAN-154, DAN-207, DAN-116, DAN-125, DAN-191
- justificativa: 
- aprofundar DAN-084: `conflicting deployed versions reused bit 460M loss root cause fix` — O resumo menciona exatamente versões conflitantes implantadas e perda de $460M, igual ao incidente atual; não bate apenas se o atual for outro caso com mesmo valor.
  - DAN-084 (llm) [What Could Possibly Go Wrong? Indeed!] 0.521: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-084 (llm) [45 Minutes of Hell] 0.506: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (causa) [sem seção] 0.424: I was speaking at a conference last year on the topics of DevOps, Configuration as Code, and Continuous Delivery and used the following story to demonstrate the importance making deployments fully aut
  - DAN-084 (correcao) [A Lesson to Learn] 0.316: ## A Lesson to Learn  The events of August 1, 2012 should be a lesson to all development and operations teams. It is not enough to build great software and test it; you also have to ensure it is deliv
  - DAN-084 (correcao) [Attack of the Killer Code Zombies] 0.361: ## Attack of the Killer Code Zombies  Its important to understand what the “dead” Power Peg code was meant to do. This functionality was meant to count the shares bought/sold against a parent order as

## q06 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-059, DAN-154, DAN-226, DAN-216, DAN-126, DAN-142, DAN-104, DAN-173, DAN-116
- justificativa: 
- aprofundar DAN-236: `root cause fix Steam deleted all local user files ~/.local/share/steam` — É exatamente o incidente atual: o cliente Steam apagou arquivos do usuário. O resumo confirma a falha, mas não explica o bug nem a correção.
  - DAN-236 (llm) [Activity] 0.774: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [Moved \~/.local/share/steam. Ran steam. It deleted everything on system owned by user. #3671] 0.755: # Moved \~/.local/share/steam. Ran steam. It deleted everything on system owned by user. #3671  ## Description  Edit: Please stop posting stupid image memes or unhelpful messages. This interferes with
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [doofy commentedon Jan 15, 2015] 0.293: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti

## q07 (esperado: DAN-088, DAN-089)

- busca inicial: DAN-088, DAN-103, DAN-087, DAN-089, DAN-129, DAN-209, DAN-116, DAN-205, DAN-146, DAN-154
- justificativa: 
- aprofundar DAN-088: `leap second xtime_lock printk klogd deadlock fix kernel` — Trata de travamento do Linux no segundo bissexto com deadlock no xtime_lock, parecido com servidores parando de responder, embora seja de 2008 e envolva printk/klogd.
- aprofundar DAN-089: `leap second futex CLOCK_REALTIME hrtimer offset fix 2012` — Trata de falha no Linux por segundo bissexto em 2012 com CLOCK_REALTIME e timers expirando cedo, gerando carga alta e quedas, bem parecido com travamento coletivo, mas focado em futex/hrtimer.
  - DAN-088 (llm) [sem seção] 0.809: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.771: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (causa) [sem seção] 0.328: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.837: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.747: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti

## q08 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-164, DAN-078, DAN-217, DAN-096, DAN-221
- justificativa: 
- aprofundar DAN-145: `Redis primary failover cluster rebalance cascading connection failure fix` — Bate: Redis primária, rebalanceamento de cluster, falha em cascata nas conexões. Não bate: foi migração automática da GCP, não queda espontânea.
- aprofundar DAN-234: `Redis cluster master crash resynchronization read-only root cause fix` — Bate: envolve cluster Redis, queda do master e impacto em serviços. Não bate: foco em cobrança/billing, não em falha em cascata de conexões de usuários.
- aprofundar DAN-217: `cascading connection failures user disconnection reconnection database capacity fix` — Bate: falha em cascata de conexões de usuários após desconexões em massa. Não bate: causa é capacidade do banco, não queda de primária Redis.
  - DAN-145 (llm) [Sequence of Events] 0.713: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.685: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-234 (llm) [What We’re Doing About It] 0.658: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.651: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn
  - DAN-217 (llm) [TUESDAY] 0.784: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [sem seção] 0.572: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [WEDNESDAY] 0.429: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou

## q09 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-157, DAN-177, DAN-136, DAN-142, DAN-124, DAN-215, DAN-233, DAN-203
- justificativa: 
- aprofundar DAN-122: `malicious packages impersonation attack JCenter Maven root cause fix` — Bate por envolver pacotes maliciosos num repositório público de bibliotecas (JCenter) com ataque de personificação, embora seja Maven/Android e não um desenvolvedor individual conhecido.
- aprofundar DAN-152: `compromised npm account maintainer malicious packages root cause remediation` — Bate por envolver conta de mantenedor comprometida e pacotes maliciosos publicados no repositório público npm, embora o alvo seja um projeto linter e não um desenvolvedor específico.
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.751: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.687: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.751: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.735: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q11 (esperado: DAN-086, DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-198, DAN-191, DAN-221, DAN-066, DAN-015, DAN-124, DAN-179, DAN-084
- justificativa: 
- aprofundar DAN-086: `certificate expiration date February 29 2012 cause fix` — Envolve certificados com data de expiração inválida por erro de ano bissexto, causa diretamente ligada a certificados, diferente do atual que pode envolver certificado expirado ou inválido.
- aprofundar DAN-090: `expired certificate add-ons outage fix privileged add-on` — Envolve certificado expirado que parou todos os add-ons do Firefox, causa raiz claramente relacionada a certificado, mas o gatilho é expiração e não data inválida.
  - DAN-086 (llm) [The Leap Day Bug] 0.573: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.555: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [sem seção] 0.619: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (llm) [Root Cause Analysis] 0.611: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q12 (esperado: nenhum)

- busca inicial: DAN-066, DAN-134, DAN-155, DAN-009, DAN-216, DAN-209, DAN-210, DAN-056, DAN-029, DAN-092
- justificativa: Busquei na base de post-mortems incidentes parecidos com a indisponibilidade do Pix do Banco Central em março de 2025, incluindo buscas específicas por "Pix Banco Central outage March 2025" e "central bank payment system unavailable March 2025 Brazil". Nenhum dos incidentes encontrados (nem os da lista inicial nem os da nova busca) trata do Pix, do Banco Central do Brasil ou de sistemas de pagamento instantâneo, portanto não há evidência histórica nesta base sobre a causa raiz nem a duração desse incidente.
- novos incidentes nos achados: DAN-191, DAN-181, DAN-068, DAN-204, DAN-073
