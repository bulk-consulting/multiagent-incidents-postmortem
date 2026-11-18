"""
Ritmo das chamadas ao LLM no NVIDIA NIM gratuito.

O painel da conta em build.nvidia.com mostra "Your API Rate Limit: Up to 40 rpm". O "up to" é real: em
2026-11-18, recebemos 429 (Too Many Requests) a ~10–15 chamadas por minuto, quando o modelo estava muito
usado. Por isso, duas proteções, válidas para todas as chamadas do processo (todas as threads):

    1. ritmo: no máximo LLM_RPM chamadas em qualquer janela de 60 s (padrão 20; configurável no .env).
       Se a próxima chamada passaria do limite, ela espera a vez.
    2. espera longa em 429: 30 s, 60 s, 120 s, 120 s, 120 s (com um pouco de aleatoriedade), até 6
       tentativas. O limite do NIM é por minuto; esperar 15 s, como antes, não bastava.

Uso:
    from limite_llm import chamar
    resposta = chamar(lambda: cliente.invoke(mensagens))
"""
from __future__ import annotations

import random
import threading
import time
from collections import deque
from pathlib import Path

from dotenv import dotenv_values

_env = dotenv_values(Path(__file__).resolve().parents[1] / ".env")
LLM_RPM = int(_env.get("LLM_RPM") or 20)
ESPERAS_429 = (30, 60, 120, 120, 120)  # segundos entre as tentativas depois de um 429

_trava = threading.Lock()
_chamadas: deque[float] = deque()  # instantes das chamadas da última janela de 60 s


def esperar_vez() -> float:
    """Bloqueia até a próxima chamada caber no limite de LLM_RPM por minuto. Devolve quanto esperou (s)."""
    esperou = 0.0
    while True:
        with _trava:
            agora = time.monotonic()
            while _chamadas and agora - _chamadas[0] >= 60:
                _chamadas.popleft()
            if len(_chamadas) < LLM_RPM:
                _chamadas.append(agora)
                return esperou
            falta = 60 - (agora - _chamadas[0]) + 0.05
        time.sleep(falta)
        esperou += falta


def eh_429(erro: BaseException) -> bool:
    """O ChatNVIDIA levanta Exception("[429] Too Many Requests ..."); o rag/llm.py, "HTTP 429: ..."."""
    texto = str(erro)
    return "[429]" in texto or "HTTP 429" in texto or "Too Many Requests" in texto


def chamar(funcao, aviso: str = "LLM"):
    """Chama `funcao()` respeitando o ritmo e, em caso de 429, espera e tenta de novo.
    Outros erros sobem na hora (quem chama decide se tenta de novo)."""
    for tentativa in range(len(ESPERAS_429) + 1):
        esperar_vez()
        try:
            return funcao()
        except Exception as erro:  # noqa: BLE001 - só o 429 é tratado aqui
            if not eh_429(erro) or tentativa == len(ESPERAS_429):
                raise
            espera = ESPERAS_429[tentativa] * random.uniform(0.9, 1.2)
            print(f"[{aviso}] 429 (limite do NIM); esperando {espera:.0f}s antes da tentativa {tentativa + 2}", flush=True)
            time.sleep(espera)
