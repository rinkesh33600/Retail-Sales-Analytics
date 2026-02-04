# load.py
# Load data into MySQL

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rinkesh@8430",
        database="analytics_platform"
    )

def load_customers(df):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE staging_customers")

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO staging_customers 
            (customer_id, customer_name, gender, age, city, state, country)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                row["customer_id"],
                row["customer_name"],
                row["gender"],
                row["age"],
                row["city"],
                row["state"],
                row["country"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

def load_orders(df):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE staging_orders")

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO staging_orders 
            (order_id, order_date, customer_id, product_id, store_id, promo_id,
             quantity, sales_amount, cost_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                row["order_id"],
                row["order_date"],
                row["customer_id"],
                row["product_id"],
                row["store_id"],
                row["promo_id"],
                row["quantity"],
                row["sales_amount"],
                row["cost_amount"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

def load_products(df):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE staging_products")

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO staging_products 
            (product_id, product_name, brand, sub_category, category)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                row["product_id"],
                row["product_name"],
                row["brand"],
                row["sub_category"],
                row["category"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

def load_stores(df):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE staging_stores")

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO staging_stores 
            (store_id, store_name, city, state, region, store_type)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                row["store_id"],
                row["store_name"],
                row["city"],
                row["state"],
                row["region"],
                row["store_type"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

def load_promotions(df):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE staging_promotions")

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO staging_promotions 
            (promo_id, promotion_type, discount_pct, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                row["promo_id"],
                row["promotion_type"],
                row["discount_pct"],
                row["start_date"],
                row["end_date"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

