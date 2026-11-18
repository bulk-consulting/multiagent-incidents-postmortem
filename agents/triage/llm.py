"""Minimal client for the LLM (GPT-OSS-20B on NVIDIA NIM).

One function: chat(messages, tools=None) -> the model's reply (a dict).

The key goes in the .env file at the repository root (it is not in git):
    NVIDIA_API_KEY=nvapi-...
"""
import time
from pathlib import Path

import httpx
from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parents[2]
env = dotenv_values(ROOT / ".env")

API_KEY = env.get("NVIDIA_API_KEY")
BASE_URL = env.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
MODEL = env.get("LLM_MODEL", "openai/gpt-oss-20b")

# The free NIM plan has a queue: one call can take a couple of minutes.
TIMEOUT = httpx.Timeout(15.0, read=300.0)

# The free plan also fails sometimes (busy server, timeouts), so we try a few times.
ATTEMPTS = 3
WAIT_SECONDS = 15


def chat(messages, tools=None, max_tokens=2048):
    """Send the messages history to the model and return its reply message.

    If the model wants to use a tool, the reply has a "tool_calls" entry.
    """
    if not API_KEY:
        raise RuntimeError(f"NVIDIA_API_KEY not found in {ROOT / '.env'}")

    body = {"model": MODEL, "messages": messages, "max_tokens": max_tokens}
    if tools:
        body["tools"] = tools
        body["tool_choice"] = "auto"  # the model decides if it needs a tool

    problem = ""
    for attempt in range(1, ATTEMPTS + 1):
        try:
            response = httpx.post(
                f"{BASE_URL}/chat/completions",
                json=body,
                headers={"Authorization": f"Bearer {API_KEY}"},
                timeout=TIMEOUT,
            )
        except httpx.TransportError as error:  # timeouts and network problems
            problem = f"network problem: {error!r}"
        else:
            if response.status_code == 200:
                choices = response.json().get("choices")
                if choices:
                    return choices[0]["message"]
                problem = "HTTP 200 but the answer has no 'choices'"
            else:
                problem = f"HTTP {response.status_code}: {response.text[:300]}"
                # Only "too many requests" and server errors are worth trying again.
                if response.status_code != 429 and response.status_code < 500:
                    raise RuntimeError(problem)

        if attempt < ATTEMPTS:
            time.sleep(WAIT_SECONDS)

    raise RuntimeError(f"The model call failed {ATTEMPTS} times. Last problem: {problem}")
