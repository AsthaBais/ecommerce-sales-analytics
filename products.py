import pandas as pd
import random
from .config import *
print("Products module is running...")
def generate_products():

    catalog = {
        1: {  # Electronics
            "Apple": ["iPhone 16", "MacBook Air", "iPad Air"],
            "Samsung": ["Galaxy S25", "Galaxy Tab S10", "Smart TV"],
            "Dell": ["Inspiron 15", "XPS 13"],
            "HP": ["Pavilion Laptop", "Victus Laptop"],
            "Sony": ["Bravia TV", "WH-1000XM5 Headphones"]
        },

        2: {  # Fashion
            "Nike": ["Running Shoes", "Sports T-Shirt"],
            "Adidas": ["Sneakers", "Track Pants"],
            "Puma": ["Hoodie", "T-Shirt"],
            "Levis": ["Jeans", "Jacket"]
        },

        3: {  # Home & Kitchen
            "Prestige": ["Mixer Grinder", "Pressure Cooker"],
            "Milton": ["Water Bottle", "Lunch Box"],
            "Cello": ["Dinner Set", "Storage Box"]
        },

        4: {  # Beauty
            "Lakme": ["Lipstick", "Face Wash"],
            "Nivea": ["Moisturizer", "Body Lotion"],
            "Dove": ["Shampoo", "Soap"]
        },

        5: {  # Sports
            "SG": ["Cricket Bat"],
            "Yonex": ["Badminton Racket"],
            "Nivia": ["Football"],
            "Boldfit": ["Yoga Mat"]
        },

        6: {  # Books
            "Pearson": ["Python Programming"],
            "O'Reilly": ["SQL Cookbook"],
            "Packt": ["Data Science Handbook"]
        },

        7: {  # Toys
            "LEGO": ["Building Blocks"],
            "Hot Wheels": ["Toy Car"],
            "Mattel": ["Barbie Doll"]
        },

        8: {  # Grocery
            "Fortune": ["Basmati Rice"],
            "Tata": ["Tea"],
            "Nescafe": ["Coffee"],
            "Saffola": ["Cooking Oil"]
        },

        9: {  # Furniture
            "Nilkamal": ["Office Chair"],
            "IKEA": ["Study Table"],
            "Home Centre": ["Sofa"]
        },

        10: {  # Accessories
            "Wildcraft": ["Laptop Bag"],
            "Titan": ["Wallet"],
            "Fastrack": ["Watch"]
        }
    }

    colors = ["Black", "White", "Blue", "Red", "Silver"]

    products = []

    for product_id in range(1, TOTAL_PRODUCTS + 1):

        category_id = random.randint(1, 10)

        brand = random.choice(list(catalog[category_id].keys()))

        product = random.choice(catalog[category_id][brand])

        variant = random.choice(colors)

        cost_price = random.randint(500, 80000)

        selling_price = int(cost_price * random.uniform(1.1, 1.4))

        discount = random.choice([0, 5, 10, 15, 20])

        stock = random.randint(20, 300)

        products.append({
            "product_id": product_id,
            "product_name": f"{brand} {product} ({variant})",
            "category_id": category_id,
            "brand": brand,
            "cost_price": cost_price,
            "selling_price": selling_price,
            "discount_percent": discount,
            "stock": stock
        })

    df = pd.DataFrame(products)

    df.to_csv("Dataset/products.csv", index=False)

    print(f"✅ Products Generated : {len(df)}")
    def generate_products():
     print("Inside generate_products()")