"""
=========================================================
E-Commerce Sales Analytics
Step 2 : Data Cleaning
Author : Abhineet Verma
=========================================================
"""

from pathlib import Path
import pandas as pd

# -------------------------------------------------
# Locate Project Folder
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "Data" / "ecommerce_sales_analytics_5000.csv"
OUTPUT_FILE = BASE_DIR / "Data" / "cleaned_sales_data.csv"

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

print("\nDataset Loaded Successfully!")

# -------------------------------------------------
# Dataset Shape
# -------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

# -------------------------------------------------
# Missing Values
# -------------------------------------------------

print("\nMissing Values")

missing = df.isnull().sum()

print(missing)

# -------------------------------------------------
# Duplicate Rows
# -------------------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows: {duplicates}")

if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")

# -------------------------------------------------
# Convert Date Column
# -------------------------------------------------

df["order_date"] = pd.to_datetime(df["order_date"])

print("\nDate column converted successfully.")

# -------------------------------------------------
# Standardize Column Names
# -------------------------------------------------

df.columns = df.columns.str.lower()

print("Column names converted to lowercase.")

# -------------------------------------------------
# Create New Features
# -------------------------------------------------

df["final_price"] = df["unit_price"] - df["discount"]

df["revenue_per_item"] = df["revenue"] / df["quantity"]

print("New columns created successfully.")

# -------------------------------------------------
# Data Types
# -------------------------------------------------

print("\nUpdated Data Types")

print(df.dtypes)

# -------------------------------------------------
# Preview Cleaned Data
# -------------------------------------------------

print("\nFirst Five Rows")

print(df.head())

# -------------------------------------------------
# Save Clean Dataset
# -------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\nClean dataset saved!")

print(f"\nLocation:\n{OUTPUT_FILE}")

print("\nData Cleaning Completed Successfully!")