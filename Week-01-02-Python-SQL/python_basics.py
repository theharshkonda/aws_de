"""
Python Basics - Variables, Data Types, Operators, and Input/Output

This module demonstrates fundamental Python concepts including:
- Variable declaration and naming conventions
- Built-in data types (int, float, str, bool)
- Arithmetic, comparison, and logical operators
- Type conversion
- Input/output operations
"""

# ============================================================================
# VARIABLES AND DATA TYPES
# ============================================================================

# Variables are created by assignment (no explicit type declaration needed)
name = "Alice"              # String
age = 28                    # Integer
height = 5.7                # Float
is_active = True            # Boolean

print("=" * 60)
print("VARIABLES AND DATA TYPES")
print("=" * 60)
print(f"Name: {name} (Type: {type(name).__name__})")
print(f"Age: {age} (Type: {type(age).__name__})")
print(f"Height: {height} (Type: {type(height).__name__})")
print(f"Active: {is_active} (Type: {type(is_active).__name__})")

# Multiple assignment
x, y, z = 10, 20, 30
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# ============================================================================
# ARITHMETIC OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("ARITHMETIC OPERATORS")
print("=" * 60)

a, b = 15, 4

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")                  # Returns float
print(f"Floor Division: {a} // {b} = {a // b}")         # Returns int
print(f"Modulus: {a} % {b} = {a % b}")                  # Remainder
print(f"Exponentiation: {a} ** {b} = {a ** b}")         # Power

# ============================================================================
# COMPARISON OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("COMPARISON OPERATORS")
print("=" * 60)

num1, num2 = 10, 20

print(f"{num1} == {num2}: {num1 == num2}")              # Equal to
print(f"{num1} != {num2}: {num1 != num2}")              # Not equal to
print(f"{num1} < {num2}: {num1 < num2}")                # Less than
print(f"{num1} > {num2}: {num1 > num2}")                # Greater than
print(f"{num1} <= {num2}: {num1 <= num2}")              # Less than or equal
print(f"{num1} >= {num2}: {num1 >= num2}")              # Greater than or equal

# ============================================================================
# LOGICAL OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("LOGICAL OPERATORS")
print("=" * 60)

p, q = True, False

print(f"True and False: {p and q}")                      # Both must be True
print(f"True or False: {p or q}")                        # At least one must be True
print(f"not True: {not p}")                              # Inverts the boolean

# Real-world logical operation
age = 25
has_license = True
can_drive = (age >= 18) and has_license
print(f"\nCan drive (age >= 18 and has_license): {can_drive}")

# ============================================================================
# STRING OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("STRING OPERATIONS")
print("=" * 60)

str1 = "Hello"
str2 = "World"

# Concatenation
result = str1 + " " + str2
print(f"Concatenation: '{result}'")

# Repetition
repeated = "Ha" * 3
print(f"Repetition: '{repeated}'")

# String length
print(f"Length of '{result}': {len(result)}")

# String indexing (0-based)
print(f"First character: '{result[0]}'")
print(f"Last character: '{result[-1]}'")

# String slicing
print(f"Characters 0-4: '{result[0:5]}'")
print(f"Every 2nd character: '{result[::2]}'")

# String methods
print(f"Uppercase: '{result.upper()}'")
print(f"Lowercase: '{result.lower()}'")
print(f"Capitalize: '{result.capitalize()}'")

# String formatting
price = 29.99
quantity = 3
print(f"\nString Formatting Examples:")
print(f"Using f-strings: Price = ${price:.2f}, Quantity = {quantity}")
print("Using format(): Price = ${:.2f}, Quantity = {}".format(price, quantity))
print("Using % operator: Price = $%.2f, Quantity = %d" % (price, quantity))

# ============================================================================
# TYPE CONVERSION
# ============================================================================

print("\n" + "=" * 60)
print("TYPE CONVERSION")
print("=" * 60)

# String to Integer
str_num = "42"
converted_int = int(str_num)
print(f"String '{str_num}' to int: {converted_int} (Type: {type(converted_int).__name__})")

# String to Float
str_float = "3.14"
converted_float = float(str_float)
print(f"String '{str_float}' to float: {converted_float} (Type: {type(converted_float).__name__})")

# Integer to String
num = 100
converted_str = str(num)
print(f"Integer {num} to string: '{converted_str}' (Type: {type(converted_str).__name__})")

# String to Boolean (non-empty string = True, empty string = False)
bool_str = bool("Hello")
print(f"Boolean of 'Hello': {bool_str}")
print(f"Boolean of '': {bool('')}")

# ============================================================================
# INPUT/OUTPUT OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("INPUT/OUTPUT OPERATIONS")
print("=" * 60)

# print() with different parameters
print("Multiple arguments:", 1, 2, 3, 4, 5)
print("Custom separator:", 1, 2, 3, sep=" -> ")
print("Custom end character:", "Line 1", end=" | ")
print("Line 2")

# Example user input (commented out for non-interactive execution)
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# Simulating input with a predefined value
print("\n[Simulated Input Example - normally uses input() function]")
user_input = "42"  # This would normally come from input()
print(f"User entered: {user_input}")
number = int(user_input)
print(f"Converted to integer: {number}")

# ============================================================================
# VARIABLE SCOPE
# ============================================================================

print("\n" + "=" * 60)
print("VARIABLE SCOPE")
print("=" * 60)

global_var = "I'm global"

def demonstrate_scope():
    """Demonstrates variable scope in functions."""
    local_var = "I'm local"
    print(f"Inside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")

print(f"Before function - Global: {global_var}")
demonstrate_scope()
print(f"After function - Global: {global_var}")

# ============================================================================
# CONSTANTS (Python convention)
# ============================================================================

print("\n" + "=" * 60)
print("CONSTANTS (Convention: UPPERCASE)")
print("=" * 60)

PI = 3.14159
MAX_ATTEMPTS = 5
DATABASE_URL = "postgresql://localhost:5432/mydb"

radius = 10
area = PI * (radius ** 2)
print(f"Circle area with radius {radius}: {area:.2f}")
print(f"Max retry attempts: {MAX_ATTEMPTS}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key Concepts Covered:
1. Variables - No explicit type declaration needed
2. Data Types - int, float, str, bool
3. Operators - Arithmetic, comparison, logical
4. String Operations - Concatenation, slicing, methods, formatting
5. Type Conversion - Convert between different types
6. Input/Output - print() and input() functions
7. Variable Scope - Global and local variables
8. Constants - Convention of using UPPERCASE names

Best Practices:
- Use meaningful variable names (snake_case)
- Use f-strings for modern string formatting
- Convert types explicitly to avoid errors
- Use comments to explain complex logic
- Follow PEP 8 style guidelines
""")
