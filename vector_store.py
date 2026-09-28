from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = "./documents/manual_technova.pdf"

embeddings_model = OllamaEmbeddings(model="mxbai-embed-large:latest")
persistent_database_path = "./chroma_db"

if Path(persistent_database_path).exists():
    vector_store = Chroma(
        persist_directory=persistent_database_path,
        embedding_function=embeddings_model,
    )
else:
    if Path(pdf_path).exists():
        report = PyPDFLoader(pdf_path).load()
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150
        )

        chunks = splitter.split_documents(report)

        vector_store = Chroma.from_documents(
            chunks,
            embeddings_model,
            persist_directory=persistent_database_path
        )
    else:
        raise FileNotFoundError("PDF not found")

# k = the number of documents I want to get
retriever = vector_store.as_retriever(search_kwargs={"k": 4})
