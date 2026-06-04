from tools.registry import TOOLS


ALLOWED_ACTIONS = {
    "respond",
    "read_file",
    "search_docs"
}

def execute_action(action):
    
    if action.action not in ALLOWED_ACTIONS:
        return "Unknown action"

    if action.action == "read_file":
        return TOOLS["read_file"](action.path)

    if action.action == "search_docs":
        return TOOLS["search_docs"](action.query)

    return None
