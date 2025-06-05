from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from .prompts import rag_prompt
from .retriever import load_retriever
from langchain_core.runnables import RunnableMap

retriever = load_retriever()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)

rag_chain = RunnableMap({
    "context": retriever,
    "question": lambda x: x["question"]
}) | rag_prompt | llm | StrOutputParser()