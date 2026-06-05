from fastapi import FastAPI

from api.routes import router
from rag.indexer import build_index


build_index()

app = FastAPI(
    title="Local AI Agent"
)

app.include_router(router)
