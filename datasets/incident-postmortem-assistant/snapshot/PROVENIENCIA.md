# Snapshot do incident-postmortem-assistant (evidência e reúso dos testes)

- Origem: https://github.com/kai2055/incident-postmortem-assistant
- Commit: d9e70a5b802faf5c693e709f1a97c9b78bbd0a24 (2026-10-02)
- Copiado em: 2026-10-30
- Licença: o repositório não tem arquivo de licença; uso interno, com citação

Removidos de propósito: .git/, docs/img/, docs/screenshots/

Uso previsto:
- data/eval/layer2_suite.json e data/eval/query_suite.json: base para a avaliação de busca
- decisions/: referência de arquitetura para a E1.4

NÃO INDEXAR corpus/raw/ NO RAG: são reescritas por LLM (ver ../README.md).
