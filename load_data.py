import pandas as pd
import mysql.connector

# -----------------------------
# 🔹 Step 1: Connect to MySQL
# -----------------------------
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='guruji@11',   # 👉 leave blank if you log in to Workbench without a password
        # password='yourpassword',  # 👈 OR put your MySQL password here if you have one
    )
    print("✅ Connected to MySQL successfully!")
except mysql.connector.Error as e:
    print("❌ Error connecting to MySQL:", e)
    exit()

cursor = conn.cursor()

# -----------------------------
# 🔹 Step 2: Create Database
# -----------------------------
cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce;")
cursor.execute("USE ecommerce;")
print("✅ Database 'ecommerce' is ready to use.")

# -----------------------------
# 🔹 Step 3: Create Tables
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100),
    pincode VARCHAR(10)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    item_price DECIMAL(10,2)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_id INT,
    item_id INT,
    quantity INT,
    item_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);
""")

print("✅ Tables created successfully (or already exist).")

# -----------------------------
# 🔹 Step 4: Load CSVs into SQL
# -----------------------------
def load_csv_to_table(filename, table_name):
    try:
        df = pd.read_csv(filename)
        cols = ', '.join(df.columns)
        placeholders = ', '.join(['%s'] * len(df.columns))
        sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"

        for _, row in df.iterrows():
            cursor.execute(sql, tuple(row))

        conn.commit()
        print(f"✅ Data loaded into '{table_name}' successfully.")
    except Exception as e:
        print(f"❌ Error loading {table_name}: {e}")

# --- Load each CSV ---
load_csv_to_table('customers.csv', 'customers')
load_csv_to_table('items.csv', 'items')
load_csv_to_table('orders.csv', 'orders')
load_csv_to_table('order_items.csv', 'order_items')

# -----------------------------
# 🔹 Step 5: Close Connection
# -----------------------------
cursor.close()
conn.close()
print("🎉 All data loaded successfully into MySQL!")
