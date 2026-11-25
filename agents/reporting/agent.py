"""The Reporting agent: writes the final answer for the analyst.

It has no tools. It is an LLM with a prompt, and a loop that checks the answer:

    shared state ──► messages history (system + user) ──► LLM ──► validate ──┬─► Report
                                                          ▲                  │
                                                          └── problems ──────┘ (up to MAX_ATTEMPTS)

If the model cannot write a valid report, the code builds a simple inconclusive one from what the
investigation found, so the flow never ends without an answer.

Run (from the repository root):
    .venv/Scripts/python.exe -m agents.reporting.tests.test_agent_loop
"""
from agents.reporting.llm import chat
from agents.reporting.prompts import SYSTEM_PROMPT, build_user_message
from agents.reporting.schema import Report, parse_report_answer
from agents.reporting.validation import _as_dict, validate_report

MAX_ATTEMPTS = 3      # the first answer plus up to 2 fixes
MAX_TOKENS = 8192     # the model "thinks" before it answers, and the message and the fields together can be long


def fallback_report(state, problems):
    """A simple inconclusive report built by code, used when the model could not write a valid one.
    It uses only data the other agents already delivered."""
    findings = state["findings"]
    diagnosis = _as_dict(state["diagnosis"])
    gaps = list(diagnosis["gaps"]) or ["The report could not be written automatically."]

    lines = ["I could not write the full report this time. This is what the investigation found so far.", ""]
    lines += ["**What is missing**"] + [f"- {gap}" for gap in gaps]
    if findings:
        lines += ["", "**Past incidents that may help (not confirmed as the cause)**"]
        lines += [f"- [{f['title']}]({f['url']})" for f in findings[:3]]

    return Report(
        incident_id=state.get("incident_id", ""),
        kind="inconclusive",
        summary="The report could not be written automatically. These are the gaps and the past incidents found.",
        message="\n".join(lines),
        gaps=gaps,
        suggested_checks=["Read the past incidents listed above."],
    )


def run_reporting_agent(state):
    """Write the report for one investigation.

    `state` is the shared state: incident_id, description, triage_result, findings, diagnosis.
    Returns (report, messages_history, attempts, problems). `problems` is empty when the model's report was valid,
    and lists what was still wrong when the code had to build the fallback report.
    """
    findings = state["findings"]
    diagnosis = _as_dict(state["diagnosis"])

    # The messages history: this is the agent's memory during one run.
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": build_user_message(state)},
    ]

    problems = []
    for attempt in range(1, MAX_ATTEMPTS + 1):
        reply = chat(messages, max_tokens=MAX_TOKENS)
        text = reply.get("content") or ""
        messages.append({"role": "assistant", "content": text})

        try:
            report = parse_report_answer(text)
            report.incident_id = state.get("incident_id", "")  # the code fills it in, the model does not
            problems = validate_report(report, findings, diagnosis)
        except ValueError as error:  # the answer does not fit the shape
            problems = [str(error)]

        if not problems:
            return report, messages, attempt, []

        # Not valid: tell the model what is wrong and let it try again.
        messages.append(
            {
                "role": "user",
                "content": "Your report has problems:\n" + "\n".join(f"- {p}" for p in problems)
                + "\nFix them. Your answer must be only the JSON object.",
            }
        )

    return fallback_report(state, problems), messages, MAX_ATTEMPTS, problems
