from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableLambda
from src.rag.rag_chain import get_rag_chain
from src.rag.retriever import get_retriever
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class AgentState(TypedDict):
    query: str
    context: str
    response: str
    error: str | None

def retrieve_node(state: AgentState) -> AgentState:
    # logger.info(f"Retrieving context: {state['query']}")
    try:
        retriever = get_retriever()
        docs = retriever.invoke(state["query"])
        state["context"] = "\n\n".join(doc.page_content for doc in docs) if docs else ""
        if not state["context"]:
            state["error"] = "No relevant documents found"
        return state
    except Exception as e:
        state["error"] = str(e)
        return state

def answer_node(state: AgentState) -> AgentState:
    # logger.info("Generating answer")
    try:
        chain = get_rag_chain()
        response = chain.invoke(state["query"])
        if not response.strip():
            state["error"] = "No answer generated"
        else:
            state["response"] = response
        return state
    except Exception as e:
        logger.error(f"Error in answer_node: {str(e)}")
        state["error"] = str(e)
        return state

def handle_error_node(state: AgentState) -> AgentState:
    logger.info("Handling error")
    if state["error"] and "429" in state["error"]:
        state["response"] = "Quá nhiều yêu cầu API. Thử lại sau."
    elif state["error"]:
        state["response"] = "Không tìm thấy thông tin. Vui lòng thử lại."
    else:
        state["response"] = "Lỗi không xác định. Thử lại."
    return state

def route_to_error(state: AgentState) -> str:
    return "handle_error" if state.get("error") or not state["context"] else "answer"

def build_agent_graph():
    graph = StateGraph(AgentState)
    graph.add_node("retrieve", RunnableLambda(retrieve_node))
    graph.add_node("answer", RunnableLambda(answer_node))
    graph.add_node("handle_error", RunnableLambda(handle_error_node))
    graph.add_edge(START, "retrieve")
    graph.add_conditional_edges("retrieve", route_to_error, {"answer": "answer", "handle_error": "handle_error"})
    graph.add_conditional_edges("answer", route_to_error, {"answer": END, "handle_error": "handle_error"})
    graph.add_edge("handle_error", END)
    return graph.compile()

def run_agent(query: str, max_retries: int = 3) -> str:
    for attempt in range(max_retries):
        try:
            graph = build_agent_graph()
            state = {"query": query, "context": "", "response": "", "error": None}
            result = graph.invoke(state)
            return result["response"]
        except Exception as e:
            logger.error(f"Error (attempt {attempt+1}): {str(e)}")
            if "429" in str(e) and attempt < max_retries - 1:
                time.sleep(15 * (attempt + 1))
                continue
            return "Lỗi. Thử lại."
    return "Lỗi API. Thử lại sau."