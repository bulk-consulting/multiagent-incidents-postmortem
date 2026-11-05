-- Tabelas do RAG. Pode ser executado várias vezes: só cria o que não existe.
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS incident (
    catalog_id    TEXT PRIMARY KEY,
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
    embedding  VECTOR(768) NOT NULL
);
