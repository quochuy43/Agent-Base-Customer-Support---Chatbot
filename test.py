# TEST 1
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



# TEST 2
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




# TEST 3
# from src.rag.rag_chain import get_rag_chain
# chain = get_rag_chain()
# response = chain.invoke("Cho mình xin đường link sản phẩm về Apple Iphone 14")
# print(response)

# import shutil

# shutil.rmtree("db", ignore_errors=True)
# print("Đã xóa thư mục db cũ.")

# TEST 4
from src.agent.agent_graph import run_agent

questions = [
    "Chính sách đổi trả là gì?",
    "Chi phí vận chuyển bao nhiêu?",
    "Cho mình xin giá Apple Iphone 14 đi ạ",
    "Mặt trăng làm từ gì?"
]
for question in questions:
    response = run_agent(question)
    print(f"Câu hỏi: {question}\nTrả lời: {response}\n")




# TEST 5
# from sentence_transformers import SentenceTransformer
# sentences = ["This is an example sentence", "Each sentence is converted"]

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# embeddings = model.encode(sentences)
# print(embeddings)




# TEST 6
# Xóa db cũ:
# import shutil

# shutil.rmtree("db", ignore_errors=True)
# print("Đã xóa thư mục db cũ.")




# TEST 7
# import streamlit as st
# from src.agent.agent_graph import run_agent

# from src.utils.config import load_config
# config = load_config()

# st.set_page_config(page_title="E-commerce Chatbot", page_icon="🛍️")
# st.title("🛒 Chatbot Hỗ trợ Khách hàng")

# # Lưu history chat, tạo bộ nhớ tạm cho phiên làm việc
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # show hischat
# for role, msg in st.session_state.chat_history:
#     if role == 'user':
#         st.chat_message('user').write(msg)
#     else:
#         st.chat_message('assistant').write(msg)

# user_input = st.chat_input("Nhập câu hỏi của bạn...")

# if user_input:
#     st.chat_message("user").write(user_input)
#     st.session_state.chat_history.append(("user", user_input))

#     try:
#         with st.spinner("🤖 Đang suy nghĩ..."):
#             response = run_agent(user_input)
#         st.chat_message("assistant").write(response)
#         st.session_state.chat_history.append(("assistant", response))
    
#     except Exception as e:
#         err_msg = str(e)
#         if "429" in err_msg:
#             friendly_error = "⚠️ Bạn đang gửi quá nhiều yêu cầu. Vui lòng thử lại sau."
#         else:
#             friendly_error = "❌ Có lỗi xảy ra. Vui lòng thử lại."
#         st.chat_message("assistant").write(friendly_error)
#         st.session_state.chat_history.append(("assistant", friendly_error))