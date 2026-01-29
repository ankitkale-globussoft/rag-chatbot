from loader import load_documents, split_documents
from vectorstore import create_vector_store

docs = load_documents()
chunks = split_documents(docs)

vectorstore = create_vector_store(chunks)

print("chroma vector created successfully")