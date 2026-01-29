from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.core.lifespan import lifespan

app = FastAPI(
    title="Local RAG Chatbot",
    lifespan=lifespan,
)

app.include_router(chat_router)
