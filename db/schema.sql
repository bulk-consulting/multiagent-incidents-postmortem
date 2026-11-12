-- Tabelas do RAG. Criadas por embed.py a cada carga (a carga apaga e recria as tabelas,
-- porque o tamanho do vetor muda junto com o modelo de embeddings).
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS incident (
    catalog_id    TEXT PRIMARY KEY,
    dataset       TEXT NOT NULL DEFAULT 'danluu',  -- de onde veio o incidente
    company       TEXT NOT NULL,
    title         TEXT NOT NULL,
    source_url    TEXT NOT NULL,
    category      TEXT NOT NULL,
    incident_date DATE  -- a danluu não traz a data em um campo próprio
);

CREATE TABLE IF NOT EXISTS chunk (
    chunk_id   TEXT PRIMARY KEY,
    catalog_id TEXT NOT NULL REFERENCES incident (catalog_id),
    chunk_type TEXT NOT NULL,  -- summary ou text
    content    TEXT NOT NULL,
    embedding  VECTOR(1024) NOT NULL  -- Qwen3-Embedding-0.6B
);
