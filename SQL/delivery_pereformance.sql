-- =====================================================
-- SECTION 7 : DELIVERY PERFORMANCE ANALYSIS
-- =====================================================

-- Q37. Overall Average Delivery Time

SELECT
    ROUND(AVG(delivery_days),2) AS Average_Delivery_Days
FROM sales;

----------------------------------------------------------

-- Q38. Average Delivery Time by Region

SELECT
    region,
    ROUND(AVG(delivery_days),2) AS Average_Delivery_Days
FROM sales
GROUP BY region
ORDER BY Average_Delivery_Days;

----------------------------------------------------------

-- Q39. Average Delivery Time by Product Category

SELECT
    product_category,
    ROUND(AVG(delivery_days),2) AS Average_Delivery_Days
FROM sales
GROUP BY product_category
ORDER BY Average_Delivery_Days;

----------------------------------------------------------

-- Q40. Average Delivery Time by Payment Method

SELECT
    payment_method,
    ROUND(AVG(delivery_days),2) AS Average_Delivery_Days
FROM sales
GROUP BY payment_method
ORDER BY Average_Delivery_Days;

----------------------------------------------------------

-- Q41. Customer Rating by Delivery Days

SELECT
    delivery_days,
    ROUND(AVG(customer_rating),2) AS Average_Rating,
    COUNT(*) AS Total_Orders
FROM sales
GROUP BY delivery_days
ORDER BY delivery_days;

----------------------------------------------------------

-- Q42. Revenue Generated Based on Delivery Days

SELECT
    delivery_days,
    ROUND(SUM(revenue),2) AS Total_Revenue
FROM sales
GROUP BY delivery_days
ORDER BY delivery_days;

----------------------------------------------------------

-- Q43. Orders Delivered Within 5 Days

SELECT
    COUNT(*) AS Orders_Within_5_Days
FROM sales
WHERE delivery_days <= 5;

----------------------------------------------------------

-- Q44. Orders Delivered After 5 Days

SELECT
    COUNT(*) AS Orders_After_5_Days
FROM sales
WHERE delivery_days > 5;