# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | sim | sim | search | não | sim | 0 | 512 |
| q-022 | DAN-104 | 4 | sim | sim | search | não | sim | 0 | 204 |
| q-170 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 193 |
| q-171 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 190 |
| q-222 | DAN-121 | 4 | sim | sim | search | não | sim | 0 | 196 |
| q-240 | DAN-152 | 4 | sim | sim | search | não | sim | 0 | 191 |
| q-012 | DAN-211 | 5 | sim | sim | search | não | sim | 0 | 186 |
| q-263 | DAN-200 | 5 | sim | sim | search | não | sim | 0 | 213 |
| q-032 | DAN-104 | 7 | sim | sim | search | não | sim | 0 | 179 |
| q-219 | DAN-116 | 7 | sim | sim | search | não | sim | 0 | 203 |
| q-223 | DAN-121 | 8 | sim | sim | search | não | sim | 0 | 181 |
| q-218 | DAN-116 | 9 | sim | sim | search | não | sim | 0 | 178 |
| q-229 | DAN-125 | 10 | sim | sim | search | não | sim | 0 | 176 |
| q-262 | DAN-200 | 10 | sim | sim | search | não | sim | 0 | 499 |
| q-228 | DAN-125 | 11 | não | não | search [1 malformada] [1 JSON consertado] | não | não | 0 | 173 |
| q-034 | DAN-004 | 12 | não | não | search | não | não | 0 | 174 |
| q-243 | DAN-154 | 12 | não | não | search | não | não | 0 | 178 |
| q-260 | DAN-197 | 19 | não | não | search | não | não | 0 | 173 |
| q-242 | DAN-154 | — | não | não | search | não | não | 0 | 179 |
| q-261 | DAN-197 | — | não | não | search | não | não | 0 | 159 |

## q-020 (esperado: DAN-164)

- busca inicial: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-091, DAN-186, DAN-092, DAN-066, DAN-058
- justificativa: 
- aprofundar DAN-043: `accidental delete production database backup restore` — Bate pela eliminação acidental do banco de produção e pela recuperação a partir de backup; não envolve falhas de infraestrutura.
- aprofundar DAN-164: `admin deleted wrong directory data loss recovery` — Bate pela eliminação acidental de arquivo de banco de produção e pela recuperação via restauração de backup; similar erro humano.
- aprofundar DAN-056: `environment variable truncate production database recovery` — Bate pela perda de dados causada por variável de ambiente, embora seja via pipeline CI em vez de manutenção direta.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.723: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.667: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [sem seção] 0.553: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (llm) [Root cause analysis] 0.544: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.732: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.701: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-022 (esperado: DAN-104)

- busca inicial: DAN-191, DAN-189, DAN-146, DAN-104, DAN-064, DAN-067, DAN-073, DAN-109, DAN-209, DAN-103
- justificativa: 
- aprofundar DAN-189: `operator typo reboot all servers outage fix` — o operador executou um comando com erro de sintaxe que reiniciou todos os servidores, semelhante ao comando de remoção na situação atual; causou queda dependente, embora seja reboot em vez de remoção.
- aprofundar DAN-104: `operator typo remove servers storage outage fix` — exatamente operador executou comando com erro tipográfico, removendo múltiplos servidores de armazenamento crítica, resultando em queda de serviços dependentes; root cause e correção estão diretamente relacionados.
  - DAN-189 (llm) [What Happened?] 0.688: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [What Happened?] 0.598: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (causa) [Next Steps] 0.434: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.455: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.448: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q-170 (esperado: DAN-018)

- busca inicial: DAN-144, DAN-066, DAN-017, DAN-018, DAN-029, DAN-191, DAN-102, DAN-037, DAN-067, DAN-154
- justificativa: 
- aprofundar DAN-018: `dashboard infinite API calls thundering herd fix` — Envolve o painel frontend fazendo muitas chamadas à API, resultando em queda.
- aprofundar DAN-144: `flapping service thundering herd memory fix` — O serviço interno em flare causou comportamento em avalanche, semelhante ao fluxo excessivo de chamadas.
  - DAN-018 (llm) [Improving visibility] 0.691: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (llm) [Reducing impact] 0.637: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [What Happened] 0.343: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-144 (llm) [Summary] 0.5: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.481: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 

## q-171 (esperado: DAN-018)

- busca inicial: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-133, DAN-129, DAN-218, DAN-145, DAN-220
- justificativa: 
- aprofundar DAN-018: `React component dependency array excessive API calls` — O incidente descreve exatamente a falha de componente React no dashboard que gerou chamadas excessivas ao API, semelhante ao nosso problema de thundering herd após deploy frontend.
- aprofundar DAN-067: `thundering herd API calls overwhelming` — DAN-067 relata ocorrência de thundering herd após reativação de serviços, que coincide com nossa inundação de chamadas ao API.
- aprofundar DAN-144: `flapping service thundering herd` — DAN-144 apresenta serviço que flutua causando thundering herd; comparável ao Flooding backend após deploy.
  - DAN-018 (llm) [What Happened] 0.566: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.555: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-067 (llm) [Disaster Recovery] 0.605: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.527: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-144 (llm) [Summary] 0.471: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.42: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 

## q-222 (esperado: DAN-121)

- busca inicial: DAN-129, DAN-144, DAN-147, DAN-121, DAN-016, DAN-137, DAN-134, DAN-209, DAN-148, DAN-220
- justificativa: 
- aprofundar DAN-121: `database backend overloaded throttle requests timeout services player video` — Incidente reproduz exatamente nossa situação: backend sobrecarregado, throttling, timeouts e player de vídeo afetado.
- aprofundar DAN-147: `request queue overload insufficient database capacity cascading failure cause fix` — Relacionado a sobrecarga de banco e falhas em fluxos de requisição; pode conter lições sobre escalonamento.
  - DAN-121 (llm) [sem seção] 0.537: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.46: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.614: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.606: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-240 (esperado: DAN-152)

- busca inicial: DAN-009, DAN-175, DAN-140, DAN-152, DAN-177, DAN-015, DAN-017, DAN-124, DAN-131, DAN-028
- justificativa: 
- aprofundar DAN-175: `private token leak root cause fix` — Envolve vazamento de tokens privados, similar à nossa situação de token sendo enviado para fora, apesar de não ter sido publicado.
- aprofundar DAN-152: `malicious npm package root cause fix` — Categoria de pacote malicioso que pode enviar tokens, embora nosso pacote não tenha sido publicado;
- aprofundar DAN-177: `GitHub personal access token leak root cause fix` — Exemplo concreto de token de acesso privado vazado, fornecendo pistas sobre como ocorreu o vazamento.
  - DAN-175 (llm) [Incident Summary] 0.558: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (llm) [Incident Summary] 0.54: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro
  - DAN-152 (llm) [Summary] 0.686: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.683: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-177 (llm) [sem seção] 0.721: On 31st July 2018 a security researcher identified a GitHub personal access token with recently elevated scopes was leaked from Homebrew’s Jenkins that gave them access to git push on Homebrew/brew an
  - DAN-177 (llm) [What was impacted] 0.607: ## What was impacted  GitHub Support was contacted and they verified the relevant token had not been used to perform any pushes to Homebrew/brew or Homebrew/homebrew-core during the period of elevated
  - DAN-177 (causa) [What we’re doing about it] 0.231: ## What we’re doing about it  - We have for several years enabled 2FA and third party application restrictions for the entire Homebrew GitHub organisation. This was also recommended by the security re

## q-012 (esperado: DAN-211)

- busca inicial: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-066, DAN-222, DAN-113, DAN-101, DAN-133
- justificativa: 
- aprofundar DAN-020: `bad service discovery config cause writes timeout` — Relevante pois envolve falha no serviço de descoberta causando sobrecarga e falha nos escritos; se fosse diferente, deixaria de envolver o layer de discovery.
- aprofundar DAN-211: `Consul streaming performance slow writes timeout` — Relevante pois descreve degradação do Consul, camada de descoberta, e impacta outras rotinas; trecho menciona degradação de performance e timeouts.
- aprofundar DAN-109: `metadata services overload network disruption timeout fix` — Relevante pois discute perda de desempenho devido a serviços de metadados sobrecarregados que podem ser análogos ao slowdown do discovery; pode ter correções semelhantes.
  - DAN-020 (llm) [A thundering herd] 0.653: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (llm) [Setting the stage] 0.628: ## Setting the stage  However, there was one crucial exception which we never see during normal operations: NXDOMAIN answers are not cached by the resolver to quickly propagate service deregistration 
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Improve the resilience of service discovery] 0.401: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.635: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Why was streaming an issue? HashiCorp explained that, while streaming was overall more efficient, it used fewer concurrency control elements (Go chan
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.632: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (causa) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.489: ### Early Triage (10/28 13:37 – 10/29 02:00)  At this point, the team developed a new theory about what was going wrong: increased traffic. Perhaps Consul was slow because our system reached a tipping
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.649: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.629: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-263 (esperado: DAN-200)

- busca inicial: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-073, DAN-146, DAN-106, DAN-069, DAN-066
- justificativa: 
- aprofundar DAN-200: `priority inversion problem causing system resets days after operation fix` — Envolve computador a bordo redimensionando após alguns dias; causa no sistema operacional e solução de patch remoto.
- aprofundar DAN-198: `design flaw excess CPU load restart lunar landing fix` — Similar ao computador a bordo reiniciando, falha por carga de CPU no software embarcado, embora ocorra durante operação de aterrissagem.
  - DAN-200 (llm) [THE FAILURE] 0.681: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.565: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.693: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.657: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-032 (esperado: DAN-104)

- busca inicial: DAN-109, DAN-210, DAN-189, DAN-191, DAN-067, DAN-073, DAN-104, DAN-103, DAN-026, DAN-070
- justificativa: 
- aprofundar DAN-104: `human error removed servers typo storage outage` — Se refere a um comando de remoção de servidores que, devido a um erro de digitação, removou muitos servidores essenciais, resultando em queda do serviço de armazenamento. Coincide com o operador que executou um comando de remoção que acabou derrubando o armazenamento.
- aprofundar DAN-189: `operator reused tool missing -n rebooted all servers outage` — Mostra um operador que usou uma ferramenta com validação fraca, esqueceu a opção -n e reiniciou todos os servidores, gerando falha no serviço de armazenamento; similar à remoção inadvertida de vários servidores.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.492: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.487: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.664: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.622: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-219 (esperado: DAN-116)

- busca inicial: DAN-066, DAN-126, DAN-103, DAN-222, DAN-205, DAN-209, DAN-116, DAN-109, DAN-191, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update crash servers cause fix` — Encaixa exatamente: a atualização de banco de dados causou falha cega e todos os servidores de impressão foram trazidos para crash simultaneamente; não há menção de falha de rede ou rede de commits.
  - DAN-116 (llm) [sem seção] 0.717: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.632: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-223 (esperado: DAN-121)

- busca inicial: DAN-147, DAN-148, DAN-101, DAN-129, DAN-134, DAN-219, DAN-164, DAN-121, DAN-144, DAN-094
- justificativa: 
- aprofundar DAN-121: `database overload throttling requests curl` — Reconhece quorum de banco afetado, throttling e timeouts, semelhante a vídeo player falhando
- aprofundar DAN-147: `request queue overflow database capacity fix` — Envolve fila sobrecarregada, capacidade de banco insuficiente, causa similar de overload e timeouts
- aprofundar DAN-164: `influx requests overloaded database recovery` — Indica inflow de requisições que sobrecarregam o banco e soluções de alívio
  - DAN-121 (llm) [sem seção] 0.499: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.421: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.61: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.606: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Timeline] 0.622: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Timeline] 0.602: ## Timeline  On January 31st an engineer started setting up multiple PostgreSQL servers in our staging environment. The plan was to try out pgpool-II to see if it would reduce the load on our database
  - DAN-164 (causa) [Root cause analysis] 0.567: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-218 (esperado: DAN-116)

- busca inicial: DAN-126, DAN-146, DAN-103, DAN-066, DAN-209, DAN-106, DAN-048, DAN-191, DAN-116, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update servers crash` — Acerca de double free acionada por atualização de banco de dados que fez com que todos os servidores tivessem falha simultaneamente; corresponde ao cenário em que todos caíram após atualização de dados.
- aprofundar DAN-126: `bug fix timestamp data loss servers` — Afixação de bug no timestamp causou perda de dados em vários servidores; embora não realça falha simultânea, envolve update de dados e propagação a múltiplos servidores.
- aprofundar DAN-146: `scheduled OS upgrade wipe servers` — A atualização programada de OS foi o gatilho e se referiu a perda de serviços em vários servidores; similar ao efeito de update generalizado porém de nível de sistema.
  - DAN-116 (llm) [sem seção] 0.703: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.6: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-126 (llm) [Server Configurations] 0.637: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [Server Configurations] 0.597: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-146 (llm) [sem seção] 0.536: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [sem seção] 0.429: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri

## q-229 (esperado: DAN-125)

- busca inicial: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-129, DAN-091, DAN-125
- justificativa: 
- aprofundar DAN-147: `request queue overload insufficient capacity downgrade failure cascade` — Cascading failure due to insufficient database capacity after downsizing
- aprofundar DAN-125: `capacity downgrade load cascade failure database outage` — Database capacity downgrade led to lack of capacity at peak causing cascading collapse of dependent servers
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.616: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.592: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-125 (llm) [Database performance issues] 0.627: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.498: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l

## q-262 (esperado: DAN-200)

- busca inicial: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073, DAN-189, DAN-146, DAN-210, DAN-043, DAN-200
- justificativa: 
- aprofundar DAN-200: `priority inversion VxWorks OS task scheduling priority inheritance fix final patch` — Similar ao computador de bordo que reinicia após alguns dias de operação, e ambos envolvem falha de sistema operacional; diferente porque ocorre apenas em missão de Marte
- aprofundar DAN-198: `design flaw excessive CPU load computer restart Apollo 11 lunar landing` — Também um computador de bordo que reinicia, mas o gatilho é carga de CPU durante aterrissagem, não após dias de operação
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.673: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.65: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-200 (causa) [THE FAILURE] 0.577: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HUMAN NATURE, DEADLINE PRESSURES] 0.436: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-198 (llm) [sem seção] 0.725: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.701: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-228 (esperado: DAN-125)

- busca inicial: DAN-164, DAN-147, DAN-156, DAN-048, DAN-096, DAN-043, DAN-094, DAN-209, DAN-134, DAN-109
- justificativa: 
- aprofundar DAN-147: `request queue overloading database capacity insufficient scaling` — Falha de cascata por sobrecarga do banco devido a capacidade insuficiente, semelhante ao banco reduzido que não aguenta pico.
- aprofundar DAN-164: `influx requests overloaded database replication lag admin wrong directory` — Outage devido a excesso de requisições que esgotou a capacidade do banco
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.621: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.61: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Timeline] 0.67: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.655: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-034 (esperado: DAN-004)

- busca inicial: DAN-005, DAN-137, DAN-051, DAN-012, DAN-220, DAN-011, DAN-016, DAN-014, DAN-006, DAN-113
- justificativa: 
- aprofundar DAN-051: `firewall rule cause fix` — Este incidente tem causa e correção relacionados a configuração de firewall que bloqueou todo o tráfego, igual ao incidente atual.
  - DAN-051 (llm) [sem seção] 0.573: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-051 (llm) [sem seção] 0.557: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi

## q-243 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210, DAN-209, DAN-205, DAN-129, DAN-109, DAN-145
- justificativa: 
- aprofundar DAN-011: `Cloudflare bug permissions file size limit outage fix` — O incidente envolveu a Cloudflare, semelhante à CDN global cara; detalhes de mudança de permissões na base de dados e erro de tamanho de arquivo. Evidem para causa raiz e correção.
- aprofundar DAN-008: `Cloudflare Tiered Cache change 530 error fix` — Mudança no sistema de cache da Cloudflare que causou falha global, ainda que parcial; serve de caso adicional de impacto CDN em escala mundial.
  - DAN-011 (llm) [sem seção] 0.708: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (llm) [The outage] 0.651: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (causa) [How Cloudflare processes requests, and how this went wrong today] 0.396: ## How Cloudflare processes requests, and how this went wrong today  Throwing us off and making us believe this might have been an attack was another apparent symptom we observed: Cloudflare’s status 
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-008 (llm) [sem seção] 0.833: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Incident timeline and impact] 0.769: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Conclusion] 0.516: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i

## q-260 (esperado: DAN-197)

- busca inicial: DAN-066, DAN-106, DAN-067, DAN-029, DAN-209, DAN-220, DAN-154, DAN-205, DAN-008, DAN-133
- justificativa: 
- aprofundar DAN-106: `Amazon EC2 RDS Service Disruption cause root reason correction` — Este incidente é um corte de serviço da Amazon em que erros humanos e problemas de networking causaram falha na API de um provedor de nuvem, similar ao fato de o serviço falha sem nenhuma mudança interna do nosso lado.
- aprofundar DAN-066: `Cloudflare partial switch misbehavior cause root cause fix` — É um falha no provedor de nuvem Cloudflare que resultou em falta de disponibilidade da API, sem mudança interna no nosso lado.
- aprofundar DAN-205: `PagerDuty independent deployments peering point network instability root cause fix` — Fala de falha na rede de um provedor que pode afetar chamadas externas, mas não tão direto como Amazon ou Cloudflare.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.807: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.795: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  **April 29, 2011**  Now that we have fully restored functionality to all affected services, we would like to shar
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.41: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.652: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (llm) [sem seção] 0.62: *An analysis of the Cloudflare API availability incident on 2020-11-02*  When we review design documents at Cloudflare, we are always on the lookout for Single Points of Failure (SPOFs). Eliminating t
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.463: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-205 (llm) [The Outage] 0.764: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.763: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-242 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-109, DAN-026, DAN-129, DAN-145, DAN-106, DAN-009, DAN-008, DAN-067, DAN-016
- justificativa: 
- aprofundar DAN-011: `permission change bot detection file exceeded limit fix` — similar global CDN outage and cause internal software limit; matching broad impact
- aprofundar DAN-009: `service tokens release bug global CDN fix` — global impact on CDN and other services due to code release error
- aprofundar DAN-016: `DDoS rule infinite loop data center fix` — global CDN outage across data centers due to rate-limiting system flaw
  - DAN-011 (llm) [Memory preallocation] 0.6: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (llm) [Remediation and follow-up steps] 0.568: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-009 (llm) [sem seção] 0.689: Several Cloudflare services became unavailable for 121 minutes on January 24, 2023 due to an error releasing code that manages service tokens. The incident degraded a wide range of Cloudflare products
  - DAN-009 (llm) [How did we fix the issue?] 0.67: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [Incident Timeline] 0.424: ### Incident Timeline  At 2023-01-24 18:56 The same solution was implemented on the Cloudflare API account, impacting Cache Purge, Cache Reserve, Images and R2. **Impact ended for Cache Purge, Cache R
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.69: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-016 (llm) [Remediation and follow-up steps] 0.644: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Incident timeline and impact] 0.405: ## Incident timeline and impact  All timestamps are UTC on 2024-06-20.  - 14:14 DDoS rule gradual deployment starts - 17:06 DDoS rule deployed globally - 17:47 First HTTP request handling process is p

## q-261 (esperado: DAN-197)

- busca inicial: DAN-067, DAN-066, DAN-220, DAN-154, DAN-029, DAN-008, DAN-133, DAN-106, DAN-205, DAN-209
- justificativa: 
- aprofundar DAN-106: `human error routine networking upgrade resource crunch fix` — Envolve erro humano durante upgrade de rede e falta de recursos que causou interrupção do serviço do provedor, semelhante ao nosso caso em que o provedor falhou sem mudança interna.
- aprofundar DAN-205: `shared peering point network instability fix` — Apresenta falha na conectividade de rede de um provedor, similar ao nosso cenário de falha de API sem alteração no nosso lado.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.458: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.444: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-205 (llm) [The Outage] 0.62: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.61: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
