/*
=========================================================
E-Commerce Sales Analytics
SQL Business Analysis
Author: Abhineet Verma
=========================================================
*/

-- =====================================================
-- SECTION 1 : BUSINESS KPIs
-- =====================================================

-- Q1. Total Number of Orders

SELECT COUNT(order_id) AS Total_Orders
FROM sales;

----------------------------------------------------------

-- Q2. Total Revenue Generated

SELECT
ROUND(SUM(revenue),2) AS Total_Revenue
FROM sales;

----------------------------------------------------------

-- Q3. Average Revenue Per Order

SELECT
ROUND(AVG(revenue),2) AS Average_Revenue
FROM sales;

----------------------------------------------------------

-- Q4. Total Quantity Sold

SELECT
SUM(quantity) AS Total_Items_Sold
FROM sales;

----------------------------------------------------------

-- Q5. Average Customer Rating

SELECT
ROUND(AVG(customer_rating),2) AS Average_Customer_Rating
FROM sales;

----------------------------------------------------------

-- Q6. Average Delivery Time

SELECT
ROUND(AVG(delivery_days),2) AS Average_Delivery_Days
FROM sales;

----------------------------------------------------------

-- Q7. Total Number of Customers

SELECT
COUNT(DISTINCT customer_id) AS Total_Customers
FROM sales;

----------------------------------------------------------

-- Q8. Total Discount Given

SELECT
ROUND(SUM(discount),2) AS Total_Discount
FROM sales;