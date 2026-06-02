from agent.core import Agent

agent = Agent()

while True:
    prompt = input("> ")
    if prompt.lower() == "reset":
        agent.reset()
        print("Conversation cleared.")
        continue
    if prompt.lower() in ["exit", "quit"]:
        break

    print(agent.ask(prompt))
