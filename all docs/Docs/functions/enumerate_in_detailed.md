# Python enumerate() Function - Complete Guide

A comprehensive reference for the enumerate() built-in function.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic Usage](#2-basic-usage)
3. [Custom Starting Index](#3-custom-starting-index)
4. [Works with All Iterables](#4-works-with-all-iterables)
5. [Practical Use Cases](#5-practical-use-cases)
6. [Common Mistakes](#6-common-mistakes)
7. [Related Functions](#7-related-functions)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What is enumerate()?

`enumerate()` is a built-in Python function that adds a counter to any iterable and returns an enumerate object. It produces pairs of (index, value) during iteration.

### Syntax

```python
enumerate(iterable, start=0)
```

**Parameters**:
- `iterable`: Any sequence (list, tuple, string, etc.)
- `start`: Starting index (default: 0)

**Returns**: Enumerate object (iterator of tuples)

### Why Use enumerate()?

Instead of manually tracking index:

```python
# OLD WAY (avoid this)
fruits = ['apple', 'banana', 'cherry']
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

# BETTER WAY (use enumerate)
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

## 2. Basic Usage

### Simple Example

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry
```

### What enumerate() Returns

```python
fruits = ['apple', 'banana', 'cherry']
result = enumerate(fruits)

print(result)       # <enumerate object at 0x...>
print(type(result)) # <class 'enumerate'>

# Convert to list to see all pairs
print(list(enumerate(fruits)))
# Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

---

## 3. Custom Starting Index

Use `start` parameter to begin from a different number:

```python
fruits = ['apple', 'banana', 'cherry']

# Start from 1 instead of 0
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 apple
# 2 banana
# 3 cherry
```

**Use Case**: Creating numbered lists for display.

```python
tasks = ['Buy groceries', 'Clean room', 'Study Python']

for num, task in enumerate(tasks, start=1):
    print(f"{num}. {task}")

# Output:
# 1. Buy groceries
# 2. Clean room
# 3. Study Python
```

---

## 4. Works with All Iterables

### With Strings

```python
word = "hello"

for index, char in enumerate(word):
    print(index, char)

# Output:
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o
```

### With Tuples

```python
colors = ('red', 'green', 'blue')

for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

# Output:
# Color 0: red
# Color 1: green
# Color 2: blue
```

### With Dictionaries

```python
# Iterates over keys by default
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

for index, name in enumerate(scores):
    print(index, name)

# Output:
# 0 Alice
# 1 Bob
# 2 Charlie

# With items() for key-value pairs
for index, (name, score) in enumerate(scores.items()):
    print(f"{index}: {name} scored {score}")

# Output:
# 0: Alice scored 85
# 1: Bob scored 92
# 2: Charlie scored 78
```

---

## 5. Practical Use Cases

### Finding Position of Items

```python
numbers = [10, 20, 30, 20, 40]

for index, num in enumerate(numbers):
    if num == 20:
        print(f"Found 20 at index {index}")

# Output:
# Found 20 at index 1
# Found 20 at index 3
```

### Modifying List Elements

```python
prices = [100, 200, 300]

for index, price in enumerate(prices):
    prices[index] = price * 1.1  # Increase by 10%

print(prices)  # [110.0, 220.0, 330.0]
```

### Tracking Progress

```python
files = ['file1.txt', 'file2.txt', 'file3.txt']
total = len(files)

for index, file in enumerate(files, start=1):
    print(f"Processing {index}/{total}: {file}")

# Output:
# Processing 1/3: file1.txt
# Processing 2/3: file2.txt
# Processing 3/3: file3.txt
```

### Reading Files with Line Numbers

```python
with open('example.txt', 'r') as file:
    for line_num, line in enumerate(file, start=1):
        print(f"Line {line_num}: {line.strip()}")
```

### List Comprehension

```python
fruits = ['apple', 'banana', 'cherry']

indexed = [f"{i}: {fruit}" for i, fruit in enumerate(fruits, start=1)]
print(indexed)
# Output: ['1: apple', '2: banana', '3: cherry']
```

### Dictionary Comprehension

```python
fruits = ['apple', 'banana', 'cherry']

fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}
print(fruit_dict)
# Output: {0: 'apple', 1: 'banana', 2: 'cherry'}
```

---

## 6. Common Mistakes

### Mistake 1: Calling enumerate as a Method

```python
# WRONG - enumerate is a function, not a method
# my_list.enumerate()  # AttributeError!

# CORRECT
enumerate(my_list)
```

### Mistake 2: Not Unpacking Both Values

```python
fruits = ['apple', 'banana']

# WRONG - Gets tuples
for item in enumerate(fruits):
    print(item)
# Output: (0, 'apple'), (1, 'banana')

# CORRECT - Unpack into two variables
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output: 0 apple, 1 banana
```

### Mistake 3: Using range(len()) Instead

```python
fruits = ['apple', 'banana', 'cherry']

# LESS PYTHONIC
for i in range(len(fruits)):
    print(i, fruits[i])

# MORE PYTHONIC
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

---

## 7. Related Functions

### zip() - Combine Multiple Iterables

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

### Combining enumerate and zip

```python
names = ['Alice', 'Bob']
ages = [25, 30]

for index, (name, age) in enumerate(zip(names, ages), start=1):
    print(f"{index}. {name} is {age}")

# Output:
# 1. Alice is 25
# 2. Bob is 30
```

### range() vs enumerate()

| Function | Use When |
|----------|----------|
| `range()` | Only need numbers |
| `enumerate()` | Need index AND values from iterable |

```python
# range - just numbers
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# enumerate - index + value
for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)  # 0 a, 1 b, 2 c
```

---

## 8. Quick Reference

### Syntax Patterns

| Pattern | Example |
|---------|---------|
| Basic | `for i, x in enumerate(items):` |
| Custom start | `for i, x in enumerate(items, start=1):` |
| To list | `list(enumerate(items))` |
| In comprehension | `[f"{i}: {x}" for i, x in enumerate(items)]` |

### When to Use enumerate()

| Situation | Use enumerate? |
|-----------|----------------|
| Need index and value | Yes |
| Just need values | No (use `for item in items`) |
| Just need indices | No (use `range(len(items))`) |
| Creating numbered lists | Yes with `start=1` |
| Tracking position | Yes |

### enumerate() vs Alternatives

| Method | Code |
|--------|------|
| Manual counter | `i = 0; for x in items: ... i += 1` |
| range + indexing | `for i in range(len(items)): items[i]` |
| enumerate | `for i, x in enumerate(items):` |

**enumerate() is best** - cleaner, more readable, more Pythonic.

### Key Points

1. `enumerate()` is a **built-in function**, not a method
2. Works with **any iterable** (list, tuple, string, dict, file, etc.)
3. Returns **iterator** of (index, value) tuples
4. Does **not modify** the original iterable
5. Default start is **0**, can be changed with `start` parameter
6. More **Pythonic** than `range(len(iterable))`
7. **Memory efficient** - generates pairs on demand

---

## Coverage Checklist

- [x] Basic usage and syntax
- [x] Custom starting index
- [x] Works with all iterables
- [x] Practical use cases
- [x] Common mistakes
- [x] Related functions (zip, range)
- [x] Quick reference tables
