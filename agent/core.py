import ollama

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

        answer = response["message"]["content"]

        self.messages.append({
            "role": "assistant",
            "content": answer
        })

        return answer

    def reset(self):
        self.messages = []
