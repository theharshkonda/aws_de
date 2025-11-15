"""
File Handling - Reading/Writing CSV, JSON, and Text Files

This module demonstrates:
- Working with text files
- Reading and writing CSV files
- Reading and writing JSON files
- File management and error handling
- Working with file paths
"""

import csv
import json
import os
from pathlib import Path

# ============================================================================
# SETUP - Create sample files for demonstration
# ============================================================================

print("=" * 60)
print("FILE HANDLING - CSV, JSON, and Text Files")
print("=" * 60)

# Create sample data directory
sample_dir = "/tmp/data_samples"
os.makedirs(sample_dir, exist_ok=True)

# ============================================================================
# WORKING WITH TEXT FILES
# ============================================================================

print("\n" + "=" * 60)
print("WORKING WITH TEXT FILES")
print("=" * 60)

# Write to text file
text_file = f"{sample_dir}/sample.txt"
try:
    with open(text_file, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a text file.\n")
        file.write("Python makes file handling easy.\n")
    print(f"Created text file: {text_file}")
except IOError as e:
    print(f"Error writing file: {e}")

# Read entire file
print("\nReading entire file:")
try:
    with open(text_file, 'r') as file:
        content = file.read()
        print(f"Content:\n{content}")
except IOError as e:
    print(f"Error reading file: {e}")

# Read line by line
print("Reading line by line:")
try:
    with open(text_file, 'r') as file:
        for line_num, line in enumerate(file, 1):
            print(f"  Line {line_num}: {line.rstrip()}")
except IOError as e:
    print(f"Error reading file: {e}")

# Read all lines into a list
print("\nReading all lines into list:")
try:
    with open(text_file, 'r') as file:
        lines = file.readlines()
        print(f"Lines: {lines}")
except IOError as e:
    print(f"Error reading file: {e}")

# Append to file
print("\nAppending to file:")
try:
    with open(text_file, 'a') as file:
        file.write("This line was appended.\n")
    print("Line appended successfully")
except IOError as e:
    print(f"Error appending: {e}")

# ============================================================================
# WORKING WITH CSV FILES
# ============================================================================

print("\n" + "=" * 60)
print("WORKING WITH CSV FILES")
print("=" * 60)

# Write to CSV file
csv_file = f"{sample_dir}/employees.csv"
try:
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['ID', 'Name', 'Department', 'Salary'])
        # Write data rows
        writer.writerow([1, 'Alice Johnson', 'Engineering', 120000])
        writer.writerow([2, 'Bob Smith', 'Marketing', 90000])
        writer.writerow([3, 'Charlie Brown', 'Sales', 85000])
        writer.writerow([4, 'Diana Prince', 'Engineering', 130000])
    print(f"Created CSV file: {csv_file}")
except IOError as e:
    print(f"Error writing CSV: {e}")

# Read CSV file (simple reading)
print("\nReading CSV file (simple):")
try:
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row_num, row in enumerate(reader, 1):
            print(f"  Row {row_num}: {row}")
except IOError as e:
    print(f"Error reading CSV: {e}")

# Read CSV file with DictReader (more practical)
print("\nReading CSV file with DictReader:")
try:
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"  {row['Name']} - {row['Department']} (${row['Salary']})")
except IOError as e:
    print(f"Error reading CSV: {e}")

# Create CSV with different delimiter
csv_file_tsv = f"{sample_dir}/data.tsv"
try:
    with open(csv_file_tsv, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Column1', 'Column2', 'Column3'])
        writer.writerow(['A', 'B', 'C'])
        writer.writerow(['D', 'E', 'F'])
    print(f"Created TSV file: {csv_file_tsv}")
except IOError as e:
    print(f"Error writing TSV: {e}")

# ============================================================================
# WORKING WITH JSON FILES
# ============================================================================

print("\n" + "=" * 60)
print("WORKING WITH JSON FILES")
print("=" * 60)

# Create sample data
students_data = {
    "students": [
        {
            "id": 101,
            "name": "Alice",
            "age": 20,
            "grades": [85, 90, 88],
            "active": True
        },
        {
            "id": 102,
            "name": "Bob",
            "age": 21,
            "grades": [92, 88, 95],
            "active": True
        },
        {
            "id": 103,
            "name": "Charlie",
            "age": 20,
            "grades": [78, 82, 80],
            "active": False
        }
    ]
}

# Write to JSON file
json_file = f"{sample_dir}/students.json"
try:
    with open(json_file, 'w') as file:
        json.dump(students_data, file, indent=2)
    print(f"Created JSON file: {json_file}")
except IOError as e:
    print(f"Error writing JSON: {e}")

# Read from JSON file
print("\nReading JSON file:")
try:
    with open(json_file, 'r') as file:
        data = json.load(file)
        print(f"Loaded data:")
        for student in data['students']:
            avg_grade = sum(student['grades']) / len(student['grades'])
            print(f"  {student['name']}: Average = {avg_grade:.1f}")
except IOError as e:
    print(f"Error reading JSON: {e}")

# Working with JSON strings
print("\nWorking with JSON strings:")
json_string = '{"name": "David", "age": 22, "city": "New York"}'
parsed = json.loads(json_string)
print(f"Parsed from string: {parsed}")

# Convert Python object to JSON string
python_dict = {"product": "Laptop", "price": 1200, "in_stock": True}
json_string = json.dumps(python_dict, indent=2)
print(f"Converted to JSON string:\n{json_string}")

# ============================================================================
# FILE OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("FILE OPERATIONS")
print("=" * 60)

# Check if file exists
test_file = f"{sample_dir}/test.txt"
print(f"\nFile exists: {os.path.exists(test_file)}")

# Get file size
sample_file = f"{sample_dir}/employees.csv"
if os.path.exists(sample_file):
    file_size = os.path.getsize(sample_file)
    print(f"File size: {file_size} bytes")

# Get file modification time
if os.path.exists(sample_file):
    import time
    mod_time = os.path.getmtime(sample_file)
    print(f"Last modified: {time.ctime(mod_time)}")

# List files in directory
print(f"\nFiles in {sample_dir}:")
if os.path.exists(sample_dir):
    for filename in os.listdir(sample_dir):
        filepath = os.path.join(sample_dir, filename)
        if os.path.isfile(filepath):
            print(f"  - {filename}")

# Using pathlib (modern approach)
print("\nUsing pathlib:")
path = Path(sample_dir)
print(f"Directory exists: {path.exists()}")
print(f"Is directory: {path.is_dir()}")

# Iterate with pathlib
print(f"Files in {sample_dir} (using pathlib):")
for file_path in path.glob('*'):
    if file_path.is_file():
        print(f"  - {file_path.name} ({file_path.stat().st_size} bytes)")

# ============================================================================
# ERROR HANDLING
# ============================================================================

print("\n" + "=" * 60)
print("ERROR HANDLING IN FILE OPERATIONS")
print("=" * 60)

# FileNotFoundError
print("\nHandling FileNotFoundError:")
try:
    with open(f"{sample_dir}/nonexistent.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("  Error: File not found")

# PermissionError
print("\nHandling PermissionError:")
try:
    # Try to read a file we may not have permission for
    with open("/root/protected.txt", 'r') as file:
        content = file.read()
except PermissionError:
    print("  Error: Permission denied")
except FileNotFoundError:
    print("  Error: File not found")

# IOError (general)
print("\nHandling general IOError:")
try:
    with open(f"{sample_dir}/test.txt", 'r') as file:
        content = file.read()
    print("  File read successfully")
except IOError as e:
    print(f"  Error: {e}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Read CSV and filter data
print("\nExample 1: Read CSV and filter Engineering employees")
try:
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        engineers = [row for row in reader if row['Department'] == 'Engineering']
        for engineer in engineers:
            print(f"  {engineer['Name']}: ${engineer['Salary']}")
except IOError as e:
    print(f"  Error: {e}")

# Example 2: Convert CSV to JSON
print("\nExample 2: Convert CSV to JSON format")
csv_to_json_file = f"{sample_dir}/employees.json"
try:
    data = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                'id': int(row['ID']),
                'name': row['Name'],
                'department': row['Department'],
                'salary': int(row['Salary'])
            })

    with open(csv_to_json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)
    print(f"  Converted and saved to {csv_to_json_file}")
except Exception as e:
    print(f"  Error: {e}")

# Example 3: Write log file with timestamp
print("\nExample 3: Writing log file")
log_file = f"{sample_dir}/app.log"
try:
    from datetime import datetime
    with open(log_file, 'w') as file:
        for i in range(3):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] Log entry {i+1}: Application started\n")
    print(f"  Log file created: {log_file}")
except IOError as e:
    print(f"  Error: {e}")

# Example 4: Parse JSON and summarize data
print("\nExample 4: Parse JSON and summarize")
try:
    with open(json_file, 'r') as file:
        data = json.load(file)
        total_students = len(data['students'])
        avg_age = sum(s['age'] for s in data['students']) / total_students
        active_count = sum(1 for s in data['students'] if s['active'])
        print(f"  Total students: {total_students}")
        print(f"  Average age: {avg_age:.1f}")
        print(f"  Active students: {active_count}")
except IOError as e:
    print(f"  Error: {e}")

# ============================================================================
# CONTEXT MANAGERS
# ============================================================================

print("\n" + "=" * 60)
print("CONTEXT MANAGERS (with statement)")
print("=" * 60)

print("""
Benefits of using 'with' statement:
1. Automatically closes file when done
2. Handles exceptions properly
3. More readable code
4. No need for try/finally

Example:
    with open('file.txt', 'r') as file:
        content = file.read()
    # File is automatically closed here

Instead of:
    file = open('file.txt', 'r')
    try:
        content = file.read()
    finally:
        file.close()
""")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
File Handling Modes:
- 'r': Read (default)
- 'w': Write (overwrites)
- 'a': Append
- 'x': Create new file
- 'b': Binary mode
- '+': Read and write

Text File Operations:
- file.read(): Read entire file
- file.readline(): Read one line
- file.readlines(): Read all lines as list
- file.write(): Write string
- file.writelines(): Write multiple lines

CSV Operations:
- csv.reader(): Read CSV
- csv.writer(): Write CSV
- csv.DictReader(): Read as dictionaries
- csv.DictWriter(): Write dictionaries

JSON Operations:
- json.load(): Read JSON from file
- json.dump(): Write JSON to file
- json.loads(): Parse JSON string
- json.dumps(): Convert to JSON string

Best Practices:
1. Always use 'with' statement (context manager)
2. Handle exceptions (IOError, FileNotFoundError, etc.)
3. Use pathlib for modern file path handling
4. Specify encoding when needed (default: UTF-8)
5. Close files properly (automatic with 'with')
6. Use newline='' when writing CSV
7. Use indent parameter in JSON for readability

Common Encodings:
- 'utf-8': Most common (default)
- 'ascii': Plain ASCII text
- 'latin-1': Western European
- 'cp1252': Windows encoding
""")

print("\n" + "=" * 60)
print("Sample files created in:", sample_dir)
print("=" * 60)
