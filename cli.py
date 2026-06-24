from agent.core import Agent
from tools.registry import TOOLS
from tools.nmap_analyzer import analyze, recommend
from rag.indexer import build_index

from rag.retriever import search

import os


build_index()
agent = Agent()

while True:

    prompt = input("> ")

    if prompt.startswith("/search "):
        query = prompt.replace("/search ", "")
        print(search(query))
        continue

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

    if prompt.startswith("/analyze "):

        path = prompt.replace("/analyze ", "")
        services = analyze(path)
        recommendations = recommend(services)

        for item in recommendations:
            print(f"\n{item['service']} ({item['port']})")
            print("-" * 20)

            print("Recommended enumeration:")

            for rec in item["recommendations"]:
                print(f"- {rec}")

        continue

    if prompt.lower() in ["exit", "quit"]:
        break

    print(agent.ask(prompt))
