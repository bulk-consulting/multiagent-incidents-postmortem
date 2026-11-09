"""
Validação da ingestão no PostgreSQL + pgvector (entregável 2.5 da E2).

Confere no banco:
1. contagens por tabela, dataset e tipo de chunk, e a última carga;
2. integridade: todo documento tem chunk de resumo e chunks de texto; todo vetor tem 1024 dimensões e
   norma ~1 (vetores normalizados); nenhum chunk sem conteúdo; metadados preenchidos; chunks de
   ficha (opcionais) com trechos de evidência;
3. amostra de vetores (as primeiras dimensões de alguns chunks);
4. perguntas de teste (sintomas em português, da suíte de avaliação) pela busca em duas etapas,
   mostrando se o incidente esperado aparece e o trecho do texto que a etapa 2 devolve;
5. o resumo da avaliação completa (ingestion/avaliacao/resultados/qwen3.json, índice resumo+texto),
   se existir.

Imprime no terminal e grava o relatório em ingestion/banco/validacao_ingestao.md.
Sai com código 1 se alguma checagem de integridade falhar.

Uso (a partir da raiz do repositório, com o container de pé):
    multiagent_env/bin/python -I ingestion/banco/validar_ingestao.py
"""
from __future__ import annotations

import importlib.util
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PASTA = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location("busca", PASTA / "busca.py")
busca = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(busca)

# perguntas de sintoma em português da suíte própria (ingestion/avaliacao/suite_propria.json)
PERGUNTAS = [
    ("DAN-189", "Todos os servidores do datacenter reiniciaram de uma vez, logo depois de um operador rodar uma "
                "ferramenta para reiniciar alguns servidores em manutenção."),
    ("DAN-043", "Acabamos de apagar o banco de dados de produção sem querer, e o último backup é de horas atrás."),
    ("DAN-086", "Hoje, 29 de fevereiro, desde a meia-noite os certificados estão sendo rejeitados e a criação de "
                "novas instâncias falha em toda a plataforma."),
    ("DAN-017", "Depois de um deploy, um serviço central passou a responder 401 para todas as requisições e vários "
                "produtos que dependem dele estão falhando."),
]


def main() -> None:
    linhas: list[str] = []
    falhas: list[str] = []

    def out(texto: str = "") -> None:
        print(texto)
        linhas.append(texto)

    with busca._carregar.conectar() as con, con.cursor() as cur:
        def um(sql: str, *p):
            cur.execute(sql, p)
            return cur.fetchone()

        def todos(sql: str, *p):
            cur.execute(sql, p)
            return cur.fetchall()

        out(f"# Validação da ingestão — {datetime.now():%Y-%m-%d %H:%M}")
        out()
        out("## 1. Contagens")
        out()
        out("| tabela | dataset | tipo | linhas | tokens médios |")
        out("|---|---|---|---|---|")
        for ds, n in todos("SELECT dataset, count(*) FROM documents GROUP BY dataset ORDER BY 1"):
            out(f"| documents | {ds} | — | {n} | — |")
        for ds, tipo, n, tok in todos("SELECT dataset, tipo, count(*), round(avg(tokens)) FROM chunks "
                                      "GROUP BY dataset, tipo ORDER BY 1, 2"):
            out(f"| chunks | {ds} | {tipo} | {n} | {tok} |")
        carga = um("SELECT modelo, feita_em, documentos, chunks, origem FROM cargas ORDER BY id DESC LIMIT 1")
        if carga:
            out()
            out(f"Última carga: {carga[2]} documentos e {carga[3]} chunks, modelo {carga[0]}, "
                f"em {carga[1].astimezone():%Y-%m-%d %H:%M}, {carga[4]}.")

        out()
        out("## 2. Integridade")
        out()
        checagens = [
            ("documentos sem chunk de resumo",
             "SELECT count(*) FROM documents d WHERE NOT EXISTS "
             "(SELECT 1 FROM chunks c WHERE c.doc_id = d.doc_id AND c.tipo = 'resumo')", 0),
            ("documentos sem chunk de texto",
             "SELECT count(*) FROM documents d WHERE NOT EXISTS "
             "(SELECT 1 FROM chunks c WHERE c.doc_id = d.doc_id AND c.tipo = 'texto')", 0),
            ("vetores com dimensão diferente de 1024", "SELECT count(*) FROM chunks WHERE vector_dims(embedding) <> 1024", 0),
            ("vetores com norma fora de 1 ± 0,01", "SELECT count(*) FROM chunks WHERE abs(vector_norm(embedding) - 1) > 0.01", 0),
            ("chunks sem conteúdo", "SELECT count(*) FROM chunks WHERE length(trim(content)) = 0", 0),
            # o resumo da ficha não tem trechos próprios (só a detecção, quando descrita); os demais têm
            ("chunks de causa, mitigação ou prevenção sem trechos de evidência",
             "SELECT count(*) FROM chunks WHERE tipo = 'ficha' AND assunto <> 'resumo' "
             "AND jsonb_array_length(trechos) = 0", 0),
            ("chunks de resumo diferentes do resumo do documento",
             "SELECT count(*) FROM chunks c JOIN documents d USING (doc_id) "
             "WHERE c.tipo = 'resumo' AND c.content IS DISTINCT FROM d.resumo", 0),
            ("documentos sem título, URL ou empresa",
             "SELECT count(*) FROM documents WHERE title IS NULL OR url IS NULL OR company IS NULL", 0),
        ]
        out("| checagem | resultado | esperado |")
        out("|---|---|---|")
        for nome, sql, esperado in checagens:
            valor = um(sql)[0]
            ok = valor == esperado
            if not ok:
                falhas.append(f"{nome}: {valor}")
            out(f"| {nome} | {valor} {'✔' if ok else '✘'} | {esperado} |")

        out()
        out("## 3. Amostra de vetores")
        out()
        out("| chunk | tipo | dimensões | norma | primeiras 5 dimensões |")
        out("|---|---|---|---|---|")
        for cid, tipo, dims, norma, vetor in todos(
                "SELECT chunk_id, tipo, vector_dims(embedding), vector_norm(embedding), embedding FROM chunks "
                "WHERE chunk_id IN ('danluu:DAN-189:resumo', 'danluu:DAN-043:texto:000', "
                "'danluu:DAN-086:ficha:mitigacao') ORDER BY 1"):
            out(f"| {cid} | {tipo} | {dims} | {norma:.4f} | {', '.join(f'{x:+.4f}' for x in vetor.to_list()[:5])} |")

    out()
    out("## 4. Perguntas de teste (busca em duas etapas)")
    out()
    acertos = 0
    for esperado, pergunta in PERGUNTAS:
        resultado = busca.buscar(pergunta, n_docs=3, n_trechos=1)
        ids = [r["doc_id"].split(":", 1)[1] for r in resultado]
        pos = ids.index(esperado) + 1 if esperado in ids else None
        acertos += pos is not None
        out(f"**Pergunta:** {pergunta}")
        out()
        out(f"Esperado: {esperado} → {'posição ' + str(pos) if pos else 'fora do top-3'}")
        out()
        for k, r in enumerate(resultado, 1):
            marca = " ← esperado" if r["doc_id"].endswith(esperado) else ""
            out(f"{k}. `{r['doc_id']}` ({r['similaridade']:.3f}) {r['company']} — {r['title']}{marca}")
            if k == 1:
                m = r["melhor_chunk"]
                out(f"   - resumo: {(r['resumo'] or '')[:220]}")
                out(f"   - achado pelo chunk de {m['tipo']}" + (f" [{m['secao']}]" if m["secao"] else ""))
                if r["detalhes"]:
                    d = r["detalhes"][0]
                    out(f"   - texto, etapa 2 [{d['secao'] or 'sem seção'}]: {d['content'][:220].replace(chr(10), ' ')}")
        out()
    out(f"Incidente esperado no top-3: {acertos} de {len(PERGUNTAS)} perguntas.")

    res = ROOT / "ingestion" / "avaliacao" / "resultados" / "qwen3.json"
    casos = [l for l in json.loads(res.read_text(encoding="utf-8"))["casos"]
             if l["esperado"] and l["suite"] != "mari"] if res.exists() else []
    if casos and all("resumo+texto" in l for l in casos):
        out()
        out("## 5. Avaliação completa (índice resumo+texto, Qwen3)")
        out()
        out("| recorte | perguntas | 1º lugar | top-5 |")
        out("|---|---|---|---|")
        for nome, f in [("todas", lambda l: True),
                        ("sintoma em português", lambda l: l["variante"] == "sintoma" and l["idioma"] == "pt"),
                        ("sintoma, difíceis", lambda l: l["variante"] == "sintoma" and l["dificuldade"] == "hard")]:
            sel = [l for l in casos if f(l)]
            h1 = sum(1 for l in sel if l["resumo+texto"]["rank"] == 1) / len(sel)
            h5 = sum(1 for l in sel if l["resumo+texto"]["rank"] and l["resumo+texto"]["rank"] <= 5) / len(sel)
            out(f"| {nome} | {len(sel)} | {h1:.0%} | {h5:.0%} |")
        out()
        out("Detalhes em ingestion/avaliacao/RESULTADOS.md.")

    out()
    out("**Resultado:** " + ("todas as checagens de integridade passaram." if not falhas
                             else "FALHAS: " + "; ".join(falhas)))
    (PASTA / "validacao_ingestao.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"\nrelatório -> {(PASTA / 'validacao_ingestao.md').relative_to(ROOT)}")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
