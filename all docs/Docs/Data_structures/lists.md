# Python Lists - Complete Guide

A comprehensive reference guide for Python Lists.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Creating Lists](#2-creating-lists)
3. [Accessing Elements](#3-accessing-elements)
4. [List Methods](#4-list-methods)
5. [List Operations](#5-list-operations)
6. [Common Mistakes](#6-common-mistakes)
7. [Best Practices](#7-best-practices)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What is a List?

A list is an **ordered**, **mutable** collection that can hold items of different data types. Lists are one of the most versatile and commonly used data structures in Python.

### Key Characteristics

| Feature | Description |
|---------|-------------|
| Ordered | Elements maintain insertion order |
| Mutable | Can add, remove, or change elements |
| Allows Duplicates | Same value can appear multiple times |
| Heterogeneous | Can hold different data types |
| Indexed | Access elements by position (0-based) |

### When to Use Lists

- When you need an ordered collection
- When you need to modify elements frequently
- When you need to allow duplicate values
- When order of elements matters

---

## 2. Creating Lists

### Basic Creation

```python
# Empty list
empty_list = []
empty_list = list()

# List with values
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed = [1, "hello", 3.14, True]

# Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
```

### Creating from Other Types

```python
# From string
chars = list("hello")
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']

# From range
numbers = list(range(5))
print(numbers)  # Output: [0, 1, 2, 3, 4]

# From tuple
my_list = list((1, 2, 3))
print(my_list)  # Output: [1, 2, 3]
```

---

## 3. Accessing Elements

### By Index

```python
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing (from start)
print(fruits[0])   # Output: apple
print(fruits[2])   # Output: cherry

# Negative indexing (from end)
print(fruits[-1])  # Output: date (last element)
print(fruits[-2])  # Output: cherry (second last)
```

### Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:end] (end is exclusive)
print(numbers[2:5])    # Output: [2, 3, 4]
print(numbers[:4])     # Output: [0, 1, 2, 3] (from start)
print(numbers[6:])     # Output: [6, 7, 8, 9] (to end)

# With step [start:end:step]
print(numbers[::2])    # Output: [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1::2])   # Output: [1, 3, 5, 7, 9] (odd indices)

# Reverse list
print(numbers[::-1])   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

## 4. List Methods

### Adding Elements

#### append(x)

**Purpose**: Adds a single item to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Note: Appending a list adds it as a single element
fruits.append(["date", "elderberry"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', ['date', 'elderberry']]
```

---

#### extend(iterable)

**Purpose**: Adds all items from an iterable to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Can extend with any iterable
fruits.extend("mango")  # String is iterable
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'm', 'a', 'n', 'g', 'o']
```

---

#### insert(index, x)

**Purpose**: Inserts an item at a specific position.

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")  # Insert at index 1
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Insert at beginning
fruits.insert(0, "avocado")
print(fruits)  # Output: ['avocado', 'apple', 'banana', 'cherry']
```

---

### Removing Elements

#### remove(x)

**Purpose**: Removes the first occurrence of a value.

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'banana']

# Raises ValueError if not found
# fruits.remove("grape")  # ValueError: list.remove(x): x not in list
```

---

#### pop(index)

**Purpose**: Removes and returns item at index (default: last item).

```python
fruits = ["apple", "banana", "cherry"]

# Remove last item
last = fruits.pop()
print(last)    # Output: cherry
print(fruits)  # Output: ['apple', 'banana']

# Remove at specific index
first = fruits.pop(0)
print(first)   # Output: apple
print(fruits)  # Output: ['banana']
```

---

#### clear()

**Purpose**: Removes all items from the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []
```

---

### Searching and Counting

#### index(x, start, end)

**Purpose**: Returns index of first occurrence of value.

```python
fruits = ["apple", "banana", "cherry", "banana"]

print(fruits.index("banana"))     # Output: 1
print(fruits.index("banana", 2))  # Output: 3 (search from index 2)

# Raises ValueError if not found
# print(fruits.index("grape"))  # ValueError
```

---

#### count(x)

**Purpose**: Returns number of times value appears.

```python
numbers = [1, 2, 2, 3, 2, 4, 2]
print(numbers.count(2))  # Output: 4
print(numbers.count(5))  # Output: 0
```

---

### Ordering

#### sort(key, reverse)

**Purpose**: Sorts the list in place.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

# Sort by custom key
words = ["banana", "apple", "Cherry"]
words.sort(key=str.lower)  # Case-insensitive sort
print(words)  # Output: ['apple', 'banana', 'Cherry']
```

---

#### reverse()

**Purpose**: Reverses the list in place.

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]
```

---

#### copy()

**Purpose**: Returns a shallow copy of the list.

```python
original = [1, 2, 3]
copied = original.copy()
copied.append(4)

print(original)  # Output: [1, 2, 3] (unchanged)
print(copied)    # Output: [1, 2, 3, 4]
```

---

## 5. List Operations

### Concatenation (+)

**Purpose**: Combines two lists into a new list (does not modify originals).

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]
print(list1)     # Output: [1, 2, 3] (unchanged)
```

### Repetition (*)

**Purpose**: Repeats list elements.

```python
numbers = [1, 2, 3]
repeated = numbers * 3
print(repeated)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Membership (in)

**Purpose**: Checks if element exists in list.

```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)   # Output: True
print("grape" in fruits)   # Output: False
print("grape" not in fruits)  # Output: True
```

### Length (len)

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3
```

---

## 6. Common Mistakes

### Mistake 1: Confusing append() and extend()

```python
# WRONG - Adding list as single element
my_list = [1, 2]
my_list.append([3, 4])
print(my_list)  # Output: [1, 2, [3, 4]] - Nested list!

# CORRECT - Adding individual elements
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)  # Output: [1, 2, 3, 4]
```

### Mistake 2: Modifying List While Iterating

```python
# WRONG - Skips elements
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # Output: [1, 3, 5] - May skip elements!

# CORRECT - Use list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # Output: [1, 3, 5]
```

### Mistake 3: Using = Instead of copy()

```python
# WRONG - Both variables point to same list
original = [1, 2, 3]
copy = original  # Not a copy!
copy.append(4)
print(original)  # Output: [1, 2, 3, 4] - Original changed!

# CORRECT - Create actual copy
original = [1, 2, 3]
copy = original.copy()
copy.append(4)
print(original)  # Output: [1, 2, 3] - Original unchanged
```

### Mistake 4: Index Out of Range

```python
fruits = ["apple", "banana", "cherry"]

# WRONG - Index doesn't exist
# print(fruits[5])  # IndexError: list index out of range

# CORRECT - Check length first
if len(fruits) > 5:
    print(fruits[5])
else:
    print("Index out of range")
```

---

## 7. Best Practices

### 1. Use List Comprehensions for Simple Transformations

```python
# Instead of:
squares = []
for x in range(5):
    squares.append(x ** 2)

# Use:
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

### 2. Use enumerate() for Index + Value

```python
fruits = ["apple", "banana", "cherry"]

# Instead of:
for i in range(len(fruits)):
    print(i, fruits[i])

# Use:
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

### 3. Use zip() for Parallel Iteration

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

---

## 8. Quick Reference

### Methods Summary Table

| Method | Purpose | Returns | Modifies List |
|--------|---------|---------|---------------|
| `append(x)` | Add single item to end | None | Yes |
| `extend(iterable)` | Add multiple items | None | Yes |
| `insert(i, x)` | Insert at index | None | Yes |
| `remove(x)` | Remove first occurrence | None | Yes |
| `pop(i)` | Remove and return at index | Item | Yes |
| `clear()` | Remove all items | None | Yes |
| `index(x)` | Find index of value | int | No |
| `count(x)` | Count occurrences | int | No |
| `sort()` | Sort in place | None | Yes |
| `reverse()` | Reverse in place | None | Yes |
| `copy()` | Create shallow copy | list | No |

### Operations Summary

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Concatenate | `list1 + list2` | Combine lists |
| Repeat | `list * n` | Repeat n times |
| Membership | `x in list` | Check existence |
| Length | `len(list)` | Get count |
| Slice | `list[start:end:step]` | Get subset |

### append vs extend vs + Comparison

| Method | Modifies Original | Adds Single Element | Adds Multiple Elements |
|--------|-------------------|---------------------|------------------------|
| `append()` | Yes | Yes | No (adds as nested) |
| `extend()` | Yes | No | Yes (adds individually) |
| `+` | No (creates new) | No | Yes |

---

## Coverage Checklist

- [x] All list methods documented
- [x] Creating and accessing lists
- [x] Slicing and indexing
- [x] Common mistakes explained
- [x] Best practices with examples
- [x] Quick reference tables
