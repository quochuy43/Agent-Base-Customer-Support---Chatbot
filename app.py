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



import streamlit as st
import time
from datetime import datetime
from src.agent.agent_graph import run_agent

st.set_page_config(
    page_title="E-commerce AI Assistant",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# custom css
st.markdown("""
<style>
    /* Import Google Fonts */
            
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    .main {
        font-family: 'Inter', sans-serif;
    }
            
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
            
    .header-title {
        color: black;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
            
    .header-subtitle {
        color: black;
        font-size: 1.1rem;
        font-weight: 300;
    }
            
    /* Stats cards */
    .stats-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin: 0.5rem 0;
    }
            
    .stats-number {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    
    .stats-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
            
    /* Message styling */
    .message-time {
        font-size: 0.75rem;
        color: #999;
    }
            
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        border-top: 1px solid #eee;
        margin-top: 3rem;
    }
            
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <div class="header-title">👋 Xin chào! Tôi là trợ lý AI</div>
    <div class="header-subtitle">Trợ lý mua sắm thông minh - Hỗ trợ 24/7</div>
</div>
""", unsafe_allow_html=True)

# Sidebar with info and feature
with st.sidebar:
    st.markdown("### 📊 Thống kê")

    # init session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "message_count" not in st.session_state:
        st.session_state.message_count = 0
    if "session_start" not in st.session_state:
        st.session_state.session_start = datetime.now()

    # statistics
    total_messages = len(st.session_state.chat_history)
    user_messages = len([msg for role, msg in st.session_state.chat_history if role == 'user'])
    session_duration = datetime.now() - st.session_state.session_start

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{total_messages}</div>
            <div class="stats-label">Tin nhắn</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{user_messages}</div>
            <div class="stats-label">Câu hỏi</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"⏱️ **Thời gian:** {str(session_duration).split('.')[0]}")

    st.markdown("---")

    # Quick actions
    st.markdown("### ⚡ Câu hỏi gợi ý")
    quick_questions = [
        "Thông tin về Apple iPhone 16 Pro Max",
        "Chính sách đổi trả như thế nào ạ",
        "Quy trình đặt hàng như nào",
        "Cho mình xin thông tin vận chuyển ạ",
        "Kiểm tra trạng thái đơn hàng như nào",
        "xin giá Combo 4 tấm che nắng ô tô"
    ]

    for question in quick_questions:
        if st.button(question, key=question, help=question):
            st.session_state.quick_question = question
    
    st.markdown("---")
    # Clear chat button
    if st.button("🗑️ Xóa lịch sử chat", type="secondary"):
        st.session_state.chat_history = []
        st.session_state.message_count = 0
        st.session_state.session_start = datetime.now()
        st.rerun()

# Main chat area
st.markdown("### 💬 Trò chuyện")

chat_container = st.container()

# display welcome message if chat not yet
with chat_container:

    # display his
    for i, (role, msg) in enumerate(st.session_state.chat_history):
        timestamp = datetime.now().strftime("%H:%M")
        if role == 'user':
            with st.chat_message('user', avatar="👤"):
                st.write(msg)
                st.markdown(f'<div class="message-time">🕰️ {timestamp}</div>', unsafe_allow_html=True)
        else:
            with st.chat_message('assistant', avatar="🤖"):
                st.write(msg)
                st.markdown(f'<div class="message-time">🕰️ {timestamp}</div>', unsafe_allow_html=True)

# Input area
user_input = st.chat_input("💬 Nhập câu hỏi của bạn... (VD: 'Xin giá trà sữa truyền thống')")

# Handle quick_question
if "quick_question" in st.session_state:
    user_input = st.session_state.quick_question
    del st.session_state.quick_question

if user_input:
    # display user's message
    timestamp = datetime.now().strftime("%H:%M")
    with st.chat_message("user", avatar="👤"):
        st.write(user_input)
        st.markdown(f'<div class="message-time">🕰️ {timestamp}</div>', unsafe_allow_html=True)

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.message_count += 1

    with st.chat_message("assistant", avatar="🤖"):
        try:
            with st.spinner("Đợi tôi một xíu..."):
            # call agent
                response = run_agent(user_input)

                st.write(response)
                timestamp = datetime.now().strftime("%H:%M")
                st.markdown(f'<div class="message-time">🕰️ {timestamp}</div>', unsafe_allow_html=True)
                
                st.session_state.chat_history.append(("assistant", response))
        
        except Exception as e:
            err_msg = str(e)
            
            if "429" in err_msg:
                friendly_error = "**Tốc độ quá nhanh!** \n\nBạn đang gửi quá nhiều yêu cầu. Vui lòng chờ một chút và thử lại. 😊"
            elif "timeout" in err_msg.lower():
                friendly_error = "**Hết thời gian chờ!** \n\nKết nối bị chậm. Vui lòng thử lại câu hỏi. 🔄"
            elif "connection" in err_msg.lower():
                friendly_error = "**Lỗi kết nối!** \n\nKiểm tra kết nối internet và thử lại. 📶"
            else:
                friendly_error = "**Có lỗi xảy ra!** \n\nVui lòng thử lại hoặc liên hệ hỗ trợ. 🛠️"
            
            st.error(friendly_error)
            timestamp = datetime.now().strftime("%H:%M")
            st.markdown(f'<div class="message-time">🕰️ {timestamp}</div>', unsafe_allow_html=True)
            
            st.session_state.chat_history.append(("assistant", friendly_error))

# Footer
st.markdown("""
<div class="footer">
    <p>Le Van Quoc Huy | Made with Streamlit</p>
    <p style="font-size: 0.8rem; margin-top: 0.5rem;">
        📞 Hỗ trợ: 0123456789 | 🌐 Website: lvqh.com
    </p>
</div>
""", unsafe_allow_html=True)

# Real-time stats update (chạy mỗi 30 giây)
if st.session_state.message_count > 0:
    time.sleep(0.1)