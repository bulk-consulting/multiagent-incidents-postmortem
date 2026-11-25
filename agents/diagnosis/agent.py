"""The Diagnosis agent: reads the Research agent's findings and returns a DiagnosisResult.

run_agent(description, triage, findings, research_round, max_rounds) returns two things:
  - the DiagnosisResult (the validated answer),
  - the messages history (useful to see what happened).

Same design as the Triage agent (agents/triage/agent.py): the model answers with JSON; Pydantic checks the shape
(schema.py) and code checks one more rule (every hypothesis is based on incidents that are in the findings). If the
answer is not valid, the error goes back to the model and it tries again (at most MAX_TURNS).

The model writes a draft (hypotheses with two comparisons each, gaps, a search request, questions); code decides
the confidence limit, whether the evidence is enough and the next step (schema.decide). In the tests, when the
model decided it itself, it said "the evidence is enough" in 24 of 24 answers, even when its own "differs" said the
past incident was another kind of failure.

The agent has no tool: when the evidence is not enough, it asks the graph for a new search (refine_search) or for
data from the analyst (ask_analyst).

Every model call goes through rag/limite_llm.py (calls per minute + long waits on HTTP 429).
"""
import re

from agents.diagnosis.prompts import SYSTEM_PROMPT, user_message
from agents.diagnosis.schema import check_based_on, decide, parse_diagnosis_answer
from agents.triage.llm import chat
from rag import limite_llm

MAX_TURNS = 3
# Model settings, chosen in the test of 7 settings × 6 cases × 3 repetitions on the same findings
# (experiments/run_diagnosis_config.py, results/diagnosis_config_2026-11-24_1824.json): with the reasoning turned
# off and temperature 0 the agent was the fastest stable setting (29 s per call against 52-74 s), had no invalid
# answer, and was the only one that did not accept a wrong cause in DAN-018. With the reasoning on, 4096 tokens were
# sometimes used up before the answer (empty answers).
MAX_TOKENS = 4096
TEMPERATURE = 0
LLM_OPTIONS: dict = {"chat_template_kwargs": {"enable_thinking": False}}  # other NIM fields (e.g. {"top_p": 0.95})


def _chat(messages):
    return limite_llm.chamar(lambda: chat(messages, max_tokens=MAX_TOKENS, temperature=TEMPERATURE, **LLM_OPTIONS), aviso="diagnosis")


def _words(text):
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


def repeats(request, previous_requests):
    """True if the request is the same as (or almost the same as: 80% of the words) a request already made."""
    new = _words(request)
    for old in map(_words, previous_requests or []):
        if new and old and len(new & old) / len(new | old) >= 0.8:
            return True
    return False


def run_agent(description, triage, findings, research_round=1, max_rounds=3, previous_requests=None):
    """previous_requests: the search requests already made in this investigation (a new one must not repeat them;
    seen in the tests: the same request in rounds 2 and 3, which wastes a round)."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message(description, triage, findings, research_round, max_rounds,
                                                 previous_requests)},
    ]
    finding_ids = [r["incident_id"] for r in findings]
    deepened_ids = [r["incident_id"] for r in findings if r.get("deepened")]
    for turn in range(MAX_TURNS):
        reply = _chat(messages)
        text = reply.get("content") or ""
        messages.append({"role": "assistant", "content": text})
        try:
            draft = parse_diagnosis_answer(text)
            check_based_on(draft, finding_ids)
            result = decide(draft, deepened_ids, research_round, max_rounds)
            # a repeated request gets one chance to be rewritten; after that it is accepted (the Research agent
            # leaves out the incidents already seen, so a repeated request still brings new ones, only fewer)
            if result.next_step == "refine_search" and turn == 0 and repeats(result.search_request, previous_requests):
                raise ValueError(f"search_request repeats a search already requested ({previous_requests}). "
                                 "Ask for another angle: another kind of trigger, component or symptom")
            return result, messages
        except ValueError as error:
            messages.append({"role": "user", "content": f"Your answer is not valid: {error}\n"
                                                        "Fix it. Your final answer must be only the JSON object."})
    error = RuntimeError(f"The diagnosis agent did not produce a valid answer in {MAX_TURNS} turns")
    error.messages = messages  # to see what the model answered (experiments, trace in the graph)
    raise error
