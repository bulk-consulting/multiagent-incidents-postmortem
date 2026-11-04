-- Esquema da busca da E2 (solução do André). Roda sozinho na primeira subida do container
-- (docker-entrypoint-initdb.d) e pode ser rodado de novo sem erro.
--
-- Busca em duas etapas:
--   etapa 1: chunks com tipo = 'ficha'  -> achar incidentes parecidos (agrupar por doc_id)
--   etapa 2: chunks com tipo = 'texto' dos documentos achados -> detalhes e evidência
-- Similaridade de cosseno: 1 - (embedding <=> vetor_da_pergunta). Os vetores já são normalizados.
-- Sem índice vetorial por enquanto: com alguns milhares de chunks a busca exata é rápida.

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS documents (
    doc_id          text PRIMARY KEY,              -- '<dataset>:<id de origem>', ex. 'danluu:DAN-001'
    dataset         text NOT NULL,                 -- de onde veio (por enquanto só 'danluu')
    source_id       text NOT NULL,                 -- id no dataset de origem, ex. 'DAN-001'
    company         text,
    title           text,
    page_title      text,                          -- título original da página, quando foi corrigido
    url             text,
    incident_date   text,                          -- texto: pode ser parcial ('2015-07')
    text_source     text,                          -- original | reextraido | reextraido_corpus
    catalogo        text,                          -- sim | parcial (cobertura da ficha)
    problemas_texto text[] NOT NULL DEFAULT '{}',  -- rodape_marketing, comentarios, pdf_embaralhado...
    categoria_causa text,
    dominio         text,
    tipo_documento  text,
    seguranca       text,
    confianca       text,                          -- alta | baixa (da ficha)
    ficha           jsonb,                         -- ficha completa, para o agente mostrar
    texto           text,                          -- texto completo limpo do corpus
    UNIQUE (dataset, source_id)
);

CREATE TABLE IF NOT EXISTS chunks (
    chunk_id        text PRIMARY KEY,              -- '<doc_id>:<tipo>:...', ex. 'danluu:DAN-001:ficha:causa'
    doc_id          text NOT NULL REFERENCES documents(doc_id) ON DELETE CASCADE,
    dataset         text NOT NULL,
    tipo            text NOT NULL CHECK (tipo IN ('ficha', 'texto')),
    assunto         text,                          -- fichas: resumo | causa | mitigacao | prevencao
    secao           text,                          -- texto: título da seção (pode ser vazio)
    ordem           integer,                       -- texto: posição no documento
    content         text NOT NULL,                 -- o que o agente mostra
    texto_embedding text NOT NULL,                 -- o que virou vetor (cabeçalho + texto normalizado)
    tokens          integer,
    trechos         jsonb NOT NULL DEFAULT '[]',   -- fichas: trechos literais que provam o chunk
    modelo          text NOT NULL,                 -- modelo que gerou o vetor
    embedding       vector(1024) NOT NULL
);

CREATE INDEX IF NOT EXISTS chunks_dataset_tipo ON chunks (dataset, tipo);
CREATE INDEX IF NOT EXISTS chunks_doc ON chunks (doc_id);

CREATE TABLE IF NOT EXISTS cargas (
    id          serial PRIMARY KEY,
    dataset     text NOT NULL,
    modelo      text NOT NULL,
    feita_em    timestamptz NOT NULL DEFAULT now(),
    documentos  integer NOT NULL,
    chunks      integer NOT NULL,
    origem      text                               -- commit/arquivos de onde veio a carga
);
