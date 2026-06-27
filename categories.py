import pandas as pd
from .config import *

def generate_categories():

    categories = [
        "Electronics",
        "Fashion",
        "Home & Kitchen",
        "Beauty",
        "Sports",
        "Books",
        "Toys",
        "Grocery",
        "Furniture",
        "Accessories"
    ]

    df = pd.DataFrame({
        "category_id": range(1, 11),
        "category_name": categories
    })

    df.to_csv("Dataset/categories.csv", index=False)

    print("✅ Categories Generated")