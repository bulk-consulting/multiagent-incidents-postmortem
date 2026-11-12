# Snapshot da IncidentDB (somente para evidência)

- Origem: https://github.com/trobasuj-cpu/incidentdb
- Commit: 925ac05a5f15283cae26e12dac51a5c4839d4277 (2026-10-05)
- Copiado em: 2026-10-30
- Licença: MIT (ver LICENSE)
- Integridade (md5):
  - data/incident_database.jsonl  0dca310c40200263e27959599a20c56a
  - src/crawler.py                5d096ea409462078d03bd2253bfbe023

Removidos de propósito:
- rag_vault/ — runbooks Markdown com campos gerados por template. NÃO indexar.
- notebook/ e .git/

Evidência principal do veredito: src/crawler.py, função parse_raw_incident,
onde breaking_config_code, remediation_patch e prevention_checklist são montados
com texto fixo. Ver ../../README.md.

NÃO USAR ESTES DADOS NO RAG.
