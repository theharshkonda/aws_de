# Python Fundamentals for Data Engineering

## Table of Contents
1. [Installation](#installation)
2. [Basics](#basics)
3. [Data Structures](#data-structures)
4. [NumPy & Pandas](#numpy--pandas)
5. [Projects](#projects)

## Installation

### Installing Python
```bash
# Check if Python is installed
python --version

# Windows: Download from python.org
# Mac: brew install python3
# Linux: sudo apt install python3
```

### Setting Up Virtual Environment
```bash
# Create virtual environment
python -m venv data_eng_env

# Activate (Windows)
data_eng_env\Scripts\activate

# Activate (Mac/Linux)
source data_eng_env/bin/activate

# Install packages
pip install pandas numpy jupyter matplotlib seaborn boto3
```

### VS Code Setup
1. Install VS Code
2. Install Python extension
3. Install Jupyter extension
4. Set Python interpreter

## Why Python for Data Engineering?

- **Most popular** language for data engineering
- **Rich ecosystem** of data libraries (Pandas, NumPy, PySpark)
- **AWS SDK (Boto3)** for AWS automation
- **Easy to learn** with readable syntax
- **Versatile** - ETL, data processing, automation

## Learning Path

### Week 1 Focus
- Variables, data types, operators
- Control flow (if/else, loops)
- Functions and modules
- Lists, dictionaries, tuples
- File handling (CSV, JSON)

### Data Engineering Specific Topics
- Reading/writing files
- Data transformation
- API calls
- Database connections
- Error handling
- Logging

## Key Concepts

### 1. Variables and Data Types
```python
# Integers
age = 25

# Float
price = 99.99

# String
name = "Data Engineer"

# Boolean
is_active = True

# None
data = None
```

### 2. Data Structures
```python
# List (ordered, mutable)
customers = ["Alice", "Bob", "Charlie"]

# Tuple (ordered, immutable)
coordinates = (10.5, 20.3)

# Dictionary (key-value pairs)
customer = {
    "name": "Alice",
    "age": 30,
    "orders": 5
}

# Set (unordered, unique)
unique_ids = {1, 2, 3, 4, 5}
```

### 3. Control Flow
```python
# If-Else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# For Loop
for customer in customers:
    print(f"Processing {customer}")

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1
```

### 4. Functions
```python
def calculate_total(items, tax_rate=0.1):
    """Calculate total price with tax"""
    subtotal = sum(items)
    tax = subtotal * tax_rate
    return subtotal + tax

# Usage
prices = [10, 20, 30]
total = calculate_total(prices)
```

### 5. File Handling
```python
# Reading CSV
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Writing JSON
import json

data = {"name": "Alice", "age": 30}
with open('output.json', 'w') as file:
    json.dump(data, file, indent=2)
```

## Practice Exercises

### Exercise 1: Data Type Conversion
```python
# Convert and validate data types
price_str = "99.99"
quantity_str = "5"

# Your task: Calculate total
# Expected output: 499.95
```

### Exercise 2: List Processing
```python
# Given a list of sales
sales = [100, 250, 175, 300, 425]

# Tasks:
# 1. Calculate total sales
# 2. Find average
# 3. Find max and min
# 4. Filter sales > 200
```

### Exercise 3: Dictionary Manipulation
```python
# Customer data
customer = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "orders": []
}

# Tasks:
# 1. Add new order
# 2. Update email
# 3. Check if key exists
# 4. Print all keys
```

### Exercise 4: File Processing
```python
# Read a CSV file and:
# 1. Count total rows
# 2. Calculate sum of a column
# 3. Filter rows based on condition
# 4. Write results to new file
```

## Common Patterns for Data Engineering

### Pattern 1: Reading Multiple Files
```python
import os
import pandas as pd

def read_all_csv_files(directory):
    """Read all CSV files from a directory"""
    all_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            all_data.append(df)
    return pd.concat(all_data, ignore_index=True)
```

### Pattern 2: Data Validation
```python
def validate_data(data):
    """Validate data before processing"""
    if not data:
        raise ValueError("Data is empty")

    required_fields = ['id', 'name', 'value']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    return True
```

### Pattern 3: Error Handling
```python
import logging

logging.basicConfig(level=logging.INFO)

def process_data(filename):
    """Process data with error handling"""
    try:
        with open(filename, 'r') as file:
            data = file.read()
            # Process data
            logging.info(f"Successfully processed {filename}")
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
    except Exception as e:
        logging.error(f"Error processing {filename}: {e}")
```

## Interview Questions

### Basic Questions
1. What are mutable and immutable data types?
2. Explain list vs tuple vs set vs dictionary
3. What is list comprehension?
4. How do you handle exceptions in Python?
5. What is the difference between `==` and `is`?

### Data Engineering Questions
1. How do you read a large CSV file efficiently?
2. How to handle missing data in Python?
3. Explain generators and when to use them
4. How to optimize Python code for large datasets?
5. What is the Global Interpreter Lock (GIL)?

## Resources

### Tutorials
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com)
- [W3Schools Python](https://www.w3schools.com/python/)

### Practice
- [LeetCode Python](https://leetcode.com/problemset/)
- [HackerRank Python](https://www.hackerrank.com/domains/python)
- [Codewars](https://www.codewars.com)

### Books
- "Python Crash Course" by Eric Matthes
- "Automate the Boring Stuff with Python" by Al Sweigart

## Next Steps
- Complete exercises in `01-Basics/`
- Practice data structures in `02-Data-Structures/`
- Move to NumPy & Pandas in `03-NumPy-Pandas/`
- Build projects in `04-Projects/`

---

**Tip**: Code every day, even if it's just 30 minutes!
