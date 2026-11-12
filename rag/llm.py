"""
Cliente do LLM: GPT-OSS-20B no NVIDIA NIM (API no formato da OpenAI).

Configuração no arquivo .env da raiz do repositório (fora do git):
    NVIDIA_API_KEY=nvapi-...
    NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
    LLM_MODEL=openai/gpt-oss-20b

Duas funções:
    conversar(mensagens)                       resposta em texto livre
    estruturado(mensagens, nome, desc, schema) resposta em JSON que segue o schema

A resposta estruturada usa uma ferramenta obrigatória (tool_choice). Nos testes de 2026-11-09,
foi a única forma que funcionou com esse modelo no NIM: o response_format com json_schema
devolveu JSON quebrado, e o guided_json foi ignorado.

Teste de conexão (entrega 3.2), a partir da raiz do repositório:
    multiagent_env/bin/python -I rag/llm.py
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import httpx
from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parents[1]
_env = dotenv_values(ROOT / ".env")

BASE_URL = _env.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
MODELO = _env.get("LLM_MODEL", "openai/gpt-oss-20b")

# O plano gratuito do NIM tem fila: nos testes, cada chamada levou de 2 a 2,5 minutos.
TIMEOUT = httpx.Timeout(15.0, read=300.0)


class ErroLLM(Exception):
    """Resposta HTTP inesperada do NIM."""


class ErroTemporarioLLM(ErroLLM):
    """Erro que vale tentar de novo (429 ou 5xx)."""


class RespostaInvalida(Exception):
    """O modelo respondeu, mas não no formato pedido."""


# Exceções que valem uma nova tentativa (usadas na RetryPolicy do grafo).
# Atenção: o default_retry_on do LangGraph não tenta de novo em erros de timeout.
TENTAR_DE_NOVO = (httpx.TimeoutException, httpx.TransportError, ErroTemporarioLLM, RespostaInvalida)


def _post(corpo: dict) -> dict:
    chave = _env.get("NVIDIA_API_KEY")
    if not chave:
        raise ErroLLM(f"NVIDIA_API_KEY não encontrada em {ROOT / '.env'}")
    r = httpx.post(f"{BASE_URL}/chat/completions", json={"model": MODELO, **corpo},
                   headers={"Authorization": f"Bearer {chave}"}, timeout=TIMEOUT)
    if r.status_code == 429 or r.status_code >= 500:
        raise ErroTemporarioLLM(f"HTTP {r.status_code}: {r.text[:200]}")
    if r.status_code != 200:
        raise ErroLLM(f"HTTP {r.status_code}: {r.text[:300]}")
    try:
        j = r.json()
    except ValueError as e:
        raise ErroTemporarioLLM(f"HTTP 200 com corpo que não é JSON: {r.text[:200]!r}") from e
    # Já aconteceu de o NIM devolver HTTP 200 sem "choices" (corpo de erro); trata como falha temporária.
    if not isinstance(j, dict) or not j.get("choices"):
        raise ErroTemporarioLLM(f"HTTP 200 sem 'choices': {json.dumps(j, ensure_ascii=False)[:300]}")
    return j


def conversar(mensagens: list[dict], max_tokens: int = 1024, temperatura: float = 1.0) -> dict:
    """Chamada simples. Devolve {"conteudo", "raciocinio", "uso", "segundos"}."""
    t = time.time()
    j = _post({"messages": mensagens, "max_tokens": max_tokens, "temperature": temperatura})
    msg = j["choices"][0]["message"]
    return {"conteudo": msg.get("content") or "", "raciocinio": msg.get("reasoning_content") or "",
            "uso": j.get("usage") or {}, "segundos": round(time.time() - t, 1)}


def estruturado(mensagens: list[dict], nome: str, descricao: str, schema: dict,
                max_tokens: int = 4096, temperatura: float = 1.0) -> dict:
    """Obriga o modelo a "chamar" a ferramenta `nome` e devolve os argumentos já convertidos de JSON.

    O limite de tokens conta também o raciocínio interno do modelo. Com 2048, o nemotron-3.5-super-vl
    gastava tudo raciocinando nas perguntas de contexto mais longo e não chegava a chamar a
    ferramenta (finish_reason=length); com 4096 respondeu (2026-11-11).

    Devolve {"dados", "raciocinio", "uso", "segundos"}. Se a resposta não vier no formato
    pedido, levanta RespostaInvalida (o grafo tenta de novo).
    """
    t = time.time()
    j = _post({"messages": mensagens, "max_tokens": max_tokens, "temperature": temperatura,
               "tools": [{"type": "function", "function": {"name": nome, "description": descricao, "parameters": schema}}],
               "tool_choice": {"type": "function", "function": {"name": nome}}})
    escolha = j["choices"][0]
    msg = escolha["message"]
    chamadas = msg.get("tool_calls") or []
    if not chamadas:
        raise RespostaInvalida(f"sem chamada de ferramenta (finish_reason={escolha.get('finish_reason')}): "
                               f"{(msg.get('content') or '')[:200]!r}")
    try:
        dados = json.loads(chamadas[0]["function"]["arguments"])
    except (json.JSONDecodeError, KeyError) as e:
        raise RespostaInvalida(f"argumentos não são JSON válido: {e}") from e
    faltando = [c for c in schema.get("required", []) if c not in dados]
    if faltando:
        raise RespostaInvalida(f"campos obrigatórios ausentes: {faltando}")
    return {"dados": dados, "raciocinio": msg.get("reasoning_content") or "",
            "uso": j.get("usage") or {}, "segundos": round(time.time() - t, 1)}


if __name__ == "__main__":
    print(f"modelo: {MODELO} em {BASE_URL}")
    print("chamando (o NIM gratuito pode levar uns 2 minutos)...")
    r = conversar([{"role": "user", "content": "Qual número é maior, 9.11 ou 9.8? Responda em uma frase."}])
    print(f"resposta ({r['segundos']}s, {r['uso'].get('total_tokens')} tokens): {r['conteudo']}")
