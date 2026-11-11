"""Chamada ao GPT-OSS-20B via NVIDIA NIM.

Uso: python llm.py "pergunta"
Sem pergunta, roda as chamadas de teste.
A chave é lida de NVIDIA_API_KEY no .env da raiz do projeto.
"""

import sys
import time

from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA

load_dotenv()

MODEL = "openai/gpt-oss-20b"

# O modelo raciocina antes de responder, e o raciocínio também consome tokens
MAX_TOKENS = 2048

# No plano gratuito a resposta pode levar mais de 2 minutos (o padrão é 60 s)
TIMEOUT = 300

TESTES = [
    "Responda apenas: OK",
    "Em uma frase, o que é um post-mortem de incidente na área de SRE?",
    "In one sentence, what is connection pool exhaustion in a database?",
]


def ask(prompt: str, system: str | None = None) -> str:
    llm = ChatNVIDIA(model=MODEL, temperature=0, max_completion_tokens=MAX_TOKENS, timeout=TIMEOUT)
    messages = [("system", system), ("user", prompt)] if system else [("user", prompt)]
    return llm.invoke(messages).content


def main() -> None:
    prompts = [" ".join(sys.argv[1:])] if len(sys.argv) > 1 else TESTES
    for prompt in prompts:
        inicio = time.perf_counter()
        resposta = ask(prompt)
        segundos = time.perf_counter() - inicio
        print(f"Pergunta: {prompt}")
        print(f"Resposta: {resposta}")
        print(f"Tempo: {segundos:.1f} s\n")


if __name__ == "__main__":
    main()
