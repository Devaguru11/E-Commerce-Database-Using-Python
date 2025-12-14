from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()

# 1️⃣ Customers
customers = []
for i in range(1, 11):  # 10 customers
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "city": fake.city(),
        "pincode": fake.postcode()
    })
pd.DataFrame(customers).to_csv("customers.csv", index=False)
print("✅ customers.csv created")

# 2️⃣ Items
items = []
for i in range(1, 11):  # 10 items
    items.append({
        "item_id": i,
        "item_name": fake.word().capitalize(),
        "item_price": round(random.uniform(100, 1000), 2)
    })
pd.DataFrame(items).to_csv("items.csv", index=False)
print("✅ items.csv created")

# 3️⃣ Orders
orders = []
for i in range(1, 21):  # 20 orders
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 10),
        "order_date": fake.date_between(start_date='-30d', end_date='today'),
        "total_amount": round(random.uniform(500, 5000), 2)
    })
pd.DataFrame(orders).to_csv("orders.csv", index=False)
print("✅ orders.csv created")

# 4️⃣ Order Items
order_items = []
for i in range(1, 51):  # 50 order items
    order_items.append({
        "order_id": random.randint(1, 20),
        "item_id": random.randint(1, 10),
        "quantity": random.randint(1, 5),
        "item_price": round(random.uniform(100, 1000), 2)
    })
pd.DataFrame(order_items).to_csv("order_items.csv", index=False)
print("✅ order_items.csv created")

print("🎉 All CSVs generated successfully!")
