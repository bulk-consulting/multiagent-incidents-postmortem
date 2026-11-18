"""The "Decision in code" box of the diagram.

This is plain Python, no model: it reads the triage result and chooses what happens next.
"""

ASK_USER = "ask_user"  # not enough information: ask the analyst
TELL_RELATED_INCIDENT = "tell_related_incident"  # a similar investigation already exists
GO_TO_RESEARCH = "go_to_research"  # new problem: continue to the research agent


def next_step(result):
    """Choose what happens after the triage agent. The order of the checks matters."""
    if not result.enough_information:
        return ASK_USER
    if result.related_incident is not None:
        return TELL_RELATED_INCIDENT
    return GO_TO_RESEARCH
