from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_messages([
    ("system", "Bạn là trợ lý hỗ trợ khách hàng trong lĩnh vực thương mại điện tử. Trả lời ngắn gọn và chính xác dựa trên ngữ cảnh được cung cấp. Nếu không có đủ thông tin, hãy nói 'Xin vui lòng cung cấp thêm chi tiết.'"),
    ("human", "Ngữ cảnh: {}\n\nCâucontext hỏi: {question}")
])