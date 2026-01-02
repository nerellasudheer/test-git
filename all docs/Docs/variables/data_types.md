# Python Data Types - Quick Reference

A guide to basic data types and type conversion in Python.

---

## Table of Contents

1. [Basic Data Types](#1-basic-data-types)
2. [Type Checking](#2-type-checking)
3. [Type Conversion](#3-type-conversion)
4. [Boolean Truthiness](#4-boolean-truthiness)
5. [User Input](#5-user-input)
6. [Quick Reference](#6-quick-reference)

---

## 1. Basic Data Types

### The Four Fundamental Types

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text (string) | `"Hello"`, `'World'` |
| `int` | Whole numbers | `42`, `-7`, `0` |
| `float` | Decimal numbers | `3.14`, `-0.5`, `2.0` |
| `bool` | True or False | `True`, `False` |

### String (str)

Text enclosed in quotes (single, double, or triple).

```python
name = "Alice"
message = 'Hello, World!'
multiline = """This is
a multiline
string"""

# Empty string
empty = ""
```

### Integer (int)

Whole numbers without decimal points.

```python
age = 25
count = -10
zero = 0

# Large numbers can use underscores for readability
big_number = 1_000_000  # Same as 1000000
```

### Float (float)

Numbers with decimal points.

```python
price = 19.99
temperature = -5.5
pi = 3.14159

# Scientific notation
large = 1.5e10   # 15000000000.0
small = 2.5e-4   # 0.00025
```

### Boolean (bool)

Logical values representing True or False.

```python
is_active = True
is_complete = False

# Result of comparisons
result = 5 > 3   # True
result = 5 == 3  # False
```

---

## 2. Type Checking

### type() Function

Check the type of any value.

```python
name = "Alice"
age = 25
price = 19.99
active = True

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(price))   # <class 'float'>
print(type(active))  # <class 'bool'>
```

### isinstance() Function

Check if a value is of a specific type.

```python
name = "Alice"

print(isinstance(name, str))    # True
print(isinstance(name, int))    # False

# Check multiple types
print(isinstance(25, (int, float)))  # True
```

---

## 3. Type Conversion

### Conversion Functions

| Function | Converts to | Example |
|----------|-------------|---------|
| `str()` | String | `str(42)` → `"42"` |
| `int()` | Integer | `int("42")` → `42` |
| `float()` | Float | `float("3.14")` → `3.14` |
| `bool()` | Boolean | `bool(1)` → `True` |

### String Conversion - str()

```python
# Convert anything to string
num_str = str(42)        # "42"
float_str = str(3.14)    # "3.14"
bool_str = str(True)     # "True"
list_str = str([1, 2])   # "[1, 2]"

# Useful for concatenation
age = 25
message = "I am " + str(age) + " years old"
```

### Integer Conversion - int()

```python
# From string (must be valid integer format)
num = int("42")      # 42
num = int("  42  ")  # 42 (handles whitespace)

# From float (truncates, doesn't round)
num = int(3.7)       # 3 (not 4!)
num = int(-3.7)      # -3

# From boolean
num = int(True)      # 1
num = int(False)     # 0

# With base (for different number systems)
num = int("1010", 2)  # 10 (binary to decimal)
num = int("ff", 16)   # 255 (hex to decimal)
```

### Float Conversion - float()

```python
# From string
num = float("3.14")   # 3.14
num = float("42")     # 42.0
num = float("-3.5")   # -3.5

# From integer
num = float(42)       # 42.0

# From boolean
num = float(True)     # 1.0
num = float(False)    # 0.0

# Special values
inf = float("inf")    # Infinity
neg_inf = float("-inf")
```

### Boolean Conversion - bool()

```python
# From numbers
bool(1)      # True
bool(0)      # False
bool(-5)     # True (any non-zero)
bool(3.14)   # True

# From strings
bool("hello")  # True
bool("")       # False (empty string)
bool(" ")      # True (space is not empty!)

# From None
bool(None)     # False

# From collections
bool([1, 2])   # True
bool([])       # False (empty list)
```

### Conversion Errors

```python
# Invalid conversions raise errors

# ValueError - invalid literal
int("hello")      # ValueError
int("3.14")       # ValueError (use float first)
float("abc")      # ValueError

# Solution: Use try-except
try:
    num = int(user_input)
except ValueError:
    print("Please enter a valid number")
```

---

## 4. Boolean Truthiness

### Falsy Values

These values evaluate to `False`:

| Value | Type |
|-------|------|
| `False` | bool |
| `0` | int |
| `0.0` | float |
| `""` (empty string) | str |
| `None` | NoneType |
| `[]` (empty list) | list |
| `{}` (empty dict) | dict |
| `()` (empty tuple) | tuple |
| `set()` (empty set) | set |

```python
# All these are "falsy"
if not False:
    print("False is falsy")

if not 0:
    print("0 is falsy")

if not "":
    print("Empty string is falsy")

if not None:
    print("None is falsy")

if not []:
    print("Empty list is falsy")
```

### Truthy Values

Everything else evaluates to `True`:

```python
# All these are "truthy"
if True:
    print("True is truthy")

if 1:
    print("Non-zero numbers are truthy")

if "hello":
    print("Non-empty strings are truthy")

if [1, 2, 3]:
    print("Non-empty lists are truthy")

if " ":
    print("Space (not empty) is truthy!")
```

### Practical Use

```python
# Check if list has items
items = [1, 2, 3]
if items:
    print("List has items")

# Check if string is not empty
name = input("Enter name: ")
if name:
    print(f"Hello, {name}")
else:
    print("No name entered")
```

---

## 5. User Input

### input() Returns String

User input is **always** a string!

```python
# Input returns string
user_input = input("Enter a number: ")
print(type(user_input))  # <class 'str'>

# Must convert for math operations
num = int(input("Enter a number: "))
result = num * 2

# Or with float
price = float(input("Enter price: "))
total = price * 1.1  # Add 10% tax
```

### Safe Input Conversion

```python
# Pattern: Try to convert, handle errors
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")

age = get_integer("Enter your age: ")
```

### Different Input Types

```python
# String (default)
name = input("Enter name: ")

# Integer
age = int(input("Enter age: "))

# Float
height = float(input("Enter height: "))

# Boolean (custom)
answer = input("Continue? (yes/no): ")
continue_flag = answer.lower() == "yes"
```

---

## 6. Quick Reference

### Type Summary

| Type | Example | Conversion | Check |
|------|---------|------------|-------|
| str | `"hello"` | `str(x)` | `type(x) == str` |
| int | `42` | `int(x)` | `type(x) == int` |
| float | `3.14` | `float(x)` | `type(x) == float` |
| bool | `True` | `bool(x)` | `type(x) == bool` |

### Common Conversions

| From | To | Code |
|------|----|------|
| int → str | `"42"` | `str(42)` |
| str → int | `42` | `int("42")` |
| float → int | `3` | `int(3.7)` |
| int → float | `42.0` | `float(42)` |
| str → float | `3.14` | `float("3.14")` |
| str → int (with float) | `3` | `int(float("3.7"))` |

### Falsy Values

```python
# All these are False
bool(False)   # False
bool(0)       # False
bool(0.0)     # False
bool("")      # False
bool(None)    # False
bool([])      # False
bool({})      # False
```

### Key Points

1. **input()** always returns a string
2. **int()** truncates floats (doesn't round)
3. **Empty** = False, **Non-empty** = True
4. Use **try-except** for safe conversion
5. **Space (" ")** is truthy (not empty!)

---

## Coverage Checklist

- [x] Four basic data types
- [x] Type checking (type, isinstance)
- [x] Type conversion functions
- [x] Boolean truthiness
- [x] User input handling
- [x] Quick reference tables
