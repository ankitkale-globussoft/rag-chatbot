from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

def create_streaming_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are a private assistant.

            Rules:
            - Answer ONLY using the provided context.
            - If the answer is not in the context, say:
              "I don't know based on the provided data."
            """
        ),
        (
            "human",
            """
            Context:
            {context}

            Question:
            {question}
            """
        )
    ])

    llm = ChatOllama(
        model="llama3.1:8b",
        temperature=0,
        streaming=True, 
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
    )

    return chain
