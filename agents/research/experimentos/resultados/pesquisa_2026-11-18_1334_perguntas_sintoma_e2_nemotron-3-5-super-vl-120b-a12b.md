# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-006 | DAN-015 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-008 | DAN-142 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-010 | DAN-137 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-012 | DAN-211 | 5 | sim | sim | search | não | sim | 0 | 9 |
| q-014 | DAN-078 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-016 | DAN-067 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-018 | DAN-162 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-020 | DAN-164 | 4 | sim | sim | search | não | sim | 0 | 12 |
| q-022 | DAN-104 | 4 | sim | sim | search | não | sim | 0 | 14 |
| q-024 | DAN-004 | 1 | sim | sim | search | não | sim | 0 | 32 |
| q-026 | DAN-011 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-028 | DAN-137 | 2 | sim | sim | search | não | sim | 0 | 13 |
| q-030 | DAN-078 | 1 | sim | sim | search | não | sim | 0 | 19 |
| q-032 | DAN-104 | 7 | sim | sim | search | não | sim | 0 | 15 |
| q-034 | DAN-004 | 12 | não | não | search | não | não | 0 | 10 |
| q-036 | DAN-019 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-038 | DAN-090 | 2 | sim | sim | search | não | sim | 0 | 7 |
| q-164 | DAN-001 | 1 | sim | sim | search | não | sim | 0 | 37 |
| q-165 | DAN-001 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-166 | DAN-003 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-167 | DAN-003 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-168 | DAN-017 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-169 | DAN-017 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-170 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 12 |
| q-171 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 9 |
| q-172 | DAN-020 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-173 | DAN-020 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-174 | DAN-022 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-175 | DAN-022 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-176 | DAN-026 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-177 | DAN-026 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-178 | DAN-033 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-179 | DAN-033 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-180 | DAN-042 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-181 | DAN-042 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-182 | DAN-043 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-183 | DAN-043 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-184 | DAN-048 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-185 | DAN-048 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-186 | DAN-049 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-187 | DAN-049 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-188 | DAN-050 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-189 | DAN-050 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-190 | DAN-058 | 2 | sim | sim | search | não | sim | 0 | 13 |
| q-191 | DAN-058 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-192 | DAN-059 | 2 | sim | sim | search | não | sim | 0 | 15 |
| q-193 | DAN-059 | 2 | sim | sim | search | não | sim | 0 | 11 |
| q-194 | DAN-060 | 3 | sim | sim | search | não | sim | 0 | 27 |
| q-195 | DAN-060 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-196 | DAN-065 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-197 | DAN-065 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-198 | DAN-069 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-199 | DAN-069 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-200 | DAN-073 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-201 | DAN-073 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-202 | DAN-076 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-203 | DAN-076 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-204 | DAN-083 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-205 | DAN-083 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-206 | DAN-085 | 2 | sim | sim | search | não | sim | 0 | 9 |
| q-207 | DAN-085 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-208 | DAN-086 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-209 | DAN-086 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-210 | DAN-088 | 1 | sim | sim | search | não | sim | 0 | 19 |
| q-211 | DAN-088 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-212 | DAN-092 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-213 | DAN-092 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-214 | DAN-093 | 3 | sim | sim | search | não | sim | 0 | 12 |
| q-215 | DAN-093 | 3 | sim | sim | search | não | sim | 0 | 10 |
| q-216 | DAN-106 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-217 | DAN-106 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-218 | DAN-116 | 9 | sim | sim | search | não | sim | 0 | 14 |
| q-219 | DAN-116 | 7 | sim | sim | search | não | sim | 0 | 7 |
| q-220 | DAN-118 | 2 | sim | sim | search | não | sim | 0 | 10 |
| q-221 | DAN-118 | 2 | sim | sim | search | não | sim | 0 | 22 |
| q-222 | DAN-121 | 4 | sim | sim | search | não | sim | 0 | 9 |
| q-223 | DAN-121 | 8 | sim | sim | search | não | sim | 0 | 13 |
| q-224 | DAN-122 | 2 | sim | sim | search | não | sim | 0 | 21 |
| q-225 | DAN-122 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-226 | DAN-124 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-227 | DAN-124 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-228 | DAN-125 | 11 | não | não | search | não | não | 0 | 11 |
| q-229 | DAN-125 | 10 | sim | sim | search | não | sim | 0 | 13 |
| q-230 | DAN-126 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-231 | DAN-126 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-232 | DAN-127 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-233 | DAN-127 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-234 | DAN-129 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-235 | DAN-129 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-236 | DAN-145 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-237 | DAN-145 | 1 | sim | sim | search | não | sim | 0 | 19 |
| q-238 | DAN-148 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-239 | DAN-148 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-240 | DAN-152 | 4 | sim | sim | search | não | sim | 0 | 7 |
| q-241 | DAN-152 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-242 | DAN-154 | — | não | não | search | não | não | 0 | 15 |
| q-243 | DAN-154 | 12 | não | não | search | não | não | 0 | 13 |
| q-244 | DAN-165 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-245 | DAN-165 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-246 | DAN-170 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-247 | DAN-170 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-248 | DAN-180 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-249 | DAN-180 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-250 | DAN-183 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-251 | DAN-183 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-252 | DAN-186 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-253 | DAN-186 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-254 | DAN-188 | 1 | sim | sim | search | não | sim | 0 | 20 |
| q-255 | DAN-188 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-256 | DAN-189 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-257 | DAN-189 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-258 | DAN-194 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-259 | DAN-194 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-260 | DAN-197 | 19 | não | não | search | não | não | 0 | 15 |
| q-261 | DAN-197 | — | não | não | search | não | não | 0 | 9 |
| q-262 | DAN-200 | 10 | sim | sim | search | não | sim | 0 | 9 |
| q-263 | DAN-200 | 5 | sim | sim | search | não | sim | 0 | 11 |
| q-264 | DAN-204 | 3 | sim | sim | search | não | sim | 0 | 8 |
| q-265 | DAN-204 | 2 | sim | sim | search | não | sim | 0 | 8 |
| q-266 | DAN-205 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-267 | DAN-205 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-268 | DAN-207 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-269 | DAN-207 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-270 | DAN-208 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-271 | DAN-208 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-272 | DAN-215 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-273 | DAN-215 | 2 | sim | sim | search | não | sim | 0 | 9 |
| q-274 | DAN-226 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-275 | DAN-226 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-276 | DAN-235 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-277 | DAN-235 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-278 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-279 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-280 | DAN-237 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-281 | DAN-237 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-282 | DAN-240 | 1 | sim | sim | search | não | sim | 0 | 22 |
| q-283 | DAN-240 | 1 | sim | sim | search | não | sim | 0 | 18 |

## q-006 (esperado: DAN-015)

- busca inicial: DAN-015, DAN-184, DAN-140, DAN-221, DAN-086, DAN-009, DAN-066, DAN-053, DAN-017, DAN-204
- justificativa: 
- aprofundar DAN-015: `credential rotation root cause fix R2 Gateway authentication` — Bate exatamente: object storage (R2), erros de autenticação após rotação de credenciais e remoção das antigas. Não bate: ambiente default vs produção por faltar flag.
- aprofundar DAN-009: `service token code release root cause fix HTTP 401` — Bate parcialmente: HTTP 401 e falha em código que gerencia service tokens. Não bate: não é rotação de credenciais, é release de código.
- aprofundar DAN-017: `deployment tool bug staging production HTTP 401 root cause fix` — Bate parcialmente: HTTP 401 e erro de deploy apontando para endpoint errado. Não bate: não envolve rotação de credenciais.
  - DAN-015 (llm) [Next steps] 0.712: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor
  - DAN-015 (llm) [Next steps] 0.702: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (causa) [Incident timeline] 0.42: ## Incident timeline  Given gradual decline in availability metrics, R2 engineering team suspected a potential regression in propagation of new credentials in storage infrastructure. | | Mar 21, 2025 
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [sem seção] 0.434: We’re deeply sorry for this incident and the disruption it may have caused to you or your users. We hold ourselves to a high standard and this is not acceptable. This blog post exactly explains the im
  - DAN-009 (llm) [What went wrong?] 0.653: ### What went wrong?  As a result of the bug, any Cloudflare account that used a service token to authenticate during the 10 minutes “last seen at” release was out would have its “client secret” value
  - DAN-009 (llm) [What went wrong?] 0.635: ### What went wrong?  The “last seen at” value was derived by scanning all new login events in an account’s login event Kafka queue. If a login event using a service token was detected, an update to t
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [How did we fix the issue?] 0.483: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-017 (llm) [Analysis] 0.547: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Resolution] 0.546: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.

## q-008 (esperado: DAN-142)

- busca inicial: DAN-142, DAN-154, DAN-146, DAN-126, DAN-226, DAN-116, DAN-217, DAN-074, DAN-143, DAN-103
- justificativa: 
- aprofundar DAN-142: `content validator bug out-of-bounds memory read Windows BSOD fix rollback revert` — DAN-142 descreve atualização de conteúdo de segurança (CrowdStrike Falcon) que causou BSOD em massa no Windows, igual ao incidente atual; ainda não se sabe se é o mesmo produto, mas o padrão de falha (update de segurança seguido de crash simultâneo de servidores Windows) coincide.
  - DAN-142 (llm) [Q: What happened?] 0.664: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [Technical Details] 0.573: ## Technical Details  - Technical Details on the outage can be found here: Read the blog Published 2024-07-20 0100 UTC - We assure our customers that *CrowdStrike is operating normally and this issue 
  - DAN-142 (causa) [What Went Wrong and Why?] 0.384: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di

## q-010 (esperado: DAN-137)

- busca inicial: DAN-137, DAN-016, DAN-005, DAN-035, DAN-183, DAN-026, DAN-220, DAN-148, DAN-106, DAN-012
- justificativa: 
- aprofundar DAN-137: `WAF rule regex backtracking CPU exhaustion rollback fix` — Gatilho idêntico: mudança de regra de firewall/WAF na borda causa exaustão de CPU e queda de requisições; difere o detalhe (regex específico vs regra genérica).
- aprofundar DAN-016: `DDoS mitigation rule rate limiting infinite loop 100% CPU fix` — Nova regra de mitigação dispara loop infinito e CPU 100% nos handlers de borda, igual ao sintoma atual; componente é rate-limiting, não exatamente firewall.
- aprofundar DAN-012: `WAF config change Lua exception ruleset module fix` — Mudança de configuração WAF se propaga nos proxies de borda, gatilho de regra semelhante; sintoma é HTTP 500, não CPU 100%.
  - DAN-137 (llm) [Appendix: About Regular Expression Backtracking] 0.724: ### Appendix: About Regular Expression Backtracking  To fully understand how ``(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*
  - DAN-137 (llm) [The events of July 2] 0.714: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [sem seção] 0.482: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.658: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.643: ## Technical description of the error and how it happened  *Global percentage of HTTP Request handling processes that were using excessive CPU during the event*  Earlier on June 20, between 14:14 - 17
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Remediation and follow-up steps] 0.472: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-012 (llm) [What happened] 0.684: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (llm) [What happened] 0.667: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 

## q-012 (esperado: DAN-211)

- busca inicial: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-066, DAN-222, DAN-113, DAN-101, DAN-133
- justificativa: 
- aprofundar DAN-020: `service discovery root cause fix config dependent client` — Direto sobre service discovery: config ruim em um cliente derrubou discovery global quando cliente dependente caiu — bate com service discovery lento e writes com timeout, mas não menciona writes especificamente.
- aprofundar DAN-211: `Consul streaming BoltDB service discovery health check load root cause fix` — Menciona Consul (service discovery) e health check load afetando serviços internos — bate com discovery lento e serviços falhando, mas o contexto é uma interrupção de 73h, não apenas writes com timeout.
- aprofundar DAN-220: `exponential backoff cascading failure microservice root cause fix` — Falha em cascata por falta de backoff exponencial — bate com outros serviços começando a falhar, mas não é específico a service discovery nem a writes com timeout.
  - DAN-020 (llm) [The failure of a core system] 0.685: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [A thundering herd] 0.665: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Improve the resilience of service discovery] 0.401: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-211 (llm) [Return to Service Attempt #1 (10/29 02:00 – 04:00)] 0.697: ### Return to Service Attempt #1 (10/29 02:00 – 04:00)  The reset went smoothly, and initially, the metrics looked good. When we removed the iptables block, the service discovery and health check load
  - DAN-211 (llm) [Outage Summary] 0.677: ### Outage Summary  The outage was unique in both duration and complexity. The team had to address a number of challenges in sequence to understand the root cause and bring the service back up.  - The
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-220 (llm) [First symptoms: two months before the outage] 0.651: ## First symptoms: two months before the outage  Two months before the big outage we had an incident connected with one of our smallest backend services: Popcount. Popcount (this is our internal name)
  - DAN-220 (llm) [Lessons learned] 0.648: ## Lessons learned  - We should have prioritized fixing the backoff bug in the client after the first Popcount incident, we did not assign the right severity. We thought having the fast fail mechanism
  - DAN-220 (causa) [The night of April 27th] 0.485: ## The night of April 27th  It was a rainy Saturday night in Stockholm. Some of our engineers were online on IRC, and discovered that Popcount was unhealthy again. We thought the fast fail logic we in
  - DAN-220 (correcao) [Remediations in place after the second incident] 0.641: ## Remediations in place after the second incident  After the outage (infamously known as OPS-6000 in our incident tracking system), we held a post-mortem meeting where we invited the entire Technolog
  - DAN-220 (correcao) [Remediations: why are they important?] 0.568: ## Remediations: why are they important?  For every incident we hold a post-mortem meeting. The goal of this meeting is producing a list of remediations that we need to put in place in order to preven

## q-014 (esperado: DAN-078)

- busca inicial: DAN-078, DAN-066, DAN-006, DAN-048, DAN-164, DAN-205, DAN-043, DAN-162, DAN-116, DAN-023
- justificativa: 
- aprofundar DAN-078: `network partition MySQL failover missing writes data integrity fix` — Bate com pane de rede entre data centers, failover de banco e dados divergentes após failover; não detalha exatamente o mesmo componente de banco.
- aprofundar DAN-048: `RDS Multi-AZ failover incorrect MySQL configuration data loss recovery` — Bate com failover de banco de dados e perda/corrompimento de dados; não bate no gatilho, que foi falha de hardware e não pane de rede.
- aprofundar DAN-205: `datacenter connectivity high latency quorum failure recovery` — Bate com problemas de conectividade entre data centers; não bate em failover de banco nem em divergência de dados entre sites.
  - DAN-078 (llm) [Incident timeline] 0.678: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [Next steps] 0.666: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [Communication] 0.474: ## Communication  In our desire to communicate meaningful information to you during the incident, we made several public estimates on time to repair based on the rate of processing of the backlog of d
  - DAN-048 (llm) [Incorrect configuration variable] 0.82: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Final thoughts] 0.814: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-205 (llm) [The Outage] 0.642: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Background] 0.622: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (causa) [Long term] 0.47: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Outage Post-Mortem – April 13, 2013] 0.374: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 

## q-016 (esperado: DAN-067)

- busca inicial: DAN-067, DAN-068, DAN-064, DAN-069, DAN-023, DAN-063, DAN-191, DAN-060, DAN-209, DAN-062
- justificativa: 
- aprofundar DAN-067: `data center power failure control plane analytics outage root cause remediation` — Escolhi porque é um outage de control plane e analytics causado por falha de energia em data center, igual ao incidente atual.
- aprofundar DAN-068: `data center power loss breaker coordination redundant power paths fix` — Escolhi porque é uma perda completa de energia em data center que bypassou redundância, mesmo gatilho, embora não mencione analytics.
- aprofundar DAN-062: `facility power loss severe weather backup energy reserves isolation breakers fix` — Escolhi porque é uma perda de energia em facility por clima severo com falha de breakers, mesmo gatilho de perda de energia no site.
  - DAN-067 (llm) [Lessons and Remediation] 0.745: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.724: ### Flexential Data Center Power Failure  The largest of the three facilities in Oregon is run by Flexential. We refer to this facility as “PDX-DC04”. Cloudflare leases space in PDX-04 where we house 
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-068 (llm) [What happened to the power in the data center?] 0.732: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.68: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.614: ### Summary of the AWS Service Event in the Sydney Region  If utility power is interrupted, the DRUPS uses this stored energy to continue to provide power to the datacenter while the integrated genera
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.559: ### Summary of the AWS Service Event in the Sydney Region  We’d like to share more detail about the AWS service disruption that occurred this past weekend in the AWS Sydney Region. The service disrupt
  - DAN-062 (causa) [Summary of the AWS Service Event in the Sydney Region] 0.399: ### Summary of the AWS Service Event in the Sydney Region  A latent bug in our instance management software led to a slower than expected recovery of the remaining instances. The team worked over the 
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.388: ### Summary of the AWS Service Event in the Sydney Region  Additionally, we will be taking actions to improve our recovery systems. The first is to fix the latent issue that led to our recovery system
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.359: ### Summary of the AWS Service Event in the Sydney Region  During the initial part of this event, customers experienced errors when trying to launch new instances, or when trying to scale their auto-s

## q-018 (esperado: DAN-162)

- busca inicial: DAN-162, DAN-026, DAN-010, DAN-164, DAN-075, DAN-020, DAN-087, DAN-066, DAN-186, DAN-049
- justificativa: 
- aprofundar DAN-162: `database migration DNS resolution failure root cause fix recovery` — O incidente atual descreve servidores DNS de um site falhando após uma migração de banco de dados, o que corresponde diretamente ao resumo do DAN-162 (migração de banco quebrou DNS em um site); difere principalmente por ser um post-mortem público da GitHub em vez do ambiente do usuário.
  - DAN-162 (llm) [sem seção] 0.554: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5

## q-020 (esperado: DAN-164)

- busca inicial: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-091, DAN-186, DAN-092, DAN-066, DAN-058
- justificativa: 
- aprofundar DAN-043: `accidental database deletion backup recovery restore` — Bate pela exclusão acidental do banco de produção e restauração via backup; não especifica se ocorreu durante manutenção.
- aprofundar DAN-056: `environment variable truncate production database fix` — Bate pelo impacto acidental no banco de produção; o gatilho é variável de ambiente em testes, não manutenção direta.
- aprofundar DAN-164: `deleted wrong directory data loss recovery` — Bate pelo erro humano de exclusão de dados; não é o banco inteiro, mas sim um diretório, e menciona admin cansado.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.693: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.617: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [Remediation] 0.717: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (llm) [What We Learned] 0.714: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a
  - DAN-164 (llm) [Timeline] 0.572: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (llm) [sem seção] 0.552: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (causa) [Root cause analysis] 0.567: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-022 (esperado: DAN-104)

- busca inicial: DAN-191, DAN-189, DAN-146, DAN-104, DAN-064, DAN-067, DAN-073, DAN-109, DAN-209, DAN-103
- justificativa: 
- aprofundar DAN-104: `human error typo command remove servers S3 outage remediation fix` — Corresponde quase exatamente: operador executou comando para remover poucos servers, um erro removeu muito mais, o serviço de storage (S3) caiu e afetou sistemas dependentes em cascata.
- aprofundar DAN-189: `operator reboot all servers input validation outage remediation` — Semelhança parcial: operador com ferramenta de validação frouxa afetou mais servidores do que pretendia, mas a ação foi reboot e não remoção, e não houve foco em serviço de storage.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.63: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.623: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.647: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.615: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-024 (esperado: DAN-004)

- busca inicial: DAN-004, DAN-017, DAN-137, DAN-091, DAN-005, DAN-066, DAN-102, DAN-130, DAN-012, DAN-154
- justificativa: 
- aprofundar DAN-004: `WAF out-of-band change Terraform drift root cause fix` — Bate porque envolve tráfego de UI e build triggers bloqueado, mudança feita fora do pipeline (IAM/WAF fora do Terraform), e WAF desconsiderada como suspeita; não bate no provedor (CircleCI) nem no detalhe do drift detection automático.
- aprofundar DAN-012: `WAF configuration change global rollout root cause fix` — Bate porque envolve mudança de configuração WAF afetando tráfego global; não bate porque não menciona ausência de mudança no pipeline nem bloqueio específico de build triggers.
- aprofundar DAN-137: `WAF rule regex backtracking CPU outage root cause fix` — Bate porque envolve regra WAF causando incidente grave de disponibilidade; não bate porque a causa é regex/CPU, não uma mudança fora do pipeline de infraestrutura.
  - DAN-004 (llm) [**Root Cause Analysis**] 0.716: ## **Root Cause Analysis**  While we manage all our infrastructure, including WAF, almost entirely with Terraform, we discovered during this incident a misconfiguration in IAM controls that allowed a 
  - DAN-004 (llm) [What Happened] 0.664: ## What Happened  - **01:15:** Initial investigation revealed broad connectivity issues between the frontend and our backing APIs, including CORS (Cross-Origin Resource Sharing) errors. The team explo
  - DAN-004 (causa) [Summary] 0.416: ## Summary  On April 4, 2025, from 00:16 to 01:49 UTC (approximately 1 hour and 33 minutes), CircleCI experienced a service disruption affecting both our user interface and build capabilities. During 
  - DAN-004 (correcao) [Future Prevention and Process Improvement] 0.505: ## Future Prevention and Process Improvement  This incident highlighted the strength of our existing systems while identifying several areas where we can improve and make them even more robust:  1. We
  - DAN-004 (correcao) [What Happened] 0.435: ## What Happened  (all times UTC)  The WAF is a critical security component that sits in front of our services and protects them from malicious traffic, while allowing legitimate requests to pass thro
  - DAN-012 (llm) [What happened] 0.676: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (llm) [sem seção] 0.61: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (causa) [The runtime error] 0.383: ### The runtime error  Cloudflare’s rulesets system consists of sets of rules which are evaluated for each request entering our system. A rule consists of a filter, which selects some traffic, and an 
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 
  - DAN-137 (llm) [The events of July 2] 0.767: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (llm) [sem seção] 0.765: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (causa) [What happened] 0.441: ### What happened  Let’s begin with the sequence of events. All times in this blog are UTC.  At 13:42 an engineer working on the firewall team deployed a minor change to the rules for XSS detection vi
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-026 (esperado: DAN-011)

- busca inicial: DAN-011, DAN-005, DAN-019, DAN-016, DAN-007, DAN-012, DAN-049, DAN-035, DAN-008, DAN-018
- justificativa: 
- aprofundar DAN-012: `WAF config change global propagation Lua exception rulesets HTTP 500 fix rollback` — WAF é sistema de filtragem de tráfego, mudança de configuração propagada globalmente causou erros HTTP; não menciona arquivo de config gerado automaticamente nem CDN.
- aprofundar DAN-016: `DDoS mitigation rule rate limiting cookie validation infinite loop CPU fix rollback` — Regra de mitigação DDoS (filtragem de tráfego) implantada expôs bug que se propagou por data centers; não é arquivo de config automático nem CDN especificamente.
- aprofundar DAN-011: `bot detection file output limit permissions database outage fix rollback` — Arquivo gerado automaticamente excedeu limites e se propagou pela rede causando pane generalizada; não é sistema de filtragem de tráfego nem CDN.
  - DAN-012 (llm) [What happened] 0.755: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (llm) [What happened] 0.743: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.743: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.728: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-011 (llm) [Remediation and follow-up steps] 0.641: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [Remediation and follow-up steps] 0.581: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [How Cloudflare processes requests, and how this went wrong today] 0.393: ## How Cloudflare processes requests, and how this went wrong today  This feature file is refreshed every few minutes and published to our entire network and allows us to react to variations in traffi

## q-028 (esperado: DAN-137)

- busca inicial: DAN-016, DAN-137, DAN-148, DAN-005, DAN-064, DAN-183, DAN-106, DAN-035, DAN-129, DAN-115
- justificativa: 
- aprofundar DAN-016: `DDoS mitigation rule cookie validation infinite loop CPU fix rollback` — Nova regra de mitigação implantada causou loop infinito e 100% de CPU em handlers de requisição, espalhando por data centers, igual ao incidente atual, embora o alvo seja cookie validation.
- aprofundar DAN-137: `WAF rule regex backtracking CPU exhaustion fix rollback` — Regra WAF implantada causou exaustão global de CPU e downtime nos edge, correspondendo à regra de segurança e CPU atual, mas o gatilho é backtracking de regex e não validação de cookie.
  - DAN-016 (llm) [Remediation and follow-up steps] 0.718: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.715: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
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
- aprofundar DAN-078: `network partition MySQL master failover cross-continent latency data integrity restoration fix` — Ambos envolvem partição de rede entre data centers, failover de banco de dados e gravações que não se propagam para o novo mestre/região, causando divergência de dados; difere pelo foco na restauração prolongada do GitHub.
- aprofundar DAN-205: `network latency data centers quorum failure connectivity fix` — Ambos envolvem instabilidade de rede entre data centers afetando consenso/disponibilidade, mas o PagerDuty trata de quorum de notificações, não especificamente de gravações divergentes de banco após failover.
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.701: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [Incident timeline] 0.678: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-205 (llm) [The Outage] 0.649: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Background] 0.61: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (causa) [Long term] 0.47: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Outage Post-Mortem – April 13, 2013] 0.374: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 

## q-032 (esperado: DAN-104)

- busca inicial: DAN-109, DAN-210, DAN-189, DAN-191, DAN-067, DAN-073, DAN-104, DAN-103, DAN-026, DAN-070
- justificativa: 
- aprofundar DAN-104: `human error remove servers typo S3 outage restart recovery fix` — Bate exatamente: operador executa comando de rotina para remover poucos servidores e, por erro, remove mais, derrubando o serviço de storage (S3) e exigindo reinício completo para recuperar; não bate: é específico da AWS.
- aprofundar DAN-189: `operator reboot all servers lax validation outage manual intervention fix` — Bate parcialmente: operador executa comando de rotina que afeta muito mais servidores do que o planejado e deixa sistemas exigindo intervenção manual; não bate: envolve reboot de datacenter, não remoção de servidores de storage.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.645: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.634: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.32: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.688: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.627: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-034 (esperado: DAN-004)

- busca inicial: DAN-005, DAN-137, DAN-051, DAN-012, DAN-220, DAN-011, DAN-016, DAN-014, DAN-006, DAN-113
- justificativa: 
- aprofundar DAN-051: `firewall configuration change blocked traffic iptables root cause fix` — Bad firewall config blocked Stack Exchange/stackoverflow, igual ao incidente atual de tráfego bloqueado por regra de firewall sem mudança lembrada.
- aprofundar DAN-005: `router rule configuration crash root cause fix` — Regra de roteador causou pane geral na edge, mas envolve crash de roteadores não firewall bloqueando tráfego.
- aprofundar DAN-137: `WAF rule regex backtracking root cause fix` — Regra de segurança WAF causou pane global, mas é WAF com regex, não firewall simples bloqueando todo tráfego.
  - DAN-051 (llm) [sem seção] 0.613: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-051 (llm) [sem seção] 0.605: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-005 (llm) [Bad Rule] 0.729: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.609: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-137 (llm) [sem seção] 0.697: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (llm) [The events of July 2] 0.668: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [What happened] 0.441: ### What happened  Let’s begin with the sequence of events. All times in this blog are UTC.  At 13:42 an engineer working on the firewall team deployed a minor change to the rules for XSS detection vi
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-036 (esperado: DAN-019)

- busca inicial: DAN-019, DAN-007, DAN-005, DAN-006, DAN-059, DAN-022, DAN-023, DAN-210, DAN-159, DAN-013
- justificativa: 
- aprofundar DAN-019: `BGP export policy prefix list filter removal route leak fix` — Corresponde a anunciar rotas internas após mudança de política de roteamento, diferindo apenas pelo prefixo IPv6.
- aprofundar DAN-007: `BGP advertised prefixes ordering policy malfunction root cause fix` — Envolve ordem incorreta de anúncios BGP, embora não mencione vazamento de rotas para peers externos.
- aprofundar DAN-023: `backbone router configuration change BGP outage root cause fix` — Mudança de configuração de roteadores backbone causou indisponibilidade global, mas retirou rotas em vez de vazá-las.
  - DAN-019 (llm) [What happened: the configuration error] 0.738: ### What happened: the configuration error  [edit policy-options policy-statement 6-PRIVATE-PEER-ANYCAST-OUT term ADV-SITELOCAL from] -      prefix-list 6-BOG04-SITE-LOCAL; [edit policy-options policy
  - DAN-019 (llm) [Follow-ups and preventing route leaks] 0.701: ### Follow-ups and preventing route leaks  We are big supporters and active contributors to efforts within the <u>IETF</u> and <u>infrastructure community</u> that strengthen routing security. We know
  - DAN-019 (causa) [What happened: the configuration error] 0.381: ### What happened: the configuration error  A|1769113609.854028|2801:14:9000::6:4112:1|64112|2a03:2880:f17c::/48|64112 22850 174 3356 13335 32934|IGP|2801:14:9000::6:4112:1|0|0|22850:65151|false|||pit
  - DAN-019 (correcao) [Timeline] 0.398: ### Timeline  | Time (UTC) | Event | |---|---| | 2026-01-22 19:52 UTC | A change that ultimately triggers the routing policy bug is merged in our network automation code repository | | 2026-01-22 20:2
  - DAN-019 (correcao) [What happened: the configuration error] 0.392: ### What happened: the configuration error  On January 22, 2026, at 20:25 UTC, we pushed a change via our policy automation platform to remove the BGP announcements from Miami for one of our data cent
  - DAN-007 (llm) [Incident timeline and impact] 0.718: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.649: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-023 (llm) [sem seção] 0.608: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.535: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-038 (esperado: DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-221, DAN-154, DAN-015, DAN-066, DAN-220, DAN-010, DAN-129, DAN-148
- justificativa: 
- aprofundar DAN-086: `certificate expiration date invalid February 2012 root cause fix` — Trata de certificados com data de expiração inválida causando outage global, igual ao sintoma de expiração de certificado do incidente atual.
- aprofundar DAN-090: `certificate expired add-ons outage root cause fix` — Trata de certificado expirado parando funcionamento de clientes/add-ons, correspondendo diretamente a certificate expiration errors do incidente atual.
  - DAN-086 (llm) [The Leap Day Bug] 0.555: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.522: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.696: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.605: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q-164 (esperado: DAN-001)

- busca inicial: DAN-001, DAN-129, DAN-024, DAN-162, DAN-067, DAN-209, DAN-218, DAN-186, DAN-119, DAN-148
- justificativa: 
- aprofundar DAN-001: `cluster resource management configuration error instances start hardware available fix` — Mesmo gatilho (campanha de marketing e pico de tráfego) e mesmo sintoma: não consegue iniciar instâncias apesar de hardware disponível.
- aprofundar DAN-148: `extreme load concurrent users service outage root cause remediation` — Semelhante no gatilho de carga extrema, mas não menciona a impossibilidade de subir instâncias com recursos livres.
- aprofundar DAN-218: `network saturation scaling up issues AWS traffic gateways fix` — Relacionado a falhas ao escalar, mas causado por saturação de rede, não por gerenciamento de cluster.
  - DAN-001 (llm) [Analysis #] 0.633: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (llm) [Outage timeline #] 0.625: ## Outage timeline #  Also just before noon, traffic peaked at 200%-300% of the traffic from previous day, depending on service. At this stage, traffic was at its highest but due to excessive resource
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa
  - DAN-148 (llm) [**Account Service outage**] 0.699: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [**XMPP outage**] 0.68: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-218 (llm) [sem seção] 0.709: A little architectural background is needed here: Slack started life, not so many years ago, with everything running in one AWS account. As we’ve grown in size, complexity, and number of engineers we’
  - DAN-218 (llm) [sem seção] 0.647: Once provision-service was back in operation (around 8:15am PST) we began to see an improvement as healthy instances entered service. We still had some less-critical production issues which were mitig
  - DAN-218 (causa) [sem seção] 0.471: Unfortunately, our scale-up did not work as intended. We run a service, aptly named ‘provision-service’, which does exactly what it says on the tin. It is responsible for configuring and testing new i
  - DAN-218 (correcao) [sem seção] 0.391: AWS assures us that they are reviewing the TGW scaling algorithms for large packet-per-second increases as part of their post-incident process. We’ve also set ourselves a reminder (a Slack reminder, o
  - DAN-218 (correcao) [sem seção] 0.383: *And now we welcome the new year. Full of things that have never been.*  *— Rainer Maria Rilke*  January 4th 2021 was the first working day of the year for many around the globe, and for most of us at

## q-165 (esperado: DAN-001)

- busca inicial: DAN-001, DAN-129, DAN-218, DAN-210, DAN-148, DAN-067, DAN-208, DAN-220, DAN-209, DAN-073
- justificativa: 
- aprofundar DAN-001: `cluster resource management configuration error prevent starting instances spare hardware fix` — O incidente atual tem pico de tráfego por campanha de marketing e não consegue iniciar instâncias apesar de hardware sobrando, exatamente como o DAN-001.
  - DAN-001 (llm) [Outage timeline #] 0.633: ## Outage timeline #  The special offer was to start at noon sharp, and a direct link to its item page had been published before. At 11:15 we manually scaled out Listing service in order to be prepare
  - DAN-001 (llm) [Analysis #] 0.631: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa

## q-166 (esperado: DAN-003)

- busca inicial: DAN-003, DAN-092, DAN-103, DAN-164, DAN-134, DAN-133, DAN-180, DAN-195, DAN-102, DAN-056
- justificativa: 
- aprofundar DAN-003: `database schema field type change job distribution rollback recovery fix` — Bate com o incidente atual: deploy alterou schema do banco, o serviço de distribuição de jobs parou de distribuir e o rollback não resolveu. Os outros incidentes envolvem replicação, RabbitMQ, MongoDB ou truncate acidental, sem relação com schema de distribuição de jobs.
  - DAN-003 (llm) [What happened] 0.688: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.503: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s

## q-167 (esperado: DAN-003)

- busca inicial: DAN-003, DAN-092, DAN-134, DAN-164, DAN-130, DAN-103, DAN-180, DAN-091, DAN-116, DAN-066
- justificativa: 
- aprofundar DAN-003: `database schema field type change job distribution rollback fix` — É o único incidente que combina deploy alterando schema do banco, serviço de distribuição parando de distribuir trabalho, jobs travados e rollback não resolvendo, exatamente como o incidente atual.
  - DAN-003 (llm) [What happened] 0.693: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.51: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s

## q-168 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-066, DAN-008, DAN-050, DAN-129, DAN-067, DAN-211, DAN-020, DAN-016
- justificativa: 
- aprofundar DAN-017: `deployment staging build 401 unauthorized endpoint root cause fix` — Corresponde a um deploy que causou 401 em todos os serviços e falhas em cascata, exatamente como no incidente atual.
- aprofundar DAN-050: `deployment bug download URL generation broken fix` — Também é um deploy com bug que quebrou funcionalidade central e afetou dependentes, embora não seja erro 401.
  - DAN-017 (llm) [Analysis] 0.537: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Resolution] 0.53: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.
  - DAN-050 (llm) [Recovery] 0.71: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Summary] 0.652: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-169 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-067, DAN-211, DAN-183, DAN-016, DAN-020, DAN-129, DAN-050, DAN-066
- justificativa: 
- aprofundar DAN-017: `deployment staging build version 401 unauthorized endpoint fix rollback root cause` — Bate: deploy triggerou 401 em todos os requests com falha em cascata em produtos dependentes, igual ao atual. Não bate: plataforma específica Cloudflare vs serviço genérico.
  - DAN-017 (llm) [Analysis] 0.573: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Timeline] 0.566: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.

## q-170 (esperado: DAN-018)

- busca inicial: DAN-144, DAN-066, DAN-017, DAN-018, DAN-029, DAN-191, DAN-102, DAN-037, DAN-067, DAN-154
- justificativa: 
- aprofundar DAN-018: `React component dashboard excessive API calls dependency array root cause fix` — Bate quase exatamente: bug no painel (frontend) causa chamadas excessivas a serviço interno após deploy/configuração, derrubando API e painel em cascata. Não bate: componente específico é React/dependency array do Cloudflare, não genérico.
- aprofundar DAN-144: `thundering herd reconnecting frontend memory queues root cause fix` — Bate: enxurrada de chamadas (thundering herd) que sobrecarrega serviços internos e derruba frontend em cascata. Não bate: origem é serviço flapping e reconexão, não chamadas do painel após deploy frontend.
- aprofundar DAN-067: `thundering herd API calls overwhelmed services rate limits fix` — Bate: volume excessivo de chamadas à API sobrecarrega serviços e exige controle de taxa. Não bate: causa é falha de energia em data center e recuperação, não deploy do frontend.
  - DAN-018 (llm) [What Happened] 0.656: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.646: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-144 (llm) [Summary] 0.511: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.508: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-067 (llm) [Disaster Recovery] 0.657: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.515: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 

## q-171 (esperado: DAN-018)

- busca inicial: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-133, DAN-129, DAN-218, DAN-145, DAN-220
- justificativa: 
- aprofundar DAN-018: `React component dependency array excessive API calls tenant service fix` — Bate: dashboard gera chamadas excessivas à API após deploy frontend, derrubando API e dashboard. Não bate: causa específica é React/dependency array e serviço interno é o Tenant Service.
- aprofundar DAN-066: `Byzantine failure partial switch cascading API dashboard outage mitigation fix` — Bate: queda em cascata de API e dashboard por comportamento anômalo interno. Não bate: causa é falha bizantina de switch parcial, não deploy frontend.
- aprofundar DAN-144: `thundering herd frontend out of memory internal queue fix reconnect` — Bate: reconexão em massa saturando serviços e afetando o frontend. Não bate: origem é serviço flutuando e filas de memória, não chamadas vindas do dashboard após deploy.
  - DAN-018 (llm) [What Happened] 0.697: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.638: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-066 (llm) [The Dashboard] 0.67: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.618: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-144 (llm) [Summary] 0.557: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.523: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (causa) [Resolved] 0.45: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Connectivity Issues] 0.428: ## Connectivity Issues  ## Postmortem  At Discord, one of our primary concerns is the uptime and reliability of our service. We’ve all experienced the frustration and annoyance that comes along with t

## q-172 (esperado: DAN-020)

- busca inicial: DAN-020, DAN-220, DAN-205, DAN-066, DAN-109, DAN-145, DAN-222, DAN-067, DAN-113, DAN-144
- justificativa: 
- aprofundar DAN-020: `service discovery config client brought down globally dependent client fix` — O resumo menciona exatamente service discovery global caindo quando um cliente dependente caiu, igual ao incidente atual; os outros incidentes tratam de rede, banco, cache ou failover sem foco em service discovery.
  - DAN-020 (llm) [The failure of a core system] 0.678: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.674: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter

## q-173 (esperado: DAN-020)

- busca inicial: DAN-020, DAN-220, DAN-066, DAN-145, DAN-109, DAN-205, DAN-211, DAN-067, DAN-222, DAN-208
- justificativa: 
- aprofundar DAN-020: `service discovery global outage dependent client went down root cause fix` — Bate porque descreve service discovery caindo globalmente quando um cliente dependente caiu, igual ao incidente atual; não bate apenas na causa raiz ser uma configuração ruim do cliente.
- aprofundar DAN-211: `Consul service discovery degradation root cause fix remediation` — Bate porque envolve Consul, ferramenta de service discovery, com degradação de descoberta de serviço; não bate no gatilho, que foi remoção de bloqueio iptables, não queda de cliente dependente.
- aprofundar DAN-220: `cascading failure exponential backoff microservice root cause fix` — Bate porque descreve falha em cascata entre microsserviços; não bate no componente, pois não menciona service discovery nem cliente dependente como gatilho.
  - DAN-020 (llm) [The failure of a core system] 0.67: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [A thundering herd] 0.664: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Improve the resilience of service discovery] 0.401: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-211 (llm) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.691: ### Early Triage (10/28 13:37 – 10/29 02:00)  The initial investigation suggested that the Consul cluster that Vault and many other services depend on was unhealthy.  Specifically, the Consul cluster 
  - DAN-211 (llm) [Return to Service Attempt #1 (10/29 02:00 – 04:00)] 0.678: ### Return to Service Attempt #1 (10/29 02:00 – 04:00)  The reset went smoothly, and initially, the metrics looked good. When we removed the iptables block, the service discovery and health check load
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-220 (llm) [First symptoms: two months before the outage] 0.646: ## First symptoms: two months before the outage  Two months before the big outage we had an incident connected with one of our smallest backend services: Popcount. Popcount (this is our internal name)
  - DAN-220 (llm) [Lessons learned] 0.641: ## Lessons learned  - We should have prioritized fixing the backoff bug in the client after the first Popcount incident, we did not assign the right severity. We thought having the fast fail mechanism
  - DAN-220 (causa) [The night of April 27th] 0.485: ## The night of April 27th  It was a rainy Saturday night in Stockholm. Some of our engineers were online on IRC, and discovered that Popcount was unhealthy again. We thought the fast fail logic we in
  - DAN-220 (correcao) [Remediations in place after the second incident] 0.641: ## Remediations in place after the second incident  After the outage (infamously known as OPS-6000 in our incident tracking system), we held a post-mortem meeting where we invited the entire Technolog
  - DAN-220 (correcao) [Remediations: why are they important?] 0.568: ## Remediations: why are they important?  For every incident we hold a post-mortem meeting. The goal of this meeting is producing a list of remediations that we need to put in place in order to preven

## q-174 (esperado: DAN-022)

- busca inicial: DAN-022, DAN-065, DAN-059, DAN-113, DAN-159, DAN-129, DAN-007, DAN-006, DAN-209, DAN-068
- justificativa: 
- aprofundar DAN-022: `multicast traffic switch configuration misconfiguration global outage fix` — O resumo cita exatamente tráfego multicast sem configuração correta de switches causando pane global, igual ao incidente atual; difere no componente (replicação de índice Solr em vez de envio de tráfego geral).
  - DAN-022 (llm) [Multicast Rsync?] 0.544: ### Multicast Rsync?  If we need to get the same bits to all of the boxes, why not send the index via multicast to the replicas? It sure would be nice to only send the data once. We found an implement
  - DAN-022 (llm) [The Index Replication Issue] 0.339: ### The Index Replication Issue  To keep all of the searches on our site working fast we optimize our indexes nightly. Index optimization creates a completely new copy of the index. As we added new bo
  - DAN-022 (causa) [Search at Etsy] 0.27: ### Search at Etsy  Search at Etsy has grown significantly over the years. In January of 2009 we started using Solr for search. We used the standard primary-replica configuration for our search server
  - DAN-022 (correcao) [Improvements] 0.279: ### Improvements  To better deal with the transfer lag we are looking at creating a Torrent file per index segment. Lucene indexes are made up of various segments. Each commit creates an index segment
  - DAN-022 (correcao) [How it Works] 0.273: ### How it Works  HTTP replication doesn’t allow for the transfer of older versions of a given index. This causes issues with some of our static indexes. When we bring up new replicas, Solr creates a 

## q-175 (esperado: DAN-022)

- busca inicial: DAN-022, DAN-159, DAN-077, DAN-113, DAN-059, DAN-209, DAN-078, DAN-109, DAN-148, DAN-006
- justificativa: 
- aprofundar DAN-022: `multicast traffic switch configuration root cause fix` — O incidente envolve tráfego multicast causando queda global de rede, exatamente como o atual. Difere por ser replicação de índice do Solr, mas o gatilho (multicast) e o impacto (site offline mundial) são iguais.
  - DAN-022 (llm) [Multicast Rsync?] 0.561: ### Multicast Rsync?  If we need to get the same bits to all of the boxes, why not send the index via multicast to the replicas? It sure would be nice to only send the data once. We found an implement
  - DAN-022 (llm) [The Index Replication Issue] 0.361: ### The Index Replication Issue  To keep all of the searches on our site working fast we optimize our indexes nightly. Index optimization creates a completely new copy of the index. As we added new bo
  - DAN-022 (causa) [Search at Etsy] 0.27: ### Search at Etsy  Search at Etsy has grown significantly over the years. In January of 2009 we started using Solr for search. We used the standard primary-replica configuration for our search server
  - DAN-022 (correcao) [Improvements] 0.279: ### Improvements  To better deal with the transfer lag we are looking at creating a Torrent file per index segment. Lucene indexes are made up of various segments. Each commit creates an index segment
  - DAN-022 (correcao) [How it Works] 0.273: ### How it Works  HTTP replication doesn’t allow for the transfer of older versions of a given index. This causes issues with some of our static indexes. When we bring up new replicas, Solr creates a 

## q-176 (esperado: DAN-026)

- busca inicial: DAN-026, DAN-020, DAN-010, DAN-162, DAN-087, DAN-137, DAN-049, DAN-075, DAN-002, DAN-065
- justificativa: 
- aprofundar DAN-026: `IP change nameserver restart zone file corrupt NXDOMAIN fix` — Corresponde fortemente: troca de IP, timeouts de consulta e NXDOMAIN após deploy que reconstrói zona a partir de API dependente de DNS; não menciona Puppet no incidente atual.
- aprofundar DAN-002: `DNS resolver fleet config change healthy host query failure remediation` — É sobre falha de resolução DNS após mudança de configuração, mas não cita troca de IP nem respostas NXDOMAIN.
- aprofundar DAN-162: `database migration broke DNS resolution cascading recovery temporary resolvers` — Envolve quebra de resolução DNS e recuperação em cascata, mas não menciona troca de IP nem NXDOMAIN.
  - DAN-026 (llm) [What happened…] 0.74: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.634: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.626: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We’d like to give you some additional information about the service disruption that occurred in 
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.604: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We are taking multiple steps to prevent recurrence of this issue, some of which are already comp
  - DAN-162 (llm) [sem seção] 0.534: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5

## q-177 (esperado: DAN-026)

- busca inicial: DAN-026, DAN-020, DAN-087, DAN-162, DAN-075, DAN-010, DAN-049, DAN-137, DAN-081, DAN-002
- justificativa: 
- aprofundar DAN-026: `DNS timeout NXDOMAIN after IP change zone file corrupt` — Mesmo gatilho (mudança de IP), mesmo sintoma (timeouts e NXDOMAIN) e mesmo componente (servidores DNS autoritativo/cache), diferindo pelo envolvimento de Puppet e exaustão de memória.
- aprofundar DAN-002: `DNS resolver fleet config change in-VPC queries failed` — Falha de DNS interno após mudança de configuração, mas sem mudança de IP nem NXDOMAIN explícitos no resumo.
- aprofundar DAN-049: `DNS resolution failure deployment root cause fix` — Falha de resolução DNS durante implantação com recriação de registros, embora sem mudança de IP nem NXDOMAIN.
  - DAN-026 (llm) [What happened…] 0.747: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.684: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.619: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We’d like to give you some additional information about the service disruption that occurred in 
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.597: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We are taking multiple steps to prevent recurrence of this issue, some of which are already comp
  - DAN-049 (llm) [Resolution] 0.679: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [Root Cause of the Outage] 0.642: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (causa) [Postmortem] 0.443: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat

## q-178 (esperado: DAN-033)

- busca inicial: DAN-033, DAN-191, DAN-221, DAN-205, DAN-195, DAN-222, DAN-165, DAN-161, DAN-231, DAN-106
- justificativa: 
- aprofundar DAN-033: `quota service bad config failure fix root cause` — O resumo cita exatamente falha de serviço de cotas por configuração ruim derrubando múltiplos serviços incluindo Gmail, espelhando o incidente atual, mas não detalha componente nem gatilho além disso.
  - DAN-033 (llm) [sem seção] 0.473: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fre
  - DAN-033 (llm) [sem seção] 0.416: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  .cc
  - DAN-033 (causa) [sem seção] 0.294: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Dec
  - DAN-033 (correcao) [sem seção] 0.262: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  enu
  - DAN-033 (correcao) [sem seção] 0.248: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fie

## q-179 (esperado: DAN-033)

- busca inicial: DAN-033, DAN-191, DAN-218, DAN-147, DAN-144, DAN-220, DAN-148, DAN-205, DAN-221, DAN-109
- justificativa: 
- aprofundar DAN-033: `quota service failure bad config root cause fix multiple services gmail` — O resumo menciona exatamente uma falha no serviço de quota que derruba múltiplos serviços incluindo Gmail, igual ao incidente atual (quota service + email down).
  - DAN-033 (llm) [sem seção] 0.5: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fre
  - DAN-033 (llm) [sem seção] 0.447: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  - B
  - DAN-033 (causa) [sem seção] 0.294: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  .cc
  - DAN-033 (correcao) [sem seção] 0.262: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  enu
  - DAN-033 (correcao) [sem seção] 0.248: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fie

## q-180 (esperado: DAN-042)

- busca inicial: DAN-042, DAN-035, DAN-049, DAN-032, DAN-015, DAN-020, DAN-033, DAN-048, DAN-029, DAN-017
- justificativa: 
- aprofundar DAN-042: `deployment config variables missing code requires root cause fix` — Bate por envolver deploy e código que exige variáveis de configuração ausentes; não especifica se a variável estava faltando nas instâncias ou apenas não sendo lida.
- aprofundar DAN-015: `deployed credentials wrong environment old credentials removed fix` — Bate por tratar de deploy com credenciais/variáveis de ambiente ausentes no environment correto; difere por ser sobre credenciais de storage, não variável genérica de app.
- aprofundar DAN-035: `configuration rollout replica cannot read config files fix` — Bate por envolver nova configuração não disponível nas instâncias após rollout; difere por ser infraestrutura de load balancer, não variável de aplicação.
  - DAN-042 (llm) [It was such a nice morning] 0.611: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Did I mess up?] 0.603: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-015 (llm) [Incident timeline] 0.663: ## Incident timeline  **All timestamps referenced are in Coordinated Universal Time (UTC).**  | Time | Event | |---|---| | Mar 21, 2025 - 19:49 UTC | The R2 engineering team started the credential rot
  - DAN-015 (llm) [Incident timeline] 0.613: ## Incident timeline  Given gradual decline in availability metrics, R2 engineering team suspected a potential regression in propagation of new credentials in storage infrastructure. | | Mar 21, 2025 
  - DAN-015 (causa) [Next steps] 0.493: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [Next steps] 0.468: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.604: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.56: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.405: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo

## q-181 (esperado: DAN-042)

- busca inicial: DAN-042, DAN-035, DAN-220, DAN-020, DAN-049, DAN-029, DAN-154, DAN-050, DAN-102, DAN-055
- justificativa: 
- aprofundar DAN-042: `missing config variable deployment code required fix rollback` — O novo código exige variáveis de configuração que o deploy não disponibilizou, exatamente como o incidente atual; difere por ser no Heroku e envolver git push.
- aprofundar DAN-055: `configuration change builds fail rollback fix root cause` — Uma mudança de configuração quebrou builds, parecido com variável ausente após deploy; difere por envolver CI builds e rollback manual que falhou.
- aprofundar DAN-029: `bad config database cluster outage root cause fix` — Mau config causou indisponibilidade, relacionado a config ausente/errada; difere por envolver cluster de banco de dados e falhas incomuns combinadas.
  - DAN-042 (llm) [Did I mess up?] 0.628: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (llm) [It was such a nice morning] 0.626: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-055 (llm) [So what happened?] 0.611: ## So what happened?  Thursday Feb 2nd, we started rolling out a new worker version (v2.6.2) on EC2, for sudo: false, container-based builds.  Friday Feb 3rd, we identified an issue with jobs being in
  - DAN-055 (llm) [So what happened?] 0.558: ## So what happened?  We also learned we did not have alerting which included the errors logged when the image pulls were failing to find v2.5.0.  Sunday, Feb 5th, in order to more quickly eliminate t
  - DAN-055 (causa) [Contributing Factors] 0.437: ## Contributing Factors  The major contributing factors in this outage were  - A change in how our worker's docker backend executes build scripts, so that bash is run explicitly with a login shell. Th
  - DAN-055 (correcao) [Going forward?] 0.437: ## Going forward?  - As part of the incident resolution, we created additional alerting, so that we know we'll be notified about similar errors in the future.  - We are discussing both incremental and
  - DAN-055 (correcao) [Summary] 0.424: ## Summary  We couldn't be more sorry about this incident and the impact that the build outages and delays had on you, our users and customers. We always use problems like these as an opportunity for 
  - DAN-029 (llm) [The following weeks] 0.711: ## The following weeks  The day after the incident, the whole team sat down to discuss two issues:  - Why did our Pacemaker cluster fail to elect a new primary database node? - How do we move back to 
  - DAN-029 (llm) [Incident timeline] 0.695: ## Incident timeline  So, how did all this go wrong?  All times in this section are in British Summer Time (UTC+1).  - 15:09: Our monitoring detects the total outage of our API and Dashboard; engineer
  - DAN-029 (causa) [Reproducing the failure] 0.515: ### Reproducing the failure  To be confident in a new cluster, we needed to understand why the existing one didn't promote a new primary, and make changes to fix that issue.  For the most part, we did
  - DAN-029 (correcao) [Wrapping up the incident] 0.496: ## Wrapping up the incident  With a plan in place, and the confidence that we'd understood and fixed the issue which stopped our cluster from failing over on 10 October, we were ready to go. Even with
  - DAN-029 (correcao) [What's next?] 0.486: ## What's next?  There's no getting away from the size of this incident.  We feel an immense duty to everyone who trusts GoCardless as their payments provider. We took some time to think through what 

## q-182 (esperado: DAN-043)

- busca inicial: DAN-043, DAN-146, DAN-056, DAN-164, DAN-048, DAN-210, DAN-186, DAN-058, DAN-066, DAN-209
- justificativa: 
- aprofundar DAN-043: `accidental deletion production database backup recovery fix` — Bate exatamente: apagamento acidental do banco de produção com perda de dados entre backups; não diz se backup era por hora.
- aprofundar DAN-056: `accidental environment variable truncate production database fix recovery` — Bate por ação acidental que truncou/deletou banco de produção; não envolve restauração de backup explicitamente.
- aprofundar DAN-164: `deleted wrong directory database replication lag data loss fix` — Bate por exclusão acidental e perda de horas de dados; gatilho foi sobrecarga e replicação, não apenas apagamento direto.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.73: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.671: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [What We Learned] 0.74: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.712: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a
  - DAN-164 (llm) [Root cause analysis] 0.713: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.702: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-183 (esperado: DAN-043)

- busca inicial: DAN-043, DAN-164, DAN-056, DAN-186, DAN-146, DAN-091, DAN-058, DAN-066, DAN-048, DAN-210
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup recovery root cause fix` — Bate por deletar banco de produção por acidente com backup antigo; não bate por ser banco gerenciado da DigitalOcean com backup diário.
- aprofundar DAN-164: `admin deleted wrong directory database replication lag data loss fix` — Bate por exclusão acidental de dados do banco com horas de perda; não bate por ser erro de administrador em diretório com replicação atrasada.
- aprofundar DAN-056: `environment variable tests truncate production database accident fix recovery` — Bate por dano acidental ao banco de produção via variável de ambiente; não bate por ser truncate em testes, não exclusão direta.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.73: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [What happened?] 0.663: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [sem seção] 0.395: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-164 (llm) [Root cause analysis] 0.706: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.666: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.746: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.703: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-184 (esperado: DAN-048)

- busca inicial: DAN-048, DAN-066, DAN-078, DAN-195, DAN-209, DAN-164, DAN-234, DAN-043, DAN-190, DAN-146
- justificativa: 
- aprofundar DAN-048: `RDS hardware failure MySQL failover data loss configuration fix` — Bate com falha de hardware, failover do MySQL e perda de dados em sistema financeiro; não bate se o gatilho é configuração incorreta além do hardware.
- aprofundar DAN-078: `MySQL master failover writes not propagated latency fix restoration` — Bate com failover do MySQL e writes recentes faltando após o failover; não bate porque o gatilho é partição de rede, não falha de hardware.
  - DAN-048 (llm) [Incorrect configuration variable] 0.787: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Final thoughts] 0.761: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.662: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [2018 October 22 11:12 UTC] 0.635: ## 2018 October 22 11:12 UTC  All database primaries established in US East Coast again. This resulted in the site becoming far more responsive as writes were now directed to a database server that wa
  - DAN-078 (causa) [Incident timeline] 0.478: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa

## q-185 (esperado: DAN-048)

- busca inicial: DAN-048, DAN-066, DAN-078, DAN-164, DAN-043, DAN-181, DAN-094, DAN-093, DAN-096, DAN-190
- justificativa: 
- aprofundar DAN-048: `RDS hardware failure MySQL configuration data loss failover fix` — Bate: falha de hardware em banco gerenciado (RDS), failover, perda de dados em sistema financeiro. Não bate: causa raiz aponta configuração incorreta do MySQL, não apenas o failover.
- aprofundar DAN-078: `MySQL master failover missing writes latency restore data integrity` — Bate: failover do MySQL master após incidente de rede, escritas recentes não propagadas ao novo mestre. Não bate: gatilho é partição de rede em manutenção, não falha de hardware.
- aprofundar DAN-093: `MySQL failover cold buffer pool data drift primary fix` — Bate: failover do MySQL levou a nó desatualizado com perda/desvio de dados recentes. Não bate: origem é migração de schema e Pacemaker, não falha de hardware.
  - DAN-048 (llm) [Incorrect configuration variable] 0.792: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Final thoughts] 0.763: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.675: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [Next steps] 0.657: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (causa) [Incident timeline] 0.478: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [2018 October 22 16:24 UTC] 0.479: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-093 (llm) [Monday, September 10th] 0.688: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [In ops I trust] 0.62: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [Tuesday, September 11th] 0.368: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s

## q-186 (esperado: DAN-049)

- busca inicial: DAN-049, DAN-073, DAN-026, DAN-109, DAN-162, DAN-050, DAN-208, DAN-024, DAN-129, DAN-164
- justificativa: 
- aprofundar DAN-049: `static.crates.io DNS record re-created deployment outage fix` — Bate com deploy de infraestrutura, domínio static parando de resolver e downloads falhando; não detalha se certificado foi causa raiz.
- aprofundar DAN-026: `Puppet manifest nameserver restart IP change corrupt zone fix` — Bate com falha DNS durante deploy; não bate especificamente em domínio de arquivos estáticos.
- aprofundar DAN-050: `download URL generation bug deployment fix crates.io` — Bate com downloads quebrando durante deploy; não bate em falha de resolução DNS do domínio estático.
  - DAN-049 (llm) [Resolution] 0.807: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [sem seção] 0.755: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat
  - DAN-049 (causa) [Postmortem] 0.443: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [Root Cause of the Outage] 0.373: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-026 (llm) [What happened…] 0.689: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (llm) [What happened…] 0.604: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-050 (llm) [2023-07-20] 0.774: ### 2023-07-20  - 12:24 UTC – https://github.com/rust-lang/crates.io/issues/6850 (Crates.io crate download API is redirecting to invalid URL) was opened - 12:25 UTC – The continuing request-per-second
  - DAN-050 (llm) [Fault] 0.769: ## Fault  The pull request introduced a few tests for the previously untested functionality, though unfortunately it was using values different from the environment variable content that is used by cr
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Recovery] 0.488: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 

## q-187 (esperado: DAN-049)

- busca inicial: DAN-049, DAN-026, DAN-020, DAN-162, DAN-050, DAN-210, DAN-073, DAN-010, DAN-129, DAN-208
- justificativa: 
- aprofundar DAN-049: `static domain DNS resolution deployment infrastructure certificates DNS records` — Bate com deploy de infraestrutura e domínio estático (static.crates.io) parando de resolver; não confirma se causa foi re-criação de certificados e registros DNS.
- aprofundar DAN-026: `DNS outage authoritative nameserver zone file corrupt fix` — Bate com outage de DNS durante operação; não bate pois envolve nameserver autoritativo e zone file corrupto, não deploy direto de domínio estático.
- aprofundar DAN-050: `download URL generation deployment bug fix downloads` — Bate com downloads falhando após deploy; não bate pois causa é bug na geração de URL, não resolução DNS do domínio estático.
  - DAN-049 (llm) [Resolution] 0.65: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [Root Cause of the Outage] 0.641: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (causa) [Postmortem] 0.443: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat
  - DAN-026 (llm) [What happened…] 0.743: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [Total number of processes across fileservers] 0.707: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (causa) [What we’re doing about it…] 0.461: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [Summary] 0.443: # Summary  We realize that GitHub is an important part of your development and workflow. Again, I would like to take a moment to apologize for the impact that this outage had to your operations. We ta
  - DAN-050 (llm) [Recovery] 0.653: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [2023-07-20] 0.628: ### 2023-07-20  - 12:24 UTC – https://github.com/rust-lang/crates.io/issues/6850 (Crates.io crate download API is redirecting to invalid URL) was opened - 12:25 UTC – The continuing request-per-second
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-188 (esperado: DAN-050)

- busca inicial: DAN-050, DAN-106, DAN-116, DAN-035, DAN-220, DAN-148, DAN-129, DAN-191, DAN-017, DAN-003
- justificativa: 
- aprofundar DAN-050: `deployment bug download URL generation fix rollback` — Bate porque falha em downloads de pacotes logo após um deploy, com clientes (cargo) tentando de novo sem parar; não bate porque é crates.io/Rust, não o mesmo ecossistema.
- aprofundar DAN-017: `deployment tool bug staging production endpoint fix rollback` — Bate porque é uma falha em larga escala causada por um deploy com erro de referência de versão; não bate porque não envolve downloads de pacotes.
- aprofundar DAN-003: `deploy database schema change rollback fix service` — Bate porque um deploy alterou o esquema e quebrou o serviço, exigindo rollback; não bate porque não são downloads de pacotes.
  - DAN-050 (llm) [Recovery] 0.733: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Response] 0.686: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-017 (llm) [Timeline] 0.604: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (llm) [Analysis] 0.592: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.
  - DAN-003 (llm) [What happened] 0.583: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.503: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s

## q-189 (esperado: DAN-050)

- busca inicial: DAN-050, DAN-220, DAN-116, DAN-106, DAN-035, DAN-183, DAN-113, DAN-003, DAN-129, DAN-001
- justificativa: 
- aprofundar DAN-050: `deployment download URL generation bug crate download fix rollback` — Um deploy introduziu bug na geração da URL de download e quebrou todos os downloads de crates, com retry do cargo, exatamente como o incidente atual (pós-deploy, downloads de pacote falhando e erro rate explodindo).
  - DAN-050 (llm) [Recovery] 0.79: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [2023-07-20] 0.771: ### 2023-07-20  - 12:24 UTC – https://github.com/rust-lang/crates.io/issues/6850 (Crates.io crate download API is redirecting to invalid URL) was opened - 12:25 UTC – The continuing request-per-second
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-190 (esperado: DAN-058)

- busca inicial: DAN-175, DAN-058, DAN-204, DAN-131, DAN-048, DAN-164, DAN-231, DAN-056, DAN-203, DAN-043
- justificativa: 
- aprofundar DAN-058: `free tier database backup identifier data leak fix` — Bate porque envolve bancos de dados do plano gratuito vazando dados de outros clientes; não bate se a causa for identificadores de backup e não consulta direta dos clientes.
- aprofundar DAN-204: `Redis cache corrupted cross user data exposure fix` — Bate porque envolve usuários vendo dados de outros usuários; não bate porque é cache Redis, não bancos de dados próprios dos clientes do plano gratuito.
- aprofundar DAN-175: `private token leaked customer data retrieval fix` — Bate porque envolve vazamento de dados de clientes; não bate porque é via tokens roubados por atacante, não clientes vendo dados alheios nos próprios bancos.
  - DAN-058 (llm) [What happened?] 0.776: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.759: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-204 (llm) [Technical details] 0.631: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.628: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-175 (llm) [Incident Summary] 0.581: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.539: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-191 (esperado: DAN-058)

- busca inicial: DAN-058, DAN-175, DAN-164, DAN-204, DAN-231, DAN-141, DAN-006, DAN-048, DAN-056, DAN-043
- justificativa: 
- aprofundar DAN-058: `free tier database data leak backup identifier fix` — Bate: free tier + banco de dados + vazamento de dados, igual ao incidente atual. Não bate: causa parece ser identificador de backup, não confirmado ainda.
- aprofundar DAN-204: `Redis cache corruption user data leak fix` — Bate: usuários veem dados de outros usuários. Não bate: não é específico de free tier e componente é cache Redis, não banco de dados próprio.
- aprofundar DAN-175: `private token leak data access fix` — Bate: vazamento permitiu acesso a dados alheios. Não bate: mecanismo é token exposto, não isolamento de banco de dados de free tier.
  - DAN-058 (llm) [What happened?] 0.781: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.76: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-204 (llm) [Technical details] 0.653: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.636: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-175 (llm) [Incident Summary] 0.568: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.549: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-192 (esperado: DAN-059)

- busca inicial: DAN-007, DAN-059, DAN-159, DAN-022, DAN-006, DAN-154, DAN-106, DAN-209, DAN-113, DAN-005
- justificativa: 
- aprofundar DAN-059: `bad BGP config transit providers Level 3 Telia Zayo outage fix` — Configuração ruim de BGP cortou múltiplos provedores de trânsito (Level 3, Telia, Zayo) e derrubou o Steam globalmente, correspondendo exatamente ao gatilho e impacto do incidente atual.
- aprofundar DAN-007: `incorrect ordering disabled BGP advertised prefixes communities datacenters malfunction fix` — Mudança na configuração BGP (padronização de comunidades) afetou anúncio de prefixos em múltiplos datacenters, semelhante à mudança de BGP atual, embora o mecanismo seja ordenação de prefixos desabilitados.
- aprofundar DAN-005: `bad config router rule edge routers crash global outage fix` — Regra de roteador com configuração ruim derrubou todos os roteadores de borda globalmente após mudança, semelhança no impacto global, mas não envolve explicitamente provedores de trânsito BGP.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.548: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [Troubles in the Data Center] 0.427: ### Troubles in the Data Center  So we have a situation with high levels of packet loss from many locations around the world. Let’s take a look at a Path Visualization to see where the network instabi
  - DAN-059 (causa) [sem seção] 0.384: Data centers are the factories of the Internet, churning out computation and services that customers demand. Apple is currently converting a 1.3M sq ft factory into a data center. And like factories, 
  - DAN-059 (correcao) [A (Nearly) Global Outage] 0.255: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-059 (correcao) [Steam Outage on May 7th] 0.254: ### Steam Outage on May 7th  Starting at 11:45 Pacific on May 7th and lasting for 2 hours, the popular online gaming service Steam suffered a widespread outage. Steam regularly has more than 8 million
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.738: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.671: ### Technical description of the error and how it happened  ``` [edit policy-options policy-statement 4-COGENT-TRANSIT-OUT term ADV-SITELOCAL then] +      community add STATIC-ROUTE; +      community 
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-005 (llm) [Bad Rule] 0.691: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.67: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp

## q-193 (esperado: DAN-059)

- busca inicial: DAN-007, DAN-059, DAN-006, DAN-023, DAN-154, DAN-022, DAN-159, DAN-205, DAN-209, DAN-019
- justificativa: 
- aprofundar DAN-059: `bad BGP config transit providers Level 3 Telia Zayo outage root cause fix` — Bate: perda simultânea de vários provedores de trânsito (Level 3, Telia, Zayo), queda global e mudança de configuração BGP — corresponde quase exatamente ao incidente atual. Não bate: não há postmortem oficial da Valve, apenas indícios.
- aprofundar DAN-007: `BGP communities prefixes ordering datacenter malfunction root cause fix` — Bate: mudança de configuração BGP (comunidades e prefixos anunciados) causou mal funcionamento em vários datacenters. Não bate: foco em ordem de prefixos desabilitados, não em perda simultânea de provedores de trânsito externos.
- aprofundar DAN-023: `backbone router configuration change global outage root cause fix` — Bate: mudanças de configuração em roteadores de backbone causaram queda global de todos os serviços. Não bate: componente são roteadores internos de backbone, não provedores de trânsito externos.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.563: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [Troubles in the Data Center] 0.427: ### Troubles in the Data Center  So we have a situation with high levels of packet loss from many locations around the world. Let’s take a look at a Path Visualization to see where the network instabi
  - DAN-059 (causa) [sem seção] 0.384: Data centers are the factories of the Internet, churning out computation and services that customers demand. Apple is currently converting a 1.3M sq ft factory into a data center. And like factories, 
  - DAN-059 (correcao) [A (Nearly) Global Outage] 0.255: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-059 (correcao) [Steam Outage on May 7th] 0.254: ### Steam Outage on May 7th  Starting at 11:45 Pacific on May 7th and lasting for 2 hours, the popular online gaming service Steam suffered a widespread outage. Steam regularly has more than 8 million
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.725: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (llm) [Incident timeline and impact] 0.665: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-023 (llm) [sem seção] 0.637: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.618: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-194 (esperado: DAN-060)

- busca inicial: DAN-068, DAN-067, DAN-060, DAN-063, DAN-062, DAN-064, DAN-191, DAN-106, DAN-071, DAN-209
- justificativa: 
- aprofundar DAN-060: `transformer failure generator PLC phase backup generators EC2 EBS RDS` — Falha de transformador impediu geradores de backup via PLC e afetou EC2, EBS e RDS, igual ao cenário de energia e geradores não entrando com instâncias/volumes/bancos fora.
- aprofundar DAN-063: `generator breaker mechanical failure overload manual generators power control` — Perda de utilidade em AZ com disjuntor do gerador aberto e falha mecânica de outro gerador, sobrecarga dos restantes; igual a geradores de reserva não entrando e zona fora.
- aprofundar DAN-068: `breaker coordination settings power loss redundant power paths` — Configuração incorreta de disjuntores causou perda total de energia ignorando caminhos redundantes; semelhança em falha de energia no datacenter com redundância comprometida, diferença é não focar em geradores.
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.754: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  Normally, when utility power fails, electrical load is seamlessly picked up by backup generators. Program
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.702: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  By Sunday morning, August 7th, we had completed the work to fully understand root cause, prevent the prob
  - DAN-060 (causa) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.442: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  In one of the days leading up to the Friday, August 5th deletion run, there was a hardware failure that t
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.417: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  We learned a number of lessons from this event that we will use to continually improve the reliability of
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.39: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  There are several places we can improve on the communication front. First, we can accelerate the pace wit
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.58: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.449: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-068 (llm) [What happened to the power in the data center?] 0.664: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.576: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is

## q-195 (esperado: DAN-060)

- busca inicial: DAN-060, DAN-068, DAN-067, DAN-062, DAN-061, DAN-063, DAN-064, DAN-071, DAN-078, DAN-070
- justificativa: 
- aprofundar DAN-060: `transformer failure PLC generator phase backup generators online EC2 EBS RDS fix` — Bate perfeitamente: perda de energia, geradores de backup não ligaram por falha no PLC de fase, afetou instâncias, volumes e bancos (EC2/EBS/RDS).
- aprofundar DAN-063: `utility power lost breaker generator mechanical failure overload automated control fix` — Semelhança forte: perda de utilidade, disjuntor abriu na frente de um gerador, segundo gerador falhou mecanicamente e sobrecarregou os restantes.
- aprofundar DAN-061: `backup generator failed stable power switch over weather load test fix` — Semelhança moderada: falha de energia por mau tempo, gerador de backup não entregou potência estável na troca, apesar de testes anteriores.
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.755: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  Normally, when utility power fails, electrical load is seamlessly picked up by backup generators. Program
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.723: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  At 11:54 AM PDT, we had been able to bring some of the backup generators online by manually phase-synchro
  - DAN-060 (causa) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.442: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  In one of the days leading up to the Friday, August 5th deletion run, there was a hardware failure that t
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.426: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  By Sunday morning, August 7th, we had completed the work to fully understand root cause, prevent the prob
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.417: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  We learned a number of lessons from this event that we will use to continually improve the reliability of
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.639: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.507: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-061 (llm) [Summary of the AWS Service Event in the US East Region] 0.634: ### Summary of the AWS Service Event in the US East Region  The generators and electrical switching equipment in the datacenter that experienced the failure were all the same brand and all installed i
  - DAN-061 (llm) [Summary of the AWS Service Event in the US East Region] 0.612: ### Summary of the AWS Service Event in the US East Region  In the single datacenter that did not successfully transfer to the generator backup, all servers continued to operate normally on Uninterrup
  - DAN-061 (causa) [Summary of the AWS Service Event in the US East Region] 0.419: ### Summary of the AWS Service Event in the US East Region  When servers lost power in the impacted datacenter, many Single-AZ RDS instances in that Availability Zone became unavailable. There was no 
  - DAN-061 (correcao) [Summary of the AWS Service Event in the US East Region] 0.436: ### Summary of the AWS Service Event in the US East Region  We apologize for the inconvenience and trouble this caused for affected customers. We know how critical our services are to our customers’ b
  - DAN-061 (correcao) [Summary of the AWS Service Event in the US East Region] 0.31: ### Summary of the AWS Service Event in the US East Region  While direct impact was limited to those ELBs which had failed in the power-affected datacenter and hadn’t yet had their traffic shifted, th

## q-196 (esperado: DAN-065)

- busca inicial: DAN-065, DAN-006, DAN-113, DAN-022, DAN-005, DAN-231, DAN-106, DAN-059, DAN-159, DAN-007
- justificativa: 
- aprofundar DAN-065: `IMP corrupted routing data recomputed checksums buffers nodes offline fix` — Nós saem da rede em cascata, buffers enchem e dados de roteamento corrompidos com checksums válidos batem exatamente; difere apenas na época/tecnologia.
- aprofundar DAN-005: `router rule bad config edge routers crash outage fix` — Roteadores de borda caírem e derrubarem rede bate com nós saindo do ar; não menciona buffers nem checksums de roteamento.
- aprofundar DAN-113: `latent defect OS failover protocol devices fail disable fix` — Dispositivos de rede falharem por defeito latente bate com nós saindo do ar; não cita buffers ou dados de roteamento com checksum válido.
  - DAN-065 (llm) [sem seção] 0.683: our own building (after taking dumps, of course).  This procedure initializes  all  of  the IMPs' dynamic data structures, and will                               - 2 - RFC 789                         
  - DAN-065 (llm) [sem seção] 0.658: require  either  a  large  number  of  CPU  cycles  (for frequent checksumming of a large area of memory)  or  a  large  amount  of memory  (to store the checksums for a lot of small areas).  Since CP
  - DAN-065 (causa) [sem seção] 0.485: ```                                                           RFC 789     Vulnerabilities of Network Control Protocols: An Example                           Eric C. Rosen                   Bolt Berane
  - DAN-065 (correcao) [sem seção] 0.395: loader/dumper.  In the case under discussion, we would have liked to  have  all  the  IMPs  go  into  their loader/dumpers when the problem arose.  This would have enabled us to  re-initialize  and re
  - DAN-065 (correcao) [sem seção] 0.389: possible  for so  many updates from one IMP to be extant simultaneously, we did understand enough to be able to get the network to recover.   All that was necessary was to patch the IMPs to disregard 
  - DAN-005 (llm) [Bad Rule] 0.723: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.661: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp
  - DAN-113 (llm) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.567: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  While disabling the new protocol resolved the event, engineering teams have continued working to identify the underlying r
  - DAN-113 (llm) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.541: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  While the removal of additional devices provided temporary remediation, several other network devices subsequently began t
  - DAN-113 (causa) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.371: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  On September 2, 2021 at 7:30 AM JST, internal alarms alerted AWS engineers to elevated packet loss for Direct Connect cust
  - DAN-113 (correcao) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.378: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  This procedure upgrades individual devices in specific places where the upgraded devices can be exposed to production traf
  - DAN-113 (correcao) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.242: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  We would like to provide additional information about the AWS Direct Connect service disruption that occurred in the Tokyo

## q-197 (esperado: DAN-065)

- busca inicial: DAN-065, DAN-113, DAN-109, DAN-005, DAN-006, DAN-238, DAN-022, DAN-026, DAN-106, DAN-218
- justificativa: 
- aprofundar DAN-065: `corrupted routing data valid checksums buffer fill nodes drop offline fix` — O incidente atual descreve nós caindo em sequência, buffers cheios, dados de roteamento estranhos e checksums válidos — exatamente o padrão do DAN-065, onde um IMP com defeito corrompia dados de roteamento, o software recomputava checksums sobre dados ruins, buffers enchiam e nós se desconectavam. Diferença: é um caso de 1980 (ARPANET), não moderno.
  - DAN-065 (llm) [sem seção] 0.606: because  of  the  failure  of some line, each has the most recent update  from   the   other   by   the   time   communication   is re-established.      This  very  short  introduction  to  the routin
  - DAN-065 (llm) [sem seção] 0.605: require  either  a  large  number  of  CPU  cycles  (for frequent checksumming of a large area of memory)  or  a  large  amount  of memory  (to store the checksums for a lot of small areas).  Since CP
  - DAN-065 (causa) [sem seção] 0.485: ```                                                           RFC 789     Vulnerabilities of Network Control Protocols: An Example                           Eric C. Rosen                   Bolt Berane
  - DAN-065 (correcao) [sem seção] 0.395: loader/dumper.  In the case under discussion, we would have liked to  have  all  the  IMPs  go  into  their loader/dumpers when the problem arose.  This would have enabled us to  re-initialize  and re
  - DAN-065 (correcao) [sem seção] 0.389: possible  for so  many updates from one IMP to be extant simultaneously, we did understand enough to be able to get the network to recover.   All that was necessary was to patch the IMPs to disregard 

## q-198 (esperado: DAN-069)

- busca inicial: DAN-069, DAN-191, DAN-068, DAN-063, DAN-205, DAN-064, DAN-067, DAN-209, DAN-060, DAN-102
- justificativa: 
- aprofundar DAN-069: `alarm bug monitoring system transmission line foliage cascading failure fix` — O incidente DAN-069 é o único que envolve linhas de transmissão elétrica caindo em cascata com alarme não disparado na sala de controle, exatamente como no atual; difere por ser um sistema de monitoramento GE de rede elétrica, não um data center.
  - DAN-069 (llm) [Cascade] 0.6: ## Cascade  ## Timeline  The following is the blackout's sequence of events on August 14, 2003 (times in EDT):  - 12:15 p.m. Incorrect telemetry data renders the state estimator, a power flow monitori
  - DAN-069 (llm) [Computer failure] 0.583: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (causa) [Findings] 0.529: ## Findings  In April 2004, the U.S.-Canada Power System Outage Task Force released their final report, placing the causes of the blackout into four groups:  - FirstEnergy (FE) and its reliability cou
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 

## q-199 (esperado: DAN-069)

- busca inicial: DAN-069, DAN-068, DAN-191, DAN-067, DAN-060, DAN-063, DAN-205, DAN-064, DAN-240, DAN-184
- justificativa: 
- aprofundar DAN-069: `alarm system bug transmission line trip cascade root cause fix` — Linhas de transmissão desarmando em cascata sem alarme devido a bug, igual ao incidente atual.
- aprofundar DAN-067: `ground fault high voltage line protective relay shutdown generator fix` — Linhas de alta tensão e medidas de proteção que desligam geradores, mas sem menção clara à falha de alarme na sala de controle.
- aprofundar DAN-063: `breaker trip automated power control malfunction generator overload fix` — Disjuntor abriu e sistema de controle automático falhou, mas envolve geradores e utilidade, não linhas de transmissão.
  - DAN-069 (llm) [Computer failure] 0.614: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (llm) [Outages in the Cleveland-Akron area] 0.571: ## Outages in the Cleveland-Akron area  FE's situational awareness was reduced by the development of faults in its General Electric Harris XA21 energy management system (EMS) from 2:14 p.m. to 2:54 p.
  - DAN-069 (causa) [Findings] 0.529: ## Findings  In April 2004, the U.S.-Canada Power System Outage Task Force released their final report, placing the causes of the blackout into four groups:  - FirstEnergy (FE) and its reliability cou
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.631: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.552: ### Informed Speculation On What Happened Next  From this decision onward, we don't yet have clarity from Flexential on the root cause or some of the decisions they made or the events. We will update 
  - DAN-067 (causa) [Lessons and Remediation] 0.574: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.614: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.497: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i

## q-200 (esperado: DAN-073)

- busca inicial: DAN-073, DAN-164, DAN-129, DAN-209, DAN-048, DAN-109, DAN-026, DAN-186, DAN-066, DAN-226
- justificativa: 
- aprofundar DAN-073: `storage volume failure root cause fix recovery outage` — Falha de storage em servidor de armazenamento derrubando site principal e programas/sites dos usuários em sequência — corresponde diretamente ao incidente atual, tanto no componente (storage) quanto no padrão de cascata afetando múltiplos sites/programas dependentes.
  - DAN-073 (llm) [Next steps¶] 0.689: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (llm) [18:23¶] 0.681: #### 18:23¶  At this time, livefile1 had the new volumes attached, and we were logged in and checking everything out. The server needed to do a full filesystem check before the storage was available, 
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi

## q-201 (esperado: DAN-073)

- busca inicial: DAN-073, DAN-209, DAN-109, DAN-226, DAN-129, DAN-208, DAN-026, DAN-191, DAN-064, DAN-103
- justificativa: 
- aprofundar DAN-073: `storage volume failure outage root cause fix recovery` — Bate exatamente: falha de storage em um servidor de storage derruba o site primeiro e depois websites/programas dos usuários, igual ao incidente atual.
- aprofundar DAN-191: `3PAR storage catastrophic outage root cause fix` — É um incidente de storage (controlador 3PAR falhou), mas o resumo indica sem impacto inicial aos usuários, diferente do atual.
- aprofundar DAN-109: `storage nodes cascading failure metadata timeout root cause fix` — Envolve storage nodes caindo em cascata, mas o gatilho é disruption de rede e metadata services, não falha direta de storage server.
  - DAN-073 (llm) [17:04¶] 0.687: #### 17:04¶  By this point we had become sure that the system was getting blocked on storage IO, but the problem did not seem to be the machine itself like the original indications had suggested. Howe
  - DAN-073 (llm) [18:23¶] 0.687: #### 18:23¶  At this time, livefile1 had the new volumes attached, and we were logged in and checking everything out. The server needed to do a full filesystem check before the storage was available, 
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Next steps¶] 0.303: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-191 (llm) [sem seção] 0.589: IT Lead                                                    Trevor B                                                                                           Mark K is the point person at     Gareth W
  - DAN-191 (llm) [sem seção] 0.582: Controllers                                                                                       4. Legacy workload (eg., oracle database, Solaris hosts,    4                      for adaptive       
  - DAN-191 (causa) [sem seção] 0.505: On the 17th October 2016 one of the four controllers within the principal HP storage system located in the Strand Data Centre failed. There was no user impact. HP hardware engineers then arrived on si
  - DAN-191 (correcao) [sem seção] 0.456: The incident timeline presented overleaf is a high level  depiction of the incident from the start on Monday 17th Oct until  the BCP Silver team handed over the recovery and restoration  work to the r
  - DAN-191 (correcao) [sem seção] 0.446: It was later established, in an assessment of the incident by HP, that the inability of the storage system to return to service after the defective hardware was replaced was due to a flaw in the firmw
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.557: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.543: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-202 (esperado: DAN-076)

- busca inicial: DAN-076, DAN-154, DAN-073, DAN-127, DAN-148, DAN-106, DAN-059, DAN-198, DAN-103, DAN-126
- justificativa: 
- aprofundar DAN-076: `boot.ini deletion expansion installer typo name conflict fix` — O resumo menciona exatamente a instalação de uma expansão de jogo deletando o boot.ini, impedindo o computador de iniciar — mesmo cenário do incidente atual (expansão + não-inicialização do PC). Outros incidentes da lista tratam de outages de serviço, infraestrutura ou bugs de patch, sem relação com boot do cliente.
  - DAN-076 (llm) [About the boot.ini issue] 0.764: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.744: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 

## q-203 (esperado: DAN-076)

- busca inicial: DAN-076, DAN-154, DAN-073, DAN-059, DAN-127, DAN-142, DAN-146, DAN-189, DAN-103, DAN-216
- justificativa: 
- aprofundar DAN-076: `boot.ini deletion expansion installer root cause fix` — O incidente atual envolve expansão de jogo impedindo o boot; este é exatamente sobre instalador de expansão deletando boot.ini, com mesma causa e sintoma.
- aprofundar DAN-142: `content update Windows BSOD root cause remediation fix` — Ambos envolvem atualização causando falha de boot/crash em máquinas Windows, embora um seja jogo e outro conteúdo de segurança.
- aprofundar DAN-127: `logging channel cluster start sequence patch root cause fix` — Mesmo estúdio (CCP) e atualização de jogo causando falhas na sequência de inicialização, mas do lado do cluster, não do cliente.
  - DAN-076 (llm) [About the boot.ini issue] 0.763: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.731: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 
  - DAN-142 (llm) [Q: What happened?] 0.668: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [Preliminary Post Incident Review] 0.627: ## Preliminary Post Incident Review  ### Content Configuration Update Impacting the Falcon Sensor and the Windows Operating System (BSOD)  This is CrowdStrike’s preliminary Post Incident Review (PIR).
  - DAN-142 (causa) [What Went Wrong and Why?] 0.384: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.637: # Behind the Scenes of a long EVE Online downtime  We had prepared a series of escalating steps that we intended to follow. Each one would progressively add more factors in to the mix, until the issue
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.62: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan

## q-204 (esperado: DAN-083)

- busca inicial: DAN-083, DAN-195, DAN-190, DAN-102, DAN-058, DAN-092, DAN-188, DAN-126, DAN-003, DAN-056
- justificativa: 
- aprofundar DAN-083: `Postgres sequence jump 32 nextval HA upgrade follower primary fix` — Mesmo componente (Postgres), mesmo gatilho (atualização de alta disponibilidade com promoção de follower a primário) e mesmo sintoma (pulou exatamente 32 IDs sequenciais); não há diferença aparente relevante.
  - DAN-083 (llm) [sem seção] 0.774: ``` /*  * We don't want to log each fetching of a value from a sequence,  * so we pre-log a few fetches in advance. In the event of  * crash we can lose (skip over) as many values as we pre-logged.  *
  - DAN-083 (llm) [sem seção] 0.68: As part of this promotion, the follower (which in many cases had a sequence value up to 32 ahead) became the new primary, at which point all sequences essentially jumped 32 values forward.  Something 
  - DAN-083 (causa) [sem seção] 0.401: 1. We go to great lengths to ensure that if someone asks us to create an incident, we do so (!). We hadn't seen any issues and had no reports from customers, either. 2. For failed incident creation to
  - DAN-083 (correcao) [See related articles] 0.426: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-083 (correcao) [sem seção] 0.318: The other day, we started getting strange reports from some customers of incident.io.  Their incident identifiers — unique numbers to identify each incident — appeared to have jumped unexpectedly. One

## q-205 (esperado: DAN-083)

- busca inicial: DAN-083, DAN-195, DAN-190, DAN-102, DAN-092, DAN-188, DAN-164, DAN-003, DAN-048, DAN-080
- justificativa: 
- aprofundar DAN-083: `Postgres nextval sequence jump 32 HA upgrade root cause fix` — Corresponde exatamente ao incidente atual: upgrade de HA do Postgres seguido de salto de 32 em sequências via nextval; busca a causa raiz e a correção relatadas.
  - DAN-083 (llm) [sem seção] 0.69: ``` /*  * We don't want to log each fetching of a value from a sequence,  * so we pre-log a few fetches in advance. In the event of  * crash we can lose (skip over) as many values as we pre-logged.  *
  - DAN-083 (llm) [sem seção] 0.643: 1. We go to great lengths to ensure that if someone asks us to create an incident, we do so (!). We hadn't seen any issues and had no reports from customers, either. 2. For failed incident creation to
  - DAN-083 (causa) [See related articles] 0.353: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-083 (correcao) [sem seção] 0.325: As part of this promotion, the follower (which in many cases had a sequence value up to 32 ahead) became the new primary, at which point all sequences essentially jumped 32 values forward.  Something 
  - DAN-083 (correcao) [sem seção] 0.318: The other day, we started getting strange reports from some customers of incident.io.  Their incident identifiers — unique numbers to identify each incident — appeared to have jumped unexpectedly. One

## q-206 (esperado: DAN-085)

- busca inicial: DAN-164, DAN-085, DAN-050, DAN-157, DAN-097, DAN-129, DAN-130, DAN-092, DAN-098, DAN-078
- justificativa: 
- aprofundar DAN-085: `SHA1 collision deduplication test data checkout consistency fix remediation` — Mesmo cenário: repositório indisponível após commit com arquivos de teste, checkout falha na verificação de consistência devido a colisão SHA-1.
  - DAN-085 (llm) [Problem Statement] 0.657: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.655: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-207 (esperado: DAN-085)

- busca inicial: DAN-085, DAN-164, DAN-050, DAN-157, DAN-055, DAN-173, DAN-097, DAN-129, DAN-078, DAN-130
- justificativa: 
- aprofundar DAN-085: `SHA1 collision deduplication checkout consistency check root cause fix remediation` — Mesmo tipo de falha: repositório com deduplicação fica indisponível e checkout falha na consistência após commit de arquivos de teste com mesmo hash, exatamente como o incidente atual; diferentemente dos demais, que são falhas de banco de dados, deploy ou segurança.
  - DAN-085 (llm) [Problem Statement] 0.7: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.684: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-208 (esperado: DAN-086)

- busca inicial: DAN-086, DAN-015, DAN-090, DAN-191, DAN-154, DAN-221, DAN-103, DAN-210, DAN-142, DAN-016
- justificativa: 
- aprofundar DAN-086: `leap year certificate expiration date bug fix Azure 2012` — Corresponde exatamente: falha em 29 de fevereiro, certificados rejeitados por data de expiração inválida (29 de fevereiro de 2013) e pane global na plataforma.
  - DAN-086 (llm) [The Leap Day Bug] 0.705: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.698: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-209 (esperado: DAN-086)

- busca inicial: DAN-086, DAN-129, DAN-210, DAN-103, DAN-029, DAN-154, DAN-049, DAN-090, DAN-189, DAN-015
- justificativa: 
- aprofundar DAN-086: `certificate expiration invalid date February 29 leap year fix` — DAN-086 é o único incidente que combina data de 29 de fevereiro, certificados rejeitados por data de expiração inválida causada por bug de ano bissexto, e pane em toda a plataforma — exatamente como o incidente atual, que também menciona falha na criação de novas instâncias.
  - DAN-086 (llm) [The Leap Day Bug] 0.62: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.556: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-210 (esperado: DAN-088)

- busca inicial: DAN-088, DAN-103, DAN-129, DAN-066, DAN-209, DAN-089, DAN-189, DAN-116, DAN-087, DAN-064
- justificativa: 
- aprofundar DAN-088: `leap second xtime_lock printk klogd deadlock fix patch` — Mesmo gatilho (leap second) e mesmo sintoma em Linux (servidores travam/ficam inativos), embora a causa seja deadlock no kernel e não pane de DNS.
- aprofundar DAN-089: `leap second CLOCK_REALTIME hrtimer futex spinwait fix patch` — Mesmo gatilho (leap second) em sistemas Linux, causando alta carga e queda de serviços, mas mecanismo é futex/hrtimer e não deadlock direto.
- aprofundar DAN-087: `leap second time.Now monotonic rand panic fix` — Mesmo gatilho (leap second), mas ocorre no DNS da Cloudflare em Go, não em servidores Linux genéricos travando.
  - DAN-088 (llm) [sem seção] 0.792: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.765: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.81: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.784: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.633: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe
  - DAN-087 (llm) [The one character fix] 0.614: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (causa) [sem seção] 0.385: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (correcao) [Timeline] 0.444: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is
  - DAN-087 (correcao) [A little bit about Cloudflare DNS] 0.318: ### A little bit about Cloudflare DNS  Cloudflare customers use our DNS service to serve the authoritative answers for DNS queries for their domains. They need to tell us the IP address of their origi

## q-211 (esperado: DAN-088)

- busca inicial: DAN-088, DAN-103, DAN-129, DAN-073, DAN-026, DAN-116, DAN-205, DAN-209, DAN-064, DAN-066
- justificativa: 
- aprofundar DAN-088: `leap second xtime_lock printk deadlock kernel fix` — O incidente atual descreve travamento em massa de servidores Linux no segundo bissexto, correspondendo exatamente ao cenário do DAN-088, que precisa ser confirmado quanto à causa raiz e correção.
  - DAN-088 (llm) [sem seção] 0.82: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.794: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco

## q-212 (esperado: DAN-092)

- busca inicial: DAN-092, DAN-103, DAN-133, DAN-134, DAN-080, DAN-209, DAN-195, DAN-101, DAN-148, DAN-035
- justificativa: 
- aprofundar DAN-092: `stale statistics after database upgrade disk reads recovery rollback` — Mesmo componente (banco de workflows), mesmo gatilho (cutover/upgrade) e mesmos sintomas (queries lendo do disco, latência alta, jobs descartados); difere porque o atual não menciona estatísticas ou ANALYZE explicitamente.
  - DAN-092 (llm) [What Happened] 0.662: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [What Happened] 0.582: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (causa) [Summary] 0.393: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-092 (correcao) [Future Prevention and Process Improvement] 0.483: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru

## q-213 (esperado: DAN-092)

- busca inicial: DAN-092, DAN-133, DAN-164, DAN-134, DAN-080, DAN-148, DAN-101, DAN-078, DAN-130, DAN-096
- justificativa: 
- aprofundar DAN-092: `stale statistics ANALYZE index disk queries workflows database cutover fix re-promote blue` — O resumo já menciona cutover de workflows database, queries lendo do disco por estatísticas desatualizadas, latência alta e jobs dropped — corresponde quase que exatamente ao incidente atual
- aprofundar DAN-133: `workflow delay root cause MongoDB JVM thread pool fix` — Também envolve delays em workflows, mas a causa é MongoDB e pools de JVM, não banco de workflows com estatísticas desatualizadas — menos parecido, mas vale verificar
- aprofundar DAN-080: `Postgres migration blocked queries root cause fix zero-downtime` — Envolve migrations de banco de dados, mas o cenário é bloqueio por query de leitura longa, não cutover com estatísticas desatualizadas
  - DAN-092 (llm) [What Happened] 0.714: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [What Happened] 0.677: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (causa) [Summary] 0.393: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-092 (correcao) [Future Prevention and Process Improvement] 0.483: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-133 (llm) [Incident Report] 0.771: ## Incident Report  Around the same time, we updated many services to a new minor version of the JVM to pick up security changes. This update also included improvements for docker-awareness enabled by
  - DAN-133 (llm) [Incident Report] 0.71: ## Incident Report  April 10, 2019 at 13:25 UTC we were alerted to sharp increases in multiple queues responsible for job and workflow processing. Our monitoring of MongoDB showed some issues, but not
  - DAN-133 (causa) [Incident Report] 0.453: ## Incident Report  Between March 26 and April 10, 2019, our platform experienced instability and downtime primarily due to issues with the datastore backing our builds queue. These datastore issues r
  - DAN-133 (correcao) [Incident Report] 0.533: ## Incident Report  Ultimately, refactoring the way we store and access portions of our data set in MongoDB will reduce load. Improving our data access and storage at the application level is one of o
  - DAN-133 (correcao) [Incident Report] 0.444: ## Incident Report  Perhaps most importantly, MongoDB support pointed us at the `tcmalloc.spinlock_total_delay_ns` MongoDB stat. This stat correlates with the time spent on database operations blocked
  - DAN-080 (llm) [Avoiding downtime] 0.721: ## Avoiding downtime  Applications vary too much for there to be a "one size fits all" solution to this problem, but there are a few good places to start:  - Eliminate long-running queries/transaction
  - DAN-080 (llm) [So what happened?] 0.704: ## So what happened?  We deployed the changes, and all of our assumptions got blown out of the water. Just after the schema migration started, we started getting alerts about API requests timing out. 
  - DAN-080 (causa) [Zero-downtime Postgres migrations - the hard parts] 0.354: ## Zero-downtime Postgres migrations - the hard parts  Written by  Last editedJun 2024  A few months ago, we took around 15 seconds of unexpected API downtime during a planned database migration. We'r
  - DAN-080 (correcao) [Background] 0.31: ## Background  We're no strangers to zero-downtime schema changes. Having the database stop responding to queries for more than a second or two isn't an option, so there's a bunch of stuff you learn e
  - DAN-080 (correcao) [The migration] 0.305: ## The migration  Jump back to late January. At the time, we were building invoicing for our Pro product. We'd been through a couple of iterations, and settled on model/table names. We'd already deplo

## q-214 (esperado: DAN-093)

- busca inicial: DAN-048, DAN-078, DAN-093, DAN-094, DAN-003, DAN-190, DAN-164, DAN-096, DAN-186, DAN-058
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover wrong owner data drift Percona` — Bate porque uma migração de schema causou failover do MySQL e repositórios privados foram roteados para donos errados, igual ao incidente atual; não bate porque envolve Percona Replication Manager e Pacemaker, não mencionados aqui.
- aprofundar DAN-078: `MySQL master failover network partition missing writes data integrity` — Bate porque envolve failover inesperado do MySQL master com perda de writes; não bate porque o gatilho foi particionamento de rede durante manutenção, não migração de schema, e não menciona dados de outras contas.
- aprofundar DAN-048: `RDS hardware failure incorrect MySQL configuration data loss fix` — Bate porque envolve configuração incorreta do MySQL e perda de dados; não bate porque o gatilho foi falha de hardware RDS, não migração de schema, e não menciona exposição entre contas.
  - DAN-093 (llm) [Monday, September 10th] 0.689: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.579: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.368: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member
  - DAN-078 (llm) [Incident timeline] 0.725: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [Next steps] 0.627: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [Communication] 0.474: ## Communication  In our desire to communicate meaningful information to you during the incident, we made several public estimates on time to repair based on the rate of processing of the backlog of d
  - DAN-048 (llm) [Final thoughts] 0.755: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (llm) [Incorrect configuration variable] 0.72: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m

## q-215 (esperado: DAN-093)

- busca inicial: DAN-048, DAN-078, DAN-093, DAN-003, DAN-164, DAN-094, DAN-096, DAN-186, DAN-080, DAN-056
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover root cause fix data drift wrong owners` — É o único incidente que combina migração de schema, failover inesperado do MySQL e dados entregus a contas/owners erradas (repositórios privados roteados para donos errados), refletindo exatamente o incidente atual.
  - DAN-093 (llm) [Monday, September 10th] 0.664: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.607: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.368: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-216 (esperado: DAN-106)

- busca inicial: DAN-106, DAN-073, DAN-048, DAN-164, DAN-109, DAN-071, DAN-191, DAN-064, DAN-139, DAN-060
- justificativa: 
- aprofundar DAN-106: `routine networking upgrade human error EBS volume freeze region outage root cause fix` — Bate: atualização de rede de rotina, impacto regional, volumes de armazenamento afetados. Não bate: perda de 0.07% dos volumes, não travamento total de todos os volumes.
- aprofundar DAN-073: `storage volume failure root cause fix dependent instances outage` — Bate: falha de volume de armazenamento derruba instâncias dependentes. Não bate: falha em um único servidor de armazenamento, não atualização de rede nem região inteira.
- aprofundar DAN-109: `network disruption storage nodes down root cause recovery fix` — Bate: problema de rede afeta armazenamento e nós se desligam. Não bate: interrupção de rede não planejada, metadados DynamoDB, não atualização de rotina nem volumes EBS.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.693: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  A large majority of the volumes in the degraded EBS cluster were still functioning properly and the focus was to 
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.691: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-073 (llm) [Next steps¶] 0.691: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (llm) [The details¶] 0.686: ### The details¶  At 16:06 UTC on 7 July 2020, a storage volume failure on one of our storage servers caused a number of outages, starting with our own site and also with our users’ programs (includin
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.566: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.548: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  The specific assignment of a group of partitions to a given server is called a “membership.” The member
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.368: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.407: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs

## q-217 (esperado: DAN-106)

- busca inicial: DAN-106, DAN-073, DAN-060, DAN-109, DAN-107, DAN-210, DAN-071, DAN-222, DAN-048, DAN-143
- justificativa: 
- aprofundar DAN-106: `routine networking upgrade resource crunch volume loss recovery fix` — Bate por ser uma atualização de rede de rotina que afetou volumes em toda a região, embora não mencione especificamente volumes parados.
- aprofundar DAN-109: `network disruption metadata service storage node timeout recovery fix` — Bate por envolver disrupção de rede e nós de armazenamento, mas não é uma atualização de rotina.
- aprofundar DAN-143: `automatic upgrade removed network rules Cilium outage recovery fix` — Bate por ser uma atualização que removeu regras de rede e afetou várias regiões, mas não envolve volumes de armazenamento bloqueados.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.544: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.543: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Second, because of the changes made to reduce the node-to-node communication used by peers to find new capacity (
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.624: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.618: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was
  - DAN-143 (llm) [Root cause] 0.656: ## Root cause  We have identified (and since disabled) the initial trigger for the outage: on March 8, 2023, at 06:00 UTC, a security update to systemd was automatically applied to a number of VMs, wh
  - DAN-143 (llm) [Root cause] 0.553: ## Root cause  However, the base OS image we use to run Kubernetes had a legacy security update channel enabled, which caused the update to apply automatically. By design we use fairly minimal base OS
  - DAN-143 (causa) [Lessons learned] 0.422: ## Lessons learned  The following is not the sum total of everything we learned during the incident but rather important themes that pertain to the whole platform.  This was our first global incident.
  - DAN-143 (correcao) [Lessons learned] 0.446: ## Lessons learned  Even with separate systems that serve live data when historical data is not accessible (e.g., APM’s Live Search and Log Management’s Live Tail), we did not provide our customers wi
  - DAN-143 (correcao) [Recovery] 0.445: ## Recovery  The high-level steps of the recovery had to be sequenced because of the magnitude of the compute capacity drop:  - First, for each region, recover enough compute capacity so that it could

## q-218 (esperado: DAN-116)

- busca inicial: DAN-126, DAN-146, DAN-103, DAN-066, DAN-209, DAN-106, DAN-048, DAN-191, DAN-116, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update all servers crash simultaneous fix` — Bate porque uma atualização de banco de dados revelou um bug que derrubou todos os servidores ao mesmo tempo, com atraso para disparar, igual ao atual; não confirma se o componente é o mesmo.
- aprofundar DAN-126: `bug fix data loss server misconfiguration hotfix rollback fix` — Bate porque envolve uma correção/atualização que afetou vários servidores depois de aplicada; não bate exatamente porque foca em perda de dados por configuração de hotfix.
- aprofundar DAN-106: `human error networking upgrade resource crunch outage fix` — Bate porque um upgrade rotineiro causou outage em múltiplas zonas/servidores; não é exatamente uma atualização de dados, mas sim de rede.
  - DAN-116 (llm) [sem seção] 0.705: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.591: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-126 (llm) [Server Configurations] 0.656: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [Server Configurations] 0.644: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (causa) [Server Configurations] 0.378: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.487: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.481: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.353: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di

## q-219 (esperado: DAN-116)

- busca inicial: DAN-066, DAN-126, DAN-103, DAN-222, DAN-205, DAN-209, DAN-116, DAN-109, DAN-191, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update server crash fix root cause` — Bate: atualização de banco de dados fez todos os servidores caírem simultaneamente, com atraso no tempo até o crash. Não bate: componente é o 'impression bus' e não o serviço crítico atual.
  - DAN-116 (llm) [sem seção] 0.708: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.642: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-220 (esperado: DAN-118)

- busca inicial: DAN-148, DAN-118, DAN-066, DAN-067, DAN-154, DAN-217, DAN-209, DAN-191, DAN-001, DAN-109
- justificativa: 
- aprofundar DAN-118: `atlassian april 2022 outage root cause fix` — Bate por centenas de clientes perderem acesso aos produtos; não bate por durar até 14 dias.
- aprofundar DAN-154: `fastly june 8 outage root cause fix` — Bate por pane global simultânea em todos os produtos; não bate por ser disparado por configuração do cliente.
- aprofundar DAN-148: `epic games service outage root cause remediation` — Bate por interrupção total de serviço sob carga extrema; não bate por ser causado por pico de usuários concorrentes.
  - DAN-118 (llm) [Table of contents] 0.751: ## Table of contents  ## Overview of Atlassian’s cloud architecture  To understand contributing factors to the incident as discussed throughout this document, it is helpful to first understand the dep
  - DAN-118 (llm) [Executive summary] 0.747: ## Executive summary  On Tuesday, April 5th, 2022, starting at 7:38 UTC, 775 Atlassian customers lost access to their Atlassian products. The outage spanned up to 14 days for a subset of these custome
  - DAN-118 (causa) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (correcao) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (correcao) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si
  - DAN-154 (llm) [sem seção] 0.77: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (llm) [**What happened?**] 0.759: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s
  - DAN-148 (llm) [**Account Service outage**] 0.711: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [**Cloud capacity limits and throttling**] 0.699: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (causa) [**XMPP outage**] 0.495: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (correcao) [Postmortem of Service Outage at 3.4M CCU] 0.399: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme

## q-221 (esperado: DAN-118)

- busca inicial: DAN-067, DAN-118, DAN-148, DAN-154, DAN-209, DAN-066, DAN-191, DAN-068, DAN-109, DAN-217
- justificativa: 
- aprofundar DAN-118: `customers lost access products outage root cause remediation fix` — 775 clientes perderam acesso a produtos (plural), bate com 'centenas de clientes' e 'todos os produtos', mas não confirma se foi simultâneo nem qual foi a causa.
- aprofundar DAN-154: `global outage software bug valid customer configuration change fix` — Outage global corresponde a 'todos os produtos de uma vez', mas é desencadeado por config change de cliente, não por perda de acesso de centenas de clientes identificados.
- aprofundar DAN-109: `cascading failure network disruption storage nodes down root cause fix` — Falha em cascata que derruba múltiplos nós/serviços pode afetar tudo de uma vez, mas incide sobre um único serviço (DynamoDB), não múltiplos produtos.
  - DAN-118 (llm) [Executive summary] 0.625: ## Executive summary  On Tuesday, April 5th, 2022, starting at 7:38 UTC, 775 Atlassian customers lost access to their Atlassian products. The outage spanned up to 14 days for a subset of these custome
  - DAN-118 (llm) [Executive summary] 0.611: ## Executive summary  At the start of the incident, we knew exactly which sites were affected and our priority was to establish communication with the approved owner for each impacted site to inform t
  - DAN-118 (causa) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (correcao) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (correcao) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si
  - DAN-154 (llm) [**What happened?**] 0.687: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (llm) [sem seção] 0.681: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.552: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.535: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  The specific assignment of a group of partitions to a given server is called a “membership.” The member
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.368: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.407: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs

## q-222 (esperado: DAN-121)

- busca inicial: DAN-129, DAN-144, DAN-147, DAN-121, DAN-016, DAN-137, DAN-134, DAN-209, DAN-148, DAN-220
- justificativa: 
- aprofundar DAN-121: `database backend overloaded throttle requests services timeout root cause fix` — Bate exatamente: banco de backend sobrecarregado limitando requisições e serviços, incluindo player de vídeo (iPlayer), dando timeout. Não bate: é um outage de 2014 de serviços BBC, não um sistema específico de streaming moderno.
- aprofundar DAN-147: `database capacity request queue overload cascading failure root cause fix` — Bate parcialmente: banco de dados sobrecarregado por filas de requisições causando falha em cascata. Não bate: é de autenticação (DUO1), não de player de vídeo, e o gatilho é capacidade insuficiente/planejamento, não throttling explícito do backend.
  - DAN-121 (llm) [sem seção] 0.492: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.464: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.616: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.595: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-223 (esperado: DAN-121)

- busca inicial: DAN-147, DAN-148, DAN-101, DAN-129, DAN-134, DAN-219, DAN-164, DAN-121, DAN-144, DAN-094
- justificativa: 
- aprofundar DAN-121: `database backend overloaded throttle requests services timeout fix` — O resumo descreve exatamente database sobrecarregado throttling requisições e serviços com timeout, igual ao incidente atual.
- aprofundar DAN-164: `influx requests overloaded database replication lag fix` — Descreve influxo de requisições sobrecarregando o database, componente igual, mas inclui exclusão acidental de diretório que não bate.
- aprofundar DAN-147: `request queue overloading insufficient database capacity cascading failure` — Descreve capacidade insuficiente do database sobrecarregada por fila de requisições, mas o gatilho é uma fila não mencionada no atual.
  - DAN-121 (llm) [sem seção] 0.477: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.458: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-164 (llm) [Timeline] 0.688: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.654: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.587: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.585: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-224 (esperado: DAN-122)

- busca inicial: DAN-152, DAN-122, DAN-124, DAN-177, DAN-157, DAN-136, DAN-215, DAN-203, DAN-237, DAN-142
- justificativa: 
- aprofundar DAN-152: `npm account compromise malicious package publication root cause fix` — Escolhi porque envolve conta de mantenedor comprometida e publicação de pacotes maliciosos no registry, igual ao atual, embora o alvo seja npm.
- aprofundar DAN-122: `JCenter impersonation attack malicious Maven package root cause remediation` — Escolhi porque descreve pacotes maliciosos inseridos em repositório público via personificação, semelhante ao atual, mas foca em Maven/JCenter.
  - DAN-152 (llm) [Summary] 0.749: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.746: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.707: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.652: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-225 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-177, DAN-124, DAN-136, DAN-203, DAN-157, DAN-142, DAN-050, DAN-216
- justificativa: 
- aprofundar DAN-122: `malicious packages impersonation attack JCenter Maven root cause fix` — Semelhante: repositório público de pacotes (JCenter/Maven) com pacotes maliciosos publicados por usurpação de identidade, mas ocorre em Maven, não npm.
- aprofundar DAN-152: `compromised npm account malicious packages published root cause fix` — Semelhante: conta de desenvolvedor conhecido comprometida no repositório público npm para publicar pacotes maliciosos, mas envolve conta mantenedor, não exatamente nome usurpado.
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.751: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.687: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.759: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.741: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-226 (esperado: DAN-124)

- busca inicial: DAN-124, DAN-131, DAN-015, DAN-140, DAN-203, DAN-017, DAN-157, DAN-053, DAN-014, DAN-175
- justificativa: 
- aprofundar DAN-124: `Shellshock prototype machine secret keys production breach cause fix` — envolve chaves secretas que levaram a violação de produção, parecido com acesso não autorizado com chaves válidas, mas diferencia-se por ser máquina antiga com Shellshock
- aprofundar DAN-131: `malware engineer laptop stolen SSO session production access remediation` — sessão válida roubada usada para acessar sistemas de produção, próximo ao uso indevido de chaves válidas, mas via malware em laptop e não diretamente com chaves
- aprofundar DAN-175: `private tokens leaked unauthorized access databases remediation fix` — tokens privados vazados permitiram acesso não autorizado a dados, semelhante a chaves válidas usadas indevidamente, mas não menciona explicitamente produção
  - DAN-124 (llm) [Where did we go wrong?] 0.582: ## Where did we go wrong?  All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover,
  - DAN-124 (llm) [What happened?] 0.558: ## What happened?  BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was t
  - DAN-124 (causa) [BrowserStack Security Incident Report — November 2014 (Resolved)] 0.331: # BrowserStack Security Incident Report — November 2014 (Resolved)  Original Incident Statement — Published November 10, 2014  As you may already know, BrowserStack experienced an attack on 9th Novemb
  - DAN-124 (correcao) [Security measures taken to mitigate and prevent further incidents] 0.556: ## Security measures taken to mitigate and prevent further incidents  - After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an add
  - DAN-124 (correcao) [Security Evolution: 2014 → 2026] 0.407: ## Security Evolution: 2014 → 2026  This incident catalyzed a complete transformation of our security infrastructure. Here is what BrowserStack looks like today.  | Area | 2014 Status | 2026 Status (C
  - DAN-131 (llm) [What happened?] 0.579: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.535: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi
  - DAN-175 (llm) [Incident Summary] 0.591: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.561: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-227 (esperado: DAN-124)

- busca inicial: DAN-124, DAN-131, DAN-140, DAN-203, DAN-015, DAN-017, DAN-157, DAN-175, DAN-132, DAN-073
- justificativa: 
- aprofundar DAN-131: `malware stolen valid SSO session production access remediation fix` — Bate: acesso não autorizado à produção usando sessão/credencial válida roubada. Não bate: foi sessão SSO via malware em laptop, não exatamente 'nossas próprias chaves'.
- aprofundar DAN-124: `Shellshock secret keys production breach root cause fix` — Bate: chaves secretas em máquina antiga levaram a violação da produção. Não bate: vetor foi Shellshock em protótipo, não uso direto de chaves válidas pelo atacante.
- aprofundar DAN-132: `breached database OAuth tokens IAM keys SSH keys revoke cycle fix` — Bate: tokens e chaves válidas (OAuth, IAM, SSH) expostas e usadas indevidamente, com revogação e rotação como correção. Não bate: origem foi vazamento de provedor banco de dados, não acesso direto com chaves próprias em produção.
  - DAN-131 (llm) [What happened?] 0.593: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [How do we know this attack vector is closed and it’s safe to build?] 0.515: ## How do we know this attack vector is closed and it’s safe to build?  We are confident that customers can safely build on CircleCI.  We have taken many steps since becoming aware of this attack, bot
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi
  - DAN-124 (llm) [Where did we go wrong?] 0.618: ## Where did we go wrong?  All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover,
  - DAN-124 (llm) [What happened?] 0.576: ## What happened?  BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was t
  - DAN-124 (causa) [BrowserStack Security Incident Report — November 2014 (Resolved)] 0.331: # BrowserStack Security Incident Report — November 2014 (Resolved)  Original Incident Statement — Published November 10, 2014  As you may already know, BrowserStack experienced an attack on 9th Novemb
  - DAN-124 (correcao) [Security measures taken to mitigate and prevent further incidents] 0.556: ## Security measures taken to mitigate and prevent further incidents  - After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an add
  - DAN-124 (correcao) [Security Evolution: 2014 → 2026] 0.407: ## Security Evolution: 2014 → 2026  This incident catalyzed a complete transformation of our security infrastructure. Here is what BrowserStack looks like today.  | Area | 2014 Status | 2026 Status (C
  - DAN-132 (llm) [Our response] 0.657: # Our response  To contain any potential risk we determined that the best course of action was to shutdown the CircleCI website and stop all builds. We also determined that it would be best to revoke 
  - DAN-132 (llm) [Our response] 0.634: # Our response  At 11:26pm we sent Heroku a list of all known SSH keys. We learned at 1:25pm today that those keys have all been revoked.  At 11:44pm we completed the process of deleting all our cache
  - DAN-132 (causa) [Incident details] 0.331: # Incident details  On Monday, October 28th, at 3:46pm Pacific, we noticed an IAM key had been deleted. We immediately searched for any evidence that our systems had been compromised, and to discover 
  - DAN-132 (correcao) [sem seção] 0.5: On October 29th, we received a notification email from our database provider telling us that they had been compromised. We later learned that our database was among those accessed by the attackers.  A
  - DAN-132 (correcao) [What you should do] 0.398: # What you should do  In order to protect your data and users, we strongly urge you to secure each of these systems:  - systems accessible by SSH keys uploaded to CircleCI - systems accessible using A

## q-228 (esperado: DAN-125)

- busca inicial: DAN-164, DAN-147, DAN-156, DAN-048, DAN-096, DAN-043, DAN-094, DAN-209, DAN-134, DAN-109
- justificativa: 
- aprofundar DAN-147: `database capacity overload cascading failure root cause fix` — Bate: falha em cascata, banco sob carga insuficiente, planejamento de capacidade. Não bate: não menciona redução recente de tamanho.
- aprofundar DAN-096: `peak hour load mysql cluster ProxySQL connection exhaustion fix` — Bate: carga em horário de pico, cluster de banco de dados, conexões esgotadas. Não bate: não menciona redução de tamanho nem servidores dependentes caindo.
- aprofundar DAN-164: `database overload replication lag root cause fix data loss` — Bate: influxo de requisições sobrecarregou o banco de dados. Não bate: causa principal inclui exclusão de diretório por erro humano, não redução de capacidade.
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.582: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.513: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.708: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.685: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev
  - DAN-164 (llm) [Root cause analysis] 0.744: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.705: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-229 (esperado: DAN-125)

- busca inicial: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-129, DAN-091, DAN-125
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade cascading collapse dependent servers peak` — Bate perfeitamente: redução recente de capacidade do banco, carga em pico e colapso em cascata de servidores dependentes.
- aprofundar DAN-147: `cascading failure insufficient database capacity request queue` — Bate: falha em cascata por capacidade insuficiente do banco. Não bate: não menciona redução recente de capacidade.
- aprofundar DAN-091: `peak load primary database queued operations fix` — Bate: carga em pico sobrecarregando banco primário. Não bate: não menciona downsizing nem cascata de servidores dependentes.
  - DAN-125 (llm) [Database performance issues] 0.591: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.486: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.599: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.586: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-091 (llm) [Postmortem] 0.696: ## Postmortem  We identified a couple of changes that required additional work but had performed well in evaluation and rolled them back. Unfortunately, by that time the queued DB operations were back
  - DAN-091 (llm) [Postmortem] 0.625: ## Postmortem  THURSDAY 09:00 UTC: We worked to bring up excess capacity to handle the backlog and push builds in as fast as we could. Then we learned that the throttles we had built into our build sc
  - DAN-091 (causa) [Postmortem] 0.464: ## Postmortem  We've also moved over 50 percent of the data that was in our primary database onto its own deployment. The data was orthogonal and didn't need to be co-located, but its heavy use was ca
  - DAN-091 (correcao) [Resolved] 0.326: ## Resolved  We’re continuing to see builds running normally. We will be monitoring closely throughout the day. Please contact us in support if you’re seeing issues with your builds.  Posted Oct 15, 2
  - DAN-091 (correcao) [Postmortem] 0.423: ## Postmortem  Getting back to the architecture, we've known for a while that our queue model needs to be rebuilt and we've been laying the foundation to get there with the items outlined above, but w

## q-230 (esperado: DAN-126)

- busca inicial: DAN-126, DAN-076, DAN-059, DAN-106, DAN-211, DAN-127, DAN-216, DAN-145, DAN-146, DAN-116
- justificativa: 
- aprofundar DAN-126: `data loss bug fix hotfix server misconfiguration rollback` — É um jogo (Destiny 2) com perda de dados após atualização/hotfix, muito parecido com perda de itens e progresso, embora a causa seja timestamps e reconfiguração de servidor.
- aprofundar DAN-127: `game patch logging channel cluster nodes startup failure` — É um jogo (EVE Online) com problema após novo patch, mas a causa é um canal de log e queda de nós, não perda direta de itens ou progresso dos jogadores.
- aprofundar DAN-146: `OS upgrade machines wiped databases outage` — Envolve perda de dados após uma atualização de sistema, mas é infraestrutura do Dropbox, não um jogo com itens de jogadores.
  - DAN-126 (llm) [Server Configurations] 0.661: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [Server Configurations] 0.651: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.686: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.666: # Behind the Scenes of a long EVE Online downtime  Via the console we modified the campaign loading functions so that they performed the load-from-DB operations normally, but all their logging operati
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan
  - DAN-146 (llm) [sem seção] 0.675: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [sem seção] 0.536: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri

## q-231 (esperado: DAN-126)

- busca inicial: DAN-126, DAN-059, DAN-076, DAN-127, DAN-146, DAN-058, DAN-145, DAN-116, DAN-142, DAN-043
- justificativa: 
- aprofundar DAN-126: `game update hotfix timestamp bug data loss rollback` — Jogo e atualização causando perda de dados de jogadores, muito parecido, mas envolve bug de timestamp e hotfix, não apenas uma update genérica.
- aprofundar DAN-127: `game patch logging cluster nodes crash fix` — Atualização/patch de jogo derrubando infraestrutura, gatilho similar, mas o resumo não menciona perda de itens ou progresso dos jogadores.
- aprofundar DAN-058: `database backup identifiers data loss fix` — Perda de dados por configuração incorreta, resultado similar, mas não é desencadeado por atualização de jogo.
  - DAN-126 (llm) [sem seção] 0.644: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (llm) [Server Configurations] 0.613: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (causa) [Server Configurations] 0.378: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (correcao) [Server Configurations] 0.408: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.658: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.625: # Behind the Scenes of a long EVE Online downtime  Once all nodes were up and we had verified that solar-systems had loaded ok, we opened up a python console on the server, allowing us to issue comman
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan
  - DAN-058 (llm) [What happened?] 0.712: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.69: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n

## q-232 (esperado: DAN-127)

- busca inicial: DAN-127, DAN-211, DAN-219, DAN-210, DAN-208, DAN-103, DAN-145, DAN-066, DAN-094, DAN-151
- justificativa: 
- aprofundar DAN-127: `logging channel cluster nodes dying start sequence patch root cause fix` — Bate exatamente: patch novo de jogo + nós do cluster morrem durante a inicialização (start sequence). Não bate se a causa específica (canal de logging) for diferente do atual.
- aprofundar DAN-210: `Kubernetes cluster upgrade failed node metadata networking fix root cause` — Bate parcialmente: falha de cluster após mudança de versão/upgrade. Não bate: não é patch de jogo e o sintoma é rede de workloads, não nós morrendo na inicialização.
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.675: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.648: # Behind the Scenes of a long EVE Online downtime  We had prepared a series of escalating steps that we intended to follow. Each one would progressively add more factors in to the mix, until the issue
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan
  - DAN-210 (llm) [Get to the Point, Spock, If You Have One] 0.695: ## Get to the Point, Spock, If You Have One  How did it actually break? That’s one of the most unexpected things of all. In doing the research, we discovered that the way that the route reflectors wer
  - DAN-210 (llm) [It Begins] 0.695: ## It Begins  All at once the site came to a screeching halt. We opened an incident immediately, and brought all hands on deck, trying to figure out what had happened. Hands were on deck and in the ca
  - DAN-210 (causa) [A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack] 0.526: ## A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack  Further investigation kicked off. We started looking at everything we could think of to try and narrow down the exact mome
  - DAN-210 (correcao) [It Begins] 0.466: ## It Begins  We are sufficiently paranoid, so of course our upgrade procedure includes taking a backup as standard. However, this backup procedure, and the restore, were written several years ago. Wh
  - DAN-210 (correcao) [TL;DR] 0.449: ## TL;DR  - Upgrades, particularly to our Kubernetes clusters, are risky for us, but we must do them anyway. We test and validate them in advance as best we can, but we still have plenty of work to do

## q-233 (esperado: DAN-127)

- busca inicial: DAN-127, DAN-211, DAN-148, DAN-070, DAN-103, DAN-210, DAN-094, DAN-208, DAN-219, DAN-029
- justificativa: 
- aprofundar DAN-127: `logging channel cluster nodes dying startup patch root cause fix` — O resumo descreve exatamente o mesmo cenário: um novo patch de jogo fazendo nós do cluster morrerem durante a sequência de inicialização, diferente dos outros que envolvem carga, energia ou banco de dados.
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.672: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.642: # Behind the Scenes of a long EVE Online downtime  Via the console we modified the campaign loading functions so that they performed the load-from-DB operations normally, but all their logging operati
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan

## q-234 (esperado: DAN-129)

- busca inicial: DAN-129, DAN-209, DAN-119, DAN-224, DAN-011, DAN-073, DAN-035, DAN-205, DAN-162, DAN-116
- justificativa: 
- aprofundar DAN-129: `health check timeout low launch latency unresponsiveness fix` — O resumo já cita duas horas após lançamento, latência alta, resposta intermitente e timeouts baixos de health check — o que bate com instâncias marcadas não saudáveis no incidente atual.
- aprofundar DAN-224: `regex backtracking health check failure outage fix` — Menciona health-check failures que levaram a outage, mas a causa (regex) não tem relação com lançamento, apenas o sintoma de health check se parece.
- aprofundar DAN-035: `load balancer configuration rollout error rate fix` — Envolve load balancer e aumento de error rates, mas não cita lançamento nem health checks, sendo menos relacionado ao incidente atual.
  - DAN-129 (llm) [Health Check Timeouts] 0.715: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [App Servers Undersized] 0.57: ### App Servers Undersized  The application servers were woefully undersized for the traffic we needed to be able to handle. The single CPU core of an m3.medium was just not enough CPU to keep up with
  - DAN-129 (causa) [Conclusion] 0.457: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 
  - DAN-224 (llm) [Follow-up Actions] 0.63: # Follow-up Actions  - Audit our regular expressions and post validation workflow for any similar issues - Add controls to our load balancer to disable the healthcheck – as we believe everything but t
  - DAN-224 (llm) [Technical Details] 0.626: # Technical Details  The regular expression was: `^[\s\u200c]+|[\s\u200c]+$` Which is intended to trim unicode space from start and end of a line. A simplified version of the Regex that exposes the sa
  - DAN-224 (causa) [Overview] 0.478: # Overview  On July 20, 2016 we experienced a 34 minute outage starting at 14:44 UTC. It took 10 minutes to identify the cause, 14 minutes to write the code to fix it, and 10 minutes to roll out the f
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.798: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.757: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.36: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration

## q-235 (esperado: DAN-129)

- busca inicial: DAN-129, DAN-218, DAN-205, DAN-011, DAN-209, DAN-148, DAN-073, DAN-035, DAN-133, DAN-211
- justificativa: 
- aprofundar DAN-129: `health check timeout low latency intermittent unresponsiveness root cause fix` — O resumo cita falha duas horas após o lançamento, latência aumentada, inresponsividade intermitente e timeouts de health check muito baixos, correspondendo diretamente aos sintomas do incidente atual.
  - DAN-129 (llm) [Health Check Timeouts] 0.757: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [sem seção] 0.601: Approximately two hours after Supermarket became the official community site it started to experience increased latency and intermittent unresponsiveness. This made downloading cookbooks problematic a
  - DAN-129 (causa) [Conclusion] 0.457: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 

## q-236 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-217, DAN-078, DAN-221, DAN-164, DAN-210
- justificativa: 
- aprofundar DAN-145: `redis primary failover cluster rebalance cascading connection fix` — O atual é exatamente Redis primário caindo, rebalance do cluster e falha em cascata de conexões; o Discord bate em causa e gatilho, diferindo só pela plataforma Google Cloud.
- aprofundar DAN-217: `cascading connection failures database capacity disconnection reconnection fix` — Bate no sintoma de falha em cascata de conexões após desconexões em massa, embora o gatilho seja usuário e não Redis primário.
- aprofundar DAN-234: `redis cluster network partition master crash read only fix` — Envolve Redis cluster e falha em cascata, mas o foco é cobrança/billing, não conexões de usuários em cascata.
  - DAN-145 (llm) [Sequence of Events] 0.707: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.681: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-217 (llm) [TUESDAY] 0.744: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [sem seção] 0.533: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [WEDNESDAY] 0.429: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou
  - DAN-234 (llm) [What We’re Doing About It] 0.59: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.582: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn

## q-237 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-048, DAN-029, DAN-070, DAN-096, DAN-210, DAN-078, DAN-221
- justificativa: 
- aprofundar DAN-145: `Redis primary failover cluster rebalance cascade connection fix` — Descreve primário Redis caindo/migrando, rebalance do cluster e falha em cascata nas conexões de usuário, igual ao incidente atual.
- aprofundar DAN-234: `Redis cluster network partition master crash read-only fix` — Envolve falha em cluster Redis com master sobrecarregado e efeitos em cascata, mas ocorre no faturamento, não nas conexões de usuário.
- aprofundar DAN-066: `cascading Byzantine failure API dashboard root cause fix` — Apenas o padrão de falha em cascata afetando a API se assemelha; não envolve Redis nem failover de primário.
  - DAN-145 (llm) [Sequence of Events] 0.724: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.686: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-234 (llm) [What We’re Doing About It] 0.586: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.581: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn
  - DAN-066 (llm) [The Dashboard] 0.667: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [Redundant Points of Failure] 0.617: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (causa) [Postscript] 0.502: ### Postscript  The distributed systems community has pointed out that the failure we've encountered would be better characterized as an omission fault rather than a Byzantine fault. Omission faults a
  - DAN-066 (correcao) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.463: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain

## q-238 (esperado: DAN-148)

- busca inicial: DAN-148, DAN-106, DAN-217, DAN-191, DAN-067, DAN-066, DAN-221, DAN-209, DAN-109, DAN-144
- justificativa: 
- aprofundar DAN-148: `3.4 million concurrent users service outage root cause fix` — Bate fortemente: pico recorde de usuários simultâneos causando disrupções parciais e totais, exatamente como o incidente atual.
- aprofundar DAN-217: `massive disconnection reconnection database capacity cascading failure fix` — Bate parcialmente: sobrecarga em cascata por conexões de usuários, mas o gatilho é tempestade de reconexão, não um pico recorde de CCU.
- aprofundar DAN-144: `thundering herd reconnect cascading frontend out of memory fix` — Bate parcialmente: reconexão em cascata esgotando recursos, mas o gatilho é serviço flapping, não pico recorde de usuários simultâneos.
  - DAN-148 (llm) [**Account Service outage**] 0.657: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [**XMPP outage**] 0.653: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-217 (llm) [TUESDAY] 0.756: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [WEDNESDAY] 0.539: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou
  - DAN-144 (llm) [Summary] 0.541: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.53: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (causa) [Resolved] 0.45: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Connectivity Issues] 0.428: ## Connectivity Issues  ## Postmortem  At Discord, one of our primary concerns is the uptime and reliability of our service. We’ve all experienced the frustration and annoyance that comes along with t

## q-239 (esperado: DAN-148)

- busca inicial: DAN-148, DAN-209, DAN-001, DAN-067, DAN-066, DAN-217, DAN-106, DAN-109, DAN-191, DAN-208
- justificativa: 
- aprofundar DAN-148: `record peak concurrent users service disruption partial total root cause fix` — O título e o resumo batem exatamente com o incidente atual: pico recorde de usuários concorrentes causando interrupções parciais e totais, enquanto os outros incidentes têm gatilhos como migração, falha de energia ou erro humano.
  - DAN-148 (llm) [**Account Service outage**] 0.654: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [**XMPP outage**] 0.632: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme

## q-240 (esperado: DAN-152)

- busca inicial: DAN-009, DAN-175, DAN-140, DAN-152, DAN-177, DAN-015, DAN-017, DAN-124, DAN-131, DAN-028
- justificativa: 
- aprofundar DAN-152: `malicious npm package access token exfiltration root cause fix` — É o único incidente sobre pacote malicioso publicado em registro público (npm) sem autorização, semelhante ao pacote não publicado enviando tokens para fora; não menciona exfiltração de tokens especificamente.
  - DAN-152 (llm) [Timeline] 0.754: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Summary] 0.718: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-241 (esperado: DAN-152)

- busca inicial: DAN-152, DAN-009, DAN-015, DAN-177, DAN-140, DAN-017, DAN-122, DAN-131, DAN-175, DAN-204
- justificativa: 
- aprofundar DAN-152: `npm account compromise malicious package publication root cause fix` — Atacante comprometeu conta npm de mantenedor e publicou pacotes maliciosos; bate com versão não publicada enviando tokens, embora sejam pacotes novos e não versões de pacote existente.
- aprofundar DAN-122: `malicious Maven packages JCenter impersonation attack root cause fix` — Pacotes maliciosos em repositório Maven via ataque de personificação; bate com compromisso de supply chain de pacotes, embora seja Maven e não npm e os pacotes tenham ficado por mais de um ano.
- aprofundar DAN-177: `GitHub token leak Jenkins unauthorized git push root cause fix` — Token vazado permitiu push não autorizado em repositórios; bate com publicação não autorizada via credenciais roubadas, embora seja git push e não versão de pacote em registry.
  - DAN-152 (llm) [Summary] 0.749: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.746: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.747: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.661: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-177 (llm) [sem seção] 0.725: On 31st July 2018 a security researcher identified a GitHub personal access token with recently elevated scopes was leaked from Homebrew’s Jenkins that gave them access to git push on Homebrew/brew an
  - DAN-177 (llm) [What was impacted] 0.618: ## What was impacted  GitHub Support was contacted and they verified the relevant token had not been used to perform any pushes to Homebrew/brew or Homebrew/homebrew-core during the period of elevated
  - DAN-177 (causa) [What we’re doing about it] 0.231: ## What we’re doing about it  - We have for several years enabled 2FA and third party application restrictions for the entire Homebrew GitHub organisation. This was also recommended by the security re

## q-242 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-109, DAN-026, DAN-129, DAN-145, DAN-106, DAN-009, DAN-008, DAN-067, DAN-016
- justificativa: 
- aprofundar DAN-011: `database permissions bot detection file output limit systemwide outage fix rollback` — É um provedor de CDN com pane sistêmica após mudança que se propagou pela rede, parecido com a CDN caindo mundialmente, embora a causa seja banco de dados/bot-detection e não cache.
- aprofundar DAN-009: `service tokens code release error CDN control plane outage fix rollback` — Atingiu serviços incluindo a CDN por erro ao liberar código, semelhança com pane repentina na CDN, mas envolve tokens de serviço e não apenas cache.
- aprofundar DAN-008: `Tiered Cache system change 530 error outage fix rollback blind spot tests` — É pane na camada de cache da CDN (Tiered Cache) após mudança, com falhas de requisição, mas impacto foi parcial (5%) e não mundial como no incidente atual.
  - DAN-011 (llm) [Remediation and follow-up steps] 0.595: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [The query behaviour change] 0.591: ### The query behaviour change  ``` SELECT   name,   type FROM system.columns WHERE   table = 'http_requests_features' order by name; ``` Note how the query does not filter for the database name. With
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-009 (llm) [sem seção] 0.673: Several Cloudflare services became unavailable for 121 minutes on January 24, 2023 due to an error releasing code that manages service tokens. The incident degraded a wide range of Cloudflare products
  - DAN-009 (llm) [Incident Timeline] 0.656: ### Incident Timeline  *All Timestamps are UTC*  At 2023-01-24 16:55 the Access engineering team initiated the release that inadvertently began to overwrite service token metadata, causing the inciden
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [How did we fix the issue?] 0.483: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-008 (llm) [sem seção] 0.75: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.7: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac

## q-243 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210, DAN-209, DAN-205, DAN-129, DAN-109, DAN-145
- justificativa: 
- aprofundar DAN-011: `bot detection permissions database file limit systemwide outage root cause fix` — É um CDN (Cloudflare) com pane mundial causada por mudança de permissão que gerou arquivo acima do limite, muito parecido com pane mundial de CDN, mas o gatilho é banco de dados de bot-detection, não cache.
- aprofundar DAN-008: `tiered cache change 530 error root cause remediation` — É pane parcial do Cloudflare Tiered Cache gerando erros 530, componente de CDN parecido, mas impacto foi parcial (5%) e não mundial.
- aprofundar DAN-067: `control plane analytics outage power failure remediation` — É pane na infraestrutura Cloudflare, mas por falha de energia em data center e afeta control plane/analytics, não diretamente o CDN mundial.
  - DAN-011 (llm) [Remediation and follow-up steps] 0.63: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [Memory preallocation] 0.608: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-008 (llm) [sem seção] 0.747: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.678: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-067 (llm) [Lessons and Remediation] 0.752: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [sem seção] 0.733: Beginning on Thursday, November 2, 2023, at 11:43 UTC Cloudflare's control plane and analytics services experienced an outage. The control plane of Cloudflare consists primarily of the customer-facing
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-244 (esperado: DAN-165)

- busca inicial: DAN-165, DAN-195, DAN-231, DAN-124, DAN-184, DAN-221, DAN-033, DAN-183, DAN-164, DAN-001
- justificativa: 
- aprofundar DAN-165: `repeated emails batch cron job non-atomic root cause fix` — O DAN-165 descreve exatamente o sintoma atual: e-mail enviado mais de 20 vezes para as mesmas pessoas por um batch cron job com operação não atômica que não marcava os usuários como atendidos até terminar o lote. Bate com o componente (mail), o gatilho (envio em lote) e o sintoma (repetição de e-mails). Não há outro incidente na lista sobre e-mails repetidos.
  - DAN-165 (llm) [So what was the bug?] 0.668: ## So what was the bug?  In the App Engine datastore, we have an object called a "notification". That notification has a "status" property, which takes on the following values: "Waiting", "Sending", a
  - DAN-165 (llm) [sem seção] 0.585: A few hours ago, the automated email system for Code Jam went a little bit crazy. I'll write about the technical details below, but the short version is that it sent an email titled "Registration Now 
  - DAN-165 (causa) [Why did I get the repeated email at all?] 0.284: ## Why did I get the repeated email at all?  We sent the notification email to users who registered for Code Jam 2013, checked the box saying "I would like to receive email notifying me about the next
  - DAN-165 (correcao) [Why does Code Jam have its own email system?] 0.272: ## Why does Code Jam have its own email system?  To automatically identify the users who should get an email based on Code Jam-specific properties (such as scores, booleans in user profiles, and regis

## q-245 (esperado: DAN-165)

- busca inicial: DAN-165, DAN-183, DAN-231, DAN-124, DAN-195, DAN-033, DAN-221, DAN-164, DAN-184, DAN-016
- justificativa: 
- aprofundar DAN-165: `repeated email batch cron job atomic mark sent fix` — O incidente atual é sobre emails duplicados dezenas de vezes. DAN-165 é o único com mesma falha (emails repetidos), mesmo componente (sistema de mail) e mesmo gatilho (batch job não atômico que não marca como enviado até terminar).
  - DAN-165 (llm) [So what was the bug?] 0.698: ## So what was the bug?  In the App Engine datastore, we have an object called a "notification". That notification has a "status" property, which takes on the following values: "Waiting", "Sending", a
  - DAN-165 (llm) [sem seção] 0.57: A few hours ago, the automated email system for Code Jam went a little bit crazy. I'll write about the technical details below, but the short version is that it sent an email titled "Registration Now 
  - DAN-165 (causa) [Why did I get the repeated email at all?] 0.284: ## Why did I get the repeated email at all?  We sent the notification email to users who registered for Code Jam 2013, checked the box saying "I would like to receive email notifying me about the next
  - DAN-165 (correcao) [Why does Code Jam have its own email system?] 0.272: ## Why does Code Jam have its own email system?  To automatically identify the users who should get an email based on Code Jam-specific properties (such as scores, booleans in user profiles, and regis

## q-246 (esperado: DAN-170)

- busca inicial: DAN-170, DAN-198, DAN-126, DAN-200, DAN-065, DAN-103, DAN-191, DAN-035, DAN-154, DAN-116
- justificativa: 
- aprofundar DAN-170: `GPS GLONASS incorrect positions update rollback not fixed fix` — O incidente envolve atualização ruim que causou posições incorretas de satélites GPS/GLONASS e um rollback que não resolveu, exatamente o padrão do incidente atual; nenhum outro item da lista trata de satélites ou navegação.
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.737: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Bad Broadcast Messages (resulting in position errors up to about ±200km) were sent out     starting April 1, 2014, 21:00; Fi
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.732: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Understood:    The GNONASS April 1st event was not a joke.    The failure was caused by wrong Broadcast Ephemerides   … p
  - DAN-170 (causa) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.337: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol of April 1). Some receivers unaffected, some stopped tracking GLONASS after 9h p.m. (red line), some even stopped GPS trackin
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.349: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  From CODE Analysis protocol: Number of GLONASS observations    reduced by about 10% on April 2nd.  this is why the IGS post
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.307: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Real-time GNSS Service   -timeIGSOpen Data       •   Observations & derived products freely available       •   Streaming da

## q-247 (esperado: DAN-170)

- busca inicial: DAN-170, DAN-126, DAN-050, DAN-198, DAN-035, DAN-103, DAN-065, DAN-200, DAN-154, DAN-074
- justificativa: 
- aprofundar DAN-170: `incorrect satellite positions update rollback did not fix root cause` — O incidente descreve posições incorretas de satélites após uma atualização e o rollback não corrigiu, exatamente como o incidente atual; difere apenas no sistema específico (GPS/GLONASS).
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.636: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  From CODE Analysis protocol: Number of GLONASS observations    reduced by about 10% on April 2nd.  this is why the IGS post
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.63: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Bad Broadcast Messages (resulting in position errors up to about ±200km) were sent out     starting April 1, 2014, 21:00; Fi
  - DAN-170 (causa) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.358: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Understood:    The GNONASS April 1st event was not a joke.    The failure was caused by wrong Broadcast Ephemerides   … p
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.318: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol of April 1). Some receivers unaffected, some stopped tracking GLONASS after 9h p.m. (red line), some even stopped GPS trackin
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.307: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Real-time GNSS Service   -timeIGSOpen Data       •   Observations & derived products freely available       •   Streaming da

## q-248 (esperado: DAN-180)

- busca inicial: DAN-180, DAN-164, DAN-191, DAN-129, DAN-209, DAN-222, DAN-048, DAN-181, DAN-107, DAN-102
- justificativa: 
- aprofundar DAN-180: `ingest system down repeatedly cache delays root cause fix` — O resumo menciona exatamente 'ingest system went down repeatedly' por mais de oito horas, mesmo padrão do incidente atual, embora a causa citada seja cache (Shepherd).
- aprofundar DAN-222: `Cassandra cluster crash ingestion producers blocking queue fix` — Envolve ingestão de dados em cluster que falha e bloqueia produtores em filas, semelhante à instabilidade de ingestão, mas o componente é um banco de dados, não o ingestor em si.
- aprofundar DAN-181: `total outage data processing root cause remediation fix` — Outage total da Honeycomb impediu processamento de dados, mas foi um evento único de uma hora, não ingestão caindo repetidamente por horas.
  - DAN-180 (llm) [The events] 0.661: ## The events  We then forced a scale-down of Shepherds to disrupt the pattern, but the autoscaler decided we had too few Shepherds—crashlooping demands a lot of CPU—and instead added more of them. We
  - DAN-180 (llm) [The events] 0.64: ## The events  We decided to do more aggressive sampling in an attempt to stabilize the Refinery cluster by keeping less data. This seemed to work, but sampling aggressively was impacting our ability 
  - DAN-180 (causa) [On causal confusion] 0.541: ### On causal confusion  At one point, our understanding of the situation looked like the following diagram, where orange denotes places where we observed unusual behavior:  Ingestion volume was highe
  - DAN-180 (correcao) [Analysis] 0.509: ## Analysis  This incident revealed areas where we had built mental models of components that proved inaccurate during incidents, and could even clash with each other. This was an opportunity to contr
  - DAN-180 (correcao) [On the solution found] 0.457: ### On the solution found  We still don’t know what triggered all of this, we just know that it was fixed by the cache pre-fill. We are confident the fix worked and is effective because it’s been thro
  - DAN-222 (llm) [sem seção] 0.667: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (llm) [sem seção] 0.657: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (causa) [sem seção] 0.457: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl
  - DAN-181 (llm) [**Corrective actions**] 0.612: ### **Corrective actions**  For the duration of the outage, no new data could be ingested. If our users or customers did not buffer this data to disk somewhere to replay it later, it is gone for good.
  - DAN-181 (llm) [**The incident**] 0.59: ## **The incident**  The moment we understood this, we wrote a command to restart our query engine’s cluster without interfering with other critical features (querying and alerting). But right before 
  - DAN-181 (causa) [**How a database dies**] 0.525: ### **How a database dies**  The core of the database failure was a deadlock in MySQL’s internals. There’s no clear path on how we specifically got there, but since this is a concurrency issue, we thi
  - DAN-181 (correcao) [**Contributing factors**] 0.535: ### **Contributing factors**  Preventing a bug by switching to the old infrastructure set up the stage. We suspended deployments during the investigation, which prevented restarts accidentally making 
  - DAN-181 (correcao) [**Conclusion**] 0.499: ## **Conclusion**  While we wish such incidents wouldn’t happen, we know that we’ll have to manage them—no matter how hard we plan for them. One of the most intriguing themes that came up from many of

## q-249 (esperado: DAN-180)

- busca inicial: DAN-180, DAN-209, DAN-181, DAN-222, DAN-164, DAN-048, DAN-208, DAN-191, DAN-067, DAN-217
- justificativa: 
- aprofundar DAN-180: `ingest system repeatedly down cache delays root cause fix` — O resumo menciona exatamente um sistema de ingest que caiu repetidamente por mais de oito horas, igual ao incidente atual, mas não detalha a causa nem a correção.
- aprofundar DAN-222: `Cassandra cluster crash ingest message bus producers blocking fix` — Envolve ingestão de dados em cluster que falhou e bloqueou produtores, similar a um pipeline de ingestão instável, embora o componente seja diferente.
- aprofundar DAN-181: `total outage data processing root cause remediation Honeycomb` — É uma pane total da Honeycomb que impediu processamento de dados, mesma empresa e plataforma de dados, mas não menciona especificamente o sistema de ingest.
  - DAN-180 (llm) [The events] 0.655: ## The events  We then forced a scale-down of Shepherds to disrupt the pattern, but the autoscaler decided we had too few Shepherds—crashlooping demands a lot of CPU—and instead added more of them. We
  - DAN-180 (llm) [The events] 0.644: ## The events  We decided to do more aggressive sampling in an attempt to stabilize the Refinery cluster by keeping less data. This seemed to work, but sampling aggressively was impacting our ability 
  - DAN-180 (causa) [On causal confusion] 0.541: ### On causal confusion  At one point, our understanding of the situation looked like the following diagram, where orange denotes places where we observed unusual behavior:  Ingestion volume was highe
  - DAN-180 (correcao) [Analysis] 0.509: ## Analysis  This incident revealed areas where we had built mental models of components that proved inaccurate during incidents, and could even clash with each other. This was an opportunity to contr
  - DAN-180 (correcao) [On the solution found] 0.457: ### On the solution found  We still don’t know what triggered all of this, we just know that it was fixed by the cache pre-fill. We are confident the fix worked and is effective because it’s been thro
  - DAN-222 (llm) [sem seção] 0.65: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (llm) [sem seção] 0.637: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (causa) [sem seção] 0.457: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl
  - DAN-181 (llm) [sem seção] 0.726: On July 25th, 2023, we experienced a total Honeycomb outage. It impacted all user-facing components from 1:40 p.m. UTC to 2:48 p.m. UTC, during which no data could be processed or accessed.  This outa
  - DAN-181 (llm) [**Corrective actions**] 0.687: ### **Corrective actions**  For the duration of the outage, no new data could be ingested. If our users or customers did not buffer this data to disk somewhere to replay it later, it is gone for good.
  - DAN-181 (causa) [**How a database dies**] 0.525: ### **How a database dies**  The core of the database failure was a deadlock in MySQL’s internals. There’s no clear path on how we specifically got there, but since this is a concurrency issue, we thi
  - DAN-181 (correcao) [**Contributing factors**] 0.535: ### **Contributing factors**  Preventing a bug by switching to the old infrastructure set up the stage. We suspended deployments during the investigation, which prevented restarts accidentally making 
  - DAN-181 (correcao) [**Conclusion**] 0.499: ## **Conclusion**  While we wish such incidents wouldn’t happen, we know that we’ll have to manage them—no matter how hard we plan for them. One of the most intriguing themes that came up from many of

## q-250 (esperado: DAN-183)

- busca inicial: DAN-183, DAN-195, DAN-134, DAN-096, DAN-148, DAN-101, DAN-133, DAN-080, DAN-094, DAN-129
- justificativa: 
- aprofundar DAN-183: `GKE Dataplane V2 anetd CPU packet drop postgres memcached timeout fix` — É o único que combina migração para nuvem (Google Cloud), timeouts de conexão Postgres, erros i/o timeout no memcached e ajuste insuficiente de pool de conexões, exatamente como o incidente atual; a causa raiz apontada (anetd/GKE Dataplane V2 saturado) ainda não foi confirmada no caso em andamento.
  - DAN-183 (llm) [OK, so what’s actually going on?] 0.691: ## OK, so what’s actually going on?  This revelation suggests that this isn't a process-local issue. What we mean by this is the fact that we were having network issues between our Kubernetes node and
  - DAN-183 (llm) [Meanwhile, a few desks away] 0.646: ## Meanwhile, a few desks away  While all this had been going on, another unrelated issue had cropped up. Thanks to an accidental database join, we’d been making thousands of duplicate network calls t
  - DAN-183 (causa) [Meanwhile, a few desks away] 0.461: ## Meanwhile, a few desks away  This was only happening for a tiny handful of requests among hundreds of thousands, with seemingly no other consistent pattern when it came to which users, organization
  - DAN-183 (correcao) [Clouds, caches and connection conundrums] 0.391: ## Clouds, caches and connection conundrums  Ben Wheatley  September 26, 2023  13 min read  We recently moved our infrastructure fully into Google Cloud. Most things went very smoothly, but there was 
  - DAN-183 (correcao) [OK, so what’s actually going on?] 0.364: ## OK, so what’s actually going on?  If you think about it, it all starts to line up pretty much perfectly with what we’d seen and done up until this point:  - We mostly fixed the DB timeouts by fixin

## q-251 (esperado: DAN-183)

- busca inicial: DAN-183, DAN-101, DAN-148, DAN-096, DAN-195, DAN-134, DAN-133, DAN-129, DAN-080, DAN-156
- justificativa: 
- aprofundar DAN-183: `root cause fix GKE Dataplane V2 anetd CPU packet drop memcached postgres timeout` — Mesmo cenário: mudança de nuvem, spikes de Postgres connection timeouts e memcached i/o timeout, tuning de pool ajudou só parcialmente.
- aprofundar DAN-101: `root cause fix connection pool exhaustion transaction Slack modal` — Também tem timeouts de conexão e tuning insuficiente do pool, mas não envolve memcached nem mudança de nuvem.
- aprofundar DAN-133: `root cause fix thread connection pool MongoDB JVM upgrade` — Envolve tuning de pools e outages em cascata, mas o componente é MongoDB/JVM, não Postgres mais memcached.
  - DAN-183 (llm) [OK, so what’s actually going on?] 0.721: ## OK, so what’s actually going on?  This revelation suggests that this isn't a process-local issue. What we mean by this is the fact that we were having network issues between our Kubernetes node and
  - DAN-183 (llm) [Meanwhile, a few desks away] 0.643: ## Meanwhile, a few desks away  While all this had been going on, another unrelated issue had cropped up. Thanks to an accidental database join, we’d been making thousands of duplicate network calls t
  - DAN-183 (causa) [Meanwhile, a few desks away] 0.461: ## Meanwhile, a few desks away  This was only happening for a tiny handful of requests among hundreds of thousands, with seemingly no other consistent pattern when it came to which users, organization
  - DAN-183 (correcao) [Clouds, caches and connection conundrums] 0.391: ## Clouds, caches and connection conundrums  Ben Wheatley  September 26, 2023  13 min read  We recently moved our infrastructure fully into Google Cloud. Most things went very smoothly, but there was 
  - DAN-183 (correcao) [OK, so what’s actually going on?] 0.364: ## OK, so what’s actually going on?  If you think about it, it all starts to line up pretty much perfectly with what we’d seen and done up until this point:  - We mostly fixed the DB timeouts by fixin
  - DAN-101 (llm) [sem seção] 0.69: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (llm) [sem seção] 0.615: Originally, we would receive this event from Slack, and within the lifetime of that HTTP request, we’d perform any responses we needed to, e.g. offering to attach a GitHub link that a user has just po
  - DAN-101 (causa) [sem seção] 0.433: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (correcao) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-101 (correcao) [sem seção] 0.381: It wasn’t until a few days later that we realised this was the root of our problems. As the timeouts were intermittent and didn’t occur every day, it took a little while to confirm the issue. But, it’
  - DAN-133 (llm) [Incident Report] 0.733: ## Incident Report  Around the same time, we updated many services to a new minor version of the JVM to pick up security changes. This update also included improvements for docker-awareness enabled by
  - DAN-133 (llm) [Incident Report] 0.668: ## Incident Report  April 10, 2019 at 13:25 UTC we were alerted to sharp increases in multiple queues responsible for job and workflow processing. Our monitoring of MongoDB showed some issues, but not
  - DAN-133 (causa) [Incident Report] 0.453: ## Incident Report  Between March 26 and April 10, 2019, our platform experienced instability and downtime primarily due to issues with the datastore backing our builds queue. These datastore issues r
  - DAN-133 (correcao) [Incident Report] 0.533: ## Incident Report  Ultimately, refactoring the way we store and access portions of our data set in MongoDB will reduce load. Improving our data access and storage at the application level is one of o
  - DAN-133 (correcao) [Incident Report] 0.444: ## Incident Report  Perhaps most importantly, MongoDB support pointed us at the `tcmalloc.spinlock_total_delay_ns` MongoDB stat. This stat correlates with the time spent on database operations blocked

## q-252 (esperado: DAN-186)

- busca inicial: DAN-186, DAN-164, DAN-120, DAN-043, DAN-048, DAN-011, DAN-156, DAN-094, DAN-195, DAN-226
- justificativa: 
- aprofundar DAN-186: `hosted database limit hit migration new database recovery` — é o mais parecido: banco de dados hospedado atingiu um limite e exigiu migração para um novo banco, mas não confirma se o limite foi de armazenamento que impediu escrita
- aprofundar DAN-120: `integer limit read only outage fix migration` — bate porque um limite do banco deixou o serviço somente leitura (sem escrita); não bate porque foi limite de inteiro, não de banco hospedado
- aprofundar DAN-195: `transaction ID wraparound outage fix vacuum Postgres` — bate porque um limite do banco causou outage parcial; não corresponde a banco hospedado ou limite de armazenamento que impede escrita
  - DAN-186 (llm) [**Full service restoration**] 0.684: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma
  - DAN-186 (llm) [**Data restoration**] 0.673: # **Data restoration**  Once the service was back up and the data dumps completed, the next step was to import all of the dumps into an instance that wasn’t subject to the 2TB file size limit. We work
  - DAN-186 (causa) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (correcao) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (correcao) [**Prevention**] 0.407: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-120 (llm) [sem seção] 0.669: Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, 
  - DAN-120 (llm) [sem seção] 0.563: We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998
  - DAN-120 (causa) [sem seção] 0.427: Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop using our status.basecamp.com updates and a play-by-play record on our blog. We can’t promise to be perfec
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.806: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.675: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg

## q-253 (esperado: DAN-186)

- busca inicial: DAN-186, DAN-164, DAN-120, DAN-094, DAN-043, DAN-048, DAN-156, DAN-147, DAN-011, DAN-096
- justificativa: 
- aprofundar DAN-186: `hosted database limit reached migration new database recovery` — Bate por mencionar limite atingido em banco de dados hospedado; não bate porque a resolução foi migração longa, não ajuste de limite.
- aprofundar DAN-120: `database integer limit read-only outage fix migration` — Bate por limite do banco deixando serviço somente leitura; não bate porque é limite inteiro específico, não limite genérico de hosted DB.
- aprofundar DAN-147: `database capacity request queue cascading failure fix` — Bate por capacidade insuficiente do banco sob carga; não bate porque é falha em cascata por fila de requisições, não limite de hosted DB.
  - DAN-186 (llm) [**Full service restoration**] 0.684: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma
  - DAN-186 (llm) [**Data restoration**] 0.673: # **Data restoration**  Once the service was back up and the data dumps completed, the next step was to import all of the dumps into an instance that wasn’t subject to the 2TB file size limit. We work
  - DAN-186 (causa) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (correcao) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (correcao) [**Prevention**] 0.407: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-120 (llm) [sem seção] 0.699: Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, 
  - DAN-120 (llm) [sem seção] 0.553: We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998
  - DAN-120 (causa) [sem seção] 0.427: Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop using our status.basecamp.com updates and a play-by-play record on our blog. We can’t promise to be perfec
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.59: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.58: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste

## q-254 (esperado: DAN-188)

- busca inicial: DAN-188, DAN-080, DAN-195, DAN-102, DAN-164, DAN-112, DAN-109, DAN-147, DAN-048, DAN-101
- justificativa: 
- aprofundar DAN-188: `PostgreSQL metadata lock transaction wraparound global lock fix` — Operações de serviço bloqueadas por lock em metadados Postgres, igual ao atual; difere por envolver wraparound e query de lock global.
- aprofundar DAN-195: `Postgres transaction ID wraparound outage root cause fix recovery` — Wraparound de transaction ID no Postgres causou outage prolongado, similar ao travamento por horas, mas não detalha lock waiting em consultas.
- aprofundar DAN-102: `PGAudit hung critical locks Postgres migration fix restart` — Extensão travada segurando locks críticos bloqueou operações Postgres, similar ao bloqueio por lock, mas envolve PGAudit e upgrade recente.
  - DAN-188 (llm) [Summary of Root Cause] 0.648: ### Summary of Root Cause  In summary:  - All Manta operations touch our sharded, PostgreSQL-backed metadata tier. - During the event, one of the shard databases had all queries on our primary table b
  - DAN-188 (llm) [Subsequent analysis] 0.64: ### Subsequent analysis  #### More background  To fully understand what happened, a little more background on PostgreSQL is required.  PostgreSQL's implementation of Multi-Version Concurrency Control 
  - DAN-188 (causa) [Root cause analysis] 0.545: ## Root cause analysis  For transparency, we've included a lot of detail here about how the incident proceeded. If you're interested in more of a summary, skip to the Summary of Root Cause section bel
  - DAN-188 (correcao) [Closing] 0.517: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working hard to prevent an issue like this from happ
  - DAN-188 (correcao) [The problem] 0.482: ### The problem  We observed the autovacuum scan the full table and all of its indexes, and then do the same thing again. After several hours, it successfully completed and updated the "last\_autovacu
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.828: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.633: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg
  - DAN-102 (llm) [sem seção] 0.644: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [sem seção] 0.603: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily

## q-255 (esperado: DAN-188)

- busca inicial: DAN-188, DAN-080, DAN-195, DAN-109, DAN-112, DAN-164, DAN-102, DAN-181, DAN-101, DAN-226
- justificativa: 
- aprofundar DAN-188: `PostgreSQL lock wraparound maintenance global lock fix` — Storage operations bloqueadas por lock no metadata do Postgres, igual ao atual; pode ou não envolver wraparound.
- aprofundar DAN-195: `transaction ID wraparound outage root cause fix vacuum` — Envolve wraparound de transaction ID no Postgres causando outage prolongado; não se sabe se o atual é wraparound.
- aprofundar DAN-102: `PGAudit migration lock hang fix restart PostgreSQL` — Extensão travada segurando locks críticos bloqueou operações do banco; não se sabe se envolve storage metadata.
  - DAN-188 (llm) [Back to the incident] 0.641: #### Back to the incident  We don't know if this is the first time we saw this, but based on our traffic patterns, we would have expected to see wraparaound autovacuums a few times on each shard alrea
  - DAN-188 (llm) [Subsequent analysis] 0.622: ### Subsequent analysis  #### More background  To fully understand what happened, a little more background on PostgreSQL is required.  PostgreSQL's implementation of Multi-Version Concurrency Control 
  - DAN-188 (causa) [Root cause analysis] 0.545: ## Root cause analysis  For transparency, we've included a lot of detail here about how the incident proceeded. If you're interested in more of a summary, skip to the Summary of Root Cause section bel
  - DAN-188 (correcao) [Closing] 0.517: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working hard to prevent an issue like this from happ
  - DAN-188 (correcao) [The problem] 0.482: ### The problem  We observed the autovacuum scan the full table and all of its indexes, and then do the same thing again. After several hours, it successfully completed and updated the "last\_autovacu
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.712: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.617: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg
  - DAN-102 (llm) [sem seção] 0.645: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [sem seção] 0.609: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily

## q-256 (esperado: DAN-189)

- busca inicial: DAN-189, DAN-103, DAN-066, DAN-146, DAN-067, DAN-064, DAN-070, DAN-106, DAN-210, DAN-191
- justificativa: 
- aprofundar DAN-189: `operator reboot maintenance tool rebooted all servers root cause fix` — Mesmo gatilho: operador usou ferramenta de reboot para manutenção e reiniciou acidentalmente todos os servidores do datacenter; difere pela causa específica (flag -n ausente) e pelo provedor (Joyent).
- aprofundar DAN-106: `human error routine networking upgrade outage root cause fix` — Erro humano em operação de rotina causou pane ampla, mas não envolve reinicialização em massa de servidores por ferramenta de manutenção.
- aprofundar DAN-146: `scheduled OS upgrade machines wiped outage root cause fix` — Atualização agendada do sistema operacional afetou muitas máquinas, mas não envolve ferramenta de reinicialização para manutenção executada por operador.
  - DAN-189 (llm) [What Happened?] 0.657: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.57: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.475: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.459: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.353: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-146 (llm) [sem seção] 0.575: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [sem seção] 0.467: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri

## q-257 (esperado: DAN-189)

- busca inicial: DAN-189, DAN-146, DAN-103, DAN-066, DAN-064, DAN-067, DAN-070, DAN-073, DAN-208, DAN-068
- justificativa: 
- aprofundar DAN-189: `reboot tool missing flag all servers datacenter input validation fix` — O operador usou uma ferramenta para reiniciar poucos servidores em manutenção e acabou reiniciando todo o datacenter, igual ao incidente atual, embora o componente seja o us-east-1 da Joyent.
  - DAN-189 (llm) [What Happened?] 0.594: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.57: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-258 (esperado: DAN-194)

- busca inicial: DAN-194, DAN-156, DAN-133, DAN-164, DAN-147, DAN-066, DAN-211, DAN-048, DAN-190, DAN-094
- justificativa: 
- aprofundar DAN-194: `secondary MongoDB overloaded troubleshooting change primary traffic overload fix` — Descreve exatamente o mesmo cenário: secundários do MongoDB sobrecarregados e, durante diagnóstico, mudança que redirecionou todo o tráfego secundário para o primário, sobrecarregando-o também.
  - DAN-194 (llm) [Website Intermittent Timeouts] 0.634: ## Website Intermittent Timeouts  ## Postmortem  ## Summary  On January 12th at 14:09 UTC, our engineers began responding to alerts for our click / open tracking services and primary MongoDB clusters 
  - DAN-194 (llm) [Summary] 0.62: ## Summary  After review of our MongoDB configurations, we deployed limits on the number of connections our services could establish to our primary MongoDB server. We prepared these changes and began 
  - DAN-194 (causa) [Corrective Actions] 0.357: ## Corrective Actions  - Deployment of Redundant Tracking Infrastructure (Complete) - Our tracking services have previously operated out of a single region. As part of previously planned infrastructur
  - DAN-194 (correcao) [Resolved] 0.444: ## Resolved  This incident has been resolved.  Posted Jan 12, 2017 - 15:10 PST  ## Monitoring  Mailgun engineers have made a series of changes to our system, which have improved the performance and st
  - DAN-194 (correcao) [Identified] 0.327: ## Identified  We’re seeing improved performance and stability from our core API & SMTP services at this time. The engineering team is continuing to work to completely resolve the issue.  Posted Jan 1

## q-259 (esperado: DAN-194)

- busca inicial: DAN-194, DAN-156, DAN-133, DAN-164, DAN-147, DAN-048, DAN-066, DAN-130, DAN-096, DAN-094
- justificativa: 
- aprofundar DAN-194: `secondary MongoDB traffic primary overload troubleshooting change root cause fix` — É o único incidente que corresponde exatamente ao atual: secundários do MongoDB sobrecarregados e uma mudança durante o troubleshooting que enviou todo o tráfego secundário ao primário, sobrecarregando-o também.
  - DAN-194 (llm) [Website Intermittent Timeouts] 0.669: ## Website Intermittent Timeouts  ## Postmortem  ## Summary  On January 12th at 14:09 UTC, our engineers began responding to alerts for our click / open tracking services and primary MongoDB clusters 
  - DAN-194 (llm) [Summary] 0.635: ## Summary  After review of our MongoDB configurations, we deployed limits on the number of connections our services could establish to our primary MongoDB server. We prepared these changes and began 
  - DAN-194 (causa) [Corrective Actions] 0.357: ## Corrective Actions  - Deployment of Redundant Tracking Infrastructure (Complete) - Our tracking services have previously operated out of a single region. As part of previously planned infrastructur
  - DAN-194 (correcao) [Resolved] 0.444: ## Resolved  This incident has been resolved.  Posted Jan 12, 2017 - 15:10 PST  ## Monitoring  Mailgun engineers have made a series of changes to our system, which have improved the performance and st
  - DAN-194 (correcao) [Identified] 0.327: ## Identified  We’re seeing improved performance and stability from our core API & SMTP services at this time. The engineering team is continuing to work to completely resolve the issue.  Posted Jan 1

## q-260 (esperado: DAN-197)

- busca inicial: DAN-066, DAN-106, DAN-067, DAN-029, DAN-209, DAN-220, DAN-154, DAN-205, DAN-008, DAN-133
- justificativa: 
- aprofundar DAN-106: `Amazon EC2 RDS outage human error networking upgrade root cause fix` — Ambos envolvem falha súbita na infraestrutura de um provedor de nuvem afetando chamadas de API sem mudança do cliente; difere porque DAN-106 foi desencadeado por upgrade de rede do provedor.
- aprofundar DAN-205: `PagerDuty outage cloud deployment connectivity latency peering point fix` — Ambos envolvem perda inesperada de conectividade com infraestrutura de nuvem sem alteração no lado do cliente; difere porque DAN-205 afetou quorum e notificações, não uma API genérica de nuvem.
- aprofundar DAN-066: `Cloudflare Byzantine failure switch misbehavior API availability fix` — Ambos envolvem perda súbita de disponibilidade de API por mau comportamento de infraestrutura subjacente; difere porque DAN-066 é a própria API/dashboard da Cloudflare, não um provedor externo chamado pelo nosso serviço.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.711: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  At 12:47 AM PDT on April 21st, a network change was performed as part of our normal AWS scaling activities in a s
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.703: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-205 (llm) [The Outage] 0.826: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.794: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.678: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (llm) [sem seção] 0.673: *An analysis of the Cloudflare API availability incident on 2020-11-02*  When we review design documents at Cloudflare, we are always on the lookout for Single Points of Failure (SPOFs). Eliminating t
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust

## q-261 (esperado: DAN-197)

- busca inicial: DAN-067, DAN-066, DAN-220, DAN-154, DAN-029, DAN-008, DAN-133, DAN-106, DAN-205, DAN-209
- justificativa: 
- aprofundar DAN-066: `Byzantine failure switch root cause API outage fix recovery` — Bate: falha na API de provedor externo sem mudança do nosso lado (switch misbehavior na infra da Cloudflare). Não bate: é problema da própria Cloudflare, não de um cliente chamando API de terceiros.
- aprofundar DAN-067: `data center power failure API calls thundering herd rate limit recovery` — Bate: chamadas de API falhando devido a falha externa de infraestrutura (energia no data center), sem mudança do nosso lado. Não bate: o foco está na recuperação com rate limit, não na causa raiz da falha de API.
- aprofundar DAN-205: `cloud deployment connectivity high latency peering point network instability outage` — Bate: problemas de conectividade entre deployments em nuvem causando falhas, sem mudança do nosso lado. Não bate: é sobre quorum e notificações, não exatamente chamadas de API para provedor externo.
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.635: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (llm) [The Dashboard] 0.611: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-067 (llm) [Disaster Recovery] 0.726: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.649: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-205 (llm) [The Outage] 0.727: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.699: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-262 (esperado: DAN-200)

- busca inicial: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073, DAN-189, DAN-146, DAN-210, DAN-043, DAN-200
- justificativa: 
- aprofundar DAN-200: `system resets days after landing VxWorks priority inversion fix patch` — O incidente envolve reinicializações do computador de bordo (system resets) dias após o pouso/entrada em operação, exatamente como o atual, embora em uma sonda marciana.
- aprofundar DAN-198: `rendezvous radar CPU load computer restart design flaw fix` — Também trata de reinicialização do computador de bordo, mas por excesso de carga de CPU durante o pouso lunar, não dias após o início da operação.
  - DAN-200 (llm) [THE FAILURE] 0.638: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.589: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.601: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.577: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.379: | | \* \* \* | | By now the area on the second floor of 75 Cambridge Parkway where we monitored missions had been moved to a larger space, but on July 20, 1969 the room was crowded despite efforts to 

## q-263 (esperado: DAN-200)

- busca inicial: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-073, DAN-146, DAN-106, DAN-069, DAN-066
- justificativa: 
- aprofundar DAN-200: `Mars Pathfinder system resets priority inversion VxWorks patch fix` — Bate com computador de bordo reiniciando dias depois de entrar em operação; não bate porque é uma sonda Mars, não um avião.
- aprofundar DAN-198: `Apollo 11 rendezvous radar CPU load computer restart fix` — Bate com reinício de computador de bordo por excesso de carga; não bate porque ocorre durante pouso lunar, não dias após operação.
  - DAN-200 (llm) [HOW WE FOUND IT] 0.659: ## HOW WE FOUND IT  The software that flies on Mars Pathfinder has several debug features within it that are used in the lab but are not used on the flight spacecraft (not used because some of them pr
  - DAN-200 (llm) [THE FAILURE] 0.631: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
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
- aprofundar DAN-204: `Redis cache corrupted queue cross-user data leak billing info root cause fix` — Bate exatamente: usuários veem dados de outros usuários, incluindo billing info, por causa de fila de requisições corrompida. Não bate o componente (Redis vs atual desconhecido).
- aprofundar DAN-058: `misconfigured backup identifiers data leak free tier databases root cause fix` — Bate parcialmente: data leak para clientes por configuração incorreta de identificadores. Não bate: não é usuário vendo dado de outro usuário em tempo real.
- aprofundar DAN-136: `parser bug memory leak private information cookies tokens root cause fix` — Bate parcialmente: dados privados expostos a usuários por bug. Não bate: é memória de edge servers, não filas de requisição.
  - DAN-204 (llm) [Technical details] 0.62: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.609: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-058 (llm) [What happened?] 0.802: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.754: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-136 (llm) [Parsing and modifying HTML on the fly] 0.691: ## Parsing and modifying HTML on the fly  It turned out that the underlying bug that caused the memory leak had been present in our Ragel-based parser for many years but no memory was leaked because o
  - DAN-136 (llm) [sem seção] 0.687: Last Friday, Tavis Ormandy from Google’s Project Zero contacted Cloudflare to report a security problem with our edge servers. He was seeing corrupted web pages being returned by some HTTP requests ru
  - DAN-136 (causa) [Some lessons] 0.41: ## Some lessons  The engineers working on the new HTML parser had been so worried about bugs affecting our service that they had spent hours verifying that it did not contain security problems.  Unfor
  - DAN-136 (correcao) [Detailed Timeline] 0.488: ## Detailed Timeline  We are very grateful to our colleagues at Google for contacting us about the problem and working closely with us through its resolution. All of which occurred without any reports
  - DAN-136 (correcao) [Going bug hunting] 0.439: ## Going bug hunting  2017-02-13 Email Obfuscation partially migrated to new parser  2017-02-18 Google reports problem to Cloudflare and leak is stopped  The greatest potential impact occurred for fou

## q-265 (esperado: DAN-204)

- busca inicial: DAN-175, DAN-204, DAN-124, DAN-058, DAN-131, DAN-203, DAN-220, DAN-107, DAN-098, DAN-164
- justificativa: 
- aprofundar DAN-204: `Redis cache corruption cross user data billing fix` — Bate exatamente: usuários viam dados de outros usuários incluindo billing info; não bate: causa foi corrupção de filas Redis, não vazamento de token.
- aprofundar DAN-058: `misconfigured DB backup identifiers data leak fix` — Bate: vazamento de dados entre clientes por identificadores incorretos; não bate: envolve bancos free tier e backups, não exibição em tempo real.
- aprofundar DAN-175: `private tokens leaked customer data access fix` — Bate: dados de clientes expostos a terceiros; não bate: vazamento de tokens privados com ataque externo, não exibição acidental entre usuários.
  - DAN-204 (llm) [Technical details] 0.633: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.632: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-058 (llm) [What happened?] 0.781: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.704: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-175 (llm) [Incident Summary] 0.582: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.532: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-266 (esperado: DAN-205)

- busca inicial: DAN-205, DAN-209, DAN-184, DAN-191, DAN-180, DAN-066, DAN-106, DAN-065, DAN-234, DAN-129
- justificativa: 
- aprofundar DAN-205: `shared peering point network instability quorum notifications root cause fix` — Corresponde quase exatamente: duas de três implantações com problemas de conectividade e latência alta, ponto comum de peering instável, perda de quorum e parada de notificações. Não há diferença relevante no cenário descrito.
  - DAN-205 (llm) [The Outage] 0.699: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.618: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-267 (esperado: DAN-205)

- busca inicial: DAN-205, DAN-209, DAN-184, DAN-148, DAN-066, DAN-116, DAN-107, DAN-191, DAN-109, DAN-234
- justificativa: 
- aprofundar DAN-205: `shared peering point network instability quorum notification failure root cause fix` — Bate com o atual: duas de três implantações com alta latência e perda de conexão ao mesmo tempo, e o sistema parou de enviar notificações. Não bate: foi um ponto de peering compartilhado na nuvem, não necessariamente nossa arquitetura.
  - DAN-205 (llm) [The Outage] 0.715: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.63: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-268 (esperado: DAN-207)

- busca inicial: DAN-207, DAN-215, DAN-084, DAN-124, DAN-132, DAN-146, DAN-050, DAN-141, DAN-131, DAN-239
- justificativa: 
- aprofundar DAN-207: `multi-sig wallet security bug root cause fix stolen cryptocurrency` — É o único incidente sobre código de carteira cripto com falha de segurança que permitiu roubo de fundos por terceiros, correspondendo diretamente a carteiras sendo esvaziadas via código; difere por ser carteira multi-sig específica e não um ataque genérico.
  - DAN-207 (llm) [sem seção] 0.751: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.743: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 

## q-269 (esperado: DAN-207)

- busca inicial: DAN-207, DAN-215, DAN-132, DAN-175, DAN-124, DAN-084, DAN-160, DAN-141, DAN-016, DAN-219
- justificativa: 
- aprofundar DAN-207: `multi sig wallet security bug root cause fix` — Envolve carteiras de criptomoedas sendo drenadas por um bug de segurança no código, igual ao incidente atual, embora o bug venha de uma mudança mal revisada implantada por terceiros.
- aprofundar DAN-215: `employee cryptocurrency theft root cause security fix` — Também envolve roubo de criptomoedas, mas por funcionário interno e falhas operacionais, não por vulnerabilidade no código da carteira explorada por atacantes externos.
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.748: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [sem seção] 0.73: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.595: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.538: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo

## q-270 (esperado: DAN-208)

- busca inicial: DAN-208, DAN-079, DAN-151, DAN-066, DAN-106, DAN-144, DAN-191, DAN-222, DAN-205, DAN-220
- justificativa: 
- aprofundar DAN-208: `Zookeeper too much data boot failure maintenance window fix` — Bate exatamente com janela de manutenção programada e Zookeeper que não consegue subir/boot.
- aprofundar DAN-079: `Zookeeper reprovisioning second leader two clusters fix` — Envolve ZooKeeper durante procedimento de rotina, mas trata de segundo líder e dois clusters, não de falha em iniciar.
  - DAN-208 (llm) [Read the socket] 0.717: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (llm) [Wrapping up] 0.715: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\
  - DAN-079 (llm) [sem seção] 0.666: In October, we experienced one incident resulting in significant impact and degraded state of availability for issues, pull requests, webhooks, GitHub Actions, and GitHub Pages services.  While reprov

## q-271 (esperado: DAN-208)

- busca inicial: DAN-208, DAN-151, DAN-079, DAN-103, DAN-211, DAN-066, DAN-135, DAN-220, DAN-026, DAN-109
- justificativa: 
- aprofundar DAN-208: `Zookeeper too much data boot scheduled maintenance window root cause fix` — O resumo cita pane durante janela de manutenção programada porque havia dados demais para o Zookeeper boota, igual ao incidente atual (Zookeeper não inicia após manutenção).
  - DAN-208 (llm) [Wrapping up] 0.72: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (llm) [Read the socket] 0.701: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\

## q-272 (esperado: DAN-215)

- busca inicial: DAN-215, DAN-207, DAN-084, DAN-050, DAN-131, DAN-015, DAN-029, DAN-203, DAN-175, DAN-124
- justificativa: 
- aprofundar DAN-215: `employee cryptocurrency theft root cause security fix` — Criptomoeda roubada várias vezes em curto período, igual ao incidente atual; difere por ser furto interno de funcionário.
- aprofundar DAN-207: `multi-sig hack root cause software bug fix` — Criptomoeda roubada, mas por bug de software em contrato inteligente, não por roubo recorrente de carteira.
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.595: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.538: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.692: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [sem seção] 0.664: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 

## q-273 (esperado: DAN-215)

- busca inicial: DAN-207, DAN-215, DAN-084, DAN-131, DAN-015, DAN-050, DAN-209, DAN-175, DAN-219, DAN-132
- justificativa: 
- aprofundar DAN-207: `multi sig wallet security bug root cause fix patch` — Envolve roubo de criptomoeda por falha de segurança, mas é um único evento grande, não repetição em semanas.
- aprofundar DAN-215: `employee theft cryptocurrency multiple hacks root cause fix` — Envolve roubo repetido de criptomoeda em curto período, mas por funcionário interno, não carteira externa.
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.738: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [sem seção] 0.716: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.539: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.511: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo

## q-274 (esperado: DAN-226)

- busca inicial: DAN-226, DAN-048, DAN-190, DAN-094, DAN-116, DAN-195, DAN-181, DAN-120, DAN-058, DAN-126
- justificativa: 
- aprofundar DAN-226: `SQL Server bugcheck root cause fix read only mode primary` — O resumo é praticamente idêntico ao incidente atual: o SQL Server primário deu bugcheck e os sites ficaram somente leitura. Mesmo componente, mesmo gatilho e mesmo sintoma; apenas o provedor (Stack Exchange) é diferente.
  - DAN-226 (llm) [sem seção] 0.581: On January 24, 2017 starting at 17:53 UTC, we experienced system degradation (read only) followed by a site outage. The Stack Exchange network went into read-only mode for approximately 5 minutes befo

## q-275 (esperado: DAN-226)

- busca inicial: DAN-226, DAN-048, DAN-181, DAN-094, DAN-173, DAN-120, DAN-116, DAN-056, DAN-195, DAN-080
- justificativa: 
- aprofundar DAN-226: `SQL Server bugcheck cause fix read-only mode outage` — Corresponde exatamente: SQL Server primário com bugcheck, sites em modo read-only e pane total; não há incompatibilidade de componente ou gatilho.
  - DAN-226 (llm) [sem seção] 0.652: On January 24, 2017 starting at 17:53 UTC, we experienced system degradation (read only) followed by a site outage. The Stack Exchange network went into read-only mode for approximately 5 minutes befo

## q-276 (esperado: DAN-235)

- busca inicial: DAN-235, DAN-231, DAN-221, DAN-184, DAN-022, DAN-165, DAN-154, DAN-059, DAN-195, DAN-069
- justificativa: 
- aprofundar DAN-235: `SMS filtering AT&T root cause fix remediation` — O incidente DAN-235 descreve exatamente o mesmo sintoma do atual: alto nível de filtragem de SMS para a rede AT&T nos Estados Unidos, impedindo a entrega. Bate em tipo de falha (filtragem de SMS), componente (rede de operadora dos EUA) e impacto (mensagens não chegam). Não bate o provedor (Twilio), que não é especificado no incidente atual.
  - DAN-235 (llm) [High Filtering On SMS Towards AT&T Network In United States] 0.704: ## High Filtering On SMS Towards AT&T Network In United States  ## Resolved  We are no longer experiencing high filtering on SMS towards AT&T network in the United States for all senders. This inciden
  - DAN-235 (llm) [Investigating] 0.696: ## Investigating  We are experiencing high filtering on SMS towards AT&T network in Unites states. Our engineers are working with our carrier partner to resolve the issue. We expect to provide another
  - DAN-235 (causa) [Update] 0.24: ## Update  We are experiencing high filtering on SMS towards AT&T network in United States. Our engineers are continuing to work with our carrier partner to resolve the issue. We expect to provide ano
  - DAN-235 (correcao) [Monitoring] 0.273: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States. We will continue to monitor to ensure full service recovery. We expect to provide another
  - DAN-235 (correcao) [Monitoring] 0.254: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States for all senders. We will continue monitoring the service to ensure a full recovery. We wil

## q-277 (esperado: DAN-235)

- busca inicial: DAN-235, DAN-231, DAN-221, DAN-184, DAN-022, DAN-165, DAN-065, DAN-195, DAN-005, DAN-006
- justificativa: 
- aprofundar DAN-235: `SMS filtering AT&T root cause resolution Twilio` — O sintoma é idêntico ao incidente atual: mensagens SMS sendo filtradas para uma operadora dos EUA (AT&T) e não chegando aos destinatários; pode diferir apenas a plataforma envolvida.
  - DAN-235 (llm) [Update] 0.77: ## Update  We are experiencing high filtering on SMS towards AT&T network in United States. Our engineers are continuing to work with our carrier partner to resolve the issue. We expect to provide ano
  - DAN-235 (llm) [Investigating] 0.768: ## Investigating  We are experiencing high filtering on SMS towards AT&T network in Unites states. Our engineers are working with our carrier partner to resolve the issue. We expect to provide another
  - DAN-235 (causa) [Monitoring] 0.24: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States. We will continue to monitor to ensure full service recovery. We expect to provide another
  - DAN-235 (correcao) [Monitoring] 0.254: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States for all senders. We will continue monitoring the service to ensure a full recovery. We wil
  - DAN-235 (correcao) [High Filtering On SMS Towards AT&T Network In United States] 0.244: ## High Filtering On SMS Towards AT&T Network In United States  ## Resolved  We are no longer experiencing high filtering on SMS towards AT&T network in the United States for all senders. This inciden

## q-278 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-146, DAN-073, DAN-231, DAN-043, DAN-104, DAN-071, DAN-173, DAN-220, DAN-048
- justificativa: 
- aprofundar DAN-236: `steam desktop client deleted local files root cause fix` — O cliente desktop Steam apagou arquivos e diretórios locais do usuário, igual ao incidente atual; difere o ambiente (Steam/Linux versus nosso cliente).
- aprofundar DAN-146: `os upgrade wiped out machines databases cause fix` — Relata máquinas apagadas após upgrade, semelhança na perda massiva de dados, mas é infraestrutura, não cliente desktop de usuário.
- aprofundar DAN-173: `filesystem corruption bug containers upgrade check fix` — Envolve corrupção de filesystem por mudança que desabilitou verificação, semelhança na perda de dados, mas ocorre em containers, não cliente desktop.
  - DAN-236 (llm) [Activity] 0.702: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.699: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 
  - DAN-146 (llm) [sem seção] 0.639: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [sem seção] 0.538: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri
  - DAN-173 (llm) [Root Causes] 0.797: ## Root Causes  Near the start of December, we upgraded our container tools. This included changing the digest algorithms and filenames used by these safety checks. We also introduced a latent bug: th
  - DAN-173 (llm) [The Fix] 0.726: ## The Fix  Once we identified the problem, we migrated all affected dynos to fresh hosts, with non-corrupted filesystems and with coherent filesystem caches. This work took the majority of the five h
  - DAN-173 (causa) [sem seção] 0.498: As part of our commitment to security and support, we periodically upgrade the stack image, so that we can install updated package versions, address security vulnerabilities, and add new packages to t
  - DAN-173 (correcao) [Technical Impact] 0.45: ## Technical Impact  This problem caught us completely by surprise. While we had taken into account that overwriting a mounted image would cause problems, none of us fully understood what those proble
  - DAN-173 (correcao) [Technical Impact] 0.417: ## Technical Impact  - Create a disk image with a simple program on it. We used sleep. dd if=/dev/zero of=demo.img bs=1024 count=10240 mkfs -F -t ext4 demo.img sudo mkdir -p /mnt/demo sudo mount -o lo

## q-279 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-146, DAN-073, DAN-164, DAN-043, DAN-104, DAN-220, DAN-126, DAN-173, DAN-058
- justificativa: 
- aprofundar DAN-236: `desktop client deleted local files root cause fix` — Bate: cliente de desktop (Steam) deletou arquivos e diretórios locais dos usuários, igual ao incidente atual. Não bate: é um caso específico do Steam no Linux, não genérico.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.549: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (llm) [jthill commentedon Jan 15, 2015] 0.532: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [Activity] 0.283: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 

## q-280 (esperado: DAN-237)

- busca inicial: DAN-237, DAN-142, DAN-152, DAN-131, DAN-136, DAN-011, DAN-124, DAN-122, DAN-034, DAN-090
- justificativa: 
- aprofundar DAN-237: `website compromised download link malicious zip root cause fix` — Bate porque envolve site comprometido com links de download alterados para um zip malicioso, igual ao incidente atual; não se sabe se o vetor foi o mesmo (servidor/CMS).
- aprofundar DAN-152: `npm account compromised malicious packages published root cause fix` — Bate porque envolve distribuição de software malicioso via conta comprometida; não bate porque são pacotes npm, não download direto de site em zip.
- aprofundar DAN-122: `JCenter malicious Maven packages impersonation attack root cause fix` — Bate porque envolve pacotes maliciosos publicados em repositório de software; não bate porque é Maven/JCenter, não site servindo zip a usuários.
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.69: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  **Elizabeth K. Joseph**     lyz at ubuntu.com  *Mon Nov 17 17:59:36 UTC 2025*  Dear community, As
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.519: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  in a controlled, read-only mode to allow migration to a new static site. To be perfectly clear: t
  - DAN-237 (causa) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.234: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  generator has actually been in the works for some time as our reliance upon the dynamic features 
  - DAN-152 (llm) [Summary] 0.751: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.739: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.719: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.647: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-281 (esperado: DAN-237)

- busca inicial: DAN-237, DAN-131, DAN-142, DAN-136, DAN-122, DAN-011, DAN-152, DAN-124, DAN-034, DAN-203
- justificativa: 
- aprofundar DAN-237: `compromised website download links malicious zip file root cause fix` — O site foi comprometido e os links de download apontavam para um zip malicioso, igual ao incidente atual; não há diferença relevante.
- aprofundar DAN-122: `malicious packages JCenter impersonation attack root cause fix` — Envolve arquivos maliciosos servidos a usuários via repositório público, mas o vetor é um registry de pacotes e não downloads diretos do site.
- aprofundar DAN-152: `compromised npm account malicious packages root cause fix` — Envolve publicação de pacotes maliciosos após comprometimento de conta, mas o alvo é um registry npm e não o site de downloads.
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.687: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  **Elizabeth K. Joseph**     lyz at ubuntu.com  *Mon Nov 17 17:59:36 UTC 2025*  Dear community, As
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.516: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  in a controlled, read-only mode to allow migration to a new static site. To be perfectly clear: t
  - DAN-237 (causa) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.234: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  generator has actually been in the works for some time as our reliance upon the dynamic features 
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.777: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.688: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.749: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.721: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-282 (esperado: DAN-240)

- busca inicial: DAN-240, DAN-068, DAN-191, DAN-063, DAN-159, DAN-066, DAN-209, DAN-210, DAN-067, DAN-239
- justificativa: 
- aprofundar DAN-240: `leased line failure backup line unstable orders fixing remediation` — Falha de linha dedicada primária para bolsa com backup instável afetando ordens, exatamente como o incidente atual.
- aprofundar DAN-159: `partial link failure redundant links misconfiguration fix remediation` — Envolve detecção de falha parcial de link e links redundantes, mas não é linha dedicada à bolsa nem afeta ordens diretamente.
  - DAN-240 (llm) [sem seção] 0.65: 13 Apr 2018, 01:48 PM  # Postmortem: Trading and hanging orders on 12th April 2018  Traders,  Yesterday, on the 12th April, one of the NSE leased line connections to our setup went down. This affected
  - DAN-240 (llm) [Postmortem: Trading and hanging orders on 12th April 2018] 0.454: # Postmortem: Trading and hanging orders on 12th April 2018  Once the CTCL was shut off, the orders which were showing any of the pending states were lapsed and reconciled with the exchange. This affe
  - DAN-159 (llm) [sem seção] 0.634: network. The switches are specifically configured to detect this sort  of problem and to protect the network by disabling links where  they detect an issue, and that’s what happened in this case.  We 
  - DAN-159 (llm) [sem seção] 0.522: To solve this problem, we purchased additional switches to build what’s  called an aggregation network, which is more of a tree structure.  Network switches at the top of the tree (aggregation swtiche
  - DAN-159 (causa) [sem seção] 0.377: On Friday, November 30th, GitHub had a rough day. We experienced 18  minutes of complete unavailability along with sporadic bursts of slow  responses and intermittent errors for the entire day. I’m ve
  - DAN-159 (correcao) [sem seção] 0.495: 1. We have worked with our network vendor to provide diagnostic information which led them to discover the root cause for the MAC learning issues. We expect a final fix for this issue within the next 
  - DAN-159 (correcao) [sem seção] 0.456: links between the access and aggregation switches, causing the poor  performance we saw throughout the day.  We worked with the vendor until late on Friday night to formulate a  mitigation plan and to

## q-283 (esperado: DAN-240)

- busca inicial: DAN-240, DAN-209, DAN-191, DAN-068, DAN-239, DAN-077, DAN-205, DAN-067, DAN-106, DAN-159
- justificativa: 
- aprofundar DAN-240: `leased line backup unstable orders root cause remediation` — Corresponde exatamente: linha alugada primária caiu, backup instável e ordens falhando na bolsa, embora o contexto seja a corretora Zerodha.
- aprofundar DAN-239: `order management system collapse fix remediation` — Mesmo domínio de corretora de ações com ordens falhando, mas a causa é colapso do OMS por volume grande, não linha alugada.
- aprofundar DAN-205: `network instability connectivity quorum failure root cause fix` — Instabilidade de rede causando falhas operacionais, mas sem relação com linha alugada dedicada à bolsa.
  - DAN-240 (llm) [sem seção] 0.645: 13 Apr 2018, 01:48 PM  # Postmortem: Trading and hanging orders on 12th April 2018  Traders,  Yesterday, on the 12th April, one of the NSE leased line connections to our setup went down. This affected
  - DAN-240 (llm) [Postmortem: Trading and hanging orders on 12th April 2018] 0.5: # Postmortem: Trading and hanging orders on 12th April 2018  Once the CTCL was shut off, the orders which were showing any of the pending states were lapsed and reconciled with the exchange. This affe
  - DAN-239 (llm) [sem seção] 0.571: 29 Aug 2019, 06:00 PM  # Post-mortem of technical issue – August 29, 2019  Between 10.00 and 10.40 AM today, we faced technical issues with our order management system (OMS). Order placements resumed 
  - DAN-239 (llm) [Post-mortem of technical issue – August 29, 2019] 0.344: # Post-mortem of technical issue – August 29, 2019  Once again, we are extremely sorry about this. There are unforeseen edge cases and rare conditions like this that can affect any technology business
  - DAN-205 (llm) [The Outage] 0.611: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Background] 0.555: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (causa) [Long term] 0.47: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Outage Post-Mortem – April 13, 2013] 0.374: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
