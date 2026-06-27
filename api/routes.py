import os
import shutil

from fastapi import APIRouter, UploadFile, File

from api.schemas import ChatRequest, ChatResponse, FilesResponse
from services.agent_service import AgentService
from rag.indexer import build_index


router = APIRouter()
service = AgentService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = service.chat(request.message)

    return ChatResponse(
        response=response
    )


@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    path = os.path.join("data", file.filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    build_index()

    return {
        "status": "ok",
        "filename": file.filename
    }

@router.get("/files", response_model=FilesResponse)
def files():

    return FilesResponse(
        files=os.listdir("data")
    )
