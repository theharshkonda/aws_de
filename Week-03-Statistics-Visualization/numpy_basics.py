"""
NumPy Basics - Array Operations and Statistics

This module demonstrates:
- NumPy array creation and manipulation
- Array operations and computations
- Statistical functions
- Array indexing and slicing
- Broadcasting
"""

import numpy as np

print("=" * 60)
print("NumPy BASICS - Array Operations and Statistics")
print("=" * 60)

# ============================================================================
# ARRAY CREATION
# ============================================================================

print("\nARRAY CREATION:")
print("-" * 60)

# Create array from list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"Array from list: {arr1}")
print(f"Type: {type(arr1)}, dtype: {arr1.dtype}, shape: {arr1.shape}")

# Create array with specific dtype
arr2 = np.array([1, 2, 3, 4, 5], dtype=float)
print(f"\nFloat array: {arr2}")

# Create 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D array:\n{arr2d}")
print(f"Shape: {arr2d.shape}")

# Create arrays with ranges
arr_range = np.arange(0, 10, 2)  # 0 to 10, step 2
print(f"\nArray with arange(0, 10, 2): {arr_range}")

arr_linspace = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
print(f"Array with linspace(0, 1, 5): {arr_linspace}")

# Create arrays with special values
zeros = np.zeros((3, 3))
print(f"\nZeros (3x3):\n{zeros}")

ones = np.ones((2, 4))
print(f"\nOnes (2x4):\n{ones}")

eye = np.eye(3)  # Identity matrix
print(f"\nIdentity matrix (3x3):\n{eye}")

# Create random arrays
np.random.seed(42)  # For reproducibility
random_arr = np.random.rand(3, 3)  # Random values [0, 1)
print(f"\nRandom array (3x3):\n{random_arr}")

random_int = np.random.randint(1, 10, size=5)  # Random integers
print(f"\nRandom integers 1-10: {random_int}")

# ============================================================================
# ARRAY PROPERTIES
# ============================================================================

print("\n" + "=" * 60)
print("ARRAY PROPERTIES:")
print("-" * 60)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array:\n{arr}\n")

print(f"Shape (dimensions): {arr.shape}")
print(f"Size (total elements): {arr.size}")
print(f"Ndim (number of dimensions): {arr.ndim}")
print(f"Dtype (data type): {arr.dtype}")
print(f"Itemsize (bytes per element): {arr.itemsize}")

# ============================================================================
# INDEXING AND SLICING
# ============================================================================

print("\n" + "=" * 60)
print("INDEXING AND SLICING:")
print("-" * 60)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Array:\n{arr}\n")

# 1D indexing
print(f"arr[0, 0]: {arr[0, 0]}")
print(f"arr[2, 3]: {arr[2, 3]}")
print(f"arr[-1, -1]: {arr[-1, -1]}")

# Slicing
print(f"\narr[0, :]: {arr[0, :]}")  # First row
print(f"arr[:, 0]: {arr[:, 0]}")  # First column
print(f"arr[1:3, 1:3]:\n{arr[1:3, 1:3]}")  # 2x2 subarray

# Boolean indexing
print(f"\nBoolean indexing (arr > 5): {arr[arr > 5]}")

# Fancy indexing
indices = [0, 2]
print(f"arr[indices]: {arr[indices, :]}")

# ============================================================================
# ARRAY OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("ARRAY OPERATIONS:")
print("-" * 60)

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 6, 8, 10])

print(f"a: {a}")
print(f"b: {b}\n")

# Element-wise operations
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Power (a ** 2): {a ** 2}")

# Scalar operations
print(f"\nScalar operations:")
print(f"a + 10: {a + 10}")
print(f"a * 2: {a * 2}")

# Matrix operations
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(f"\nMatrix operations:")
print(f"arr1 @ arr2 (matrix multiplication):\n{arr1 @ arr2}")
print(f"np.dot(arr1, arr2):\n{np.dot(arr1, arr2)}")

# ============================================================================
# BROADCASTING
# ============================================================================

print("\n" + "=" * 60)
print("BROADCASTING:")
print("-" * 60)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array (2x3):\n{arr}\n")

# Adding scalar
print(f"arr + 10:\n{arr + 10}\n")

# Adding 1D array to 2D array
print(f"arr + [1, 2, 3]:\n{arr + np.array([1, 2, 3])}\n")

# ============================================================================
# AGGREGATION FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("AGGREGATION FUNCTIONS:")
print("-" * 60)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Array:\n{arr}\n")

print(f"Sum: {np.sum(arr)}")
print(f"Sum along axis 0 (columns): {np.sum(arr, axis=0)}")
print(f"Sum along axis 1 (rows): {np.sum(arr, axis=1)}")

print(f"\nMean: {np.mean(arr)}")
print(f"Mean along axis 0: {np.mean(arr, axis=0)}")

print(f"\nMin: {np.min(arr)}")
print(f"Max: {np.max(arr)}")

print(f"\nStandard deviation: {np.std(arr)}")
print(f"Variance: {np.var(arr)}")

# ============================================================================
# STATISTICAL FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("STATISTICAL FUNCTIONS:")
print("-" * 60)

data = np.array([23, 45, 56, 12, 78, 34, 56, 89, 12, 45])
print(f"Data: {data}\n")

print(f"Mean: {np.mean(data):.2f}")
print(f"Median: {np.median(data):.2f}")
print(f"Standard deviation: {np.std(data):.2f}")
print(f"Variance: {np.var(data):.2f}")

print(f"\nMin: {np.min(data)}")
print(f"Max: {np.max(data)}")
print(f"Range: {np.max(data) - np.min(data)}")

# Percentiles
print(f"\n25th percentile: {np.percentile(data, 25)}")
print(f"50th percentile (median): {np.percentile(data, 50)}")
print(f"75th percentile: {np.percentile(data, 75)}")

# Quantiles
print(f"\nQuantiles: {np.quantile(data, [0.25, 0.5, 0.75])}")

# ============================================================================
# RESHAPING AND TRANSPOSING
# ============================================================================

print("\n" + "=" * 60)
print("RESHAPING AND TRANSPOSING:")
print("-" * 60)

arr = np.arange(12)
print(f"Original array: {arr}")

reshaped = arr.reshape(3, 4)
print(f"\nReshaped (3, 4):\n{reshaped}")

reshaped2 = arr.reshape(2, 2, 3)
print(f"\nReshaped (2, 2, 3):\n{reshaped2}")

flattened = reshaped.flatten()
print(f"\nFlattened: {flattened}")

# Transpose
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nOriginal 2D:\n{arr2d}")
print(f"Transposed:\n{arr2d.T}")

# ============================================================================
# SORTING AND UNIQUE
# ============================================================================

print("\n" + "=" * 60)
print("SORTING AND UNIQUE:")
print("-" * 60)

arr = np.array([5, 2, 8, 2, 9, 1, 5, 5])
print(f"Array: {arr}\n")

print(f"Sorted: {np.sort(arr)}")
print(f"Argsort (indices): {np.argsort(arr)}")
print(f"Unique values: {np.unique(arr)}")

# Count occurrences
unique, counts = np.unique(arr, return_counts=True)
print(f"\nUnique values and counts:")
for val, count in zip(unique, counts):
    print(f"  {val}: {count} times")

# ============================================================================
# USEFUL FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("USEFUL FUNCTIONS:")
print("-" * 60)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}\n")

print(f"Cumulative sum: {np.cumsum(arr)}")
print(f"Cumulative product: {np.cumprod(arr)}")
print(f"Differences: {np.diff(arr)}")

# Where condition
print(f"\nWhere (arr > 3): {np.where(arr > 3, 'Yes', 'No')}")

# Clip values
clipped = np.clip(arr, 2, 4)
print(f"Clipped [2, 4]: {clipped}")

# ============================================================================
# PRACTICAL EXAMPLE
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - Data Analysis:")
print("-" * 60)

# Generate sample data: Test scores for 30 students
np.random.seed(42)
scores = np.random.normal(loc=75, scale=10, size=30)
scores = np.round(np.clip(scores, 0, 100))

print(f"Test Scores (30 students):\n{scores}\n")

print("STATISTICS:")
print(f"  Mean: {np.mean(scores):.2f}")
print(f"  Median: {np.median(scores):.2f}")
print(f"  Std Dev: {np.std(scores):.2f}")
print(f"  Min: {np.min(scores)}")
print(f"  Max: {np.max(scores)}")

print("\nGRADE DISTRIBUTION:")
grades = {'A': np.sum(scores >= 90), 'B': np.sum((scores >= 80) & (scores < 90)),
          'C': np.sum((scores >= 70) & (scores < 80)), 'D': np.sum((scores >= 60) & (scores < 70)),
          'F': np.sum(scores < 60)}
for grade, count in grades.items():
    print(f"  {grade}: {count} students ({count/len(scores)*100:.1f}%)")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
NumPy Key Concepts:

1. ARRAY CREATION:
   - np.array(): From list
   - np.arange(): Range with step
   - np.linspace(): Evenly spaced values
   - np.zeros(), np.ones(), np.eye()
   - np.random functions

2. INDEXING AND SLICING:
   - Zero-based indexing
   - 2D arrays: arr[row, col]
   - Slicing: arr[start:stop:step]
   - Boolean indexing: arr[arr > 5]

3. OPERATIONS:
   - Element-wise: +, -, *, /
   - Matrix operations: @ or np.dot()
   - Broadcasting: automatic dimension expansion

4. AGGREGATION:
   - sum(), mean(), min(), max()
   - std(), var(), median()
   - With axis parameter for 2D arrays

5. RESHAPING:
   - reshape(): Change dimensions
   - flatten(): Convert to 1D
   - T: Transpose

6. BEST PRACTICES:
   - Use NumPy for numerical operations (faster than Python lists)
   - Vectorize code (avoid loops)
   - Use axis parameter for multi-dimensional operations
   - Set random seed for reproducibility
""")
