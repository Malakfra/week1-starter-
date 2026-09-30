import pandas as pd

customers = pd.read_csv("data/customers.csv")
products = pd.read_json("data/products.json")
orders = pd.read_csv("data/orders_2026-09-03.csv")

print("CUSTOMERS"); print(customers)
print("PRODUCTS"); print(products)
print("DAY 3 ORDERS"); print(orders)

# Check 1: replace the next comment with a missing-values check on customers.
# TODO
print("check 1")

print(customers.isna().sum())
# Check 2: replace the next comment with a duplicate-rows check on customers.
# TODO
print("check 2")

print(customers.duplicated().sum())
# Check 3: replace the next comment to inspect the column types of orders.
# TODO
print("check 3")

print(orders.dtypes)
