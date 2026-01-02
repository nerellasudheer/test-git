# Python For Loops - Complete Guide

Iterate over sequences with the for loop.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic For Loop](#2-basic-for-loop)
3. [range() Function](#3-range-function)
4. [Looping Through Data Types](#4-looping-through-data-types)
5. [Loop Control Statements](#5-loop-control-statements)
6. [Nested Loops](#6-nested-loops)
7. [Loop with else](#7-loop-with-else)
8. [Useful Loop Patterns](#8-useful-loop-patterns)
9. [Quick Reference](#9-quick-reference)

---

## 1. Overview

### What is a For Loop?

A for loop iterates over a sequence (list, tuple, string, etc.) and executes code for each item.

### Basic Syntax

```python
for item in sequence:
    # code to execute for each item
```

### How It Works

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

---

## 2. Basic For Loop

### Iterating Over a List

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num * 2)

# Output: 2, 4, 6, 8, 10
```

### Iterating Over a String

```python
word = "Python"

for char in word:
    print(char)

# Output: P, y, t, h, o, n
```

### Accumulating Values

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(f"Sum: {total}")  # Sum: 15
```

---

## 3. range() Function

### Basic range()

```python
# range(stop) - 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - start to stop-1
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### range() Parameters

| Syntax | Description | Example Output |
|--------|-------------|----------------|
| `range(5)` | 0 to 4 | 0, 1, 2, 3, 4 |
| `range(2, 5)` | 2 to 4 | 2, 3, 4 |
| `range(0, 10, 2)` | 0 to 9, step 2 | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5 to 1, step -1 | 5, 4, 3, 2, 1 |

### Counting Backwards

```python
# Countdown
for i in range(5, 0, -1):
    print(i)
print("Blast off!")

# Output: 5, 4, 3, 2, 1, Blast off!
```

### Common Use: Loop N Times

```python
# Print "Hello" 3 times
for _ in range(3):  # _ means we don't need the variable
    print("Hello")
```

---

## 4. Looping Through Data Types

### Lists

```python
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
```

### Tuples

```python
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)
```

### Strings

```python
for char in "Hello":
    print(char, end=" ")  # H e l l o
```

### Dictionaries

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Keys only (default)
for key in person:
    print(key)

# Values only
for value in person.values():
    print(value)

# Both keys and values
for key, value in person.items():
    print(f"{key}: {value}")
```

### Sets

```python
unique_nums = {1, 2, 3, 4, 5}
for num in unique_nums:
    print(num)  # Order not guaranteed
```

---

## 5. Loop Control Statements

### break - Exit Loop Early

```python
# Find first even number
numbers = [1, 3, 5, 6, 7, 8]

for num in numbers:
    if num % 2 == 0:
        print(f"First even: {num}")
        break

# Output: First even: 6
```

### continue - Skip Current Iteration

```python
# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Output: 1, 3, 5, 7, 9
```

### pass - Placeholder

```python
# Placeholder for future code
for i in range(5):
    if i == 3:
        pass  # TODO: handle this case
    print(i)
```

### Comparison

| Statement | Effect |
|-----------|--------|
| `break` | Exit the entire loop |
| `continue` | Skip to next iteration |
| `pass` | Do nothing (placeholder) |

---

## 6. Nested Loops

### Basic Nested Loop

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")
```

### Working with 2D Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # New line after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

### Breaking Out of Nested Loops

```python
# Using a flag
found = False
for i in range(5):
    for j in range(5):
        if i * j == 6:
            print(f"Found: {i} x {j}")
            found = True
            break
    if found:
        break
```

---

## 7. Loop with else

### Syntax

The `else` block executes if the loop completes without `break`.

```python
for item in sequence:
    # loop body
else:
    # executes if loop completes normally (no break)
```

### Example: Search with else

```python
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")

# Output: 4 not found
```

### Practical Use: Prime Number Check

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # break would skip else
    else:
        return True  # No divisor found

print(is_prime(17))  # True
print(is_prime(15))  # False
```

---

## 8. Useful Loop Patterns

### enumerate() - Get Index and Value

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
```

### zip() - Loop Multiple Lists Together

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

### reversed() - Loop Backwards

```python
colors = ["red", "green", "blue"]

for color in reversed(colors):
    print(color)

# Output: blue, green, red
```

### sorted() - Loop in Sorted Order

```python
numbers = [3, 1, 4, 1, 5, 9]

for num in sorted(numbers):
    print(num)  # 1, 1, 3, 4, 5, 9

# Descending order
for num in sorted(numbers, reverse=True):
    print(num)  # 9, 5, 4, 3, 1, 1
```

### List Comprehension (Alternative to Loop)

```python
# Traditional loop
squares = []
for i in range(5):
    squares.append(i ** 2)

# List comprehension (more Pythonic)
squares = [i ** 2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

## 9. Quick Reference

### Basic Syntax

```python
# Simple for loop
for item in sequence:
    do_something(item)

# With range
for i in range(n):
    do_something(i)

# With enumerate
for index, item in enumerate(sequence):
    do_something(index, item)

# With zip
for a, b in zip(list1, list2):
    do_something(a, b)
```

### range() Summary

| Pattern | Description | Output |
|---------|-------------|--------|
| `range(5)` | 0 to 4 | 0,1,2,3,4 |
| `range(1, 6)` | 1 to 5 | 1,2,3,4,5 |
| `range(0, 10, 2)` | Even numbers | 0,2,4,6,8 |
| `range(5, 0, -1)` | Countdown | 5,4,3,2,1 |

### Loop Control

| Statement | Purpose |
|-----------|---------|
| `break` | Exit loop immediately |
| `continue` | Skip to next iteration |
| `pass` | Do nothing |
| `else` | Runs if no break |

### Useful Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `enumerate()` | Index + value | `for i, v in enumerate(list)` |
| `zip()` | Parallel iteration | `for a, b in zip(l1, l2)` |
| `reversed()` | Reverse order | `for x in reversed(list)` |
| `sorted()` | Sorted order | `for x in sorted(list)` |

### Common Patterns

| Pattern | Use Case |
|---------|----------|
| `for _ in range(n)` | Repeat n times |
| `for i, item in enumerate(list)` | Need index |
| `for key, val in dict.items()` | Iterate dict |
| `for row in matrix` | 2D iteration |

---

## Coverage Checklist

- [x] Basic for loop syntax
- [x] range() function (start, stop, step)
- [x] Looping through all data types
- [x] break, continue, pass
- [x] Nested loops
- [x] Loop with else clause
- [x] enumerate(), zip(), reversed(), sorted()
- [x] List comprehension mention
- [x] Quick reference tables
