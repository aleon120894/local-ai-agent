from agent.core import Agent


class AgentService:

    def __init__(self):
        self.agent = Agent()

    def chat(self, message: str):
        return self.agent.ask(message)
