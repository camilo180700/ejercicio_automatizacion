import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path
OUTPUT_PATH = Path("data/raw_sales.csv")

def generate_sales_data(n_rows=15000):
    print(f"Generating {n_rows} rows of synthetic sales data...")
    # Datos base
    customers = ["Ana", "Luis", "Carlos", "Maria", "Jorge", "Sofia", "Diego", "Valeria"]
    regions = ["Norte", "Sur", "Centro", "Este", "Oeste"]
    products = {
        "Laptop": (900, 1500),
        "Mouse": (15, 40),
        "Keyboard": (50, 120),
        "Monitor": (200, 600),
        "Tablet": (250, 800),
        "Headphones": (30, 200)
    }
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 12, 31)
    date_range_days = (end_date - start_date).days
    data = []
    for order_id in range(1, n_rows + 1):
        product = random.choice(list(products.keys()))
        price_range = products[product]
        random_days = random.randint(0, date_range_days)
        date = start_date + timedelta(days=random_days)
        quantity = np.random.poisson(lam=2) + 1  # más realista que random.randint
        price = round(random.uniform(*price_range), 2)
        data.append([
            order_id,
            date.strftime("%Y-%m-%d"),
            random.choice(customers),
            random.choice(regions),
            product,
            quantity,
            price
        ])
    df = pd.DataFrame(data, columns=[
        "order_id",
        "date",
        "customer",
        "region",
        "product",
        "quantity",
        "price"
    ])
    return df

def save_data(df):
    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    df = generate_sales_data(n_rows=20000)  # puedes cambiar aquí
    save_data(df)