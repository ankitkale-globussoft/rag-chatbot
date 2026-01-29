from langchain_core.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template=
    """
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