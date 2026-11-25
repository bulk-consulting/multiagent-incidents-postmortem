"""The Triage agent as a LangGraph node.

We do not rewrite the agent. The agent keeps its own loop (agent.py). This file only wraps it
in two small functions that a LangGraph graph can use:

    triage_node          reads the analyst message from the shared state, runs the agent,
                         and writes the result back into the state
    route_after_triage   reads the result from the state and says where the graph goes next

How to plug it into a graph (the graph itself is built by whoever owns the main flow):

    graph.add_node("triage", triage_node)
    graph.add_edge(START, "triage")
    graph.add_conditional_edges("triage", route_after_triage, {
        ASK_USER: END,                  # send the questions back to the analyst
        TELL_RELATED_INCIDENT: END,     # tell the analyst the incident already exists
        GO_TO_RESEARCH: "research",     # continue with the Research agent
    })

Shared state keys (the names of docs/E5_Estado_e_Formatos.md, section 3):

    description      in   the analyst message (and their answers, when the graph asked for more information)
    triage_result    out  the full TriageResult (symptoms, service, triggers, category, questions, related incident)
    symptoms         out  the symptoms alone, which is the input the Research agent expects

The agent's messages history stays inside the agent. It is not put in the shared state,
because the Research agent has its own "messages" key and the two would mix.
"""
from agents.triage.agent import run_agent
from agents.triage.routing import next_step


def triage_node(state: dict) -> dict:
    """Run the Triage agent on the analyst message. Returns only the keys it updates."""
    result, _messages_history = run_agent(state["description"])
    return {
        "triage_result": result,
        "symptoms": result.symptoms,
    }


def route_after_triage(state: dict) -> str:
    """Conditional edge: the same "Decision in code" as before (routing.py)."""
    return next_step(state["triage_result"])
