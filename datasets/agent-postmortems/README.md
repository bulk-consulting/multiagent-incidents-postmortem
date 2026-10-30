# Avaliação — agent-postmortems

Avaliação feita em 30/10/2026 do repositório
[swarmproof/agent-postmortems](https://github.com/swarmproof/agent-postmortems),
commit `99de604a587bfba55591270ab3d5021b8b342b37` (26/10/2026).
Licenças: código Apache-2.0, dados CC-BY-4.0.

## Veredito

**Não usar no RAG do Incident Copilot: fora do escopo.** É uma base real e bem documentada, mas de
**falhas de agentes de IA** (injeção de prompt, vazamento de dados, agentes executando ações destrutivas),
não de incidentes de infraestrutura como os da Stratus.

**Serve como referência de segurança para o próprio Copilot**, que é um sistema multi-agente: os casos de
agentes que apagaram bancos de produção mostram por que o Copilot deve só recomendar, nunca executar
ações sem aprovação humana. O schema também é uma boa referência de modelagem.

## O que tem

| Item | Valor |
|---|---|
| Registros | 63 (34 incidentes reais, 29 riscos demonstrados ou quase-incidentes) |
| Período | 2023–2026 (36 de 2026, 22 de 2025) |
| Formato | Um YAML por incidente em `incidents/`; exportação completa em `export/incidents.json` |
| Fontes | 2 a 4 links públicos por registro (notícias 79, pesquisa primária 53, divulgação de fornecedor 8, outras) |
| Atualização | Ativa; contagem e exportação regeneradas automaticamente a cada merge |

**Classe de falha principal:** prompt injection (22), uso autônomo indevido (8), agência excessiva (8),
alucinação (4), comprometimento de cadeia de suprimentos (4), reward hacking (4), falha multi-agente (3),
ação insegura (3), outras (7).

Campos de cada registro: título, resumo, data, tipo, status, confiança, severidade (com justificativa),
sistema, classe principal e cadeia de classes de falha, vetor de ataque, causa, gatilho, causa raiz, fatores
contribuintes, detecção, recuperação, prevenção, raio de impacto, IDs externos (CVE/CWE), mapeamentos
(OWASP LLM, OWASP Agentic, MITRE ATLAS), tags e fontes.

## Por que está fora do escopo

- Os sistemas envolvidos são chatbots, assistentes de código, servidores MCP e navegadores com IA, não
  servidores, clusters Kubernetes ou microsserviços.
- As causas são de segurança e comportamento de modelo (injeção de prompt, jailbreak, reward hacking),
  não de operação (configuração, capacidade, rede, banco de dados).
- Quase metade dos registros são riscos demonstrados, não incidentes que aconteceram.

Os três casos mais próximos de operação são agentes que apagaram dados de produção:
`2025-replit-prod-db-deletion`, `2026-pocketos-cursor-db-deletion` e
`2026-openclaw-email-deletion-context-compaction`.

## O que vale aproveitar

- **Requisitos de segurança do Copilot (E1.2/E1.4):** os casos de ação destrutiva e de agência excessiva
  justificam que o Copilot apenas recomende remediações, com aprovação humana explícita para qualquer ação.
  Os casos de injeção de prompt alertam que post-mortems e logs indexados são dados, não instruções.
- **Referência de schema:**
  - cadeia de classes de falha em vez de um rótulo único (`failure_classes`);
  - campo `confidence` e separação entre incidente real e risco demonstrado (`incident_type`);
  - registros contestados são anotados, nunca apagados (ADR 0008);
  - toda afirmação exige fonte pública com link, verificada em CI.
