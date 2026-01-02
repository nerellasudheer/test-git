# Python Comprehensions - Complete Guide

A comprehensive reference guide for List, Dictionary, and Set Comprehensions.

---

## Table of Contents

1. [Overview](#1-overview)
2. [List Comprehensions](#2-list-comprehensions)
3. [Dictionary Comprehensions](#3-dictionary-comprehensions)
4. [Set Comprehensions](#4-set-comprehensions)
5. [Nested Comprehensions](#5-nested-comprehensions)
6. [When to Use Comprehensions](#6-when-to-use-comprehensions)
7. [Common Mistakes](#7-common-mistakes)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What are Comprehensions?

Comprehensions are a concise way to create collections (lists, dictionaries, sets) from existing iterables in a single line of code.

### Benefits

| Benefit | Description |
|---------|-------------|
| Concise | One line instead of multiple |
| Readable | Clear intent when simple |
| Faster | Often faster than equivalent loops |
| Pythonic | Idiomatic Python style |

### Types of Comprehensions

| Type | Syntax | Creates |
|------|--------|---------|
| List | `[expr for item in iterable]` | List |
| Dict | `{key: value for item in iterable}` | Dictionary |
| Set | `{expr for item in iterable}` | Set |
| Generator | `(expr for item in iterable)` | Generator |

---

## 2. List Comprehensions

### Basic Syntax

```python
new_list = [expression for item in iterable]
```

### With Condition

```python
new_list = [expression for item in iterable if condition]
```

### Basic Examples

```python
# Create list of squares
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Equivalent loop
squares = []
for x in range(5):
    squares.append(x**2)
```

---

### With Condition (Filter)

```python
# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Filter and transform
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]
```

---

### With If-Else (Transform)

```python
# If-else in expression (NOT filter)
result = [x if x % 2 == 0 else -x for x in range(5)]
print(result)  # Output: [0, -1, 2, -3, 4]

# Classify numbers
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # Output: ['even', 'odd', 'even', 'odd', 'even']
```

**Important**:
- `if` after `for` = **filter** (which items to include)
- `if-else` before `for` = **transform** (what value to use)

---

### String Operations

```python
# Uppercase letters
letters = [char.upper() for char in "hello"]
print(letters)  # Output: ['H', 'E', 'L', 'L', 'O']

# Filter vowels
vowels = [char for char in "hello world" if char in "aeiou"]
print(vowels)  # Output: ['e', 'o', 'o']

# Word lengths
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)  # Output: [5, 6, 6]
```

---

### With Functions

```python
# Using built-in functions
numbers = ["1", "2", "3", "4", "5"]
integers = [int(n) for n in numbers]
print(integers)  # Output: [1, 2, 3, 4, 5]

# Using custom functions
def double(x):
    return x * 2

doubled = [double(x) for x in range(5)]
print(doubled)  # Output: [0, 2, 4, 6, 8]
```

---

## 3. Dictionary Comprehensions

### Basic Syntax

```python
new_dict = {key_expr: value_expr for item in iterable}
```

### Basic Examples

```python
# Squares dictionary
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

---

### With Condition

```python
# Only even squares
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Filter from existing dict
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0, "date": 1.5}
expensive = {k: v for k, v in prices.items() if v > 1.0}
print(expensive)  # Output: {'cherry': 2.0, 'date': 1.5}
```

---

### Transform Existing Dictionary

```python
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}

# Apply discount
discounted = {k: v * 0.9 for k, v in prices.items()}
print(discounted)  # Output: {'apple': 0.9, 'banana': 0.45, 'cherry': 1.8}

# Swap keys and values
swapped = {v: k for k, v in prices.items()}
print(swapped)  # Output: {1.0: 'apple', 0.5: 'banana', 2.0: 'cherry'}

# Uppercase keys
upper_keys = {k.upper(): v for k, v in prices.items()}
print(upper_keys)  # Output: {'APPLE': 1.0, 'BANANA': 0.5, 'CHERRY': 2.0}
```

---

### From List of Tuples

```python
# Create dict from list of tuples
pairs = [("name", "Alice"), ("age", 25), ("city", "NYC")]
my_dict = {k: v for k, v in pairs}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'NYC'}
```

---

## 4. Set Comprehensions

### Basic Syntax

```python
new_set = {expression for item in iterable}
```

### Basic Examples

```python
# Unique squares
squares = {x**2 for x in range(-3, 4)}
print(squares)  # Output: {0, 1, 4, 9}

# Remove duplicates while transforming
words = ["hello", "world", "hello", "python"]
unique_lengths = {len(word) for word in words}
print(unique_lengths)  # Output: {5, 6}
```

---

### With Condition

```python
# Even numbers set
evens = {x for x in range(10) if x % 2 == 0}
print(evens)  # Output: {0, 2, 4, 6, 8}

# Unique vowels from string
text = "hello world python"
vowels = {char for char in text if char in "aeiou"}
print(vowels)  # Output: {'e', 'o'}
```

---

## 5. Nested Comprehensions

### Flatten a Matrix

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten to single list
flat = [num for row in matrix for num in row]
print(flat)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Equivalent loop
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
```

---

### Create 2D Lists

```python
# Create 3x3 matrix
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Create multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

### All Pairs (Cartesian Product)

```python
colors = ["red", "blue"]
sizes = ["S", "M", "L"]

# All combinations
pairs = [(color, size) for color in colors for size in sizes]
print(pairs)
# Output: [('red', 'S'), ('red', 'M'), ('red', 'L'),
#          ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

---

### Nested with Conditions

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Get all even numbers from matrix
evens = [num for row in matrix for num in row if num % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8]
```

---

## 6. When to Use Comprehensions

### Use Comprehensions When:

1. **Simple transformations**
   ```python
   # Good - simple and clear
   squares = [x**2 for x in range(10)]
   ```

2. **Simple filtering**
   ```python
   # Good - easy to understand
   evens = [x for x in numbers if x % 2 == 0]
   ```

3. **Creating from existing data**
   ```python
   # Good - clear data transformation
   names = [user["name"] for user in users]
   ```

### Avoid Comprehensions When:

1. **Complex logic**
   ```python
   # BAD - too complex
   result = [
       func1(x) if cond1(x) else func2(x) if cond2(x) else func3(x)
       for x in items
       if some_condition(x) and another_condition(x)
   ]

   # BETTER - use a loop
   result = []
   for x in items:
       if some_condition(x) and another_condition(x):
           if cond1(x):
               result.append(func1(x))
           elif cond2(x):
               result.append(func2(x))
           else:
               result.append(func3(x))
   ```

2. **Side effects needed**
   ```python
   # BAD - comprehension for side effects
   [print(x) for x in range(5)]  # Don't do this!

   # GOOD - use a loop
   for x in range(5):
       print(x)
   ```

3. **Multiple operations per item**
   ```python
   # BAD - multiple operations hidden
   [process(validate(transform(x))) for x in items]

   # BETTER - clearer with loop or function
   def handle(x):
       x = transform(x)
       x = validate(x)
       return process(x)

   result = [handle(x) for x in items]
   ```

---

## 7. Common Mistakes

### Mistake 1: If vs If-Else Position

```python
numbers = [1, 2, 3, 4, 5]

# WRONG - SyntaxError (if-else must be before for)
# result = [x for x in numbers if x > 2 else 0]

# CORRECT - if-else for transformation (before for)
result = [x if x > 2 else 0 for x in numbers]
print(result)  # Output: [0, 0, 3, 4, 5]

# CORRECT - if for filtering (after for)
result = [x for x in numbers if x > 2]
print(result)  # Output: [3, 4, 5]
```

### Mistake 2: Creating Matrix with *

```python
# WRONG - all rows share same list object!
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)  # Output: [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - All changed!

# CORRECT - use comprehension
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # Output: [[1, 0, 0], [0, 0, 0], [0, 0, 0]] - Only first changed
```

### Mistake 3: Using Comprehension for Side Effects

```python
# WRONG - comprehension creates unused list
[print(x) for x in range(5)]

# CORRECT - use a loop
for x in range(5):
    print(x)
```

### Mistake 4: Overly Complex Comprehensions

```python
# BAD - hard to read
result = [x**2 if x % 2 == 0 else x**3 for x in range(10) if x > 0 and x < 8]

# BETTER - split into steps or use loop
result = []
for x in range(1, 8):
    if x % 2 == 0:
        result.append(x**2)
    else:
        result.append(x**3)
```

---

## 8. Quick Reference

### Basic Syntax

| Type | Syntax |
|------|--------|
| List | `[expr for item in iterable]` |
| List + Filter | `[expr for item in iterable if condition]` |
| List + Transform | `[expr1 if cond else expr2 for item in iterable]` |
| Dict | `{key: value for item in iterable}` |
| Set | `{expr for item in iterable}` |

### Common Patterns

| Pattern | Example |
|---------|---------|
| Transform | `[x*2 for x in nums]` |
| Filter | `[x for x in nums if x > 0]` |
| Transform + Filter | `[x*2 for x in nums if x > 0]` |
| Conditional Value | `[x if x > 0 else 0 for x in nums]` |
| Flatten | `[x for row in matrix for x in row]` |
| Zip | `{k: v for k, v in zip(keys, values)}` |

### Position Rules

| Element | Position | Purpose |
|---------|----------|---------|
| `expression` | Before `for` | What to include |
| `if-else` | Before `for` | Transform value |
| `if` only | After `for` | Filter items |

### Best Practices

1. Keep comprehensions simple and readable
2. Use loops for complex logic
3. Don't use comprehensions for side effects
4. Consider readability over brevity
5. Use generator expressions for large datasets

---

## Coverage Checklist

- [x] List comprehension basics
- [x] List comprehension with conditions
- [x] Dictionary comprehensions
- [x] Set comprehensions
- [x] Nested comprehensions
- [x] When to use vs avoid
- [x] Common mistakes explained
- [x] Quick reference tables
