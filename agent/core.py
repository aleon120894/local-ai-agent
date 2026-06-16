import ollama

from agent.parser import safe_parse
from agent.schemas import AgentAction
from agent.tool_executor import execute_action

from memory.memory_manager import save, load


class Agent:

    def __init__(self):
        self.model = "qwen2.5:1.5b"

        with open("prompts/system_prompt.txt", "r") as f:
            system_prompt = f.read()

        saved_messages = load()

        if saved_messages:
            self.messages = saved_messages

        else:
            self.messages = [
                {"role": "system", "content": system_prompt}
            ]

        print(f"Loaded {len(self.messages)} messages")


    def ask(self, prompt: str):

        self.messages.append({
            "role": "user",
            "content": prompt
        })

        response = ollama.chat(
            model=self.model,
            messages=self.messages
        )

        raw = response["message"]["content"]

        # 1. SAFE PARSE (no crash)
        data = safe_parse(raw)

        if data is None:

            # fallback: treat as direct answer
            self.messages.append({
                "role": "assistant",
                "content": raw
            })

            save(self.messages)

            return raw

        # 2. SAFE VALIDATION (no crash)
        try:
            action = AgentAction.model_validate(data)
        except Exception:
            return f"Invalid schema: {data}"

        # 3. TOOL EXECUTION LAYER
        if action.action == "search_docs":
            content = action.content or "Empty response"

            self.messages.append({
                "role": "assistant",
                "content": content
            })

            save(self.messages)

            return content

        if action.action == "read_file":
            return execute_action(action)

        if action.action == "respond":
            return action.content or "Empty response"

        return f"Unknown action: {action.action}"

    def reset(self):
        with open("prompts/system_prompt.txt", "r") as f:
            system_prompt = f.read()

        self.messages = [
            {"role": "system", "content": system_prompt}
        ]

        save(self.messages)
