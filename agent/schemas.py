from pydantic import BaseModel


class AgentAction(BaseModel):
    action: str
    path: str | None = None
    content: str | None = None
