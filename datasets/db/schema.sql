-- Tabelas do RAG. Criadas por embed.py a cada carga (a carga apaga e recria as tabelas,
-- porque o tamanho do vetor muda junto com o modelo de embeddings).
CREATE EXTENSION IF NOT EXISTS vector;

-- Um registro por post-mortem público (a base de conhecimento do RAG)
CREATE TABLE IF NOT EXISTS post_mortems (
    post_mortem_id TEXT PRIMARY KEY,                 -- DAN-011 (o catalog_id do catálogo da danluu)
    dataset        TEXT NOT NULL DEFAULT 'danluu',   -- de onde veio o post-mortem
    company        TEXT NOT NULL,
    title          TEXT NOT NULL,
    source_url     TEXT NOT NULL,
    category       TEXT NOT NULL,
    incident_date  DATE  -- data do incidente descrito; a danluu não traz a data em um campo próprio
);

-- Um registro por chunk de um post-mortem, com o vetor
CREATE TABLE IF NOT EXISTS chunk (
    chunk_id       TEXT PRIMARY KEY,                 -- DAN-011-001
    post_mortem_id TEXT NOT NULL REFERENCES post_mortems (post_mortem_id),
    chunk_type     TEXT NOT NULL,                    -- summary ou text
    content        TEXT NOT NULL,
    embedding      VECTOR(1024) NOT NULL             -- Qwen3-Embedding-0.6B
);
