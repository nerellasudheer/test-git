# Python Tuples - Complete Guide

A comprehensive reference guide for Python Tuples.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Creating Tuples](#2-creating-tuples)
3. [Accessing Elements](#3-accessing-elements)
4. [Tuple Methods](#4-tuple-methods)
5. [Tuple Operations](#5-tuple-operations)
6. [Immutability - The Key Concept](#6-immutability---the-key-concept)
7. [When to Use Tuples](#7-when-to-use-tuples)
8. [Common Mistakes](#8-common-mistakes)
9. [Quick Reference](#9-quick-reference)

---

## 1. Overview

### What is a Tuple?

A tuple is an **ordered**, **immutable** collection that can hold items of different data types. Once created, a tuple cannot be modified (no adding, removing, or changing elements).

### Key Characteristics

| Feature | Description |
|---------|-------------|
| Ordered | Elements maintain insertion order |
| Immutable | Cannot change after creation |
| Allows Duplicates | Same value can appear multiple times |
| Heterogeneous | Can hold different data types |
| Indexed | Access elements by position (0-based) |
| Hashable | Can be used as dictionary keys |

### Tuple vs List Comparison

| Feature | Tuple | List |
|---------|-------|------|
| Mutability | Immutable | Mutable |
| Syntax | `()` | `[]` |
| Performance | Slightly faster | Slightly slower |
| Methods | Only 2 (`count`, `index`) | Many (10+) |
| Memory | Less memory | More memory |
| Use as dict key | Yes | No |

---

## 2. Creating Tuples

### Basic Creation

```python
# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Tuple with values
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")

# Mixed data types
mixed = (1, "hello", 3.14, True)

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
```

### Important: Single Element Tuple

```python
# WRONG - This is just a string, not a tuple!
not_tuple = ("hello")
print(type(not_tuple))  # Output: <class 'str'>

# CORRECT - Add trailing comma for single element
single_tuple = ("hello",)
print(type(single_tuple))  # Output: <class 'tuple'>

# Also works without parentheses
single = 42,
print(type(single))  # Output: <class 'tuple'>
```

### Tuple Packing and Unpacking

```python
# Packing - creating tuple without parentheses
coordinates = 10, 20, 30
print(coordinates)  # Output: (10, 20, 30)

# Unpacking - extracting values
x, y, z = coordinates
print(x, y, z)  # Output: 10 20 30

# Unpacking with * (rest operator)
first, *rest = (1, 2, 3, 4, 5)
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5] (becomes a list!)

# Swap values using unpacking
a, b = 10, 20
a, b = b, a
print(a, b)  # Output: 20 10
```

### Creating from Other Types

```python
# From list
my_tuple = tuple([1, 2, 3])
print(my_tuple)  # Output: (1, 2, 3)

# From string
chars = tuple("hello")
print(chars)  # Output: ('h', 'e', 'l', 'l', 'o')

# From range
numbers = tuple(range(5))
print(numbers)  # Output: (0, 1, 2, 3, 4)
```

---

## 3. Accessing Elements

### By Index

```python
fruits = ("apple", "banana", "cherry", "date")

# Positive indexing (from start)
print(fruits[0])   # Output: apple
print(fruits[2])   # Output: cherry

# Negative indexing (from end)
print(fruits[-1])  # Output: date (last element)
print(fruits[-2])  # Output: cherry (second last)
```

### Slicing

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing [start:end] (end is exclusive)
print(numbers[2:5])    # Output: (2, 3, 4)
print(numbers[:4])     # Output: (0, 1, 2, 3) (from start)
print(numbers[6:])     # Output: (6, 7, 8, 9) (to end)

# With step [start:end:step]
print(numbers[::2])    # Output: (0, 2, 4, 6, 8) (every 2nd)
print(numbers[::-1])   # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0) (reversed)
```

---

## 4. Tuple Methods

Tuples have only **2 methods** due to their immutable nature.

### count(x)

**Purpose**: Returns the number of times a value appears in the tuple.

```python
numbers = (1, 2, 2, 3, 2, 4, 2, 5)

print(numbers.count(2))  # Output: 4
print(numbers.count(5))  # Output: 1
print(numbers.count(10)) # Output: 0
```

---

### index(x, start, end)

**Purpose**: Returns the index of the first occurrence of a value.

```python
fruits = ("apple", "banana", "cherry", "banana", "date")

# Find first occurrence
print(fruits.index("banana"))  # Output: 1

# Find from specific position
print(fruits.index("banana", 2))  # Output: 3 (search from index 2)

# Raises ValueError if not found
try:
    print(fruits.index("grape"))
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: tuple.index(x): x not in tuple
```

---

## 5. Tuple Operations

### Concatenation (+)

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)
```

### Repetition (*)

```python
numbers = (1, 2, 3)
repeated = numbers * 3
print(repeated)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### Membership (in)

```python
fruits = ("apple", "banana", "cherry")
print("apple" in fruits)      # Output: True
print("grape" in fruits)      # Output: False
print("grape" not in fruits)  # Output: True
```

### Length (len)

```python
fruits = ("apple", "banana", "cherry")
print(len(fruits))  # Output: 3
```

### Min/Max/Sum (for numeric tuples)

```python
numbers = (5, 2, 8, 1, 9)
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 9
print(sum(numbers))  # Output: 25
```

---

## 6. Immutability - The Key Concept

### The Fundamental Rule

Once a tuple is created, you **cannot**:
- Add elements
- Remove elements
- Change existing elements

```python
fruits = ("apple", "banana", "cherry")

# These will all raise TypeError
# fruits[0] = "avocado"      # TypeError: 'tuple' object does not support item assignment
# fruits.append("date")      # AttributeError: 'tuple' object has no attribute 'append'
# del fruits[0]              # TypeError: 'tuple' object doesn't support item deletion
```

### The Exception: Mutable Objects Inside Tuples

If a tuple contains a mutable object (like a list), you **can** modify the contents of that mutable object.

```python
# Tuple containing a list
my_tuple = (1, 2, [30, 40], "hello")

# CANNOT replace the list
# my_tuple[2] = [50, 60]  # TypeError!

# CAN modify the list's contents
my_tuple[2].append(50)
my_tuple[2][0] = 300

print(my_tuple)  # Output: (1, 2, [300, 40, 50], 'hello')
```

**Why does this work?**
- The tuple stores a *reference* to the list, not the list itself
- The reference hasn't changed - it still points to the same list object
- Only the list's internal contents changed

### "Modifying" a Tuple (Creating New)

To "change" a tuple, create a new tuple:

```python
original = (1, 2, 3)

# Add element - create new tuple
new_tuple = original + (4,)
print(new_tuple)  # Output: (1, 2, 3, 4)

# Remove element - use slicing and concatenation
# Remove element at index 1
new_tuple = original[:1] + original[2:]
print(new_tuple)  # Output: (1, 3)

# Convert to list, modify, convert back
temp_list = list(original)
temp_list[0] = 100
modified = tuple(temp_list)
print(modified)  # Output: (100, 2, 3)
```

---

## 7. When to Use Tuples

### 1. Fixed Data That Shouldn't Change

```python
# Coordinates
point = (10.5, 20.3)

# RGB color values
red = (255, 0, 0)

# Date components
date = (2024, 12, 25)
```

### 2. Dictionary Keys

```python
# Tuples can be dictionary keys (lists cannot!)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}

print(locations[(40.7128, -74.0060)])  # Output: New York
```

### 3. Multiple Return Values from Functions

```python
def get_user_info():
    return "Alice", 25, "alice@email.com"

# Unpack the returned tuple
name, age, email = get_user_info()
print(name, age, email)  # Output: Alice 25 alice@email.com
```

### 4. Heterogeneous Data Records

```python
# Employee record (name, id, salary, is_active)
employee = ("John Doe", 12345, 75000.0, True)
```

### 5. Performance-Critical Code

```python
# Tuples are faster and use less memory than lists
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))   # Output: ~104 bytes
print(sys.getsizeof(my_tuple))  # Output: ~80 bytes
```

---

## 8. Common Mistakes

### Mistake 1: Forgetting Comma for Single Element

```python
# WRONG - Creates a string, not a tuple
single = ("hello")
print(type(single))  # Output: <class 'str'>

# CORRECT - Add trailing comma
single = ("hello",)
print(type(single))  # Output: <class 'tuple'>
```

### Mistake 2: Trying to Modify a Tuple

```python
# WRONG - Tuples are immutable
fruits = ("apple", "banana")
# fruits[0] = "avocado"  # TypeError!

# CORRECT - Create a new tuple
fruits = ("avocado",) + fruits[1:]
print(fruits)  # Output: ('avocado', 'banana')
```

### Mistake 3: Confusing Unpacking with Indexing

```python
data = (1, 2, 3)

# WRONG for getting multiple values
first = data[0]
second = data[1]
third = data[2]

# BETTER - Use unpacking
first, second, third = data
```

### Mistake 4: Not Understanding Nested Mutable Objects

```python
# Tuple with list inside
t = ([1, 2], [3, 4])

# This modifies the list, not the tuple
t[0].append(100)
print(t)  # Output: ([1, 2, 100], [3, 4])

# The tuple structure is unchanged, only list content changed
```

---

## 9. Quick Reference

### Creating Tuples

| Syntax | Description |
|--------|-------------|
| `()` | Empty tuple |
| `(1, 2, 3)` | Tuple with values |
| `(1,)` | Single element tuple |
| `1, 2, 3` | Packing (without parentheses) |
| `tuple([1, 2, 3])` | From list |

### Methods

| Method | Purpose | Returns |
|--------|---------|---------|
| `count(x)` | Count occurrences of x | int |
| `index(x)` | Find first index of x | int |

### Operations

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Concatenate | `tuple1 + tuple2` | Combine tuples |
| Repeat | `tuple * n` | Repeat n times |
| Membership | `x in tuple` | Check existence |
| Length | `len(tuple)` | Get count |
| Slice | `tuple[start:end:step]` | Get subset |
| Unpack | `a, b, c = tuple` | Extract values |

### Tuple vs List Summary

| Operation | Tuple | List |
|-----------|-------|------|
| Create | `(1, 2, 3)` | `[1, 2, 3]` |
| Add element | Not possible | `append()`, `extend()` |
| Remove element | Not possible | `remove()`, `pop()` |
| Change element | Not possible | `list[i] = value` |
| As dict key | Yes | No |
| Methods | 2 | 10+ |

---

## Coverage Checklist

- [x] Creating tuples (all methods)
- [x] Accessing elements (indexing, slicing)
- [x] Both tuple methods (count, index)
- [x] Tuple operations (+, *, in, len)
- [x] Immutability explained with exception
- [x] Use cases documented
- [x] Common mistakes explained
- [x] Quick reference tables
