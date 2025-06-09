import streamlit as st
from src.agent.agent_graph import run_agent

from src.utils.config import load_config
config = load_config()

st.set_page_config(page_title="E-commerce Chatbot", page_icon="🛍️")
st.title("🛒 Chatbot Hỗ trợ Khách hàng")

# Lưu history chat, tạo bộ nhớ tạm cho phiên làm việc
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show hischat
for role, msg in st.session_state.chat_history:
    if role == 'user':
        st.chat_message('user').write(msg)
    else:
        st.chat_message('assistant').write(msg)

user_input = st.chat_input("Nhập câu hỏi của bạn...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(("user", user_input))

    try:
        with st.spinner("🤖 Đang suy nghĩ..."):
            response = run_agent(user_input)
        st.chat_message("assistant").write(response)
        st.session_state.chat_history.append(("assistant", response))
    
    except Exception as e:
        err_msg = str(e)
        if "429" in err_msg:
            friendly_error = "⚠️ Bạn đang gửi quá nhiều yêu cầu. Vui lòng thử lại sau."
        else:
            friendly_error = "❌ Có lỗi xảy ra. Vui lòng thử lại."
        st.chat_message("assistant").write(friendly_error)
        st.session_state.chat_history.append(("assistant", friendly_error))



# import streamlit as st
# import time
# from datetime import datetime
# from src.agent.agent_graph import run_agent

# # Cấu hình trang với theme tối
# st.set_page_config(
#     page_title="E-commerce AI Assistant", 
#     page_icon="🛍️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS để làm đẹp giao diện
# st.markdown("""
# <style>
#     /* Import Google Fonts */
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
#     /* Main container styling */
#     .main {
#         font-family: 'Inter', sans-serif;
#     }
    
#     /* Header styling */
#     .header-container {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         padding: 2rem;
#         border-radius: 15px;
#         margin-bottom: 2rem;
#         text-align: center;
#         box-shadow: 0 10px 30px rgba(0,0,0,0.1);
#     }
    
#     .header-title {
#         color: white;
#         font-size: 2.5rem;
#         font-weight: 700;
#         margin-bottom: 0.5rem;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
#     }
    
#     .header-subtitle {
#         color: rgba(255,255,255,0.9);
#         font-size: 1.1rem;
#         font-weight: 300;
#     }
    
#     /* Chat container */
#     .chat-container {
#         background: white;
#         border-radius: 15px;
#         padding: 1.5rem;
#         box-shadow: 0 5px 20px rgba(0,0,0,0.08);
#         margin-bottom: 2rem;
#         min-height: 400px;
#         max-height: 600px;
#         overflow-y: auto;
#     }
    
#     /* Stats cards */
#     .stats-card {
#         background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#         padding: 1rem;
#         border-radius: 10px;
#         text-align: center;
#         color: white;
#         margin: 0.5rem 0;
#     }
    
#     .stats-number {
#         font-size: 1.8rem;
#         font-weight: 700;
#         margin-bottom: 0.2rem;
#     }
    
#     .stats-label {
#         font-size: 0.9rem;
#         opacity: 0.9;
#     }
    
#     /* Quick actions */
#     .quick-action {
#         background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
#         padding: 0.8rem;
#         border-radius: 8px;
#         margin: 0.3rem 0;
#         border: none;
#         cursor: pointer;
#         width: 100%;
#         text-align: left;
#         transition: transform 0.2s;
#     }
    
#     .quick-action:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 5px 15px rgba(0,0,0,0.1);
#     }
    
#     /* Typing indicator */
#     .typing-indicator {
#         display: flex;
#         align-items: center;
#         padding: 1rem;
#         background: #f8f9fa;
#         border-radius: 20px;
#         margin: 1rem 0;
#     }
    
#     .typing-dot {
#         width: 8px;
#         height: 8px;
#         border-radius: 50%;
#         background: #667eea;
#         margin: 0 2px;
#         animation: typing 1.4s infinite ease-in-out;
#     }
    
#     .typing-dot:nth-child(1) { animation-delay: -0.32s; }
#     .typing-dot:nth-child(2) { animation-delay: -0.16s; }
    
#     @keyframes typing {
#         0%, 80%, 100% { transform: scale(0.8); opacity: 0.5; }
#         40% { transform: scale(1); opacity: 1; }
#     }
    
#     /* Message styling */
#     .message-time {
#         font-size: 0.7rem;
#         color: #999;
#         margin-top: 0.3rem;
#     }
    
#     /* Footer */
#     .footer {
#         text-align: center;
#         padding: 2rem;
#         color: #666;
#         border-top: 1px solid #eee;
#         margin-top: 3rem;
#     }
    
#     /* Hide streamlit default elements */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     .stDeployButton {display:none;}
# </style>
# """, unsafe_allow_html=True)

# # Header với thiết kế đẹp
# st.markdown("""
# <div class="header-container">
#     <div class="header-title">🛒 AI Shopping Assistant</div>
#     <div class="header-subtitle">Trợ lý mua sắm thông minh - Hỗ trợ 24/7</div>
# </div>
# """, unsafe_allow_html=True)

# # Sidebar với thông tin và tính năng
# with st.sidebar:
#     st.markdown("### 📊 Thống kê phiên làm việc")
    
#     # Khởi tạo session state
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []
#     if "message_count" not in st.session_state:
#         st.session_state.message_count = 0
#     if "session_start" not in st.session_state:
#         st.session_state.session_start = datetime.now()
    
#     # Thống kê
#     total_messages = len(st.session_state.chat_history)
#     user_messages = len([msg for role, msg in st.session_state.chat_history if role == 'user'])
#     session_duration = datetime.now() - st.session_state.session_start
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown(f"""
#         <div class="stats-card">
#             <div class="stats-number">{total_messages}</div>
#             <div class="stats-label">Tin nhắn</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown(f"""
#         <div class="stats-card">
#             <div class="stats-number">{user_messages}</div>
#             <div class="stats-label">Câu hỏi</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown(f"⏱️ **Thời gian:** {str(session_duration).split('.')[0]}")
    
#     st.markdown("---")
    
#     # Quick Actions
#     st.markdown("### ⚡ Câu hỏi gợi ý")
    
#     quick_questions = [
#         "🏷️ Sản phẩm khuyến mãi hôm nay",
#         "📱 Điện thoại mới nhất",
#         "👕 Thời trang trending",
#         "🏠 Đồ gia dụng hot",
#         "💄 Mỹ phẩm bestseller",
#         "📦 Tra cứu đơn hàng"
#     ]
    
#     for question in quick_questions:
#         if st.button(question, key=question, help=f"Hỏi về {question}"):
#             st.session_state.quick_question = question.split(" ", 1)[1]
    
#     st.markdown("---")
    
#     # Settings
#     st.markdown("### ⚙️ Cài đặt")
    
#     # Theme toggle (placeholder)
#     theme_mode = st.selectbox("🎨 Giao diện", ["Sáng", "Tối", "Tự động"])
    
#     # Language selection
#     language = st.selectbox("🌐 Ngôn ngữ", ["Tiếng Việt", "English"])
    
#     # Clear chat button
#     if st.button("🗑️ Xóa lịch sử chat", type="secondary"):
#         st.session_state.chat_history = []
#         st.session_state.message_count = 0
#         st.session_state.session_start = datetime.now()
#         st.rerun()

# # Main chat area
# st.markdown("### 💬 Trò chuyện")

# # Container cho chat
# chat_container = st.container()

# with chat_container:
#     # Hiển thị welcome message nếu chưa có chat
#     if not st.session_state.chat_history:
#         st.markdown("""
#         <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); border-radius: 15px; margin: 1rem 0;">
#             <h3 style="color: #333; margin-bottom: 1rem;">👋 Xin chào! Tôi là trợ lý AI</h3>
#             <p style="color: #666; margin-bottom: 0;">Hãy hỏi tôi về sản phẩm, giá cả, khuyến mãi, hoặc bất kỳ điều gì bạn muốn biết!</p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     # Hiển thị lịch sử chat
#     for i, (role, msg) in enumerate(st.session_state.chat_history):
#         timestamp = datetime.now().strftime("%H:%M")
        
#         if role == 'user':
#             with st.chat_message('user', avatar="👤"):
#                 st.write(msg)
#                 st.markdown(f'<div class="message-time">📤 {timestamp}</div>', unsafe_allow_html=True)
#         else:
#             with st.chat_message('assistant', avatar="🤖"):
#                 st.write(msg)
#                 st.markdown(f'<div class="message-time">📥 {timestamp}</div>', unsafe_allow_html=True)

# # Input area với placeholder đẹp
# user_input = st.chat_input("💭 Nhập câu hỏi của bạn... (VD: 'Tìm điện thoại dưới 10 triệu')")

# # Xử lý quick question
# if "quick_question" in st.session_state:
#     user_input = st.session_state.quick_question
#     del st.session_state.quick_question

# # Xử lý input
# if user_input:
#     # Hiển thị message của user
#     timestamp = datetime.now().strftime("%H:%M")
#     with st.chat_message("user", avatar="👤"):
#         st.write(user_input)
#         st.markdown(f'<div class="message-time">📤 {timestamp}</div>', unsafe_allow_html=True)
    
#     st.session_state.chat_history.append(("user", user_input))
#     st.session_state.message_count += 1
    
#     # Hiển thị typing indicator
#     with st.chat_message("assistant", avatar="🤖"):
#         typing_placeholder = st.empty()
#         typing_placeholder.markdown("""
#         <div class="typing-indicator">
#             <span style="margin-right: 10px;">🤖 Đang suy nghĩ</span>
#             <div class="typing-dot"></div>
#             <div class="typing-dot"></div>
#             <div class="typing-dot"></div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         try:
#             # Gọi agent
#             response = run_agent(user_input)
            
#             # Xóa typing indicator và hiển thị response
#             typing_placeholder.empty()
#             st.write(response)
#             timestamp = datetime.now().strftime("%H:%M")
#             st.markdown(f'<div class="message-time">📥 {timestamp}</div>', unsafe_allow_html=True)
            
#             st.session_state.chat_history.append(("assistant", response))
            
#         except Exception as e:
#             typing_placeholder.empty()
#             err_msg = str(e)
            
#             if "429" in err_msg:
#                 friendly_error = "⚠️ **Tốc độ quá nhanh!** \n\nBạn đang gửi quá nhiều yêu cầu. Vui lòng chờ một chút và thử lại. 😊"
#             elif "timeout" in err_msg.lower():
#                 friendly_error = "⏱️ **Hết thời gian chờ!** \n\nKết nối bị chậm. Vui lòng thử lại câu hỏi. 🔄"
#             elif "connection" in err_msg.lower():
#                 friendly_error = "🌐 **Lỗi kết nối!** \n\nKiểm tra kết nối internet và thử lại. 📶"
#             else:
#                 friendly_error = "❌ **Có lỗi xảy ra!** \n\nVui lòng thử lại hoặc liên hệ hỗ trợ. 🛠️"
            
#             st.error(friendly_error)
#             timestamp = datetime.now().strftime("%H:%M")
#             st.markdown(f'<div class="message-time">⚠️ {timestamp}</div>', unsafe_allow_html=True)
            
#             st.session_state.chat_history.append(("assistant", friendly_error))

# # Footer
# st.markdown("""
# <div class="footer">
#     <p>🚀 Powered by AI Technology | 💝 Made with Streamlit</p>
#     <p style="font-size: 0.8rem; margin-top: 0.5rem;">
#         📞 Hỗ trợ: support@company.com | 🌐 Website: company.com
#     </p>
# </div>
# """, unsafe_allow_html=True)

# # Real-time stats update (chạy mỗi 30 giây)
# if st.session_state.message_count > 0:
#     time.sleep(0.1)  # Nhỏ delay để tránh lag