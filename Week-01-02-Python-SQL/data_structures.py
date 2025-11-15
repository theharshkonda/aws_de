"""
Data Structures - Lists, Tuples, Dictionaries, and Sets

This module demonstrates Python's core data structures:
- Lists: Ordered, mutable collections
- Tuples: Ordered, immutable collections
- Dictionaries: Key-value mappings
- Sets: Unordered, unique collections
- List comprehensions
- Dictionary comprehensions
"""

# ============================================================================
# LISTS
# ============================================================================

print("=" * 60)
print("LISTS - Ordered, Mutable Collections")
print("=" * 60)

# Create lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "string", 3.14, True, None]

print(f"Numbers list: {numbers}")
print(f"Mixed list: {mixed}")
print(f"List length: {len(numbers)}")

# List indexing (0-based)
print(f"\nFirst element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Second to last: {numbers[-2]}")

# List slicing
print(f"Elements 1-3: {numbers[1:4]}")
print(f"First 3 elements: {numbers[:3]}")
print(f"Last 3 elements: {numbers[-3:]}")
print(f"Every 2nd element: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")

# List methods
print("\nList methods:")
colors = ["red", "blue", "green"]
colors.append("yellow")
print(f"After append('yellow'): {colors}")

colors.insert(1, "orange")
print(f"After insert(1, 'orange'): {colors}")

colors.remove("blue")
print(f"After remove('blue'): {colors}")

popped = colors.pop()
print(f"After pop(): {colors}, popped value: {popped}")

colors.extend(["purple", "pink"])
print(f"After extend(['purple', 'pink']): {colors}")

# List copying (important!)
print("\nList copying:")
original = [1, 2, 3]
shallow_copy = original  # This is not a copy, just a reference
deep_copy = original.copy()  # This is a true copy

shallow_copy.append(4)
print(f"Original: {original}, Shallow copy: {shallow_copy}")  # Both changed!

original.append(5)
print(f"Original: {original}, Deep copy: {deep_copy}")  # Only original changed

# Sorting and reversing
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal: {numbers}")
print(f"Sorted: {sorted(numbers)}")
print(f"Sorted descending: {sorted(numbers, reverse=True)}")

numbers.sort()
print(f"After .sort(): {numbers}")

# List comprehensions
print("\nList comprehensions:")
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares 1-5: {squares}")

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Squares of even numbers 1-10: {even_squares}")

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3 multiplication table: {matrix}")

# ============================================================================
# TUPLES
# ============================================================================

print("\n" + "=" * 60)
print("TUPLES - Ordered, Immutable Collections")
print("=" * 60)

# Create tuples
empty_tuple = ()
single_element = (42,)  # Note: comma required for single element
coordinates = (10, 20)
person = ("Alice", 28, "Engineer")

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")
print(f"Tuple length: {len(person)}")

# Tuple indexing and slicing (same as lists)
print(f"First element: {person[0]}")
print(f"Last element: {person[-1]}")
print(f"Elements 0-1: {person[0:2]}")

# Unpacking tuples
name, age, job = person
print(f"\nUnpacked: name={name}, age={age}, job={job}")

# Swapping variables using tuple unpacking
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print(f"\nTuple: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Immutability - tuples cannot be modified
# numbers[0] = 10  # This would raise TypeError

# Tuple concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"\nCombined: {combined}")
print(f"Repeated: {tuple1 * 2}")

# Converting between lists and tuples
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"List to tuple: {my_tuple}")

my_list2 = list(my_tuple)
print(f"Tuple to list: {my_list2}")

# ============================================================================
# DICTIONARIES
# ============================================================================

print("\n" + "=" * 60)
print("DICTIONARIES - Key-Value Mappings")
print("=" * 60)

# Create dictionaries
empty_dict = {}
person = {
    "name": "Alice",
    "age": 28,
    "city": "Boston",
    "occupation": "Engineer"
}

print(f"Person: {person}")
print(f"Dictionary length: {len(person)}")

# Accessing values
print(f"\nAccessing values:")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Using get() method (safer, returns None if key doesn't exist)
print(f"Country: {person.get('country')}")
print(f"Country with default: {person.get('country', 'USA')}")

# Adding and modifying items
person['email'] = 'alice@example.com'
print(f"After adding email: {person}")

person['age'] = 29
print(f"After updating age: {person}")

# Removing items
del person['email']
print(f"After deleting email: {person}")

popped_value = person.pop('occupation')
print(f"After pop('occupation'): {person}, popped value: {popped_value}")

# Dictionary methods
print("\nDictionary methods:")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Iterating over dictionaries
print("\nIterating over dictionary:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # Python 3.5+
print(f"\nMerged: {merged}")

dict1.update(dict2)  # In-place merge
print(f"After update(): {dict1}")

# Dictionary comprehensions
print("\nDictionary comprehensions:")
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Squares: {squares_dict}")

# Conditional dictionary comprehension
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Creating dict from list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print(f"Dict from pairs: {dict_from_pairs}")

# Nested dictionaries
company = {
    "name": "TechCorp",
    "employees": {
        "alice": {"position": "Engineer", "salary": 100000},
        "bob": {"position": "Manager", "salary": 120000}
    }
}
print(f"\nNested dict - Alice's position: {company['employees']['alice']['position']}")

# ============================================================================
# SETS
# ============================================================================

print("\n" + "=" * 60)
print("SETS - Unordered, Unique Collections")
print("=" * 60)

# Create sets
empty_set = set()  # Note: {} creates empty dict, not set
numbers = {1, 2, 3, 4, 5}
colors = {"red", "blue", "green", "red"}  # Duplicates removed

print(f"Numbers set: {numbers}")
print(f"Colors set: {colors}")  # Note: "red" appears only once
print(f"Set length: {len(numbers)}")

# Adding and removing items
colors.add("yellow")
print(f"After add('yellow'): {colors}")

colors.discard("blue")
print(f"After discard('blue'): {colors}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet operations:")
print(f"Union: {set1 | set2}")  # All elements
print(f"Intersection: {set1 & set2}")  # Common elements
print(f"Difference: {set1 - set2}")  # In set1 but not set2
print(f"Symmetric difference: {set1 ^ set2}")  # In either but not both

# Set methods
print(f"\nSet methods:")
print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")
print(f"Is disjoint: {set1.isdisjoint({10, 11})}")  # No common elements
print(f"Is subset: {set2.issubset(set1)}")  # All of set2 in set1?
print(f"Is superset: {set1.issuperset({1, 2})}")  # Contains all of {1,2}?

# Removing duplicates
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = list(set(numbers_with_duplicates))
print(f"\nRemoving duplicates: {unique_numbers}")

# Set comprehension
squares_set = {x ** 2 for x in range(1, 6)}
print(f"Squares set: {squares_set}")

# ============================================================================
# COMPARISON OF DATA STRUCTURES
# ============================================================================

print("\n" + "=" * 60)
print("COMPARISON OF DATA STRUCTURES")
print("=" * 60)

comparison = {
    "List": ["Ordered", "Mutable", "Duplicates OK", "Slower lookup"],
    "Tuple": ["Ordered", "Immutable", "Duplicates OK", "Slightly faster"],
    "Dict": ["Ordered (3.7+)", "Mutable", "Keys unique", "Fast lookup"],
    "Set": ["Unordered", "Mutable", "Unique items", "Very fast lookup"]
}

for structure, characteristics in comparison.items():
    print(f"{structure}: {', '.join(characteristics)}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Count word frequency
print("\nExample 1: Count word frequency")
sentence = "python python is awesome python"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word frequency: {word_count}")

# Example 2: Find common elements between lists
print("\nExample 2: Find common elements")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")

# Example 3: Group data by category
print("\nExample 3: Group by category")
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"}
]

by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

for grade, names in sorted(by_grade.items()):
    print(f"Grade {grade}: {names}")

# Example 4: Nested data structure processing
print("\nExample 4: Process nested data")
data = {
    "users": [
        {"id": 1, "name": "Alice", "scores": [85, 90, 88]},
        {"id": 2, "name": "Bob", "scores": [92, 88, 95]},
        {"id": 3, "name": "Charlie", "scores": [78, 82, 80]}
    ]
}

for user in data["users"]:
    avg_score = sum(user["scores"]) / len(user["scores"])
    print(f"{user['name']}: Average score = {avg_score:.1f}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Data Structure Overview:

LIST [1, 2, 3]:
- Ordered, mutable, allows duplicates
- Index-based access
- Use for: Sequences, collections needing modification
- Methods: append(), extend(), insert(), remove(), pop(), sort()

TUPLE (1, 2, 3):
- Ordered, immutable, allows duplicates
- Lightweight, hashable (can use as dict key)
- Use for: Fixed collections, function returns
- Methods: count(), index()

DICTIONARY {"key": "value"}:
- Key-value pairs, mutable (3.7+ maintains order)
- Fast key lookup
- Use for: Mappings, records, configurations
- Methods: keys(), values(), items(), get(), pop(), update()

SET {1, 2, 3}:
- Unordered, unique items, mutable
- Very fast membership testing
- Use for: Unique collections, set operations
- Methods: add(), remove(), union(), intersection(), difference()

Key Differences:
- Mutability: Lists and Dicts are mutable; Tuples are not
- Ordering: Lists, Tuples preserve order; Sets don't
- Performance: Sets are fastest for membership testing
- Use Cases: Choose based on your specific needs

Best Practices:
- Use lists for ordered collections
- Use tuples for immutable sequences
- Use dicts for key-value data
- Use sets for unique items and set operations
- Use comprehensions for concise list/dict/set creation
- Remember: lists are references, use .copy() when needed
""")
