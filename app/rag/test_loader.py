from loader import load_documents

docs = load_documents()

print(f"Loaded {len(docs)} documents\n")

for doc in docs[:2]:
    print("SOURCE:", doc.metadata)
    print("CONTENT:", doc.page_content[:200])
    print("-" * 50)
