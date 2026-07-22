"""
=========================================================
E-Commerce Sales Analytics
Step 4 : Data Visualization
Author : Abhineet Verma
=========================================================
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "Data" / "cleaned_sales_data.csv"

OUTPUT_FOLDER = BASE_DIR / "Outputs" / "Charts"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("DATA VISUALIZATION")
print("=" * 60)

# ==================================================
# Chart 1 - Revenue by Product Category
# ==================================================

product = df.groupby("product_category")["revenue"].sum().sort_values()

plt.figure(figsize=(10,6))
plt.bar(product.index, product.values)

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(OUTPUT_FOLDER / "01_product_revenue.png")
plt.close()

print("✓ Product Revenue Chart Saved")

# ==================================================
# Chart 2 - Revenue by Region
# ==================================================

region = df.groupby("region")["revenue"].sum()

plt.figure(figsize=(8,6))

plt.bar(region.index, region.values)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(OUTPUT_FOLDER / "02_region_revenue.png")
plt.close()

print("✓ Region Revenue Chart Saved")

# ==================================================
# Chart 3 - Payment Method Distribution
# ==================================================

payment = df.groupby("payment_method")["revenue"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    payment.values,
    labels=payment.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue by Payment Method")

plt.savefig(OUTPUT_FOLDER / "03_payment_method.png")
plt.close()

print("✓ Payment Method Chart Saved")

# ==================================================
# Chart 4 - Monthly Revenue Trend
# ==================================================

df["order_date"] = pd.to_datetime(df["order_date"])

monthly = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
    .sum()
)

monthly.index = monthly.index.astype(str)

plt.figure(figsize=(12,6))

plt.plot(monthly.index, monthly.values, marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(OUTPUT_FOLDER / "04_monthly_revenue.png")
plt.close()

print("✓ Monthly Revenue Chart Saved")

# ==================================================
# Chart 5 - Customer Rating by Product Category
# ==================================================

rating = (
    df.groupby("product_category")["customer_rating"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10,6))

plt.bar(rating.index, rating.values)

plt.title("Average Customer Rating")
plt.xlabel("Product Category")
plt.ylabel("Rating")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(OUTPUT_FOLDER / "05_customer_rating.png")
plt.close()

print("✓ Customer Rating Chart Saved")

# ==================================================
# Chart 6 - Top 10 Customers
# ==================================================

customers = (
    df.groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

plt.barh(
    customers.index.astype(str),
    customers.values
)

plt.title("Top 10 Customers")
plt.xlabel("Revenue")
plt.ylabel("Customer ID")

plt.tight_layout()

plt.savefig(OUTPUT_FOLDER / "06_top_customers.png")
plt.close()

print("✓ Top Customers Chart Saved")

print("\nAll Charts Created Successfully!")