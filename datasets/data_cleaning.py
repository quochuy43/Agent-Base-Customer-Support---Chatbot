import pandas as pd
df = pd.read_csv("datasets/cleaned_customer_support_dataset.csv")

# delete duplicate rcs
df = df.drop_duplicates()
df = df.dropna()

valid_intents = [
    "create_account", "delete_account", "edit_account", "switch_account",
    "check_cancellation_fee", "delivery_options", "complaint", "review",
    "check_invoice", "get_invoice", "newsletter_subscription", "cancel_order",
    "change_order", "place_order", "check_payment_methods", "payment_issue",
    "check_refund_policy", "track_refund", "change_shipping_address",
    "set_up_shipping_address"
]

df = df[df["intent"].isin(valid_intents)]

# 100 records/ỉntent
records_per_intent = 65
sampled_df = pd.DataFrame()

for intent in valid_intents:
    intent_df = df[df["intent"] == intent]
    # random, max = valid = records_per_intent
    sampled_intent = intent_df.sample(n=min(records_per_intent, len(intent_df)),
    random_state=42)
    sampled_df = pd.concat([sampled_df, sampled_intent])

sampled_df.to_csv("datasets/reduced_customer_support_dataset.csv", index=False)

print("sum of records: ", len(sampled_df))
print(sampled_df["intent"].value_counts())