# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-020 | DAN-164 | 4 | não | sim | find → search | sim | sim | 2 | 18 |
| q-022 | DAN-104 | 4 | não | sim | find → search | sim | sim | 2 | 48 |
| q-170 | DAN-018 | 4 | não | sim | find → search | sim | sim | 2 | 352 |
| q-171 | DAN-018 | 4 | não | sim | find → search | sim | sim | 2 | 43 |
| q-222 | DAN-121 | 4 | não | sim | find → search | sim | sim | 2 | 71 |
| q-240 | DAN-152 | 4 | não | sim | find → search | sim | sim | 2 | 50 |
| q-012 | DAN-211 | 5 | não | sim | find → search | sim | sim | 2 | 8 |
| q-263 | DAN-200 | 5 | não | sim | find → search | sim | sim | 2 | 9 |
| q-032 | DAN-104 | 7 | não | sim | find → search | sim | sim | 2 | 42 |
| q-219 | DAN-116 | 7 | não | sim | find → search | sim | sim | 2 | 15 |
| q-223 | DAN-121 | 8 | não | sim | find → search | sim | sim | 3 | 252 |
| q-218 | DAN-116 | 9 | não | sim | find → search | sim | sim | 2 | 10 |
| q-229 | DAN-125 | 10 | não | sim | find → search | sim | sim | 2 | 14 |
| q-262 | DAN-200 | 10 | não | sim | find → search | sim | sim | 2 | 139 |
| q-228 | DAN-125 | 11 | não | sim | find → search | sim | sim | 2 | 11 |
| q-034 | DAN-004 | 12 | não | sim | find → search | sim | sim | 2 | 41 |
| q-243 | DAN-154 | 12 | não | não | find → search | não | não | 2 | 142 |
| q-260 | DAN-197 | 19 | não | sim | find → search | sim | sim | 2 | 10 |
| q-242 | DAN-154 | — | não | não | find → search | não | não | 2 | 12 |
| q-261 | DAN-197 | — | não | sim | find → search | sim | sim | 2 | 15 |

## q-020 (esperado: DAN-164)

- busca inicial: 
- justificativa: 
- aprofundar DAN-043: `root cause accidental production database deletion recovery backup` — Corresponde diretamente: engenheiros deletaram o banco de produção por acidente, igual ao incidente atual. Difere no provedor (DigitalOcean) e no tempo de recuperação.
- aprofundar DAN-056: `root cause accidental truncate production database environment variable fix` — Também envolve dano acidental ao banco de produção, mas provocado por variável de ambiente e testes, não por deleção direta durante manutenção.
- aprofundar DAN-164: `root cause admin deleted wrong directory data loss recovery` — Erro humano do admin apagando o alvo errado e perdendo dados, semântica próxima, embora o alvo seja um diretório e não o banco inteiro.
- novos incidentes nos achados: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-091, DAN-186, DAN-092, DAN-066, DAN-058, DAN-102, DAN-094, DAN-208, DAN-120
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.722: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [What happened?] 0.628: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [sem seção] 0.395: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-056 (llm) [What We Learned] 0.733: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.678: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a
  - DAN-164 (llm) [Root cause analysis] 0.617: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.514: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-022 (esperado: DAN-104)

- busca inicial: 
- justificativa: 
- aprofundar DAN-104: `human error remove servers typo S3 outage root cause corrective action` — O incidente atual é remoção de servidores por comando de operador derrubando serviço de armazenamento e dependentes; DAN-104 (Amazon S3) corresponde quase exatamente: comando para remover poucos servidores, erro de digitação removeu mais, derrubou S3 e serviços dependentes em cascata.
- aprofundar DAN-189: `operator tool lax input validation reboot small number servers affected all root cause fix` — Também envolve operador executando comando destinado a poucos servidores mas afetando muitos, embora seja reboot e não remoção, e não seja especificamente serviço de armazenamento.
- novos incidentes nos achados: DAN-191, DAN-189, DAN-146, DAN-104, DAN-064, DAN-067, DAN-073, DAN-109, DAN-209, DAN-103, DAN-107, DAN-048, DAN-125, DAN-230, DAN-222
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.652: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.643: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.631: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.577: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-170 (esperado: DAN-018)

- busca inicial: 
- justificativa: 
- aprofundar DAN-018: `root cause React component dashboard excessive API calls dependency array fix mitigation` — O resumo menciona bug em componente React do dashboard causando chamadas excessivas à API do Tenant Service, derrubando API e dashboard — espelha exatamente o incidente atual (painel enviando enxurrada de chamadas a serviço interno após deploy do frontend).
- aprofundar DAN-017: `deployment tool bug staging build cascading failure API dashboard root cause fix` — Envolve falha em deploy que roteia tráfego incorretamente e causa falhas em cascata na API e dashboard, mas não menciona especificamente o painel inundando um serviço interno; ainda assim, o gatilho de deploy se encaixa.
- novos incidentes nos achados: DAN-144, DAN-066, DAN-017, DAN-018, DAN-029, DAN-191, DAN-102, DAN-037, DAN-067, DAN-154, DAN-133, DAN-182, DAN-129, DAN-025, DAN-016
  - DAN-018 (llm) [What Happened] 0.649: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.649: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-017 (llm) [Timeline] 0.576: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (llm) [Analysis] 0.573: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.

## q-171 (esperado: DAN-018)

- busca inicial: 
- justificativa: 
- aprofundar DAN-018: `React component bug dashboard excessive API calls dependency array fix rollback` — O incidente atual é dashboard inundando serviço interno após deploy do frontend; este Cloudflare descreve exatamente um bug de componente React no dashboard causando chamadas excessivas de API após deploy, com correção envolvendo o dependency array e rollback.
- aprofundar DAN-144: `thundering herd frontend services internal queues memory outage fix` — Também envolve serviço frontend enchendo filas internas e falha em cascata que derruba serviços, embora o gatilho seja flapping e não um deploy do frontend.
- novos incidentes nos achados: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-133, DAN-129, DAN-218, DAN-145, DAN-220, DAN-155, DAN-011
  - DAN-018 (llm) [What Happened] 0.671: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.64: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-144 (llm) [Summary] 0.542: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.528: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (causa) [Resolved] 0.45: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Connectivity Issues] 0.428: ## Connectivity Issues  ## Postmortem  At Discord, one of our primary concerns is the uptime and reliability of our service. We’ve all experienced the frustration and annoyance that comes along with t

## q-222 (esperado: DAN-121)

- busca inicial: 
- justificativa: 
- aprofundar DAN-121: `database backend overloaded throttle requests timeout fix mitigation` — Corresponde quase exatamente: banco sobrecarregado throttling serviços, timeouts, e menciona iPlayer (player de vídeo). Diferença: é um post-mortem de blogs, não necessariamente mesmo stack.
- aprofundar DAN-147: `cascading failure request queue overloading database capacity fix` — Também é sobrecarga de banco causando falha em cascata, mas o gatilho é fila de requisições, não throttling explícito, e não menciona player de vídeo.
- aprofundar DAN-164: `influx of requests overloaded database replication lag fix recovery` — Banco sobrecarregado por influxo de requisições, mas inclui erro humano ao deletar diretório, o que não bate com o incidente atual.
- novos incidentes nos achados: DAN-129, DAN-144, DAN-147, DAN-121, DAN-016, DAN-137, DAN-134, DAN-209, DAN-148, DAN-220, DAN-186, DAN-194, DAN-164, DAN-094, DAN-156
  - DAN-121 (llm) [sem seção] 0.466: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.452: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.61: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.601: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Timeline] 0.697: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.678: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-240 (esperado: DAN-152)

- busca inicial: 
- justificativa: 
- aprofundar DAN-152: `malicious packages published compromised maintainer account root cause remediation` — Envolve pacotes maliciosos publicados em um registro (npm) por meio de uma conta comprometida, bem parecido com um pacote nosso não publicado enviando tokens; difere no alvo (lint vs. nossos pacotes) e no vetor (conta do mantenedor vs. desconhecido).
- aprofundar DAN-122: `impersonation attack malicious packages repository removal remediation` — Trata de ataque de personificação com pacotes maliciosos em um repositório (JCenter) que afetaram dependências, semelhante ao pacote não publicado por nós enviando tokens; difere no ecossistema (Maven/Android vs. nosso pacote) e no tempo de exposição.
- aprofundar DAN-141: `supply chain attack OAuth credentials exfiltration remediation revocation` — É um ataque de cadeia de suprimentos com exfiltração de dados via credenciais obtidas, relacionado ao vazamento de tokens, mas não envolve diretamente um pacote malicioso publicado sob nosso nome.
- novos incidentes nos achados: DAN-009, DAN-175, DAN-140, DAN-152, DAN-177, DAN-015, DAN-017, DAN-124, DAN-131, DAN-028, DAN-141, DAN-122, DAN-157, DAN-132
  - DAN-152 (llm) [Timeline] 0.638: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Summary] 0.599: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.62: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.593: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-141 (llm) [August 26–29, 2025: Scaling the response and proactive measures] 0.653: ### August 26–29, 2025: Scaling the response and proactive measures  While the primary Salesforce and Salesloft credentials had already been rotated, our next step was to terminate and securely re-est
  - DAN-141 (llm) [The Salesloft Drift breach] 0.612: ## The Salesloft Drift breach  As Salesloft has <u>announced</u>, a threat actor breached their systems. As part of the breach, the threat actor was able to obtain OAuth credentials associated with th
  - DAN-141 (causa) [August 17, 2025: Final exfiltration and coverup] 0.319: ### August 17, 2025: Final exfiltration and coverup  GRUB1 initiated the data exfiltration phase by switching to new infrastructure, logging in at **11:11:23** from the IP address `208[.]68[.]36[.]90`
  - DAN-141 (correcao) [Cloudflare's response and remediation] 0.513: ## Cloudflare's response and remediation  When Salesforce and Salesloft notified us on August 23, 2025, that the Drift integration had been abused across multiple organizations, including Cloudflare, 
  - DAN-141 (correcao) [August 25, 2025: Cloudflare initiates response activity] 0.432: ### August 25, 2025: Cloudflare initiates response activity  By August 25, we had received additional intelligence about the incident and escalated our response beyond the initial vendor-recommended c

## q-012 (esperado: DAN-211)

- busca inicial: 
- justificativa: 
- aprofundar DAN-020: `service discovery root cause fix dependent client cascading failure` — Direto sobre service discovery: config ruim de um cliente derrubou o service discovery globalmente quando um cliente dependente caiu. Bate com o componente (service discovery) e com o sintoma de impacto em outros serviços.
- aprofundar DAN-211: `Consul streaming BoltDB root cause fix outage service discovery` — Menciona Consul, que é uma camada de service discovery, e problemas de streaming/BoltDB. Bate com o componente afetado (service discovery) do incidente atual.
- aprofundar DAN-109: `metadata services timeout storage nodes retry cascading failure root cause fix` — Sintomas semelhantes: tempo de resposta excedendo timeouts, nós se desligando, retry aumentando carga e falha em cascata. Bate com writes timeoutando e outros serviços falhando.
- novos incidentes nos achados: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-066, DAN-222, DAN-113, DAN-101, DAN-133, DAN-205, DAN-151, DAN-219, DAN-221
  - DAN-020 (llm) [A thundering herd] 0.691: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (llm) [The failure of a core system] 0.671: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Improve the resilience of service discovery] 0.401: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.718: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  But what was going on with the slow leaders? We did not figure this out during the incident, but HashiCorp engineers determined the root cause in the
  - DAN-211 (llm) [Outage Summary] 0.709: ### Outage Summary  The outage was unique in both duration and complexity. The team had to address a number of challenges in sequence to understand the root cause and bring the service back up.  - The
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.63: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.608: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-263 (esperado: DAN-200)

- busca inicial: 
- justificativa: 
- aprofundar DAN-200: `root cause system reset priority inversion VxWorks fix priority inheritance patch` — Bate com o incidente atual: computador de bordo reiniciando sozinho dias depois de entrar em operação. Diferença: é uma sonda marciana, não um sistema terrestre genérico.
- novos incidentes nos achados: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-073, DAN-146, DAN-106, DAN-069, DAN-066, DAN-107, DAN-074, DAN-211, DAN-154, DAN-210
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.672: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.627: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-200 (causa) [THE FAILURE] 0.577: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HUMAN NATURE, DEADLINE PRESSURES] 0.436: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we

## q-032 (esperado: DAN-104)

- busca inicial: 
- justificativa: 
- aprofundar DAN-104: `root cause fix human error remove servers command typo S3 outage recovery restart` — Corresponde quase exatamente: operador executou comando para remover poucos servidores, mas removiu um conjunto maior que sustentava o serviço de armazenamento (S3), causando pane generalizada que não se recuperou sozinha (precisou de reinicialização completa dos sistemas dependentes). Difere só no detalhe de ter sido um erro de digitação no comando.
- aprofundar DAN-112: `root cause fix storage nodes could not rejoin cluster metadata nodes handshake timeout manual restart recovery` — Semelha no ponto de o serviço de armazenamento ficar baixo e não se recuperar automaticamente: nós de storage saíram do cluster e não puderam voltar porque os nós de metadados que os autorizariam também tinham caído; a correção exigiu intervenção manual (aumentar timeout e reiniciar nós de metadados). Difere no gatilho (falha de energia, não comando do operador).
- aprofundar DAN-189: `root cause fix operator tool lax input validation reboot all servers outage manual intervention` — Compartilha o padrão de um operador mexer em um pequeno conjunto de servidores e causar pane em escala maior por falha na ferramenta/processo, exigindo intervenção manual. Difere porque é reboot, não remoção, e não foca especificamente em serviço de armazenamento.
- novos incidentes nos achados: DAN-109, DAN-210, DAN-189, DAN-191, DAN-067, DAN-073, DAN-104, DAN-103, DAN-026, DAN-070, DAN-112, DAN-146, DAN-143, DAN-209, DAN-029
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.605: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.601: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-112 (llm) [Summary of the Amazon SimpleDB Service Disruption] 0.6: ### Summary of the Amazon SimpleDB Service Disruption  Once the problem was identified, we had to manually increase the handshake timeout values and restart a subset of metadata nodes so that they cou
  - DAN-112 (llm) [Summary of the Amazon SimpleDB Service Disruption] 0.533: ### Summary of the Amazon SimpleDB Service Disruption  In this event, multiple storage nodes became unavailable simultaneously in a single data center (after power was lost to the servers on which the
  - DAN-112 (causa) [Summary of the Amazon SimpleDB Service Disruption] 0.33: ### Summary of the Amazon SimpleDB Service Disruption  We wanted to share what we've learned from our investigation of the June 13 SimpleDB disruption in the US East Region. The service was unavailabl
  - DAN-189 (llm) [What Happened?] 0.633: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.624: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-219 (esperado: DAN-116)

- busca inicial: 
- justificativa: 
- aprofundar DAN-116: `double free database update all servers crash simultaneously root cause fix` — Bate com falha simultânea de todos os servidores após atualização de banco de dados e atraso para disparar o bug; não especifica o componente exato do serviço atual.
- aprofundar DAN-209: `migration critical backend system outage root cause fix` — Bate com atualização/migração de sistema crítico causando queda; não confirma que todos os servidores caíram ao mesmo tempo.
- novos incidentes nos achados: DAN-066, DAN-126, DAN-103, DAN-222, DAN-205, DAN-209, DAN-116, DAN-109, DAN-191, DAN-189, DAN-146, DAN-164, DAN-154, DAN-094, DAN-043
  - DAN-116 (llm) [sem seção] 0.692: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.602: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-209 (llm) [sem seção] 0.572: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.547: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 

## q-223 (esperado: DAN-121)

- busca inicial: 
- justificativa: 
- aprofundar DAN-121: `database overload throttle requests services timeout root cause fix` — Bate quase exatamente: banco de dados sobrecarregado throttling requisições de vários serviços e timeouts, incluindo serviço de vídeo (iPlayer).
- aprofundar DAN-101: `database connection pool exhaustion timeout root cause fix` — Bate em sintoma de timeout de banco e serviços, mas não menciona throttling explícito nem vídeo player.
- aprofundar DAN-147: `cascading failure database capacity overload root cause fix` — Bate em falha em cascata por sobrecarga de banco, mas não detalha throttling de requisições nem timeouts de serviços específicos.
- novos incidentes nos achados: DAN-147, DAN-148, DAN-101, DAN-129, DAN-134, DAN-219, DAN-164, DAN-121, DAN-144, DAN-094, DAN-183, DAN-156, DAN-096, DAN-181, DAN-133
  - DAN-121 (llm) [sem seção] 0.51: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.482: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-101 (llm) [sem seção] 0.671: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (llm) [sem seção] 0.666: It wasn’t until a few days later that we realised this was the root of our problems. As the timeouts were intermittent and didn’t occur every day, it took a little while to confirm the issue. But, it’
  - DAN-101 (causa) [sem seção] 0.405: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (correcao) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-101 (correcao) [sem seção] 0.317: Originally, we would receive this event from Slack, and within the lifetime of that HTTP request, we’d perform any responses we needed to, e.g. offering to attach a GitHub link that a user has just po
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.594: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.519: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we

## q-218 (esperado: DAN-116)

- busca inicial: 
- justificativa: 
- aprofundar DAN-116: `root cause database update double free all servers crash simultaneous time delay` — Bate muito: atualização de banco de dados revelou um bug que fez todos os servidores do 'impression bus' caírem ao mesmo tempo, com atraso temporal antes de disparar — igual ao incidente atual (queda simultânea após atualização de dados).
- aprofundar DAN-142: `root cause content update out-of-bounds memory read Windows crash BSOD remediation` — Bate parcialmente: uma atualização de conteúdo com erros não detectados causou crash simultâneo em milhões de máquinas. Difere porque é um update de conteúdo Windows, não exatamente atualização de dados de serviço.
- aprofundar DAN-154: `root cause software bug triggered by customer configuration change global outage remediation` — Bate parcialmente: bug não descoberto disparado por mudança de configuração causou outage global. Difere porque é mudança de configuração do cliente, não atualização de dados aplicada ao serviço.
- novos incidentes nos achados: DAN-126, DAN-146, DAN-103, DAN-066, DAN-209, DAN-106, DAN-048, DAN-191, DAN-116, DAN-189, DAN-142, DAN-205, DAN-208, DAN-026, DAN-154
  - DAN-116 (llm) [sem seção] 0.707: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.661: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-142 (llm) [Q: What happened?] 0.709: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [Preliminary Post Incident Review] 0.591: ## Preliminary Post Incident Review  ### Content Configuration Update Impacting the Falcon Sensor and the Windows Operating System (BSOD)  This is CrowdStrike’s preliminary Post Incident Review (PIR).
  - DAN-142 (causa) [What Went Wrong and Why?] 0.384: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di
  - DAN-154 (llm) [**What happened?**] 0.669: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (llm) [sem seção] 0.657: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s

## q-229 (esperado: DAN-125)

- busca inicial: 
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade cascading collapse remediation` — Bate quase perfeitamente: banco reduzido/downgrade, carga de pico e colapso em cascata de servidores dependentes, igual ao incidente atual.
- aprofundar DAN-147: `insufficient database capacity cascading failure root cause fix` — Falha em cascata por capacidade insuficiente do banco, mas sem menção ao redimensionamento recente.
- aprofundar DAN-219: `cache nodes removal high workload outage root cause fix` — Remoção de infraestrutura causou sobrecarga e pane, análogo ao downsizing, mas componente é cache, não banco de dados.
- novos incidentes nos achados: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-129, DAN-091, DAN-125, DAN-219, DAN-148, DAN-134, DAN-066, DAN-120
  - DAN-125 (llm) [Database performance issues] 0.604: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.532: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.578: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.524: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-219 (llm) [Cascading failure in the cache and datastore tiers] 0.606: ## Cascading failure in the cache and datastore tiers  Once the system is in either a healthy state or a cascading failure state it will tend to stay there, unless there is an external intervention th
  - DAN-219 (llm) [What triggered the incident?] 0.602: ## What triggered the incident?  The PBR step on February 22 updated Consul on 25% of the fleet. It followed two previous 25% steps the prior week, both of which had occurred without any incident. How
  - DAN-219 (causa) [Learnings] 0.551: ## Learnings  The incident has also highlighted some other risks. A brief network outage or partition affecting the cache nodes might trigger the same kind of cascading failure scenario as the Consul 
  - DAN-219 (correcao) [Learnings] 0.467: ## Learnings  We see familiar patterns here which often arise in incidents: performance bottlenecks, cascading failures, dependency on a warm cache, and changes as triggering events. Reading an incide
  - DAN-219 (correcao) [What triggered the incident?] 0.408: ## What triggered the incident?  The Mcrib component is a relatively new piece of software. Prior to Mcrib, we used a distributed locking mechanism based on Consul locks to generate the Mcrouter hash 

## q-262 (esperado: DAN-200)

- busca inicial: 
- justificativa: 
- aprofundar DAN-200: `priority inversion system reset VxWorks patch fix` — O incidente atual é um computador de bordo reiniciando sozinho dias após entrar em operação; DAN-200 é exatamente um computador espacial reiniciando dias após o pouso em Marte, com causa raiz e correção remota documentadas.
- aprofundar DAN-198: `rendezvous radar CPU load computer restart Apollo 11 fix` — Também envolve reinício de computador de bordo por sobrecarga de CPU, embora o gatilho seja durante o pouso lunar e não dias após o início da operação.
- novos incidentes nos achados: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073, DAN-189, DAN-146, DAN-210, DAN-043, DAN-200, DAN-182, DAN-137, DAN-102, DAN-154, DAN-069
  - DAN-200 (llm) [THE FAILURE] 0.623: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.61: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.736: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.704: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-228 (esperado: DAN-125)

- busca inicial: 
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade root cause fix cascading collapse dependent servers peak` — Corresponde quase exatamente: redução de capacidade do banco, pico de carga e colapso em cascata de servidores dependentes, igual ao incidente atual.
- aprofundar DAN-147: `cascading failure insufficient database capacity request queue root cause remediation` — Também envolve falha em cascata por capacidade insuficiente do banco de dados, sem mencionar redução recente, mas o padrão de sintoma é semelhante.
- aprofundar DAN-096: `peak hour load mysql cluster ProxySQL connections exhausted root cause fix throttling` — Envolve carga em pico sobrecarregando o banco de dados com impacto em serviços dependentes, embora não mencione downsizing.
- novos incidentes nos achados: DAN-164, DAN-147, DAN-156, DAN-048, DAN-096, DAN-043, DAN-094, DAN-209, DAN-134, DAN-109, DAN-130, DAN-219, DAN-194, DAN-125, DAN-066
  - DAN-125 (llm) [Database performance issues] 0.594: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.537: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.623: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.605: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.681: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.662: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev

## q-034 (esperado: DAN-004)

- busca inicial: 
- justificativa: 
- aprofundar DAN-051: `firewall config root cause fix blocked traffic` — Bate com o sintoma de tráfego bloqueado por firewall; não sei se houve mudança não registrada.
- aprofundar DAN-004: `unrecorded WAF change root cause fix Terraform drift` — Muito parecido: mudança de firewall/WAF não registrada bloqueando tráfego, operadores não sabiam da mudança.
- novos incidentes nos achados: DAN-005, DAN-137, DAN-051, DAN-012, DAN-220, DAN-011, DAN-016, DAN-014, DAN-006, DAN-113, DAN-009, DAN-004, DAN-007
  - DAN-051 (llm) [sem seção] 0.586: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-051 (llm) [sem seção] 0.542: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-004 (llm) [**Root Cause Analysis**] 0.747: ## **Root Cause Analysis**  While we manage all our infrastructure, including WAF, almost entirely with Terraform, we discovered during this incident a misconfiguration in IAM controls that allowed a 
  - DAN-004 (llm) [What Happened] 0.657: ## What Happened  - **01:15:** Initial investigation revealed broad connectivity issues between the frontend and our backing APIs, including CORS (Cross-Origin Resource Sharing) errors. The team explo
  - DAN-004 (causa) [Summary] 0.416: ## Summary  On April 4, 2025, from 00:16 to 01:49 UTC (approximately 1 hour and 33 minutes), CircleCI experienced a service disruption affecting both our user interface and build capabilities. During 
  - DAN-004 (correcao) [Future Prevention and Process Improvement] 0.505: ## Future Prevention and Process Improvement  This incident highlighted the strength of our existing systems while identifying several areas where we can improve and make them even more robust:  1. We
  - DAN-004 (correcao) [What Happened] 0.435: ## What Happened  (all times UTC)  The WAF is a critical security component that sits in front of our services and protects them from malicious traffic, while allowing legitimate requests to pass thro

## q-243 (esperado: DAN-154)

- busca inicial: 
- justificativa: 
- aprofundar DAN-005: `bad config router rule edge routers crash root cause fix` — Cloudflare is a CDN; a bad router config caused all edge routers to crash and took down all of Cloudflare worldwide, closely matching a sudden worldwide CDN outage.
- aprofundar DAN-011: `database permissions file exceeded limits systemwide outage root cause fix` — Cloudflare systemwide outage propagated through the network after a database permission change, matching a CDN failing globally.
- aprofundar DAN-023: `backbone routers configuration changes global outage root cause fix` — Configuration changes to backbone routers caused a global outage of all services, similar to a sudden worldwide service loss though not CDN-specific.
- novos incidentes nos achados: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210, DAN-209, DAN-205, DAN-129, DAN-109, DAN-145, DAN-005, DAN-023, DAN-016, DAN-006, DAN-007
  - DAN-005 (llm) [Bad Rule] 0.705: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.613: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-011 (llm) [Memory preallocation] 0.565: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (llm) [sem seção] 0.56: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-023 (llm) [sem seção] 0.64: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.63: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-260 (esperado: DAN-197)

- busca inicial: 
- justificativa: 
- aprofundar DAN-197: `root cause Azure breaking change fix recovery downstream service` — Bate muito: provedor de nuvem (Azure) publicou uma mudança quebrada sem aviso, afetando serviço downstream sem mudança do lado do cliente — exatamente o sintoma atual de chamadas de API falhando do nada.
- novos incidentes nos achados: DAN-066, DAN-106, DAN-067, DAN-029, DAN-209, DAN-220, DAN-154, DAN-205, DAN-008, DAN-133, DAN-184, DAN-018, DAN-197, DAN-193, DAN-169
  - DAN-197 (llm) [sem seção] 0.698: Although APIs are the lifeblood of so many software applications today, the impact on their dependencies when they break can often be overlooked. And while full outages can have a more widespread and 
  - DAN-197 (llm) [Discovery of the Outage] 0.661: ## Discovery of the Outage  We first noticed the problem with the partial outage of our Azure CosmosDB service monitor September 14th at 18:42 UTC. We reported to our users that the product was not fu
  - DAN-197 (causa) [Discovery of the Outage] 0.424: ## Discovery of the Outage  While this data was not the most helpful, it confirmed that there was something wrong with our request, despite no changes to how we made the request in months. Until seein
  - DAN-197 (correcao) [Background] 0.362: ## Background  First, a bit of background on how we use Azure CosmosDB, and how we obtained the debugging data to determine that Azure published a breaking change without telling their customers. Metr
  - DAN-197 (correcao) [Conclusions] 0.356: ## Conclusions  All in all, this was a fairly simple fix, but because of the nature of the API, it could have been worse. The more deeply ingrained a given API is into one’s app, the bigger an effect 

## q-242 (esperado: DAN-154)

- busca inicial: 
- justificativa: 
- aprofundar DAN-005: `router rule config change all edge routers crash global outage rollback fix` — Bate: queda global repentina de CDN com todos os servidores/edge routers fora, causada por mudança de config. Não bate se a causa atual for de aplicação e não de roteamento.
- aprofundar DAN-011: `database permissions bot detection file limit systemwide Cloudflare outage remediation` — Bate: pane sistêmica global na CDN da Cloudflare gerada por mudança em sistema de segurança. Não bate se o sintoma atual for só erro de servidor sem relação com bot detection.
- aprofundar DAN-137: `WAF rule regex backtracking CPU exhaustion global Cloudflare downtime fix` — Bate: queda global dos serviços Cloudflare/CDN por regra implantada em produção. Não bate se a causa atual não for uma regra de WAF ou expressão regular.
- novos incidentes nos achados: DAN-011, DAN-109, DAN-026, DAN-129, DAN-145, DAN-106, DAN-009, DAN-008, DAN-067, DAN-016, DAN-005, DAN-023, DAN-184, DAN-193, DAN-137
  - DAN-005 (llm) [Bad Rule] 0.666: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.654: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-011 (llm) [Remediation and follow-up steps] 0.693: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-011 (llm) [Remediation and follow-up steps] 0.677: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [How Cloudflare processes requests, and how this went wrong today] 0.393: ## How Cloudflare processes requests, and how this went wrong today  This feature file is refreshed every few minutes and published to our entire network and allows us to react to variations in traffi
  - DAN-137 (llm) [The events of July 2] 0.824: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (llm) [sem seção] 0.815: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (causa) [What happened] 0.441: ### What happened  Let’s begin with the sequence of events. All times in this blog are UTC.  At 13:42 an engineer working on the firewall team deployed a minor change to the rules for XSS detection vi
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-261 (esperado: DAN-197)

- busca inicial: 
- justificativa: 
- aprofundar DAN-197: `Azure breaking change downstream systems root cause fix recovery` — O Azure fez uma mudança não avisada que quebrou sistemas downstream, exatamente 'nenhuma mudança do nosso lado' mas falha na API do provedor de nuvem.
- aprofundar DAN-193: `AWS us-east-1 outage API degradation root cause fix` — Interrupção da AWS afetou a API do LaunchDarkly sem mudança do lado deles, similar ao chamado a API de provedor de nuvem falhando.
- aprofundar DAN-106: `EC2 RDS disruption human error networking upgrade root cause fix` — Interrupção da Amazon EC2/RDS afetou clientes sem mudança do lado deles, prove­niente do provedor de nuvem.
- novos incidentes nos achados: DAN-067, DAN-066, DAN-220, DAN-154, DAN-029, DAN-008, DAN-133, DAN-106, DAN-205, DAN-209, DAN-018, DAN-193, DAN-189, DAN-197, DAN-037
  - DAN-197 (llm) [sem seção] 0.705: Although APIs are the lifeblood of so many software applications today, the impact on their dependencies when they break can often be overlooked. And while full outages can have a more widespread and 
  - DAN-197 (llm) [Discovery of the Outage] 0.654: ## Discovery of the Outage  While this data was not the most helpful, it confirmed that there was something wrong with our request, despite no changes to how we made the request in months. Until seein
  - DAN-197 (causa) [Discovery of the Outage] 0.42: ## Discovery of the Outage  We first noticed the problem with the partial outage of our Azure CosmosDB service monitor September 14th at 18:42 UTC. We reported to our users that the product was not fu
  - DAN-197 (correcao) [Background] 0.362: ## Background  First, a bit of background on how we use Azure CosmosDB, and how we obtained the debugging data to determine that Azure published a breaking change without telling their customers. Metr
  - DAN-197 (correcao) [Conclusions] 0.356: ## Conclusions  All in all, this was a fairly simple fix, but because of the nature of the API, it could have been worse. The more deeply ingrained a given API is into one’s app, the bigger an effect 
  - DAN-193 (llm) [What Happened and What Caused It] 0.717: ## What Happened and What Caused It  The incident unfolded in two phases.  The **first phase** (between October 19, 11:50 PM and October 20, 11:40 AM) began late on October 19, when AWS us-east-1 expe
  - DAN-193 (llm) [What Happened and What Caused It] 0.716: ## What Happened and What Caused It  However, **a second phase** (between October 20, 11:40 AM and October 21, 12:05 AM) of disruption began shortly after. At 11:48 AM, while we were stabilizing our s
  - DAN-193 (causa) [sem seção] 0.369: On October 20, 2025, LaunchDarkly experienced a widespread service disruption that impacted feature flag management, feature flag delivery, as well as our guarded releases, observability, experimentat
  - DAN-193 (correcao) [How We’re Improving] 0.441: ## How We’re Improving  We’ve already made substantial improvements to our systems, and more are underway. Our goal is clear: to help ensure that a regional cloud outage cannot cause the same kind of 
  - DAN-193 (correcao) [3. Strengthening Multi-region availability and Disaster Recovery] 0.336: #### 3. Strengthening Multi-region availability and Disaster Recovery  We are relocating all disaster recovery orchestration systems out of us-east-1.  We are investigating multi-region improvements a
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.672: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.669: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
