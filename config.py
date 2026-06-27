from faker import Faker
import random
import numpy as np
import os

fake = Faker("en_IN")

random.seed(42)
np.random.seed(42)

os.makedirs("Dataset", exist_ok=True)

TOTAL_CUSTOMERS = 5000
TOTAL_PRODUCTS = 500
TOTAL_ORDERS = 20000