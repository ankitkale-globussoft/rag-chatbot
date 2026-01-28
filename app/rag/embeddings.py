from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.documents import Document

def get_embedding_model():
    return OllamaEmbeddings( model="nomic-embed-text" )

def embed_documents(documents: list[Document]):
    embeddings = get_embedding_model()
    return embeddings.embed_documents(
        [doc.page_content for doc in documents]
    )