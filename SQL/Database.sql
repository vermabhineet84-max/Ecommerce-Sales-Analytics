CREATE DATABASE ecommerce_analysis;

USE ecommerce_analysis;

CREATE TABLE orders (

order_id INT PRIMARY KEY,

order_date DATE,

customer_id INT,

product_category VARCHAR(50),

region VARCHAR(50),

quantity INT,

unit_price DECIMAL(10,2),

discount DECIMAL(5,2),

payment_method VARCHAR(30),

delivery_days INT,

customer_rating DECIMAL(2,1),

revenue DECIMAL(10,2)

);
