from vectorstore import load_vector_store

vectorstore = load_vector_store()
results = vectorstore.similarity_search(
    "What features does TaskFlow provide?",
    k=3
)

for i, doc in enumerate(results, 1):
    print(f"\nResult {i}")
    print("SOURCE:", doc.metadata)
    print(doc.page_content[:300])