-- Esquema da busca da E2. Roda sozinho na primeira subida do container
-- (docker-entrypoint-initdb.d) e de novo a cada carga (carregar.py), sem erro: os ALTER do fim
-- atualizam um banco criado com a versão anterior.
--
-- Busca em duas etapas:
--   etapa 1: chunks com tipo 'resumo' ou 'texto' -> achar incidentes parecidos (agrupar por doc_id)
--   etapa 2: chunks com tipo = 'texto' dos documentos achados -> detalhes e evidência
-- Chunks com tipo = 'ficha' são opcionais (enriquecimento para os agentes) e não entram na busca.
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
    catalogo        text,                          -- sim | parcial (o texto cobre o incidente do catálogo?)
    resumo          text,                          -- resumo do incidente (vira o chunk de resumo)
    resumo_origem   text,                          -- danluu (escrito por pessoas) | gerado (LLM)
    problemas_texto text[] NOT NULL DEFAULT '{}',  -- rodape_marketing, comentarios, pdf_embaralhado...
    categoria_causa text,
    dominio         text,
    tipo_documento  text,
    seguranca       text,
    confianca       text,                          -- alta | baixa (da ficha, quando houver)
    ficha           jsonb,                         -- ficha completa, quando houver (opcional)
    texto           text,                          -- texto completo limpo do corpus
    UNIQUE (dataset, source_id)
);

CREATE TABLE IF NOT EXISTS chunks (
    chunk_id        text PRIMARY KEY,              -- '<doc_id>:<tipo>:...', ex. 'danluu:DAN-001:ficha:causa'
    doc_id          text NOT NULL REFERENCES documents(doc_id) ON DELETE CASCADE,
    dataset         text NOT NULL,
    tipo            text NOT NULL CONSTRAINT chunks_tipo_check CHECK (tipo IN ('resumo', 'texto', 'ficha')),
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

-- atualização de um banco criado antes do chunk de resumo (idempotente)
ALTER TABLE documents ADD COLUMN IF NOT EXISTS resumo text;
ALTER TABLE documents ADD COLUMN IF NOT EXISTS resumo_origem text;
ALTER TABLE chunks DROP CONSTRAINT IF EXISTS chunks_tipo_check;
ALTER TABLE chunks ADD CONSTRAINT chunks_tipo_check CHECK (tipo IN ('resumo', 'texto', 'ficha'));
