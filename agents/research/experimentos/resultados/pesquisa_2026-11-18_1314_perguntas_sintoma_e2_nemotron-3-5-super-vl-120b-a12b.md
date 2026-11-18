# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-006 | DAN-015 | 1 | sim | não | search | não | sim | 0 | 19 |
| q-008 | DAN-142 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-010 | DAN-137 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-012 | DAN-211 | 5 | sim | sim | search | não | sim | 0 | 15 |
| q-014 | DAN-078 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-016 | DAN-067 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-018 | DAN-162 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-020 | DAN-164 | 4 | sim | sim | search | não | sim | 0 | 9 |
| q-022 | DAN-104 | 4 | sim | sim | search | não | sim | 0 | 9 |
| q-024 | DAN-004 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-026 | DAN-011 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-028 | DAN-137 | 2 | sim | sim | search | não | sim | 0 | 15 |
| q-030 | DAN-078 | 1 | sim | sim | search | não | sim | 0 | 24 |
| q-032 | DAN-104 | 7 | sim | sim | search | não | sim | 0 | 10 |
| q-034 | DAN-004 | 12 | não | não | search | não | não | 0 | 15 |
| q-036 | DAN-019 | 1 | sim | sim | search | não | sim | 0 | 28 |
| q-038 | DAN-090 | 2 | sim | sim | search | não | sim | 0 | 7 |
| q-164 | DAN-001 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-165 | DAN-001 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-166 | DAN-003 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-167 | DAN-003 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-168 | DAN-017 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-169 | DAN-017 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-170 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 13 |
| q-171 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 22 |
| q-172 | DAN-020 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-173 | DAN-020 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-174 | DAN-022 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-175 | DAN-022 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-176 | DAN-026 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-177 | DAN-026 | 1 | sim | sim | search | não | sim | 0 | 25 |
| q-178 | DAN-033 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-179 | DAN-033 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-180 | DAN-042 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-181 | DAN-042 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-182 | DAN-043 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-183 | DAN-043 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-184 | DAN-048 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-185 | DAN-048 | 1 | sim | sim | search | não | sim | 0 | 24 |
| q-186 | DAN-049 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-187 | DAN-049 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-188 | DAN-050 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-189 | DAN-050 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-190 | DAN-058 | 2 | sim | sim | search | não | sim | 0 | 8 |
| q-191 | DAN-058 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-192 | DAN-059 | 2 | sim | sim | search | não | sim | 0 | 18 |
| q-193 | DAN-059 | 2 | sim | sim | search | não | sim | 0 | 10 |
| q-194 | DAN-060 | 3 | sim | sim | search | não | sim | 0 | 8 |
| q-195 | DAN-060 | 1 | sim | sim | search | não | sim | 0 | 23 |
| q-196 | DAN-065 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-197 | DAN-065 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-198 | DAN-069 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-199 | DAN-069 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-200 | DAN-073 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-201 | DAN-073 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-202 | DAN-076 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-203 | DAN-076 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-204 | DAN-083 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-205 | DAN-083 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-206 | DAN-085 | 2 | sim | sim | search | não | sim | 0 | 6 |
| q-207 | DAN-085 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-208 | DAN-086 | 1 | sim | sim | search | não | sim | 0 | 19 |
| q-209 | DAN-086 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-210 | DAN-088 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-211 | DAN-088 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-212 | DAN-092 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-213 | DAN-092 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-214 | DAN-093 | 3 | sim | sim | search | não | sim | 0 | 6 |
| q-215 | DAN-093 | 3 | sim | sim | search | não | sim | 0 | 8 |
| q-216 | DAN-106 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-217 | DAN-106 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-218 | DAN-116 | 9 | sim | sim | search | não | sim | 0 | 20 |
| q-219 | DAN-116 | 7 | sim | sim | search | não | sim | 0 | 16 |
| q-220 | DAN-118 | 2 | sim | sim | search | não | sim | 0 | 15 |
| q-221 | DAN-118 | 2 | sim | sim | search | não | sim | 0 | 20 |
| q-222 | DAN-121 | 4 | sim | sim | search | não | sim | 0 | 14 |
| q-223 | DAN-121 | 8 | sim | sim | search | não | sim | 0 | 12 |
| q-224 | DAN-122 | 2 | sim | sim | search | não | sim | 0 | 7 |
| q-225 | DAN-122 | 1 | sim | sim | search | não | sim | 0 | 44 |
| q-226 | DAN-124 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-227 | DAN-124 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-228 | DAN-125 | 11 | não | não | search | não | não | 0 | 20 |
| q-229 | DAN-125 | 10 | sim | sim | search | não | sim | 0 | 15 |
| q-230 | DAN-126 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-231 | DAN-126 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-232 | DAN-127 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-233 | DAN-127 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-234 | DAN-129 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-235 | DAN-129 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-236 | DAN-145 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-237 | DAN-145 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-238 | DAN-148 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-239 | DAN-148 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-240 | DAN-152 | 4 | sim | sim | search | não | sim | 0 | 10 |
| q-241 | DAN-152 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-242 | DAN-154 | — | não | não | search | não | não | 0 | 14 |
| q-243 | DAN-154 | 12 | não | não | search | não | não | 0 | 15 |
| q-244 | DAN-165 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-245 | DAN-165 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-246 | DAN-170 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-247 | DAN-170 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-248 | DAN-180 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-249 | DAN-180 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-250 | DAN-183 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-251 | DAN-183 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-252 | DAN-186 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-253 | DAN-186 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-254 | DAN-188 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-255 | DAN-188 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-256 | DAN-189 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-257 | DAN-189 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-258 | DAN-194 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-259 | DAN-194 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-260 | DAN-197 | 19 | não | não | search | não | não | 0 | 15 |
| q-261 | DAN-197 | — | não | não | search | não | não | 0 | 14 |
| q-262 | DAN-200 | 10 | sim | sim | search | não | sim | 0 | 11 |
| q-263 | DAN-200 | 5 | sim | sim | search | não | sim | 0 | 10 |
| q-264 | DAN-204 | 3 | sim | sim | search | não | sim | 0 | 17 |
| q-265 | DAN-204 | 2 | sim | sim | search | não | sim | 0 | 14 |
| q-266 | DAN-205 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-267 | DAN-205 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-268 | DAN-207 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-269 | DAN-207 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-270 | DAN-208 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-271 | DAN-208 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-272 | DAN-215 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-273 | DAN-215 | 2 | sim | sim | search | não | sim | 0 | 12 |
| q-274 | DAN-226 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-275 | DAN-226 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-276 | DAN-235 | 1 | sim | sim | search | não | sim | 0 | 26 |
| q-277 | DAN-235 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-278 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-279 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-280 | DAN-237 | 1 | sim | sim | search | não | sim | 0 | 43 |
| q-281 | DAN-237 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-282 | DAN-240 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-283 | DAN-240 | 1 | sim | sim | search | não | sim | 0 | 15 |

## q-006 (esperado: DAN-015)

- busca inicial: DAN-015, DAN-184, DAN-140, DAN-221, DAN-086, DAN-009, DAN-066, DAN-053, DAN-017, DAN-204
- justificativa: 
- aviso: search_inside_incidents: Error invoking tool 'search_inside_incidents' with kwargs {'searches': '[{"incident_id": "DAN-015", "query": "R2 credential rotation storage authentication error credentials environment production fix

## q-008 (esperado: DAN-142)

- busca inicial: DAN-142, DAN-154, DAN-146, DAN-126, DAN-226, DAN-116, DAN-217, DAN-074, DAN-143, DAN-103
- justificativa: 
- aprofundar DAN-142: `content validator bug out of bounds memory read BSOD fix revert` — Corresponde exatamente: atualização de software de segurança (Falcon Content Update) causou BSOD simultâneo em milhões de máquinas Windows; nenhum outro incidente combina atualização de segurança com BSOD em massa.
  - DAN-142 (llm) [Q: What happened?] 0.636: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [What Went Wrong and Why?] 0.575: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (causa) [Third Party Validation] 0.38: ### Third Party Validation  - Conduct multiple independent third-party security code reviews. - Conduct independent reviews of end-to-end quality processes from development through deployment.  *In ad
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di

## q-010 (esperado: DAN-137)

- busca inicial: DAN-137, DAN-016, DAN-005, DAN-035, DAN-183, DAN-026, DAN-220, DAN-148, DAN-106, DAN-012
- justificativa: 
- aprofundar DAN-137: `WAF rule regex backtracking CPU exhaustion fix rollback` — Bate: mudança de regra de firewall/WAF seguida de exaustão de CPU nos servidores de borda. Não bate: causa específica é regex com backtracking, não confirmada no incidente atual.
- aprofundar DAN-016: `DDoS mitigation rule cookie validation infinite loop CPU fix` — Bate: regra recém implantada causou loop infinito e 100% de CPU propagando entre data centers. Não bate: componente afetado é o rate-limiting/cookie validation, não confirmado como firewall.
- aprofundar DAN-005: `router rule config edge routers crash fix rollback` — Bate: mudança de regra de configuração afetou roteadores de borda. Não bate: causou crash dos roteadores, não 100% de CPU nos servidores de borda.
  - DAN-137 (llm) [Appendix: About Regular Expression Backtracking] 0.726: ### Appendix: About Regular Expression Backtracking  To fully understand how ``(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*
  - DAN-137 (llm) [The events of July 2] 0.723: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [sem seção] 0.482: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.721: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.697: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-005 (llm) [Bad Rule] 0.683: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.619: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp

## q-012 (esperado: DAN-211)

- busca inicial: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-066, DAN-222, DAN-113, DAN-101, DAN-133
- justificativa: 
- aprofundar DAN-020: `service discovery bad config client global outage root cause fix` — Envolve diretamente a camada de service discovery sendo derrubada por um cliente dependente, espelhando a lentidão e o efeito em cascata no serviço atual, embora a causa seja configuração e não performance de gravação.
- aprofundar DAN-211: `Consul streaming BoltDB service discovery performance degradation root cause fix` — O Consul é uma camada de service discovery e relatou degradação de desempenho sob carga, semelhante à camada lenta atual, embora o contexto seja uma interrupção longa com iptables.
- aprofundar DAN-109: `metadata service load timeout storage nodes retry storm root cause fix` — Mostra sobrecarga de serviço de backend causando timeouts e falha em cascata em outros componentes, parecido com writes timeoutando e outros serviços falhando, embora não seja service discovery.
  - DAN-020 (llm) [The failure of a core system] 0.692: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.678: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.711: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.701: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  But what was going on with the slow leaders? We did not figure this out during the incident, but HashiCorp engineers determined the root cause in the
  - DAN-211 (causa) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.489: ### Early Triage (10/28 13:37 – 10/29 02:00)  At this point, the team developed a new theory about what was going wrong: increased traffic. Perhaps Consul was slow because our system reached a tipping
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.617: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.593: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-014 (esperado: DAN-078)

- busca inicial: DAN-078, DAN-066, DAN-006, DAN-048, DAN-164, DAN-205, DAN-043, DAN-162, DAN-116, DAN-023
- justificativa: 
- aprofundar DAN-078: `network partition MySQL failover replication lag data inconsistency recovery fix` — Bate com o incidente atual: partição de rede entre data centers causou failover de master MySQL e dados divergentes por latência intercontinental; não bate por ser durante manutenção planejada e não um hiccup não planejado.
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.709: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [Incident timeline] 0.68: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa

## q-016 (esperado: DAN-067)

- busca inicial: DAN-067, DAN-068, DAN-064, DAN-069, DAN-023, DAN-063, DAN-191, DAN-060, DAN-209, DAN-062
- justificativa: 
- aprofundar DAN-067: `data center power failure control plane analytics outage root cause remediation` — Bate exatamente: controle/analytics fora do ar por falha de energia em data center. Não bate: provedor específico Cloudflare/Flexential.
- aprofundar DAN-068: `breaker coordination power loss data center root cause fix` — Bate: perda total de energia em data center por falha elétrica. Não bate: foco em breakers, não menciona painel de controle/analytics.
- aprofundar DAN-063: `utility power loss generator failure network config root cause fix` — Bate: perda de utilidade em AZ/data center com impacto em serviços. Não bate: inclui falha de geradores e rota de rede inválida, não apenas perda de energia.
  - DAN-067 (llm) [Lessons and Remediation] 0.745: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.724: ### Flexential Data Center Power Failure  The largest of the three facilities in Oregon is run by Flexential. We refer to this facility as “PDX-DC04”. Cloudflare leases space in PDX-04 where we house 
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-068 (llm) [What happened to the power in the data center?] 0.767: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.68: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.621: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.599: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.438: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo

## q-018 (esperado: DAN-162)

- busca inicial: DAN-162, DAN-026, DAN-010, DAN-164, DAN-075, DAN-020, DAN-087, DAN-066, DAN-186, DAN-049
- justificativa: 
- aprofundar DAN-162: `database migration DNS resolution failure recovery fix` — Bate perfeitamente: falha de DNS em um site logo após migração de banco de dados, exatamente como o incidente atual; não bate o fato de ser GitHub e ter havido cascata para outros sites.
- aprofundar DAN-049: `DNS record recreation certificate deployment downtime fix` — Bate parcialmente: falha de DNS após deploy envolvendo recriação de registros DNS e certificados de banco; não há relação clara com migração de banco de dados ou escopo de um único site.
- aprofundar DAN-026: `Puppet authoritative nameserver restart IP change corrupt zone fix` — Bate parcialmente: falha de resolução DNS após mudança de infraestrutura (IP); não bate porque o gatilho foi um bug de Puppet, não uma migração de banco de dados.
  - DAN-162 (llm) [sem seção] 0.553: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5
  - DAN-049 (llm) [Resolution] 0.677: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [Postmortem] 0.673: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (causa) [Root Cause of the Outage] 0.422: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat
  - DAN-026 (llm) [What happened…] 0.709: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (llm) [What happened…] 0.645: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto

## q-020 (esperado: DAN-164)

- busca inicial: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-091, DAN-186, DAN-092, DAN-066, DAN-058
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup recovery fix` — Mesmo cenário exato: exclusão acidental do banco de produção, com restauração via backup e perda de dados.
- aprofundar DAN-164: `admin deleted wrong directory data loss recovery fix` — Erro humano de exclusão de dados (banco/diretório errado), mas sem contexto de janela de manutenção.
- aprofundar DAN-056: `accidental environment variable truncate production database fix` — Truncamento acidental de banco de produção por erro humano, mas disparado por variável de ambiente em testes.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.734: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.661: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [sem seção] 0.548: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (llm) [Root cause analysis] 0.547: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.732: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.72: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-022 (esperado: DAN-104)

- busca inicial: DAN-191, DAN-189, DAN-146, DAN-104, DAN-064, DAN-067, DAN-073, DAN-109, DAN-209, DAN-103
- justificativa: 
- aprofundar DAN-104: `human error remove servers typo S3 outage root cause fix` — Bate porque envolve operador executando comando para remover poucos servidores que acabou removendo um conjunto maior, derrubando serviço de armazenamento (S3) e sistemas dependentes; não bate porque foi um erro de digitação, não remoção intencional.
- aprofundar DAN-189: `operator reboot servers lax input validation outage root cause fix` — Bate porque operador usou ferramenta com validação frouxa e afetou mais servidores do que pretendia, causando pane generalizada; não bate porque foi reboot, não remoção de servidores, e não atingiu especificamente serviço de armazenamento.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.646: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.621: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.658: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [What Happened?] 0.592: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (causa) [Next Steps] 0.434: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-024 (esperado: DAN-004)

- busca inicial: DAN-004, DAN-017, DAN-137, DAN-091, DAN-005, DAN-066, DAN-102, DAN-130, DAN-012, DAN-154
- justificativa: 
- aprofundar DAN-004: `IAM role gap WAF out-of-band change Terraform drift detection fix` — O incidente atual descreve tráfego de UI e build triggers bloqueado sem mudança no pipeline de infraestrutura, o que corresponde ao DAN-004: uma alteração fora do Terraform no AWS WAF bloqueou tráfego legítimo do CircleCI e foi inicialmente ignorada porque não aparecia no pipeline; os outros incidentes envolvem filas, banco de dados, deploys ou regras de WAF com mecanismo diferente.
  - DAN-004 (llm) [**Root Cause Analysis**] 0.769: ## **Root Cause Analysis**  While we manage all our infrastructure, including WAF, almost entirely with Terraform, we discovered during this incident a misconfiguration in IAM controls that allowed a 
  - DAN-004 (llm) [Future Prevention and Process Improvement] 0.695: ## Future Prevention and Process Improvement  This incident highlighted the strength of our existing systems while identifying several areas where we can improve and make them even more robust:  1. We
  - DAN-004 (causa) [Summary] 0.416: ## Summary  On April 4, 2025, from 00:16 to 01:49 UTC (approximately 1 hour and 33 minutes), CircleCI experienced a service disruption affecting both our user interface and build capabilities. During 
  - DAN-004 (correcao) [What Happened] 0.473: ## What Happened  - **01:15:** Initial investigation revealed broad connectivity issues between the frontend and our backing APIs, including CORS (Cross-Origin Resource Sharing) errors. The team explo
  - DAN-004 (correcao) [What Happened] 0.435: ## What Happened  (all times UTC)  The WAF is a critical security component that sits in front of our services and protects them from malicious traffic, while allowing legitimate requests to pass thro

## q-026 (esperado: DAN-011)

- busca inicial: DAN-011, DAN-005, DAN-019, DAN-016, DAN-007, DAN-012, DAN-049, DAN-035, DAN-008, DAN-018
- justificativa: 
- aprofundar DAN-011: `bot detection file output exceeded limits propagation outage fix rollback` — Sistema de detecção de bots (filtragem de tráfego) gera um arquivo que se propaga globalmente e causa outage sistêmico, semelhante a um arquivo de configuração de filtro de tráfego gerado automaticamente derrubando o CDN mundialmente.
- aprofundar DAN-016: `DDoS mitigation rule rate limiting infinite loop CPU fix rollback` — Regra recém implantada de mitigação DDoS (filtragem de tráfego) causa erros que se propagam entre datacenters, similar a uma configuração de filtro de tráfego push global derrubando o CDN.
- aprofundar DAN-012: `WAF configuration change propagated globally HTTP 500 proxy rulesets fix` — Mudança de configuração do WAF propagada globalmente causa erros HTTP 500 no proxy, parecido com uma configuração de filtro de tráfego gerada automaticamente derrubando o CDN globalmente.
  - DAN-011 (llm) [Remediation and follow-up steps] 0.666: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [Memory preallocation] 0.581: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-016 (llm) [Remediation and follow-up steps] 0.675: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.658: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-012 (llm) [What happened] 0.715: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (llm) [What happened] 0.71: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 

## q-028 (esperado: DAN-137)

- busca inicial: DAN-016, DAN-137, DAN-148, DAN-005, DAN-064, DAN-183, DAN-106, DAN-035, DAN-129, DAN-115
- justificativa: 
- aprofundar DAN-016: `DDoS mitigation rule cookie validation infinite loop CPU fix` — Bate: regra de segurança recém-implantada, 100% CPU e propagação global em edge/data centers. Não bate: foco em validação de cookie e rate limiting, não regex de WAF.
- aprofundar DAN-137: `WAF rule regex backtracking CPU exhaustion fix rollback` — Bate: regra WAF (segurança) implantada em produção, exaustão de CPU e downtime global. Não bate: causa é backtracking de regex, não menciona ter passado em testes.
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.721: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.697: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-137 (llm) [Appendix: About Regular Expression Backtracking] 0.726: ### Appendix: About Regular Expression Backtracking  To fully understand how ``(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*
  - DAN-137 (llm) [The events of July 2] 0.723: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [sem seção] 0.482: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-030 (esperado: DAN-078)

- busca inicial: DAN-078, DAN-066, DAN-048, DAN-164, DAN-006, DAN-075, DAN-043, DAN-205, DAN-060, DAN-058
- justificativa: 
- aprofundar DAN-078: `cross region database failover divergent writes replication latency recovery` — Mesma falha: pane de rede entre regiões provocou failover de MySQL master e writes não replicaram, exigindo restauração de integridade de dados.
- aprofundar DAN-205: `network latency between data centers quorum failure connectivity` — Conectividade instável entre data centers causou falha de quorum, mas não envolve banco de dados nem writes divergentes.
- aprofundar DAN-048: `RDS MySQL failover hardware failure configuration data loss recovery` — Falha em RDS/MySQL causou perda de dados, mas o gatilho foi hardware e config incorreta, não pane de rede entre regiões.
  - DAN-078 (llm) [2018 October 22 11:12 UTC] 0.708: ## 2018 October 22 11:12 UTC  All database primaries established in US East Coast again. This resulted in the site becoming far more responsive as writes were now directed to a database server that wa
  - DAN-078 (llm) [Incident timeline] 0.697: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-205 (llm) [The Outage] 0.664: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Background] 0.618: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (causa) [Long term] 0.47: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Outage Post-Mortem – April 13, 2013] 0.374: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-048 (llm) [Incorrect configuration variable] 0.781: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Final thoughts] 0.744: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m

## q-032 (esperado: DAN-104)

- busca inicial: DAN-109, DAN-210, DAN-189, DAN-191, DAN-067, DAN-073, DAN-104, DAN-103, DAN-026, DAN-070
- justificativa: 
- aprofundar DAN-104: `typo command remove servers S3 outage recovery root cause fix` — Bate: operador executou comando de rotina para remover poucos servidores e derrubou serviço de armazenamento (S3); não bate: foi erro de digitação que removeu mais servidores, e não falha de recuperação automática.
- aprofundar DAN-189: `operator reboot servers lax input validation all servers datacenter outage recovery fix` — Bate: operador usou ferramenta com validação frouxa afetando mais servidores que o previsto; não bate: reboot em vez de remoção, e não é serviço de armazenamento.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.667: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.667: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.677: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.625: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-034 (esperado: DAN-004)

- busca inicial: DAN-005, DAN-137, DAN-051, DAN-012, DAN-220, DAN-011, DAN-016, DAN-014, DAN-006, DAN-113
- justificativa: 
- aprofundar DAN-051: `firewall configuration iptables change root cause fix` — O sintoma é idêntico: uma mudança incorreta na configuração de firewall (iptáveis) bloqueou todo o tráfego dos sites da Stack Exchange, enquanto o incidente atual também envolve tráfego bloqueado por regra de firewall sem mudança lembrada.
- aprofundar DAN-137: `WAF rule regex backtracking root cause fix` — Envolve uma regra de WAF (firewall de aplicação) que causou queda global, mas a causa foi esgotamento de CPU por expressão regular, não bloqueio direto de tráfego por regra de firewall.
  - DAN-051 (llm) [sem seção] 0.607: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-051 (llm) [sem seção] 0.604: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-137 (llm) [sem seção] 0.697: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (llm) [The events of July 2] 0.668: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [What happened] 0.441: ### What happened  Let’s begin with the sequence of events. All times in this blog are UTC.  At 13:42 an engineer working on the firewall team deployed a minor change to the rules for XSS detection vi
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-036 (esperado: DAN-019)

- busca inicial: DAN-019, DAN-007, DAN-005, DAN-006, DAN-059, DAN-022, DAN-023, DAN-210, DAN-159, DAN-013
- justificativa: 
- aprofundar DAN-019: `BGP export policy prefix list filter route leak root cause fix` — Bate pelo sintoma de anunciar prefixos internos a peers após erro em política de exportação BGP; não bate por ser IPv6 específico da Cloudflare.
- aprofundar DAN-007: `BGP advertised prefixes ordering routing policy root cause fix` — Bate por envolver ordem incorreta de prefixos anunciados em políticas BGP; não bate por afetar datacenters internos em vez de peers externos.
- aprofundar DAN-023: `backbone router configuration change routing outage root cause fix` — Bate pelo gatilho de mudança de configuração em roteadores de backbone; não bate por causar outage global sem menção a anúncio inadequado de rotas.
  - DAN-019 (llm) [What happened: the configuration error] 0.745: ### What happened: the configuration error  [edit policy-options policy-statement 6-PRIVATE-PEER-ANYCAST-OUT term ADV-SITELOCAL from] -      prefix-list 6-BOG04-SITE-LOCAL; [edit policy-options policy
  - DAN-019 (llm) [What happened: the configuration error] 0.714: ### What happened: the configuration error  ``` policy-options policy-statement 6-TELIA-ACCEPT-EXPORT {     term ADV-SITELOCAL-GRE-RECEIVER {         from route-type internal;         then {          
  - DAN-019 (causa) [What happened: the configuration error] 0.381: ### What happened: the configuration error  A|1769113609.854028|2801:14:9000::6:4112:1|64112|2a03:2880:f17c::/48|64112 22850 174 3356 13335 32934|IGP|2801:14:9000::6:4112:1|0|0|22850:65151|false|||pit
  - DAN-019 (correcao) [Follow-ups and preventing route leaks] 0.369: ### Follow-ups and preventing route leaks  We are big supporters and active contributors to efforts within the <u>IETF</u> and <u>infrastructure community</u> that strengthen routing security. We know
  - DAN-019 (correcao) [Timeline] 0.398: ### Timeline  | Time (UTC) | Event | |---|---| | 2026-01-22 19:52 UTC | A change that ultimately triggers the routing policy bug is merged in our network automation code repository | | 2026-01-22 20:2
  - DAN-007 (llm) [Incident timeline and impact] 0.706: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.627: ### Technical description of the error and how it happened  ``` [edit policy-options policy-statement 4-COGENT-TRANSIT-OUT term ADV-SITELOCAL then] +      community add STATIC-ROUTE; +      community 
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-023 (llm) [sem seção] 0.6: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.594: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-038 (esperado: DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-221, DAN-154, DAN-015, DAN-066, DAN-220, DAN-010, DAN-129, DAN-148
- justificativa: 
- aprofundar DAN-086: `certificate expiration root cause fix leap year date` — Envolve certificados expirados causando falha geral de clientes, igual ao incidente atual; difere no gatilho (bug de ano bissexto).
- aprofundar DAN-090: `certificate expired root cause fix add-ons outage` — Certificado expirado derrubou todos os clientes/extensions ao mesmo tempo, muito parecido com o incidente atual; difere no componente (add-ons do Firefox).
  - DAN-086 (llm) [The Leap Day Bug] 0.62: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.539: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.675: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.62: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (causa) [sem seção] 0.366: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q-164 (esperado: DAN-001)

- busca inicial: DAN-001, DAN-129, DAN-024, DAN-162, DAN-067, DAN-209, DAN-218, DAN-186, DAN-119, DAN-148
- justificativa: 
- aprofundar DAN-001: `cluster resource management configuration error prevent starting instances traffic spike` — Bate com o atual: queda após campanha de marketing, tráfego disparado e impossibilidade de subir mais instâncias embora houvesse hardware disponível. Não bate: é um postmortem específico do Allegro, com detalhes de cluster próprios deles.
- aprofundar DAN-148: `extreme load concurrent users service disruption root cause fix` — Bate parcialmente: pico extremo de usuários simultâneos com disrupções totais e parciais. Não bate: o resumo não menciona máquinas ociosas nem impedimento de iniciar instâncias por configuração.
- aprofundar DAN-218: `network saturation scale up caused issues root cause fix` — Bate parcialmente: tentativa de escalar piorou a situação com perda de pacotes. Não bate: não há campanha de marketing nem máquinas sobrando enquanto faltava capacidade de instâncias.
  - DAN-001 (llm) [Analysis #] 0.691: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (llm) [Outage timeline #] 0.689: ## Outage timeline #  Also just before noon, traffic peaked at 200%-300% of the traffic from previous day, depending on service. At this stage, traffic was at its highest but due to excessive resource
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa
  - DAN-148 (llm) [**XMPP outage**] 0.669: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (llm) [**Account Service outage**] 0.665: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-218 (llm) [sem seção] 0.639: Unfortunately, our scale-up did not work as intended. We run a service, aptly named ‘provision-service’, which does exactly what it says on the tin. It is responsible for configuring and testing new i
  - DAN-218 (llm) [sem seção] 0.62: Once provision-service was back in operation (around 8:15am PST) we began to see an improvement as healthy instances entered service. We still had some less-critical production issues which were mitig
  - DAN-218 (causa) [sem seção] 0.459: To narrow down the list of possible causes we quickly rolled back some changes that had been pushed out that day (turned out they weren’t the issue). We pulled in several more people from our infrastr
  - DAN-218 (correcao) [sem seção] 0.391: AWS assures us that they are reviewing the TGW scaling algorithms for large packet-per-second increases as part of their post-incident process. We’ve also set ourselves a reminder (a Slack reminder, o
  - DAN-218 (correcao) [sem seção] 0.383: *And now we welcome the new year. Full of things that have never been.*  *— Rainer Maria Rilke*  January 4th 2021 was the first working day of the year for many around the globe, and for most of us at

## q-165 (esperado: DAN-001)

- busca inicial: DAN-001, DAN-129, DAN-218, DAN-210, DAN-148, DAN-067, DAN-208, DAN-220, DAN-209, DAN-073
- justificativa: 
- aprofundar DAN-001: `cluster resource management configuration error prevent start instances traffic spike fix` — O incidente atual tem pico de tráfego por campanha de marketing e impossibilidade de iniciar novas instâncias apesar de máquinas livres, exatamente como o Allegro, mas preciso da causa raiz e da correção detalhadas.
  - DAN-001 (llm) [Analysis #] 0.69: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (llm) [Outage timeline #] 0.688: ## Outage timeline #  Also just before noon, traffic peaked at 200%-300% of the traffic from previous day, depending on service. At this stage, traffic was at its highest but due to excessive resource
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa

## q-166 (esperado: DAN-003)

- busca inicial: DAN-003, DAN-092, DAN-103, DAN-164, DAN-134, DAN-133, DAN-180, DAN-195, DAN-102, DAN-056
- justificativa: 
- aprofundar DAN-003: `schema change job distribution service rollback recovery fix offending field` — Bate com o incidente atual: deploy alterou schema do banco, distribuidor de jobs parou, rollback não resolveu e a recuperação exigiu build que ignorava o campo problemático. Não bate apenas no detalhe do campo específico, mas a estrutura do incidente é a mesma.
  - DAN-003 (llm) [What happened] 0.684: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Background] 0.512: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.348: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe

## q-167 (esperado: DAN-003)

- busca inicial: DAN-003, DAN-092, DAN-134, DAN-164, DAN-130, DAN-103, DAN-180, DAN-091, DAN-116, DAN-066
- justificativa: 
- aprofundar DAN-003: `database schema field type change job distribution rollback recovery fix` — Bate: deploy alterou esquema do banco, serviço de distribuição parou e rollback não ajudou — quase idêntico ao incidente atual.
- aprofundar DAN-092: `database statistics tables stale ANALYZE query planner recovery fix` — Bate: envolve banco de dados e atraso em workflows; não bate: causa foi estatísticas desatualizadas, não mudança de esquema.
- aprofundar DAN-134: `RabbitMQ consumer acknowledgment timeout channel closed recovery fix` — Bate: distribuição de trabalhos foi bloqueada; não bate: gatilho foi upgrade do RabbitMQ, não alteração de esquema do banco.
  - DAN-003 (llm) [What happened] 0.688: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.503: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s
  - DAN-092 (llm) [What Happened] 0.692: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.542: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-134 (llm) [Contributing Event:] 0.664: ## Contributing Event:  On May 20th, we upgraded RabbitMQ from 3.8.9 to 3.8.16 as part of routine upgrades. As usual, the team checked the changelog to ensure there were no breaking changes listed and
  - DAN-134 (llm) [What Happened] 0.572: ## What Happened  At this time there was confidence that the system was in a stable state and everyone dispersed to get some much-needed rest. This incident involved folks from EMEA and NA and came cl
  - DAN-134 (causa) [What Happened] 0.473: ## What Happened  The system had become “wedged” and we had found ourselves in a vicious cycle of creating VMs and then not being able to remove them due to hitting our GCP quotas. In order to break o
  - DAN-134 (correcao) [Resolution and future prevention:] 0.445: ## Resolution and future prevention:  This was a long-running incident with numerous follow-on effects. Remediation falls into two broad categories: detecting this specific failure sooner and improvin
  - DAN-134 (correcao) [What Happened] 0.404: ## What Happened  (all times UTC)  On the 20th of May at 08:37, CircleCI engineers performed routine maintenance on our RabbitMQ cluster and upgraded to version 3.8.16 from 3.8.9. The upgrade was succ

## q-168 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-066, DAN-008, DAN-050, DAN-129, DAN-067, DAN-211, DAN-020, DAN-016
- justificativa: 
- aprofundar DAN-017: `deployment tool bug staging build production 401 unauthorized endpoint root cause fix` — O deploy foi o gatilho, o serviço central passou a retornar 401 para todas as requisições e houve falha em cascata em produtos dependentes — igual ao incidente atual. Difere por envolver um build de staging referenciado por engano na produção.
- aprofundar DAN-016: `deployed DDoS rule rate limiting cookie validation infinite loop fix` — Houve um deploy recente como gatilho, mas a falha foi loop de CPU por validação de cookie, não 401 generalizado em serviço central.
- aprofundar DAN-050: `deployment bug download URL generation broken crate downloads fix` — Houve um deploy com bug que quebrou requisições, mas o sintoma foi download de crates quebrado, não 401 em serviço central.
  - DAN-017 (llm) [Analysis] 0.571: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Analysis] 0.554: ### Analysis  Workers KV is a low-latency key-value store that allows users to store persistent data on Cloudflare's network, as close to the users as possible. This distributed key-value store is use
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.777: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.737: ## Technical description of the error and how it happened  ``` for (rule in active_mitigations) {    // ... (ignore other rule types)    if (rule.match_current_request()) {        if (!has_valid_cooki
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Remediation and follow-up steps] 0.472: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-050 (llm) [Summary] 0.768: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (llm) [2023-07-20] 0.759: ### 2023-07-20  - 12:24 UTC – https://github.com/rust-lang/crates.io/issues/6850 (Crates.io crate download API is redirecting to invalid URL) was opened - 12:25 UTC – The continuing request-per-second
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Recovery] 0.488: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 

## q-169 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-067, DAN-211, DAN-183, DAN-016, DAN-020, DAN-129, DAN-050, DAN-066
- justificativa: 
- aprofundar DAN-017: `deploy staging build 401 unauthorized endpoint root cause fix` — Deploy causou erro 401 generalizado e falhas em cascata em produtos dependentes, correspondendo diretamente ao incidente atual.
  - DAN-017 (llm) [Analysis] 0.531: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Resolution] 0.518: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.

## q-170 (esperado: DAN-018)

- busca inicial: DAN-144, DAN-066, DAN-017, DAN-018, DAN-029, DAN-191, DAN-102, DAN-037, DAN-067, DAN-154
- justificativa: 
- aprofundar DAN-018: `React dashboard excessive API calls dependency array root cause fix` — O resumo menciona um bug de componente React no painel que gerou chamadas excessivas de API para um serviço interno (Tenant Service), derrubando API e painel após mudança no frontend — corresponde diretamente ao incidente atual, que também envolve chamadas do próprio painel após deploy do frontend.
  - DAN-018 (llm) [Improving visibility] 0.656: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (llm) [What Happened] 0.651: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 

## q-171 (esperado: DAN-018)

- busca inicial: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-133, DAN-129, DAN-218, DAN-145, DAN-220
- justificativa: 
- aprofundar DAN-018: `React component bug dashboard excessive API calls dependency array fix` — O dashboard gera chamadas excessivas para um serviço interno após deploy frontend, igual ao bug de componente React com dependency array mal configurado que sobrecarregou o Tenant Service e derrubou API e dashboard; é o padrão mais próximo do incidente atual.
- aprofundar DAN-067: `thundering herd API calls overwhelmed internal service rate limits fix` — Ambos envolvem um serviço sendo inundado de chamadas de API (manada) que sobrecarrega o sistema, mas lá o gatilho foi falha de energia no data center, não um deploy de frontend.
- aprofundar DAN-144: `thundering herd reconnecting frontend services internal queues cascading failure fix` — Há rebanho de conexões e impacto em serviços frontend com filas internas, mas o alagamento vem de clientes reconectando, não do dashboard chamando um serviço interno após deploy.
  - DAN-018 (llm) [What Happened] 0.679: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.647: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-067 (llm) [Disaster Recovery] 0.643: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.519: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-144 (llm) [Summary] 0.573: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.565: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 

## q-172 (esperado: DAN-020)

- busca inicial: DAN-020, DAN-220, DAN-205, DAN-066, DAN-109, DAN-145, DAN-222, DAN-067, DAN-113, DAN-144
- justificativa: 
- aprofundar DAN-020: `service discovery config dependent client global outage root cause fix` — Bate quase exatamente: descoberta de serviço caiu globalmente quando um cliente dependente caiu; não se sabe ainda se a causa é uma configuração ruim do cliente como naquele incidente.
  - DAN-020 (llm) [The failure of a core system] 0.71: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.684: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter

## q-173 (esperado: DAN-020)

- busca inicial: DAN-020, DAN-220, DAN-066, DAN-145, DAN-109, DAN-205, DAN-211, DAN-067, DAN-222, DAN-208
- justificativa: 
- aprofundar DAN-020: `service discovery global outage root cause dependent client config fix remediation` — O resumo diz exatamente o mesmo padrão: service discovery caiu globalmente quando um cliente dependente caiu, devido a uma config ruim de service discovery em um cliente. É o mais parecido com o incidente atual.
  - DAN-020 (llm) [The failure of a core system] 0.691: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.666: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter

## q-174 (esperado: DAN-022)

- busca inicial: DAN-022, DAN-065, DAN-059, DAN-113, DAN-159, DAN-129, DAN-007, DAN-006, DAN-209, DAN-068
- justificativa: 
- aprofundar DAN-022: `multicast traffic switch misconfiguration outage root cause fix` — O resumo menciona exatamente tráfego multicast sem configuração adequada de switches causando um outage global, igual ao incidente atual; nenhum outro incidente cita multicast.
  - DAN-022 (llm) [Multicast Rsync?] 0.569: ### Multicast Rsync?  If we need to get the same bits to all of the boxes, why not send the index via multicast to the replicas? It sure would be nice to only send the data once. We found an implement
  - DAN-022 (llm) [The Index Replication Issue] 0.361: ### The Index Replication Issue  To keep all of the searches on our site working fast we optimize our indexes nightly. Index optimization creates a completely new copy of the index. As we added new bo
  - DAN-022 (causa) [Search at Etsy] 0.27: ### Search at Etsy  Search at Etsy has grown significantly over the years. In January of 2009 we started using Solr for search. We used the standard primary-replica configuration for our search server
  - DAN-022 (correcao) [Improvements] 0.279: ### Improvements  To better deal with the transfer lag we are looking at creating a Torrent file per index segment. Lucene indexes are made up of various segments. Each commit creates an index segment
  - DAN-022 (correcao) [How it Works] 0.273: ### How it Works  HTTP replication doesn’t allow for the transfer of older versions of a given index. This causes issues with some of our static indexes. When we bring up new replicas, Solr creates a 

## q-175 (esperado: DAN-022)

- busca inicial: DAN-022, DAN-159, DAN-077, DAN-113, DAN-059, DAN-209, DAN-078, DAN-109, DAN-148, DAN-006
- justificativa: 
- aprofundar DAN-022: `multicast traffic switch configuration misconfiguration outage fix` — Descreve tráfego multicast que causou pane global na rede, igual ao incidente atual, embora o contexto seja replicação de índice Solr.
  - DAN-022 (llm) [Multicast Rsync?] 0.549: ### Multicast Rsync?  If we need to get the same bits to all of the boxes, why not send the index via multicast to the replicas? It sure would be nice to only send the data once. We found an implement
  - DAN-022 (llm) [The Index Replication Issue] 0.346: ### The Index Replication Issue  To keep all of the searches on our site working fast we optimize our indexes nightly. Index optimization creates a completely new copy of the index. As we added new bo
  - DAN-022 (causa) [Search at Etsy] 0.27: ### Search at Etsy  Search at Etsy has grown significantly over the years. In January of 2009 we started using Solr for search. We used the standard primary-replica configuration for our search server
  - DAN-022 (correcao) [Improvements] 0.279: ### Improvements  To better deal with the transfer lag we are looking at creating a Torrent file per index segment. Lucene indexes are made up of various segments. Each commit creates an index segment
  - DAN-022 (correcao) [How it Works] 0.273: ### How it Works  HTTP replication doesn’t allow for the transfer of older versions of a given index. This causes issues with some of our static indexes. When we bring up new replicas, Solr creates a 

## q-176 (esperado: DAN-026)

- busca inicial: DAN-026, DAN-020, DAN-010, DAN-162, DAN-087, DAN-137, DAN-049, DAN-075, DAN-002, DAN-065
- justificativa: 
- aprofundar DAN-026: `DNS zone corruption NXDOMAIN after IP change fix` — Bate fortemente: troca de IP, timeouts de consulta e NXDOMAIN em massa gerados por zona reconstruída via API que depende de DNS — mesmo padrão do incidente atual.
- aprofundar DAN-162: `DNS resolution broken after migration recovery fix` — DNS parou de funcionar após uma mudança de infraestrutura e a recuperação caiu em cascata, semelhante à falha de DNS pós-mudança atual, embora o gatilho seja uma migração de banco e não troca de IP.
- aprofundar DAN-002: `DNS resolver config change query failure fix` — Mudança de configuração derrubou consultas DNS, mas não gera NXDOMAIN nem envolve troca de IP; serve como contraste de causa e correção de resolvedor.
  - DAN-026 (llm) [What happened…] 0.747: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.658: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-162 (llm) [sem seção] 0.564: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.562: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We’d like to give you some additional information about the service disruption that occurred in 
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.558: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We are taking multiple steps to prevent recurrence of this issue, some of which are already comp

## q-177 (esperado: DAN-026)

- busca inicial: DAN-026, DAN-020, DAN-087, DAN-162, DAN-075, DAN-010, DAN-049, DAN-137, DAN-081, DAN-002
- justificativa: 
- aprofundar DAN-026: `DNS NXDOMAIN IP change root cause fix zone file` — Bate IP change, timeouts e NXDOMAIN; não bate memória nos fileservers.
- aprofundar DAN-002: `DNS resolver configuration change root cause fix` — Bate mudança de configuração e falha de DNS interno; não bate IP change nem NXDOMAIN.
- aprofundar DAN-0162: `DNS resolution database migration root cause fix` — Bate quebra de resolução DNS após mudança; não bate IP change nem NXDOMAIN.
- aviso: DAN-0162 não está entre os incidentes encontrados; ignorado.
  - DAN-026 (llm) [What happened…] 0.732: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.653: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.576: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We’d like to give you some additional information about the service disruption that occurred in 
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.549: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We are taking multiple steps to prevent recurrence of this issue, some of which are already comp

## q-178 (esperado: DAN-033)

- busca inicial: DAN-033, DAN-191, DAN-221, DAN-205, DAN-195, DAN-222, DAN-165, DAN-161, DAN-231, DAN-106
- justificativa: 
- aprofundar DAN-033: `quota service bad config failure root cause fix` — É o único incidente que menciona falha de serviço de cotas derrubando vários serviços incluindo Gmail, igual ao incidente atual, embora seja do projeto Chromium.
  - DAN-033 (llm) [sem seção] 0.472: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fre
  - DAN-033 (llm) [sem seção] 0.414: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  enu
  - DAN-033 (causa) [sem seção] 0.294: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  .cc
  - DAN-033 (correcao) [sem seção] 0.248: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fie
  - DAN-033 (correcao) [sem seção] 0.247: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  kno

## q-179 (esperado: DAN-033)

- busca inicial: DAN-033, DAN-191, DAN-218, DAN-147, DAN-144, DAN-220, DAN-148, DAN-205, DAN-221, DAN-109
- justificativa: 
- aprofundar DAN-033: `quota service bad config failure mitigation fix` — Bate diretamente: serviço de cota falhou por má configuração e derrubou serviços dependentes incluindo e-mail/Gmail, exatamente como o incidente atual. Não há outro incidente na lista que mencione serviço de cota.
  - DAN-033 (llm) [sem seção] 0.464: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fre
  - DAN-033 (llm) [sem seção] 0.416: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  enu
  - DAN-033 (causa) [sem seção] 0.294: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  .cc
  - DAN-033 (correcao) [sem seção] 0.248: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fie
  - DAN-033 (correcao) [sem seção] 0.247: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  kno

## q-180 (esperado: DAN-042)

- busca inicial: DAN-042, DAN-035, DAN-049, DAN-032, DAN-015, DAN-020, DAN-033, DAN-048, DAN-029, DAN-017
- justificativa: 
- aprofundar DAN-042: `deployment config variable missing root cause fix` — O resumo diz exatamente que variáveis de configuração novas não foram usadas quando o código as exigiu, igual ao incidente atual. Difere por ser no Heroku, mas o padrão de deploy/config ausente é o mesmo.
- aprofundar DAN-015: `credentials omitted environment default production root cause fix` — Envolve credenciais que faltaram no ambiente onde eram necessárias após deploy, parecido com variável de config ausente. Difere porque é credencial R2, não variável genérica de config.
- aprofundar DAN-032: `bad autogenerated config outage root cause fix` — Envolve configuração ruim que derrubou serviços, mas não menciona variável ausente específica após deploy, então é menos parecido.
  - DAN-042 (llm) [It was such a nice morning] 0.633: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Houston, we have a problem] 0.605: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Did I mess up?] 0.334: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-015 (llm) [Incident timeline] 0.594: ## Incident timeline  **All timestamps referenced are in Coordinated Universal Time (UTC).**  | Time | Event | |---|---| | Mar 21, 2025 - 19:49 UTC | The R2 engineering team started the credential rot
  - DAN-015 (llm) [Incident timeline] 0.565: ## Incident timeline  Given gradual decline in availability metrics, R2 engineering team suspected a potential regression in propagation of new credentials in storage infrastructure. | | Mar 21, 2025 
  - DAN-015 (causa) [Next steps] 0.493: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [Next steps] 0.468: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor
  - DAN-032 (llm) [Today’s outage for several Google services] 0.562: # Today’s outage for several Google services  Earlier today, most Google users who use logged-in services like Gmail, Google+, Calendar and Documents found they were unable to access those services fo
  - DAN-032 (llm) [Today’s outage for several Google services] 0.555: # Today’s outage for several Google services  With services once again working normally, our work is now focused on (a) removing the source of failure that caused today’s outage, and (b) speeding up r

## q-181 (esperado: DAN-042)

- busca inicial: DAN-042, DAN-035, DAN-220, DAN-020, DAN-049, DAN-029, DAN-154, DAN-050, DAN-102, DAN-055
- justificativa: 
- aprofundar DAN-042: `deployment config variable not used code required fix rollback` — Bate por envolver um deploy em que novas variáveis de configuração exigidas pelo código não foram aplicadas; não bate porque o resumo diz que não foram usadas, não que estavam ausentes nas instâncias.
- aprofundar DAN-055: `configuration change builds fail manual rollback broke fix` — Bate por uma mudança de configuração quebrar builds após deploy; não bate porque não se trata de variável ausente nas instâncias e o rollback manual quebrou.
- aprofundar DAN-050: `deployment bug download URL generation broken fix` — Bate por um deploy que quebrou o serviço por um bug no código implantado; não bate porque não envolve variável de configuração ausente.
  - DAN-042 (llm) [It was such a nice morning] 0.646: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Did I mess up?] 0.643: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-055 (llm) [So what happened?] 0.585: ## So what happened?  Thursday Feb 2nd, we started rolling out a new worker version (v2.6.2) on EC2, for sudo: false, container-based builds.  Friday Feb 3rd, we identified an issue with jobs being in
  - DAN-055 (llm) [So what happened?] 0.55: ## So what happened?  We also learned we did not have alerting which included the errors logged when the image pulls were failing to find v2.5.0.  Sunday, Feb 5th, in order to more quickly eliminate t
  - DAN-055 (causa) [Contributing Factors] 0.437: ## Contributing Factors  The major contributing factors in this outage were  - A change in how our worker's docker backend executes build scripts, so that bash is run explicitly with a login shell. Th
  - DAN-055 (correcao) [Going forward?] 0.437: ## Going forward?  - As part of the incident resolution, we created additional alerting, so that we know we'll be notified about similar errors in the future.  - We are discussing both incremental and
  - DAN-055 (correcao) [Summary] 0.424: ## Summary  We couldn't be more sorry about this incident and the impact that the build outages and delays had on you, our users and customers. We always use problems like these as an opportunity for 
  - DAN-050 (llm) [Recovery] 0.71: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Summary] 0.652: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-182 (esperado: DAN-043)

- busca inicial: DAN-043, DAN-146, DAN-056, DAN-164, DAN-048, DAN-210, DAN-186, DAN-058, DAN-066, DAN-209
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup recovery fix` — Bate por exclusão acidental do banco de produção e perda de horas de dados por backup antigo, mas difere no provedor (DigitalOcean).
- aprofundar DAN-056: `accidental environment variable truncate production database fix` — Bate por exclusão/truncamento acidental do banco de produção, mas difere no gatilho (variável de ambiente em testes).
- aprofundar DAN-164: `admin deleted wrong directory database recovery fix` — Bate por exclusão acidental de diretório/banco e perda de horas de dados, mas difere pelo contexto (replication lag antes da exclusão).
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.734: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.661: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [What We Learned] 0.732: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.72: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a
  - DAN-164 (llm) [Root cause analysis] 0.59: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.559: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-183 (esperado: DAN-043)

- busca inicial: DAN-043, DAN-164, DAN-056, DAN-186, DAN-146, DAN-091, DAN-058, DAN-066, DAN-048, DAN-210
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup recovery` — Exclusão acidental de banco de produção com backup diário e perda de horas de dados, idêntica ao incidente atual.
- aprofundar DAN-164: `deleted wrong directory database outage recovery fix` — Admin apagou o diretório errado e perdeu seis horas de dados, similar à exclusão acidental com backup antigo.
- aprofundar DAN-056: `environment variable truncate production database fix` — Variável de ambiente acidental truncou o banco de produção, parecido com a perda acidental de dados do banco.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.728: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.664: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Root cause analysis] 0.671: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.653: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [Remediation] 0.717: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (llm) [What We Learned] 0.714: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-184 (esperado: DAN-048)

- busca inicial: DAN-048, DAN-066, DAN-078, DAN-195, DAN-209, DAN-164, DAN-234, DAN-043, DAN-190, DAN-146
- justificativa: 
- aprofundar DAN-048: `RDS hardware failure MySQL data loss failover financial system root cause fix` — Bate por ser falha de hardware em MySQL gerenciado (RDS) com perda de dados em sistema financeiro; não bate se a causa foi configuração incorreta e não exatamente replicação assíncrona no failover.
- aprofundar DAN-078: `MySQL master failover missing writes data integrity restoration fix` — Bate por failover MySQL com writes recentes não propagados e restauração de integridade; não bate porque o gatilho foi partição de rede, não falha de hardware.
- aprofundar DAN-164: `database replication lag data loss root cause fix` — Bate por perda de dados associada a lag de replicação; não bate porque causado por exclusão humana de diretório, não failover de hardware.
  - DAN-048 (llm) [Incorrect configuration variable] 0.763: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Data loss] 0.758: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-048 (causa) [Final thoughts] 0.515: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Replication failure] 0.351: ## Replication failure  So, we had no other option but wait for the snapshots to finish and keep monitoring the master instance in the meantime. We waited six hours for the snapshot to complete and on
  - DAN-078 (llm) [Next steps] 0.688: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.662: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (causa) [Incident timeline] 0.478: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [2018 October 22 16:24 UTC] 0.479: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-164 (llm) [Root cause analysis] 0.746: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.703: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-185 (esperado: DAN-048)

- busca inicial: DAN-048, DAN-066, DAN-078, DAN-164, DAN-043, DAN-181, DAN-094, DAN-093, DAN-096, DAN-190
- justificativa: 
- aprofundar DAN-048: `RDS hardware failure MySQL configuration data loss fix` — Bate por falha de hardware no RDS gerenciado, failover e perda de dados em sistema financeiro; não bate por a causa raiz ser configuração incorreta do MySQL e não falha de hardware pura.
- aprofundar DAN-078: `MySQL master failover missing writes latency fix` — Bate por failover do MySQL master com writes recentes não propagados para o novo master; não bate por ser particionamento de rede durante manutenção, não falha de hardware.
- aprofundar DAN-093: `MySQL failover stale node data drift fix` — Bate por failover para nó desatualizado causando perda/drift de dados recentes; não bate por ser desencadeado por migração de schema e Pacemaker, não falha de hardware.
  - DAN-048 (llm) [Final thoughts] 0.759: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (llm) [Incorrect configuration variable] 0.721: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.628: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [2018 October 22 11:12 UTC] 0.613: ## 2018 October 22 11:12 UTC  All database primaries established in US East Coast again. This resulted in the site becoming far more responsive as writes were now directed to a database server that wa
  - DAN-078 (causa) [Incident timeline] 0.478: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-093 (llm) [Monday, September 10th] 0.651: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.639: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-186 (esperado: DAN-049)

- busca inicial: DAN-049, DAN-073, DAN-026, DAN-109, DAN-162, DAN-050, DAN-208, DAN-024, DAN-129, DAN-164
- justificativa: 
- aprofundar DAN-049: `static domain DNS resolution failure deployment infrastructure certificates DNS records` — Mesmo gatilho (deploy de infraestrutura) e mesmo sintoma (domínio static.* parou de resolver), embora o componente seja crates.io.
- aprofundar DAN-026: `DNS outage deployment authoritative nameserver zone file corrupt NXDOMAIN fix` — DNS outage durante um deploy com reconstrução de zone, mas foco em nameserver autoritativo e não especificamente em arquivos estáticos.
- aprofundar DAN-162: `database migration broke DNS resolution recovery cascading temporary resolvers fix` — DNS resolution quebrada por mudança de deploy com cascata, mas em banco de dados e sites, não em domínio de arquivos estáticos.
  - DAN-049 (llm) [Resolution] 0.688: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [Root Cause of the Outage] 0.68: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (causa) [Postmortem] 0.443: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat
  - DAN-026 (llm) [What happened…] 0.804: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [Total number of processes across fileservers] 0.679: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (causa) [What we’re doing about it…] 0.461: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [Summary] 0.443: # Summary  We realize that GitHub is an important part of your development and workflow. Again, I would like to take a moment to apologize for the impact that this outage had to your operations. We ta
  - DAN-162 (llm) [sem seção] 0.53: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5

## q-187 (esperado: DAN-049)

- busca inicial: DAN-049, DAN-026, DAN-020, DAN-162, DAN-050, DAN-210, DAN-073, DAN-010, DAN-129, DAN-208
- justificativa: 
- aprofundar DAN-049: `static crates.io DNS record deployment certificate recreation fix` — O domínio static.crates.io parou de resolver durante deploy de infraestrutura, igual ao incidente atual; difere porque certificados e registros DNS foram recriados juntos.
- aprofundar DAN-050: `download URL generation deployment bug crate downloads fix` — Downloads quebrados após deploy, sintoma semelhante, mas causa é bug na geração de URL de download e não falha de DNS do domínio estático.
- aprofundar DAN-026: `DNS outage deploy Puppet nameserver zone file corrupt fix` — Indisponibilidade DNS provocada por mudança/deploy, se acerca da falha de resolução, mas o mecanismo é reinicialização de nameserver e zona corrompida, não domínio de arquivos estáticos.
  - DAN-049 (llm) [Postmortem] 0.703: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (llm) [Root Cause of the Outage] 0.69: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (causa) [Postmortem] 0.4: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [Resolution] 0.401: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat
  - DAN-050 (llm) [2023-07-20] 0.71: ### 2023-07-20  - 12:24 UTC – https://github.com/rust-lang/crates.io/issues/6850 (Crates.io crate download API is redirecting to invalid URL) was opened - 12:25 UTC – The continuing request-per-second
  - DAN-050 (llm) [Summary] 0.708: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Recovery] 0.488: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-026 (llm) [What happened…] 0.719: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.705: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto

## q-188 (esperado: DAN-050)

- busca inicial: DAN-050, DAN-106, DAN-116, DAN-035, DAN-220, DAN-148, DAN-129, DAN-191, DAN-017, DAN-003
- justificativa: 
- aprofundar DAN-050: `deployment bug download URL generation crates.io fix rollback` — Bate porque é um deploy que quebrou todos os downloads de pacotes com retries de clientes; não bate porque é crates.io/rust, não o mesmo ecossistema.
- aprofundar DAN-003: `deploy changed database field type schema validation rollback fix` — Bate porque é um deploy que quebrou um serviço distribuído logo após o deploy; não bate porque envolve banco de dados/jobs, não downloads de pacotes.
- aprofundar DAN-017: `deployment tool bug staging build HTTP 401 rollback fix` — Bate porque é um deployment tool bug que causou falha em cascata após deploy; não bate porque não envolve downloads de pacotes.
  - DAN-050 (llm) [Recovery] 0.8: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Response] 0.765: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-003 (llm) [What happened] 0.58: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.449: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s
  - DAN-017 (llm) [Analysis] 0.558: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Timeline] 0.542: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.

## q-189 (esperado: DAN-050)

- busca inicial: DAN-050, DAN-220, DAN-116, DAN-106, DAN-035, DAN-183, DAN-113, DAN-003, DAN-129, DAN-001
- justificativa: 
- aprofundar DAN-050: `deployment bug download URL generation crate download failed fix rollback` — Escolhi porque trata de falha em downloads de pacotes logo após um deploy, com clientes repetindo requisições, igual ao incidente atual.
- aprofundar DAN-035: `configuration rollout load balancer bug error rate fix rollback` — Escolhi porque envolve aumento de erros após roll-out de configuração, embora não seja específico a downloads de pacotes.
- aprofundar DAN-003: `deploy changed field type database schema validation fix rollback` — Escolhi porque começou após um deploy que alterou dados e causou falha de validação, embora não seja sobre downloads.
  - DAN-050 (llm) [Recovery] 0.795: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Response] 0.766: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.8: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.758: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.36: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration
  - DAN-003 (llm) [What happened] 0.62: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.461: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s

## q-190 (esperado: DAN-058)

- busca inicial: DAN-175, DAN-058, DAN-204, DAN-131, DAN-048, DAN-164, DAN-231, DAN-056, DAN-203, DAN-043
- justificativa: 
- aprofundar DAN-058: `free tier database data leak backup identifier fix` — É o mais parecido: vazamento de dados em bancos de clientes do plano gratuito, exatamente como o incidente atual, causado por identificadores de backup configurados incorretamente.
- aprofundar DAN-204: `Redis cache corruption cross-user data leak fix` — Usuários viam dados de outros usuários, mas em cache Redis/ChatGPT, não especificamente em bancos de clientes do plano gratuito.
- aprofundar DAN-175: `private token leak customer data access fix` — Vazamento de dados de clientes via tokens expostos, mas envolve acesso de atacantes, não clientes vendo dados alheios em seus próprios bancos.
  - DAN-058 (llm) [What happened?] 0.781: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.76: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-204 (llm) [Technical details] 0.651: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.649: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-175 (llm) [Incident Summary] 0.597: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.551: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-191 (esperado: DAN-058)

- busca inicial: DAN-058, DAN-175, DAN-164, DAN-204, DAN-231, DAN-141, DAN-006, DAN-048, DAN-056, DAN-043
- justificativa: 
- aprofundar DAN-058: `free tier database backup identifier data leak fix` — É o mais parecido: vazamento de dados em bancos de dados do free tier, embora a causa seja identificadores de backup mal configurados, não isolamento de consultas ao vivo.
- aprofundar DAN-204: `Redis cache corrupted queue cross user data leak fix` — Bate em usuários verem dados de outros usuários, mas a causa é fila de cache corrompida e não é específico do free tier.
- aprofundar DAN-175: `private token leak customer data access fix` — Envolve vazamento que expõe dados de clientes, mas se trata de token roubado em ataque, não falha de isolamento do free tier.
  - DAN-058 (llm) [What happened?] 0.776: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.759: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-204 (llm) [Technical details] 0.635: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.63: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-175 (llm) [Incident Summary] 0.597: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.551: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-192 (esperado: DAN-059)

- busca inicial: DAN-007, DAN-059, DAN-159, DAN-022, DAN-006, DAN-154, DAN-106, DAN-209, DAN-113, DAN-005
- justificativa: 
- aprofundar DAN-059: `bad BGP config severed transit providers global outage fix` — Bate com perda simultânea de vários provedores de trânsito (Level 3, Telia, Zayo) por configuração BGP ruim e outage global; não confirma se a causa foi uma mudança recente nem detalhes da correção.
- aprofundar DAN-007: `BGP communities disabled prefixes ordering datacenter malfunction fix` — Bate com mudança recente de configuração BGP (padronização de comunidades/prefixos) e impacto amplo em vários datacenters; não menciona provedores de trânsito externos.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.608: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [Troubles in the Data Center] 0.465: ### Troubles in the Data Center  So we have a situation with high levels of packet loss from many locations around the world. Let’s take a look at a Path Visualization to see where the network instabi
  - DAN-059 (causa) [sem seção] 0.384: Data centers are the factories of the Internet, churning out computation and services that customers demand. Apple is currently converting a 1.3M sq ft factory into a data center. And like factories, 
  - DAN-059 (correcao) [A (Nearly) Global Outage] 0.255: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-059 (correcao) [Steam Outage on May 7th] 0.254: ### Steam Outage on May 7th  Starting at 11:45 Pacific on May 7th and lasting for 2 hours, the popular online gaming service Steam suffered a widespread outage. Steam regularly has more than 8 million
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.718: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.668: ### Technical description of the error and how it happened  ``` [edit policy-options policy-statement 4-COGENT-TRANSIT-OUT term ADV-SITELOCAL then] +      community add STATIC-ROUTE; +      community 
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We

## q-193 (esperado: DAN-059)

- busca inicial: DAN-007, DAN-059, DAN-006, DAN-023, DAN-154, DAN-022, DAN-159, DAN-205, DAN-209, DAN-019
- justificativa: 
- aprofundar DAN-059: `bad BGP config severed transit providers global outage fix` — é o mais parecido: más configuração BGP cortou vários provedores de trânsito (Level 3, Telia, Zayo) e derrubou o serviço globalmente, mas não se sabe se há correção documentada.
- aprofundar DAN-007: `incorrect ordering disabled BGP advertised prefixes outage fix` — bate por ser uma mudança de configuração BGP que afetou múltiplos datacenters, embora não mencione perda de provedores de trânsito externos.
- aprofundar DAN-023: `configuration changes backbone routers global outage fix` — bate por outage global após mudanças de configuração em roteadores de rede, embora o foco seja o backbone interno e não provedores de trânsito.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.608: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [Troubles in the Data Center] 0.465: ### Troubles in the Data Center  So we have a situation with high levels of packet loss from many locations around the world. Let’s take a look at a Path Visualization to see where the network instabi
  - DAN-059 (causa) [sem seção] 0.384: Data centers are the factories of the Internet, churning out computation and services that customers demand. Apple is currently converting a 1.3M sq ft factory into a data center. And like factories, 
  - DAN-059 (correcao) [A (Nearly) Global Outage] 0.255: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-059 (correcao) [Steam Outage on May 7th] 0.254: ### Steam Outage on May 7th  Starting at 11:45 Pacific on May 7th and lasting for 2 hours, the popular online gaming service Steam suffered a widespread outage. Steam regularly has more than 8 million
  - DAN-007 (llm) [Incident timeline and impact] 0.696: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.684: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-023 (llm) [sem seção] 0.621: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.613: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-194 (esperado: DAN-060)

- busca inicial: DAN-068, DAN-067, DAN-060, DAN-063, DAN-062, DAN-064, DAN-191, DAN-106, DAN-071, DAN-209
- justificativa: 
- aprofundar DAN-060: `transformer failure PLC generator in phase backup generators online EC2 EBS RDS fix` — Bate: falta de energia + geradores de reserva não entraram + instâncias, volumes e bancos (EC2/EBS/RDS) em uma zona afetados. Não bate: causa foi PLC de sincronia, não falha mecânica dos geradores.
- aprofundar DAN-063: `utility power lost generator breaker mechanical failure overload manual start power control system fix` — Bate: perda de utilidade em AZ + geradores falharam (disjuntor + mecânico) + sobrecarga + acionamento manual. Não bate: houve problema extra de rede após restauração.
- aprofundar DAN-062: `power loss severe weather isolation breakers backup energy reserves grid fix` — Bate: perda de energia em instalação + instâncias de uma AZ afetadas + reservas de backup esgotadas. Não bate: disjuntores de isolamento não engataram, não geradores que não ligam.
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.735: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  Normally, when utility power fails, electrical load is seamlessly picked up by backup generators. Program
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.689: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  By Sunday morning, August 7th, we had completed the work to fully understand root cause, prevent the prob
  - DAN-060 (causa) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.442: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  In one of the days leading up to the Friday, August 5th deletion run, there was a hardware failure that t
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.417: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  We learned a number of lessons from this event that we will use to continually improve the reliability of
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.39: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  There are several places we can improve on the communication front. First, we can accelerate the pace wit
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.622: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.505: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.626: ### Summary of the AWS Service Event in the Sydney Region  If utility power is interrupted, the DRUPS uses this stored energy to continue to provide power to the datacenter while the integrated genera
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.556: ### Summary of the AWS Service Event in the Sydney Region  We’d like to share more detail about the AWS service disruption that occurred this past weekend in the AWS Sydney Region. The service disrupt
  - DAN-062 (causa) [Summary of the AWS Service Event in the Sydney Region] 0.399: ### Summary of the AWS Service Event in the Sydney Region  A latent bug in our instance management software led to a slower than expected recovery of the remaining instances. The team worked over the 
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.388: ### Summary of the AWS Service Event in the Sydney Region  Additionally, we will be taking actions to improve our recovery systems. The first is to fix the latent issue that led to our recovery system
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.359: ### Summary of the AWS Service Event in the Sydney Region  During the initial part of this event, customers experienced errors when trying to launch new instances, or when trying to scale their auto-s

## q-195 (esperado: DAN-060)

- busca inicial: DAN-060, DAN-068, DAN-067, DAN-062, DAN-061, DAN-063, DAN-064, DAN-071, DAN-078, DAN-070
- justificativa: 
- aprofundar DAN-060: `transformer failure PLC generator phase backup generators online fix EC2 EBS RDS` — Bate por perda de energia no datacenter e geradores de backup que não entram online, afetando EC2, EBS e RDS (instâncias, volumes, bancos), como o incidente atual; não se sabe se o gatilho (transformer/PLC) é o mesmo.
- aprofundar DAN-063: `utility power lost breaker generator mechanical failure overload automated control manual fix` — Bate por perda de energia de utilidade, geradores com falha (breaker abriu, falha mecânica) e sistema automatizado que mal funcionou, exigindo bring-up manual, semelhante a geradores que não entram online.
- aprofundar DAN-067: `ground fault tripped circuits generators manually restarted power restoration fix` — Bate por falha de energia no datacenter e geradores que precisaram de reinicialização manual após falha de terra; difere por ser colocation e não nuvem pública.
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.733: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  Normally, when utility power fails, electrical load is seamlessly picked up by backup generators. Program
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.692: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  At 11:54 AM PDT, we had been able to bring some of the backup generators online by manually phase-synchro
  - DAN-060 (causa) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.442: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  In one of the days leading up to the Friday, August 5th deletion run, there was a hardware failure that t
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.426: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  By Sunday morning, August 7th, we had completed the work to fully understand root cause, prevent the prob
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.417: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  We learned a number of lessons from this event that we will use to continually improve the reliability of
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.637: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.49: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-067 (llm) [Attempting to Restore Power] 0.65: ### Attempting to Restore Power  While we haven't gotten official confirmation, we have been told by employees that three things hampered getting the generators back online. First, they needed to be p
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.644: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (causa) [Lessons and Remediation] 0.574: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-196 (esperado: DAN-065)

- busca inicial: DAN-065, DAN-006, DAN-113, DAN-022, DAN-005, DAN-231, DAN-106, DAN-059, DAN-159, DAN-007
- justificativa: 
- aprofundar DAN-065: `corrupted routing data valid checksums buffers filling nodes offline root cause fix` — DAN-065 é o único que descreve exatamente o padrão atual: dados de roteamento corrompidos com checksums válidos (recomputados), sequência incorreta enchendo buffers, buffers cheios perdendo keepalives e nós saindo da rede um a um. Outros incidentes são falhas de configuração ou bugs de SO sem esse conjunto de sintomas.
  - DAN-065 (llm) [sem seção] 0.616: because  of  the  failure  of some line, each has the most recent update  from   the   other   by   the   time   communication   is re-established.      This  very  short  introduction  to  the routin
  - DAN-065 (llm) [sem seção] 0.616: our own building (after taking dumps, of course).  This procedure initializes  all  of  the IMPs' dynamic data structures, and will                               - 2 - RFC 789                         
  - DAN-065 (causa) [sem seção] 0.485: ```                                                           RFC 789     Vulnerabilities of Network Control Protocols: An Example                           Eric C. Rosen                   Bolt Berane
  - DAN-065 (correcao) [sem seção] 0.395: loader/dumper.  In the case under discussion, we would have liked to  have  all  the  IMPs  go  into  their loader/dumpers when the problem arose.  This would have enabled us to  re-initialize  and re
  - DAN-065 (correcao) [sem seção] 0.389: possible  for so  many updates from one IMP to be extant simultaneously, we did understand enough to be able to get the network to recover.   All that was necessary was to patch the IMPs to disregard 

## q-197 (esperado: DAN-065)

- busca inicial: DAN-065, DAN-113, DAN-109, DAN-005, DAN-006, DAN-238, DAN-022, DAN-026, DAN-106, DAN-218
- justificativa: 
- aprofundar DAN-065: `malfunctioning IMP corrupted routing data checksums buffers nodes offline fix recovery` — O incidente atual descreve nós caindo um após o outro, buffers enchendo, dados de roteamento estranhos e checksums válidos — exatamente a cadeia do DAN-065: IMP com mau funcionamento corrompeu dados de roteamento, checksums recomputados mascarando dados ruins, números de sequência incorretos enchendo buffers e nós saindo da rede.
  - DAN-065 (llm) [sem seção] 0.714: our own building (after taking dumps, of course).  This procedure initializes  all  of  the IMPs' dynamic data structures, and will                               - 2 - RFC 789                         
  - DAN-065 (llm) [sem seção] 0.665: possible  for so  many updates from one IMP to be extant simultaneously, we did understand enough to be able to get the network to recover.   All that was necessary was to patch the IMPs to disregard 
  - DAN-065 (causa) [sem seção] 0.485: ```                                                           RFC 789     Vulnerabilities of Network Control Protocols: An Example                           Eric C. Rosen                   Bolt Berane
  - DAN-065 (correcao) [sem seção] 0.395: loader/dumper.  In the case under discussion, we would have liked to  have  all  the  IMPs  go  into  their loader/dumpers when the problem arose.  This would have enabled us to  re-initialize  and re
  - DAN-065 (correcao) [sem seção] 0.365: a problem.  There is only one exception  to  this.   Suppose  two IMPs  A  and  B  are  out  of  communication for a period of time because there is no physical path between them.  (This may be due ei

## q-198 (esperado: DAN-069)

- busca inicial: DAN-069, DAN-191, DAN-068, DAN-063, DAN-205, DAN-064, DAN-067, DAN-209, DAN-060, DAN-102
- justificativa: 
- aprofundar DAN-069: `alarm bug transmission line foliage cascading failure fix` — Bate por falha em linha de transmissão com alarme não disparado e falha em cascata; não bate por o gatilho ser vegetação, não um problema genérico da sala de controle.
- aprofundar DAN-068: `breaker coordination settings power loss redundant paths fix` — Bate por perda de energia em cascata envolvendo breakers; não bate por ser datacenter, não linhas de transmissão nem ausência de alarme na sala de controle.
- aprofundar DAN-063: `breaker generator failure automated power control malfunction fix` — Bate por breaker abrindo, geradores falhando e sistema automatizado com mau funcionamento; não bate por ser região de nuvem, não transmissão de energia.
  - DAN-069 (llm) [Cascade] 0.59: ## Cascade  ## Timeline  The following is the blackout's sequence of events on August 14, 2003 (times in EDT):  - 12:15 p.m. Incorrect telemetry data renders the state estimator, a power flow monitori
  - DAN-069 (llm) [Computer failure] 0.56: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (causa) [Findings] 0.529: ## Findings  In April 2004, the U.S.-Canada Power System Outage Task Force released their final report, placing the causes of the blackout into four groups:  - FirstEnergy (FE) and its reliability cou
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 
  - DAN-068 (llm) [What happened to the power in the data center?] 0.656: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.563: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.644: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.51: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i

## q-199 (esperado: DAN-069)

- busca inicial: DAN-069, DAN-068, DAN-191, DAN-067, DAN-060, DAN-063, DAN-205, DAN-064, DAN-240, DAN-184
- justificativa: 
- aprofundar DAN-069: `alarm bug transmission line foliage cascading failure fix` — Linhas de transmissão, alarme que não disparou e falha em cascata, exatamente como o incidente atual.
- aprofundar DAN-068: `breaker coordination settings power loss redundant paths fix` — Envolve breakers e perda de energia em cascata, embora não mencione alarme ausente.
- aprofundar DAN-067: `ground fault high voltage power lines protective measure generator shutdown fix` — Falha em linhas de alta tensão acionou proteção que desligou equipamentos, sem alarme mencionado.
  - DAN-069 (llm) [Cascade] 0.59: ## Cascade  ## Timeline  The following is the blackout's sequence of events on August 14, 2003 (times in EDT):  - 12:15 p.m. Incorrect telemetry data renders the state estimator, a power flow monitori
  - DAN-069 (llm) [Computer failure] 0.56: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (causa) [Findings] 0.529: ## Findings  In April 2004, the U.S.-Canada Power System Outage Task Force released their final report, placing the causes of the blackout into four groups:  - FirstEnergy (FE) and its reliability cou
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 
  - DAN-068 (llm) [What happened to the power in the data center?] 0.656: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.563: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.672: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.58: ### Informed Speculation On What Happened Next  From this decision onward, we don't yet have clarity from Flexential on the root cause or some of the decisions they made or the events. We will update 
  - DAN-067 (causa) [Lessons and Remediation] 0.574: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-200 (esperado: DAN-073)

- busca inicial: DAN-073, DAN-164, DAN-129, DAN-209, DAN-048, DAN-109, DAN-026, DAN-186, DAN-066, DAN-226
- justificativa: 
- aprofundar DAN-073: `storage volume failure outage root cause fix recovery` — Bate exatamente: falha de volume em servidor de armazenamento derruba primeiro o próprio site e depois sites/programas dos usuários dependentes desse volume, se espalhando para outros hosted sites — mesmo componente e mesma propagação do incidente atual.
- aprofundar DAN-109: `storage nodes taking themselves down metadata load outage fix` — Bate parcialmente: envolve nós de armazenamento e efeito cascata que derruba serviços, mas o gatilho é uma disrupção de rede, não uma falha de volume de storage.
- aprofundar DAN-066: `Byzantine failure cascading outage API dashboard recovery fix` — Bate parcialmente: descreve uma falha em cascata que afeta disponibilidade, mas o componente é um switch de rede com comportamento bizantino, não um servidor de armazenamento.
  - DAN-073 (llm) [17:04¶] 0.687: #### 17:04¶  By this point we had become sure that the system was getting blocked on storage IO, but the problem did not seem to be the machine itself like the original indications had suggested. Howe
  - DAN-073 (llm) [18:23¶] 0.687: #### 18:23¶  At this time, livefile1 had the new volumes attached, and we were logged in and checking everything out. The server needed to do a full filesystem check before the storage was available, 
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Next steps¶] 0.303: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.587: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.578: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was
  - DAN-066 (llm) [The Dashboard] 0.65: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.64: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust

## q-201 (esperado: DAN-073)

- busca inicial: DAN-073, DAN-209, DAN-109, DAN-226, DAN-129, DAN-208, DAN-026, DAN-191, DAN-064, DAN-103
- justificativa: 
- aprofundar DAN-073: `storage volume failure root cause fix cascading outage` — O incidente atual descreve exatamente uma falha em um storage server que derruba o site e programas/websites dos usuários em sequência, igual ao DAN-073.
  - DAN-073 (llm) [Next steps¶] 0.688: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (llm) [The details¶] 0.671: ### The details¶  At 16:06 UTC on 7 July 2020, a storage volume failure on one of our storage servers caused a number of outages, starting with our own site and also with our users’ programs (includin
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi

## q-202 (esperado: DAN-076)

- busca inicial: DAN-076, DAN-154, DAN-073, DAN-127, DAN-148, DAN-106, DAN-059, DAN-198, DAN-103, DAN-126
- justificativa: 
- aprofundar DAN-076: `boot.ini deletion expansion installer root cause fix` — O instalador de expansão apagava o boot.ini e impedia o boot do computador, igual ao incidente atual; difere por ser específico do EVE Online.
  - DAN-076 (llm) [About the boot.ini issue] 0.763: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.731: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 

## q-203 (esperado: DAN-076)

- busca inicial: DAN-076, DAN-154, DAN-073, DAN-059, DAN-127, DAN-142, DAN-146, DAN-189, DAN-103, DAN-216
- justificativa: 
- aprofundar DAN-076: `boot.ini deletion expansion installer root cause fix` — O instalador de expansão do EVE Online apagou o boot.ini e impediu a inicialização, exatamente como o incidente atual (expansão de jogo → computador não boot); difere por envolver um arquivo específico do Windows antigo.
- aprofundar DAN-142: `content update Windows BSOD root cause rollback fix` — Uma atualização de conteúdo causou pane no Windows (BSOD) em milhões de máquinas, sintoma semelhante ao computador que não inicia após atualização; difere por ser atualização de segurança, não expansão de jogo.
  - DAN-076 (llm) [About the boot.ini issue] 0.763: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.731: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 
  - DAN-142 (llm) [Q: What happened?] 0.644: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [What Happened?] 0.606: ### What Happened?  On Friday, July 19, 2024 at 04:09 UTC, as part of regular operations, CrowdStrike released a content configuration update for the Windows sensor to gather telemetry on possible nov
  - DAN-142 (causa) [What Went Wrong and Why?] 0.384: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di

## q-204 (esperado: DAN-083)

- busca inicial: DAN-083, DAN-195, DAN-190, DAN-102, DAN-058, DAN-092, DAN-188, DAN-126, DAN-003, DAN-056
- justificativa: 
- aprofundar DAN-083: `nextval sequence cache 32 WAL HA promotion root cause fix` — Mesmo componente (Postgres HA), mesmo gatilho (promoção de follower para primary) e mesmo sintoma (pulo de exatamente 32 em IDs sequenciais); causa aparente idêntica: nextval pré-aloca 32 valores de sequência no WAL.
  - DAN-083 (llm) [sem seção] 0.675: ``` /*  * We don't want to log each fetching of a value from a sequence,  * so we pre-log a few fetches in advance. In the event of  * crash we can lose (skip over) as many values as we pre-logged.  *
  - DAN-083 (llm) [sem seção] 0.58: 1. We go to great lengths to ensure that if someone asks us to create an incident, we do so (!). We hadn't seen any issues and had no reports from customers, either. 2. For failed incident creation to
  - DAN-083 (causa) [See related articles] 0.353: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-083 (correcao) [sem seção] 0.325: As part of this promotion, the follower (which in many cases had a sequence value up to 32 ahead) became the new primary, at which point all sequences essentially jumped 32 values forward.  Something 
  - DAN-083 (correcao) [sem seção] 0.318: The other day, we started getting strange reports from some customers of incident.io.  Their incident identifiers — unique numbers to identify each incident — appeared to have jumped unexpectedly. One

## q-205 (esperado: DAN-083)

- busca inicial: DAN-083, DAN-195, DAN-190, DAN-102, DAN-092, DAN-188, DAN-164, DAN-003, DAN-048, DAN-080
- justificativa: 
- aprofundar DAN-083: `Postgres nextval sequence jump 32 HA promotion follower primary fix` — É o único incidente que corresponde exatamente: salto de 32 em sequências após upgrade de HA do Postgres com promoção de follower a primary; os demais tratam de wraparound, MySQL, locks, estatísticas ou outros tópicos sem relação com sequências.
  - DAN-083 (llm) [sem seção] 0.748: ``` /*  * We don't want to log each fetching of a value from a sequence,  * so we pre-log a few fetches in advance. In the event of  * crash we can lose (skip over) as many values as we pre-logged.  *
  - DAN-083 (llm) [sem seção] 0.675: As part of this promotion, the follower (which in many cases had a sequence value up to 32 ahead) became the new primary, at which point all sequences essentially jumped 32 values forward.  Something 
  - DAN-083 (causa) [sem seção] 0.401: 1. We go to great lengths to ensure that if someone asks us to create an incident, we do so (!). We hadn't seen any issues and had no reports from customers, either. 2. For failed incident creation to
  - DAN-083 (correcao) [See related articles] 0.426: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-083 (correcao) [sem seção] 0.318: The other day, we started getting strange reports from some customers of incident.io.  Their incident identifiers — unique numbers to identify each incident — appeared to have jumped unexpectedly. One

## q-206 (esperado: DAN-085)

- busca inicial: DAN-164, DAN-085, DAN-050, DAN-157, DAN-097, DAN-129, DAN-130, DAN-092, DAN-098, DAN-078
- justificativa: 
- aprofundar DAN-085: `SHA-1 collision deduplication test data checkout consistency fix` — Bate: repositório de código indisponível após commit de arquivos de teste e checkout falhando na consistência. Não bate: usa Subversion com deduplicação e colisão SHA-1, não necessariamente o mesmo VCS ou mecanismo do incidente atual.
  - DAN-085 (llm) [Problem Statement] 0.643: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.639: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-207 (esperado: DAN-085)

- busca inicial: DAN-085, DAN-164, DAN-050, DAN-157, DAN-055, DAN-173, DAN-097, DAN-129, DAN-078, DAN-130
- justificativa: 
- aprofundar DAN-085: `SHA1 collision dedup test files checkout consistency check fix remediation` — O resumo é praticamente idêntico ao incidente atual: repositório indisponível após commit de arquivos de teste com mesmo SHA-1 e checkout que falha na consistência. Não aparece nenhuma diferença relevante no resumo.
  - DAN-085 (llm) [Problem Statement] 0.706: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Wrapping Up] 0.697: ## Wrapping Up  Finally, there is still another problem scenario to be aware of and that is on the SVN client. Suppose you decide to turn off representation sharing in the repository. When this happen
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-208 (esperado: DAN-086)

- busca inicial: DAN-086, DAN-015, DAN-090, DAN-191, DAN-154, DAN-221, DAN-103, DAN-210, DAN-142, DAN-016
- justificativa: 
- aprofundar DAN-086: `leap year certificate date computation bug fix recovery` — Mesmo gatilho (29 de fevereiro) e mesma falha: certificados rejeitados por erro no cálculo de data; difere: o incidente atual cita também criação de instâncias falhando.
- aprofundar DAN-090: `certificate expiry outage fix recovery` — Envolve certificados rejeitados causando interrupção ampla; difere: não é 29 de fevereiro nem data inválida, foi expiração normal do certificado.
  - DAN-086 (llm) [The Leap Day Bug] 0.588: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.535: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.621: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.535: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (causa) [sem seção] 0.366: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q-209 (esperado: DAN-086)

- busca inicial: DAN-086, DAN-129, DAN-210, DAN-103, DAN-029, DAN-154, DAN-049, DAN-090, DAN-189, DAN-015
- justificativa: 
- aprofundar DAN-086: `leap year certificate expiration invalid date fix` — Mesma data (29 de fevereiro), mesmo sintoma (certificados rejeitados) e mesmo impacto em toda a plataforma; os outros incidentes não têm gatilho de ano bissexto nem falha de data de validade.
  - DAN-086 (llm) [The Leap Day Bug] 0.619: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.521: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-210 (esperado: DAN-088)

- busca inicial: DAN-088, DAN-103, DAN-129, DAN-066, DAN-209, DAN-089, DAN-189, DAN-116, DAN-087, DAN-064
- justificativa: 
- aprofundar DAN-088: `leap second deadlock xtime_lock printk klogd fix` — Bate: Linux, leap second, servidores travando (deadlock). Não bate: causa é printk/klogd, não futex nem hrtimer.
- aprofundar DAN-089: `leap second futex CLOCK_REALTIME hrtimer offset fix patch` — Bate: Linux, leap second, servidores/web services caindo em massa. Não bate: sintoma é alta carga por spinwait, não travamento total.
- aprofundar DAN-087: `leap second backwards time Go monotonic rand.Int63n panic fix` — Bate: leap second causando falha em massa na virada. Não bate: é Cloudflare DNS/Go, não kernel Linux genérico.
  - DAN-088 (llm) [sem seção] 0.798: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.766: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.821: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.742: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.239: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.673: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe
  - DAN-087 (llm) [The one character fix] 0.602: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (causa) [sem seção] 0.385: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (correcao) [Timeline] 0.444: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is
  - DAN-087 (correcao) [A little bit about Cloudflare DNS] 0.318: ### A little bit about Cloudflare DNS  Cloudflare customers use our DNS service to serve the authoritative answers for DNS queries for their domains. They need to tell us the IP address of their origi

## q-211 (esperado: DAN-088)

- busca inicial: DAN-088, DAN-103, DAN-129, DAN-073, DAN-026, DAN-116, DAN-205, DAN-209, DAN-064, DAN-066
- justificativa: 
- aprofundar DAN-088: `leap second xtime_lock deadlock printk klogd root cause fix` — É o único incidente que trata exatamente de servidores Linux travando no leap second, com deadlock no xtime_lock causado por printk e klogd, o que corresponde diretamente ao sintoma atual.
  - DAN-088 (llm) [sem seção] 0.802: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.763: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco

## q-212 (esperado: DAN-092)

- busca inicial: DAN-092, DAN-103, DAN-133, DAN-134, DAN-080, DAN-209, DAN-195, DAN-101, DAN-148, DAN-035
- justificativa: 
- aprofundar DAN-092: `workflows database cutover stale statistics ANALYZE disk queries jobs dropped` — Bate exatamente: cutover de banco de workflows, estatísticas desatualizadas, consultas no disco, latência e jobs descartados; não se sabe se o banco é Postgres ou outro.
- aprofundar DAN-133: `MongoDB slow queries workflow build queue JVM thread pool fix` — Bate em workflows e latência após upgrade, mas a causa é pools/threads, não estatísticas de banco stale.
- aprofundar DAN-080: `PostgreSQL migration long running query blocked queries fix` — Bate em migração Postgres e queries bloqueadas, mas não é cutover com estatísticas desatualizadas.
  - DAN-092 (llm) [What Happened] 0.687: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [What Happened] 0.667: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (causa) [Summary] 0.393: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-092 (correcao) [Future Prevention and Process Improvement] 0.483: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-133 (llm) [Incident Report] 0.696: ## Incident Report  April 10, 2019 at 13:25 UTC we were alerted to sharp increases in multiple queues responsible for job and workflow processing. Our monitoring of MongoDB showed some issues, but not
  - DAN-133 (llm) [Incident Report] 0.686: ## Incident Report  Around the same time, we updated many services to a new minor version of the JVM to pick up security changes. This update also included improvements for docker-awareness enabled by
  - DAN-133 (causa) [Incident Report] 0.453: ## Incident Report  Between March 26 and April 10, 2019, our platform experienced instability and downtime primarily due to issues with the datastore backing our builds queue. These datastore issues r
  - DAN-133 (correcao) [Incident Report] 0.533: ## Incident Report  Ultimately, refactoring the way we store and access portions of our data set in MongoDB will reduce load. Improving our data access and storage at the application level is one of o
  - DAN-133 (correcao) [Incident Report] 0.444: ## Incident Report  Perhaps most importantly, MongoDB support pointed us at the `tcmalloc.spinlock_total_delay_ns` MongoDB stat. This stat correlates with the time spent on database operations blocked
  - DAN-080 (llm) [So what happened?] 0.693: ## So what happened?  We deployed the changes, and all of our assumptions got blown out of the water. Just after the schema migration started, we started getting alerts about API requests timing out. 
  - DAN-080 (llm) [Avoiding downtime] 0.674: ## Avoiding downtime  Applications vary too much for there to be a "one size fits all" solution to this problem, but there are a few good places to start:  - Eliminate long-running queries/transaction
  - DAN-080 (causa) [Zero-downtime Postgres migrations - the hard parts] 0.354: ## Zero-downtime Postgres migrations - the hard parts  Written by  Last editedJun 2024  A few months ago, we took around 15 seconds of unexpected API downtime during a planned database migration. We'r
  - DAN-080 (correcao) [Background] 0.31: ## Background  We're no strangers to zero-downtime schema changes. Having the database stop responding to queries for more than a second or two isn't an option, so there's a bunch of stuff you learn e
  - DAN-080 (correcao) [The migration] 0.305: ## The migration  Jump back to late January. At the time, we were building invoicing for our Pro product. We'd been through a couple of iterations, and settled on model/table names. We'd already deplo

## q-213 (esperado: DAN-092)

- busca inicial: DAN-092, DAN-133, DAN-164, DAN-134, DAN-080, DAN-148, DAN-101, DAN-078, DAN-130, DAN-096
- justificativa: 
- aprofundar DAN-092: `database statistics stale index disk query planner ANALYZE fix re-promote old database` — Misma base de dados de workflows, mesmo cenário de cutover/upgrade após upgrade, mesmos sintomas (latência disparada, queries lendo tudo do disco, jobs sendo descartados). Difere na causa específica (estatísticas do planner invalidadas por upgrade de versão major durante o mesmo deployment).
  - DAN-092 (llm) [What Happened] 0.675: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.539: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers

## q-214 (esperado: DAN-093)

- busca inicial: DAN-048, DAN-078, DAN-093, DAN-094, DAN-003, DAN-190, DAN-164, DAN-096, DAN-186, DAN-058
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover wrong owner data drift fix` — Bate: schema migration provocou failover do MySQL e registros foram direcionados a donos errados, igual ao incidente atual. Não bate: envolveu Percona Replication Manager e Pacemaker, não mencionados no atual.
- aprofundar DAN-078: `MySQL master failover maintenance network partition data integrity fix` — Bate: failover do MySQL master com trabalho de restauração de integridade de dados. Não bate: gatilho foi partição de rede durante manutenção, não migração de schema, e não houve registro de outra conta.
  - DAN-093 (llm) [Monday, September 10th] 0.666: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.594: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.368: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member
  - DAN-078 (llm) [Incident timeline] 0.657: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.639: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa

## q-215 (esperado: DAN-093)

- busca inicial: DAN-048, DAN-078, DAN-093, DAN-003, DAN-164, DAN-094, DAN-096, DAN-186, DAN-080, DAN-056
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover stale node data drift wrong owner fix` — Schema migration triggered a MySQL failover to a stale node, causing data drift that routed private repositories to wrong owners — matches the current incident's schema migration → unexpected failover → users seeing other accounts' records.
  - DAN-093 (llm) [Monday, September 10th] 0.668: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.621: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-216 (esperado: DAN-106)

- busca inicial: DAN-106, DAN-073, DAN-048, DAN-164, DAN-109, DAN-071, DAN-191, DAN-064, DAN-139, DAN-060
- justificativa: 
- aprofundar DAN-106: `routine networking upgrade EBS volumes freeze region outage root cause fix` — Ambos envolvem atualização de rede de rotina causando falha regional de volumes de armazenamento em bloco e paradas de instâncias dependentes; diferem no provedor e na perda de 0,07% dos volumes.
- aprofundar DAN-109: `network disruption storage nodes down timeout retry root cause fix` — Ambos envolvem problema de rede que derruba nós de armazenamento/instâncias dependentes; diferem por se tratar de metadados DynamoDB e não volumes de bloco durante upgrade.
- aprofundar DAN-073: `storage volume failure dependent instances outage root cause fix` — Ambos envolvem falha de volume de armazenamento que derruba instâncias dependentes; diferem no gatilho (falha de servidor único vs upgrade de rede de rotina) e escopo regional.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.722: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  A large majority of the volumes in the degraded EBS cluster were still functioning properly and the focus was to 
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.72: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.583: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.524: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  The specific assignment of a group of partitions to a given server is called a “membership.” The member
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.368: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.407: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-073 (llm) [The details¶] 0.692: ### The details¶  At 16:06 UTC on 7 July 2020, a storage volume failure on one of our storage servers caused a number of outages, starting with our own site and also with our users’ programs (includin
  - DAN-073 (llm) [17:04¶] 0.69: #### 17:04¶  By this point we had become sure that the system was getting blocked on storage IO, but the problem did not seem to be the machine itself like the original indications had suggested. Howe
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Next steps¶] 0.303: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 

## q-217 (esperado: DAN-106)

- busca inicial: DAN-106, DAN-073, DAN-060, DAN-109, DAN-107, DAN-210, DAN-071, DAN-222, DAN-048, DAN-143
- justificativa: 
- aprofundar DAN-106: `network upgrade block storage volumes outage root cause fix` — Bate: rotineira atualização de rede (networking upgrade) causando problema em volumes e outage regional. Não bate: perda foi de 0,07% dos volumes, não todos presos.
- aprofundar DAN-143: `automatic upgrade network rules removed multi-region outage fix` — Bate: upgrade de rede/configuração causando outage em múltiplas regiões. Não bate: afeta clusters Kubernetes e regras de rede, não volumes de block storage explicitamente.
- aprofundar DAN-109: `network disruption storage nodes timeout retry storm root cause fix` — Bate: disrupção de rede levando storage nodes a falharem. Não bate: é DynamoDB/metadados, não uma atualização de rede rotineira que prende block storage.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.572: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.542: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  A large majority of the volumes in the degraded EBS cluster were still functioning properly and the focus was to 
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-143 (llm) [Root cause] 0.678: ## Root cause  We have identified (and since disabled) the initial trigger for the outage: on March 8, 2023, at 06:00 UTC, a security update to systemd was automatically applied to a number of VMs, wh
  - DAN-143 (llm) [Root cause] 0.621: ## Root cause  However, the base OS image we use to run Kubernetes had a legacy security update channel enabled, which caused the update to apply automatically. By design we use fairly minimal base OS
  - DAN-143 (causa) [Lessons learned] 0.422: ## Lessons learned  The following is not the sum total of everything we learned during the incident but rather important themes that pertain to the whole platform.  This was our first global incident.
  - DAN-143 (correcao) [Lessons learned] 0.446: ## Lessons learned  Even with separate systems that serve live data when historical data is not accessible (e.g., APM’s Live Search and Log Management’s Live Tail), we did not provide our customers wi
  - DAN-143 (correcao) [Recovery] 0.445: ## Recovery  The high-level steps of the recovery had to be sequenced because of the magnitude of the compute capacity drop:  - First, for each region, recover enough compute capacity so that it could
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.582: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.525: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-218 (esperado: DAN-116)

- busca inicial: DAN-126, DAN-146, DAN-103, DAN-066, DAN-209, DAN-106, DAN-048, DAN-191, DAN-116, DAN-189
- justificativa: 
- aprofundar DAN-116: `database update double free impression bus servers crash root cause fix` — O incidente envolve uma atualização de banco de dados que fez todos os servidores de um serviço caírem simultaneamente, exatamente como no atual, embora o componente específico (impression bus) seja diferente.
- aprofundar DAN-209: `migration critical backend system outage error root cause fix` — Ambos envolvem uma mudança em um sistema backend crítico (migração vs atualização de dados) que gerou uma queda generalizada, mas não menciona todos os servidores caindo no mesmo instante.
- aprofundar DAN-126: `bug fix data loss hotfix server misconfiguration update root cause fix` — Envolve efeitos colaterais de uma correção/atualização que afetaram vários servidores, porém foca em perda de dados e reconfiguração, não em queda simultânea de todos os servidores após atualização de dados.
  - DAN-116 (llm) [sem seção] 0.708: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (llm) [sem seção] 0.695: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-209 (llm) [sem seção] 0.572: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.547: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 
  - DAN-126 (llm) [Server Configurations] 0.644: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [Server Configurations] 0.637: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’

## q-219 (esperado: DAN-116)

- busca inicial: DAN-066, DAN-126, DAN-103, DAN-222, DAN-205, DAN-209, DAN-116, DAN-109, DAN-191, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update impression bus servers crash fix` — O resumo cita atualização de banco de dados que derrubou todos os servidores do impression bus simultaneamente, exatamente como o incidente atual, com atraso temporal para disparar o bug.
- aprofundar DAN-209: `migration critical backend system outage root cause fix` — O resumo menciona erro durante migração de sistema crítico de backend causando queda, similar a atualização de dados, embora não especifique queda simultânea de todos os servidores.
- aprofundar DAN-126: `bug fix hotfix server misconfiguration data loss reappear update` — O resumo envolve correção/hotfix e reaparecimento de problema em vários servidores após atualização, embora trate de perda de dados e não queda simultânea de todos.
  - DAN-116 (llm) [sem seção] 0.715: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.692: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-209 (llm) [sem seção] 0.572: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.547: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 
  - DAN-126 (llm) [Server Configurations] 0.673: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [Server Configurations] 0.665: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’

## q-220 (esperado: DAN-118)

- busca inicial: DAN-148, DAN-118, DAN-066, DAN-067, DAN-154, DAN-217, DAN-209, DAN-191, DAN-001, DAN-109
- justificativa: 
- aprofundar DAN-118: `atlassian outage root cause customer access fix restoration` — Semelhança: centenas de clientes perderam acesso a produtos; diferença: a interrupção durou dias e foi gradual, não de uma só vez.
- aprofundar DAN-154: `fastly global outage software bug configuration change fix` — Semelhança: pane global afetou todos os serviços de uma vez; diferença: gatilho foi mudança de configuração de cliente.
- aprofundar DAN-109: `dynamodb network disruption storage nodes retry cascade fix` — Semelhança: falha de rede afetou múltiplos serviços ao mesmo tempo; diferença: incidente regional do DynamoDB, não todos os produtos.
  - DAN-118 (llm) [Executive summary] 0.764: ## Executive summary  On Tuesday, April 5th, 2022, starting at 7:38 UTC, 775 Atlassian customers lost access to their Atlassian products. The outage spanned up to 14 days for a subset of these custome
  - DAN-118 (llm) [Workstream 2: Early recovery and the Restoration 1 approach] 0.715: #### Workstream 2: Early recovery and the Restoration 1 approach  - Creation of the new site, licenses, Cloud ID, and activation of the correct set of products - Migrating the site to the correct regi
  - DAN-118 (causa) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (correcao) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (correcao) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si
  - DAN-154 (llm) [**What happened?**] 0.758: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (llm) [sem seção] 0.738: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.711: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.68: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-221 (esperado: DAN-118)

- busca inicial: DAN-067, DAN-118, DAN-148, DAN-154, DAN-209, DAN-066, DAN-191, DAN-068, DAN-109, DAN-217
- justificativa: 
- aprofundar DAN-118: `Atlassian April 2022 outage root cause remediation fix` — Semelha por centenas de clientes perderem acesso aos produtos, mas difere por durar até 14 dias.
- aprofundar DAN-154: `Fastly June 8 global outage root cause fix` — Semelha por interrupção global de todos os clientes de uma vez, mas difere por ser desencadeada por mudança de configuração.
- aprofundar DAN-068: `Cloudflare data center power failure breaker coordination fix` — Semelha por perda completa de acesso, mas difere por ser falha de energia em um datacenter específico.
  - DAN-118 (llm) [Executive summary] 0.747: ## Executive summary  On Tuesday, April 5th, 2022, starting at 7:38 UTC, 775 Atlassian customers lost access to their Atlassian products. The outage spanned up to 14 days for a subset of these custome
  - DAN-118 (llm) [What happened] 0.744: ### What happened  *Figure 9: Timeline of the key incident communications milestones.*  **Timestamp: Days 1 – 3 (April 5th – 7th)**  **Early response**  The first support ticket was created on April 5
  - DAN-118 (causa) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (correcao) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (correcao) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si
  - DAN-154 (llm) [**What happened?**] 0.812: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (llm) [sem seção] 0.804: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s
  - DAN-068 (llm) [What happened to the power in the data center?] 0.767: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [sem seção] 0.728: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (causa) [What happened to the power in the data center?] 0.502: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is

## q-222 (esperado: DAN-121)

- busca inicial: DAN-129, DAN-144, DAN-147, DAN-121, DAN-016, DAN-137, DAN-134, DAN-209, DAN-148, DAN-220
- justificativa: 
- aprofundar DAN-121: `database backend overloaded throttle requests timeout fix recovery` — Corresponde exatamente: banco de dados sobrecarregado, throttling de requisições e serviços (incluindo iPlayer de vídeo) com timeout. Difere por ser um caso da BBC, não do nosso ambiente.
- aprofundar DAN-147: `database capacity overload request queue cascading failure fix` — Semelhança: banco de dados sobrecarregado por fila de requisições causando falha em cascata. Difere: foco em planejamento de capacidade, não em throttling direto de requisições.
  - DAN-121 (llm) [sem seção] 0.492: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (llm) [sem seção] 0.49: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.606: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.594: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-223 (esperado: DAN-121)

- busca inicial: DAN-147, DAN-148, DAN-101, DAN-129, DAN-134, DAN-219, DAN-164, DAN-121, DAN-144, DAN-094
- justificativa: 
- aprofundar DAN-121: `database backend overloaded throttle requests services timing out fix` — Bate porque descreve banco de backend sobrecarregado throttling requisições e serviços com timeout, quase igual ao atual; não bate por envolver BBC iPlayer/blogs, não vídeo player.
- aprofundar DAN-147: `request queue overloading insufficient database capacity cascading failure fix` — Bate porque envolve fila de requisições sobrecarregando capacidade insuficiente do banco com falha em cascata; não bate por focar em planejamento de capacidade e autenticação DUO.
- aprofundar DAN-164: `influx requests overloaded database replication lag fix` — Bate porque influxo de requisições sobrecarregou o banco de dados; não bate porque inclui exclusão acidental de diretório e perda de seis horas de dados.
  - DAN-121 (llm) [sem seção] 0.473: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.451: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.608: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.6: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Timeline] 0.688: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.654: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-224 (esperado: DAN-122)

- busca inicial: DAN-152, DAN-122, DAN-124, DAN-177, DAN-157, DAN-136, DAN-215, DAN-203, DAN-237, DAN-142
- justificativa: 
- aprofundar DAN-152: `npm account compromise malicious packages root cause fix` — Escolhi porque um atacante comprometeu a conta de um mantenedor conhecido e publicou pacotes maliciosos no repositório público npm, igual ao incidente atual, embora o ecossistema seja JavaScript.
- aprofundar DAN-122: `malicious packages impersonation JCenter root cause fix` — Escolhi porque envolve pacotes maliciosos incluídos em repositório público via ataque de personificação, semelhante ao cenário, embora o alvo sejam pacotes Maven/JCenter.
  - DAN-152 (llm) [Summary] 0.735: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.71: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.783: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.704: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-225 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-177, DAN-124, DAN-136, DAN-203, DAN-157, DAN-142, DAN-050, DAN-216
- justificativa: 
- aprofundar DAN-152: `ESLint compromised npm account malicious packages root cause fix` — Atacante comprometeu a conta do mantenedor e publicou pacotes maliciosos sob o nome de um desenvolvedor conhecido, batendo com o incidente atual; difere no registro (npm).
- aprofundar DAN-122: `JCenter malicious Maven packages impersonation attack root cause fix` — Pacotes maliciosos em repositório público de pacotes via ataque de personificação, batendo com o incidente atual; difere ao atingir JCenter/Maven.
- aprofundar DAN-177: `Homebrew leaked GitHub token git push repositories root cause fix` — Vazamento de token permitiu push em repositórios do Homebrew, relacionado a comprometimento de repositório público; difere por ser acesso git e não publicação de pacotes.
  - DAN-152 (llm) [Summary] 0.846: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.812: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.719: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.647: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-177 (llm) [sem seção] 0.781: On 31st July 2018 a security researcher identified a GitHub personal access token with recently elevated scopes was leaked from Homebrew’s Jenkins that gave them access to git push on Homebrew/brew an
  - DAN-177 (llm) [What was impacted] 0.736: ## What was impacted  GitHub Support was contacted and they verified the relevant token had not been used to perform any pushes to Homebrew/brew or Homebrew/homebrew-core during the period of elevated
  - DAN-177 (causa) [What we’re doing about it] 0.231: ## What we’re doing about it  - We have for several years enabled 2FA and third party application restrictions for the entire Homebrew GitHub organisation. This was also recommended by the security re

## q-226 (esperado: DAN-124)

- busca inicial: DAN-124, DAN-131, DAN-015, DAN-140, DAN-203, DAN-017, DAN-157, DAN-053, DAN-014, DAN-175
- justificativa: 
- aprofundar DAN-124: `secret keys Shellshock prototype machine production breach root cause fix` — Envolve chaves secretas válidas expostas que levaram a acesso não autorizado à produção, exatamente como o incidente atual.
- aprofundar DAN-131: `valid SSO session malware engineer laptop production access root cause fix` — Envolve uso de sessão válida roubada para acessar produção sem autorização, mas o vetor é malware em laptop, não chaves diretamente.
- aprofundar DAN-175: `private tokens leaked unauthorized access data root cause fix` — Envolve tokens privados vazados usados para acessar dados sem autorização, semelhante ao uso de chaves válidas, mas foca em dados e não acesso à produção.
  - DAN-124 (llm) [Where did we go wrong?] 0.621: ## Where did we go wrong?  All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover,
  - DAN-124 (llm) [What happened?] 0.603: ## What happened?  BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was t
  - DAN-124 (causa) [BrowserStack Security Incident Report — November 2014 (Resolved)] 0.331: # BrowserStack Security Incident Report — November 2014 (Resolved)  Original Incident Statement — Published November 10, 2014  As you may already know, BrowserStack experienced an attack on 9th Novemb
  - DAN-124 (correcao) [Security measures taken to mitigate and prevent further incidents] 0.556: ## Security measures taken to mitigate and prevent further incidents  - After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an add
  - DAN-124 (correcao) [Security Evolution: 2014 → 2026] 0.407: ## Security Evolution: 2014 → 2026  This incident catalyzed a complete transformation of our security infrastructure. Here is what BrowserStack looks like today.  | Area | 2014 Status | 2026 Status (C
  - DAN-131 (llm) [What happened?] 0.554: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [How do we know this attack vector is closed and it’s safe to build?] 0.491: ## How do we know this attack vector is closed and it’s safe to build?  We are confident that customers can safely build on CircleCI.  We have taken many steps since becoming aware of this attack, bot
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi
  - DAN-175 (llm) [Incident Summary] 0.571: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.563: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-227 (esperado: DAN-124)

- busca inicial: DAN-124, DAN-131, DAN-140, DAN-203, DAN-015, DAN-017, DAN-157, DAN-175, DAN-132, DAN-073
- justificativa: 
- aprofundar DAN-131: `malware stolen valid session keys production access fix remediation` — Bate: uso de chaves/sessões válidas roubadas para acessar produção. Não bate: vetor foi malware no laptop de engenheiro, não chave exposta diretamente.
- aprofundar DAN-124: `secret keys Shellshock prototype machine production breach fix` — Bate: chaves secretas em máquina comprometida levaram à violação de produção. Não bate: causa foi vulnerabilidade Shellshock em protótipo antigo.
- aprofundar DAN-132: `database breach OAuth tokens API keys revoked rotation fix` — Bate: chaves e tokens válidos acessados em violação, com rotação e revogação. Não bate: origem foi provedor externo (MongoHQ), não acesso direto com chaves próprias.
  - DAN-131 (llm) [What happened?] 0.573: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.559: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi
  - DAN-124 (llm) [Where did we go wrong?] 0.643: ## Where did we go wrong?  All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover,
  - DAN-124 (llm) [What happened?] 0.607: ## What happened?  BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was t
  - DAN-124 (causa) [BrowserStack Security Incident Report — November 2014 (Resolved)] 0.331: # BrowserStack Security Incident Report — November 2014 (Resolved)  Original Incident Statement — Published November 10, 2014  As you may already know, BrowserStack experienced an attack on 9th Novemb
  - DAN-124 (correcao) [Security measures taken to mitigate and prevent further incidents] 0.556: ## Security measures taken to mitigate and prevent further incidents  - After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an add
  - DAN-124 (correcao) [Security Evolution: 2014 → 2026] 0.407: ## Security Evolution: 2014 → 2026  This incident catalyzed a complete transformation of our security infrastructure. Here is what BrowserStack looks like today.  | Area | 2014 Status | 2026 Status (C
  - DAN-132 (llm) [Our response] 0.636: # Our response  To contain any potential risk we determined that the best course of action was to shutdown the CircleCI website and stop all builds. We also determined that it would be best to revoke 
  - DAN-132 (llm) [sem seção] 0.603: On October 29th, we received a notification email from our database provider telling us that they had been compromised. We later learned that our database was among those accessed by the attackers.  A
  - DAN-132 (causa) [Incident details] 0.331: # Incident details  On Monday, October 28th, at 3:46pm Pacific, we noticed an IAM key had been deleted. We immediately searched for any evidence that our systems had been compromised, and to discover 
  - DAN-132 (correcao) [Our response] 0.427: # Our response  At 11:26pm we sent Heroku a list of all known SSH keys. We learned at 1:25pm today that those keys have all been revoked.  At 11:44pm we completed the process of deleting all our cache
  - DAN-132 (correcao) [What you should do] 0.398: # What you should do  In order to protect your data and users, we strongly urge you to secure each of these systems:  - systems accessible by SSH keys uploaded to CircleCI - systems accessible using A

## q-228 (esperado: DAN-125)

- busca inicial: DAN-164, DAN-147, DAN-156, DAN-048, DAN-096, DAN-043, DAN-094, DAN-209, DAN-134, DAN-109
- justificativa: 
- aprofundar DAN-147: `database capacity insufficient cascading failure remediation` — Bate com falha em cascata e capacidade insuficiente do banco sob carga de pico, mas não menciona redução recente de tamanho.
- aprofundar DAN-096: `ProxySQL connection exhaustion peak load remediation` — Bate com carga de pico no cluster de banco de dados esgotando conexões, mas não menciona redução de tamanho nem servidores dependentes caindo em cascata.
- aprofundar DAN-109: `metadata service load timeout cascading failure remediation` — Bate com sobrecarga em serviço de metadados derrubando nós em cascata, mas é desencadeado por disrupção de rede, não por redução de tamanho do banco.
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.549: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.528: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.659: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.644: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.626: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.589: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-229 (esperado: DAN-125)

- busca inicial: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-129, DAN-091, DAN-125
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade cascading collapse dependent servers peak load` — Bate pelo downgrade recente da capacidade do banco, carga de pico e colapso em cascata dos servidores dependentes, exatamente como o incidente atual.
- aprofundar DAN-147: `cascading failure insufficient database capacity request queue overload` — Bate pela falha em cascata e capacidade insuficiente do banco, mas não menciona redução recente de capacidade.
- aprofundar DAN-091: `peak load database queued operations stop catching up failover` — Bate pela sobrecarga do banco em carga de pico com filas e failover, mas não cita downsizing recente.
  - DAN-125 (llm) [Database performance issues] 0.612: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.49: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.605: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.589: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-091 (llm) [Postmortem] 0.666: ## Postmortem  We identified a couple of changes that required additional work but had performed well in evaluation and rolled them back. Unfortunately, by that time the queued DB operations were back
  - DAN-091 (llm) [Postmortem] 0.641: ## Postmortem  THURSDAY 09:00 UTC: We worked to bring up excess capacity to handle the backlog and push builds in as fast as we could. Then we learned that the throttles we had built into our build sc
  - DAN-091 (causa) [Postmortem] 0.464: ## Postmortem  We've also moved over 50 percent of the data that was in our primary database onto its own deployment. The data was orthogonal and didn't need to be co-located, but its heavy use was ca
  - DAN-091 (correcao) [Resolved] 0.326: ## Resolved  We’re continuing to see builds running normally. We will be monitoring closely throughout the day. Please contact us in support if you’re seeing issues with your builds.  Posted Oct 15, 2
  - DAN-091 (correcao) [Postmortem] 0.423: ## Postmortem  Getting back to the architecture, we've known for a while that our queue model needs to be rebuilt and we've been laying the foundation to get there with the items outlined above, but w

## q-230 (esperado: DAN-126)

- busca inicial: DAN-126, DAN-076, DAN-059, DAN-106, DAN-211, DAN-127, DAN-216, DAN-145, DAN-146, DAN-116
- justificativa: 
- aprofundar DAN-126: `bug fix wrong timestamps data loss hotfix rollback Destiny 2 root cause fix` — Jogo recebendo atualização e causando perda de itens/progresso — bate com atualização/bug fix que causou data loss no Destiny 2; não bate se o incidente atual envolve múltiplos servidores ou rollback específico.
  - DAN-126 (llm) [sem seção] 0.736: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (llm) [Server Configurations] 0.711: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (causa) [Server Configurations] 0.378: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (correcao) [Server Configurations] 0.408: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’

## q-231 (esperado: DAN-126)

- busca inicial: DAN-126, DAN-059, DAN-076, DAN-127, DAN-146, DAN-058, DAN-145, DAN-116, DAN-142, DAN-043
- justificativa: 
- aprofundar DAN-126: `game update data loss timestamp bug fix hotfix regression` — Bate: atualização de jogo causando perda de dados que reaparece após outra atualização, semelhante a itens e progresso sumindo depois de update. Não bate: é sobre timestamps e servidores, não especificamente inventário de jogadores.
- aprofundar DAN-058: `database backup identifier data loss fix configuration` — Bate: perda de dados decorrente de correção/configuração incorreta após incidente. Não bate: banco de dados de tier gratuito, não jogo com itens de jogador.
- aprofundar DAN-076: `game expansion installer typo name conflict file deletion` — Bate: instalação/atualização de jogo causando exclusão acidental de dados. Não bate: arquivo do sistema boot.ini, não itens ou progresso dentro do jogo.
  - DAN-126 (llm) [Server Configurations] 0.608: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [sem seção] 0.607: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-126 (correcao) [Server Configurations] 0.372: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-058 (llm) [What happened?] 0.745: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.67: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-076 (llm) [About the boot.ini issue] 0.633: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.588: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 

## q-232 (esperado: DAN-127)

- busca inicial: DAN-127, DAN-211, DAN-219, DAN-210, DAN-208, DAN-103, DAN-145, DAN-066, DAN-094, DAN-151
- justificativa: 
- aprofundar DAN-127: `game patch cluster nodes dying start sequence logging channel fix` — Bate exatamente: novo patch de jogo, nós do cluster morrem na sequência de inicialização; não sei se a causa (canal de log) se aplica ao caso atual.
- aprofundar DAN-210: `Kubernetes cluster upgrade failed node metadata networking fix` — Semelhança parcial: atualização/patch de cluster derruba carga de trabalho na inicialização, mas envolve Kubernetes e não um jogo.
- aprofundar DAN-208: `Zookeeper boot too much data maintenance outage fix` — Semelhança parcial: falha de inicialização durante janela de manutenção, mas componente é Zookeeper e não patch de jogo.
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.675: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.674: # Behind the Scenes of a long EVE Online downtime  We had prepared a series of escalating steps that we intended to follow. Each one would progressively add more factors in to the mix, until the issue
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan
  - DAN-210 (llm) [It Begins] 0.68: ## It Begins  All at once the site came to a screeching halt. We opened an incident immediately, and brought all hands on deck, trying to figure out what had happened. Hands were on deck and in the ca
  - DAN-210 (llm) [Get to the Point, Spock, If You Have One] 0.676: ## Get to the Point, Spock, If You Have One  How did it actually break? That’s one of the most unexpected things of all. In doing the research, we discovered that the way that the route reflectors wer
  - DAN-210 (causa) [A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack] 0.526: ## A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack  Further investigation kicked off. We started looking at everything we could think of to try and narrow down the exact mome
  - DAN-210 (correcao) [It Begins] 0.466: ## It Begins  We are sufficiently paranoid, so of course our upgrade procedure includes taking a backup as standard. However, this backup procedure, and the restore, were written several years ago. Wh
  - DAN-210 (correcao) [TL;DR] 0.449: ## TL;DR  - Upgrades, particularly to our Kubernetes clusters, are risky for us, but we must do them anyway. We test and validate them in advance as best we can, but we still have plenty of work to do
  - DAN-208 (llm) [Wrapping up] 0.728: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (llm) [Read the socket] 0.713: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\

## q-233 (esperado: DAN-127)

- busca inicial: DAN-127, DAN-211, DAN-148, DAN-070, DAN-103, DAN-210, DAN-094, DAN-208, DAN-219, DAN-029
- justificativa: 
- aprofundar DAN-127: `logging channel cluster nodes dying startup game patch root cause fix` — O incidente descreve exatamente o mesmo gatilho (novo patch de jogo) e sintoma (nós do cluster morrem durante a sequência de inicialização), sendo o mais parecido com o atual.
- aprofundar DAN-210: `Kubernetes cluster upgrade node metadata workload networking failure fix` — Envolve falha de inicialização de nós de cluster após uma mudança/upgrade, mas sem relação com patch de jogo e com foco em rede de workloads.
- aprofundar DAN-070: `servers not booting Redis clusters repair power datacenter fix` — Menciona servidores que não inicializam, mas a causa é perda de energia no datacenter, não um patch de jogo.
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.692: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.679: # Behind the Scenes of a long EVE Online downtime  Via the console we modified the campaign loading functions so that they performed the load-from-DB operations normally, but all their logging operati
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan
  - DAN-210 (llm) [Get to the Point, Spock, If You Have One] 0.669: ## Get to the Point, Spock, If You Have One  How did it actually break? That’s one of the most unexpected things of all. In doing the research, we discovered that the way that the route reflectors wer
  - DAN-210 (llm) [It Begins] 0.653: ## It Begins  All at once the site came to a screeching halt. We opened an incident immediately, and brought all hands on deck, trying to figure out what had happened. Hands were on deck and in the ca
  - DAN-210 (causa) [A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack] 0.526: ## A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack  Further investigation kicked off. We started looking at everything we could think of to try and narrow down the exact mome
  - DAN-210 (correcao) [It Begins] 0.466: ## It Begins  We are sufficiently paranoid, so of course our upgrade procedure includes taking a backup as standard. However, this backup procedure, and the restore, were written several years ago. Wh
  - DAN-210 (correcao) [TL;DR] 0.449: ## TL;DR  - Upgrades, particularly to our Kubernetes clusters, are risky for us, but we must do them anyway. We test and validate them in advance as best we can, but we still have plenty of work to do
  - DAN-070 (llm) [The Event] 0.798: ## The Event  By this point, we had a fairly clear picture of what was required to restore service and began working towards that end. We needed to repair our servers that were not booting, and we nee
  - DAN-070 (llm) [The Event] 0.681: ## The Event  Initial notifications for unreachable servers and a spike in exceptions related to Redis connectivity directed our team to investigate a possible outage in our internal network. We also 
  - DAN-070 (causa) [Future Work] 0.507: ## Future Work  Complex systems are defined by the interaction of many discrete components working together to achieve an end result. Understanding the dependencies for each component in a complex sys
  - DAN-070 (correcao) [Future Work] 0.534: ## Future Work  A number of less technical improvements are also being implemented. Strengthening our cross-team communications would have shaved minutes off the recovery time. Predefining escalation 
  - DAN-070 (correcao) [In Conclusion] 0.461: ## In Conclusion  We realize how important GitHub is to the workflows that enable your projects and businesses to succeed. All of us at GitHub would like to apologize for the impact of this outage. We

## q-234 (esperado: DAN-129)

- busca inicial: DAN-129, DAN-209, DAN-119, DAN-224, DAN-011, DAN-073, DAN-035, DAN-205, DAN-162, DAN-116
- justificativa: 
- aprofundar DAN-129: `low health check timeout intermittent unresponsiveness latency fix` — Bate por ser duas horas após lançamento, intermitência, latência alta e problemas de health check; não diz explicitamente instâncias não saudáveis, mas health checks falhando implicam isso.
- aprofundar DAN-224: `health check failure regex backtracking outage fix` — Menciona health-check failures levando a outage, mas a causa é regex backtracking em um post, não lançamento de novo site.
- aprofundar DAN-035: `load balancer config rollout increased error rates fix` — Envolve load balancer e taxas de erro elevadas, mas não há lançamento nem intermitência pós-lançamento.
  - DAN-129 (llm) [Health Check Timeouts] 0.693: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [sem seção] 0.6: Approximately two hours after Supermarket became the official community site it started to experience increased latency and intermittent unresponsiveness. This made downloading cookbooks problematic a
  - DAN-129 (causa) [Conclusion] 0.457: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 
  - DAN-224 (llm) [Follow-up Actions] 0.662: # Follow-up Actions  - Audit our regular expressions and post validation workflow for any similar issues - Add controls to our load balancer to disable the healthcheck – as we believe everything but t
  - DAN-224 (llm) [Overview] 0.635: # Overview  On July 20, 2016 we experienced a 34 minute outage starting at 14:44 UTC. It took 10 minutes to identify the cause, 14 minutes to write the code to fix it, and 10 minutes to roll out the f
  - DAN-224 (causa) [Technical Details] 0.25: # Technical Details  The regular expression was: `^[\s\u200c]+|[\s\u200c]+$` Which is intended to trim unicode space from start and end of a line. A simplified version of the Regex that exposes the sa
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.793: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.753: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.36: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration

## q-235 (esperado: DAN-129)

- busca inicial: DAN-129, DAN-218, DAN-205, DAN-011, DAN-209, DAN-148, DAN-073, DAN-035, DAN-133, DAN-211
- justificativa: 
- aprofundar DAN-129: `health check timeout low latency intermittent unresponsiveness root cause fix` — O incidente bate com o atual por ocorrer duas horas após o lançamento, com latência alta, resposta intermitente e instâncias marcadas como não saudáveis por health checks; diferentemente dos demais, que envolvem rede, armazenamento ou carga extrema sem relação com o lançamento.
  - DAN-129 (llm) [Health Check Timeouts] 0.757: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [sem seção] 0.601: Approximately two hours after Supermarket became the official community site it started to experience increased latency and intermittent unresponsiveness. This made downloading cookbooks problematic a
  - DAN-129 (causa) [Conclusion] 0.457: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 

## q-236 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-217, DAN-078, DAN-221, DAN-164, DAN-210
- justificativa: 
- aprofundar DAN-145: `Redis primary failover cluster rebalance cascading connection failure` — Corresponde quase exatamente: primário Redis caiu, cluster rebalanceou e houve falha em cascata, embora o gatilho seja migração de nuvem.
- aprofundar DAN-217: `mass disconnection reconnection cascading connection failure database capacity` — Semelhança nas falhas em cascata de conexão após desconexões em massa, mas sem cluster Redis ou rebalanceamento.
- aprofundar DAN-234: `Redis cluster network partition master crash recovery fix` — Envolve cluster Redis e queda do master, mas no contexto de faturamento e modo somente-leitura, não conexões de usuários.
  - DAN-145 (llm) [Sequence of Events] 0.699: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.657: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-217 (llm) [TUESDAY] 0.722: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [MONDAY] 0.517: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (causa) [WEDNESDAY] 0.41: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou
  - DAN-234 (llm) [What We’re Doing About It] 0.622: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.585: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn

## q-237 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-048, DAN-029, DAN-070, DAN-096, DAN-210, DAN-078, DAN-221
- justificativa: 
- aprofundar DAN-145: `Redis primary failover cluster rebalance cascade root cause fix` — O incidente descreve Redis primary caindo, rebalance automático do cluster e falha em cascata nas conexões de usuários, exatamente como o incidente atual.
  - DAN-145 (llm) [Sequence of Events] 0.716: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.664: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci

## q-238 (esperado: DAN-148)

- busca inicial: DAN-148, DAN-106, DAN-217, DAN-191, DAN-067, DAN-066, DAN-221, DAN-209, DAN-109, DAN-144
- justificativa: 
- aprofundar DAN-148: `root cause concurrent users overload service disruption fix mitigation` — O único com mesmo gatilho: pico recorde de usuários simultâneos causando misto de interrupções parciais e totais. Os outros têm gatilhos diferentes (erro humano, migração, falha de rede, energia).
  - DAN-148 (llm) [**XMPP outage**] 0.628: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (llm) [**Account Service outage**] 0.622: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme

## q-239 (esperado: DAN-148)

- busca inicial: DAN-148, DAN-209, DAN-001, DAN-067, DAN-066, DAN-217, DAN-106, DAN-109, DAN-191, DAN-208
- justificativa: 
- aprofundar DAN-148: `concurrent user peak service disruption root cause fix mitigation` — Corresponde exatamente: pico recorde de usuários concorrentes com disrupções parciais e totais, igual ao incidente atual.
- aprofundar DAN-001: `traffic spike cluster resource management configuration error fix` — Semelhança: pico repentino de tráfego derrubando serviços, embora a causa seja erro de configuração em gerenciamento de cluster, não apenas carga.
- aprofundar DAN-217: `database capacity cascading connection failures root cause fix` — Semelhança: falhas em cascata por capacidade excedida, mas o gatilho é reconexão em massa de usuários, não pico de CCU.
  - DAN-148 (llm) [**Account Service outage**] 0.642: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [Postmortem of Service Outage at 3.4M CCU] 0.64: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (causa) [**XMPP outage**] 0.495: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-001 (llm) [Analysis #] 0.683: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (llm) [Outage timeline #] 0.678: ## Outage timeline #  Also just before noon, traffic peaked at 200%-300% of the traffic from previous day, depending on service. At this stage, traffic was at its highest but due to excessive resource
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa
  - DAN-217 (llm) [TUESDAY] 0.644: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [MONDAY] 0.489: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (causa) [WEDNESDAY] 0.41: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou

## q-240 (esperado: DAN-152)

- busca inicial: DAN-009, DAN-175, DAN-140, DAN-152, DAN-177, DAN-015, DAN-017, DAN-124, DAN-131, DAN-028
- justificativa: 
- aprofundar DAN-152: `malicious package npm maintainer account compromise root cause fix` — Bate porque envolve pacote malicioso publicado em registro público por conta de mantenedor comprometida, igual ao pacote não publicado enviando tokens; não bate porque o resumo não menciona exfiltração de tokens de acesso.
  - DAN-152 (llm) [Timeline] 0.725: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Summary] 0.723: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-241 (esperado: DAN-152)

- busca inicial: DAN-152, DAN-009, DAN-015, DAN-177, DAN-140, DAN-017, DAN-122, DAN-131, DAN-175, DAN-204
- justificativa: 
- aprofundar DAN-152: `npm account compromise malicious package publication root cause fix` — O incidente envolve atacante que comprometeu conta npm e publicou pacotes maliciosos, exatamente como o atual (versão não publicada enviando tokens). Difere por ser ESLint/JavaScript, não nosso pacote.
- aprofundar DAN-122: `malicious package impersonation JCenter root cause fix` — Envolve pacotes maliciosos publicados por ataque de personificação em repositório de pacotes, similar ao pacote não publicado enviando tokens. Difere por ser Maven/JCenter/Android, não npm.
  - DAN-152 (llm) [Summary] 0.749: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.746: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.785: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.691: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-242 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-109, DAN-026, DAN-129, DAN-145, DAN-106, DAN-009, DAN-008, DAN-067, DAN-016
- justificativa: 
- aprofundar DAN-011: `database permission file exceeded limits systemwide outage fix` — É uma CDN (Cloudflare) com pane mundial repentina e propagação pela rede, mas o gatilho é banco de dados/bot-detection, não um erro genérico de servidores.
- aprofundar DAN-016: `DDoS mitigation rule rate limiting bug infinite loop CPU fix` — É uma CDN (Cloudflare) com pane mundial e propagação entre datacenters, mas o gatilho é regra de DDoS/rate-limiting, não necessariamente erro na maioria dos servidores.
- aprofundar DAN-009: `service tokens code release CDN outage recovery fix` — É uma CDN (Cloudflare) com pane mundial repentina por erro em release de código, afetando o CDN, embora o resumo mencione controle de tokens mais que servidores devolvendo erro.
  - DAN-011 (llm) [Memory preallocation] 0.567: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (llm) [sem seção] 0.549: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.693: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.657: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-009 (llm) [How did we fix the issue?] 0.688: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-009 (llm) [sem seção] 0.678: Several Cloudflare services became unavailable for 121 minutes on January 24, 2023 due to an error releasing code that manages service tokens. The incident degraded a wide range of Cloudflare products
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [Incident Timeline] 0.424: ### Incident Timeline  At 2023-01-24 18:56 The same solution was implemented on the Cloudflare API account, impacting Cache Purge, Cache Reserve, Images and R2. **Impact ended for Cache Purge, Cache R

## q-243 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210, DAN-209, DAN-205, DAN-129, DAN-109, DAN-145
- justificativa: 
- aprofundar DAN-011: `Cloudflare bot detection permissions database file limit systemwide outage fix` — É um outage mundial de CDN (Cloudflare) causado por mudança de permissão que gerou arquivo acima do limite e se espalhou pela rede, similar ao CDN global caindo no incidente atual.
- aprofundar DAN-008: `Cloudflare Tiered Cache change 530 error partial outage fix` — É uma interrupção parcial da Cloudflare causada por mudança no sistema de Tiered Cache que gerou erros 530, envolvendo um CDN como no atual, mas com impacto parcial e não mundial.
  - DAN-011 (llm) [sem seção] 0.695: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (llm) [Remediation and follow-up steps] 0.688: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-008 (llm) [sem seção] 0.865: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Incident timeline and impact] 0.796: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Conclusion] 0.516: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i

## q-244 (esperado: DAN-165)

- busca inicial: DAN-165, DAN-195, DAN-231, DAN-124, DAN-184, DAN-221, DAN-033, DAN-183, DAN-164, DAN-001
- justificativa: 
- aprofundar DAN-165: `repeated email batch cron job non atomic cause fix` — Escolhi DAN-165 porque descreve exatamente o mesmo sintoma — e-mail enviado mais de 20 vezes — causado por um job de lote não atômico que não marca os destinatários como enviados até terminar, igual ao incidente atual.
- aprofundar DAN-195: `transaction ID wraparound Postgres queued mail resolution` — Escolhi DAN-195 porque envolve e-mail enfileirado, mas a causa é wraparound de ID e uma interrupção, não duplicação de mensagem, então é menos parecido que o DAN-165.
  - DAN-165 (llm) [So what was the bug?] 0.677: ## So what was the bug?  In the App Engine datastore, we have an object called a "notification". That notification has a "status" property, which takes on the following values: "Waiting", "Sending", a
  - DAN-165 (llm) [sem seção] 0.574: A few hours ago, the automated email system for Code Jam went a little bit crazy. I'll write about the technical details below, but the short version is that it sent an email titled "Registration Now 
  - DAN-165 (causa) [Why did I get the repeated email at all?] 0.284: ## Why did I get the repeated email at all?  We sent the notification email to users who registered for Code Jam 2013, checked the box saying "I would like to receive email notifying me about the next
  - DAN-165 (correcao) [Why does Code Jam have its own email system?] 0.272: ## Why does Code Jam have its own email system?  To automatically identify the users who should get an email based on Code Jam-specific properties (such as scores, booleans in user profiles, and regis
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.778: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.652: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg

## q-245 (esperado: DAN-165)

- busca inicial: DAN-165, DAN-183, DAN-231, DAN-124, DAN-195, DAN-033, DAN-221, DAN-164, DAN-184, DAN-016
- justificativa: 
- aprofundar DAN-165: `batch cron job repeated emails non-atomic mark waiting fix` — Escolhi DAN-165 porque envolve emails enviados mais de 20 vezes por um job em lote não atômico que não marca os usuários como atendidos até terminar tudo, exatamente o sintoma de emails duplicados do incidente atual, embora o contexto seja o Google Code Jam.
  - DAN-165 (llm) [So what was the bug?] 0.742: ## So what was the bug?  In the App Engine datastore, we have an object called a "notification". That notification has a "status" property, which takes on the following values: "Waiting", "Sending", a
  - DAN-165 (llm) [sem seção] 0.591: A few hours ago, the automated email system for Code Jam went a little bit crazy. I'll write about the technical details below, but the short version is that it sent an email titled "Registration Now 
  - DAN-165 (causa) [Why did I get the repeated email at all?] 0.284: ## Why did I get the repeated email at all?  We sent the notification email to users who registered for Code Jam 2013, checked the box saying "I would like to receive email notifying me about the next
  - DAN-165 (correcao) [Why does Code Jam have its own email system?] 0.272: ## Why does Code Jam have its own email system?  To automatically identify the users who should get an email based on Code Jam-specific properties (such as scores, booleans in user profiles, and regis

## q-246 (esperado: DAN-170)

- busca inicial: DAN-170, DAN-198, DAN-126, DAN-200, DAN-065, DAN-103, DAN-191, DAN-035, DAN-154, DAN-116
- justificativa: 
- aprofundar DAN-170: `GPS incorrect positions update rollback did not fix root cause` — É o único incidente sobre posições incorretas de satélites após atualização, com reversão que não resolveu, igual ao incidente atual.
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.63: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Bad Broadcast Messages (resulting in position errors up to about ±200km) were sent out     starting April 1, 2014, 21:00; Fi
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.626: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  From CODE Analysis protocol: Number of GLONASS observations    reduced by about 10% on April 2nd.  this is why the IGS post
  - DAN-170 (causa) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.358: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Understood:    The GNONASS April 1st event was not a joke.    The failure was caused by wrong Broadcast Ephemerides   … p
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.318: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol of April 1). Some receivers unaffected, some stopped tracking GLONASS after 9h p.m. (red line), some even stopped GPS trackin
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.307: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Real-time GNSS Service   -timeIGSOpen Data       •   Observations & derived products freely available       •   Streaming da

## q-247 (esperado: DAN-170)

- busca inicial: DAN-170, DAN-126, DAN-050, DAN-198, DAN-035, DAN-103, DAN-065, DAN-200, DAN-154, DAN-074
- justificativa: 
- aprofundar DAN-170: `GPS incorrect position bad update rollback root cause fix` — O incidente atual envolve receptores recebendo posições incorretas de satélites após uma atualização e o rollback não corrigiu; DAN-170 é o único que menciona GPS/GLONASS, atualização ruim, posições incorretas e rollback ineficaz.
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.625: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Bad Broadcast Messages (resulting in position errors up to about ±200km) were sent out     starting April 1, 2014, 21:00; Fi
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.621: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Understood:    The GNONASS April 1st event was not a joke.    The failure was caused by wrong Broadcast Ephemerides   … p
  - DAN-170 (causa) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.337: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol of April 1). Some receivers unaffected, some stopped tracking GLONASS after 9h p.m. (red line), some even stopped GPS trackin
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.349: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  From CODE Analysis protocol: Number of GLONASS observations    reduced by about 10% on April 2nd.  this is why the IGS post
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.307: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Real-time GNSS Service   -timeIGSOpen Data       •   Observations & derived products freely available       •   Streaming da

## q-248 (esperado: DAN-180)

- busca inicial: DAN-180, DAN-164, DAN-191, DAN-129, DAN-209, DAN-222, DAN-048, DAN-181, DAN-107, DAN-102
- justificativa: 
- aprofundar DAN-180: `ingest system repeated outages root cause fix cache delay` — Bate com o atual: ingest system caindo repetidamente por mais de oito horas. Não garante que a causa (cache delays) seja a mesma.
- aprofundar DAN-222: `Cassandra cluster crash ingestion message bus producers blocking fix` — Bate com o atual: dados sendo ingeridos em cluster com falha em cadeia até derrubar a aplicação. Não garante que o componente (Cassandra) seja o mesmo.
- aprofundar DAN-107: `data collection server memory leak reporting agent outage fix` — Bate com o atual: servidor de coleta de dados e instabilidade prolongada. Não garante que a causa (memory leak no agent) seja a mesma.
  - DAN-180 (llm) [The events] 0.665: ## The events  We then forced a scale-down of Shepherds to disrupt the pattern, but the autoscaler decided we had too few Shepherds—crashlooping demands a lot of CPU—and instead added more of them. We
  - DAN-180 (llm) [The events] 0.636: ## The events  We decided to do more aggressive sampling in an attempt to stabilize the Refinery cluster by keeping less data. This seemed to work, but sampling aggressively was impacting our ability 
  - DAN-180 (causa) [On causal confusion] 0.541: ### On causal confusion  At one point, our understanding of the situation looked like the following diagram, where orange denotes places where we observed unusual behavior:  Ingestion volume was highe
  - DAN-180 (correcao) [Analysis] 0.509: ## Analysis  This incident revealed areas where we had built mental models of components that proved inaccurate during incidents, and could even clash with each other. This was an opportunity to contr
  - DAN-180 (correcao) [On the solution found] 0.457: ### On the solution found  We still don’t know what triggered all of this, we just know that it was fixed by the cache pre-fill. We are confident the fix worked and is effective because it’s been thro
  - DAN-222 (llm) [sem seção] 0.641: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (llm) [sem seção] 0.638: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (causa) [sem seção] 0.457: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl
  - DAN-107 (llm) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.662: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Last week, one of the data collection servers in the affected Availability Zone had a hardware failure and was replaced. As
  - DAN-107 (llm) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.56: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  We have deployed monitoring that will alarm if we see this specific memory leak again in any of our production EBS servers,
  - DAN-107 (causa) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.433: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  The memory pressure on many of the EBS servers had reached a point where EBS servers began losing the ability to process cu
  - DAN-107 (correcao) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.407: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Normally these events are simultaneous. Between the period of time the masters were disconnected from their standbys and th
  - DAN-107 (correcao) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.399: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Unfortunately, a bug in the traffic shifting functionality incorrectly mapped a small number of the affected load balancers

## q-249 (esperado: DAN-180)

- busca inicial: DAN-180, DAN-209, DAN-181, DAN-222, DAN-164, DAN-048, DAN-208, DAN-191, DAN-067, DAN-217
- justificativa: 
- aprofundar DAN-180: `ingest system repeatedly down cache delays root cause fix` — O sistema de ingest caiu repetidamente por mais de oito horas, exatamente como o incidente atual; diferem o componente (cache do Shepherd) e a causa específica.
- aprofundar DAN-222: `Cassandra cluster crash ingest data producers blocking queue fix` — Envolve ingestão de dados em cluster que falha e bloqueia produtores, gerando instabilidade em cadeia; não cita ingest repetidamente por horas de forma idêntica.
- aprofundar DAN-181: `Honeycomb total outage root cause remediation data processing` — Mesma empresa (Honeycomb) e interrupção total do processamento de dados; não cita especificamente o sistema de ingest instável por horas.
  - DAN-180 (llm) [The events] 0.655: ## The events  We then forced a scale-down of Shepherds to disrupt the pattern, but the autoscaler decided we had too few Shepherds—crashlooping demands a lot of CPU—and instead added more of them. We
  - DAN-180 (llm) [The events] 0.644: ## The events  We decided to do more aggressive sampling in an attempt to stabilize the Refinery cluster by keeping less data. This seemed to work, but sampling aggressively was impacting our ability 
  - DAN-180 (causa) [On causal confusion] 0.541: ### On causal confusion  At one point, our understanding of the situation looked like the following diagram, where orange denotes places where we observed unusual behavior:  Ingestion volume was highe
  - DAN-180 (correcao) [Analysis] 0.509: ## Analysis  This incident revealed areas where we had built mental models of components that proved inaccurate during incidents, and could even clash with each other. This was an opportunity to contr
  - DAN-180 (correcao) [On the solution found] 0.457: ### On the solution found  We still don’t know what triggered all of this, we just know that it was fixed by the cache pre-fill. We are confident the fix worked and is effective because it’s been thro
  - DAN-222 (llm) [sem seção] 0.685: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (llm) [sem seção] 0.669: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (causa) [sem seção] 0.457: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl
  - DAN-181 (llm) [sem seção] 0.696: On July 25th, 2023, we experienced a total Honeycomb outage. It impacted all user-facing components from 1:40 p.m. UTC to 2:48 p.m. UTC, during which no data could be processed or accessed.  This outa
  - DAN-181 (llm) [**Corrective actions**] 0.655: ### **Corrective actions**  For the duration of the outage, no new data could be ingested. If our users or customers did not buffer this data to disk somewhere to replay it later, it is gone for good.
  - DAN-181 (causa) [**How a database dies**] 0.525: ### **How a database dies**  The core of the database failure was a deadlock in MySQL’s internals. There’s no clear path on how we specifically got there, but since this is a concurrency issue, we thi
  - DAN-181 (correcao) [**Contributing factors**] 0.535: ### **Contributing factors**  Preventing a bug by switching to the old infrastructure set up the stage. We suspended deployments during the investigation, which prevented restarts accidentally making 
  - DAN-181 (correcao) [**Conclusion**] 0.499: ## **Conclusion**  While we wish such incidents wouldn’t happen, we know that we’ll have to manage them—no matter how hard we plan for them. One of the most intriguing themes that came up from many of

## q-250 (esperado: DAN-183)

- busca inicial: DAN-183, DAN-195, DAN-134, DAN-096, DAN-148, DAN-101, DAN-133, DAN-080, DAN-094, DAN-129
- justificativa: 
- aprofundar DAN-183: `GKE Dataplane V2 anetd CPU saturation packet drops memcached Postgres connection timeout root cause fix` — Mesmo cenário: migração para nova nuvem, picos de timeout de conexão no Postgres (~200 conexões/s), erros de i/o timeout no memcached, ajuste de pool ajudou só parcialmente. Difere no provedor (Google Cloud) e na causa específica (saturação de CPU do anetd por bursts de chamadas paralelas/N+1).
  - DAN-183 (llm) [OK, so what’s actually going on?] 0.698: ## OK, so what’s actually going on?  This revelation suggests that this isn't a process-local issue. What we mean by this is the fact that we were having network issues between our Kubernetes node and
  - DAN-183 (llm) [Meanwhile, a few desks away] 0.666: ## Meanwhile, a few desks away  While all this had been going on, another unrelated issue had cropped up. Thanks to an accidental database join, we’d been making thousands of duplicate network calls t
  - DAN-183 (causa) [Meanwhile, a few desks away] 0.461: ## Meanwhile, a few desks away  This was only happening for a tiny handful of requests among hundreds of thousands, with seemingly no other consistent pattern when it came to which users, organization
  - DAN-183 (correcao) [Clouds, caches and connection conundrums] 0.391: ## Clouds, caches and connection conundrums  Ben Wheatley  September 26, 2023  13 min read  We recently moved our infrastructure fully into Google Cloud. Most things went very smoothly, but there was 
  - DAN-183 (correcao) [OK, so what’s actually going on?] 0.364: ## OK, so what’s actually going on?  If you think about it, it all starts to line up pretty much perfectly with what we’d seen and done up until this point:  - We mostly fixed the DB timeouts by fixin

## q-251 (esperado: DAN-183)

- busca inicial: DAN-183, DAN-101, DAN-148, DAN-096, DAN-195, DAN-134, DAN-133, DAN-129, DAN-080, DAN-156
- justificativa: 
- aprofundar DAN-183: `GKE Dataplane V2 anetd CPU saturation packet drop memcached Postgres fix` — corresponde quase exatamente: mudança para nuvem, timeouts do Postgres, erros de i/o do memcached e ajuste de pool apenas parcial; difere no agente de rede específico.
- aprofundar DAN-101: `Go database/sql pool exhaustion unnecessary transaction fix` — compartilha timeouts de pool de conexão e correções parciais, mas não tem erros do memcached nem gatilho de migração para nuvem.
  - DAN-183 (llm) [OK, so what’s actually going on?] 0.683: ## OK, so what’s actually going on?  This revelation suggests that this isn't a process-local issue. What we mean by this is the fact that we were having network issues between our Kubernetes node and
  - DAN-183 (llm) [Meanwhile, a few desks away] 0.593: ## Meanwhile, a few desks away  While all this had been going on, another unrelated issue had cropped up. Thanks to an accidental database join, we’d been making thousands of duplicate network calls t
  - DAN-183 (causa) [Meanwhile, a few desks away] 0.461: ## Meanwhile, a few desks away  This was only happening for a tiny handful of requests among hundreds of thousands, with seemingly no other consistent pattern when it came to which users, organization
  - DAN-183 (correcao) [Clouds, caches and connection conundrums] 0.391: ## Clouds, caches and connection conundrums  Ben Wheatley  September 26, 2023  13 min read  We recently moved our infrastructure fully into Google Cloud. Most things went very smoothly, but there was 
  - DAN-183 (correcao) [OK, so what’s actually going on?] 0.364: ## OK, so what’s actually going on?  If you think about it, it all starts to line up pretty much perfectly with what we’d seen and done up until this point:  - We mostly fixed the DB timeouts by fixin
  - DAN-101 (llm) [sem seção] 0.66: When our app communicates with our database, it uses a client-side connection pool that is implemented in the`database/sql` Go package. The package uses these pools to limit the number of processes in
  - DAN-101 (llm) [sem seção] 0.632: ``` func trackUsage(ctx context.Context) (end func()) { 	inTransaction, _ := ctx.Value(InTransactionContextKey).(bool) 	startTime := time.Now() 	return func() { 		duration := time.Since(startTime) 		l
  - DAN-101 (causa) [sem seção] 0.433: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (correcao) [sem seção] 0.424: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (correcao) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you

## q-252 (esperado: DAN-186)

- busca inicial: DAN-186, DAN-164, DAN-120, DAN-043, DAN-048, DAN-011, DAN-156, DAN-094, DAN-195, DAN-226
- justificativa: 
- aprofundar DAN-186: `hosted database limit reached migration new database recovery` — Bate: banco de dados hospedado atingiu limite, igual ao atual; não bate: não detalha qual limite ou se writes pararam.
- aprofundar DAN-120: `integer limit database read-only outage fix` — Bate: banco atingiu limite e serviu em read-only; não bate: limite de inteiro (ID), não de capacidade de hosted DB.
- aprofundar DAN-195: `Postgres transaction ID wraparound outage recovery fix` — Bate: limite de transação causou outage parcial do banco; não bate: específico do Postgres XID, não banco hospedado genérico.
  - DAN-186 (llm) [**Full service restoration**] 0.684: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma
  - DAN-186 (llm) [**Data restoration**] 0.673: # **Data restoration**  Once the service was back up and the data dumps completed, the next step was to import all of the dumps into an instance that wasn’t subject to the 2TB file size limit. We work
  - DAN-186 (causa) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (correcao) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (correcao) [**Prevention**] 0.407: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-120 (llm) [sem seção] 0.705: Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, 
  - DAN-120 (llm) [sem seção] 0.582: We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998
  - DAN-120 (causa) [sem seção] 0.427: Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop using our status.basecamp.com updates and a play-by-play record on our blog. We can’t promise to be perfec
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.808: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.616: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg

## q-253 (esperado: DAN-186)

- busca inicial: DAN-186, DAN-164, DAN-120, DAN-094, DAN-043, DAN-048, DAN-156, DAN-147, DAN-011, DAN-096
- justificativa: 
- aprofundar DAN-186: `hosted database limit reached migration fix recovery` — Bate com o incidente atual por envolver limite atingido em banco de dados hospedado; não menciona explicitamente modo somente leitura.
- aprofundar DAN-120: `integer limit read-only database outage fix recovery` — Bate por envolver limite do banco de dados e modo somente leitura (não consegue gravar); não especifica se é banco hospedado.
- aprofundar DAN-094: `LimitNOFILE cap database outage fix recovery` — Envolve um limite do sistema afetando o banco de dados, mas é sobre descritores de arquivo, não exatamente limite de armazenamento ou capacidade do banco hospedado.
  - DAN-186 (llm) [**Prevention**] 0.683: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-186 (llm) [**Full service restoration**] 0.669: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma
  - DAN-186 (causa) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (correcao) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (correcao) [**Reflections**] 0.427: # **Reflections**  This is any web application developer’s worst nightmare. A filesystem-based limitation we weren’t aware of and had no visibility into rendered not only our production database usele
  - DAN-120 (llm) [sem seção] 0.693: Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, 
  - DAN-120 (llm) [sem seção] 0.593: We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998
  - DAN-120 (causa) [sem seção] 0.427: Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop using our status.basecamp.com updates and a play-by-play record on our blog. We can’t promise to be perfec
  - DAN-094 (llm) [2020, February 25 16:36 UTC (lasting for two hours 12 minutes)] 0.611: ## 2020, February 25 16:36 UTC (lasting for two hours 12 minutes)  In this third incident involving ProxySQL, active database connections crossed a critical threshold that changed the behavior of this
  - DAN-094 (llm) [2020, February 20 21:31 UTC (lasting for 47 minutes)] 0.58: ## 2020, February 20 21:31 UTC (lasting for 47 minutes)  Two days later, as part of a planned master database promotion, we saw unexpectedly high load which triggered a similar ProxySQL failure. The i
  - DAN-094 (causa) [Background] 0.437: ## Background  Originally, all our MySQL data lived in a single database cluster. Over time, as mysql1 grew larger and busier, we split functionally grouped sets of tables into new clusters and create
  - DAN-094 (correcao) [Next steps] 0.365: ## Next steps  ## Immediate changes: Data partitioning  We shipped a sizable chunk of data partitioning efforts we’ve worked on for the past six months just days after these incidents for one of our m
  - DAN-094 (correcao) [In summary] 0.481: ## In summary  We know you depend on our platform to be reliable. With the immediate changes we’ve made and long-term plans in progress, we’ll continue to use what we’ve learned to make GitHub better 

## q-254 (esperado: DAN-188)

- busca inicial: DAN-188, DAN-080, DAN-195, DAN-102, DAN-164, DAN-112, DAN-109, DAN-147, DAN-048, DAN-101
- justificativa: 
- aprofundar DAN-188: `PostgreSQL lock transaction wraparound global lock metadata server fix` — Bate: travas no banco de metadados Postgres bloqueando operações de armazenamento, causadas por manutenção de wraparound e query com lock global. Não bate: o atual não menciona wraparound nem query específica.
- aprofundar DAN-195: `transaction ID wraparound outage root cause fix vacuum` — Bate: wraparound de transaction ID no Postgres causou interrupção parcial de um dia e meio, compatível com esperas de lock por horas. Não bate: resumo não detalha se houve bloqueio de lock explícito.
- aprofundar DAN-102: `PGAudit extension held locks blocked database operations restart fix` — Bate: extensão Postgres travada segurando lock crítica bloqueou outras operações do banco. Não bate: causa é extensão PGAudit após upgrade, não wraparound ou storage service.
  - DAN-188 (llm) [Subsequent analysis] 0.629: ### Subsequent analysis  #### More background  To fully understand what happened, a little more background on PostgreSQL is required.  PostgreSQL's implementation of Multi-Version Concurrency Control 
  - DAN-188 (llm) [Summary of Root Cause] 0.626: ### Summary of Root Cause  In summary:  - All Manta operations touch our sharded, PostgreSQL-backed metadata tier. - During the event, one of the shard databases had all queries on our primary table b
  - DAN-188 (causa) [Root cause analysis] 0.545: ## Root cause analysis  For transparency, we've included a lot of detail here about how the incident proceeded. If you're interested in more of a summary, skip to the Summary of Root Cause section bel
  - DAN-188 (correcao) [Closing] 0.517: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working hard to prevent an issue like this from happ
  - DAN-188 (correcao) [The problem] 0.482: ### The problem  We observed the autovacuum scan the full table and all of its indexes, and then do the same thing again. After several hours, it successfully completed and updated the "last\_autovacu
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.712: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.617: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg
  - DAN-102 (llm) [sem seção] 0.676: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [sem seção] 0.668: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily

## q-255 (esperado: DAN-188)

- busca inicial: DAN-188, DAN-080, DAN-195, DAN-109, DAN-112, DAN-164, DAN-102, DAN-181, DAN-101, DAN-226
- justificativa: 
- aprofundar DAN-188: `PostgreSQL metadata lock wraparound global lock root cause fix` — Serviço de storage (Manta) com operações bloqueadas por lock no Postgres metadata; causa envolve wraparound e lock global desnecessário, bem próximo do incidente atual.
- aprofundar DAN-195: `transaction ID wraparound root cause fix Postgres` — Wraparound de transaction ID no Postgres aparece como parte da causa do DAN-188, mas este incidente não foca em storage nem em lock de metadados específico.
- aprofundar DAN-102: `PGAudit critical locks Postgres restart fix` — Postgres com extensão segurando locks críticos e bloqueando operações, mas trigger é upgrade/PGAudit, não metadata de storage com lock por horas.
  - DAN-188 (llm) [Summary of Root Cause] 0.686: ### Summary of Root Cause  In summary:  - All Manta operations touch our sharded, PostgreSQL-backed metadata tier. - During the event, one of the shard databases had all queries on our primary table b
  - DAN-188 (llm) [The problem] 0.65: ### The problem  We quickly identified that API requests were hanging and ultimately failing because all queries to one of the PostgreSQL databases were themselves hanging. API servers timed out these
  - DAN-188 (causa) [Root cause analysis] 0.545: ## Root cause analysis  For transparency, we've included a lot of detail here about how the incident proceeded. If you're interested in more of a summary, skip to the Summary of Root Cause section bel
  - DAN-188 (correcao) [Closing] 0.517: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working hard to prevent an issue like this from happ
  - DAN-188 (correcao) [The problem] 0.482: ### The problem  We observed the autovacuum scan the full table and all of its indexes, and then do the same thing again. After several hours, it successfully completed and updated the "last\_autovacu
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.8: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.627: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg
  - DAN-102 (llm) [sem seção] 0.611: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [sem seção] 0.598: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily

## q-256 (esperado: DAN-189)

- busca inicial: DAN-189, DAN-103, DAN-066, DAN-146, DAN-067, DAN-064, DAN-070, DAN-106, DAN-210, DAN-191
- justificativa: 
- aprofundar DAN-189: `operator reboot tool lax validation rebooted all servers fix` — Bate com o incidente atual: um operador usou uma ferramenta de reinício com validação frouxa para reiniciar poucos servidores em manutenção e acabou reiniciando todos os servidores do datacenter, exatamente o cenário descrito. Não há diferença relevante aparente.
  - DAN-189 (llm) [What Happened?] 0.646: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.587: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-257 (esperado: DAN-189)

- busca inicial: DAN-189, DAN-146, DAN-103, DAN-066, DAN-064, DAN-067, DAN-070, DAN-073, DAN-208, DAN-068
- justificativa: 
- aprofundar DAN-189: `root cause fix reboot all servers maintenance tool input validation` — O Joyent DAN-189 é o único com o mesmo gatilho: operador usou ferramenta de reinício em manutenção e acabou reiniciando todo o datacenter. Difere pelo detalhe do parâmetro -n esquecido, que o incidente atual não menciona.
  - DAN-189 (llm) [What Happened?] 0.563: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.55: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-258 (esperado: DAN-194)

- busca inicial: DAN-194, DAN-156, DAN-133, DAN-164, DAN-147, DAN-066, DAN-211, DAN-048, DAN-190, DAN-094
- justificativa: 
- aprofundar DAN-194: `secondary MongoDB overloaded troubleshooting change primary traffic overload root cause fix` — bate exatamente: secundárias MongoDB sobrecarregadas e mudança durante diagnóstico enviando tráfego ao primário; não há diferença relevante.
- aprofundar DAN-156: `MongoDB out of memory load query pattern monitoring fix` — bate no componente MongoDB e sobrecarga sob carga, mas não tem o gatilho de mudança acidental enviando tráfego para o primário.
- aprofundar DAN-133: `MongoDB replica set slow queries thread connection pool fix` — bate em MongoDB replica sets e lentidão, mas envolve upgrade JVM e pools de conexão, não a mudança de diagnóstico descrita.
  - DAN-194 (llm) [Website Intermittent Timeouts] 0.646: ## Website Intermittent Timeouts  ## Postmortem  ## Summary  On January 12th at 14:09 UTC, our engineers began responding to alerts for our click / open tracking services and primary MongoDB clusters 
  - DAN-194 (llm) [Summary] 0.621: ## Summary  After review of our MongoDB configurations, we deployed limits on the number of connections our services could establish to our primary MongoDB server. We prepared these changes and began 
  - DAN-194 (causa) [Corrective Actions] 0.357: ## Corrective Actions  - Deployment of Redundant Tracking Infrastructure (Complete) - Our tracking services have previously operated out of a single region. As part of previously planned infrastructur
  - DAN-194 (correcao) [Resolved] 0.444: ## Resolved  This incident has been resolved.  Posted Jan 12, 2017 - 15:10 PST  ## Monitoring  Mailgun engineers have made a series of changes to our system, which have improved the performance and st
  - DAN-194 (correcao) [Identified] 0.327: ## Identified  We’re seeing improved performance and stability from our core API & SMTP services at this time. The engineering team is continuing to work to completely resolve the issue.  Posted Jan 1
  - DAN-156 (llm) [Foursquare outage post mortem - mongodb-user | Google Groups] 0.653: ## Foursquare outage post mortem - mongodb-user | Google Groups  After the first day's outage it had become clear that chunk migration, sans compaction, was not going to solve the immediate problem. B
  - DAN-156 (llm) [Foursquare outage post mortem - mongodb-user | Google Groups] 0.646: ## Foursquare outage post mortem - mongodb-user | Google Groups  From: Eliot Horowitz <eliothorow...@gmail.com>  (Note: this is being posted with Foursquare’s permission.)  As many of you are aware, F
  - DAN-156 (causa) [Foursquare outage post mortem - mongodb-user | Google Groups] 0.442: ## Foursquare outage post mortem - mongodb-user | Google Groups  * What we missed in the interim Over these two months, check-ins were being written continually to each shard. Unfortunately, these che
  - DAN-156 (correcao) [Foursquare outage post mortem - mongodb-user | Google Groups] 0.322: ## Foursquare outage post mortem - mongodb-user | Google Groups  Most sharded deployments will not meet these criteria. Anyone whose documents are larger than 4KB will not suffer significant fragmenta
  - DAN-133 (llm) [Incident Report] 0.655: ## Incident Report  April 10, 2019 at 13:25 UTC we were alerted to sharp increases in multiple queues responsible for job and workflow processing. Our monitoring of MongoDB showed some issues, but not
  - DAN-133 (llm) [Incident Report] 0.646: ## Incident Report  Perhaps most importantly, MongoDB support pointed us at the `tcmalloc.spinlock_total_delay_ns` MongoDB stat. This stat correlates with the time spent on database operations blocked
  - DAN-133 (causa) [Incident Report] 0.453: ## Incident Report  Between March 26 and April 10, 2019, our platform experienced instability and downtime primarily due to issues with the datastore backing our builds queue. These datastore issues r
  - DAN-133 (correcao) [Incident Report] 0.533: ## Incident Report  Ultimately, refactoring the way we store and access portions of our data set in MongoDB will reduce load. Improving our data access and storage at the application level is one of o
  - DAN-133 (correcao) [Incident Report] 0.47: ## Incident Report  Around the same time, we updated many services to a new minor version of the JVM to pick up security changes. This update also included improvements for docker-awareness enabled by

## q-259 (esperado: DAN-194)

- busca inicial: DAN-194, DAN-156, DAN-133, DAN-164, DAN-147, DAN-048, DAN-066, DAN-130, DAN-096, DAN-094
- justificativa: 
- aprofundar DAN-194: `MongoDB secondary overload troubleshooting change primary overload fix` — Secundários do MongoDB sobrecarregados e mudança durante troubleshooting enviou todo o tráfego secundário para o primário, sobrecarregando-o também — corresponde exatamente ao incidente atual.
  - DAN-194 (llm) [Website Intermittent Timeouts] 0.624: ## Website Intermittent Timeouts  ## Postmortem  ## Summary  On January 12th at 14:09 UTC, our engineers began responding to alerts for our click / open tracking services and primary MongoDB clusters 
  - DAN-194 (llm) [Summary] 0.611: ## Summary  After review of our MongoDB configurations, we deployed limits on the number of connections our services could establish to our primary MongoDB server. We prepared these changes and began 
  - DAN-194 (causa) [Corrective Actions] 0.357: ## Corrective Actions  - Deployment of Redundant Tracking Infrastructure (Complete) - Our tracking services have previously operated out of a single region. As part of previously planned infrastructur
  - DAN-194 (correcao) [Resolved] 0.444: ## Resolved  This incident has been resolved.  Posted Jan 12, 2017 - 15:10 PST  ## Monitoring  Mailgun engineers have made a series of changes to our system, which have improved the performance and st
  - DAN-194 (correcao) [Identified] 0.327: ## Identified  We’re seeing improved performance and stability from our core API & SMTP services at this time. The engineering team is continuing to work to completely resolve the issue.  Posted Jan 1

## q-260 (esperado: DAN-197)

- busca inicial: DAN-066, DAN-106, DAN-067, DAN-029, DAN-209, DAN-220, DAN-154, DAN-205, DAN-008, DAN-133
- justificativa: 
- aprofundar DAN-066: `Byzantine failure switch misbehavior API outage root cause fix` — Falha repentina na API de um provedor de nuvem sem mudanças do usuário, causada por comportamento anômalo de infraestrutura (switch), muito parecido com o incidente atual.
- aprofundar DAN-067: `data center power failure thundering herd API calls rate limit fix` — Chamadas de API começaram a falhar repentinamente por causa de falha de infraestrutura do provedor (energia), sem mudanças do cliente, embora o thundering herd seja efeito colateral.
- aprofundar DAN-008: `Tiered Cache change 530 errors root cause fix rollback` — Requisições à API começaram a falhar de repente por mudança do provedor (não do usuário), embora aqui haja alteração de cache do lado do provedor e não apenas falha de chamada.
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.612: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.612: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-067 (llm) [Disaster Recovery] 0.704: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.65: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-008 (llm) [sem seção] 0.768: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.703: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac

## q-261 (esperado: DAN-197)

- busca inicial: DAN-067, DAN-066, DAN-220, DAN-154, DAN-029, DAN-008, DAN-133, DAN-106, DAN-205, DAN-209
- justificativa: 
- aprofundar DAN-106: `EC2 RDS networking outage human error root cause fix` — Provedor de nuvem (AWS) com API/serviço caindo sem mudança do cliente, causado por erro de rede do próprio provedor.
- aprofundar DAN-066: `Byzantine switch failure API availability root cause fix` — Falha de infraestrutura do provedor (switch) derrubando API, sem mudança do cliente.
- aprofundar DAN-067: `data center power failure API thundering herd fix` — Chamadas de API falhando após falha externa no data center do provedor, com recuperação via controle de carga.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.715: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.698: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.61: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.603: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-067 (llm) [Attempting to Restore Power] 0.702: ### Attempting to Restore Power  While we haven't gotten official confirmation, we have been told by employees that three things hampered getting the generators back online. First, they needed to be p
  - DAN-067 (llm) [Lessons and Remediation] 0.691: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-262 (esperado: DAN-200)

- busca inicial: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073, DAN-189, DAN-146, DAN-210, DAN-043, DAN-200
- justificativa: 
- aprofundar DAN-200: `Mars Pathfinder system resets priority inversion VxWorks patch priority inheritance` — Semelha porque descreve reinícios do computador de bordo dias depois do início da operação, com causa e correção de software.
- aprofundar DAN-198: `Apollo 11 rendezvous radar CPU load computer restart cause fix` — Semelha porque envolve reinício do computador de uma nave, embora o gatilho seja sobrecarga durante o pouso, não dias após a operação.
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.662: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [THE FAILURE] 0.639: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.733: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.696: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-263 (esperado: DAN-200)

- busca inicial: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-073, DAN-146, DAN-106, DAN-069, DAN-066
- justificativa: 
- aprofundar DAN-200: `Mars Pathfinder priority inversion VxWorks reset patch priority inheritance` — O computador de bordo reinicia dias após começar a operar, exatamente como o Pathfinder em Marte; a diferença é o contexto espacial versus operação genérica.
- aprofundar DAN-198: `Apollo 11 rendezvous radar CPU load computer restart fix` — Ambos envolvem reinicialização de computador de bordo por sobrecarga de CPU, mas o Apolo 11 ocorreu durante o pouso lunar, não dias após iniciar a operação.
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.65: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [THE FAILURE] 0.63: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.735: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.696: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-264 (esperado: DAN-204)

- busca inicial: DAN-175, DAN-215, DAN-204, DAN-203, DAN-124, DAN-131, DAN-058, DAN-136, DAN-141, DAN-107
- justificativa: 
- aprofundar DAN-204: `corrupted Redis queue mixed user responses billing info root cause fix` — O resumo descreve exatamente usuários vendo dados de outros usuários, incluindo billing info, por corrupção de filas Redis, o que bate com o incidente atual; não bate porque é um outage do ChatGPT, não necessariamente o mesmo sistema.
- aprofundar DAN-175: `private tokens leaked customer data access root cause fix` — Vazamento de tokens privados permitiu acesso a dados de clientes, semelhante à exposição de dados de outros usuários, mas via credenciais vazadas e atacantes externos, não filas corrompidas.
- aprofundar DAN-058: `incorrect DB backup identifiers data leak free tier fix root cause` — Identificadores de backup incorretos causaram vazamento de dados entre clientes, parecido com exposição cross-user, mas ocorre em backups de banco, não em cache ou filas de requisição.
  - DAN-204 (llm) [Technical details] 0.624: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.599: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-175 (llm) [Incident Summary] 0.588: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.554: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro
  - DAN-058 (llm) [What happened?] 0.777: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.758: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n

## q-265 (esperado: DAN-204)

- busca inicial: DAN-175, DAN-204, DAN-124, DAN-058, DAN-131, DAN-203, DAN-220, DAN-107, DAN-098, DAN-164
- justificativa: 
- aprofundar DAN-204: `Redis cache corruption out of sequence cross user data billing info fix` — Mesmo sintoma do incidente atual: usuários veem dados de outros usuários, incluindo informações de faturamento, embora a causa (corrupção de cache Redis) possa ser diferente.
- aprofundar DAN-175: `private token leak unauthorized data access root cause fix` — Envolve vazamento de dados de clientes através de tokens expostos, mas se trata de atacantes externos e não de usuários comuns vendo dados uns dos outros.
- aprofundar DAN-058: `misconfigured DB backup identifiers data leak free tier fix` — Vazamento de dados causado por configuração incorreta de identificadores, mas afeta bancos de dados de tier gratuito em vez de exposição cruzada entre usuários.
  - DAN-204 (llm) [Technical details] 0.639: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.624: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-175 (llm) [Incident Summary] 0.58: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (llm) [Incident Summary] 0.576: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro
  - DAN-058 (llm) [What happened?] 0.806: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.755: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n

## q-266 (esperado: DAN-205)

- busca inicial: DAN-205, DAN-209, DAN-184, DAN-191, DAN-180, DAN-066, DAN-106, DAN-065, DAN-234, DAN-129
- justificativa: 
- aprofundar DAN-205: `two deployments high latency connectivity quorum notifications root cause fix peering point` — Bate: duas de três implantações independentes, latência alta de rede, perda de conectividade e falha no envio de notificações devido à perda de quorum — padrão idêntico ao incidente atual. Não bate: a causa (ponto de peering compartilhado instável) ainda não está confirmada no incidente em andamento.
  - DAN-205 (llm) [The Outage] 0.751: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.649: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-267 (esperado: DAN-205)

- busca inicial: DAN-205, DAN-209, DAN-184, DAN-148, DAN-066, DAN-116, DAN-107, DAN-191, DAN-109, DAN-234
- justificativa: 
- aprofundar DAN-205: `two deployments high latency connection loss quorum notification failure fix peering point` — Bate exatamente: duas de três implantações com alta latência e perda de conexão simultânea, e o sistema parou de enviar notificações por falha de quórum; não bate o detalhe da causa raiz (ponto de peering compartilhado), ainda desconhecida no incidente atual.
  - DAN-205 (llm) [The Outage] 0.744: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.638: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-268 (esperado: DAN-207)

- busca inicial: DAN-207, DAN-215, DAN-084, DAN-124, DAN-132, DAN-146, DAN-050, DAN-141, DAN-131, DAN-239
- justificativa: 
- aprofundar DAN-207: `Parity multi-sig wallet security bug root cause fix` — DAN-207 envolve criptomoedas sendo roubadas/direcionadas devido a um bug de segurança em código implantado e usado por terceiros, semelhante ao incidente atual de carteiras cripto sendo esvaziadas via código; difere por ser um bug em biblioteca multi-sig rotulado como mudança de UI.
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.838: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [sem seção] 0.79: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 

## q-269 (esperado: DAN-207)

- busca inicial: DAN-207, DAN-215, DAN-132, DAN-175, DAN-124, DAN-084, DAN-160, DAN-141, DAN-016, DAN-219
- justificativa: 
- aprofundar DAN-207: `multi-sig wallet security bug root cause patch fix` — O incidente envolve roubo de criptomoeda por falha de segurança em código de carteira multi-assinatura implantado e usado por terceiros, semelhante ao atual, diferindo por se tratar de contrato inteligente e não biblioteca de carteira.
- aprofundar DAN-215: `cryptocurrency theft employee security controls remediation` — Envolve roubo de criptomoeda, mas por funcionário interno com práticas de segurança ruins, não por atacantes externos explorando vulnerabilidade no código da carteira.
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.752: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [sem seção] 0.73: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.597: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.528: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Rovion installed a rootkit at /bin/udevd-bridge Rovion purchased information from a previous employee which allowed him to conduct the attacks on ShapeShift. This
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.355: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo

## q-270 (esperado: DAN-208)

- busca inicial: DAN-208, DAN-079, DAN-151, DAN-066, DAN-106, DAN-144, DAN-191, DAN-222, DAN-205, DAN-220
- justificativa: 
- aprofundar DAN-208: `Zookeeper scheduled maintenance too much data boot failure fix` — Mesmo cenário: janela de manutenção programada e Zookeeper que não consegue subir/bootar, diferindo apenas no detalhe de excesso de dados.
- aprofundar DAN-079: `Zookeeper reprovisioning replacement hosts second leader fix` — Também envolve Zookeeper em manutenção/reprovisioning, mas o sintoma é eleição de segundo líder, não incapacidade de subir.
  - DAN-208 (llm) [Wrapping up] 0.703: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (llm) [Read the socket] 0.671: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\
  - DAN-079 (llm) [sem seção] 0.642: In October, we experienced one incident resulting in significant impact and degraded state of availability for issues, pull requests, webhooks, GitHub Actions, and GitHub Pages services.  While reprov

## q-271 (esperado: DAN-208)

- busca inicial: DAN-208, DAN-151, DAN-079, DAN-103, DAN-211, DAN-066, DAN-135, DAN-220, DAN-026, DAN-109
- justificativa: 
- aprofundar DAN-208: `Zookeeper cannot start too much data boot root cause fix` — Escolhi porque ambos ocorrem durante janela de manutenção programada e envolvem o Zookeeper que não consegue inicializar, embora o resumo mencione excesso de dados como causa específica.
- aprofundar DAN-079: `ZooKeeper reprovisioning second leader split brain fix root cause` — Escolhi porque envolve ZooKeeper e mudança programada (reprovisionamento), mas a falha é eleição de segundo líder/cluster dividido, não a incapacidade de iniciar após manutenção.
  - DAN-208 (llm) [Read the socket] 0.685: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (llm) [Wrapping up] 0.642: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\
  - DAN-079 (llm) [sem seção] 0.66: In October, we experienced one incident resulting in significant impact and degraded state of availability for issues, pull requests, webhooks, GitHub Actions, and GitHub Pages services.  While reprov

## q-272 (esperado: DAN-215)

- busca inicial: DAN-215, DAN-207, DAN-084, DAN-050, DAN-131, DAN-015, DAN-029, DAN-203, DAN-175, DAN-124
- justificativa: 
- aprofundar DAN-215: `employee cryptocurrency theft multiple hacks security fix remediation` — Bate: roubo de criptomoeda repetido (3 hacks em 1 mês) e falha de segurança. Não bate: foi interno (funcionário), não carteira externa.
- aprofundar DAN-207: `multi sig wallet security bug fix patch stolen funds` — Bate: criptomoeda desviada/roubada. Não bate: causa foi bug em contrato multi-sig, não roubo direto de carteira.
- aprofundar DAN-131: `session cookie theft malware credential compromise remediation fix` — Bate: invasão via roubo de credenciais/sessão. Não bate: não envolve criptomoeda diretamente.
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.619: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.547: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo
  - DAN-207 (llm) [sem seção] 0.729: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.722: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-131 (llm) [What happened?] 0.599: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.481: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi

## q-273 (esperado: DAN-215)

- busca inicial: DAN-207, DAN-215, DAN-084, DAN-131, DAN-015, DAN-050, DAN-209, DAN-175, DAN-219, DAN-132
- justificativa: 
- aprofundar DAN-215: `cryptocurrency theft multiple hacks employee security practices root cause fix` — Bate com roubo de criptomoeda ocorrendo várias vezes em curto período (1 mês), igual ao 'segunda vez em poucas semanas' do atual; não bate porque o autor foi um funcionário interno, não um invasor externo.
- aprofundar DAN-207: `multi-sig hack security bug software change root cause fix` — Bate com roubo/diversão de criptomoeda causado por falha de segurança; não bate porque foi um único evento grande decorrente de mudança de software, não roubos repetidos em poucas semanas.
- aprofundar DAN-131: `unauthorized third party malware session cookie theft root cause fix` — Bate com intrusão de terceiro não autorizado e roubo de credenciais/sessão; não bate porque não envolve criptomoeda nem repetição do incidente em curto espaço de tempo.
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.571: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.517: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.681: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [HOW DID THE BUG ESCAPE NOTICE?] 0.667: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (causa) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.31: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [sem seção] 0.307: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-131 (llm) [What happened?] 0.611: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.507: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi

## q-274 (esperado: DAN-226)

- busca inicial: DAN-226, DAN-048, DAN-190, DAN-094, DAN-116, DAN-195, DAN-181, DAN-120, DAN-058, DAN-126
- justificativa: 
- aprofundar DAN-226: `SQL Server bugcheck root cause read only mode fix` — DAN-226 descreve exatamente o mesmo cenário do incidente atual: o SQL Server primário deu bugcheck e os sites entraram em modo somente leitura, diferentemente dos demais que envolvem outros bancos de dados ou causas distintas.
  - DAN-226 (llm) [sem seção] 0.584: On January 24, 2017 starting at 17:53 UTC, we experienced system degradation (read only) followed by a site outage. The Stack Exchange network went into read-only mode for approximately 5 minutes befo

## q-275 (esperado: DAN-226)

- busca inicial: DAN-226, DAN-048, DAN-181, DAN-094, DAN-173, DAN-120, DAN-116, DAN-056, DAN-195, DAN-080
- justificativa: 
- aprofundar DAN-226: `SQL Server bugcheck root cause fix read only mode` — Mesmo componente (SQL Server) e mesmos sintomas (bugcheck do processo primário, sites em modo read-only) do incidente atual.
- aprofundar DAN-120: `database integer limit read only mode root cause fix` — Compartilha o sintoma de modo read-only do banco, mas a causa é limite inteiro, não bugcheck do SQL Server.
  - DAN-226 (llm) [sem seção] 0.586: On January 24, 2017 starting at 17:53 UTC, we experienced system degradation (read only) followed by a site outage. The Stack Exchange network went into read-only mode for approximately 5 minutes befo
  - DAN-120 (llm) [sem seção] 0.661: Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, 
  - DAN-120 (llm) [sem seção] 0.493: We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998
  - DAN-120 (causa) [sem seção] 0.427: Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop using our status.basecamp.com updates and a play-by-play record on our blog. We can’t promise to be perfec

## q-276 (esperado: DAN-235)

- busca inicial: DAN-235, DAN-231, DAN-221, DAN-184, DAN-022, DAN-165, DAN-154, DAN-059, DAN-195, DAN-069
- justificativa: 
- aprofundar DAN-235: `high filtering SMS AT&T network root cause fix carrier blocking` — Descreve exatamente filtragem elevada de SMS para a rede AT&T nos Estados Unidos, igual ao sintoma atual; não há indício de que o componente ou gatilho sejam diferentes.
  - DAN-235 (llm) [Investigating] 0.724: ## Investigating  We are experiencing high filtering on SMS towards AT&T network in Unites states. Our engineers are working with our carrier partner to resolve the issue. We expect to provide another
  - DAN-235 (llm) [High Filtering On SMS Towards AT&T Network In United States] 0.712: ## High Filtering On SMS Towards AT&T Network In United States  ## Resolved  We are no longer experiencing high filtering on SMS towards AT&T network in the United States for all senders. This inciden
  - DAN-235 (causa) [Update] 0.24: ## Update  We are experiencing high filtering on SMS towards AT&T network in United States. Our engineers are continuing to work with our carrier partner to resolve the issue. We expect to provide ano
  - DAN-235 (correcao) [Monitoring] 0.273: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States. We will continue to monitor to ensure full service recovery. We expect to provide another
  - DAN-235 (correcao) [Monitoring] 0.254: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States for all senders. We will continue monitoring the service to ensure a full recovery. We wil

## q-277 (esperado: DAN-235)

- busca inicial: DAN-235, DAN-231, DAN-221, DAN-184, DAN-022, DAN-165, DAN-065, DAN-195, DAN-005, DAN-006
- justificativa: 
- aprofundar DAN-235: `SMS filtering AT&T network root cause fix resolution` — O incidente atual envolve filtragem de SMS para uma grande operadora dos EUA; DAN-235 trata exatamente de alta filtragem de SMS para a rede AT&T nos EUA, com mesmo sintoma e tipo de falha, diferindo apenas pelo provedor (Twilio).
  - DAN-235 (llm) [High Filtering On SMS Towards AT&T Network In United States] 0.732: ## High Filtering On SMS Towards AT&T Network In United States  ## Resolved  We are no longer experiencing high filtering on SMS towards AT&T network in the United States for all senders. This inciden
  - DAN-235 (llm) [Investigating] 0.727: ## Investigating  We are experiencing high filtering on SMS towards AT&T network in Unites states. Our engineers are working with our carrier partner to resolve the issue. We expect to provide another
  - DAN-235 (causa) [Update] 0.24: ## Update  We are experiencing high filtering on SMS towards AT&T network in United States. Our engineers are continuing to work with our carrier partner to resolve the issue. We expect to provide ano
  - DAN-235 (correcao) [Monitoring] 0.273: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States. We will continue to monitor to ensure full service recovery. We expect to provide another
  - DAN-235 (correcao) [Monitoring] 0.254: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States for all senders. We will continue monitoring the service to ensure a full recovery. We wil

## q-278 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-146, DAN-073, DAN-231, DAN-043, DAN-104, DAN-071, DAN-173, DAN-220, DAN-048
- justificativa: 
- aprofundar DAN-236: `steam desktop client deleted user files root cause fix` — É o único incidente com cliente desktop apagando arquivos locais do usuário, exatamente o sintoma atual.
- aprofundar DAN-146: `os upgrade wiped out machines databases root cause fix` — Também envolve apagamento de dados em máquinas, mas o gatilho é upgrade de SO, não cliente desktop.
- aprofundar DAN-043: `accidental database deletion human error recovery fix` — Envolve exclusão acidental de dados, embora seja banco de dados gerenciado, não cliente desktop.
  - DAN-236 (llm) [Activity] 0.696: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.696: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 
  - DAN-146 (llm) [sem seção] 0.616: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [sem seção] 0.507: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.694: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.629: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo

## q-279 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-146, DAN-073, DAN-164, DAN-043, DAN-104, DAN-220, DAN-126, DAN-173, DAN-058
- justificativa: 
- aprofundar DAN-236: `steam desktop client deleted user files root cause mitigation` — O cliente Steam deletou arquivos locais do usuário, igual ao incidente atual, embora tenha sido acionado após mover um diretório do Steam.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.683: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (llm) [Activity] 0.68: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 

## q-280 (esperado: DAN-237)

- busca inicial: DAN-237, DAN-142, DAN-152, DAN-131, DAN-136, DAN-011, DAN-124, DAN-122, DAN-034, DAN-090
- justificativa: 
- aprofundar DAN-237: `website compromised download links malicious zip root cause fix` — O incidente Xubuntu envolve exatamente um site comprometido cujos links de download apontam para um zip malicioso, igual ao cenário atual; não se trata de pacote npm, atualização de software ou infraestrutura indireta.
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.69: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  **Elizabeth K. Joseph**     lyz at ubuntu.com  *Mon Nov 17 17:59:36 UTC 2025*  Dear community, As
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.521: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  in a controlled, read-only mode to allow migration to a new static site. To be perfectly clear: t
  - DAN-237 (causa) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.234: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  generator has actually been in the works for some time as our reliance upon the dynamic features 

## q-281 (esperado: DAN-237)

- busca inicial: DAN-237, DAN-131, DAN-142, DAN-136, DAN-122, DAN-011, DAN-152, DAN-124, DAN-034, DAN-203
- justificativa: 
- aprofundar DAN-237: `website compromised download link malicious zip root cause fix` — O site do Xubuntu foi comprometido e os links de download alterados para servir um zip malicioso, igual ao incidente atual; não há diferença relevante no tipo de falha.
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.69: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  **Elizabeth K. Joseph**     lyz at ubuntu.com  *Mon Nov 17 17:59:36 UTC 2025*  Dear community, As
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.519: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  in a controlled, read-only mode to allow migration to a new static site. To be perfectly clear: t
  - DAN-237 (causa) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.234: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  generator has actually been in the works for some time as our reliance upon the dynamic features 

## q-282 (esperado: DAN-240)

- busca inicial: DAN-240, DAN-068, DAN-191, DAN-063, DAN-159, DAN-066, DAN-209, DAN-210, DAN-067, DAN-239
- justificativa: 
- aprofundar DAN-240: `leased line failure backup unstable order management fix remediation` — O incidente envolve falha de linha dedicada primária para bolsa e linha de backup instável afetando ordens, exatamente como o atual, embora o componente seja uma leased line da CTCL e não um link dedicado genérico.
  - DAN-240 (llm) [sem seção] 0.633: 13 Apr 2018, 01:48 PM  # Postmortem: Trading and hanging orders on 12th April 2018  Traders,  Yesterday, on the 12th April, one of the NSE leased line connections to our setup went down. This affected
  - DAN-240 (llm) [Postmortem: Trading and hanging orders on 12th April 2018] 0.485: # Postmortem: Trading and hanging orders on 12th April 2018  Once the CTCL was shut off, the orders which were showing any of the pending states were lapsed and reconciled with the exchange. This affe

## q-283 (esperado: DAN-240)

- busca inicial: DAN-240, DAN-209, DAN-191, DAN-068, DAN-239, DAN-077, DAN-205, DAN-067, DAN-106, DAN-159
- justificativa: 
- aprofundar DAN-240: `primary leased line failure backup line sporadic root cause fix orders validation` — Bate exatamente: linha alugada primária para bolsa caiu, linha de backup instável, ordens afetadas. Não bate: provedor não melhorou confiabilidade fundamentalmente.
  - DAN-240 (llm) [sem seção] 0.623: 13 Apr 2018, 01:48 PM  # Postmortem: Trading and hanging orders on 12th April 2018  Traders,  Yesterday, on the 12th April, one of the NSE leased line connections to our setup went down. This affected
  - DAN-240 (llm) [Postmortem: Trading and hanging orders on 12th April 2018] 0.426: # Postmortem: Trading and hanging orders on 12th April 2018  Once the CTCL was shut off, the orders which were showing any of the pending states were lapsed and reconciled with the exchange. This affe
