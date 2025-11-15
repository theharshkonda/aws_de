"""
Functions - Function Definitions, Lambda Functions, and Functional Programming

This module demonstrates:
- Function definitions with parameters and return values
- Default parameters and keyword arguments
- *args and **kwargs
- Lambda functions
- map(), filter(), and reduce()
- Function documentation and best practices
"""

# ============================================================================
# BASIC FUNCTIONS
# ============================================================================

print("=" * 60)
print("BASIC FUNCTIONS")
print("=" * 60)

# Function with no parameters
def greet():
    """Say hello."""
    return "Hello!"

print(f"greet(): {greet()}")

# Function with parameters
def add(a, b):
    """Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b

result = add(5, 3)
print(f"add(5, 3) = {result}")

# Function with multiple return values
def divide(a, b):
    """Divide two numbers and return quotient and remainder.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Tuple of (quotient, remainder)
    """
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(f"divide(17, 5) = quotient: {q}, remainder: {r}")

# Function that modifies a list
def append_to_list(item, lst=None):
    """Append item to list (demonstrates mutable default argument issue).

    Args:
        item: Item to append
        lst: List to append to (creates new if None)

    Returns:
        Modified list
    """
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# Important: Using mutable defaults is dangerous
list1 = append_to_list(1)
list2 = append_to_list(2)
print(f"list1: {list1}, list2: {list2}")

# ============================================================================
# DEFAULT PARAMETERS AND KEYWORD ARGUMENTS
# ============================================================================

print("\n" + "=" * 60)
print("DEFAULT PARAMETERS AND KEYWORD ARGUMENTS")
print("=" * 60)

def power(base, exponent=2):
    """Raise base to exponent power.

    Args:
        base: The base number
        exponent: The power (default: 2)

    Returns:
        Result of base ** exponent
    """
    return base ** exponent

print(f"power(5) = {power(5)}")          # Uses default exponent=2
print(f"power(5, 3) = {power(5, 3)}")    # Overrides default

# Keyword arguments
def describe_person(name, age, city="Unknown", occupation="Unemployed"):
    """Describe a person with optional details.

    Args:
        name: Person's name (required)
        age: Person's age (required)
        city: Person's city (optional)
        occupation: Person's occupation (optional)

    Returns:
        Description string
    """
    return f"{name}, {age}, lives in {city}, works as {occupation}"

print("\nKeyword arguments:")
print(describe_person("Alice", 28))
print(describe_person("Bob", 35, city="New York"))
print(describe_person("Charlie", 42, occupation="Engineer", city="Seattle"))

# ============================================================================
# *ARGS AND **KWARGS
# ============================================================================

print("\n" + "=" * 60)
print("*ARGS AND **KWARGS")
print("=" * 60)

# *args: Variable number of positional arguments (tuple)
def sum_numbers(*args):
    """Sum any number of arguments.

    Args:
        *args: Variable number of numbers

    Returns:
        Sum of all arguments
    """
    total = 0
    for num in args:
        total += num
    return total

print(f"sum_numbers(1, 2, 3) = {sum_numbers(1, 2, 3)}")
print(f"sum_numbers(10, 20, 30, 40, 50) = {sum_numbers(10, 20, 30, 40, 50)}")

# **kwargs: Variable keyword arguments (dictionary)
def print_details(**kwargs):
    """Print all key-value pairs.

    Args:
        **kwargs: Variable keyword arguments
    """
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nprint_details() with keyword arguments:")
print_details(name="Alice", age=28, city="Boston")

# Combining regular args, *args, and **kwargs
def flexible_function(required, *args, **kwargs):
    """Demonstrate flexible function parameters.

    Args:
        required: Required positional argument
        *args: Additional positional arguments
        **kwargs: Keyword arguments
    """
    print(f"Required: {required}")
    print(f"Additional args: {args}")
    print(f"Keyword args: {kwargs}")

print("\nflexible_function('needed', 1, 2, 3, name='Alice', age=28):")
flexible_function('needed', 1, 2, 3, name='Alice', age=28)

# ============================================================================
# LAMBDA FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("LAMBDA FUNCTIONS")
print("=" * 60)

# Simple lambda
square = lambda x: x ** 2
print(f"Lambda square: square(5) = {square(5)}")

# Lambda with multiple parameters
add_lambda = lambda x, y: x + y
print(f"Lambda add: add_lambda(3, 7) = {add_lambda(3, 7)}")

# Lambda with conditional
classify = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"Lambda classify: classify(7) = {classify(7)}, classify(8) = {classify(8)}")

# Lambda are often used with map(), filter(), reduce()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"\nLambda with map - double numbers: {doubled}")

# ============================================================================
# MAP FUNCTION
# ============================================================================

print("\n" + "=" * 60)
print("MAP FUNCTION")
print("=" * 60)

# map() applies a function to every item in an iterable
numbers = [1, 2, 3, 4, 5]

# Convert to kilometers
def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934

distances_km = list(map(miles_to_km, [1, 2, 5, 10]))
print(f"Miles to KM: {distances_km}")

# Using lambda with map
prices = [10, 20, 30, 40]
discounted = list(map(lambda x: x * 0.9, prices))
print(f"10% discount: {discounted}")

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"Sum of two lists: {sums}")

# ============================================================================
# FILTER FUNCTION
# ============================================================================

print("\n" + "=" * 60)
print("FILTER FUNCTION")
print("=" * 60)

# filter() keeps only items where function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(f"Even numbers: {even_numbers}")

# Filter with lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers: {odd_numbers}")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {greater_than_5}")

# Filter students with passing grades
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 62},
    {"name": "Charlie", "grade": 91},
    {"name": "Diana", "grade": 58}
]

passing = list(filter(lambda s: s["grade"] >= 70, students))
print(f"\nPassing students: {[s['name'] for s in passing]}")

# ============================================================================
# REDUCE FUNCTION
# ============================================================================

print("\n" + "=" * 60)
print("REDUCE FUNCTION")
print("=" * 60)

from functools import reduce

# reduce() applies function cumulatively to items in iterable
numbers = [1, 2, 3, 4, 5]

# Sum all numbers using reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of {numbers}: {product}")

# Find maximum using reduce
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum of {numbers}: {max_num}")

# Build a sentence from words
words = ["Python", "is", "awesome"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"Sentence: {sentence}")

# ============================================================================
# HIGHER-ORDER FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("HIGHER-ORDER FUNCTIONS")
print("=" * 60)

# Function that returns a function
def make_multiplier(n):
    """Create a multiplier function.

    Args:
        n: Multiplier factor

    Returns:
        Function that multiplies by n
    """
    def multiplier(x):
        return x * n
    return multiplier

times_3 = make_multiplier(3)
times_5 = make_multiplier(5)

print(f"times_3(4) = {times_3(4)}")
print(f"times_5(4) = {times_5(4)}")

# Function that takes a function as parameter
def apply_twice(func, x):
    """Apply function twice to value.

    Args:
        func: Function to apply
        x: Value to apply function to

    Returns:
        Result of applying func twice
    """
    return func(func(x))

double = lambda x: x * 2
result = apply_twice(double, 5)
print(f"\napply_twice(double, 5) = {result}")  # (5*2)*2 = 20

# ============================================================================
# DECORATORS
# ============================================================================

print("\n" + "=" * 60)
print("DECORATORS (Introduction)")
print("=" * 60)

# Simple decorator
def uppercase_decorator(func):
    """Decorator to convert output to uppercase."""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet_decorated():
    """Greet function with decorator."""
    return "hello world"

print(f"With decorator: {greet_decorated()}")

# Decorator with arguments
def repeat_decorator(times):
    """Decorator that repeats function output."""
    def decorator(func):
        def wrapper():
            return (func() + " ") * times
        return wrapper
    return decorator

@repeat_decorator(3)
def say_hello():
    """Say hello, repeated."""
    return "Hello"

print(f"Repeated: {say_hello()}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Data transformation pipeline
print("\nExample 1: Data transformation pipeline")
raw_data = [
    {"name": "alice", "score": 85},
    {"name": "bob", "score": 92},
    {"name": "charlie", "score": 78}
]

# Step 1: Filter passing grades
passing = list(filter(lambda x: x["score"] >= 80, raw_data))

# Step 2: Transform to upper case names
transformed = list(map(lambda x: {**x, "name": x["name"].upper()}, passing))

print(f"Filtered and transformed: {transformed}")

# Example 2: Recursive function (factorial)
def factorial(n):
    """Calculate factorial using recursion.

    Args:
        n: Number to calculate factorial for

    Returns:
        n! (n factorial)
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\nExample 2: factorial(5) = {factorial(5)}")

# Example 3: Function composition
def compose(*functions):
    """Compose functions together.

    Args:
        *functions: Functions to compose

    Returns:
        Function that applies all functions
    """
    def inner(arg):
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result
    return inner

add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2
square = lambda x: x ** 2

# Apply: square, then multiply by 2, then add 1
composed = compose(add_one, multiply_by_two, square)
print(f"\nExample 3: compose(add_one, multiply_by_two, square)(5) = {composed(5)}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key Concepts:

1. FUNCTION DEFINITIONS:
   - def keyword to define functions
   - Parameters and return values
   - Multiple return values (tuples)

2. DEFAULT PARAMETERS:
   - Provide default values for parameters
   - Parameters without defaults must come first
   - Avoid mutable defaults (lists, dicts)

3. *ARGS AND **KWARGS:
   - *args: Collect variable positional arguments (tuple)
   - **kwargs: Collect variable keyword arguments (dict)
   - Useful for flexible function signatures

4. LAMBDA FUNCTIONS:
   - Anonymous functions defined with lambda keyword
   - Useful for short, simple operations
   - Often used with map, filter, reduce

5. FUNCTIONAL PROGRAMMING:
   - map(): Apply function to all items
   - filter(): Keep items where function returns True
   - reduce(): Apply function cumulatively

6. HIGHER-ORDER FUNCTIONS:
   - Functions that take functions as parameters
   - Functions that return functions
   - Enables function composition

7. BEST PRACTICES:
   - Use meaningful function names
   - Write comprehensive docstrings
   - Keep functions focused on one task
   - Use type hints for clarity (Python 3.5+)
   - Avoid side effects when possible
   - Use built-in functions (map, filter, reduce) judiciously
   - Consider readability over cleverness
""")
