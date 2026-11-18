"""Test 1: can we talk to the model? (no tools)

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_llm
"""
import time

from agents.triage.llm import MODEL, chat

# This list is the "messages history" from the diagram: instructions + user message.
messages = [
    {"role": "system", "content": "You are a helpful assistant. Answer in one short sentence."},
    {"role": "user", "content": "What is a production incident?"},
]

print(f"model: {MODEL}")
print("calling the model (the free NIM plan can take a couple of minutes)...")
start = time.time()
reply = chat(messages)
print(f"reply after {time.time() - start:.1f}s:")
print(reply["content"])
