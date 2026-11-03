# Self-review of the fichas (second pass)

You have written every ficha of the batch and the validator passed. Now review each ficha **again, one at a time**, against its own prompt file (the document and the rules). This pass looks for the mistakes that most often survive the first pass. For each ficha, check every item below and fix what is wrong, in the ficha itself.

## Checklist, per ficha

1. **Each detail has its own `trecho`.** For every `texto` (including every step of `mitigacao` and every action of `prevencao`), list each time, date, number, name, place, actor and result it states. Each one must appear in a `trecho` of that same claim. Times that only appear in a summary paragraph ("unavailable from 16:06 to 18:53 UTC") need that sentence as a `trecho`. If a detail is not supported, add the passage or remove the detail.
2. **Nothing is written as done that the text does not say was done.** Look for "decided", "the decision was made", "planned", "scheduled", "asked X to", "called X to", "tried to", "worked to", "focused on", "devised", "to determine", "to ensure", "to check", "was being restored". Write these as a decision, request, attempt, purpose or ongoing work, not as a result.
3. **No causal link the text does not state** ("so", "because", "which caused", "until"), also in `resumo`.
4. **Uncertainty kept**: "may have", "likely", "appears", "we believe" stay as they are, also in `resumo`.
5. **`mitigacao`** contains only actions that changed something to restore service, before the impact ended. Out: opening an incident, assembling a team, investigating, monitoring, detecting the cause, communicating, and actions after the impact ended. `nivel` is `especifica` if at least one step says what was changed and in which component.
6. **`fatores_contribuintes`** are conditions that made it worse, delayed detection or slowed recovery. Out: the impact itself, a step of the root-cause mechanism, the normal behaviour of the system, mitigation steps restated, delays in communicating, statements about a person.
7. **`deteccao.descricao`** has the first symptom noticed when the text gives it (even if `forma` is `nao_informada`), and no response steps.
8. **`confianca`**: for each field named in `motivo_confianca_baixa`, reread that field's definition. If the definition picks one value, use it, move the note to `observacoes` and set `alta` if no other doubt is left. Keep `baixa` only where you can quote the part of the definition that both values satisfy.
9. **`problemas_texto`**: footers, mailing-list footers, "advertising"/"careers" links and calls to subscribe or contribute are `rodape_marketing`.

## Then

- Run the validator again on the batch.
- In your final message, list for each ficha what you changed in this pass (or "no change"), e.g. "DAN-123: added trecho for 18:53 in mitigacao[3]; 'decided at 19:15' instead of 'scaled'; confianca baixa → alta".
