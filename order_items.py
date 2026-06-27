import pandas as pd
import random
from .config import *

def generate_order_items():

    items = []
    item_id = 1

    for order_id in range(1, TOTAL_ORDERS + 1):

        # Har order me 1–5 products honge
        no_of_products = random.randint(1, 5)

        for _ in range(no_of_products):

            quantity = random.randint(1, 4)

            price = random.randint(500, 80000)

            items.append({
                "order_item_id": item_id,
                "order_id": order_id,
                "product_id": random.randint(1, TOTAL_PRODUCTS),
                "quantity": quantity,
                "unit_price": price
            })

            item_id += 1

    df = pd.DataFrame(items)

    df.to_csv("Dataset/order_items.csv", index=False)

    print(f"✅ Order Items Generated : {len(df)}")