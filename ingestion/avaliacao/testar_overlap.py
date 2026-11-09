"""
Testa sobreposição (overlap) nos chunks de texto: os chunks atuais (sem overlap) contra três
variantes, avaliadas sozinhas e junto com o chunk de resumo, nas 278 perguntas, com o Qwen3.

Variantes (o overlap entra só no texto que vira vetor; o `content` mostrado ao agente não muda):
- A: limite 450 + as últimas frases do chunk anterior da mesma seção, até ~60 tokens;
- B: limite 390 + ~60 tokens da mesma seção (fica perto dos 450);
- C: limite 390 + ~60 tokens do chunk anterior, mesmo de outra seção.

Gera os vetores na hora (~9 min na GPU) e não grava nada: só imprime a tabela. Resultado e
decisão em ingestion/avaliacao/RESULTADOS.md.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/avaliacao/testar_overlap.py
"""

import csv, importlib.util, json, re, sys, os, time
os.environ.setdefault("TRANSFORMERS_VERBOSITY","error"); os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS","1")
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[2]; OV = 60
def mod(p, n):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
ct = mod(ROOT/"ingestion/corpus/chunk_texto.py", "ct"); g = mod(ROOT/"ingestion/corpus/gerar_embeddings.py", "g")
av = mod(ROOT/"ingestion/avaliacao/avaliar.py", "av")
contar, metodo = ct.escolher_contador([]); print("contagem:", metodo, flush=True)
docs_c = [json.loads(l) for l in open(ROOT/"ingestion/corpus/corpus.jsonl")]
def chunks(limite): return [c for d in docs_c for c in ct.montar_chunks(d, limite, 100, contar)]
def cauda(texto):
    """últimas frases (ou palavras) do texto que cabem em OV tokens"""
    fr = [u for u in ct.FRASE.split(texto.replace("\n", " ")) if u.strip()]
    out = []
    for u in reversed(fr):
        if contar(" ".join([u] + out)) > OV: break
        out.insert(0, u)
    if not out:
        w = texto.split(); out = [" ".join(w[-40:])]
        while contar(out[0]) > OV and len(out[0].split()) > 5: out = [" ".join(out[0].split()[5:])]
    return " ".join(out)
def com_overlap(cs, mesma_secao):
    out = []
    for i, c in enumerate(cs):
        c = dict(c); p = cs[i-1] if i else None
        if p and p["catalog_id"] == c["catalog_id"] and (not mesma_secao or p["secao"] == c["secao"]):
            cab, corpo = c["texto_embedding"].split("\n", 1)
            c["texto_embedding"] = cab + "\n" + ct.normalizar_para_embedding(cauda(p["content"])) + "\n" + corpo
            c["ov"] = True
        out.append(c)
    return out
base450 = chunks(450); base390 = chunks(390)
VAR = {"sem overlap (hoje, 450)": base450,
       "A: 450 + 60 mesma seção": com_overlap(base450, True),
       "B: 390 + 60 mesma seção": com_overlap(base390, True),
       "C: 390 + 60 qualquer vizinho": com_overlap(base390, False)}
for n, cs in VAR.items():
    t = sorted(contar(c["texto_embedding"]) for c in cs)
    print(f"{n:30} chunks {len(cs):5}  com overlap {sum(1 for c in cs if c.get('ov')):5}  tokens mediana {t[len(t)//2]} max {t[-1]}", flush=True)
m, _ = g.carregar_modelo("qwen3"); cfg = g.MODELOS["qwen3"]
docs = sorted(d["catalog_id"] for d in docs_c); pos = {d: k for k, d in enumerate(docs)}
# chunk de resumo igual ao do pipeline (chunk_resumo.py); documento sem resumo fica só com o texto
cr = mod(ROOT/"ingestion/corpus/chunk_resumo.py", "cr")
resumos = [c for c in (cr.montar_chunk(d, contar) for d in docs_c) if c]
R = m.encode([c["texto_embedding"] for c in resumos], normalize_embeddings=True, batch_size=16).astype(np.float32)
R_idx = np.array([pos[c["catalog_id"]] for c in resumos])
casos = [c for c in av.carregar_casos() if c["esperado"] and c["suite"] != "mari"]  # as 278
Q = m.encode([cfg["prefixo_query"] + c["pergunta"] for c in casos], normalize_embeddings=True, batch_size=32).astype(np.float32)
cortes = [("Todas", lambda c: True), ("Sintoma PT", lambda c: c["variante"]=="sintoma" and c["idioma"]=="pt"),
          ("Sintoma difícil", lambda c: c["variante"]=="sintoma" and c["dificuldade"]=="hard"), ("Causa", lambda c: c["variante"]=="causa")]
linhas = []
for n, cs in VAR.items():
    t0 = time.time()
    V = m.encode([c["texto_embedding"] for c in cs], normalize_embeddings=True, batch_size=16).astype(np.float32)
    idx = np.array([pos[c["catalog_id"]] for c in cs])
    print(f"  vetores {n}: {time.time()-t0:.0f}s", flush=True)
    for rot, VV, II in ((f"{n} | só texto", V, idx), (f"{n} | resumo+texto", np.vstack([R, V]), np.concatenate([R_idx, idx]))):
        ranks = []
        for c, q in zip(casos, Q):
            ordem, _ = av.ranquear(VV @ q, II, len(docs)); top = [docs[i] for i in ordem[:20]]
            ranks.append(next((k+1 for k, d in enumerate(top) if d in c["esperado"]), None))
        cel = []
        for _, f in cortes:
            r = [x for x, c in zip(ranks, casos) if f(c)]
            cel.append(f"{sum(1 for x in r if x==1)/len(r):.0%} / {sum(1 for x in r if x and x<=5)/len(r):.0%}")
        mrr = sum(1/x for x in ranks if x)/len(ranks)
        linhas.append(f"{rot:48}" + "".join(f"{x:>17}" for x in cel) + f"   MRR {mrr:.3f}")
print(f"\n{'variante':48}" + "".join(f"{n:>17}" for n, _ in cortes) + f"   (n={len(casos)})")
for l in sorted(linhas, key=lambda s: ("resumo" in s, s)): print(l)
