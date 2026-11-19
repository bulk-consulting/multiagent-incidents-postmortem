# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-207 | DAN-085 | 1 | não | sim | find → search | sim | sim | 2 | 6 |
| q-208 | DAN-086 | 1 | não | sim | find → search | sim | sim | 2 | 34 |
| q-209 | DAN-086 | 1 | não | sim | find → search | sim | sim | 2 | 41 |
| q-210 | DAN-088 | 1 | não | sim | find → search | sim | sim | 2 | 47 |
| q-211 | DAN-088 | 1 | não | sim | find → search | sim | sim | 2 | 7 |
| q-212 | DAN-092 | 1 | não | sim | find → search | sim | sim | 2 | 6 |
| q-213 | DAN-092 | 1 | não | sim | find → search | sim | sim | 2 | 41 |
| q-214 | DAN-093 | 3 | não | sim | find → search | sim | sim | 2 | 43 |
| q-215 | DAN-093 | 3 | não | sim | find → search | sim | sim | 2 | 76 |
| q-216 | DAN-106 | 1 | não | sim | find → search | sim | sim | 2 | 42 |

## q-207 (esperado: DAN-085)

- busca inicial: 
- justificativa: 
- aprofundar DAN-085: `SHA1 collision deduplication test files consistency check root cause fix remediation` — Bate com o incidente atual: repositório de código indisponível, checkout falha na consistência, logo após commit com arquivos de teste. Os outros resultados são falhas de banco de dados/infra e não correspondem ao sintoma.
- novos incidentes nos achados: DAN-085, DAN-164, DAN-050, DAN-157, DAN-055, DAN-173, DAN-097, DAN-129, DAN-078, DAN-130, DAN-190, DAN-073, DAN-029, DAN-099, DAN-161
  - DAN-085 (llm) [Problem Statement] 0.688: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.663: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-208 (esperado: DAN-086)

- busca inicial: 
- justificativa: 
- aprofundar DAN-086: `root cause fix certificate expiration February 29 2013 invalid date leap year code current date plus one year` — Bate com o incidente atual: certificados rejeitados e falha na criação de instâncias em 29 de fevereiro, causado por bug de ano bissexto no cálculo de validade de certificados. Não bate: plataforma é Azure, não a mesma do incidente atual.
- novos incidentes nos achados: DAN-086, DAN-015, DAN-090, DAN-191, DAN-154, DAN-221, DAN-103, DAN-210, DAN-142, DAN-016, DAN-087, DAN-116, DAN-010, DAN-053, DAN-029
  - DAN-086 (llm) [The Leap Day Bug] 0.626: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.545: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-209 (esperado: DAN-086)

- busca inicial: 
- justificativa: 
- aprofundar DAN-086: `root cause certificate expiration February 29 leap year fix solution` — Este incidente é quase idêntico ao atual: falha de certificados e criação de instâncias em 29 de fevereiro, causada por cálculo incorreto de 'um ano' que gerou data de expiração inválida em 29 de fevereiro de 2013.
- novos incidentes nos achados: DAN-086, DAN-129, DAN-210, DAN-103, DAN-029, DAN-154, DAN-049, DAN-090, DAN-189, DAN-015, DAN-087, DAN-142, DAN-088, DAN-053
  - DAN-086 (llm) [The Leap Day Bug] 0.617: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.545: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-210 (esperado: DAN-088)

- busca inicial: 
- justificativa: 
- aprofundar DAN-088: `leap second deadlock xtime_lock printk klogd root cause fix` — Bate: leap second no kernel Linux fazendo servidores travarem/ficarem inativos por deadlock. Não bate: é um deadlock específico de timer interrupt, não descrito como congelamento geral do servidor.
- aprofundar DAN-089: `leap second futex CLOCK_REALTIME hrtimer offset fix patch root cause` — Bate: leap second afetando muitos sistemas Linux simultaneamente, causando alta carga e queda de serviços web. Não bate: o sintoma é spinwait/carga alta, não exatamente travamento total dos servidores.
- aprofundar DAN-087: `leap second time.Now monotonic DNS resolver panic negative value fix` — Bate: falha em massa provocada pelo retrocesso do horário no leap second. Não bate: é específico do DNS/Go do Cloudflare, não servidores Linux genéricos travando.
- novos incidentes nos achados: DAN-088, DAN-103, DAN-129, DAN-066, DAN-209, DAN-089, DAN-189, DAN-116, DAN-087, DAN-064, DAN-073, DAN-151, DAN-230, DAN-026, DAN-170
  - DAN-088 (llm) [sem seção] 0.809: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.77: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.825: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.735: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.239: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.742: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe
  - DAN-087 (llm) [The one character fix] 0.713: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (causa) [sem seção] 0.385: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (correcao) [Timeline] 0.444: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is
  - DAN-087 (correcao) [A little bit about Cloudflare DNS] 0.318: ### A little bit about Cloudflare DNS  Cloudflare customers use our DNS service to serve the authoritative answers for DNS queries for their domains. They need to tell us the IP address of their origi

## q-211 (esperado: DAN-088)

- busca inicial: 
- justificativa: 
- aprofundar DAN-088: `xtime_lock deadlock leap second timer interrupt printk klogd fix` — Corresponde diretamente: segundo bissexto, servidores Linux travando, deadlock no timer interrupt com xtime_lock.
- aprofundar DAN-089: `leap second futex hrtimer base offset CLOCK_REALTIME fix patch` — Corresponde: segundo bissexto causando problemas de timer/futex em sistemas Linux e quedas de serviços em larga escala.
- novos incidentes nos achados: DAN-088, DAN-103, DAN-129, DAN-073, DAN-026, DAN-116, DAN-205, DAN-209, DAN-064, DAN-066, DAN-089, DAN-087, DAN-230, DAN-126, DAN-189
  - DAN-088 (llm) [sem seção] 0.809: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.751: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (causa) [sem seção] 0.328: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.827: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.745: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.239: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti

## q-212 (esperado: DAN-092)

- busca inicial: 
- justificativa: 
- aprofundar DAN-092: `root cause stale statistics missing indexes disk reads after cutover fix re-promote blue database` — Corresponde fortemente ao incidente atual: cutover de banco de workflows, latência disparou, consultas lendo do disco e jobs descartados; diferente dos demais que envolvem MongoDB, RabbitMQ, DNS ou migração genérica sem sintoma de leitura em disco.
- novos incidentes nos achados: DAN-092, DAN-103, DAN-133, DAN-134, DAN-080, DAN-209, DAN-195, DAN-101, DAN-148, DAN-035, DAN-186, DAN-078, DAN-164, DAN-096, DAN-162
  - DAN-092 (llm) [What Happened] 0.703: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.579: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers

## q-213 (esperado: DAN-092)

- busca inicial: 
- justificativa: 
- aprofundar DAN-092: `statistics tables stale ANALYZE planner indexes disk reads re-promote blue database` — É o mais parecido: upgrade/cutover do banco de workflows, queries lendo tudo do disco, latência disparou e jobs foram descartados após retry. A causa (estatísticas desatualizadas após upgrade de versão major) e a correção (re-promover o banco antigo) batem diretamente com o incidente atual.
- novos incidentes nos achados: DAN-092, DAN-133, DAN-164, DAN-134, DAN-080, DAN-148, DAN-101, DAN-078, DAN-130, DAN-096, DAN-195, DAN-219, DAN-180, DAN-125, DAN-209
  - DAN-092 (llm) [What Happened] 0.653: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.59: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers

## q-214 (esperado: DAN-093)

- busca inicial: 
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover wrong owner data drift root cause fix` — Bate muito com o incidente atual: schema migration provocou failover do MySQL e usuários viram dados de outros donos (registros de outras contas). Diferença: lá foi Percona Replication Manager e buffer pool frio, aqui o gatilho é a migração de schema em si.
- aprofundar DAN-078: `MySQL master failover data integrity restoration root cause fix` — Envolve failover inesperado do MySQL com problemas de integridade de dados após manutenção, mas o gatilho foi partição de rede, não schema migration. Útil para comparar o padrão de failover → dados incorretos.
- novos incidentes nos achados: DAN-048, DAN-078, DAN-093, DAN-094, DAN-003, DAN-190, DAN-164, DAN-096, DAN-186, DAN-058, DAN-056, DAN-162, DAN-155, DAN-043, DAN-091
  - DAN-093 (llm) [Monday, September 10th] 0.671: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.593: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.368: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.687: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [Next steps] 0.64: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (causa) [Incident timeline] 0.478: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [2018 October 22 16:24 UTC] 0.479: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 

## q-215 (esperado: DAN-093)

- busca inicial: 
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover stale node data drift wrong owners root cause fix` — O único incidente que combina migração de schema, failover do MySQL e usuários acessando dados de outros proprietários (repositórios privados roteados para donos errados), exatamente o padrão do incidente atual.
- novos incidentes nos achados: DAN-048, DAN-078, DAN-093, DAN-003, DAN-164, DAN-094, DAN-096, DAN-186, DAN-080, DAN-056, DAN-058, DAN-043, DAN-146, DAN-175, DAN-162
  - DAN-093 (llm) [Monday, September 10th] 0.677: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.632: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-216 (esperado: DAN-106)

- busca inicial: 
- justificativa: 
- aprofundar DAN-106: `root cause fix human error networking upgrade resource crunch EBS volumes outage` — Bate muito com o incidente atual: upgrade de rede de rotina, impacto regional em todas as AZs e volumes de storage afetados. Difere pelo detalhe de perda de 0.07% de volumes em vez de travamento total.
- aprofundar DAN-109: `root cause fix network disruption metadata service load storage nodes shut down retry` — Bate pelo gatilho de rede causando problema em storage nodes em escala regional. Difere por ser DynamoDB/metadata, não exatamente volumes em bloco de instâncias EC2.
- novos incidentes nos achados: DAN-106, DAN-073, DAN-048, DAN-164, DAN-109, DAN-071, DAN-191, DAN-064, DAN-139, DAN-060, DAN-063, DAN-209, DAN-208, DAN-107, DAN-143
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.646: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.646: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.394: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.663: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.65: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was
