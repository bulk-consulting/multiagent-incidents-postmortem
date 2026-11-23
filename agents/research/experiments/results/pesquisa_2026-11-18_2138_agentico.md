# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q01 | DAN-164 | — | não | sim | find → search | sim | sim | 2 | 11 |
| q02 | DAN-104 | — | não | sim | find → search | sim | sim | 3 | 43 |
| q03 | DAN-090 | — | não | sim | find → search | sim | sim | 2 | 5 |
| q04 | DAN-071 | — | não | sim | find → search | sim | sim | 2 | 51 |
| q05 | DAN-084 | — | não | sim | find → search | sim | sim | 2 | 7 |
| q06 | DAN-236 | — | não | sim | find → search | sim | sim | 2 | 49 |
| q07 | DAN-088, DAN-089 | — | não | sim | find → search | sim | sim | 2 | 111 |
| q08 | DAN-145 | — | não | sim | find → search | sim | sim | 2 | 75 |
| q09 | DAN-122 | — | não | sim | find → search | sim | sim | 2 | 7 |
| q10 | DAN-017 | — | não | sim | find → search | sim | sim | 2 | 15 |
| q11 | DAN-086, DAN-090 | — | não | sim | find → search | sim | sim | 2 | 255 |
| q12 | (nenhum) | — | — | — | find → find → find → find | — | — | 8 | 87 |

## q01 (esperado: DAN-164)

- busca inicial: 
- justificativa: 
- aprofundar DAN-164: `root cause tired admin deleted wrong directory fix data loss recovery` — O resumo menciona exatamente administrador cansado apagou o diretório errado e seis horas de dados perdidos, correspondendo ao incidente atual.
- aprofundar DAN-043: `root cause accidentally deleted production database fix backup recovery data loss` — Engenheiros apagaram produção por acidente e perderam horas de dados; sintoma de exclusão acidental com perda de dados é semelhante, embora seja banco de dados, não diretório.
- aprofundar DAN-104: `root cause human error typo command removed servers fix remediation S3 outage` — Erro humano durante operação com comando digitado errado causou remoção maior que o previsto; causa é erro operacional, mas componente afetado são servidores, não diretório.
- novos incidentes nos achados: DAN-164, DAN-043, DAN-104, DAN-048, DAN-146, DAN-058, DAN-056, DAN-103, DAN-106, DAN-118
  - DAN-164 (llm) [Root cause analysis] 0.634: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.535: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.705: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.651: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.625: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.619: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q02 (esperado: DAN-104)

- busca inicial: 
- justificativa: 
- aprofundar DAN-104: `root cause typo command removed servers S3 systems restart corrective actions changes after outage` — é o único que descreve exatamente um comando digitado errado que removeu demasiados servidores e derrubou o S3, incluindo o que mudou depois.
- novos incidentes nos achados: DAN-104, DAN-060, DAN-106, DAN-230, DAN-105, DAN-107, DAN-189, DAN-061, DAN-164, DAN-075
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.612: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.609: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q03 (esperado: DAN-090)

- busca inicial: 
- justificativa: 
- aprofundar DAN-090: `root cause certificate expired fix privileged add-on certificate store` — Este incidente é a correspondência exata: certificado expirado fazendo os add-ons do Firefox pararem de funcionar, com resolução descrita. Preciso da causa raiz detalhada e como foi corrigido.
- novos incidentes nos achados: DAN-090, DAN-086, DAN-025, DAN-216, DAN-154, DAN-136, DAN-011, DAN-137, DAN-008, DAN-024
  - DAN-090 (llm) [Root Cause Analysis] 0.65: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.455: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (causa) [sem seção] 0.366: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q04 (esperado: DAN-071)

- busca inicial: 
- justificativa: 
- aprofundar DAN-071: `lightning strikes root cause power loss disk permanent data loss fix mitigation` — É o único incidente que corresponde exatamente: raios atingiram o datacenter europeu e causaram perda de energia nos discos de armazenamento, com erros de I/O e perda permanente de dados em uma pequena fração — o mesmo sintoma do incidente atual.
- novos incidentes nos achados: DAN-068, DAN-071, DAN-067, DAN-062, DAN-060, DAN-061, DAN-064, DAN-070, DAN-073, DAN-231
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.633: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.593: # Google Compute Engine Incident #15056  However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk. This outage is wholly Google's responsib
  - DAN-071 (causa) [Google Compute Engine Incident #15056] 0.415: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.335: # Google Compute Engine Incident #15056  The service has been partially recovered. Meanwhile, affected customers can restore from snapshots as a workaround solution. We will provide another status upd
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.324: # Google Compute Engine Incident #15056  Please also feel free to proactively contact support for more information. We will conduct an internal investigation of this issue and make appropriate improve

## q05 (esperado: DAN-084)

- busca inicial: 
- justificativa: 
- aprofundar DAN-084: `root cause conflicting deployed versions old code new code fix rollback $460M loss` — O resumo menciona exatamente versões implantadas conflitantes e perda de $460M, correspondendo ao incidente atual de deploy com versões diferentes do código.
- novos incidentes nos achados: DAN-084, DAN-017, DAN-116, DAN-042, DAN-050, DAN-106, DAN-068, DAN-003, DAN-049, DAN-154
  - DAN-084 (llm) [sem seção] 0.533: I was speaking at a conference last year on the topics of DevOps, Configuration as Code, and Continuous Delivery and used the following story to demonstrate the importance making deployments fully aut
  - DAN-084 (llm) [45 Minutes of Hell] 0.53: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (causa) [What Could Possibly Go Wrong? Indeed!] 0.41: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-084 (correcao) [A Lesson to Learn] 0.316: ## A Lesson to Learn  The events of August 1, 2012 should be a lesson to all development and operations teams. It is not enough to build great software and test it; you also have to ensure it is deliv
  - DAN-084 (correcao) [Attack of the Killer Code Zombies] 0.361: ## Attack of the Killer Code Zombies  Its important to understand what the “dead” Power Peg code was meant to do. This functionality was meant to count the shares bought/sold against a parent order as

## q06 (esperado: DAN-236)

- busca inicial: 
- justificativa: 
- aprofundar DAN-236: `root cause fix Steam deleted everything user files` — O incidente DAN-236 descreve exatamente o cliente Steam deletando todos os arquivos e diretórios locais do usuário, mesmo sintoma do incidente atual; a diferença é que ocorre no Steam for Linux, enquanto o incidente atual não especifica o sistema operacional.
- aprofundar DAN-076: `root cause fix installer deleted boot.ini file` — DAN-076 envolve um instalador de jogo deletando um arquivo do sistema por erro de digitação e conflito de nome, semelhante no sentido de deletar arquivos do usuário, mas o componente é um instalador de expansão, não o cliente Steam.
- novos incidentes nos achados: DAN-236, DAN-059, DAN-076, DAN-142, DAN-126, DAN-154, DAN-173, DAN-146, DAN-116, DAN-050
  - DAN-236 (llm) [Activity] 0.703: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.696: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 
  - DAN-076 (llm) [About the boot.ini issue] 0.746: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.729: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 

## q07 (esperado: DAN-088, DAN-089)

- busca inicial: 
- justificativa: 
- aprofundar DAN-089: `leap second futex hrtimer CLOCK_REALTIME offset patch fix` — Mesmo gatilho (leap second) e mesmo componente (relógio do kernel Linux); sintoma de servidores ficando inresponsivos com carga alta bate com o atual, embora o mecanismo seja spinwait de timers.
- aprofundar DAN-088: `leap second xtime_lock deadlock printk klogd fix` — Mesmo gatilho e componente (kernel Linux no segundo bissexto); deadlock congelou sistemas, bate com 'travaram e pararam de responder', embora seja de 2008-2009.
- novos incidentes nos achados: DAN-089, DAN-088, DAN-103, DAN-129, DAN-073, DAN-016, DAN-230, DAN-087, DAN-116, DAN-026
  - DAN-089 (llm) [sem seção] 0.819: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.754: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.239: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-088 (llm) [sem seção] 0.792: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.761: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (causa) [sem seção] 0.328: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco

## q08 (esperado: DAN-145)

- busca inicial: 
- justificativa: 
- aprofundar DAN-145: `Redis primary failover root cause fix cluster rebalance cascading connection failure` — O incidente Discord (DAN-145) é o mais parecido: Redis primário em cluster de alta disponibilidade caiu, forçou rebalanceamento do cluster e gerou falha em cascata no sistema em tempo real, exatamente como descrito no incidente atual.
- novos incidentes nos achados: DAN-145, DAN-234, DAN-066, DAN-210, DAN-029, DAN-211, DAN-109, DAN-026, DAN-078, DAN-096
  - DAN-145 (llm) [Sequence of Events] 0.701: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.656: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci

## q09 (esperado: DAN-122)

- busca inicial: 
- justificativa: 
- aprofundar DAN-152: `root cause fix compromised npm account malicious packages published` — Bate exatamente: conta de mantenedor comprometida e pacotes maliciosos publicados no registro público (npm). O incidente atual também envolve pacotes maliciosos em nome de um desenvolvedor conhecido.
- aprofundar DAN-122: `root cause fix malicious Maven packages JCenter impersonation attack` — Também é relevante: pacotes maliciosos incluídos em repositório público (JCenter) por ataque de personificação. Difere um pouco porque foca em pacotes Maven/Android, mas o sintoma de pacotes maliciosos no repositório público é o mesmo.
- novos incidentes nos achados: DAN-152, DAN-177, DAN-157, DAN-131, DAN-122, DAN-175, DAN-203, DAN-124, DAN-050, DAN-233
  - DAN-152 (llm) [Summary] 0.748: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.733: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.727: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.638: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q10 (esperado: DAN-017)

- busca inicial: 
- justificativa: 
- aprofundar DAN-017: `deployment staging build unauthorized endpoint 401 root cause fix rollback` — Bate muito: deploy em produção apontou para build de staging/endpoint não autorizado, gerando HTTP 401 e falha em cascata em serviços dependentes, igual ao incidente atual. Não bate: componente é Cloudflare (Workers KV/Pages/etc.), não o serviço central descrito aqui.
- aprofundar DAN-015: `credential rotation wrong environment authentication failure 401 root cause fix` — Bate: credenciais implantadas no ambiente errado após deploy causaram falha de autenticação (401) no gateway. Não bate: é rotação de credenciais R2/storage, não necessariamente um serviço central com todos os produtos dependentes.
- novos incidentes nos achados: DAN-017, DAN-015, DAN-042, DAN-220, DAN-050, DAN-116, DAN-113, DAN-102, DAN-147, DAN-003
  - DAN-017 (llm) [Analysis] 0.562: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Timeline] 0.542: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.
  - DAN-015 (llm) [Next steps] 0.665: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (llm) [Incident timeline] 0.613: ## Incident timeline  **All timestamps referenced are in Coordinated Universal Time (UTC).**  | Time | Event | |---|---| | Mar 21, 2025 - 19:49 UTC | The R2 engineering team started the credential rot
  - DAN-015 (causa) [Incident timeline] 0.42: ## Incident timeline  Given gradual decline in availability metrics, R2 engineering team suspected a potential regression in propagation of new credentials in storage infrastructure. | | Mar 21, 2025 
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [Next steps] 0.468: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor

## q11 (esperado: DAN-086, DAN-090)

- busca inicial: 
- justificativa: 
- aprofundar DAN-086: `certificate root cause fix leap year expiration` — O incidente da Azure envolveu certificados com data de expiração inválida (29 de fevereiro de 2013) gerada por um cálculo incorreto de 'um ano', causando uma interrupção global. Quero entender a causa raiz exata e como foi corrigido.
- aprofundar DAN-090: `certificate expired add-ons fix root cause` — O incidente da Mozilla envolveu o vencimento de um certificado que desativou praticamente todos os add-ons do Firefox. Quero confirmar a causa raiz (expiração do certificado) e a correção aplicada (injeção de certificado válido).
- novos incidentes nos achados: DAN-086, DAN-090, DAN-191, DAN-189, DAN-015, DAN-209, DAN-154, DAN-066, DAN-210, DAN-067
  - DAN-086 (llm) [The Leap Day Bug] 0.611: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.531: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.696: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.583: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (causa) [sem seção] 0.366: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q12 (esperado: nenhum)

- busca inicial: 
- justificativa: 
- novos incidentes nos achados: DAN-209, DAN-221, DAN-066, DAN-191, DAN-154, DAN-029, DAN-056, DAN-148, DAN-068, DAN-204, DAN-234, DAN-193, DAN-186, DAN-116, DAN-073, DAN-210, DAN-013, DAN-181, DAN-222, DAN-195, DAN-205, DAN-216, DAN-059, DAN-180, DAN-067, DAN-129, DAN-011, DAN-137, DAN-102, DAN-023, DAN-164, DAN-109, DAN-189, DAN-224, DAN-118, DAN-020, DAN-133, DAN-070, DAN-001, DAN-169
