from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(req: ChatRequest, request: Request):
    rag_chain = request.app.state.rag_chain

    result = rag_chain(req.question)

    return {
        "answer": result["result"],
        "sources": [
            doc.metadata for doc in result["source_documents"]
        ]
    }
