-- ============================================
-- SQL BASICS FOR DATA ENGINEERING
-- ============================================

/*
This file contains essential SQL queries for data engineering.
Practice each section and try to write your own variations.

Database: MySQL/PostgreSQL
Setup: Run the CREATE TABLE statements first
*/

-- ============================================
-- 1. CREATE DATABASE AND TABLES
-- ============================================

-- Create database
CREATE DATABASE IF NOT EXISTS data_engineering_practice;
USE data_engineering_practice;

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    signup_date DATE,
    is_active BOOLEAN DEFAULT TRUE
);

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2),
    stock_quantity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create order_items table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- ============================================
-- 2. INSERT SAMPLE DATA
-- ============================================

-- Insert customers
INSERT INTO customers (first_name, last_name, email, city, state, country, signup_date)
VALUES
('Alice', 'Johnson', 'alice@example.com', 'Seattle', 'WA', 'USA', '2024-01-15'),
('Bob', 'Smith', 'bob@example.com', 'Portland', 'OR', 'USA', '2024-01-20'),
('Charlie', 'Brown', 'charlie@example.com', 'San Francisco', 'CA', 'USA', '2024-02-01'),
('Diana', 'Davis', 'diana@example.com', 'Austin', 'TX', 'USA', '2024-02-10'),
('Eve', 'Wilson', 'eve@example.com', 'Boston', 'MA', 'USA', '2024-02-15');

-- Insert products
INSERT INTO products (product_name, category, price, stock_quantity)
VALUES
('Laptop', 'Electronics', 1200.00, 50),
('Mouse', 'Electronics', 25.00, 200),
('Keyboard', 'Electronics', 75.00, 150),
('Monitor', 'Electronics', 300.00, 75),
('Desk Chair', 'Furniture', 250.00, 100),
('Desk', 'Furniture', 400.00, 50),
('Notebook', 'Stationery', 5.00, 500),
('Pen Set', 'Stationery', 15.00, 300);

-- Insert orders
INSERT INTO orders (customer_id, order_date, total_amount, status)
VALUES
(1, '2024-02-20', 1275.00, 'completed'),
(2, '2024-02-22', 325.00, 'completed'),
(1, '2024-02-25', 100.00, 'pending'),
(3, '2024-03-01', 1500.00, 'completed'),
(4, '2024-03-05', 675.00, 'shipped');

-- Insert order items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
(1, 1, 1, 1200.00),
(1, 2, 3, 25.00),
(2, 4, 1, 300.00),
(2, 2, 1, 25.00),
(3, 3, 1, 75.00),
(3, 2, 1, 25.00),
(4, 1, 1, 1200.00),
(4, 4, 1, 300.00),
(5, 5, 2, 250.00),
(5, 6, 1, 400.00);


-- ============================================
-- 3. SELECT QUERIES
-- ============================================

-- Select all columns
SELECT * FROM customers;

-- Select specific columns
SELECT first_name, last_name, email FROM customers;

-- Select with alias
SELECT
    first_name AS "First Name",
    last_name AS "Last Name",
    email AS "Email Address"
FROM customers;

-- Select distinct values
SELECT DISTINCT city FROM customers;
SELECT DISTINCT category FROM products;


-- ============================================
-- 4. WHERE CLAUSE
-- ============================================

-- Filter by condition
SELECT * FROM products WHERE price > 100;

-- Multiple conditions (AND)
SELECT * FROM products
WHERE category = 'Electronics' AND price < 500;

-- Multiple conditions (OR)
SELECT * FROM customers
WHERE city = 'Seattle' OR city = 'Portland';

-- IN operator
SELECT * FROM customers
WHERE state IN ('WA', 'OR', 'CA');

-- BETWEEN operator
SELECT * FROM products
WHERE price BETWEEN 50 AND 300;

-- LIKE operator (pattern matching)
SELECT * FROM customers
WHERE email LIKE '%@example.com';

SELECT * FROM products
WHERE product_name LIKE 'M%';

-- IS NULL / IS NOT NULL
SELECT * FROM customers
WHERE email IS NOT NULL;


-- ============================================
-- 5. ORDER BY
-- ============================================

-- Sort ascending
SELECT * FROM products
ORDER BY price ASC;

-- Sort descending
SELECT * FROM products
ORDER BY price DESC;

-- Multiple column sort
SELECT * FROM customers
ORDER BY state ASC, city ASC;


-- ============================================
-- 6. LIMIT and OFFSET
-- ============================================

-- Get first 3 records
SELECT * FROM products
ORDER BY price DESC
LIMIT 3;

-- Pagination (skip 2, take 3)
SELECT * FROM products
ORDER BY product_id
LIMIT 3 OFFSET 2;


-- ============================================
-- 7. AGGREGATE FUNCTIONS
-- ============================================

-- COUNT
SELECT COUNT(*) AS total_customers FROM customers;
SELECT COUNT(DISTINCT city) AS unique_cities FROM customers;

-- SUM
SELECT SUM(total_amount) AS total_revenue FROM orders;

-- AVG
SELECT AVG(price) AS average_price FROM products;

-- MIN and MAX
SELECT
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM products;

-- Multiple aggregates
SELECT
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS average_order_value,
    MIN(total_amount) AS min_order,
    MAX(total_amount) AS max_order
FROM orders;


-- ============================================
-- 8. GROUP BY
-- ============================================

-- Group by single column
SELECT
    category,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price
FROM products
GROUP BY category;

-- Group by multiple columns
SELECT
    state,
    city,
    COUNT(*) AS customer_count
FROM customers
GROUP BY state, city;

-- Group by with ORDER BY
SELECT
    category,
    SUM(stock_quantity) AS total_stock
FROM products
GROUP BY category
ORDER BY total_stock DESC;


-- ============================================
-- 9. HAVING CLAUSE
-- ============================================

-- Filter grouped results
SELECT
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category
HAVING COUNT(*) > 2;

-- Having with multiple conditions
SELECT
    category,
    AVG(price) AS avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 100
ORDER BY avg_price DESC;


-- ============================================
-- 10. JOINS
-- ============================================

-- INNER JOIN
SELECT
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date,
    o.total_amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;

-- LEFT JOIN (all customers, even without orders)
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- Multiple JOINs
SELECT
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date,
    p.product_name,
    oi.quantity,
    oi.unit_price
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id;


-- ============================================
-- 11. UPDATE
-- ============================================

-- Update single record
UPDATE products
SET price = 1300.00
WHERE product_id = 1;

-- Update multiple records
UPDATE products
SET stock_quantity = stock_quantity - 10
WHERE category = 'Electronics';

-- Update with condition
UPDATE customers
SET is_active = FALSE
WHERE signup_date < '2024-02-01';


-- ============================================
-- 12. DELETE
-- ============================================

-- Delete specific records
DELETE FROM customers
WHERE customer_id = 999;

-- Delete with condition
DELETE FROM products
WHERE stock_quantity = 0;

-- Delete all records (use with caution!)
-- DELETE FROM table_name;


-- ============================================
-- 13. PRACTICE EXERCISES
-- ============================================

/*
EXERCISE 1: Basic Queries
1. Find all products in the 'Electronics' category
2. Find customers from California (CA)
3. Find orders with total_amount greater than $500
4. Find products with price between $20 and $100
*/

/*
EXERCISE 2: Aggregations
1. Count total number of orders
2. Calculate total revenue from all orders
3. Find average product price by category
4. Find the most expensive product in each category
*/

/*
EXERCISE 3: Joins
1. List all orders with customer names
2. Find total amount spent by each customer
3. List all products ordered with their quantities
4. Find customers who haven't placed any orders
*/

/*
EXERCISE 4: Complex Queries
1. Find top 3 customers by total spending
2. Find products that have never been ordered
3. Calculate average order value by customer
4. Find categories with total stock value > $10,000
*/


-- ============================================
-- 14. DATA ENGINEERING PATTERNS
-- ============================================

-- Pattern 1: Data Quality Check
SELECT
    'customers' AS table_name,
    COUNT(*) AS total_records,
    COUNT(DISTINCT email) AS unique_emails,
    COUNT(*) - COUNT(email) AS null_emails
FROM customers;

-- Pattern 2: Duplicate Detection
SELECT
    email,
    COUNT(*) AS occurrence
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;

-- Pattern 3: Date Range Analysis
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    COUNT(*) AS order_count,
    SUM(total_amount) AS monthly_revenue
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;

-- Pattern 4: Running Total
SELECT
    order_date,
    total_amount,
    SUM(total_amount) OVER (ORDER BY order_date) AS running_total
FROM orders;


-- ============================================
-- INTERVIEW TIPS
-- ============================================

/*
COMMON SQL INTERVIEW QUESTIONS:

1. Explain the difference between WHERE and HAVING
   - WHERE: Filters rows before grouping
   - HAVING: Filters groups after aggregation

2. What are the types of JOINs?
   - INNER JOIN: Matching records from both tables
   - LEFT JOIN: All from left + matching from right
   - RIGHT JOIN: All from right + matching from left
   - FULL OUTER JOIN: All records from both tables

3. What is the difference between DELETE and TRUNCATE?
   - DELETE: Can use WHERE, slower, can rollback
   - TRUNCATE: Removes all rows, faster, can't rollback

4. Explain PRIMARY KEY vs FOREIGN KEY
   - PRIMARY KEY: Unique identifier for table
   - FOREIGN KEY: References PRIMARY KEY in another table

5. What are indexes and why use them?
   - Speed up data retrieval
   - Trade-off: Slower INSERT/UPDATE/DELETE
*/

-- ============================================
-- NEXT STEPS
-- ============================================

/*
1. Practice all queries above
2. Try to write variations
3. Move to advanced SQL (subqueries, CTEs, window functions)
4. Solve problems on LeetCode/HackerRank
5. Build a project using SQL
*/
