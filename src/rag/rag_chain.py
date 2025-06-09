from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from .retriever import get_retriever
from .prompts import get_chatbot_prompt
import os
import time
import logging

# logger = logging.getLogger(__name__)

def get_rag_chain():
    try:
        # Khởi tạo mô hình Gemini
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.2,
            max_output_tokens=500
        )

        # Lấy retriever và prompt
        retriever = get_retriever()
        prompt = get_chatbot_prompt()

        # Định dạng ngữ cảnh từ retriever
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # Tạo chain RAG
        rag_chain = (
            {"context": retriever | format_docs, "query": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        return rag_chain
    except Exception as e:
        if "429" in str(e):
            print("Lỗi: Quá nhiều yêu cầu API. Vui lòng thử lại sau vài giây.")
            time.sleep(5)
            return get_rag_chain()
        else:
            raise e