"""
=========================================================
E-Commerce Sales Analytics
Step 3 : Exploratory Data Analysis (EDA)
Author : Abhineet Verma
=========================================================
"""

from pathlib import Path
import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "Data" / "cleaned_sales_data.csv"
OUTPUT_FOLDER = BASE_DIR / "Outputs" / "CSV"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ==================================================
# 1. Product Analysis
# ==================================================

product_revenue = (
    df.groupby("product_category")["revenue"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

print("\nTop Product Categories")
print(product_revenue)

product_revenue.to_csv(
    OUTPUT_FOLDER / "product_revenue.csv",
    index=False
)

# ==================================================
# 2. Regional Analysis
# ==================================================

region_revenue = (
    df.groupby("region")["revenue"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

print("\nRevenue by Region")
print(region_revenue)

region_revenue.to_csv(
    OUTPUT_FOLDER / "region_revenue.csv",
    index=False
)

# ==================================================
# 3. Payment Method Analysis
# ==================================================

payment_analysis = (
    df.groupby("payment_method")["revenue"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

print("\nRevenue by Payment Method")
print(payment_analysis)

payment_analysis.to_csv(
    OUTPUT_FOLDER / "payment_analysis.csv",
    index=False
)

# ==================================================
# 4. Customer Rating Analysis
# ==================================================

rating_analysis = (
    df.groupby("product_category")["customer_rating"]
      .mean()
      .round(2)
      .sort_values(ascending=False)
      .reset_index()
)

print("\nAverage Rating by Category")
print(rating_analysis)

rating_analysis.to_csv(
    OUTPUT_FOLDER / "rating_analysis.csv",
    index=False
)

# ==================================================
# 5. Delivery Analysis
# ==================================================

delivery_analysis = (
    df.groupby("region")["delivery_days"]
      .mean()
      .round(2)
      .sort_values()
      .reset_index()
)

print("\nAverage Delivery Days")
print(delivery_analysis)

delivery_analysis.to_csv(
    OUTPUT_FOLDER / "delivery_analysis.csv",
    index=False
)

# ==================================================
# 6. Monthly Revenue
# ==================================================

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
      .sum()
      .reset_index()
)

monthly_revenue["order_date"] = monthly_revenue["order_date"].astype(str)

print("\nMonthly Revenue")
print(monthly_revenue)

monthly_revenue.to_csv(
    OUTPUT_FOLDER / "monthly_revenue.csv",
    index=False
)

# ==================================================
# 7. Top Customers
# ==================================================

top_customers = (
    df.groupby("customer_id")["revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

print("\nTop 10 Customers")
print(top_customers)

top_customers.to_csv(
    OUTPUT_FOLDER / "top_customers.csv",
    index=False
)

print("\nEDA Completed Successfully!")