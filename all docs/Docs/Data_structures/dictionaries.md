# Python Dictionaries - Complete Guide

A comprehensive reference guide for Python Dictionaries.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Creating Dictionaries](#2-creating-dictionaries)
3. [Accessing Values](#3-accessing-values)
4. [Dictionary Methods](#4-dictionary-methods)
5. [Iterating Through Dictionaries](#5-iterating-through-dictionaries)
6. [Nested Dictionaries](#6-nested-dictionaries)
7. [Dictionary Comprehensions](#7-dictionary-comprehensions)
8. [Common Mistakes](#8-common-mistakes)
9. [Best Practices](#9-best-practices)
10. [Quick Reference](#10-quick-reference)

---

## 1. Overview

### What is a Dictionary?

A dictionary is an **unordered** (ordered in Python 3.7+), **mutable** collection of key-value pairs. Each key must be unique and immutable, while values can be of any type.

### Key Characteristics

| Feature | Description |
|---------|-------------|
| Key-Value Pairs | Data stored as `key: value` |
| Mutable | Can add, remove, modify items |
| Keys Must Be Unique | Duplicate keys not allowed |
| Keys Must Be Immutable | Strings, numbers, tuples only |
| Values Can Be Any Type | Including other dictionaries |
| Ordered (Python 3.7+) | Maintains insertion order |

### Dictionary vs Other Data Structures

| Feature | Dictionary | List | Set |
|---------|------------|------|-----|
| Access by | Key | Index | N/A |
| Ordered | Yes (3.7+) | Yes | No |
| Mutable | Yes | Yes | Yes |
| Duplicates | Keys: No | Yes | No |
| Use case | Key-value mapping | Ordered collection | Unique items |

---

## 2. Creating Dictionaries

### Basic Creation

```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with values
student = {"name": "Alice", "age": 20, "major": "CS"}

# Using dict() constructor with keyword arguments
student = dict(name="Alice", age=20, major="CS")

# From list of tuples
items = dict([("a", 1), ("b", 2), ("c", 3)])
print(items)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

### Creating with Default Values

```python
# Using fromkeys() - all keys get same value
keys = ["a", "b", "c"]
my_dict = dict.fromkeys(keys, 0)
print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# Without default value (None)
my_dict = dict.fromkeys(keys)
print(my_dict)  # Output: {'a': None, 'b': None, 'c': None}
```

---

## 3. Accessing Values

### Using Square Brackets []

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

# Access existing key
print(student["name"])  # Output: Alice

# KeyError if key doesn't exist
# print(student["grade"])  # KeyError: 'grade'
```

### Using get() Method (Safer)

```python
student = {"name": "Alice", "age": 20}

# Returns value if key exists
print(student.get("name"))  # Output: Alice

# Returns None if key doesn't exist (no error)
print(student.get("grade"))  # Output: None

# Returns default value if key doesn't exist
print(student.get("grade", "N/A"))  # Output: N/A
```

### Checking Key Existence

```python
student = {"name": "Alice", "age": 20}

# Using 'in' operator (checks keys, not values)
print("name" in student)    # Output: True
print("grade" in student)   # Output: False
print("Alice" in student)   # Output: False (checks keys only!)

# Check in values
print("Alice" in student.values())  # Output: True
```

---

## 4. Dictionary Methods

### Adding and Updating

#### Direct Assignment

```python
student = {"name": "Alice"}

# Add new key-value pair
student["age"] = 20
print(student)  # Output: {'name': 'Alice', 'age': 20}

# Update existing value
student["age"] = 21
print(student)  # Output: {'name': 'Alice', 'age': 21}
```

---

#### update()

**Purpose**: Updates dictionary with key-value pairs from another dictionary or iterable.

```python
student = {"name": "Alice", "age": 20}

# Update with another dictionary
student.update({"age": 21, "major": "CS"})
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'CS'}

# Update with keyword arguments
student.update(gpa=3.8, year=2)
print(student)  # Output: {..., 'gpa': 3.8, 'year': 2}
```

**Note**: Existing keys are overwritten, new keys are added.

---

#### setdefault()

**Purpose**: Returns value if key exists. If not, inserts key with default value and returns it.

```python
student = {"name": "Alice"}

# Key exists - returns existing value
result = student.setdefault("name", "Unknown")
print(result)   # Output: Alice
print(student)  # Output: {'name': 'Alice'}

# Key doesn't exist - adds it with default value
result = student.setdefault("age", 20)
print(result)   # Output: 20
print(student)  # Output: {'name': 'Alice', 'age': 20}
```

---

### Removing Items

#### pop()

**Purpose**: Removes and returns value for specified key.

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

# Remove and get value
age = student.pop("age")
print(age)      # Output: 20
print(student)  # Output: {'name': 'Alice', 'major': 'CS'}

# With default value (no error if key missing)
grade = student.pop("grade", "N/A")
print(grade)    # Output: N/A

# Without default - raises KeyError if key missing
# student.pop("grade")  # KeyError: 'grade'
```

---

#### popitem()

**Purpose**: Removes and returns the last inserted key-value pair (LIFO).

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

# Remove last item
last_item = student.popitem()
print(last_item)  # Output: ('major', 'CS')
print(student)    # Output: {'name': 'Alice', 'age': 20}
```

---

#### del

**Purpose**: Deletes a key-value pair or entire dictionary.

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

# Delete specific key
del student["age"]
print(student)  # Output: {'name': 'Alice', 'major': 'CS'}

# Delete entire dictionary
# del student
# print(student)  # NameError: name 'student' is not defined
```

---

#### clear()

**Purpose**: Removes all items from the dictionary.

```python
student = {"name": "Alice", "age": 20}
student.clear()
print(student)  # Output: {}
```

---

### Viewing Items

#### keys()

**Purpose**: Returns a view object of all keys.

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

keys = student.keys()
print(keys)        # Output: dict_keys(['name', 'age', 'major'])
print(list(keys))  # Output: ['name', 'age', 'major']
```

---

#### values()

**Purpose**: Returns a view object of all values.

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

values = student.values()
print(values)        # Output: dict_values(['Alice', 20, 'CS'])
print(list(values))  # Output: ['Alice', 20, 'CS']
```

---

#### items()

**Purpose**: Returns a view object of all key-value pairs as tuples.

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

items = student.items()
print(items)        # Output: dict_items([('name', 'Alice'), ('age', 20), ('major', 'CS')])
print(list(items))  # Output: [('name', 'Alice'), ('age', 20), ('major', 'CS')]
```

**Note**: View objects are dynamic - they reflect changes to the dictionary.

```python
student = {"name": "Alice"}
keys = student.keys()
student["age"] = 20
print(keys)  # Output: dict_keys(['name', 'age']) - Updated automatically!
```

---

#### get()

**Purpose**: Returns value for key, or default if key doesn't exist.

```python
student = {"name": "Alice", "age": 20}

print(student.get("name"))         # Output: Alice
print(student.get("grade"))        # Output: None
print(student.get("grade", "N/A")) # Output: N/A
```

---

#### copy()

**Purpose**: Returns a shallow copy of the dictionary.

```python
original = {"name": "Alice", "age": 20}
copied = original.copy()

copied["age"] = 21
print(original)  # Output: {'name': 'Alice', 'age': 20} - Unchanged
print(copied)    # Output: {'name': 'Alice', 'age': 21}
```

---

## 5. Iterating Through Dictionaries

### Iterating Over Keys (Default)

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

# Method 1: Direct iteration
for key in student:
    print(key)
# Output: name, age, major

# Method 2: Using keys()
for key in student.keys():
    print(key)
```

### Iterating Over Values

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

for value in student.values():
    print(value)
# Output: Alice, 20, CS
```

### Iterating Over Key-Value Pairs

```python
student = {"name": "Alice", "age": 20, "major": "CS"}

for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 20
# major: CS
```

---

## 6. Nested Dictionaries

### Creating Nested Dictionaries

```python
# Students with nested information
students = {
    "alice": {
        "name": "Alice Smith",
        "grades": {"math": 90, "english": 85},
        "courses": ["CS101", "MATH201"]
    },
    "bob": {
        "name": "Bob Jones",
        "grades": {"math": 78, "english": 92},
        "courses": ["CS101", "ENG102"]
    }
}
```

### Accessing Nested Values

```python
# Get Alice's math grade
print(students["alice"]["grades"]["math"])  # Output: 90

# Get Bob's first course
print(students["bob"]["courses"][0])  # Output: CS101

# Safe access with get()
print(students.get("charlie", {}).get("name", "Unknown"))  # Output: Unknown
```

### Modifying Nested Values

```python
# Update Alice's math grade
students["alice"]["grades"]["math"] = 95

# Add new course to Bob
students["bob"]["courses"].append("PHYS101")
```

### Real-World Example: API Response

```python
api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@email.com"},
            {"id": 2, "name": "Bob", "email": "bob@email.com"}
        ],
        "total": 2
    }
}

# Get first user's email
print(api_response["data"]["users"][0]["email"])  # Output: alice@email.com

# Get total users
print(api_response["data"]["total"])  # Output: 2
```

---

## 7. Dictionary Comprehensions

### Basic Syntax

```python
# {key_expression: value_expression for item in iterable}
```

### Examples

```python
# Create dictionary from range
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform existing dictionary
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
discounted = {k: v * 0.9 for k, v in prices.items()}
print(discounted)  # Output: {'apple': 0.9, 'banana': 0.45, 'cherry': 1.8}
```

---

## 8. Common Mistakes

### Mistake 1: Using [] Instead of get() for Missing Keys

```python
student = {"name": "Alice"}

# WRONG - Raises KeyError
# print(student["grade"])  # KeyError: 'grade'

# CORRECT - Returns default value
print(student.get("grade", "N/A"))  # Output: N/A
```

### Mistake 2: Using Mutable Objects as Keys

```python
# WRONG - Lists are mutable, can't be keys
# my_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# CORRECT - Use tuples (immutable)
my_dict = {(1, 2): "value"}
print(my_dict[(1, 2)])  # Output: value
```

### Mistake 3: Modifying Dictionary While Iterating

```python
# WRONG - RuntimeError: dictionary changed size during iteration
# for key in my_dict:
#     if some_condition:
#         del my_dict[key]

# CORRECT - Iterate over a copy of keys
my_dict = {"a": 1, "b": 2, "c": 3}
for key in list(my_dict.keys()):
    if my_dict[key] < 2:
        del my_dict[key]
print(my_dict)  # Output: {'b': 2, 'c': 3}
```

### Mistake 4: Shallow Copy with Nested Dictionaries

```python
import copy

original = {"user": {"name": "Alice"}}

# WRONG - Shallow copy, nested dict is shared
shallow = original.copy()
shallow["user"]["name"] = "Bob"
print(original)  # Output: {'user': {'name': 'Bob'}} - Changed!

# CORRECT - Deep copy for nested structures
original = {"user": {"name": "Alice"}}
deep = copy.deepcopy(original)
deep["user"]["name"] = "Bob"
print(original)  # Output: {'user': {'name': 'Alice'}} - Unchanged
```

---

## 9. Best Practices

### 1. Use get() for Safe Access

```python
# Instead of:
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = default

# Use:
value = my_dict.get("key", default)
```

### 2. Use setdefault() for Default Initialization

```python
# Instead of:
if "key" not in my_dict:
    my_dict["key"] = []
my_dict["key"].append(value)

# Use:
my_dict.setdefault("key", []).append(value)
```

### 3. Use Dictionary Comprehensions

```python
# Instead of:
result = {}
for item in items:
    result[item.key] = item.value

# Use:
result = {item.key: item.value for item in items}
```

### 4. Use items() for Key-Value Iteration

```python
# Instead of:
for key in my_dict:
    value = my_dict[key]
    print(key, value)

# Use:
for key, value in my_dict.items():
    print(key, value)
```

---

## 10. Quick Reference

### Methods Summary

| Method | Purpose | Returns |
|--------|---------|---------|
| `get(key, default)` | Get value safely | Value or default |
| `keys()` | Get all keys | dict_keys view |
| `values()` | Get all values | dict_values view |
| `items()` | Get key-value pairs | dict_items view |
| `update(other)` | Add/update from another dict | None |
| `setdefault(key, default)` | Get or set default | Value |
| `pop(key, default)` | Remove and return | Value |
| `popitem()` | Remove last item | (key, value) tuple |
| `clear()` | Remove all items | None |
| `copy()` | Shallow copy | dict |
| `fromkeys(keys, value)` | Create with keys | dict |

### Operations

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Access | `dict[key]` or `dict.get(key)` | Get value |
| Add/Update | `dict[key] = value` | Set value |
| Delete | `del dict[key]` | Remove item |
| Membership | `key in dict` | Check if key exists |
| Length | `len(dict)` | Count items |

### Creating Dictionaries

| Method | Example |
|--------|---------|
| Literal | `{"a": 1, "b": 2}` |
| Constructor | `dict(a=1, b=2)` |
| From tuples | `dict([("a", 1), ("b", 2)])` |
| Comprehension | `{x: x**2 for x in range(5)}` |
| fromkeys | `dict.fromkeys(["a", "b"], 0)` |

---

## Coverage Checklist

- [x] Creating dictionaries (all methods)
- [x] Accessing values ([], get)
- [x] All dictionary methods documented
- [x] Iterating (keys, values, items)
- [x] Nested dictionaries with examples
- [x] Dictionary comprehensions
- [x] Common mistakes explained
- [x] Best practices
- [x] Quick reference tables
