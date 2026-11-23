# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-207 | DAN-085 | 1 | não | sim | find → search | sim | sim | 3 | 3 |
| q-208 | DAN-086 | 1 | não | sim | find → search | sim | sim | 2 | 71 |
| q-209 | DAN-086 | 1 | não | sim | find → search | sim | sim | 2 | 4 |
| q-210 | DAN-088 | 1 | não | sim | find → search | sim | sim | 2 | 37 |
| q-211 | DAN-088 | 1 | não | sim | find → search | sim | sim | 2 | 41 |
| q-212 | DAN-092 | 1 | não | sim | find → search | sim | sim | 2 | 4 |
| q-213 | DAN-092 | 1 | não | sim | find → search | sim | sim | 2 | 66 |
| q-214 | DAN-093 | 3 | não | sim | find → search | sim | sim | 3 | 34 |
| q-215 | DAN-093 | 3 | não | sim | find → search | sim | sim | 3 | 34 |
| q-216 | DAN-106 | 1 | não | sim | find → search | sim | sim | 3 | 5 |

## q-207 (esperado: DAN-085)

- busca inicial: 
- justificativa: 
- aprofundar DAN-085: `SHA-1 collision deduplication checkout consistency check root cause remediation fix` — DAN-085 descreve exatamente um repositório de código (Subversion com deduplicação) que ficou indisponível após commits de arquivos de teste com mesmo SHA-1, fazendo checkout falhar consistência — igual ao incidente atual. Preciso da causa raiz e correção detalhadas.
- novos incidentes nos achados: DAN-085, DAN-164, DAN-050, DAN-157, DAN-055, DAN-173, DAN-097, DAN-129, DAN-078, DAN-130, DAN-190, DAN-073, DAN-049, DAN-029
  - DAN-085 (llm) [Problem Statement] 0.685: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.683: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-208 (esperado: DAN-086)

- busca inicial: 
- justificativa: 
- aprofundar DAN-086: `root cause fix leap year certificate expiration February 29 invalid date remediation` — É o único incidente que corresponde exatamente: certificado criado com data de vencimento em 29 de fevereiro do ano seguinte (inválida), rejeitado, causando falha global de serviço no dia bissexto, exatamente como o incidente atual de 29 de fevereiro com certificados rejeitados e criação de instâncias falhando.
- novos incidentes nos achados: DAN-086, DAN-015, DAN-090, DAN-191, DAN-154, DAN-221, DAN-103, DAN-210, DAN-142, DAN-016, DAN-049, DAN-087, DAN-010, DAN-217, DAN-009
  - DAN-086 (llm) [The Leap Day Bug] 0.612: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.563: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-209 (esperado: DAN-086)

- busca inicial: 
- justificativa: 
- aprofundar DAN-086: `root cause fix certificate expiration February 29 2012 leap year code bug` — É o único incidente que bate diretamente: certificados rejeitados por data inválida em 29 de fevereiro (ano bissexto), afetando toda a plataforma — exatamente o sintoma do incidente atual. Outros resultados tratam de expiração de certificado em datas comuns, falhas de DNS, upgrades de Kubernetes e erros de deploy, sem relação com 29 de fevereiro.
- novos incidentes nos achados: DAN-086, DAN-129, DAN-210, DAN-103, DAN-029, DAN-154, DAN-049, DAN-090, DAN-189, DAN-015, DAN-010, DAN-142, DAN-039, DAN-026, DAN-017
  - DAN-086 (llm) [The Leap Day Bug] 0.6: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.573: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-210 (esperado: DAN-088)

- busca inicial: 
- justificativa: 
- aprofundar DAN-088: `leap second deadlock xtime_lock printk klogd root cause fix` — É exatamente o mesmo sintoma: vários servidores Linux travaram simultaneamente na virada do leap second, com causa raiz no kernel (deadlock em xtime_lock durante o tratamento do leap second).
- aprofundar DAN-089: `leap second futex hrtimer CLOCK_REALTIME rewind root cause fix 2012` — Também é um incidente de leap second afetando muitos sistemas Linux simultaneamente, embora o mecanismo (futex/hrtimer) seja diferente do deadlock do DAN-088.
- aprofundar DAN-087: `leap second backwards time flow DNS panic root cause fix` — É outro incidente de leap second, mas afeta o DNS da Cloudflare (aplicação Go), não servidores Linux travando no kernel.
- novos incidentes nos achados: DAN-088, DAN-103, DAN-129, DAN-066, DAN-209, DAN-089, DAN-189, DAN-116, DAN-087, DAN-064, DAN-126, DAN-073, DAN-069, DAN-151, DAN-154
  - DAN-088 (llm) [sem seção] 0.809: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.77: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.812: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.744: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.239: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [sem seção] 0.733: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (llm) [Timeline] 0.698: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is
  - DAN-087 (causa) [A little bit about Cloudflare DNS] 0.331: ### A little bit about Cloudflare DNS  Cloudflare customers use our DNS service to serve the authoritative answers for DNS queries for their domains. They need to tell us the IP address of their origi
  - DAN-087 (correcao) [The one character fix] 0.332: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (correcao) [A falsehood programmers believe about time] 0.251: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe

## q-211 (esperado: DAN-088)

- busca inicial: 
- justificativa: 
- aprofundar DAN-088: `leap second deadlock xtime_lock printk klogd root cause fix` — É exatamente o incidente descrito: muitos servidores Linux travaram simultaneamente no leap second, com deadlock no xtime_lock causado por printk/klogd no handler do timer interrupt.
- aprofundar DAN-089: `leap second CLOCK_REALTIME hrtimer offset futex spinwait high load root cause fix` — Também é um incidente de leap second afetando muitos sistemas Linux simultaneamente, mas por um mecanismo diferente (timers expirando cedo e spinwait de futex), o que é uma causa raiz alternativa para o mesmo sintoma.
- novos incidentes nos achados: DAN-088, DAN-103, DAN-129, DAN-073, DAN-026, DAN-116, DAN-205, DAN-209, DAN-064, DAN-066, DAN-087, DAN-089, DAN-189, DAN-126, DAN-208
  - DAN-088 (llm) [sem seção] 0.809: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.77: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.806: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.725: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti

## q-212 (esperado: DAN-092)

- busca inicial: 
- justificativa: 
- aprofundar DAN-092: `root cause stale statistics missing indexes disk reads after database upgrade cutover fix re-promote old database run ANALYZE` — O resumo já mostra um padrão muito próximo ao incidente atual: cutover para banco de workflows atualizado, latência disparada, consultas lendo tudo do disco por estatísticas/planner desatualizadas, e jobs descartados. Preciso confirmar a causa raiz exata e a correção dentro do incidente.
- aprofundar DAN-133: `root cause slow queries MongoDB replica sets build queue workflow latency fix thread connection pools upsizing MongoDB` — Também envolve latência de workflows e banco, mas o gatilho é uma atualização de JVM que encolheu pools de conexão, não um cutover de banco com leitura em disco; ainda vale verificar se há paralelismo na correção.
- novos incidentes nos achados: DAN-092, DAN-103, DAN-133, DAN-134, DAN-080, DAN-209, DAN-195, DAN-101, DAN-148, DAN-035, DAN-164, DAN-146, DAN-186, DAN-125, DAN-130
  - DAN-092 (llm) [What Happened] 0.738: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.596: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-133 (llm) [Incident Report] 0.721: ## Incident Report  April 10, 2019 at 13:25 UTC we were alerted to sharp increases in multiple queues responsible for job and workflow processing. Our monitoring of MongoDB showed some issues, but not
  - DAN-133 (llm) [Incident Report] 0.685: ## Incident Report  Perhaps most importantly, MongoDB support pointed us at the `tcmalloc.spinlock_total_delay_ns` MongoDB stat. This stat correlates with the time spent on database operations blocked
  - DAN-133 (causa) [Incident Report] 0.453: ## Incident Report  Between March 26 and April 10, 2019, our platform experienced instability and downtime primarily due to issues with the datastore backing our builds queue. These datastore issues r
  - DAN-133 (correcao) [Incident Report] 0.533: ## Incident Report  Ultimately, refactoring the way we store and access portions of our data set in MongoDB will reduce load. Improving our data access and storage at the application level is one of o
  - DAN-133 (correcao) [Incident Report] 0.47: ## Incident Report  Around the same time, we updated many services to a new minor version of the JVM to pick up security changes. This update also included improvements for docker-awareness enabled by

## q-213 (esperado: DAN-092)

- busca inicial: 
- justificativa: 
- aprofundar DAN-092: `root cause stale statistics ANALYZE index not used after database upgrade cutover fix` — É o único que combina cutover de banco de workflows, queries lendo tudo do disco, latência alta e jobs sendo dropped após upgrade.
- aprofundar DAN-003: `database field type change job distribution service schema validation rollback recovery` — Também envolve banco e distribuição de jobs, mas o sintoma é validação de schema, não leitura total de disco nem cutover de versão maior.
- novos incidentes nos achados: DAN-092, DAN-133, DAN-164, DAN-134, DAN-080, DAN-148, DAN-101, DAN-078, DAN-130, DAN-096, DAN-195, DAN-102, DAN-156, DAN-188, DAN-003
  - DAN-092 (llm) [What Happened] 0.745: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.595: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-003 (llm) [What happened] 0.669: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Background] 0.518: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.348: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe

## q-214 (esperado: DAN-093)

- busca inicial: 
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover cold buffer pool wrong owner data drift cross-account` — É o único que une migração de schema + failover do MySQL + registros roteados para contas erradas, exatamente o padrão do incidente atual (migração provocou failover e usuários veem dados de outras contas).
- aprofundar DAN-048: `RDS MySQL failover configuration data loss financial system` — Envolve failover do MySQL após incidente de infraestrutura, mas o resumo não menciona migração de schema nem vazamento entre contas; serve como contra-exemplo.
- aprofundar DAN-078: `MySQL master failover network partition maintenance missing writes data integrity` — Trata de failover do MySQL durante manutenção, mas sem relação com migração de schema nem dados expostos para usuários errados.
- novos incidentes nos achados: DAN-048, DAN-078, DAN-093, DAN-094, DAN-003, DAN-190, DAN-164, DAN-096, DAN-186, DAN-058, DAN-056, DAN-155, DAN-194, DAN-162, DAN-043
  - DAN-093 (llm) [Monday, September 10th] 0.669: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.548: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.368: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member
  - DAN-048 (llm) [Incorrect configuration variable] 0.786: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Data loss] 0.774: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-048 (causa) [Final thoughts] 0.515: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Replication failure] 0.351: ## Replication failure  So, we had no other option but wait for the snapshots to finish and keep monitoring the master instance in the meantime. We waited six hours for the snapshot to complete and on
  - DAN-078 (llm) [Incident timeline] 0.706: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [Next steps] 0.642: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [Communication] 0.474: ## Communication  In our desire to communicate meaningful information to you during the incident, we made several public estimates on time to repair based on the rate of processing of the backlog of d

## q-215 (esperado: DAN-093)

- busca inicial: 
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover wrong tenant records cross-account data exposure root cause fix` — É o único resultado que envolve schema migration + MySQL failover + registros roteados para os proprietários errados, bem parecido com o incidente atual de usuários vendo registros de outras contas.
- novos incidentes nos achados: DAN-048, DAN-078, DAN-093, DAN-003, DAN-164, DAN-094, DAN-096, DAN-186, DAN-080, DAN-056, DAN-058, DAN-099, DAN-181, DAN-066, DAN-043
  - DAN-093 (llm) [Monday, September 10th] 0.598: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.578: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.368: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-216 (esperado: DAN-106)

- busca inicial: 
- justificativa: 
- aprofundar DAN-106: `root cause routine networking upgrade block storage volumes freeze instances stopped region fix` — É o único que combina atualização de rede de rotina com impacto regional em volumes de armazenamento em bloco e instâncias. DAN-073 é apenas uma falha de volume isolada, e os demais não envolvem atualização de rede nem congelamento regional de volumes.
- aprofundar DAN-043: `root cause automatic upgrade network rules removed Kubernetes clusters outage fix` — Também envolve uma atualização (automática) que removeu regras de rede e derrubou clusters em múltiplas regiões, mas o componente é orquestração Kubernetes, não armazenamento em bloco, e não há menção a volumes congelados.
- aprofundar DAN-107: `root cause storage server memory leak EBS outage failover fix October 2012 US-East` — Envolve servidores de armazenamento EBS e outage regional, mas o gatilho é um vazamento de memória no agente de reporting, não uma atualização de rede, e não há descrição de volumes travados durante manutenção de rede.
- novos incidentes nos achados: DAN-106, DAN-073, DAN-048, DAN-164, DAN-109, DAN-071, DAN-191, DAN-064, DAN-139, DAN-060, DAN-208, DAN-107, DAN-143, DAN-134, DAN-188
- aviso: DAN-043 não está entre os incidentes encontrados; ignorado.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.622: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.601: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  A large majority of the volumes in the degraded EBS cluster were still functioning properly and the focus was to 
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-107 (llm) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.77: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  The memory pressure on many of the EBS servers had reached a point where EBS servers began losing the ability to process cu
  - DAN-107 (llm) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.748: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  We have deployed monitoring that will alarm if we see this specific memory leak again in any of our production EBS servers,
  - DAN-107 (causa) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.413: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Last week, one of the data collection servers in the affected Availability Zone had a hardware failure and was replaced. As
  - DAN-107 (correcao) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.407: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Normally these events are simultaneous. Between the period of time the masters were disconnected from their standbys and th
  - DAN-107 (correcao) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.399: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Unfortunately, a bug in the traffic shifting functionality incorrectly mapped a small number of the affected load balancers
