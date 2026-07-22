-- =====================================================
-- SECTION 4 : CUSTOMER ANALYSIS
-- =====================================================

-- Q24. Top 10 Customers by Total Revenue

SELECT
    customer_id,
    ROUND(SUM(revenue),2) AS Total_Spent
FROM sales
GROUP BY customer_id
ORDER BY Total_Spent DESC
LIMIT 10;

----------------------------------------------------------

-- Q25. Top 10 Customers by Number of Orders

SELECT
    customer_id,
    COUNT(order_id) AS Total_Orders
FROM sales
GROUP BY customer_id
ORDER BY Total_Orders DESC
LIMIT 10;

----------------------------------------------------------

-- Q26. Average Spending Per Customer

SELECT
    customer_id,
    ROUND(AVG(revenue),2) AS Average_Spending
FROM sales
GROUP BY customer_id
ORDER BY Average_Spending DESC;

----------------------------------------------------------

-- Q27. Total Quantity Purchased by Each Customer

SELECT
    customer_id,
    SUM(quantity) AS Total_Items
FROM sales
GROUP BY customer_id
ORDER BY Total_Items DESC;

----------------------------------------------------------

-- Q28. Highest Single Order by Customer

SELECT
    customer_id,
    MAX(revenue) AS Highest_Order
FROM sales
GROUP BY customer_id
ORDER BY Highest_Order DESC;

----------------------------------------------------------

-- Q29. Customer Rating Given by Customers

SELECT
    customer_id,
    ROUND(AVG(customer_rating),2) AS Average_Rating
FROM sales
GROUP BY customer_id
ORDER BY Average_Rating DESC;

----------------------------------------------------------

-- Q30. Customers Who Have Placed More Than 5 Orders

SELECT
    customer_id,
    COUNT(order_id) AS Total_Orders
FROM sales
GROUP BY customer_id
HAVING COUNT(order_id) > 5
ORDER BY Total_Orders DESC;