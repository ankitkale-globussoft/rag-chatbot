from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    question: str

@router.post("/stream")
async def chat_stream(payload: ChatRequest, request: Request):
    """
    Streaming RAG chat endpoint
    """

    question = payload.question

    rag_chain = request.app.state.streaming_rag_chain

    async def token_generator():
        async for chunk in rag_chain.astream(question):
            if chunk.content:
                yield chunk.content

    return StreamingResponse(
        token_generator(),
        media_type="text/plain"
    )
