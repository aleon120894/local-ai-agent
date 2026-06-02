import ollama


SYSTEM_PROMPT = """
You are a cybersecurity AI assistant.
"""

class Agent:
    def __init__(self):

        self.model = "qwen2.5:1.5b"
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def ask(self, prompt):
        self.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        response = ollama.chat(
            model=self.model,
            messages=self.messages
        )

        answer = response["message"]["content"]

        self.messages.append(
            {
                "role": "assistant",
                "content": prompt
            }
        )

        return answer

    def reset(self):

        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
