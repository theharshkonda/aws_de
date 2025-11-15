"""
Pandas DataFrames - Creation, Manipulation, and Exploration

This module demonstrates:
- Creating and loading DataFrames
- Data exploration and inspection
- Selecting and filtering data
- Adding and modifying columns
- Handling missing data
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS DATAFRAMES - Creation and Manipulation")
print("=" * 60)

# ============================================================================
# CREATING DATAFRAMES
# ============================================================================

print("\nCREATING DATAFRAMES:")
print("-" * 60)

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [28, 35, 42, 31],
    'Salary': [75000, 85000, 95000, 82000],
    'Department': ['Engineering', 'Sales', 'Engineering', 'Marketing']
}
df = pd.DataFrame(data)
print("From dictionary:")
print(df)

# From list of dictionaries
employees = [
    {'id': 1, 'name': 'Alice', 'salary': 75000},
    {'id': 2, 'name': 'Bob', 'salary': 85000},
    {'id': 3, 'name': 'Charlie', 'salary': 95000}
]
df2 = pd.DataFrame(employees)
print("\n\nFrom list of dictionaries:")
print(df2)

# From numpy arrays
df3 = pd.DataFrame(
    np.random.randn(4, 3),
    columns=['A', 'B', 'C'],
    index=['row1', 'row2', 'row3', 'row4']
)
print("\n\nFrom NumPy array:")
print(df3)

# ============================================================================
# DATAFRAME INSPECTION
# ============================================================================

print("\n" + "=" * 60)
print("DATAFRAME INSPECTION:")
print("-" * 60)

print("\nDataFrame info:")
print(f"Shape: {df.shape}")  # (rows, columns)
print(f"Size: {df.size}")  # Total elements
print(f"Columns: {list(df.columns)}")
print(f"Index: {list(df.index)}")
print(f"Dtypes:\n{df.dtypes}")

print("\nData types:")
print(df.dtypes)

print("\nBasic statistics:")
print(df.describe())

print("\nFirst 2 rows:")
print(df.head(2))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nInfo about DataFrame:")
df.info()

# ============================================================================
# SELECTING DATA
# ============================================================================

print("\n" + "=" * 60)
print("SELECTING DATA:")
print("-" * 60)

# Select single column
print("Select column 'Name':")
print(df['Name'])
print(f"Type: {type(df['Name'])}")

# Select multiple columns
print("\n\nSelect multiple columns:")
print(df[['Name', 'Age']])

# Select by position (iloc)
print("\n\nSelect first 2 rows:")
print(df.iloc[0:2])

print("\n\nSelect specific cell (row 1, col 2):")
print(f"df.iloc[1, 2]: {df.iloc[1, 2]}")

# Select by label (loc)
print("\n\nSelect by label (loc):")
print(df.loc[0:2, 'Name'])

# ============================================================================
# FILTERING DATA
# ============================================================================

print("\n" + "=" * 60)
print("FILTERING DATA:")
print("-" * 60)

# Filter by condition
print("Employees with salary > 80000:")
high_earners = df[df['Salary'] > 80000]
print(high_earners)

# Multiple conditions
print("\n\nEngineers earning > 80000:")
engineers_high = df[(df['Department'] == 'Engineering') & (df['Salary'] > 80000)]
print(engineers_high)

# Using isin()
print("\n\nEmployees in Engineering or Sales:")
print(df[df['Department'].isin(['Engineering', 'Sales'])])

# Using str methods
print("\n\nNames starting with 'C':")
print(df[df['Name'].str.startswith('C')])

# ============================================================================
# ADDING AND MODIFYING COLUMNS
# ============================================================================

print("\n" + "=" * 60)
print("ADDING AND MODIFYING COLUMNS:")
print("-" * 60)

df_copy = df.copy()

# Add new column
df_copy['Bonus'] = df_copy['Salary'] * 0.1
print("Added Bonus column:")
print(df_copy)

# Modify existing column
df_copy['Salary'] = df_copy['Salary'] * 1.05
print("\n\nAfter 5% salary increase:")
print(df_copy)

# Add column based on condition
df_copy['Level'] = df_copy['Salary'].apply(
    lambda x: 'Senior' if x > 85000 else 'Junior'
)
print("\n\nAdded Level column:")
print(df_copy)

# Using map for categorical
level_map = {28: 'Junior', 35: 'Mid', 42: 'Senior', 31: 'Mid'}
df_copy['AgeGroup'] = df_copy['Age'].map(level_map)
print("\n\nAdded AgeGroup using map:")
print(df_copy)

# ============================================================================
# MISSING DATA
# ============================================================================

print("\n" + "=" * 60)
print("HANDLING MISSING DATA:")
print("-" * 60)

# Create DataFrame with missing values
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

print("DataFrame with missing values:")
print(df_missing)

print("\n\nCheck for missing values:")
print(df_missing.isnull())

print("\n\nCount missing values:")
print(df_missing.isnull().sum())

# Drop rows with missing values
print("\n\nAfter dropna():")
print(df_missing.dropna())

# Fill missing values
print("\n\nAfter fillna(0):")
print(df_missing.fillna(0))

print("\n\nForward fill (propagate values forward):")
print(df_missing.fillna(method='ffill'))

# ============================================================================
# SORTING AND RANKING
# ============================================================================

print("\n" + "=" * 60)
print("SORTING AND RANKING:")
print("-" * 60)

print("Original DataFrame:")
print(df)

print("\n\nSorted by Salary (ascending):")
print(df.sort_values('Salary'))

print("\n\nSorted by Salary (descending):")
print(df.sort_values('Salary', ascending=False))

print("\n\nMultiple column sort:")
print(df.sort_values(['Department', 'Salary']))

print("\n\nRank by salary:")
print(df['Salary'].rank())

# ============================================================================
# DUPLICATE HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("DUPLICATE HANDLING:")
print("-" * 60)

df_dup = pd.DataFrame({
    'A': [1, 2, 2, 3, 3, 3],
    'B': ['x', 'y', 'y', 'z', 'z', 'z']
})

print("DataFrame with duplicates:")
print(df_dup)

print("\n\nCheck duplicates:")
print(df_dup.duplicated())

print("\n\nAfter drop_duplicates():")
print(df_dup.drop_duplicates())

# ============================================================================
# CONCATENATION AND MERGING
# ============================================================================

print("\n" + "=" * 60)
print("CONCATENATION AND MERGING:")
print("-" * 60)

# Create sample DataFrames
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['A', 'B', 'D'],
    'value2': [4, 5, 6]
})

print("DataFrame 1:")
print(df1)
print("\n\nDataFrame 2:")
print(df2)

# Concatenate (row-wise)
print("\n\nConcatenate (row-wise):")
concat_df = pd.concat([df1, df2], ignore_index=True)
print(concat_df)

# Merge (join on key)
print("\n\nMerge on 'key' (inner join):")
merged = df1.merge(df2, on='key', how='inner')
print(merged)

print("\n\nMerge on 'key' (left join):")
merged_left = df1.merge(df2, on='key', how='left')
print(merged_left)

# ============================================================================
# PRACTICAL EXAMPLE
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - Sales Data Analysis:")
print("-" * 60)

# Create sample sales data
sales_data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse'],
    'Region': ['North', 'South', 'North', 'East', 'South', 'East'],
    'Quarter': ['Q1', 'Q1', 'Q2', 'Q2', 'Q1', 'Q2'],
    'Sales': [15000, 2000, 3000, 8000, 18000, 2500]
}

sales_df = pd.DataFrame(sales_data)
print("Sales Data:")
print(sales_df)

# Analysis
print("\n\nTotal sales by product:")
print(sales_df.groupby('Product')['Sales'].sum())

print("\n\nTotal sales by region:")
print(sales_df.groupby('Region')['Sales'].sum())

print("\n\nAverage sales by quarter:")
print(sales_df.groupby('Quarter')['Sales'].mean())

# Add derived column
sales_df['Category'] = sales_df['Sales'].apply(
    lambda x: 'High' if x > 5000 else 'Low'
)

print("\n\nWith Category column:")
print(sales_df)

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Pandas DataFrame Key Operations:

1. CREATION:
   - From dict: pd.DataFrame(data)
   - From list of dicts: pd.DataFrame([{}, {}])
   - From NumPy arrays: pd.DataFrame(array)
   - From CSV: pd.read_csv('file.csv')

2. INSPECTION:
   - df.head(), df.tail()
   - df.shape, df.size
   - df.info(), df.describe()
   - df.dtypes

3. SELECTION:
   - df['column']: Single column (Series)
   - df[['col1', 'col2']]: Multiple columns
   - df.iloc[row, col]: By position
   - df.loc[row, col]: By label

4. FILTERING:
   - df[condition]: Boolean indexing
   - df[df['col'] > value]
   - df.isin(), df.str methods

5. MODIFICATION:
   - df['new'] = values: Add column
   - df['col'].apply(func): Transform
   - df['col'].map(dict): Remap values

6. MISSING DATA:
   - df.isnull(), df.notnull()
   - df.dropna(): Remove missing
   - df.fillna(value): Fill missing

7. GROUPING AND AGGREGATION:
   - df.groupby('col').agg()
   - .sum(), .mean(), .count()

8. BEST PRACTICES:
   - Use copy() to avoid warnings
   - Use inplace=False by default
   - Chain operations for readability
   - Use apply/map for transformations
""")
