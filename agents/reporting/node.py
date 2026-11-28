"""The Reporting agent as a LangGraph node (same idea as agents/triage/node.py: wrap, do not rewrite).

The node reads the shared state, runs the agent, and writes the report back. It never lets the flow
end without an answer: if the model fails, it writes the simple inconclusive report built by code.

State keys it reads:    incident_id, description, triage_result, findings, diagnosis
State keys it writes:   report, report_attempts, report_problems, errors
(The names follow docs/E5_Orchestrated_Multi_Agent_System/E5_Estado_e_Formatos.md, section 3.)

How to plug it into the main graph:
    graph.add_node("reporting", reporting_node)
"""
from agents.reporting.agent import fallback_report, run_reporting_agent


def reporting_node(state: dict) -> dict:
    """Write the final report for one investigation. Returns only the keys it updates."""
    try:
        report, _messages_history, attempts, problems = run_reporting_agent(state)
    except Exception as error:  # the model call itself failed (network, key, busy server...)
        report = fallback_report(state, [str(error)])
        attempts, problems = 0, [f"the model call failed: {error}"]

    # `errors` is a list that the graph adds to, so we return only what is new.
    errors = [{"node": "reporting", "error": "; ".join(problems)}] if problems else []
    return {
        "report": report,
        "report_attempts": attempts,
        "report_problems": problems,
        "errors": errors,
    }
