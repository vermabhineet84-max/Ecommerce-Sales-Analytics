-- =====================================================
-- SECTION 3 : REGIONAL SALES ANALYSIS
-- =====================================================

-- Q16. Total Revenue by Region

SELECT
    region,
    ROUND(SUM(revenue),2) AS Total_Revenue
FROM sales
GROUP BY region
ORDER BY Total_Revenue DESC;

----------------------------------------------------------

-- Q17. Total Orders by Region

SELECT
    region,
    COUNT(order_id) AS Total_Orders
FROM sales
GROUP BY region
ORDER BY Total_Orders DESC;

----------------------------------------------------------

-- Q18. Total Quantity Sold by Region

SELECT
    region,
    SUM(quantity) AS Total_Quantity
FROM sales
GROUP BY region
ORDER BY Total_Quantity DESC;

----------------------------------------------------------

-- Q19. Average Revenue per Order by Region

SELECT
    region,
    ROUND(AVG(revenue),2) AS Average_Revenue
FROM sales
GROUP BY region
ORDER BY Average_Revenue DESC;

----------------------------------------------------------

-- Q20. Average Customer Rating by Region

SELECT
    region,
    ROUND(AVG(customer_rating),2) AS Average_Rating
FROM sales
GROUP BY region
ORDER BY Average_Rating DESC;

----------------------------------------------------------

-- Q21. Average Delivery Time by Region

SELECT
    region,
    ROUND(AVG(delivery_days),2) AS Average_Delivery_Days
FROM sales
GROUP BY region
ORDER BY Average_Delivery_Days;

----------------------------------------------------------

-- Q22. Average Discount by Region

SELECT
    region,
    ROUND(AVG(discount),2) AS Average_Discount
FROM sales
GROUP BY region
ORDER BY Average_Discount DESC;

----------------------------------------------------------

-- Q23. Number of Unique Customers by Region

SELECT
    region,
    COUNT(DISTINCT customer_id) AS Unique_Customers
FROM sales
GROUP BY region
ORDER BY Unique_Customers DESC;