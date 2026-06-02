from agent.core import Agent
from tools.registry import TOOLS

agent = Agent()

while True:

    prompt = input("> ")

    if prompt.lower() == "reset":
        agent.reset()
        print("Conversation cleared.")
        continue

    if prompt.startswith("/read "):
        path = prompt.replace("/read ", "")
        result = TOOLS["read_file"](path)
        print(result)
        continue

    if prompt.lower() in ["exit", "quit"]:
        break

    print(agent.ask(prompt))
