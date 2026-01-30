from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.rag.vectorstore import load_vector_store
from app.rag.chain import create_rag_chain
from app.rag.stream_chain import create_streaming_rag_chain

@asynccontextmanager
async def lifespan(app: FastAPI):
    vectorstore = load_vector_store()
    app.state.rag_chain = create_rag_chain(vectorstore)
    app.state.streaming_rag_chain = create_streaming_rag_chain(vectorstore)

    yield

    #shutdown