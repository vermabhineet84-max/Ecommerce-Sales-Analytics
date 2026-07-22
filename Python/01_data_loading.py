"""
===========================================================
E-Commerce Sales Analytics
Step 1 : Data Loading
Author : Abhineet Verma
===========================================================
"""

from pathlib import Path
import pandas as pd

# -------------------------------------------------
# Locate Project Folder
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "Data" / "ecommerce_sales_analytics_5000.csv"

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

print("=" * 60)
print("LOADING DATASET")
print("=" * 60)

print(f"\nReading file:\n{DATA_FILE}")

df = pd.read_csv(DATA_FILE)

print("\nDataset Loaded Successfully!")

# -------------------------------------------------
# Basic Information
# -------------------------------------------------

print("\nDataset Shape")
print(df.shape)

print("\nFirst Five Rows")
print(df.head())

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nSummary Statistics")
print(df.describe())

print("\nDataset Information")
df.info()