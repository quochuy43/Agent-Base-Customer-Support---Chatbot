import pandas as pd
from langsmith import Client
from src.rag.rag_chain import get_rag_chain
from src.utils.config import load_config

def evaluate_chatbot():
    config = load_config()
    client = Client()
    rag_chain = get_rag_chain()

    eval_data = pd.read_csv("src/traces/evaluation_dataset.csv")

    # Tạo dataset trên langsmith
    dataset_name = "CustomerSupportEval"
    dataset = client.create_dataset(dataset_name=dataset_name)

    # Thêm ex vào dataset
    for _, row in eval_data.iterrows():
        client.create_example(
            inputs={"query": row["query"]},
            outputs={"expected_response": row["expected_response"]},
            dataset_id=dataset.id
        )

    # Chạy đánh giá
    for _, row in eval_data.iterrows():
        query = row["query"]
        try:
            response = rag_chain.invoke(query)
            # Lấy run gần nhất bằng cách lọc theo query và dataset
            runs = client.list_runs(project_name="CustomerSupportChatbot", inputs={"query": query}, limit=1)
            run = next(runs, None)
            if run:
                run_id = run.id
                score = 1 if response.strip() == row["expected_response"].strip() else 0
                client.create_feedback(
                    run_id=run_id,
                    key="accuracy",
                    score=score,
                    comment=f"Query: {query}\nActual: {response}\nExpected: {row['expected_response']}"
                )
            else:
                print(f"No run found for query '{query}'")
        except Exception as e:
            print(f"Error evaluating query '{query}': {str(e)}")

if __name__ == "__main__":
    evaluate_chatbot()