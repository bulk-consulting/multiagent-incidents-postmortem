"""
Pipeline de ingestão da E2: do dado bruto do danluu até o PostgreSQL + pgvector, num comando só.

Etapas (cada uma chama os scripts que já existem, na ordem):
    1 inventario   triagem/01_inventario.py        lê os brutos e classifica a qualidade de cada documento
    2 reextracao   reextracao/reextrair.py         refaz o texto dos documentos estragados (HTML salvo)
    3 fichas       fichas/validar_fichas.py        valida as fichas aceitas (schema e trechos literais)
    4 corpus       corpus/montar_corpus.py         escolhe o texto de cada documento e limpa
    5 chunks       corpus/chunk_fichas.py + chunk_texto.py   chunks das fichas e do texto completo
    6 embeddings   corpus/gerar_embeddings.py qwen3          vetores com Qwen3-Embedding-0.6B
    7 banco        banco/carregar.py               sobe o container (se preciso) e carrega no pgvector
    8 validacao    banco/validar_ingestao.py       contagens, integridade e perguntas de teste

As fichas NÃO são geradas aqui: foram extraídas por LLM e conferidas no GPT, lote a lote, num
processo curado (ver ingestion/README.md). A etapa 3 só valida as que estão em fichas/saida/.

Uso (a partir da raiz do repositório):
    multiagent_env/bin/python -I ingestion/pipeline.py                  # tudo
    multiagent_env/bin/python -I ingestion/pipeline.py --listar
    multiagent_env/bin/python -I ingestion/pipeline.py --desde corpus   # da etapa 'corpus' em diante
    multiagent_env/bin/python -I ingestion/pipeline.py --ate chunks     # até a etapa 'chunks'
    multiagent_env/bin/python -I ingestion/pipeline.py --so validacao   # só uma etapa
    multiagent_env/bin/python -I ingestion/pipeline.py --forcar-embeddings   # gera os vetores mesmo se
                                                                              # já baterem com os chunks

A etapa embeddings é pulada quando os vetores gravados (versionados no git) correspondem aos chunks
atuais; ela usa a GPU se houver e senão o processador (bem mais lento).
"""
from __future__ import annotations

import os
import secrets
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ING = ROOT / "ingestion"
PY = [sys.executable, "-I"]
BANCO = ING / "banco"
CONTAINER = "e2-pgvector-andre"

ETAPAS: list[tuple[str, str, list[list[str]]]] = [
    ("inventario", "lê os brutos do danluu e classifica a qualidade de cada documento",
     [PY + [str(ING / "triagem" / "01_inventario.py")]]),
    ("reextracao", "refaz o texto dos documentos estragados a partir do HTML salvo",
     [PY + [str(ING / "reextracao" / "reextrair.py")]]),
    ("fichas", "valida as fichas aceitas (schema e trechos literais no texto)",
     [PY + [str(ING / "fichas" / "validar_fichas.py")]]),  # arquivos acrescentados em rodar()
    ("corpus", "escolhe o texto de cada documento e aplica a limpeza",
     [PY + [str(ING / "corpus" / "montar_corpus.py")]]),
    ("chunks", "gera os chunks das fichas (etapa 1 da busca) e do texto completo (etapa 2)",
     [PY + [str(ING / "corpus" / "chunk_fichas.py")], PY + [str(ING / "corpus" / "chunk_texto.py")]]),
    ("embeddings", "gera os vetores dos chunks com Qwen3-Embedding-0.6B",
     [PY + [str(ING / "corpus" / "gerar_embeddings.py"), "qwen3"]]),
    ("banco", "sobe o PostgreSQL + pgvector (se preciso) e carrega documentos, chunks e vetores",
     [PY + [str(BANCO / "carregar.py")]]),
    ("validacao", "confere contagens e integridade e roda perguntas de teste no banco",
     [PY + [str(BANCO / "validar_ingestao.py")]]),
]
NOMES = [e[0] for e in ETAPAS]
AMBIENTE = {**os.environ, "TRANSFORMERS_VERBOSITY": "error", "HF_HUB_DISABLE_PROGRESS_BARS": "1",
            "TOKENIZERS_PARALLELISM": "false", "PYTHONWARNINGS": "ignore"}
# com o modelo já baixado, não consulta o Hugging Face pela internet a cada carga (mais rápido)
_CACHE_QWEN = Path(os.environ.get("HF_HOME", Path.home() / ".cache" / "huggingface")) / "hub" / "models--Qwen--Qwen3-Embedding-0.6B"
if _CACHE_QWEN.exists() and (Path.home() / ".cache" / "huggingface" / "hub" / "models--intfloat--multilingual-e5-base").exists():
    AMBIENTE["HF_HUB_OFFLINE"] = "1"


def garantir_banco() -> None:
    """Cria o .env na primeira vez (senha aleatória) e sobe o container se não estiver saudável."""
    env = BANCO / ".env"
    if not env.exists():
        modelo = (BANCO / ".env.example").read_text(encoding="utf-8")
        linhas = [l for l in modelo.replace("troque-esta-senha", secrets.token_urlsafe(18)).splitlines()
                  if l and not l.startswith("#")]
        env.write_text("\n".join(linhas) + "\n", encoding="utf-8")
        env.chmod(0o600)
        print(f"  criado {env.relative_to(ROOT)} com senha aleatória", flush=True)
    estado = subprocess.run(["docker", "inspect", "-f", "{{.State.Health.Status}}", CONTAINER],
                            capture_output=True, text=True).stdout.strip()
    if estado != "healthy":
        print("  subindo o container do banco...", flush=True)
        subprocess.run(["docker", "compose", "--env-file", ".env", "up", "-d"], cwd=BANCO, check=True)
        for _ in range(60):
            estado = subprocess.run(["docker", "inspect", "-f", "{{.State.Health.Status}}", CONTAINER],
                                    capture_output=True, text=True).stdout.strip()
            if estado == "healthy":
                break
            time.sleep(2)
        else:
            sys.exit("  o container não ficou saudável; veja: docker logs " + CONTAINER)
    print(f"  banco no ar ({CONTAINER})", flush=True)


def rodar(nome: str, descricao: str, comandos: list[list[str]], numero: int, forcar_embeddings: bool = False) -> float:
    print(f"\n{'=' * 78}\n[{numero}/{len(ETAPAS)}] {nome}: {descricao}\n{'=' * 78}", flush=True)
    t0 = time.time()
    if nome == "embeddings" and not forcar_embeddings:
        # os vetores só mudam quando os chunks mudam; os do Qwen3 estão no git, então uma máquina
        # sem GPU não precisa gerá-los (no processador levaria ~2 h)
        conf = subprocess.run(comandos[0] + ["--conferir"], cwd=ROOT, env=AMBIENTE, capture_output=True, text=True)
        print(conf.stdout.strip(), flush=True)
        if conf.returncode == 0:
            print("-- embeddings: vetores reaproveitados (use --forcar-embeddings para gerar de novo)", flush=True)
            return time.time() - t0
    if nome == "banco":
        garantir_banco()
    for cmd in comandos:
        if nome == "fichas":
            cmd = cmd + sorted(str(p) for p in (ING / "fichas" / "saida").glob("DAN-*.json"))
        r = subprocess.run(cmd, cwd=ROOT, env=AMBIENTE, capture_output=nome == "fichas", text=True)
        if nome == "fichas":  # o validador lista as 213 fichas; mostra só falhas e o resumo
            saida = [l for l in r.stdout.splitlines() if not l.startswith("OK ")]
            print("\n".join(saida[-15:]), flush=True)
        if r.returncode != 0:
            sys.exit(f"\nA etapa '{nome}' falhou (código {r.returncode}). O pipeline parou aqui.")
    dt = time.time() - t0
    print(f"-- {nome} concluída em {dt:.0f}s", flush=True)
    return dt


def main() -> None:
    args = sys.argv[1:]
    if "--listar" in args:
        for k, (nome, desc, _) in enumerate(ETAPAS, 1):
            print(f"{k} {nome:11} {desc}")
        return
    valor = lambda op: args[args.index(op) + 1] if op in args else None
    desde, ate, so = valor("--desde"), valor("--ate"), valor("--so")
    for v in (desde, ate, so):
        if v and v not in NOMES:
            sys.exit(f"etapa desconhecida: {v} (use --listar)")
    ini = NOMES.index(so or desde) if (so or desde) else 0
    fim = NOMES.index(so or ate) if (so or ate) else len(NOMES) - 1
    tempos = []
    t0 = time.time()
    for k in range(ini, fim + 1):
        nome, desc, cmds = ETAPAS[k]
        tempos.append((nome, rodar(nome, desc, cmds, k + 1, "--forcar-embeddings" in args)))
    print(f"\n{'=' * 78}\nPipeline concluído em {time.time() - t0:.0f}s: "
          + ", ".join(f"{n} {t:.0f}s" for n, t in tempos))


if __name__ == "__main__":
    main()
