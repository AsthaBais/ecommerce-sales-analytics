import pandas as pd
import random
from .config import *

def generate_orders():

    status_list = [
        "Delivered",
        "Shipped",
        "Processing",
        "Cancelled"
    ]

    orders = []

    for order_id in range(1, TOTAL_ORDERS + 1):

        orders.append({
            "order_id": order_id,
            "customer_id": random.randint(1, TOTAL_CUSTOMERS),
            "order_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            "status": random.choice(status_list),
            "shipper_id": random.randint(1, 5)
        })

    df = pd.DataFrame(orders)

    df.to_csv("Dataset/orders.csv", index=False)

    print(f"✅ Orders Generated : {len(df)}")