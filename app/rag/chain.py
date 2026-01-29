from langchain_ollama import OllamaLLM
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a private assistant.

Rules:
- Answer ONLY using the provided context.
- Do NOT use outside knowledge.
- If the answer is not in the context, say:
  "I don't know based on the provided data."

Context:
{context}

Question:
{question}

Answer:
"""
)

def create_rag_chain(vectorstore):
    llm = OllamaLLM(
        model="llama3.1:8b",
        temperature=0,
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,   # ✅ CORRECT
        chain_type="stuff",
        chain_type_kwargs={
            "prompt": RAG_PROMPT
        },
        return_source_documents=True,
    )
