from loader import load_documents, split_documents
from embeddings import get_embedding_model

docs = load_documents()
chunks = split_documents(docs)

embedder = get_embedding_model()

vector = embedder.embed_query(
    "How authentication works?"
)

print("vector length:", len(vector))
print("1st five values:", vector)