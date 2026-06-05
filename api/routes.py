from fastapi import APIRouter

from api.schemas import ChatRequest, ChatResponse
from agent.core import Agent

router = APIRouter()

agent = Agent()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = agent.ask(request.message)

    return ChatResponse(
        response=response
    )
