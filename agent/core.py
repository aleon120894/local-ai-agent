import ollama

class Agent:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "You are a cybersecurity AI assistant."
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
            model="qwen2.5:1.5b",
            messages=self.messages
        )

        answer = response["message"]["content"]

        self.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer
