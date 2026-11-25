"""The LLM client of the Reporting agent.

It is the same client the Triage agent uses (NVIDIA NIM, model set by LLM_MODEL in the .env file).
We reuse it instead of copying it. When the team moves the client to a shared place, only this line changes.
"""
from agents.triage.llm import chat  # noqa: F401  (re-exported on purpose)
