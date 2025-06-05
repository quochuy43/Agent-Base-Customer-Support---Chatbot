from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def load_retriever(persist_dir="db"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    return vectordb.as_retriever()