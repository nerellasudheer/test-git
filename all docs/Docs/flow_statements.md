# Python Control Flow Statements - Complete Guide

A comprehensive reference for Python's control flow and statement keywords.

---

## Table of Contents

1. [Overview](#1-overview)
2. [pass Statement](#2-pass-statement)
3. [return Statement](#3-return-statement)
4. [break Statement](#4-break-statement)
5. [continue Statement](#5-continue-statement)
6. [yield Statement](#6-yield-statement)
7. [raise Statement](#7-raise-statement)
8. [assert Statement](#8-assert-statement)
9. [with Statement](#9-with-statement)
10. [del Statement](#10-del-statement)
11. [global and nonlocal](#11-global-and-nonlocal)
12. [print() end Parameter](#12-print-end-parameter)
13. [Quick Reference](#13-quick-reference)

---

## 1. Overview

### What are Control Flow Statements?

Control flow statements are keywords that control the execution flow of your program. They determine how and when code blocks are executed.

---

## 2. pass Statement

### Definition

A null statement that does nothing. Used as a placeholder when a statement is syntactically required.

### Usage

```python
# Empty function placeholder
def future_function():
    pass  # Will implement later

# Empty class
class MyClass:
    pass

# Conditional with no action needed
for i in range(10):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(i)

# Exception handling placeholder
try:
    risky_operation()
except ValueError:
    pass  # Ignore this error silently
```

---

## 3. return Statement

### Definition

Exits a function and optionally sends a value back to the caller.

### Usage

```python
# Return a value
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8

# Return without value (returns None)
def greet(name):
    print(f"Hello, {name}")
    return  # Function ends here

# Early return based on condition
def divide(a, b):
    if b == 0:
        return None  # Exit early if invalid
    return a / b

# Return multiple values
def get_user_info():
    return "John", 25, "Engineer"

name, age, job = get_user_info()
```

---

## 4. break Statement

### Definition

Immediately exits the innermost loop (for or while). No further iterations are executed.

### Usage

```python
# Exit loop when condition met
for i in range(10):
    if i == 5:
        break  # Loop stops at 5
    print(i)
# Output: 0, 1, 2, 3, 4

# Search and exit when found
numbers = [1, 3, 5, 7, 9, 2, 4]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break  # Stop searching

# Exit infinite loop
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
```

---

## 5. continue Statement

### Definition

Skips the rest of the current iteration and moves to the next iteration of the loop.

### Usage

```python
# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip rest of loop for even numbers
    print(i)
# Output: 1, 3, 5, 7, 9

# Skip invalid data
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print(f"Processing: {num}")

# Avoid nested if statements
for user in users:
    if not user.is_active:
        continue
    if not user.has_permission:
        continue
    process_user(user)
```

---

## 6. yield Statement

### Definition

Used in generator functions. Returns a value and pauses the function, resuming from that point on next call.

### Usage

```python
# Simple generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Returns value and pauses
        count += 1

for num in count_up_to(5):
    print(num)
# Output: 1, 2, 3, 4, 5

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Read large file efficiently
def read_large_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()
```

---

## 7. raise Statement

### Definition

Used to manually trigger an exception.

### Usage

```python
# Raise exception with message
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Raise custom exception
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Invalid email format")

# Re-raise exception
try:
    risky_operation()
except ValueError:
    print("Logging error...")
    raise  # Re-raises the same exception
```

---

## 8. assert Statement

### Definition

Tests if a condition is true. If false, raises an AssertionError. Used for debugging and testing.

### Usage

```python
# Basic assertion
x = 5
assert x > 0  # Passes silently

# Assertion with message
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)

# Testing assumptions
def process_data(data):
    assert isinstance(data, list), "Data must be a list"
    assert len(data) > 0, "Data cannot be empty"
    # Process data

# Note: Assertions can be disabled with -O flag
# python -O script.py
```

---

## 9. with Statement

### Definition

Used for context management. Ensures proper acquisition and release of resources.

### Usage

```python
# File handling (automatically closes file)
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed here

# Multiple context managers
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())

# Thread locking
from threading import Lock
lock = Lock()

with lock:
    # Critical section
    shared_resource += 1
# Lock automatically released
```

---

## 10. del Statement

### Definition

Deletes objects, variables, or items from collections.

### Usage

```python
# Delete variable
x = 10
del x
# print(x)  # NameError: x is not defined

# Delete list items
numbers = [1, 2, 3, 4, 5]
del numbers[2]  # Remove index 2
print(numbers)  # [1, 2, 4, 5]

del numbers[1:3]  # Remove slice
print(numbers)  # [1, 5]

# Delete dictionary keys
person = {"name": "John", "age": 30, "city": "NYC"}
del person["age"]
print(person)  # {'name': 'John', 'city': 'NYC'}
```

---

## 11. global and nonlocal

### global Statement

Declares that a variable refers to a global variable:

```python
count = 0

def increment():
    global count  # Access global variable
    count += 1

increment()
print(count)  # 1
```

### nonlocal Statement

Refers to a variable in the nearest enclosing scope:

```python
def outer():
    x = 10

    def inner():
        nonlocal x  # Access outer function's variable
        x += 5

    inner()
    print(x)  # 15

outer()
```

---

## 12. print() end Parameter

### Definition

The `end` parameter specifies what is printed at the end of the line. Default is newline (`\n`).

### Usage

```python
# Default behavior (newline after each print)
for i in range(1, 4):
    print(i)
# Output:
# 1
# 2
# 3

# Using end="" (no newline)
for i in range(1, 10):
    print(i, end="")
# Output: 123456789

# Using custom separator
for i in range(1, 10):
    print(i, end=", ")
# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9,
```

---

## 13. Quick Reference

### Statement Summary

| Statement | Type | Purpose | Scope |
|-----------|------|---------|-------|
| `pass` | Placeholder | Does nothing | Any block |
| `return` | Function control | Exits function, returns value | Functions |
| `break` | Loop control | Exits loop completely | Loops |
| `continue` | Loop control | Skips current iteration | Loops |
| `yield` | Generator control | Pauses function, returns value | Functions |
| `raise` | Exception control | Triggers exception | Anywhere |
| `assert` | Testing | Checks condition | Anywhere |
| `del` | Memory management | Deletes objects | Anywhere |
| `with` | Context management | Manages resources | Anywhere |
| `global` | Scope control | Declares global variable | Functions |
| `nonlocal` | Scope control | Declares enclosing scope variable | Nested functions |

### Comparison: break vs continue vs pass vs return

```python
# break: exits loop completely
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0, 1, 2

# continue: skips current iteration
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4

# pass: does nothing
for i in range(5):
    if i == 3:
        pass
    print(i)
# Output: 0, 1, 2, 3, 4

# return: exits function
def test_return():
    for i in range(5):
        if i == 3:
            return
        print(i)

test_return()
# Output: 0, 1, 2
```

### When to Use What

| Use | When |
|-----|------|
| `pass` | Need a syntactically required placeholder |
| `return` | Exit a function and optionally return a value |
| `break` | Exit a loop completely |
| `continue` | Skip current iteration, continue looping |
| `yield` | Create a generator for lazy evaluation |
| `raise` | Signal an error condition |
| `assert` | Verify assumptions during development |
| `del` | Remove variables or free memory |
| `with` | Need automatic resource management |
| `global/nonlocal` | Modify variables from outer scopes |

---

## Coverage Checklist

- [x] pass statement
- [x] return statement
- [x] break statement
- [x] continue statement
- [x] yield statement
- [x] raise statement
- [x] assert statement
- [x] with statement
- [x] del statement
- [x] global and nonlocal
- [x] print() end parameter
- [x] Comparison table
- [x] Quick reference
