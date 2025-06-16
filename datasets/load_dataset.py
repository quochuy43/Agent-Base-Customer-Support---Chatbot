from datasets import load_dataset
ds = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset")

ds['train'].to_csv("customer_support_dataset.csv")