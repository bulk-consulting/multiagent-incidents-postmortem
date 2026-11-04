<!--
Prompt de extração da ficha (peça 2). Versão: v2.14.
v1 guardada em prompt_extracao_v1.md. Mudanças da v2 (revisão do piloto, ver FICHA.md):
regra 2 (trechos sustentam todo detalhe do texto), regras 3 e 4 novas (causalidade e plano x feito),
gatilho x causa raiz, categoria pela causa raiz, detecção, resumo com desfecho, mitigação com a correção concreta.
v2.1 (revisão da DAN-164): plano não entra em mitigacao; ação de operador não é mudanca_causadora; confiança alta só sem nenhuma escolha.
v2.2 (revisão das DAN-169 e 183): feito marcado como feito em prevencao; na dúvida entre níveis, o mais fraco; gatilho não é observação de investigação;
mudança de ambiente sem ligação declarada não é mudanca_causadora; "worth trying" precisa de trecho que confirme a execução.
v2.3 (revisão das DAN-024, 152, 166): gatilho null quando o texto não separa gatilho e causa (regra em destaque); recomendações a terceiros em prevencao.
v2.4 (revisão das DAN-027, 046, 063): gatilho só com condição prévia distinta; "X e depois Y identificado" não é causa; ano pela data de publicação no texto; categoria pela causa raiz mesmo contra a manchete.
v2.5 (teste às cegas das 10 fichas do gabarito): tipo postmortem x artigo_tecnico; status final x preliminar; concreta x incerta; duração declarada prevalece sobre calculada.
v2.6 (leitura do prompt pelo GPT): consolidação. Campo observacoes separado da confiança; bloco causal reescrito
(gatilho, causa_raiz, ação de operador, mudança generica x ausente); escopo de catalogo parcial; nível da mitigação; duração do impacto.
v2.7 (2º teste às cegas, 93%): detecção inclui o sintoma notado; categoria human-error quando a ação do operador é o gatilho;
exemplo de ataque no gatilho; critério de especificas na prevenção.
v2.8 (revisão do lote 01, 23 ERRADOS em 9 fichas): checklist de confiança; duração só do impacto; trechos com contexto;
tentado não é feito; fator não é impacto nem mecanismo nem comunicação; ataque por mecanismo; documento com vários incidentes; autoria do time.
v2.9 (revisão do lote 02, 21 ERRADOS em 10 fichas, metade de trecho que não prova o texto): passo de verificação detalhe a detalhe;
motivo de baixa precisa dizer por que a regra não decide; mitigação só até o fim do impacto.
v2.10 (revisão do lote 03, 15 ERRADOS em 10 fichas): mitigação sem passos de resposta; fator sem funcionamento normal nem mitigação repetida;
rodape_marketing inclui rodapé de lista de e-mail e de site.
v2.11 (revisão do lote 04, 14 ERRADOS em 9 fichas): pedido a outra equipe não é feito; detecção sem resposta; fator não é sobre pessoa;
cabeçalho no texto vale para a data; verificação detalhe a detalhe também em cada passo da mitigação.
v2.12 (revisão do lote 05, 15 ERRADOS em 10 fichas): objetivo não é resultado; "decided at X" não é "did at X"; horário de parágrafo de resumo;
software de controle físico do data center; bug antigo sem queda delimitada.
v2.13 (amostra do lote 06, 6 ERRADOS em 6 fichas): equipe_interna só quando o texto diz que alguém notou sem alerta;
atividade operacional automática (scaling, failover) não é mudanca_causadora.
v2.14 (amostra do lote 09, 4 ERRADOS em 7 fichas): duração com marcas de início/fim no texto; serviço de volta degradado é o fim; faixa de minutos é null.
Escrito em inglês de propósito (ver FICHA.md, seção "Idioma").
A parte entre ===== INPUT ===== é preenchida para cada documento.
-->

# Post-mortem extraction — prompt v2.14

You are extracting a structured record ("ficha") from one public incident post-mortem. The record will be used by an incident-diagnosis assistant that must **never state anything the source does not say**. Your job is to organize what the text says, with proof. You are not writing a post-mortem, summarizing for readers, or judging the company.

## Non-negotiable rules

1. **Only the text.** Use only the document below. Never add facts from your own knowledge, even if you know the incident well. If the text does not say it, the field is `null`, empty, or `ausente`.
2. **Every claim has verbatim evidence.** Each `texto` comes with `trechos`: exact copies of passages from the document. A program will check that every `trecho` exists in the document; any `trecho` that does not match makes the record fail.
   - Copy character by character. Do not fix typos, change quotes, translate, or reformat.
   - One `trecho` = one contiguous passage, usually one sentence (10 to ~300 characters). Never join separate passages and never use "...".
   - Prefer the passage that most directly supports the claim.
   - **The `trechos` of a claim must support every detail of its `texto` on their own**: names, dates, times, numbers, who did or recommended something, and results. A reader must not need any other part of the document to check the claim. If a detail is not in the `trechos`, add the passage that states it or remove the detail.
   - If a `trecho` refers back with "this", "these metrics", "it", "the change", "at this point", "something", "that fix", add the passage that says what it refers to. A number or a name in the `texto` (a TTL value, a version, who recommended something) must appear in a `trecho` of that same claim.
3. **No causal links the text does not state.** Do not connect two facts with "so", "which caused", "until", "because" unless the document states that link. "At the same time" or "we then noticed" is not "because". "X happened, and eventually they identified Y" is not "Y caused X": write it in the text's order. If the document only suggests a link, keep its wording ("the authors consider it likely that…").
4. **Done is not planned.** Keep apart what was done from what was planned or proposed ("this process would involve", "we will", "we are looking into", "we figured it was worth trying"). A planned step is described as planned, never as done. The other way round too: an action already done that appears among future actions is marked "Already done:". If the passage you found only proposes a step, add the passage that confirms it was carried out ("shortly after making those changes…", "the downgrade was successful"). **Tried is not achieved either**: "focused on recovering", "worked to", "tried to", "devised a fix", "scheduled", "asked the data center team to reboot", "called X to" describe effort, intent or a request; write them that way. **A purpose is not a result**: "tested X to determine that it has no effect", "to ensure", "to check" state what the test was for, not what it found. **In timelines, "at 19:15 the decision was made to scale" is a decision**: write "decided at 19:15", and state that it was done only if another passage says so; write them that way, never as a result ("recovered", "fixed", "deployed").
5. **Keep the certainty of the source.** If the text says "we believe", "likely", "appears", "we suspect", "still investigating", your `texto` must keep that uncertainty. Never turn a hypothesis into a fact.
6. **Neutral and blameless.** Describe systems and conditions, not people. No judgment words (careless, negligent, terrible, etc.). Do not name individuals.
7. **When in doubt, choose the weaker option** (e.g. `incerta` over `concreta`, `generica` over `especifica`). If, after applying every rule below, two values still fit a field, choose the weaker one and set `confianca` to `baixa` (see `confianca`).
8. **All free text in English**: `resumo`, every `texto`, `perguntas_em_aberto`, `motivo_confianca_baixa`, `observacoes`. Field names and enum values stay exactly as specified (they are in Portuguese).

## Procedure

1. Read the catalog description, then the whole document.
2. Fill `triagem` (what kind of document this is).
3. If `catalogo` is `nao` or `nao_verificavel`: set the four other classification fields to `null`, set `incidente` to `null`, and stop.
4. Otherwise fill `incidente`, field by field, finding the `trechos` first and writing `texto` from them.
5. **Detail check, claim by claim (mandatory).** For each `texto`, list every name, number, date, time, place, actor and result it states (e.g. "20:50 UTC", "mrsync", "the main MySQL database", "brought the app back up", "the next morning"). For each item, find the `trecho` of **that same claim** that contains it. If none does, add the passage that states it (a timeline row with its timestamp, the sentence that names the tool, the sentence that confirms the result) or remove the detail. A detail you cannot find anywhere in the document must be removed. Times often appear only in a summary paragraph ("unavailable from 16:06 to 18:53 UTC") far from the step that uses them; add that summary sentence as a `trecho` of the step. Do this for **every step of `mitigacao` and every action of `prevencao`** too: in long documents these steps gather details (hardware sizes, percentages, who was asked, what was checked) from several paragraphs, and each one needs its own `trecho`.
6. Check, claim by claim: remove any causal link the text does not state (rule 3); check that nothing planned or merely attempted is written as done (rule 4); every enum value is from the lists below; uncertainty is preserved ("may have" stays "may have", also in `resumo`).
7. Check `confianca` with the checklist in that section.
8. Output the JSON.

## `triagem`

**`catalogo`** — compare the document with the catalog description.
- `sim`: the document is mainly about the incident described in the catalog. If the catalog itself describes **a set of incidents** (e.g. "a tale of multiple incidents"), it is `sim`; then `causa_raiz` holds the shared cause the authors state, `gatilho` is `null`, and each incident's own mechanism goes to `fatores_contribuintes`.
- `parcial`: the incident appears but is a small part of a text about something else, or the text mixes several incidents. **Extract only the catalog incident.** Another incident enters only as a `fatores_contribuintes` item, and only if the text links it to the catalog incident's impact.
- `nao`: the document has content, but about a different incident or subject.
- `nao_verificavel`: there is no article content to compare (empty, or only menus/navigation).

**`autoria`** — `primaria`: written by the affected company or the provider responsible for the service, including a member of the team that built or ran the affected system writing later in a personal capacity. `secundaria`: written by a third party (press, encyclopedia, outside analyst, investigating body).

**`tipo`**
- `postmortem`: account written after the incident by the affected company or provider (what happened, why, what will change). A blog post by that company entirely about one incident is `postmortem` even if written as a narrative.
- `atualizacoes_status`: updates published during the incident, with or without a post-mortem at the end. If the document contains status updates at all, this wins over `postmortem`.
- `relatorio_periodico`: report covering several incidents of a period (e.g. monthly availability report).
- `artigo_tecnico`: technical article where the incident is one part, or a third party's technical analysis of an incident.
- `relatorio_formal`: long investigation, consulting or governance report.
- `noticia_enciclopedia`: news article or encyclopedia entry.
- `outro`: none of the above (mailing list, forum, issue, thread).

**`dominio`** — classify by the **origin** of the problem, not its effect.
- `software_servicos`: software, configuration, deployment, database, logical network, cloud, dependencies.
- `infra_fisica_datacenter`: power, cooling, hardware or physical network **inside a data center**, including the software that controls these physical systems (a cooling or power control system with a bug).
- `seguranca`: the origin is a malicious action (intrusion, stolen credentials, malicious package, supply-chain attack).
- `fora_de_ti`: not an IT system (public power grid, aviation, space, healthcare, ships, industrial plants). Embedded software in such systems is still `fora_de_ti`.

**`seguranca`** — `nao`: no data exposure and no malicious action. `exposicao_dados`: user data exposed by a failure, without an attack. `ataque`: there was a malicious action (then `dominio` should be `seguranca`).

**`problemas_texto`** — list (possibly empty) of problems in the extracted text: `sem_conteudo` (only menus, navigation, page chrome), `comentarios` (reader comments included), `rodape_marketing` (footer, ads, job calls, newsletter prompts, mailing-list footers, calls to contribute or sign up, site footer links such as "advertising" or "careers"), `pdf_embaralhado` (columns or order of a PDF mixed up).

## `incidente`

**`resumo`** — 1 to 3 neutral sentences (max 600 characters): what failed, impact, **and how service was restored** (or that the text does not say). No `trechos` needed, but it must not say anything the other fields do not support, and rules 3 and 4 apply.

**`data_incidente`** — `YYYY-MM-DD`, `YYYY-MM` or `YYYY`, only if the text states it. Otherwise `null`. The year may come from a publication date written in the extracted text when the event is described as days before it (say so in `observacoes`); never from the page title or the URL. A heading **inside the extracted text** that dates the incident (e.g. "# 2014-01-28 Outage Postmortem") is part of the text and may be used; "page title" means the metadata title that does not appear in the extracted text.

**`status_relatorio`** — the stage of the text, not the certainty of the cause.
- `final`: written after the incident ended and not presented as preliminary. Points the text says are still pending (e.g. forensics not completed) do not change this; they go to `perguntas_em_aberto`.
- `preliminar`: written while the incident was ongoing, or presented by the text itself as preliminary or subject to change.
- `misto`: preliminary updates and a final report in the same text.
- `indefinido`: the text does not let you tell when it was written relative to the incident.

**`servicos_afetados`** — services or products the text says were impacted. **`tecnologias`** — technical components the text names as involved (e.g. `PostgreSQL`, `BGP`, `Kubernetes`, `systemd`). Use the names as written; empty list if none.

**`categoria_causa`** — classifies the **`causa_raiz`, not the `gatilho`** (`null` if `causa_raiz.status` is `ausente`). Examples: a policy change (trigger) reaches code with no error handling (root cause) → `software-bug`; a password rotation (trigger) is not applied to one service's configuration, which can no longer authenticate (root cause) → `credential-auth`; an operator runs a destructive command on the wrong host, and the text gives no other condition → `human-error`. If the root cause has no stated mechanism that fits a category (e.g. "the correction didn't register"), use `other`, even if the article's headline blames something else.
- `configuration-error`: a change to configuration, rules or policy caused it.
- `human-error`: an operator action (wrong command, parameter or target).
- `credential-auth`: compromised, expired or mis-deployed credentials.
- `database-storage`: the datastore itself failed (limits, corruption, replication break).
- `cascading-failure`: one component's degradation propagated through dependencies.
- `network-bgp`: routing itself failed (leak, hijack), not a config change with routing symptoms.
- `capacity-load`: load, limits or capacity exhausted without a configuration change.
- `hardware-power`: power, cooling or hardware failure.
- `software-bug`: a code defect that fits none of the above.
- `supply-chain`: tampered material left one organization and ran in another's environment.
- For **attacks** (`seguranca: ataque`), classify the mechanism of the root cause: a DDoS that floods the network → `capacity-load`; stolen or reused credentials → `credential-auth`; a tampered package → `supply-chain` only when the root cause is the tampering itself, not how the attacker got access.
- `other`: none of the above.

**`deteccao`** — how the problem was **first noticed**, not what was done next. "The team was triaging within 2 minutes", "we began investigating", "an incident was raised", "a team was assembled" are response, not detection; leave them out of `descricao`. `forma`: `alerta_automatico` (monitoring/alerting fired), `usuarios_clientes` (users or customers reported), `equipe_interna` (the text says a person noticed it without an alert, e.g. "an operator noticed", "an engineer saw"), `terceiros` (another company, press), `nao_informada` (the text does not say how: "we detected this internally", "real-time detection" or only the symptom, without saying whether an alert fired or a person noticed). `descricao`: what was first noticed (the symptom, e.g. "higher than normal re-queue rates", "a larger-than-normal number of Postgres connection timeouts") and, if the text says it, how; claim + `trechos`. `null` only if the text says neither. The symptom can be filled while `forma` is `nao_informada`.

**Cause fields.** Four fields describe the cause; decide them together.
- **`causa_raiz`** always holds the failure that produced the impact, as the text states it.
- **`gatilho`** is filled only when the text describes **two distinct things**: an event, and a **pre-existing condition** in the system that made that event harmful. Then `gatilho` holds the event and `causa_raiz` holds the condition.
- **`fatores_contribuintes`** holds what made it worse, delayed detection or slowed recovery.
- **`mudanca_causadora`** says whether a persistent change set it off.

**`gatilho`** — the event **immediately before the impact started** (a deploy, a policy push, a password rotation, a capacity addition, a traffic spike, a power loss, an operator command), **only** when the text also describes a separate pre-existing condition. Examples with both: a password rotation + a service configuration that was never updated with the new password; a policy push + code with no error handling; a utility power loss + backup generators that then failed; an attacker's action (logging in, publishing a package) + a weakness that existed before (a reused password, no two-factor authentication). It is **`null`** when:
- the change or event is itself the defect ("an erroneous configuration change broke the health checks");
- the text gives only one causal fact ("after we introduced a change that affected our configuration systems");
- the text does not say what started the first impact. Observations made later while investigating an affected request (a spike, dropped packets) are evidence for the root cause, not the trigger.

**`causa_raiz`** — the failure that produced the impact. With a `gatilho`, it is the condition that made the trigger harmful (e.g. "a small capacity addition" (trigger) made servers exceed "the operating system's maximum thread limit" (root cause)). With `gatilho` `null`, it is the change, event or defect itself.
- Stay at the technical level the text gives. Organizational causes (no owner, no tests, missing documentation) go to `fatores_contribuintes`, unless the text presents them as the cause itself.
- **Operator actions.** If the text describes a condition that made the action possible or harmful (e.g. a manual, undocumented procedure), the action is the `gatilho` and that condition is the `causa_raiz`; `categoria_causa` is still `human-error`. If it describes no such condition, `gatilho` is `null` and the action itself is the `causa_raiz` (`human-error`).
- If the text describes **more than one mechanism**, `causa_raiz` holds the one that started the impact; the others go to `fatores_contribuintes`, each with the role the text gives it (e.g. "the boot failures continued after the leaked VMs were deleted"). If the text does not make clear which one started the impact, that is a judgment call (`confianca` `baixa`).
- `status`:
  - `concreta`: the text says **what** failed and **why**, with a technical mechanism someone else could look for in their own system. A hedged or still-investigated detail about how that failure came about keeps `concreta` (e.g. the text states that a breaker opened and a generator failed, and only *why* the breaker opened is under forensics; or the account compromise is stated and only how the attacker got the password is "presumably" a breach). Put a stated open point in `perguntas_em_aberto`.
  - `incerta`: the text hedges **what failed** itself ("likely", "we believe", "appears" about the central failure), or gives only hypotheses.
  - `vaga`: only a category or generic term ("a network issue", "an upstream provider").
  - `ausente`: the text does not say why it happened → `descricao` = `null`.

**`fatores_contribuintes`** — up to 6 conditions that made it worse, delayed detection or slowed recovery (e.g. retries amplifying load, missing alerts, circular dependency in monitoring, a second technical mechanism). **Not factors:** the impact itself (emails sent to the wrong users, data exposed), a step of the root-cause mechanism already in `causa_raiz` (the cache that carried the wrong data), delays in communicating with customers (a late status page or tweet), the normal behaviour of the system when it is not what made things worse ("each connection starts by gossiping"), mitigation steps restated as a factor ("recovery required clearing state, which took hours"), and statements about a person ("the developer did not realize the mistake"; describe the system condition instead, if the text gives one); put a useful one in `observacoes`. Each is a claim + `trechos`. Choose the ones that matter most for diagnosing a similar incident; merge closely related ones. Empty list if none.

**`mudanca_causadora`** — the persistent change (configuration, code, version, parameter, policy) that set off the problem.
- `especifica`: the exact item is named (a parameter, file, version, rule).
- `generica`: the text says **what kind of change and where**, but not the exact item ("a configuration change to the databases", "a new feature for quota policy checks").
- `ausente`: the text says a change happened but **nothing about what or where** ("a recent change introduced the problem") → `descricao` = `null`.
- `nao_se_aplica`: the problem was not set off by a persistent change (hardware failure, load, attack, a latent bug with no change, a one-off operator command, an automated operational activity such as scaling or failover) → `descricao` = `null`. Running a command is not a change. An earlier change of environment (a migration, a new cluster) counts only if the text says it set off the problem; "we hadn't seen this before the migration" is context for `fatores_contribuintes`.

**`mitigacao`** — what was done **during** the incident to restore service, in order, **up to the end of the impact**. Actions after the impact ended (reverting the change in the code repository, re-enabling automation, cleanup) are not mitigation; put them in `prevencao` as "Already done:" if they prevent recurrence. **Response steps are not mitigation either**: opening an incident, assembling a team, investigating, detecting the cause (e.g. drift detection finding the change), communicating with customers. A step goes here only if it changed something in the system to restore service (rule 4: only what was done; steps the text gives only as a plan do not go here at all). Do not copy the full timeline; it stays in the original text. Include failed attempts only when they reveal something about the cause. **When the text names the actual fix** (what was changed, and to what), the step must include it; "the recommended changes were applied" is not enough if the text says what they were.
- `especifica`: at least one step says what was changed or acted on and in which component ("bypassed the automated control system and brought generators online manually", "took the misconfigured network device out of service").
- `generica`: every step is only a generic action ("we rolled back", "we restarted", "we applied a fix"), even if the component is named.
- `ausente`: the text does not say how service came back → `passos` = `[]`.

**`prevencao`** — what the document says will be done, or has already been done, to avoid recurrence.
- `especificas`: at least one action names the mechanism and where it applies, so someone could check it was done ("feature flags, disabled by default, for all changes to critical binaries", "hourly LVM snapshots of the production databases", "Prometheus monitoring for backups").
- `genericas`: every action names only an area or intention ("additional guardrails in our change management process", "more sensible concurrency limits", "improve our processes").
- `ausentes`: no prevention mentioned → `acoes` = `[]`.
- Recommendations the authors give **to others** (users, other maintainers, the community) may be listed, each `texto` starting with "Recommendation to <who>:". They are not commitments of the company; say so in `observacoes` if they are all the document offers.

**`duracao`** — the duration of the **impact** of the catalog incident (from the start of the impact to recovery), as `{"minutos": <integer>, "trechos": [...]}`, only if the text states it or gives start and end times that let you compute it; otherwise `null`.
- **A duration the text states explicitly ("approximately an hour", "Duration: 3 hours") wins over one computed from times, but only if it measures the impact.** The length of the attack, of the power outage or of a window in which data may have been exposed is not the impact when service came back later. Compute only when no impact duration is stated, and then include both passages. If the text does not say when service came back, `null`.
- If the text states two different durations, use the later or final report and note the other in `observacoes`.
- **Start and end of the impact.** If the text marks them (a timeline line "Impact starts" / "Impact ends", "resolved"), use those marks over other times in the text, and note any other start or end time in `observacoes`. If it marks no end but says service came back at a stated time, even in a degraded or partial form ("limited access to archives", "largely flowing as normal", "substantially recovered"), that time is the end of the impact; the later full restoration goes to `observacoes`. These cases are decided by this rule, not judgment calls.
- Vague amounts ("several hours", "more than two hours") and ranges ("10-15 minutes") → `null`; note a range in `observacoes`.
- **A long-standing bug without a bounded outage** (it happened from time to time over months or years): `duracao` is `null`, and the code fix that ended it is the `mitigacao` step; do not repeat it in `prevencao`.

**`perguntas_em_aberto`** — things the text **explicitly** says remain unknown or under investigation. Empty list if none. Do not add your own questions, and do not turn a hedged cause ("likely") into a question: that is already `causa_raiz.status = incerta`.

## `confianca` and `observacoes`

**`confianca`** measures whether the **rules** decided every field, not how certain the source is (that is `causa_raiz.status`).
- `alta`: for every field, the rules above leave only one value.
- `baixa`: for at least one field, two values still fit after applying every rule. Then `motivo_confianca_baixa` (English) names each such field, the two values, and **why the field's definition does not decide between them** (quote the part of the definition that both values satisfy). If you cannot write that reason, the definition decides: use its value and set `alta`.
- **Checklist before writing `baixa`**: for each field you hesitated on, reread its definition above. If the definition picks one value, use it, write the reason in `observacoes` if useful, and do **not** count it as a doubt. Cases that the rules already decide: `generica` vs `ausente` (the text says where the change was → `generica`); `final` vs `preliminar` (written after the incident and not presented as preliminary → `final`); a configuration or instance change vs `capacity-load` (a change was made → not `capacity-load`); a stated duration that does not measure the impact; "needed to block traffic" vs a mitigation step (needed is not done → not a step).

**`observacoes`** (optional, English) — notes a reader of the record should know that are **not** judgment calls: where a value came from (the year taken from the publication date), the other duration when two were given, a list announced in the text but missing from it, text repeated in another language, recommendations being all the prevention offered. A note here does not lower `confianca`. Omit the key if there is nothing to note.

## Output

Return **only** one JSON object, no comments, no Markdown fences, matching this shape exactly (all keys present; use `null`, `[]` or the `ausente`-type values when the text does not say):

{
  "schema_version": "1.0",
  "catalog_id": "<catalog_id>",
  "triagem": {
    "catalogo": "...", "autoria": "...", "tipo": "...", "dominio": "...", "seguranca": "...",
    "problemas_texto": []
  },
  "incidente": {
    "resumo": "...",
    "data_incidente": "..." | null,
    "status_relatorio": "...",
    "servicos_afetados": [],
    "tecnologias": [],
    "categoria_causa": "..." | null,
    "deteccao": { "forma": "...", "descricao": {"texto": "...", "trechos": ["..."]} | null },
    "gatilho": {"texto": "...", "trechos": ["..."]} | null,
    "causa_raiz": { "status": "...", "descricao": {"texto": "...", "trechos": ["..."]} | null },
    "fatores_contribuintes": [ {"texto": "...", "trechos": ["..."]} ],
    "mudanca_causadora": { "nivel": "...", "descricao": {"texto": "...", "trechos": ["..."]} | null },
    "mitigacao": { "nivel": "...", "passos": [ {"texto": "...", "trechos": ["..."]} ] },
    "prevencao": { "nivel": "...", "acoes": [ {"texto": "...", "trechos": ["..."]} ] },
    "duracao": {"minutos": 0, "trechos": ["..."]} | null,
    "perguntas_em_aberto": []
  },
  "confianca": "alta" | "baixa",
  "motivo_confianca_baixa": "..."   (only when confianca is "baixa"),
  "observacoes": "..."              (optional),
  "extracao": { "modelo": "<model name>", "data": "<YYYY-MM-DD>", "versao_prompt": "v2.14" }
}

===== INPUT =====

catalog_id: {catalog_id}
company: {company}
catalog description: {catalog_description}
source URL: {source_url}

Document (extracted text):
"""
{extracted_text}
"""

===== END INPUT =====
