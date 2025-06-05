from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

def create_vector_store(docs, persist_directory="db"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        documents = docs,
        embedding = embeddings,
        persist_directory=persist_directory
    )
    vectordb.persist()
    return vectordb