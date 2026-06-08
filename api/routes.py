from fastapi import APIRouter

from api.schemas import ChatRequest, ChatResponse
from services.agent_service import AgentService


router = APIRouter()

service = AgentService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = service.chat(request.message)

    return ChatResponse(
        response=response
    )
