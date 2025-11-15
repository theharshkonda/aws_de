# SQL Interview Questions for Data Engineers

## Difficulty Levels
- ⭐ Easy
- ⭐⭐ Medium
- ⭐⭐⭐ Hard

---

## Section 1: Basic SELECT Questions (⭐)

### Q1: Select all customers from California
```sql
-- Given table: customers (id, name, state, email)

-- Your Answer:
SELECT * FROM customers WHERE state = 'CA';
```

### Q2: Count total number of orders
```sql
-- Given table: orders (order_id, customer_id, amount, date)

-- Your Answer:
SELECT COUNT(*) AS total_orders FROM orders;
```

### Q3: Find average order amount
```sql
SELECT AVG(amount) AS avg_order_amount FROM orders;
```

### Q4: List unique product categories
```sql
-- Given table: products (id, name, category, price)

SELECT DISTINCT category FROM products;
```

### Q5: Find products priced between $50 and $100
```sql
SELECT * FROM products
WHERE price BETWEEN 50 AND 100;
```

---

## Section 2: JOIN Questions (⭐⭐)

### Q6: List customers with their orders
```sql
-- Tables: customers (id, name), orders (order_id, customer_id, amount)

SELECT
    c.id,
    c.name,
    o.order_id,
    o.amount
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id;
```

### Q7: Find customers who haven't placed any orders
```sql
SELECT
    c.id,
    c.name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.order_id IS NULL;
```

### Q8: List products with their category names
```sql
-- Tables: products (id, name, category_id), categories (id, category_name)

SELECT
    p.name AS product_name,
    c.category_name
FROM products p
INNER JOIN categories c ON p.category_id = c.id;
```

### Q9: Join three tables: customers, orders, products
```sql
-- Get customer name, order date, product name

SELECT
    c.name AS customer_name,
    o.order_date,
    p.name AS product_name
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id;
```

### Q10: Self JOIN - Find employees and their managers
```sql
-- Table: employees (id, name, manager_id)

SELECT
    e.name AS employee_name,
    m.name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## Section 3: GROUP BY and Aggregations (⭐⭐)

### Q11: Count orders by customer
```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id;
```

### Q12: Total revenue by product category
```sql
SELECT
    p.category,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products p
INNER JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
```

### Q13: Find customers with more than 5 orders
```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 5;
```

### Q14: Average order value by month
```sql
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    AVG(amount) AS avg_order_value
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;
```

### Q15: Top 5 products by sales
```sql
SELECT
    p.name,
    SUM(oi.quantity) AS total_sold
FROM products p
INNER JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name
ORDER BY total_sold DESC
LIMIT 5;
```

---

## Section 4: Subqueries (⭐⭐)

### Q16: Find products more expensive than average
```sql
SELECT *
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

### Q17: Find customers who ordered product 'Laptop'
```sql
SELECT DISTINCT c.name
FROM customers c
WHERE c.id IN (
    SELECT o.customer_id
    FROM orders o
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE p.name = 'Laptop'
);
```

### Q18: Find departments with above-average salaries
```sql
-- Tables: employees (id, name, department_id, salary)

SELECT
    department_id,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
```

### Q19: Second highest salary
```sql
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Or using LIMIT:
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

### Q20: Correlated subquery - Employees earning more than dept average
```sql
SELECT e1.name, e1.salary, e1.department_id
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```

---

## Section 5: Window Functions (⭐⭐⭐)

### Q21: Rank employees by salary
```sql
SELECT
    name,
    department_id,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;
```

### Q22: Rank employees within each department
```sql
SELECT
    name,
    department_id,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q23: Running total of sales
```sql
SELECT
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

### Q24: Find previous and next order amounts
```sql
SELECT
    order_id,
    amount,
    LAG(amount) OVER (ORDER BY order_date) AS previous_amount,
    LEAD(amount) OVER (ORDER BY order_date) AS next_amount
FROM orders;
```

### Q25: ROW_NUMBER vs RANK vs DENSE_RANK
```sql
SELECT
    name,
    score,
    ROW_NUMBER() OVER (ORDER BY score DESC) AS row_num,
    RANK() OVER (ORDER BY score DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rank
FROM students;

-- Difference:
-- ROW_NUMBER: 1, 2, 3, 4, 5 (always sequential)
-- RANK: 1, 2, 2, 4, 5 (skips numbers after tie)
-- DENSE_RANK: 1, 2, 2, 3, 4 (no gaps)
```

### Q26: Moving average
```sql
SELECT
    order_date,
    amount,
    AVG(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3
FROM orders;
```

### Q27: First and last value in group
```sql
SELECT
    customer_id,
    order_date,
    amount,
    FIRST_VALUE(amount) OVER (
        PARTITION BY customer_id ORDER BY order_date
    ) AS first_order_amount,
    LAST_VALUE(amount) OVER (
        PARTITION BY customer_id ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_order_amount
FROM orders;
```

---

## Section 6: CTEs (Common Table Expressions) (⭐⭐)

### Q28: Simple CTE
```sql
WITH high_value_customers AS (
    SELECT
        customer_id,
        SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer_id
    HAVING SUM(amount) > 1000
)
SELECT
    c.name,
    hvc.total_spent
FROM high_value_customers hvc
INNER JOIN customers c ON hvc.customer_id = c.id;
```

### Q29: Multiple CTEs
```sql
WITH
customer_totals AS (
    SELECT
        customer_id,
        SUM(amount) AS total_spent,
        COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
),
avg_spend AS (
    SELECT AVG(total_spent) AS avg_customer_spend
    FROM customer_totals
)
SELECT
    c.name,
    ct.total_spent,
    ct.order_count
FROM customer_totals ct
INNER JOIN customers c ON ct.customer_id = c.id
CROSS JOIN avg_spend a
WHERE ct.total_spent > a.avg_customer_spend;
```

### Q30: Recursive CTE - Organization hierarchy
```sql
WITH RECURSIVE employee_hierarchy AS (
    -- Base case: Top-level employees (no manager)
    SELECT
        id,
        name,
        manager_id,
        1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive case
    SELECT
        e.id,
        e.name,
        e.manager_id,
        eh.level + 1
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy
ORDER BY level, name;
```

---

## Section 7: Data Manipulation (⭐⭐)

### Q31: Insert multiple rows
```sql
INSERT INTO customers (name, email, city)
VALUES
    ('Alice', 'alice@example.com', 'Seattle'),
    ('Bob', 'bob@example.com', 'Portland'),
    ('Charlie', 'charlie@example.com', 'Austin');
```

### Q32: Update with JOIN
```sql
-- Increase price by 10% for products in 'Electronics' category

UPDATE products p
INNER JOIN categories c ON p.category_id = c.id
SET p.price = p.price * 1.10
WHERE c.name = 'Electronics';
```

### Q33: Delete duplicates (keep one)
```sql
-- Keep row with smallest id for each duplicate email

DELETE c1
FROM customers c1
INNER JOIN customers c2
WHERE c1.email = c2.email
AND c1.id > c2.id;
```

### Q34: Upsert (INSERT ... ON DUPLICATE KEY UPDATE)
```sql
INSERT INTO product_inventory (product_id, quantity)
VALUES (1, 100)
ON DUPLICATE KEY UPDATE quantity = quantity + 100;
```

---

## Section 8: Advanced Queries (⭐⭐⭐)

### Q35: Find duplicates
```sql
SELECT
    email,
    COUNT(*) AS occurrence
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;
```

### Q36: Pivot table (transform rows to columns)
```sql
-- Without PIVOT function (MySQL)
SELECT
    product_id,
    SUM(CASE WHEN MONTH(order_date) = 1 THEN quantity ELSE 0 END) AS Jan,
    SUM(CASE WHEN MONTH(order_date) = 2 THEN quantity ELSE 0 END) AS Feb,
    SUM(CASE WHEN MONTH(order_date) = 3 THEN quantity ELSE 0 END) AS Mar
FROM order_items oi
INNER JOIN orders o ON oi.order_id = o.order_id
GROUP BY product_id;
```

### Q37: Unpivot (transform columns to rows)
```sql
-- Transform sales_2023, sales_2024 columns to rows

SELECT id, 'sales_2023' AS year, sales_2023 AS amount FROM sales
UNION ALL
SELECT id, 'sales_2024' AS year, sales_2024 AS amount FROM sales;
```

### Q38: Gap and Islands problem
```sql
-- Find consecutive date ranges in bookings

WITH ranked_dates AS (
    SELECT
        booking_date,
        ROW_NUMBER() OVER (ORDER BY booking_date) AS rn,
        DATE_SUB(booking_date, INTERVAL ROW_NUMBER() OVER (ORDER BY booking_date) DAY) AS grp
    FROM bookings
)
SELECT
    MIN(booking_date) AS start_date,
    MAX(booking_date) AS end_date,
    COUNT(*) AS consecutive_days
FROM ranked_dates
GROUP BY grp;
```

### Q39: Median calculation
```sql
-- MySQL doesn't have built-in MEDIAN, need to calculate

WITH ordered_values AS (
    SELECT
        salary,
        ROW_NUMBER() OVER (ORDER BY salary) AS row_num,
        COUNT(*) OVER () AS total_count
    FROM employees
)
SELECT AVG(salary) AS median_salary
FROM ordered_values
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
```

### Q40: Cumulative percentage
```sql
SELECT
    product_id,
    sales,
    SUM(sales) OVER (ORDER BY sales DESC) AS cumulative_sales,
    100.0 * SUM(sales) OVER (ORDER BY sales DESC) / SUM(sales) OVER () AS cumulative_percent
FROM product_sales;
```

---

## Section 9: Query Optimization (⭐⭐⭐)

### Q41: Index optimization
```sql
-- Before: Slow query
SELECT * FROM orders WHERE customer_id = 123;

-- Create index
CREATE INDEX idx_customer_id ON orders(customer_id);

-- After: Fast query (uses index)
```

### Q42: Avoid SELECT *
```sql
-- Bad
SELECT * FROM orders;

-- Good (only select needed columns)
SELECT order_id, customer_id, amount FROM orders;
```

### Q43: Use EXISTS instead of IN for large datasets
```sql
-- Slower
SELECT * FROM customers
WHERE id IN (SELECT customer_id FROM orders);

-- Faster
SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

### Q44: LIMIT with large OFFSET is slow
```sql
-- Slow for large offset
SELECT * FROM orders ORDER BY order_id LIMIT 10 OFFSET 100000;

-- Better: Use indexed column
SELECT * FROM orders
WHERE order_id > 100000
ORDER BY order_id
LIMIT 10;
```

### Q45: EXPLAIN query plan
```sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 123;

-- Look for:
-- - Type: ALL (bad), ref/eq_ref (good)
-- - Key: Index being used
-- - Rows: Number of rows scanned
```

---

## Section 10: Data Quality & Validation (⭐⭐)

### Q46: Find NULL values
```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT(email) AS rows_with_email,
    COUNT(*) - COUNT(email) AS null_emails
FROM customers;
```

### Q47: Data type validation
```sql
-- Find invalid emails (basic check)
SELECT *
FROM customers
WHERE email NOT LIKE '%_@__%.__%';
```

### Q48: Outlier detection
```sql
-- Find salaries more than 3 standard deviations from mean

WITH stats AS (
    SELECT
        AVG(salary) AS mean_salary,
        STDDEV(salary) AS stddev_salary
    FROM employees
)
SELECT e.*
FROM employees e, stats s
WHERE ABS(e.salary - s.mean_salary) > 3 * s.stddev_salary;
```

### Q49: Referential integrity check
```sql
-- Find orders with invalid customer_id

SELECT o.*
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
WHERE c.id IS NULL;
```

### Q50: Date range validation
```sql
-- Find invalid date ranges (end_date before start_date)

SELECT *
FROM projects
WHERE end_date < start_date;
```

---

## Common Interview Patterns

### Pattern 1: Top N per Group
```sql
-- Top 3 employees by salary in each department

WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rn
    FROM employees
)
SELECT * FROM ranked WHERE rn <= 3;
```

### Pattern 2: Running Calculations
```sql
-- Running total, running average

SELECT
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) AS running_total,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7day
FROM sales;
```

### Pattern 3: Data Deduplication
```sql
-- Remove duplicates keeping first occurrence

DELETE FROM customers
WHERE id NOT IN (
    SELECT MIN(id)
    FROM customers
    GROUP BY email
);
```

---

## Interview Tips

### Before Writing Query
1. ✅ Understand the table schema
2. ✅ Clarify expected output
3. ✅ Ask about edge cases
4. ✅ Think about NULL values

### While Writing Query
1. ✅ Start with simple SELECT
2. ✅ Add JOINs one at a time
3. ✅ Test each step
4. ✅ Use meaningful aliases

### After Writing Query
1. ✅ Check for NULL handling
2. ✅ Verify aggregations
3. ✅ Test with edge cases
4. ✅ Discuss optimization

### Common Mistakes
- ❌ Forgetting GROUP BY columns
- ❌ Not handling NULLs
- ❌ Using WHERE instead of HAVING
- ❌ Ambiguous column names in JOINs
- ❌ Forgetting ORDER BY with LIMIT

---

## Practice Resources

1. **LeetCode Database**: 200+ SQL problems
2. **HackerRank SQL**: Easy to Hard
3. **StrataScratch**: Real interview questions
4. **DataLemur**: Data science SQL
5. **SQLZoo**: Interactive tutorials

---

## Next Steps

- [ ] Solve 10 easy questions
- [ ] Solve 20 medium questions
- [ ] Solve 10 hard questions
- [ ] Practice window functions
- [ ] Master CTEs
- [ ] Optimize slow queries

**Goal**: Solve 5 SQL questions daily for 20 days = 100 questions!
