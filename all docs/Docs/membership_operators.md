# Python Membership Operators - Quick Reference

Understanding `in` and `not in` operators in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [in Operator](#2-in-operator)
3. [not in Operator](#3-not-in-operator)
4. [With Different Data Types](#4-with-different-data-types)
5. [Quick Reference](#5-quick-reference)

---

## 1. Overview

### What are Membership Operators?

Membership operators test whether a value exists in a sequence (string, list, tuple, set, or dictionary).

### The Two Operators

| Operator | Meaning | Returns |
|----------|---------|---------|
| `in` | Returns `True` if value is present | Boolean |
| `not in` | Returns `True` if value is NOT present | Boolean |

---

## 2. in Operator

### Basic Usage

```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)     # True
print("grape" in fruits)     # False
```

### With Strings

```python
text = "Hello World"

print("Hello" in text)       # True
print("hello" in text)       # False (case-sensitive!)
print("World" in text)       # True
```

---

## 3. not in Operator

### Basic Usage

```python
text = "hello world"

print("hello" not in text)   # False (because 'hello' exists)
print("bye" not in text)     # True
```

### With Lists

```python
numbers = [1, 2, 3, 4, 5]

print(6 not in numbers)      # True
print(3 not in numbers)      # False
```

---

## 4. With Different Data Types

### With Strings

```python
message = "Python is awesome"

print("Python" in message)       # True
print("python" in message)       # False (case-sensitive)
print("Java" not in message)     # True
```

### With Lists

```python
colors = ["red", "green", "blue"]

print("red" in colors)           # True
print("yellow" in colors)        # False
print("yellow" not in colors)    # True
```

### With Tuples

```python
coordinates = (10, 20, 30)

print(20 in coordinates)         # True
print(50 in coordinates)         # False
```

### With Sets

```python
unique_numbers = {1, 2, 3, 4, 5}

print(3 in unique_numbers)       # True
print(6 in unique_numbers)       # False
```

### With Dictionaries

**Important**: `in` checks **keys only**, not values (by default).

```python
student = {"name": "Alice", "age": 22}

print("name" in student)         # True  (key exists)
print("Alice" in student)        # False (value not checked)
print("grade" not in student)    # True

# To check values:
print("Alice" in student.values())   # True
```

---

## 5. Quick Reference

### Summary Table

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `in` | Checks if element exists | `'a' in 'apple'` | `True` |
| `not in` | Checks if element doesn't exist | `'x' not in 'apple'` | `True` |

### Key Points to Remember

| Point | Description |
|-------|-------------|
| Works with | Strings, lists, tuples, sets, dictionaries |
| Case-sensitive | `'A' in 'apple'` → `False` |
| Dictionaries | Checks keys only (use `.values()` for values) |
| Returns | Boolean (`True` or `False`) |

### Practical Examples

```python
# Check before accessing
if "key" in my_dict:
    print(my_dict["key"])

# Filter items
allowed_users = ["admin", "editor", "viewer"]
user = "admin"
if user in allowed_users:
    print("Access granted")

# Search in string
email = "user@example.com"
if "@" in email:
    print("Valid email format")

# Check for absence
blacklist = ["spam", "virus", "malware"]
filename = "document.pdf"
if filename not in blacklist:
    print("File is safe")
```

### With Loops and Conditions

```python
# Using in with if statement
fruits = ["apple", "banana", "cherry"]
search = "banana"

if search in fruits:
    print(f"{search} is in the list")
else:
    print(f"{search} is not in the list")

# Using in with for loop
text = "hello"
for char in text:
    if char in "aeiou":
        print(f"{char} is a vowel")
```

---

## Coverage Checklist

- [x] Definition of membership operators
- [x] `in` operator usage
- [x] `not in` operator usage
- [x] Usage with different data types
- [x] Dictionary key vs value checking
- [x] Case sensitivity note
- [x] Practical examples
- [x] Quick reference table
