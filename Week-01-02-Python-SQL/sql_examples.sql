-- SQL Examples - Basic to Intermediate Queries
-- This file contains SQL examples for:
-- - Basic SELECT queries
-- - WHERE clauses and filtering
-- - ORDER BY and GROUP BY
-- - JOINs (INNER, LEFT, RIGHT, FULL)
-- - Aggregation functions
-- - Subqueries
-- - UNION, UNION ALL
-- - Common Table Expressions (CTEs)

-- ============================================================================
-- SETUP: CREATE SAMPLE TABLES
-- ============================================================================

-- Create employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    hire_date DATE,
    salary DECIMAL(10, 2),
    department_id INT,
    manager_id INT
);

-- Create departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50),
    budget DECIMAL(12, 2)
);

-- Create projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    department_id INT,
    status VARCHAR(20)
);

-- Create project_assignments table (Many-to-Many relationship)
CREATE TABLE project_assignments (
    assignment_id INT PRIMARY KEY,
    employee_id INT,
    project_id INT,
    hours_allocated INT,
    role VARCHAR(50),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create salaries_history table
CREATE TABLE salaries_history (
    salary_id INT PRIMARY KEY,
    employee_id INT,
    old_salary DECIMAL(10, 2),
    new_salary DECIMAL(10, 2),
    change_date DATE,
    reason VARCHAR(100),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- ============================================================================
-- INSERT SAMPLE DATA
-- ============================================================================

-- Insert departments
INSERT INTO departments VALUES
(1, 'Engineering', 'San Francisco', 500000),
(2, 'Marketing', 'New York', 300000),
(3, 'Sales', 'Chicago', 400000),
(4, 'Human Resources', 'Boston', 150000),
(5, 'Finance', 'Atlanta', 200000);

-- Insert employees
INSERT INTO employees VALUES
(101, 'John', 'Smith', 'john.smith@company.com', '555-1001', '2020-01-15', 95000, 1, NULL),
(102, 'Alice', 'Johnson', 'alice.johnson@company.com', '555-1002', '2021-03-20', 85000, 1, 101),
(103, 'Bob', 'Williams', 'bob.williams@company.com', '555-1003', '2021-06-10', 75000, 1, 101),
(104, 'Carol', 'Davis', 'carol.davis@company.com', '555-1004', '2020-05-12', 92000, 2, NULL),
(105, 'David', 'Miller', 'david.miller@company.com', '555-1005', '2022-01-18', 70000, 2, 104),
(106, 'Emma', 'Wilson', 'emma.wilson@company.com', '555-1006', '2021-09-01', 88000, 3, NULL),
(107, 'Frank', 'Moore', 'frank.moore@company.com', '555-1007', '2021-11-22', 78000, 3, 106),
(108, 'Grace', 'Taylor', 'grace.taylor@company.com', '555-1008', '2022-02-14', 65000, 4, NULL),
(109, 'Henry', 'Anderson', 'henry.anderson@company.com', '555-1009', '2020-08-30', 110000, 5, NULL);

-- Insert projects
INSERT INTO projects VALUES
(201, 'AI Platform Development', 'Build machine learning platform', '2023-01-01', '2023-12-31', 500000, 1, 'In Progress'),
(202, 'Mobile App', 'Develop iOS and Android app', '2023-03-15', '2024-03-15', 300000, 1, 'In Progress'),
(203, 'Marketing Campaign 2023', 'Annual marketing campaign', '2023-01-01', '2023-12-31', 150000, 2, 'Completed'),
(204, 'Sales Dashboard', 'Real-time sales analytics', '2023-06-01', '2023-12-31', 80000, 3, 'In Progress'),
(205, 'Cloud Migration', 'Migrate to AWS', '2023-09-01', '2024-03-01', 250000, 1, 'In Progress');

-- Insert project assignments
INSERT INTO project_assignments VALUES
(301, 101, 201, 40, 'Project Manager'),
(302, 102, 201, 35, 'Senior Engineer'),
(303, 103, 201, 30, 'Engineer'),
(304, 102, 205, 5, 'Technical Lead'),
(305, 104, 203, 20, 'Campaign Manager'),
(306, 105, 203, 15, 'Coordinator'),
(307, 106, 204, 40, 'Sales Analyst'),
(308, 107, 204, 35, 'Data Analyst');

-- Insert salary history
INSERT INTO salaries_history VALUES
(401, 101, 90000, 95000, '2023-01-15', 'Annual increase'),
(402, 102, 80000, 85000, '2023-01-15', 'Annual increase'),
(403, 104, 87000, 92000, '2023-01-15', 'Promotion'),
(404, 106, 83000, 88000, '2023-01-15', 'Annual increase');

-- ============================================================================
-- BASIC SELECT QUERIES
-- ============================================================================

-- Select all columns from employees table
-- Output: All employee records
SELECT * FROM employees;

-- Select specific columns
-- Output: Employee names and emails
SELECT first_name, last_name, email FROM employees;

-- Select with column alias
-- Output: Full name and email columns renamed
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    email AS email_address
FROM employees;

-- ============================================================================
-- WHERE CLAUSE - FILTERING DATA
-- ============================================================================

-- Filter by salary
-- Output: Employees earning more than $80,000
SELECT employee_id, first_name, last_name, salary
FROM employees
WHERE salary > 80000
ORDER BY salary DESC;

-- Filter with multiple conditions (AND)
-- Output: Engineers in Engineering department earning > $75k
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE department_id = 1 AND salary > 75000;

-- Filter with OR
-- Output: Employees from Engineering OR Marketing
SELECT first_name, last_name, department_id
FROM employees
WHERE department_id = 1 OR department_id = 2;

-- Filter with IN
-- Output: Employees in specific departments
SELECT first_name, last_name, department_id
FROM employees
WHERE department_id IN (1, 2, 3);

-- Filter with BETWEEN
-- Output: Salaries between $70k and $90k
SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 70000 AND 90000;

-- Filter with LIKE
-- Output: Employees with last name starting with 'M'
SELECT first_name, last_name
FROM employees
WHERE last_name LIKE 'M%';

-- Filter with NULL check
-- Output: Employees without a manager (managers)
SELECT employee_id, first_name, last_name
FROM employees
WHERE manager_id IS NULL;

-- ============================================================================
-- ORDER BY - SORTING RESULTS
-- ============================================================================

-- Sort ascending
-- Output: Employees sorted by salary (lowest first)
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary ASC;

-- Sort descending
-- Output: Employees sorted by salary (highest first)
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;

-- Multiple column sort
-- Output: Sorted by department, then by salary
SELECT first_name, last_name, department_id, salary
FROM employees
ORDER BY department_id ASC, salary DESC;

-- ============================================================================
-- GROUP BY AND AGGREGATION FUNCTIONS
-- ============================================================================

-- Count employees per department
-- Output: Department ID and employee count
SELECT
    department_id,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;

-- Average salary by department
-- Output: Department ID and average salary
SELECT
    d.department_name,
    COUNT(e.employee_id) AS employee_count,
    AVG(e.salary) AS average_salary,
    MIN(e.salary) AS minimum_salary,
    MAX(e.salary) AS maximum_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name
ORDER BY average_salary DESC;

-- Filter groups with HAVING
-- Output: Departments with average salary > $85k
SELECT
    d.department_name,
    COUNT(e.employee_id) AS employee_count,
    AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name
HAVING AVG(e.salary) > 85000
ORDER BY average_salary DESC;

-- Count aggregate
-- Output: Total employees
SELECT COUNT(*) AS total_employees FROM employees;

-- Count distinct
-- Output: Number of departments with employees
SELECT COUNT(DISTINCT department_id) AS departments_with_staff
FROM employees;

-- Sum and average
-- Output: Total and average salary
SELECT
    SUM(salary) AS total_payroll,
    AVG(salary) AS average_salary,
    COUNT(*) AS total_employees
FROM employees;

-- ============================================================================
-- JOINS - COMBINING TABLES
-- ============================================================================

-- INNER JOIN (most common)
-- Output: Employees with their department information
SELECT
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.last_name;

-- LEFT JOIN
-- Output: All employees and their projects (even if not assigned)
SELECT
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    p.project_name,
    pa.role,
    pa.hours_allocated
FROM employees e
LEFT JOIN project_assignments pa ON e.employee_id = pa.employee_id
LEFT JOIN projects p ON pa.project_id = p.project_id
ORDER BY e.last_name;

-- Join multiple tables
-- Output: Complete project information with department and employee details
SELECT
    p.project_name,
    d.department_name,
    e.first_name,
    e.last_name,
    pa.role,
    pa.hours_allocated
FROM projects p
INNER JOIN departments d ON p.department_id = d.department_id
LEFT JOIN project_assignments pa ON p.project_id = pa.project_id
LEFT JOIN employees e ON pa.employee_id = e.employee_id
ORDER BY p.project_name, e.last_name;

-- Self join (joining table to itself)
-- Output: Employee names with their manager names
SELECT
    CONCAT(e.first_name, ' ', e.last_name) AS employee,
    CONCAT(m.first_name, ' ', m.last_name) AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
ORDER BY manager, employee;

-- ============================================================================
-- SUBQUERIES
-- ============================================================================

-- Subquery in WHERE clause
-- Output: Employees earning above average salary
SELECT
    first_name,
    last_name,
    salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

-- Subquery with IN
-- Output: Employees working on 'AI Platform Development'
SELECT
    first_name,
    last_name,
    department_id
FROM employees
WHERE employee_id IN (
    SELECT employee_id
    FROM project_assignments
    WHERE project_id = (
        SELECT project_id
        FROM projects
        WHERE project_name = 'AI Platform Development'
    )
);

-- Correlated subquery
-- Output: Employees and their salary compared to department average
SELECT
    first_name,
    last_name,
    salary,
    (SELECT AVG(salary)
     FROM employees e2
     WHERE e2.department_id = e1.department_id) AS dept_avg_salary
FROM employees e1
ORDER BY department_id, salary DESC;

-- ============================================================================
-- UNION AND UNION ALL
-- ============================================================================

-- UNION (removes duplicates)
-- Output: Combined list of project and department locations
SELECT location FROM departments
UNION
SELECT DISTINCT location FROM (
    SELECT d.location
    FROM departments d
    JOIN projects p ON d.department_id = p.department_id
) AS sub;

-- ============================================================================
-- COMMON TABLE EXPRESSIONS (CTEs)
-- ============================================================================

-- Basic CTE
-- Output: High earners with their department info
WITH high_earners AS (
    SELECT
        employee_id,
        first_name,
        last_name,
        salary,
        department_id
    FROM employees
    WHERE salary > 80000
)
SELECT
    he.employee_id,
    he.first_name,
    he.last_name,
    he.salary,
    d.department_name
FROM high_earners he
JOIN departments d ON he.department_id = d.department_id
ORDER BY he.salary DESC;

-- Multiple CTEs
-- Output: Department stats and employee rankings
WITH dept_stats AS (
    SELECT
        department_id,
        AVG(salary) AS avg_salary,
        MAX(salary) AS max_salary,
        COUNT(*) AS emp_count
    FROM employees
    GROUP BY department_id
),
employee_data AS (
    SELECT
        e.employee_id,
        e.first_name,
        e.last_name,
        e.salary,
        e.department_id,
        RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS salary_rank
    FROM employees e
)
SELECT
    ed.first_name,
    ed.last_name,
    ed.salary,
    ds.avg_salary,
    ed.salary_rank,
    d.department_name
FROM employee_data ed
JOIN dept_stats ds ON ed.department_id = ds.department_id
JOIN departments d ON ed.department_id = d.department_id
WHERE ed.salary_rank <= 2
ORDER BY d.department_name;

-- ============================================================================
-- WINDOW FUNCTIONS (Advanced)
-- ============================================================================

-- ROW_NUMBER and RANK
-- Output: Employee salary ranking within each department
SELECT
    first_name,
    last_name,
    salary,
    department_id,
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
FROM employees
ORDER BY department_id, rank;

-- LAG and LEAD
-- Output: Compare each salary with previous hire's salary
SELECT
    first_name,
    last_name,
    hire_date,
    salary,
    LAG(salary) OVER (ORDER BY hire_date) AS previous_salary,
    LEAD(salary) OVER (ORDER BY hire_date) AS next_salary
FROM employees
ORDER BY hire_date;

-- ============================================================================
-- DATA MODIFICATION
-- ============================================================================

-- INSERT - Add new employee
INSERT INTO employees
(employee_id, first_name, last_name, email, phone, hire_date, salary, department_id, manager_id)
VALUES
(110, 'Iris', 'Jackson', 'iris.jackson@company.com', '555-1010', '2023-06-01', 72000, 2, 104);

-- UPDATE - Modify existing data
UPDATE employees
SET salary = salary * 1.05
WHERE department_id = 1;

-- UPDATE with WHERE condition
UPDATE employees
SET manager_id = 101
WHERE employee_id = 108;

-- DELETE - Remove data
DELETE FROM employees
WHERE employee_id = 110;

-- ============================================================================
-- SUMMARY AND COMMON PATTERNS
-- ============================================================================

-- Pattern 1: Get top N records
-- Output: Top 3 highest paid employees
SELECT TOP 3
    first_name,
    last_name,
    salary
FROM employees
ORDER BY salary DESC;

-- Pattern 2: Get records with no matches
-- Output: Employees not assigned to any project
SELECT DISTINCT e.employee_id, e.first_name, e.last_name
FROM employees e
LEFT JOIN project_assignments pa ON e.employee_id = pa.employee_id
WHERE pa.assignment_id IS NULL;

-- Pattern 3: Count by condition
-- Output: Count of active and inactive projects
SELECT
    status,
    COUNT(*) AS project_count,
    SUM(budget) AS total_budget
FROM projects
GROUP BY status;

-- Pattern 4: Date filtering
-- Output: Employees hired in 2021
SELECT
    first_name,
    last_name,
    hire_date
FROM employees
WHERE YEAR(hire_date) = 2021
ORDER BY hire_date;
