from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.documents import Document
from pathlib import Path

CHROMA_PATH = "data/chroma"

def get_embedding_model():
    return OllamaEmbeddings( model="nomic-embed-text" )

def create_vector_store( documents: list[Document] ):
    embeddings = get_embedding_model()
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
    )

    vectorstore.persist()
    return vectorstore

def load_vector_store():
    embeddings = get_embedding_model()

    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
    )