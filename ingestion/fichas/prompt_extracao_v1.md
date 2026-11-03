<!--
Prompt de extração da ficha (peça 2). Versão: v1.
Escrito em inglês de propósito (ver FICHA.md, seção "Idioma").
A parte entre ===== INPUT ===== é preenchida para cada documento.
-->

# Post-mortem extraction — prompt v1

You are extracting a structured record ("ficha") from one public incident post-mortem. The record will be used by an incident-diagnosis assistant that must **never state anything the source does not say**. Your job is to organize what the text says, with proof. You are not writing a post-mortem, summarizing for readers, or judging the company.

## Non-negotiable rules

1. **Only the text.** Use only the document below. Never add facts from your own knowledge, even if you know the incident well. If the text does not say it, the field is `null`, empty, or `ausente`.
2. **Every claim has verbatim evidence.** Each `texto` comes with `trechos`: exact copies of passages from the document. A program will check that every `trecho` exists in the document; any `trecho` that does not match makes the record fail.
   - Copy character by character. Do not fix typos, change quotes, translate, or reformat.
   - One `trecho` = one contiguous passage, usually one sentence (10 to ~300 characters). Never join separate passages and never use "...".
   - Prefer the passage that most directly supports the claim.
3. **Keep the certainty of the source.** If the text says "we believe", "likely", "appears", "we suspect", "still investigating", your `texto` must keep that uncertainty. Never turn a hypothesis into a fact.
4. **Neutral and blameless.** Describe systems and conditions, not people. No judgment words (careless, negligent, terrible, etc.). Do not name individuals.
5. **When in doubt, choose the weaker option** (e.g. `incerta` over `concreta`, `generica` over `especifica`) and set `confianca` to `baixa` with a reason.
6. **All free text in English**: `resumo`, every `texto`, `perguntas_em_aberto`, `motivo_confianca_baixa`. Field names and enum values stay exactly as specified (they are in Portuguese).

## Procedure

1. Read the catalog description, then the whole document.
2. Fill `triagem` (what kind of document this is).
3. If `catalogo` is `nao` or `nao_verificavel`: set the four other classification fields to `null`, set `incidente` to `null`, and stop.
4. Otherwise fill `incidente`, field by field, finding the `trechos` first and writing `texto` from them.
5. Check: every `texto` is supported by its `trechos`; every enum value is from the lists below; uncertainty is preserved.
6. Output the JSON.

## `triagem`

**`catalogo`** — compare the document with the catalog description.
- `sim`: the document is mainly about the incident described in the catalog.
- `parcial`: the incident appears but is a small part of a text about something else, or the text mixes several incidents.
- `nao`: the document has content, but about a different incident or subject.
- `nao_verificavel`: there is no article content to compare (empty, or only menus/navigation).

**`autoria`** — `primaria`: written by the affected company or the provider responsible for the service. `secundaria`: written by a third party (press, encyclopedia, outside analyst, investigating body).

**`tipo`**
- `postmortem`: structured account after the incident (what happened, why, what will change).
- `atualizacoes_status`: updates published during the incident, with or without a post-mortem at the end.
- `relatorio_periodico`: report covering several incidents of a period (e.g. monthly availability report).
- `artigo_tecnico`: technical article where the incident is one part.
- `relatorio_formal`: long investigation, consulting or governance report.
- `noticia_enciclopedia`: news article or encyclopedia entry.
- `outro`: none of the above (mailing list, forum, issue, thread).

**`dominio`** — classify by the **origin** of the problem, not its effect.
- `software_servicos`: software, configuration, deployment, database, logical network, cloud, dependencies.
- `infra_fisica_datacenter`: power, cooling, hardware or physical network **inside a data center**.
- `seguranca`: the origin is a malicious action (intrusion, stolen credentials, malicious package, supply-chain attack).
- `fora_de_ti`: not an IT system (public power grid, aviation, space, healthcare, ships, industrial plants). Embedded software in such systems is still `fora_de_ti`.

**`seguranca`** — `nao`: no data exposure and no malicious action. `exposicao_dados`: user data exposed by a failure, without an attack. `ataque`: there was a malicious action (then `dominio` should be `seguranca`).

**`problemas_texto`** — list (possibly empty) of problems in the extracted text: `sem_conteudo` (only menus, navigation, page chrome), `comentarios` (reader comments included), `rodape_marketing` (footer, ads, job calls, newsletter prompts), `pdf_embaralhado` (columns or order of a PDF mixed up).

## `incidente`

**`resumo`** — 1 to 3 neutral sentences (max 600 characters): what failed, impact, how it ended. No `trechos` needed, but it must not say anything the other fields do not support.

**`data_incidente`** — `YYYY-MM-DD`, `YYYY-MM` or `YYYY`, only if the text states it. Otherwise `null`.

**`status_relatorio`** — `final` (complete report after the incident), `preliminar` (published while still investigating), `misto` (preliminary updates and a final report in the same text), `indefinido`.

**`servicos_afetados`** — services or products the text says were impacted. **`tecnologias`** — technical components the text names as involved (e.g. `PostgreSQL`, `BGP`, `Kubernetes`, `systemd`). Use the names as written; empty list if none.

**`categoria_causa`** — origin of the failure (`null` if `causa_raiz.status` is `ausente`):
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
- `other`: none of the above.

**`deteccao`** — `forma`: `alerta_automatico` (monitoring/alerting fired), `usuarios_clientes` (users or customers reported), `equipe_interna` (staff noticed without an alert), `terceiros` (another company, press), `nao_informada`. `descricao`: claim + `trechos`, or `null` if the text does not describe it.

**`gatilho`** — the event that **set off** the incident (a deploy, a capacity addition, a traffic spike, a power loss). `null` if the text does not distinguish it from the root cause.

**`causa_raiz`** — the **underlying** failure. Trigger and root cause are different: e.g. "a small capacity addition" (trigger) made servers exceed "the operating system's maximum thread limit" (root cause).
- `status`:
  - `concreta`: the text says **what** failed and **why**, with a technical mechanism someone else could look for in their own system.
  - `incerta`: hypotheses or a partial mechanism, and the text says the cause was not confirmed.
  - `vaga`: only a category or generic term ("a network issue", "an upstream provider").
  - `ausente`: the text does not say why it happened → `descricao` = `null`.

**`fatores_contribuintes`** — up to 6 conditions that made it worse or slowed recovery (e.g. retries amplifying load, missing alerts, circular dependency in monitoring). Each is a claim + `trechos`. Empty list if none.

**`mudanca_causadora`** — the configuration, code, version or parameter whose change set off the problem.
- `especifica`: the exact item is named (a parameter, file, version, rule, command).
- `generica`: the text says something changed but not exactly what.
- `nao_se_aplica`: the trigger was not a change (hardware failure, load, attack, latent bug without a change) → `descricao` = `null`.
- `ausente`: there was a change but the text does not say which → `descricao` = `null`.

**`mitigacao`** — what was done **during** the incident to restore service, in order.
- `especifica`: concrete steps (what was changed, in what order, which components).
- `generica`: only a generic action ("we rolled back", "we restarted", "we applied a fix").
- `ausente`: the text does not say how service came back → `passos` = `[]`.

**`prevencao`** — what will be done to avoid recurrence.
- `especificas`: concrete, verifiable actions (new limit, validation, test, alert, architecture change).
- `genericas`: intentions without detail ("we will improve our processes").
- `ausentes`: no prevention mentioned → `acoes` = `[]`.

**`duracao`** — `{"minutos": <integer>, "trechos": [...]}` only if the text states the duration or start and end times that let you compute it; otherwise `null`. If computed from start and end times, include both passages.

**`perguntas_em_aberto`** — things the text itself says remain unknown or under investigation. Empty list if none. Do not add your own questions.

## `confianca`

`alta` if you are confident in every classification. `baixa` if any field required a judgment call between two options; then `motivo_confianca_baixa` (English) says which field and why.

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
  "extracao": { "modelo": "<model name>", "data": "<YYYY-MM-DD>", "versao_prompt": "v1" }
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
