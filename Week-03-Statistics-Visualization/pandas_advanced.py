"""
Pandas Advanced - GroupBy, Merge, Pivot Tables, and Data Manipulation

This module demonstrates:
- GroupBy operations
- Merging and joining DataFrames
- Pivot tables and reshaping
- Advanced filtering and transformations
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS ADVANCED - GroupBy, Merge, Pivot Tables")
print("=" * 60)

# Create sample data
employees_df = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4, 5, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'Marketing', 'Sales', 'Engineering'],
    'Salary': [95000, 75000, 90000, 85000, 72000, 98000],
    'YearsExperience': [5, 3, 6, 4, 2, 7]
})

print("\nSample Employee Data:")
print(employees_df)

# ============================================================================
# GROUPBY OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("GROUPBY OPERATIONS:")
print("-" * 60)

# Basic groupby
print("\nAverage salary by department:")
dept_avg = employees_df.groupby('Department')['Salary'].mean()
print(dept_avg)

# Multiple aggregations
print("\n\nMultiple aggregations by department:")
dept_stats = employees_df.groupby('Department')['Salary'].agg([
    ('count', 'count'),
    ('mean', 'mean'),
    ('min', 'min'),
    ('max', 'max'),
    ('sum', 'sum')
])
print(dept_stats)

# Group by multiple columns
print("\n\nGroup by department and custom experience level:")
employees_df['ExperienceLevel'] = pd.cut(
    employees_df['YearsExperience'],
    bins=[0, 3, 6, 10],
    labels=['Junior', 'Mid', 'Senior']
)

multi_group = employees_df.groupby(['Department', 'ExperienceLevel']).agg({
    'Salary': ['count', 'mean'],
    'YearsExperience': 'mean'
})
print(multi_group)

# Custom aggregation function
print("\n\nCustom aggregation (salary range):")
def salary_range(group):
    return group.max() - group.min()

salary_ranges = employees_df.groupby('Department')['Salary'].apply(salary_range)
print(salary_ranges)

# Filter groups
print("\n\nDepartments with average salary > $85000:")
high_pay_depts = employees_df.groupby('Department').filter(
    lambda x: x['Salary'].mean() > 85000
)
print(high_pay_depts)

# ============================================================================
# MERGING AND JOINING
# ============================================================================

print("\n" + "=" * 60)
print("MERGING AND JOINING:")
print("-" * 60)

# Create additional DataFrames
departments_df = pd.DataFrame({
    'Department': ['Engineering', 'Sales', 'Marketing'],
    'Budget': [500000, 300000, 200000],
    'Manager': ['John', 'Sarah', 'Mike']
})

projects_df = pd.DataFrame({
    'ProjectID': [101, 102, 103, 104],
    'ProjectName': ['AI Platform', 'Mobile App', 'Web Redesign', 'Data Pipeline'],
    'Department': ['Engineering', 'Engineering', 'Marketing', 'Engineering'],
    'Budget': [100000, 80000, 50000, 120000]
})

print("Departments DataFrame:")
print(departments_df)

print("\n\nProjects DataFrame:")
print(projects_df)

# Inner merge
print("\n\nInner merge (employees with departments):")
inner_merge = employees_df.merge(departments_df, on='Department', how='inner')
print(inner_merge[['Name', 'Department', 'Salary', 'Budget']])

# Left merge
print("\n\nLeft merge (keep all employees):")
left_merge = employees_df.merge(departments_df, on='Department', how='left')
print(left_merge[['Name', 'Department', 'Salary', 'Budget']].drop_duplicates())

# Multiple merges
print("\n\nMultiple merges (employees, departments, budgets):")
merged = employees_df.merge(departments_df, on='Department', how='left')
print(merged[['Name', 'Department', 'Salary', 'Budget_x', 'Manager']].drop_duplicates())

# ============================================================================
# PIVOT TABLES
# ============================================================================

print("\n" + "=" * 60)
print("PIVOT TABLES:")
print("-" * 60)

# Create sales data for pivot examples
sales_data = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=12, freq='MS'),
    'Region': ['North', 'South', 'East', 'West'] * 3,
    'Product': ['A', 'B', 'A', 'B'] * 3,
    'Sales': [10000, 15000, 12000, 18000, 11000, 16000, 13000, 19000,
              14000, 17000, 15000, 20000]
})

print("Sales Data:")
print(sales_data.head(8))

# Basic pivot table
print("\n\nPivot: Sales by Region and Product:")
pivot = pd.pivot_table(
    sales_data,
    values='Sales',
    index='Region',
    columns='Product',
    aggfunc='sum'
)
print(pivot)

# Pivot with multiple values
print("\n\nPivot: Sales count by Region and Product:")
pivot_count = pd.pivot_table(
    sales_data,
    values='Sales',
    index='Region',
    columns='Product',
    aggfunc=['sum', 'mean']
)
print(pivot_count)

# ============================================================================
# RESHAPING DATA
# ============================================================================

print("\n" + "=" * 60)
print("RESHAPING DATA:")
print("-" * 60)

# Stack (wide to long)
print("Original pivot table:")
print(pivot)

print("\n\nStacked (wide to long):")
stacked = pivot.stack()
print(stacked)

# Unstack (long to wide)
print("\n\nUnstacked back:")
unstacked = stacked.unstack()
print(unstacked)

# Melt (convert wide to long format)
wide_data = pd.DataFrame({
    'ID': [1, 2, 3],
    'Q1': [100, 150, 200],
    'Q2': [120, 160, 210],
    'Q3': [140, 170, 220]
})

print("\n\nWide format:")
print(wide_data)

print("\n\nMelted to long format:")
melted = pd.melt(
    wide_data,
    id_vars=['ID'],
    var_name='Quarter',
    value_name='Sales'
)
print(melted)

# ============================================================================
# WINDOW FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("WINDOW FUNCTIONS:")
print("-" * 60)

# Create time series data
ts_data = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=10),
    'Sales': [100, 120, 115, 140, 135, 160, 155, 180, 175, 200]
})

print("Time Series Data:")
print(ts_data)

# Rolling mean
print("\n\n3-period rolling mean:")
ts_data['Rolling_Mean'] = ts_data['Sales'].rolling(window=3).mean()
print(ts_data)

# Cumulative sum
print("\n\nCumulative sum:")
ts_data['Cumsum'] = ts_data['Sales'].cumsum()
print(ts_data)

# Percent change
print("\n\nPercent change:")
ts_data['PctChange'] = ts_data['Sales'].pct_change()
print(ts_data)

# ============================================================================
# STRING OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("STRING OPERATIONS:")
print("-" * 60)

text_data = pd.DataFrame({
    'Name': ['alice johnson', 'bob SMITH', 'charlie brown'],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com']
})

print("Original data:")
print(text_data)

# String methods
print("\n\nString methods:")
text_data['NameUpper'] = text_data['Name'].str.upper()
text_data['NameTitle'] = text_data['Name'].str.title()
text_data['FirstName'] = text_data['Name'].str.split().str[0]
text_data['Domain'] = text_data['Email'].str.split('@').str[1]

print(text_data)

# ============================================================================
# CATEGORICAL DATA
# ============================================================================

print("\n" + "=" * 60)
print("CATEGORICAL DATA:")
print("-" * 60)

cat_data = pd.DataFrame({
    'Color': pd.Categorical(['red', 'blue', 'red', 'green', 'blue'],
                            categories=['red', 'blue', 'green', 'yellow']),
    'Size': pd.Categorical(['S', 'M', 'L', 'M', 'S'],
                           categories=['S', 'M', 'L', 'XL'],
                           ordered=True)
})

print("Categorical Data:")
print(cat_data)
print(f"\nColor categories: {cat_data['Color'].cat.categories.tolist()}")
print(f"Size categories: {cat_data['Size'].cat.categories.tolist()}")
print(f"Size is ordered: {cat_data['Size'].cat.ordered}")

# ============================================================================
# CROSS TABULATION
# ============================================================================

print("\n" + "=" * 60)
print("CROSS TABULATION:")
print("-" * 60)

# Create sample data
survey_data = pd.DataFrame({
    'Age': ['Young', 'Young', 'Old', 'Old', 'Young', 'Old', 'Young', 'Old'],
    'Satisfaction': ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes']
})

print("Survey Data:")
print(survey_data)

print("\n\nCrosstab (Age vs Satisfaction):")
crosstab = pd.crosstab(survey_data['Age'], survey_data['Satisfaction'])
print(crosstab)

print("\n\nCrosstab with margins:")
crosstab_margin = pd.crosstab(survey_data['Age'], survey_data['Satisfaction'],
                              margins=True)
print(crosstab_margin)

# ============================================================================
# PRACTICAL EXAMPLE
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - Sales Analysis Pipeline:")
print("-" * 60)

# Create comprehensive sales dataset
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
sales_df = pd.DataFrame({
    'Date': dates,
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor'], 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Sales': np.random.randint(1000, 5000, 100),
    'Quantity': np.random.randint(1, 20, 100)
})

# Analysis pipeline
print("Step 1: Group by product and get total sales")
product_sales = sales_df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print(product_sales)

print("\n\nStep 2: Add monthly aggregation")
sales_df['Month'] = sales_df['Date'].dt.to_period('M')
monthly_sales = sales_df.groupby('Month').agg({'Sales': 'sum', 'Quantity': 'sum'})
print(monthly_sales.head())

print("\n\nStep 3: Pivot table - Sales by Product and Region")
pivot_result = pd.pivot_table(
    sales_df,
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc='sum'
)
print(pivot_result)

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Pandas Advanced Key Operations:

1. GROUPBY:
   - df.groupby('col').agg()
   - Multiple aggregations
   - Custom aggregation functions
   - Filter groups with .filter()

2. MERGING:
   - df.merge(): SQL-like joins
   - how: 'inner', 'left', 'right', 'outer'
   - on: column name or list of names

3. PIVOT TABLES:
   - pd.pivot_table()
   - index, columns, values, aggfunc
   - Reorganize data efficiently

4. RESHAPING:
   - .stack() / .unstack(): Wide/long
   - .melt(): Unpivot data
   - .reshape() operations

5. WINDOW FUNCTIONS:
   - .rolling(): Moving calculations
   - .cumsum(), .cumprod(): Cumulative
   - .pct_change(): Percent change

6. STRING OPERATIONS:
   - .str accessor for strings
   - .split(), .contains(), .replace()
   - .upper(), .lower(), .title()

7. CATEGORICAL DATA:
   - pd.Categorical() for categories
   - Memory efficient for repeated values

8. CROSS TABULATION:
   - pd.crosstab(): Frequency tables
   - useful for exploratory analysis

9. BEST PRACTICES:
   - Chain operations for readability
   - Use groupby for aggregations
   - Use merge instead of join
   - Categoricals for memory efficiency
""")
