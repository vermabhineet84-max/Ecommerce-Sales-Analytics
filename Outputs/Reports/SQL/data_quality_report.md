# Data Quality Report

## Project
**E-Commerce Sales Analytics using SQL & Python**

---

# Data Inspection Summary

The dataset was inspected using SQL after importing it into MySQL. Multiple quality checks were performed to ensure that the data was complete, consistent, and ready for analysis.

---

## Dataset Information

| Attribute | Value |
|-----------|--------|
| Table Name | sales |
| Total Records | 5,000 |
| Total Columns | 12 |
| Inspection Tool | MySQL Workbench |

---

# Columns

| Column Name | Data Type |
|--------------|-----------|
| order_id | Integer |
| order_date | Date |
| customer_id | Integer |
| product_category | Text |
| region | Text |
| quantity | Integer |
| unit_price | Decimal |
| discount | Decimal |
| payment_method | Text |
| delivery_days | Integer |
| customer_rating | Integer |
| revenue | Decimal |

---

# Missing Value Analysis

The dataset was checked for NULL values using SQL.

### Query Used

```sql
SELECT
SUM(order_id IS NULL),
SUM(order_date IS NULL),
SUM(customer_id IS NULL),
SUM(product_category IS NULL),
SUM(region IS NULL),
SUM(quantity IS NULL),
SUM(unit_price IS NULL),
SUM(discount IS NULL),
SUM(payment_method IS NULL),
SUM(delivery_days IS NULL),
SUM(customer_rating IS NULL),
SUM(revenue IS NULL)
FROM sales;
```

### Result

✅ No NULL values were found in any column.

| Status | Result |
|---------|---------|
| Missing Values | 0 |

---

# Duplicate Record Analysis

Duplicate Order IDs were checked using:

```sql
SELECT order_id,
COUNT(*)
FROM sales
GROUP BY order_id
HAVING COUNT(*) > 1;
```

### Result

✅ No duplicate Order IDs were found.

---

# Product Categories

Unique Categories

- Beauty
- Clothing
- Electronics
- Home

Total Categories: **4**

---

# Regions

The dataset contains sales from four regions.

- North
- South
- East
- West

Total Regions: **4**

---

# Payment Methods

The dataset contains three payment methods.

- Card
- Wallet
- COD

Total Payment Methods: **3**

---

# Customer Ratings

| Metric | Value |
|---------|--------|
| Lowest Rating | 1 |
| Highest Rating | 5 |

---

# Revenue Statistics

| Metric | Value |
|---------|--------|
| Minimum Revenue | 11.21 |
| Maximum Revenue | 4119.33 |
| Average Revenue | 1021.96 |

---

# Data Quality Assessment

| Check | Status |
|---------|---------|
| Missing Values | ✅ Passed |
| Duplicate Records | ✅ Passed |
| Invalid Ratings | ✅ Passed |
| Revenue Values | ✅ Passed |
| Product Categories | ✅ Valid |
| Regions | ✅ Valid |
| Payment Methods | ✅ Valid |

---

# Conclusion

The dataset successfully passed all preliminary data quality checks.

Key observations:

- Dataset contains **5,000** transaction records.
- No missing values were detected.
- No duplicate Order IDs were found.
- Revenue values appear consistent.
- Customer ratings are within the expected range (1–5).
- Product categories, regions, and payment methods contain valid values.
- The dataset is clean and suitable for exploratory data analysis (EDA), SQL querying, visualization, and business intelligence reporting.

**Dataset Status:** ✅ Ready for Analysis