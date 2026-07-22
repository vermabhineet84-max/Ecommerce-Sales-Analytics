-- =====================================================
-- SECTION 5 : PAYMENT METHOD ANALYSIS
-- =====================================================

-- Q31. Number of Orders by Payment Method

SELECT
    payment_method,
    COUNT(order_id) AS Total_Orders
FROM sales
GROUP BY payment_method
ORDER BY Total_Orders DESC;

----------------------------------------------------------

-- Q32. Total Revenue by Payment Method

SELECT
    payment_method,
    ROUND(SUM(revenue),2) AS Total_Revenue
FROM sales
GROUP BY payment_method
ORDER BY Total_Revenue DESC;

----------------------------------------------------------

-- Q33. Average Revenue per Order by Payment Method

SELECT
    payment_method,
    ROUND(AVG(revenue),2) AS Average_Revenue
FROM sales
GROUP BY payment_method
ORDER BY Average_Revenue DESC;

----------------------------------------------------------

-- Q34. Average Customer Rating by Payment Method

SELECT
    payment_method,
    ROUND(AVG(customer_rating),2) AS Average_Rating
FROM sales
GROUP BY payment_method
ORDER BY Average_Rating DESC;

----------------------------------------------------------

-- Q35. Average Delivery Time by Payment Method

SELECT
    payment_method,
    ROUND(AVG(delivery_days),2) AS Average_Delivery_Days
FROM sales
GROUP BY payment_method
ORDER BY Average_Delivery_Days;

----------------------------------------------------------

-- Q36. Average Discount by Payment Method

SELECT
    payment_method,
    ROUND(AVG(discount),2) AS Average_Discount
FROM sales
GROUP BY payment_method
ORDER BY Average_Discount DESC;