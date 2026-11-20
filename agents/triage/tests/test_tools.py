"""Test: does the tool work, and does it handle the model's mistakes?
No model call, so it runs in a second.

Run from the repository root:
    .venv/Scripts/python.exe -m agents.triage.tests.test_tools
"""
import json

from agents.triage.tests.checks import Checker
from agents.triage.tools import clean_tool_name, list_investigations, run_tool

checker = Checker()


def ids(result):
    """The investigation ids inside a tool result."""
    return [item["incident_id"] for item in result["investigations"]]


print("list_investigations")
checker.check("without filter: returns all 4", len(ids(list_investigations())) == 4)
checker.check("filter 'login': only INC-042", ids(list_investigations("login")) == ["INC-042"])
checker.check(
    "filter ignores case and extra words ('Login page')",
    ids(list_investigations("Login page")) == ["INC-042"],
)

wrong_guess = list_investigations("recommendations")
checker.check(
    "unknown service: returns everything, with a note",
    len(ids(wrong_guess)) == 4 and "note" in wrong_guess,
)

print("\nrun_tool (what the agent calls)")
checker.check(
    "valid call with arguments as JSON text",
    ids(run_tool("list_investigations", '{"service": "search"}')) == ["INC-044"],
)
checker.check("empty arguments are fine", len(ids(run_tool("list_investigations", ""))) == 4)
checker.check("unknown tool gives an error", "error" in run_tool("delete_everything", "{}"))
checker.check(
    "argument that does not exist gives an error",
    "error" in run_tool("list_investigations", '{"id": "INC-042"}'),
)
checker.check("broken JSON gives an error", "error" in run_tool("list_investigations", "{not json"))
checker.check("the result can be turned into JSON text", bool(json.dumps(run_tool("list_investigations", "{}"))))

print("\nclean_tool_name")
checker.check("exact name is kept", clean_tool_name("list_investigations") == "list_investigations")
checker.check(
    "extra text glued to the name is removed",
    clean_tool_name("list_investigationscommentary") == "list_investigations",
)
checker.check("unknown names are kept as they are", clean_tool_name("other_tool") == "other_tool")

checker.finish()
