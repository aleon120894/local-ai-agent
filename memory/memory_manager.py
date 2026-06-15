import json
import os


MEMORY_FILE = "memory/conversations.json"

def save(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f)

def load():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)
