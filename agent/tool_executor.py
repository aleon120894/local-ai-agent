from tools.registry import TOOLS


ALLOWED_ACTIONS = {
    "respond",
    "read_file"
}

def execute_action(action):
    
    if action.action not in ALLOWED_ACTIONS:
        return "Unknown action"

    if action.action == "read_file":
        return TOOLS["read_file"](action.path)

    return None
