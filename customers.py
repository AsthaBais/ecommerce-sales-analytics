import pandas as pd
from .config import *

def generate_customers():

    cities_states = [
        ("Mumbai", "Maharashtra"),
        ("Pune", "Maharashtra"),
        ("Nagpur", "Maharashtra"),
        ("Delhi", "Delhi"),
        ("Bengaluru", "Karnataka"),
        ("Hyderabad", "Telangana"),
        ("Chennai", "Tamil Nadu"),
        ("Ahmedabad", "Gujarat"),
        ("Surat", "Gujarat"),
        ("Jaipur", "Rajasthan"),
        ("Lucknow", "Uttar Pradesh"),
        ("Kolkata", "West Bengal"),
        ("Patna", "Bihar"),
        ("Bhopal", "Madhya Pradesh"),
        ("Indore", "Madhya Pradesh")
    ]

    customers = []

    for customer_id in range(1, TOTAL_CUSTOMERS + 1):

        city, state = random.choice(cities_states)

        first_name = fake.first_name()
        last_name = fake.last_name()

        customers.append({
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": random.choice(["Male", "Female"]),
            "age": random.randint(18, 60),
            "email": f"{first_name.lower()}.{last_name.lower()}{customer_id}@gmail.com",
            "phone": f"9{random.randint(100000000,999999999)}",
            "city": city,
            "state": state,
            "signup_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            )
        })

    customers_df = pd.DataFrame(customers)

    customers_df.to_csv(
        "Dataset/customers.csv",
        index=False
    )

    print("✅ Customers Generated :", len(customers_df))