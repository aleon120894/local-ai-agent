from agent.core import Agent
from tools.registry import TOOLS
from rag.indexer import build_index

import os


build_index()
agent = Agent()

while True:

    prompt = input("> ")

    if prompt.lower() == "reset":
        agent.reset()
        print("Conversation cleared.")
        continue

    if prompt.lower() == "/rebuild":
        build_index()
        print("Knowledge base rebuilt.")
        continue

    if prompt.lower() == "/docs":
        files = os.listdir("data")

        print("\nDocuments:")
        for file in files:
            print(f"- {file}")

        continue

    if prompt.startswith("/read "):
        path = prompt.replace("/read ", "")
        result = TOOLS["read_file"](path)
        print(result)
        continue

    if prompt.lower() in ["exit", "quit"]:
        break

    print(agent.ask(prompt))
