"""Validação da ingestão no PostgreSQL + pgvector.

1. Conta incidentes e chunks.
2. Mostra uma amostra de embedding.
3. Faz buscas com descrições simples de incidentes conhecidos e confere se o
   incidente esperado aparece entre os 5 primeiros resultados.
"""

import psycopg
from pgvector.psycopg import register_vector
from sentence_transformers import SentenceTransformer

from search import DATABASE_URL, MODEL, search

# Descrição do incidente (em português) -> incidente que deveria aparecer
TESTES = [
    ("um administrador cansado apagou o diretório errado e perdemos seis horas de dados", "DAN-164"),
    ("um comando digitado errado removeu servidores demais e derrubou o armazenamento S3", "DAN-104"),
    ("um certificado expirou e os complementos do navegador Firefox pararam de funcionar", "DAN-090"),
    ("raios atingiram o datacenter e causaram queda de energia nos discos", "DAN-071"),
    ("um deploy com versões diferentes do código causou prejuízo de 460 milhões de dólares", "DAN-084"),
    ("o cliente do Steam apagou todos os arquivos do computador do usuário", "DAN-236"),
]


def main() -> None:
    model = SentenceTransformer(MODEL)
    with psycopg.connect(DATABASE_URL) as conn:
        register_vector(conn)

        print("1. Contagem")
        print(f"   incidentes: {conn.execute('SELECT count(*) FROM incident').fetchone()[0]}")
        for chunk_type, total in conn.execute("SELECT chunk_type, count(*) FROM chunk GROUP BY 1 ORDER BY 1"):
            print(f"   chunks {chunk_type}: {total}")

        chunk_id, embedding = conn.execute(
            "SELECT chunk_id, embedding FROM chunk ORDER BY chunk_id LIMIT 1").fetchone()
        embedding = embedding.to_list()
        print("\n2. Amostra de embedding")
        print(f"   {chunk_id}: {len(embedding)} dimensões, início {[round(float(x), 4) for x in embedding[:5]]}")

        print("\n3. Buscas de teste")
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
