# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-207 | DAN-085 | 1 | não | sim | find → search | sim | sim | 2 | 12 |
| q-208 | DAN-086 | 1 | não | sim | find → search | sim | sim | 2 | 10 |
| q-209 | DAN-086 | 1 | não | sim | find → search | sim | sim | 2 | 109 |
| q-210 | DAN-088 | 1 | não | sim | find → search | sim | sim | 2 | 14 |
| q-211 | DAN-088 | 1 | não | sim | find → search | sim | sim | 2 | 110 |
| q-212 | DAN-092 | 1 | não | sim | find → search | sim | sim | 2 | 10 |
| q-213 | DAN-092 | 1 | não | sim | find → search | sim | sim | 2 | 14 |
| q-214 | DAN-093 | 3 | não | sim | find → search | sim | sim | 2 | 75 |
| q-215 | DAN-093 | 3 | não | sim | find → search | sim | sim | 2 | 46 |
| q-216 | DAN-106 | 1 | não | sim | find → search | sim | sim | 2 | 99 |

## q-207 (esperado: DAN-085)

- busca inicial: 
- justificativa: 
- aprofundar DAN-085: `root cause SHA1 collision test files consistency check failure fix remediation Subversion repository` — O incidente bate com o atual: repositório de código indisponível, checkout falha na consistência, ocorrido logo após commit com arquivos de teste. O componente (repositório VCS) e o gatilho (commit com test files) coincidem.
- novos incidentes nos achados: DAN-085, DAN-164, DAN-050, DAN-157, DAN-055, DAN-173, DAN-097, DAN-129, DAN-078, DAN-130, DAN-190, DAN-029, DAN-142, DAN-049
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.754: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (llm) [Final note] 0.749: ## Final note  These interpretations of the problem and its severity are obviously my own. I have tried to explain the problem, how to prevent it, and how to resolve it, as accurately as possible as w
  - DAN-085 (causa) [Problem Statement] 0.287: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-208 (esperado: DAN-086)

- busca inicial: 
- justificativa: 
- aprofundar DAN-086: `root cause certificate expiration February 29 fix leap year date computation` — Este incidente é de 29 de fevereiro, envolve certificados rejeitados por data de expiração inválida e causou interrupção global da plataforma, batendo exatamente com o sintoma e a data do incidente atual.
- novos incidentes nos achados: DAN-086, DAN-015, DAN-090, DAN-191, DAN-154, DAN-221, DAN-103, DAN-210, DAN-142, DAN-016, DAN-218, DAN-049, DAN-066, DAN-189, DAN-026
  - DAN-086 (llm) [The Leap Day Bug] 0.635: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.546: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-209 (esperado: DAN-086)

- busca inicial: 
- justificativa: 
- aprofundar DAN-086: `root cause certificate expiration February 29 2013 fix workaround` — Bate exatamente: falha em 29 de fevereiro, certificados rejeitados por data de expiração inválida (29/02/2013 não existe), criação de instâncias falhando e impacto em toda a plataforma. Difere apenas pelo ano (2012 vs atual) e pelo provedor (Azure).
- novos incidentes nos achados: DAN-086, DAN-129, DAN-210, DAN-103, DAN-029, DAN-154, DAN-049, DAN-090, DAN-189, DAN-015, DAN-087, DAN-142, DAN-083, DAN-219, DAN-058
  - DAN-086 (llm) [The Leap Day Bug] 0.547: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.511: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-210 (esperado: DAN-088)

- busca inicial: 
- justificativa: 
- aprofundar DAN-088: `leap second deadlock xtime_lock printk klogd fix` — Mesmo gatilho (leap second) e mesmo componente (Linux kernel); sintoma de servidores travando por deadlock é muito parecido com o incidente atual.
- aprofundar DAN-089: `leap second futex hrtimer base.offset fix patch` — Mesmo gatilho (leap second 2012) e sintoma de alta carga/serviços caindo em muitos sistemas; componente é o Linux kernel, batendo com o incidente atual.
- novos incidentes nos achados: DAN-088, DAN-103, DAN-129, DAN-066, DAN-209, DAN-089, DAN-189, DAN-116, DAN-087, DAN-064, DAN-073, DAN-151, DAN-230, DAN-026, DAN-126
  - DAN-088 (llm) [sem seção] 0.798: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.766: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.761: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.721: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti

## q-211 (esperado: DAN-088)

- busca inicial: 
- justificativa: 
- aprofundar DAN-088: `leap second xtime_lock deadlock printk klogd fix` — Incidente atual envolve leap second travando servidores Linux; DAN-088 descreve deadlock por xtime_lock durante leap second, muito similar.
- aprofundar DAN-089: `leap second CLOCK_REALTIME hrtimer futex spinwait patch fix` — DAN-089 também trata de leap second no Linux causando pane em serviços, com causa raiz em CLOCK_REALTIME e hrtimer.
- novos incidentes nos achados: DAN-088, DAN-103, DAN-129, DAN-073, DAN-026, DAN-116, DAN-205, DAN-209, DAN-064, DAN-066, DAN-089, DAN-087, DAN-230, DAN-189, DAN-173
  - DAN-088 (llm) [sem seção] 0.792: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.761: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (causa) [sem seção] 0.328: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.809: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.782: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti

## q-212 (esperado: DAN-092)

- busca inicial: 
- justificativa: 
- aprofundar DAN-092: `root cause stale statistics indexes disk reads fix ANALYZE re-promote old database` — É o único que bate em todos os pontos: cutover do banco de workflows, queries lendo tudo do disco, latência alta e jobs descartados depois do retry; a causa (estatísticas/índices obsoletos após upgrade major) e a correção (re-promover o banco antigo) são exatamente o que o diagnóstico precisa.
- novos incidentes nos achados: DAN-092, DAN-103, DAN-133, DAN-134, DAN-080, DAN-209, DAN-195, DAN-101, DAN-148, DAN-035, DAN-164, DAN-219, DAN-094, DAN-156, DAN-091
  - DAN-092 (llm) [What Happened] 0.693: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.534: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers

## q-213 (esperado: DAN-092)

- busca inicial: 
- justificativa: 
- aprofundar DAN-092: `root cause fix ANALYZE statistics stale planner indexes disk reads after database upgrade cutover` — Bate em quase tudo: cutover de banco de workflows, queries lendo do disco, latência alta e jobs sendo dropped após upgrade. Difere apenas no detalhe de ser blue/green e estatísticas estarem desatualizadas.
- novos incidentes nos achados: DAN-092, DAN-133, DAN-164, DAN-134, DAN-080, DAN-148, DAN-101, DAN-078, DAN-130, DAN-096, DAN-186, DAN-209, DAN-190, DAN-195, DAN-091
  - DAN-092 (llm) [What Happened] 0.708: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [What Happened] 0.575: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (causa) [Summary] 0.393: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-092 (correcao) [Future Prevention and Process Improvement] 0.483: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru

## q-214 (esperado: DAN-093)

- busca inicial: 
- justificativa: 
- aprofundar DAN-093: `schema migration failover stale node data drift wrong owners root cause fix` — O incidente envolve migração de schema que causou failover do MySQL e dados roteados para proprietários errados, semelhante a usuários vendo registros de outras contas.
- aprofundar DAN-078: `MySQL master failover maintenance network partition data integrity root cause fix` — Envolve failover do MySQL durante manutenção com problemas de integridade de dados, embora o gatilho seja partição de rede e não migração de schema.
- novos incidentes nos achados: DAN-048, DAN-078, DAN-093, DAN-094, DAN-003, DAN-190, DAN-164, DAN-096, DAN-186, DAN-058, DAN-056, DAN-066, DAN-194, DAN-043, DAN-146
  - DAN-093 (llm) [Monday, September 10th] 0.628: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.61: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member
  - DAN-078 (llm) [Incident timeline] 0.686: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.639: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa

## q-215 (esperado: DAN-093)

- busca inicial: 
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover stale node wrong owner root cause fix remediation` — É o único que combina schema migration → failover do MySQL → usuários vendo registros de outras contas (repositórios privados roteados para donos errados), exatamente o padrão do incidente atual.
- novos incidentes nos achados: DAN-048, DAN-078, DAN-093, DAN-003, DAN-164, DAN-094, DAN-096, DAN-186, DAN-080, DAN-056, DAN-058, DAN-155, DAN-099, DAN-181, DAN-162
  - DAN-093 (llm) [Monday, September 10th] 0.676: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.646: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-216 (esperado: DAN-106)

- busca inicial: 
- justificativa: 
- aprofundar DAN-106: `routine networking upgrade human error volume loss root cause fix` — Bate muito com o incidente atual: atualização de rede de rotina, erro humano, pane regional e perda de volumes. Difere porque é da Amazon EC2/RDS, não especificamente block storage travar instâncias.
- aprofundar DAN-143: `automatic upgrade network rules removed outage fix remediation` — Semelhança: upgrade de rede automático causando pane em múltiplas regiões. Difere: remove regras de rede em vez de travar volumes de bloco, e afeta clusters Kubernetes, não instâncias diretas.
- aprofundar DAN-109: `network disruption storage nodes down root cause fix` — Semelhança: problema de rede derrubando nós de armazenamento. Difere: é uma disruption de rede, não uma atualização planejada de rotina, e foca em DynamoDB metadata, não EBS/block storage.
- novos incidentes nos achados: DAN-106, DAN-073, DAN-048, DAN-164, DAN-109, DAN-071, DAN-191, DAN-064, DAN-139, DAN-060, DAN-143, DAN-208, DAN-065, DAN-189, DAN-063
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.456: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.452: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-143 (llm) [Root cause] 0.628: ## Root cause  We have identified (and since disabled) the initial trigger for the outage: on March 8, 2023, at 06:00 UTC, a security update to systemd was automatically applied to a number of VMs, wh
  - DAN-143 (llm) [Root cause] 0.553: ## Root cause  However, the base OS image we use to run Kubernetes had a legacy security update channel enabled, which caused the update to apply automatically. By design we use fairly minimal base OS
  - DAN-143 (causa) [Lessons learned] 0.422: ## Lessons learned  The following is not the sum total of everything we learned during the incident but rather important themes that pertain to the whole platform.  This was our first global incident.
  - DAN-143 (correcao) [Lessons learned] 0.446: ## Lessons learned  Even with separate systems that serve live data when historical data is not accessible (e.g., APM’s Live Search and Log Management’s Live Tail), we did not provide our customers wi
  - DAN-143 (correcao) [Recovery] 0.445: ## Recovery  The high-level steps of the recovery had to be sequenced because of the magnitude of the compute capacity drop:  - First, for each region, recover enough compute capacity so that it could
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.561: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.545: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  The specific assignment of a group of partitions to a given server is called a “membership.” The member
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.368: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.407: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
