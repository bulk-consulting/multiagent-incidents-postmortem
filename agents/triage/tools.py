"""The tools the triage agent can use.

A tool has two parts:
  1. a normal Python function (does the real work),
  2. a description (TOOLS) that the model reads to know what the tool is for
     and which arguments it accepts.
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "investigations.json"


def list_investigations(service=None):
    """Return the recent investigations (for now, read from a JSON file).

    If `service` is given, return only the investigations of that service.
    """
    investigations = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    # No filter: return everything.
    if not service:
        return {"service_filter": None, "investigations": investigations}

    # Filter by service. The match is loose ("Checkout page" matches "checkout").
    wanted = service.strip().lower()
    matches = [
        item
        for item in investigations
        if wanted in item["service"].lower() or item["service"].lower() in wanted
    ]
    if matches:
        return {"service_filter": service, "investigations": matches}

    # Nothing matched. The model may have guessed the service name wrong, so we return
    # everything: a wrong guess must not hide the investigation we are looking for.
    return {
        "service_filter": service,
        "note": "No investigation has this service, so all investigations are shown.",
        "investigations": investigations,
    }


# Tool name -> Python function.
TOOL_FUNCTIONS = {
    "list_investigations": list_investigations,
}

# What the model sees. The description tells it WHEN to use the tool.
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_investigations",
            "description": (
                "List the recent incident investigations (incident_id, summary, service, status). "
                "Use it to check whether the problem the analyst reports is already "
                "being investigated."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {
                        "type": "string",
                        "description": "Affected service, to see only its investigations (example: checkout).",
                    },
                },
                "required": [],
            },
        },
    },
]


def clean_tool_name(name):
    """GPT-OSS sometimes glues extra text to the tool name (for example 'list_investigationscommentary').
    If the name starts with a known tool name, use the known name."""
    for known in TOOL_FUNCTIONS:
        if name.startswith(known):
            return known
    return name


def run_tool(name, arguments_json):
    """Run the tool the model asked for and return its result.

    If something goes wrong, return {"error": ...}. That error goes back to the model,
    which can read it and try again.
    """
    function = TOOL_FUNCTIONS.get(name)
    if function is None:
        return {"error": f"Unknown tool: {name}"}
    try:
        arguments = json.loads(arguments_json or "{}")
        return function(**arguments)
    except Exception as error:
        return {"error": str(error)}
