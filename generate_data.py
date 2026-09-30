"""Instructor supplied simulator. Students run this file without editing it."""
import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
DATA.mkdir(exist_ok=True)
customers = [
    ["C001", "Lina", "lina@example.test", "Amman"],
    ["C002", "Omar", "", "Irbid"],
    ["C003", "Noor", "noor@example.test", "Amman"],
    ["C003", "Noor", "noor@example.test", "Amman"],
    ["C004", "Sami", "sami@example.test", "Zarqa"],
]
with (DATA / "customers.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id", "name", "email", "city"])
    writer.writerows(customers)
products = [
    {"product_id": "P001", "name": "Coffee", "category": "Grocery", "price_jod": 5},
    {"product_id": "P002", "name": "Notebook", "category": "Stationery", "price_jod": 2},
    {"product_id": "P003", "name": "Mug", "price_jod": 4},
]
(DATA / "products.json").write_text(json.dumps(products, indent=2), encoding="utf-8")
orders = {
    "2026-09-01": [
        ["O001", "C001", "P001", 1, "2026-09-01"],
        ["O002", "C002", "P002", 2, "2026-09-01"],
        ["O003", "C003", "P003", 1, "2026-09-01"],
        ["O004", "C004", "P001", 2, "2026-09-01"],
    ],
    "2026-09-02": [
        ["O005", "C001", "P002", 1, "2026-09-02"],
        ["O006", "C002", "P003", 2, "2026-09-02"],
        ["O006", "C002", "P003", 2, "2026-09-02"],
        ["O007", "", "P001", 1, "2026-09-02"],
    ],
    "2026-09-03": [
        ["O008", "C003", "P001", 1, "03/09/2026"],
        ["O009", "C004", "P002", "two", "2026-09-03"],
        ["O010", "C001", "P003", 1, "2026-09-03"],
        ["O011", "C002", "P001", 2, "2026-09-03"],
    ],
}
for day, rows in orders.items():
    with (DATA / f"orders_{day}.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["order_id", "customer_id", "product_id", "quantity", "order_date"])
        writer.writerows(rows)
print("Created data/customers.csv: 5 rows")
print("Created data/products.json: 3 records")
print("Created 3 daily orders CSV files: 4 rows each")
print("Synthetic practice data only. Re-running replaces these five files.")
