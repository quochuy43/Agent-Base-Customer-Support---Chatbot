# from src.embeddings.embed_store import create_vector_store
# from src.loaders.document_loader import load_and_split_documents

# if __name__ == "__main__":
#     docs = load_and_split_documents()
#     vectorstore = create_vector_store(docs)
    
#     retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

#     query = "Các bước để đặt hàng ạ"
#     docs = retriever.get_relevant_documents(query)

#     for i, doc in enumerate(docs):
#         print(f"\n--- Kết quả {i+1} ---\n {doc.page_content[:300]}...")

# test.py
# from src.rag.rag_chain import rag_chain

# questions = [
#     "Chính sách đổi trả là gì?",
#     "Chi phí vận chuyển bao nhiêu?",
#     "Làm sao để đổi sản phẩm lỗi?"
# ]

# for q in questions:
#     print("-", q)
#     answer = rag_chain.invoke({"question": q})
#     print("-", answer)
#     print("-" * 50)


# from src.rag.rag_chain import get_rag_chain
# chain = get_rag_chain()
# response = chain.invoke("Chính sách đổi trả là gì?")
# print(response)

from src.agent.agent_graph import run_agent

questions = [
    "Chính sách đổi trả là gì?",
    "Chi phí vận chuyển bao nhiêu?",
    "Tôi muốn mua sản phẩm X, làm thế nào?",
    "Mặt trăng làm từ gì?"
]
for question in questions:
    response = run_agent(question)
    print(f"Câu hỏi: {question}\nTrả lời: {response}\n")
