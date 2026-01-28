# this is document loader
from pathlib import Path 
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

DATA_DIR = Path("data/docs")

def load_documents() -> list[Document]:
    documents: list[Document] = []
    for file in DATA_DIR.iterdir():
        if file.suffix == ".pdf":
            loader = PyPDFLoader(str(file))
            documents.extend(loader.load())
        elif file.suffix in [".txt", ".md"]:
            loader = TextLoader(str(file), encoding="utf-8")
            documents.extend(loader.load())
    
    return documents

def split_documents(documents: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120,
        separators=["\n\n", "\n", ".", " ", ""],
    )
    return splitter.split_documents(documents)

"""
This splitter:
Tries to split by paragraphs
Then lines
Then sentences
Then words (only if needed)
➡️ This preserves meaning better than naive slicing.
separators
Order matters:
["\n\n", "\n", ".", " ", ""]
Means:
First try splitting by paragraphs
If still too big → sentences
Worst case → character-level
"""