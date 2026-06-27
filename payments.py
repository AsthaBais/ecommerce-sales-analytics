import pandas as pd
import random
from .config import *

def generate_payments():

    payment_methods = [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Cash on Delivery"
    ]

    payments = []

    for payment_id in range(1, TOTAL_ORDERS + 1):

        payments.append({
            "payment_id": payment_id,
            "order_id": payment_id,
            "payment_method": random.choice(payment_methods),
            "payment_status": random.choice(["Paid","Paid","Paid","Pending"]),
            "transaction_id": fake.uuid4()[:12]
        })

    df = pd.DataFrame(payments)

    df.to_csv("Dataset/payments.csv", index=False)

    print(f"✅ Payments Generated : {len(df)}")