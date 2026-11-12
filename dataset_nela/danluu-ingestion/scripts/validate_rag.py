"""Validação da ingestão no PostgreSQL + pgvector.

1. Conta incidentes e chunks e compara com data/chunks/danluu_chunks.jsonl.
2. Checagens de integridade (dimensões, norma dos vetores, incidentes sem chunks...).
3. Mostra uma amostra de embedding.
4. Faz buscas com descrições simples de incidentes conhecidos e confere se o
   incidente esperado aparece entre os 5 primeiros resultados.
"""

import json
from pathlib import Path

import psycopg
from pgvector.psycopg import register_vector

from search import DATABASE_URL, DIMENSIONS, load_model, search

CHUNKS = Path(__file__).resolve().parent.parent / "data" / "chunks" / "danluu_chunks.jsonl"

# Descrição do incidente (em inglês, o idioma do corpus) -> incidente que deveria aparecer
TESTES = [
    ("a tired administrator deleted the wrong directory and we lost six hours of data", "DAN-164"),
    ("a mistyped command removed too many servers and took down S3 storage", "DAN-104"),
    ("a certificate expired and Firefox browser add-ons stopped working", "DAN-090"),
    ("lightning strikes hit the datacenter and caused power loss on the disks", "DAN-071"),
    ("a deploy with different versions of the code caused a loss of 460 million dollars", "DAN-084"),
    ("the Steam client deleted all files on the user's computer", "DAN-236"),
]

# (descrição, SQL que devolve o número de problemas)
CHECAGENS = [
    ("vetores com outra dimensão", f"SELECT count(*) FROM chunk WHERE vector_dims(embedding) <> {DIMENSIONS}"),
    ("vetores sem norma 1 (não normalizados)", "SELECT count(*) FROM chunk WHERE abs(vector_norm(embedding) - 1) > 0.01"),
    ("chunks com texto vazio", "SELECT count(*) FROM chunk WHERE trim(content) = ''"),
    ("incidentes sem nenhum chunk",
     "SELECT count(*) FROM incident i WHERE NOT EXISTS (SELECT 1 FROM chunk c WHERE c.catalog_id = i.catalog_id)"),
    ("incidentes sem chunk de summary",
     "SELECT count(*) FROM incident i WHERE NOT EXISTS "
     "(SELECT 1 FROM chunk c WHERE c.catalog_id = i.catalog_id AND c.chunk_type = 'summary')"),
    ("tipos de chunk desconhecidos", "SELECT count(*) FROM chunk WHERE chunk_type NOT IN ('summary', 'text')"),
    ("chunks com o mesmo vetor de outro chunk",
     "SELECT count(*) FROM (SELECT embedding FROM chunk GROUP BY embedding HAVING count(*) > 1) d"),
]


def main() -> None:
    esperados = [json.loads(line)["chunk_id"] for line in CHUNKS.open(encoding="utf-8")]
    with psycopg.connect(DATABASE_URL) as conn:
        register_vector(conn)

        print("1. Contagem")
        print(f"   incidentes: {conn.execute('SELECT count(*) FROM incident').fetchone()[0]}")
        for chunk_type, total in conn.execute("SELECT chunk_type, count(*) FROM chunk GROUP BY 1 ORDER BY 1"):
            print(f"   chunks {chunk_type}: {total}")
        no_banco = {row[0] for row in conn.execute("SELECT chunk_id FROM chunk")}
        faltando = [c for c in esperados if c not in no_banco]
        print(f"   chunks do arquivo de chunking: {len(esperados)} | fora do banco: {len(faltando)}"
              + (f" (ex.: {', '.join(faltando[:3])})" if faltando else ""))

        print("\n2. Integridade")
        problemas = 0
        for descricao, sql in CHECAGENS:
            n = conn.execute(sql).fetchone()[0]
            problemas += n
            print(f"   {'OK  ' if n == 0 else 'ERRO'} {descricao}: {n}")
        print(f"   {'tudo certo' if problemas == 0 else f'{problemas} problema(s)'}")

        chunk_id, embedding = conn.execute(
            "SELECT chunk_id, embedding FROM chunk ORDER BY chunk_id LIMIT 1").fetchone()
        embedding = embedding.to_list()
        print("\n3. Amostra de embedding")
        print(f"   {chunk_id}: {len(embedding)} dimensões, início {[round(float(x), 4) for x in embedding[:5]]}")

        print("\n4. Buscas de teste")
        model = load_model()
        acertos = 0
        for texto, esperado in TESTES:
            ids = [row[0].rsplit("-", 1)[0] for row in search(conn, model, texto)]
            posicao = ids.index(esperado) + 1 if esperado in ids else None
            acertos += posicao is not None
            resultado = f"OK (posição {posicao})" if posicao else "não encontrado no top 5"
            print(f"   [{esperado}] {texto}\n      -> {resultado}")

        print(f"\n   Acertos: {acertos} de {len(TESTES)}")


if __name__ == "__main__":
    main()
