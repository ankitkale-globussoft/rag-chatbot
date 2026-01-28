from loader import load_documents, split_documents

docs = load_documents()
chunks = split_documents(docs)

print(f"Original documents: {len(docs)}")
print(f"Chunks created: {len(chunks)}\n")

for chunk in chunks[:2]:
    print("SOURCE:", chunk.metadata)
    print("Chunk Size:", len(chunk.page_content))
    print(chunk.page_content[:200])
    print("-" * 60)