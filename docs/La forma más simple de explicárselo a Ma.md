
**Estructura de carpetas sugerida**
```
app/
  api/          # routers FastAPI (endpoints)
  schemas/      # modelos Pydantic (entrada/salida)
  services/     # lógica: nueva vs refinamiento, estructurar complemento
  agents/       # grafo LangGraph: agente 1 (RAG), agente 2 (análisis), nodos de decisión
  rag/          # chunking, embeddings, búsqueda vectorial
  db/           # modelos y repositorios Postgres/pgvector
  core/         # config, auth, logging
```

**Endpoints mínimos** (siguiendo tu diagrama)
- `POST /incidents` → crea investigación, devuelve `incident_id` y estado
- `POST /incidents/{id}/complements` → complemento o refinamiento
- `GET /incidents/{id}` → estado (`investigando`, `aguardando_informacoes`, `pendente_revisao`, `concluido`) e informe
- `POST /incidents/{id}/review` → aprobación de la revisión humana

Como la investigación puede tardar, conviene que el POST responda rápido (202) y el frontend consulte el estado con el GET.
