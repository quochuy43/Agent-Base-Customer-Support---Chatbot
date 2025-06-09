import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        "google_api_key": os.getenv("GOOGLE_API_KEY"),
        "langchain_api_key": os.getenv("LANGCHAIN_API_KEY"),
        "langchain_tracing_v2": os.getenv("LANGCHAIN_TRACING_V2"),
        "langchain_project": os.getenv("LANGCHAIN_PROJECT")
    }