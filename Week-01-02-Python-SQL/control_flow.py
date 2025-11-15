"""
Control Flow - If/Else Statements, Loops, Break/Continue

This module demonstrates control flow structures:
- Conditional statements (if, elif, else)
- While loops
- For loops
- Loop control (break, continue)
- Nested loops
- Loop-else construct
"""

# ============================================================================
# IF/ELIF/ELSE STATEMENTS
# ============================================================================

print("=" * 60)
print("IF/ELIF/ELSE STATEMENTS")
print("=" * 60)

# Basic if statement
age = 20
if age >= 18:
    print(f"Age {age}: You are an adult")

# if-else statement
temperature = 15
if temperature > 25:
    print(f"Temperature {temperature}: It's hot")
else:
    print(f"Temperature {temperature}: It's cold")

# if-elif-else statement
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score}: Grade {grade}")

# Nested if statements
username = "admin"
password = "secure123"

if username == "admin":
    if password == "secure123":
        print("Login successful!")
    else:
        print("Incorrect password")
else:
    print("User not found")

# Ternary operator (conditional expression)
age = 17
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# ============================================================================
# WHILE LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("WHILE LOOPS")
print("=" * 60)

# Basic while loop
print("\nCounting with while loop (1 to 5):")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# While loop with break
print("\nWhile loop with break (search):")
search_value = 7
numbers = [2, 4, 6, 7, 9, 11]
index = 0
while index < len(numbers):
    if numbers[index] == search_value:
        print(f"Found {search_value} at index {index}")
        break
    index += 1
else:
    print(f"{search_value} not found")

# While loop with continue
print("\nWhile loop with continue (skip even numbers):")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {count}")

# ============================================================================
# FOR LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("FOR LOOPS")
print("=" * 60)

# For loop with range()
print("\nFor loop with range (1 to 5):")
for i in range(1, 6):
    print(f"Number: {i}")

# For loop with step
print("\nFor loop with step (0 to 10, step 2):")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# For loop with list
print("\nFor loop with list:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"- {fruit}")

# For loop with enumerate (index and value)
print("\nFor loop with enumerate (index and value):")
for index, fruit in enumerate(fruits):
    print(f"  [{index}] {fruit}")

# For loop with break
print("\nFor loop with break (find first even number):")
numbers = [1, 3, 5, 7, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break

# For loop with continue
print("\nFor loop with continue (skip odd numbers):")
for num in range(1, 11):
    if num % 2 != 0:
        continue  # Skip odd numbers
    print(f"Even: {num}")

# For-else construct (else executes if loop completes without break)
print("\nFor-else construct (loop completed normally):")
for i in range(1, 4):
    print(f"Iteration {i}")
else:
    print("Loop completed successfully!")

# For-else with break (else won't execute)
print("\nFor-else with break (loop interrupted):")
for i in range(1, 10):
    if i == 3:
        print(f"Breaking at {i}")
        break
    print(f"Iteration {i}")
else:
    print("This won't print because of break")

# ============================================================================
# NESTED LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("NESTED LOOPS")
print("=" * 60)

# Multiplication table
print("\nMultiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}*{j}={i*j}", end=" | ")
    print()

# Nested loop with break (breaking outer loop)
print("\nNested loop searching for a target:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5
found = False

for row in matrix:
    for num in row:
        if num == target:
            print(f"Found {target} in matrix")
            found = True
            break
    if found:
        break

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: FizzBuzz problem
print("\nExample 1: FizzBuzz (1 to 15):")
for i in range(1, 16):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if not output:
        output = str(i)
    print(output, end=" ")
print()

# Example 2: Sum of numbers with condition
print("\nExample 2: Sum of numbers 1-10 (skip if divisible by 3):")
total = 0
for i in range(1, 11):
    if i % 3 == 0:
        continue
    total += i
    print(f"Adding {i}, Total: {total}")
print(f"Final Total: {total}")

# Example 3: Password validation loop
print("\nExample 3: Password validation (simulated):")
max_attempts = 3
attempt = 0
correct_password = "secret123"

# Simulating with a while loop (normally would use input())
passwords = ["wrong1", "wrong2", "secret123"]  # Pre-defined for demo
while attempt < max_attempts:
    entered_password = passwords[attempt]
    print(f"Attempt {attempt + 1}: Password entered: {entered_password}")

    if entered_password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect password, try again")
        attempt += 1
else:
    print("Maximum attempts exceeded. Access denied.")

# Example 4: Prime number checker
print("\nExample 4: Prime numbers from 2 to 20:")
for num in range(2, 21):
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime", end=" | ")
print()

# Example 5: Processing a list of dictionaries
print("\nExample 5: Processing a list of dictionaries:")
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 95}
]

for student in students:
    if student["score"] >= 90:
        status = "Excellent"
    elif student["score"] >= 80:
        status = "Good"
    else:
        status = "Needs improvement"

    print(f"{student['name']}: {student['score']} - {status}")

# ============================================================================
# COMMON PATTERNS
# ============================================================================

print("\n" + "=" * 60)
print("COMMON PATTERNS")
print("=" * 60)

# Pattern 1: Count occurrences
print("\nPattern 1: Count occurrences of a value:")
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
target = 4
count = 0
for value in data:
    if value == target:
        count += 1
print(f"Value {target} appears {count} times")

# Pattern 2: Filter values
print("\nPattern 2: Filter even numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# Pattern 3: Transform values
print("\nPattern 3: Transform (square) numbers:")
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(f"Squared: {squared}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Control Flow Structures:

1. IF/ELIF/ELSE:
   - Single condition: if
   - Multiple conditions: if-elif-else
   - Nested: if inside if
   - Ternary: value_if_true if condition else value_if_false

2. WHILE LOOPS:
   - Repeats while condition is True
   - Use break to exit early
   - Use continue to skip to next iteration
   - Optional else clause executes if loop completes normally

3. FOR LOOPS:
   - Iterates over sequences (lists, strings, ranges)
   - Use range(start, stop, step)
   - Use enumerate() for index and value
   - Use break and continue for control
   - Optional else clause

4. NESTED LOOPS:
   - Loop inside another loop
   - Use break in inner loop, but need flag for outer

5. BEST PRACTICES:
   - Keep conditions simple and readable
   - Use meaningful variable names
   - Avoid deeply nested loops (>3 levels)
   - Use continue to reduce nesting
   - Consider list comprehensions for simple transformations
""")
