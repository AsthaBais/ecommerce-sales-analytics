import pandas as pd
import random
from .config import *

def generate_returns():

    reasons = [
        "Damaged",
        "Wrong Item",
        "Defective",
        "Quality Issue",
        "Size Issue"
    ]

    returns = []

    return_id = 1

    for order_id in range(1, TOTAL_ORDERS + 1):

        if random.random() < 0.10:

            returns.append({
                "return_id": return_id,
                "order_id": order_id,
                "reason": random.choice(reasons),
                "return_date": fake.date_between(
                    start_date="-1y",
                    end_date="today"
                )
            })

            return_id += 1

    df = pd.DataFrame(returns)

    df.to_csv("Dataset/returns.csv", index=False)

    print(f"✅ Returns Generated : {len(df)}")