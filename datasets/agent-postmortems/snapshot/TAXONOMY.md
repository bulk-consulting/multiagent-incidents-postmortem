# The Agent Failure Taxonomy

**Version 1.0** — rendered from [`schema/taxonomy.yaml`](./schema/taxonomy.yaml), the machine authority file. If this document and the YAML disagree, the YAML wins.

An incident is classified as an **ordered chain** of `class`/`subclass` pairs (`failure_classes`) — real agent failures are causal sequences, not single labels. The first entry must equal `primary_failure_class`.

Governance: adding or renaming a class/subclass bumps `taxonomy_version` and requires an ADR (see [`adr/`](./adr/)). `other` is always allowed as an escape hatch but requires descriptive `tags`. Every class maps to cairn-protocol's failure taxonomy via `cairn_map`; divergences are flagged in an ADR.

| Class | Definition | Subclasses | cairn map |
|---|---|---|---|
| `prompt-injection` | Untrusted input overrides intended instructions | `direct` · `indirect` · `multimodal` · `tool-metadata` | injection |
| `jailbreak` | Safety/guardrail circumvention of the model itself | `role-play` · `obfuscation` · `system-prompt-leak` · `direct-elicitation` | guardrail-bypass |
| `tool-misuse` | Agent invokes a tool wrongly/over-broadly | `wrong-tool` · `over-broad-scope` · `unvalidated-args` | tool-misuse |
| `unsafe-action` | Destructive/irreversible action taken (often against instructions) | `data-deletion` · `unauthorized-write` · `prod-mutation` · `cross-domain-action` | unsafe-action |
| `data-exfiltration` | Sensitive data leaves its trust boundary | `via-tool` · `via-output` · `cross-repo` | data-exfiltration |
| `excessive-agency` | Agent acts beyond granted authority/scope | `missing-approval-gate` · `scope-creep` | excessive-agency |
| `runaway-loop` | Non-terminating / repeating action loop | `retry-storm` · `self-trigger` | runaway-loop |
| `cost-blowup` | Denial-of-wallet / unbounded spend | `token-spiral` · `tool-call-spiral` · `mispriced-action` | cost-blowup |
| `double-side-effect` | Non-idempotent action fires more than once | `duplicate-payment` · `duplicate-message` | double-side-effect |
| `hallucination` | Confidently-wrong output presented as fact | `fabricated-policy` · `fabricated-capability` · `false-state` | hallucination |
| `reward-hacking` | Optimizes the metric, not the goal (spec-gaming) | `eval-exploit` · `metric-gaming` | reward-hacking |
| `goal-misalignment` | Pursues an unintended objective | `goal-hijack` · `sycophancy-to-harm` | misalignment |
| `memory-context-poisoning` | Malicious/false content persisted into memory/RAG | `rag-poisoning` · `memory-injection` | context-poisoning |
| `supply-chain-compromise` | Malicious code/config enters the agent stack | `dependency` · `extension` · `mcp-server` | supply-chain |
| `insecure-output` | Agent-generated artifact is unsafe (code/config) | `secret-exposure` · `injection-vuln` · `broken-authz` | insecure-output |
| `multi-agent-failure` | Emergent failure from agent-to-agent interaction | `collusion` · `cascade` · `deadlock` | multi-agent |
| `task-failure` | Fails the intended task (quality/comprehension) | `misunderstanding` · `quality-degradation` | task-failure |
| `autonomous-misuse` | Agent capabilities weaponized for abuse at scale | `cyber-ops` · `fraud-automation` | autonomous-misuse |
| `other` | Escape hatch pending classification (must add `tags`) | — | other |

## Examples in the wild

Real incidents from the corpus, referenced per class:

- `reward-hacking` — [`2025-sakana-ai-cuda-reward-hacking`](https://swarmproof.github.io/agent-postmortems/2025-sakana-ai-cuda-reward-hacking/): an AI CUDA kernel optimizer exploited a flaw in its evaluation harness to report apparent speedups it did not actually achieve.

## Classifying an incident

1. Identify the **causal sequence**: what class of failure happened first, and what did it lead to? E.g. a poisoned tool description is `prompt-injection/tool-metadata` → `data-exfiltration/via-tool`.
2. Set `primary_failure_class` to the first (inducing) class in the chain.
3. Pick the most specific subclass; omit `subclass` if none fits rather than forcing one.
4. If nothing fits, use `other` **and** add `tags` describing the failure — that's the signal a taxonomy extension may be needed.
