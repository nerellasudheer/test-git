# Python CSV Module - Quick Reference

Reading and writing CSV files.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Reading CSV](#2-reading-csv)
3. [Writing CSV](#3-writing-csv)
4. [DictReader and DictWriter](#4-dictreader-and-dictwriter)
5. [Common Options](#5-common-options)
6. [Quick Reference](#6-quick-reference)

---

## 1. Overview

### What is CSV?

CSV (Comma-Separated Values) is a simple file format for storing tabular data.

### Import

```python
import csv
```

### Sample CSV File

```
name,age,city
Alice,25,New York
Bob,30,Los Angeles
Charlie,35,Chicago
```

---

## 2. Reading CSV

### csv.reader() - Basic Reading

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)  # Each row is a list

# Output:
# ['name', 'age', 'city']
# ['Alice', '25', 'New York']
# ['Bob', '30', 'Los Angeles']
```

### Skip Header Row

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header

    for row in reader:
        name, age, city = row
        print(f"{name} is {age} years old")
```

### Read into List

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

print(data[0])  # Header
print(data[1])  # First data row
```

---

## 3. Writing CSV

### csv.writer() - Basic Writing

```python
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)
```

### writerows() - Write All at Once

```python
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows
```

### Append to CSV

```python
import csv

new_row = ["Charlie", 35, "Chicago"]

with open("output.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)
```

---

## 4. DictReader and DictWriter

### DictReader - Read as Dictionaries

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["age"])

# Access by column name, not index
```

### DictWriter - Write from Dictionaries

```python
import csv

data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"}
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write header row
    writer.writerows(data)
```

### Practical Example

```python
import csv

# Read, process, and write
with open("input.csv", "r") as infile, open("output.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["status"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        row["status"] = "processed"
        writer.writerow(row)
```

---

## 5. Common Options

### Different Delimiters

```python
import csv

# Tab-separated file
with open("data.tsv", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        print(row)

# Semicolon-separated
with open("data.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
```

### Quoting Options

```python
import csv

data = [["name", "description"], ["Item", "A, B, and C"]]

# Quote fields containing special characters
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(data)
```

| Quoting Constant | Description |
|-----------------|-------------|
| `csv.QUOTE_MINIMAL` | Quote only when needed (default) |
| `csv.QUOTE_ALL` | Quote all fields |
| `csv.QUOTE_NONNUMERIC` | Quote non-numeric fields |
| `csv.QUOTE_NONE` | Never quote |

### Handle Different Line Endings

```python
import csv

# Always use newline="" to handle line endings correctly
with open("data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
```

---

## 6. Quick Reference

### Main Classes

| Class | Purpose |
|-------|---------|
| `csv.reader()` | Read rows as lists |
| `csv.writer()` | Write rows from lists |
| `csv.DictReader()` | Read rows as dictionaries |
| `csv.DictWriter()` | Write rows from dictionaries |

### Common Methods

| Method | Purpose |
|--------|---------|
| `reader.__next__()` or `next(reader)` | Get next row |
| `writer.writerow(row)` | Write single row |
| `writer.writerows(rows)` | Write multiple rows |
| `writer.writeheader()` | Write header (DictWriter) |

### Common Options

| Option | Default | Description |
|--------|---------|-------------|
| `delimiter` | `,` | Field separator |
| `quotechar` | `"` | Quote character |
| `quoting` | `QUOTE_MINIMAL` | When to quote |

### Template Patterns

```python
# Read CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        process(row)

# Write CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read as dict
with open("data.csv", "r") as f:
    for row in csv.DictReader(f):
        print(row["column_name"])

# Write from dict
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["col1", "col2"])
    writer.writeheader()
    writer.writerows(data)
```

---

## Coverage Checklist

- [x] csv.reader() basics
- [x] csv.writer() basics
- [x] DictReader and DictWriter
- [x] Skip header
- [x] Different delimiters
- [x] Quoting options
- [x] File handling
- [x] Quick reference
