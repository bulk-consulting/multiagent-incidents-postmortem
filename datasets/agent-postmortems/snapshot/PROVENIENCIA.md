# Snapshot do agent-postmortems

- Origem: https://github.com/swarmproof/agent-postmortems
- Commit: 99de604a587bfba55591270ab3d5021b8b342b37 (2026-10-26; o mesmo avaliado em 2026-10-30)
- Copiado em: 2026-11-02
- Licenças: código Apache-2.0 (LICENSE), dados CC-BY-4.0 (LICENSE-DATA)
- Integridade (md5):
  - SCHEMA.md                    f1e9b9149808d0a58e16f4d20e4d5b6c
  - schema/incident.schema.json  d3f8d50d2ba7e9cebae876c5475f8a61
  - schema/taxonomy.yaml         b36685045df14cee43478a78b7a329bb

Removidos de propósito:
- .git/
- .claude/ — configuração de agente do Claude Code criada pelos autores do repositório;
  conteúdo baixado não deve definir agentes neste projeto.

Adicionado:
- referencia/incident-curator.md — o mesmo `.claude/agents/incident-curator.md` do commit acima,
  baixado de raw.githubusercontent.com e guardado fora de `.claude/` apenas como texto de
  referência (padrão de curadoria por LLM). md5 88d065659a99bc04951c527fd672cca9

Uso: referência de schema (gatilho separado da causa raiz, fatores contribuintes,
confiança, fontes obrigatórias) para a ficha extraída dos post-mortems do danluu.
Fora do escopo do RAG (falhas de agentes de IA, não de infraestrutura). Ver ../README.md.
