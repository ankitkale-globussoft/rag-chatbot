from vectorstore import load_vector_store
from chain import create_rag_chain

vectorstore = load_vector_store()
ragchain = create_rag_chain(vectorstore)

querry = "can you find what is line number 13 in notes.txt"

result = ragchain(querry)

print("\nAnswer:\n", result["result"])
print("\nSources:")
for doc in result["source_documents"]:
    print("-", doc.metadata)