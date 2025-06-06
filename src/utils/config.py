import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("src/logs/agent.log")
    ]
)

def load_config():
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")
    if not google_api_key:
        logging.error("GOOGLE_API_KEY không được tìm thấy trong .env")
        raise ValueError("GOOGLE_API_KEY không được thiết lập")
    if not langsmith_api_key:
        logging.warning("LANGCHAIN_API_KEY không được tìm thấy, LangSmith sẽ không hoạt động")
    return {"google_api_key": google_api_key, "langsmith_api_key": langsmith_api_key}