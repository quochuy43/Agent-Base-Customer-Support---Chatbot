from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

_embeddings = None

def get_retriever(persist_directory="db", k=5):
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=_embeddings)
    return vectordb.as_retriever(search_kwargs={"k": k})

# retriever = get_retriever()
# docs = retriever.invoke("giá của Bánh Mì Pate Trứng")
# for doc in docs:
#     print(doc.page_content)