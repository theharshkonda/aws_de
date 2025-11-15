"""
Python Basics for Data Engineering
Complete this file with practice exercises
"""

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================

# Integer
age = 25
employee_count = 100

# Float
price = 99.99
tax_rate = 0.15

# String
name = "Data Engineer"
company = "AWS"

# Boolean
is_active = True
has_access = False

# None
data = None

# Print examples
print("=" * 50)
print("VARIABLES AND DATA TYPES")
print("=" * 50)
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Price: {price}, Type: {type(price)}")
print(f"Is Active: {is_active}, Type: {type(is_active)}")


# ============================================
# 2. OPERATORS
# ============================================

print("\n" + "=" * 50)
print("OPERATORS")
print("=" * 50)

# Arithmetic Operators
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# Comparison Operators
print(f"\n{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# Logical Operators
x = True
y = False
print(f"\nTrue and False: {x and y}")
print(f"True or False: {x or y}")
print(f"not True: {not x}")


# ============================================
# 3. STRING OPERATIONS
# ============================================

print("\n" + "=" * 50)
print("STRING OPERATIONS")
print("=" * 50)

# String manipulation
text = "  aws data engineer  "
print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Title: '{text.title()}'")
print(f"Strip: '{text.strip()}'")
print(f"Replace: '{text.replace('aws', 'AWS')}'")

# String formatting
name = "Alice"
role = "Data Engineer"
salary = 120000

# F-strings (Python 3.6+)
print(f"\n{name} is a {role} with salary ${salary:,}")

# Format method
print("{} is a {} with salary ${}".format(name, role, salary))


# ============================================
# 4. CONTROL FLOW - IF/ELSE
# ============================================

print("\n" + "=" * 50)
print("CONTROL FLOW - IF/ELSE")
print("=" * 50)

# Basic if-else
temperature = 25

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm!")
elif temperature > 10:
    print("It's cool!")
else:
    print("It's cold!")

# Data validation example
data_size = 150

if data_size > 100:
    print("Large dataset - use batch processing")
elif data_size > 50:
    print("Medium dataset - standard processing")
else:
    print("Small dataset - quick processing")


# ============================================
# 5. LOOPS
# ============================================

print("\n" + "=" * 50)
print("LOOPS")
print("=" * 50)

# For loop with list
customers = ["Alice", "Bob", "Charlie", "Diana"]

print("Customer List:")
for customer in customers:
    print(f"  - {customer}")

# For loop with range
print("\nNumbers 1-5:")
for i in range(1, 6):
    print(i, end=" ")

# While loop
print("\n\nCountdown:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Launch!")

# Break and Continue
print("\n\nBreak Example:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")

print("\n\nContinue Example:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")


# ============================================
# 6. FUNCTIONS
# ============================================

print("\n\n" + "=" * 50)
print("FUNCTIONS")
print("=" * 50)

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

def calculate_total(price, quantity, tax_rate=0.1):
    """Calculate total with tax"""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

# Function calls
print(greet("Data Engineer"))
print(f"Total: ${calculate_total(100, 5, 0.15):.2f}")

# Function with multiple return values
def get_stats(numbers):
    """Calculate statistics"""
    return sum(numbers), min(numbers), max(numbers), len(numbers)

nums = [10, 20, 30, 40, 50]
total, minimum, maximum, count = get_stats(nums)
print(f"\nStats: Total={total}, Min={minimum}, Max={maximum}, Count={count}")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(f"\nSquare of 5: {square(5)}")

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even}")


# ============================================
# 7. PRACTICE EXERCISES
# ============================================

print("\n\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# Exercise 1: Temperature Converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    # YOUR CODE HERE
    pass

# Exercise 2: Check if number is even
def is_even(number):
    """Check if number is even"""
    # YOUR CODE HERE
    pass

# Exercise 3: Calculate factorial
def factorial(n):
    """Calculate factorial of n"""
    # YOUR CODE HERE
    pass

# Exercise 4: Find largest number in list
def find_max(numbers):
    """Find maximum number in list"""
    # YOUR CODE HERE
    pass

# Exercise 5: Count vowels in string
def count_vowels(text):
    """Count vowels in string"""
    # YOUR CODE HERE
    pass

# Exercise 6: Reverse a string
def reverse_string(text):
    """Reverse a string"""
    # YOUR CODE HERE
    pass

# Exercise 7: Check if palindrome
def is_palindrome(text):
    """Check if text is palindrome"""
    # YOUR CODE HERE
    pass

# Exercise 8: FizzBuzz
def fizzbuzz(n):
    """
    Print numbers 1 to n
    For multiples of 3: print "Fizz"
    For multiples of 5: print "Buzz"
    For multiples of both: print "FizzBuzz"
    """
    # YOUR CODE HERE
    pass


# ============================================
# 8. DATA ENGINEERING EXAMPLES
# ============================================

print("\n" + "=" * 50)
print("DATA ENGINEERING EXAMPLES")
print("=" * 50)

# Example: Clean and validate data
def clean_email(email):
    """Clean and validate email"""
    email = email.strip().lower()
    if '@' in email and '.' in email:
        return email
    else:
        return None

emails = ["  ALICE@EXAMPLE.COM  ", "bob@test.com", "invalid", "charlie@domain.org"]
print("\nEmail Cleaning:")
for email in emails:
    cleaned = clean_email(email)
    print(f"{email:30} -> {cleaned}")

# Example: Parse and transform data
def parse_log_line(log_line):
    """Parse log line into components"""
    parts = log_line.split("|")
    return {
        "timestamp": parts[0].strip(),
        "level": parts[1].strip(),
        "message": parts[2].strip()
    }

log = "2024-01-15 10:30:00 | ERROR | Database connection failed"
parsed = parse_log_line(log)
print(f"\nParsed Log: {parsed}")

# Example: Data aggregation
def aggregate_sales(sales_data):
    """Aggregate sales by product"""
    totals = {}
    for sale in sales_data:
        product = sale['product']
        amount = sale['amount']
        if product in totals:
            totals[product] += amount
        else:
            totals[product] = amount
    return totals

sales = [
    {"product": "Laptop", "amount": 1200},
    {"product": "Mouse", "amount": 25},
    {"product": "Laptop", "amount": 1300},
    {"product": "Keyboard", "amount": 75},
    {"product": "Mouse", "amount": 20},
]

aggregated = aggregate_sales(sales)
print(f"\nAggregated Sales: {aggregated}")


# ============================================
# 9. TIPS AND BEST PRACTICES
# ============================================

"""
DATA ENGINEERING BEST PRACTICES:

1. Use meaningful variable names
   - Good: customer_count, total_revenue
   - Bad: x, temp, data1

2. Write docstrings for functions
   - Explain what the function does
   - Document parameters and return values

3. Handle errors gracefully
   - Use try-except blocks
   - Log errors for debugging

4. Keep functions small and focused
   - One function = one responsibility
   - Easier to test and maintain

5. Use list comprehensions for simple operations
   - More readable and faster
   - Example: [x**2 for x in numbers]

6. Comment your code
   - Explain WHY, not WHAT
   - Future you will thank you

7. Follow PEP 8 style guide
   - Consistent formatting
   - Use tools like black, flake8
"""

print("\n" + "=" * 50)
print("Complete the exercises above and move to data_structures.py")
print("=" * 50)
