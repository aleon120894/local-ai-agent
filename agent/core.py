import ollama
import json

from agent.schemas import AgentAction
from agent.tool_executor import execute_action


class Agent:
    def __init__(self):
        self.model = "qwen2.5:1.5b"

        with open("prompts/system_prompt.txt", "r") as f:
            system_prompt = f.read()

        self.messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    def ask(self, prompt):
        self.messages.append({
            "role": "user",
            "content": prompt
        })

        response = ollama.chat(
            model=self.model,
            messages=self.messages
        )

        raw_response = response["message"]["content"]
        print(raw_response)

        try:
            raw_response = raw_response.strip()
            data = json.loads(raw_response)
            action = AgentAction.model_validate(data)

            if action.action == "respond":
                return action.content

            return execute_action(action)

        except Exception as e:

            return f"JSON error: {e}"

    def reset(self):
        self.messages = []
