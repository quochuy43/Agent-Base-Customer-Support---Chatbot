from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_documents(path="knowledge_base"):
    loader = DirectoryLoader(path, glob="**/*.md")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap=200
    )

    docs = splitter.split_documents(documents)
    return docs

