# Python Generator Expressions - Complete Guide

A concise reference guide for Generator Expressions in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Syntax](#2-syntax)
3. [Generator vs List Comprehension](#3-generator-vs-list-comprehension)
4. [Using Generators](#4-using-generators)
5. [Practical Examples](#5-practical-examples)
6. [When to Use Generators](#6-when-to-use-generators)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is a Generator Expression?

A generator expression is a concise way to create a **generator object** - an iterator that generates values **on demand** (lazily), one at a time, instead of storing the entire sequence in memory.

### Key Benefits

| Benefit | Description |
|---------|-------------|
| Memory Efficient | Doesn't store all values in memory |
| Lazy Evaluation | Values computed only when needed |
| Single Use | Can only iterate once |
| Fast for Large Data | Ideal for large/infinite sequences |

---

## 2. Syntax

### Basic Formula

```python
(expression for item in iterable)
```

### With Condition (Filter)

```python
(expression for item in iterable if condition)
```

### Component Breakdown

| Component | Role | Example |
|-----------|------|---------|
| `( )` | Parentheses define the generator | `(...)` |
| `expression` | Value produced for each element | `x * 2` |
| `item` | Variable representing current element | `x` |
| `iterable` | Source sequence | `range(10)` |
| `condition` | Optional filter | `if x % 2 == 0` |

---

## 3. Generator vs List Comprehension

### Key Differences

| Feature | Generator `()` | List Comprehension `[]` |
|---------|----------------|-------------------------|
| Syntax | `(x for x in range(5))` | `[x for x in range(5)]` |
| Result Type | `<generator object>` | `list` |
| Memory | Minimal (one value at a time) | Stores all values |
| Evaluation | Lazy (on demand) | Eager (immediate) |
| Reusable | No (single iteration) | Yes |

### Side-by-Side Example

```python
# Generator Expression
gen = (x * 2 for x in range(5))
print(gen)        # Output: <generator object ...>
print(list(gen))  # Output: [0, 2, 4, 6, 8]

# List Comprehension
lst = [x * 2 for x in range(5)]
print(lst)        # Output: [0, 2, 4, 6, 8]
```

### Memory Comparison

```python
import sys

# List - stores all 1 million values
list_comp = [x for x in range(1000000)]
print(sys.getsizeof(list_comp))  # ~8 MB

# Generator - stores only the generator object
gen_exp = (x for x in range(1000000))
print(sys.getsizeof(gen_exp))    # ~100 bytes
```

---

## 4. Using Generators

### Method 1: Iterate with for Loop

```python
gen = (x ** 2 for x in range(5))

for value in gen:
    print(value)
# Output: 0, 1, 4, 9, 16
```

### Method 2: Use next()

```python
gen = (x ** 2 for x in range(3))

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4
# print(next(gen))  # StopIteration error (exhausted)
```

### Method 3: Convert to List

```python
gen = (x ** 2 for x in range(5))
result = list(gen)
print(result)  # Output: [0, 1, 4, 9, 16]
```

### Method 4: Pass to Functions

Many functions accept iterables directly:

```python
# sum()
total = sum(x ** 2 for x in range(5))
print(total)  # Output: 30

# max() / min()
largest = max(x * 2 for x in range(10))
print(largest)  # Output: 18

# any() / all()
has_even = any(x % 2 == 0 for x in range(10))
print(has_even)  # Output: True
```

**Note**: When a generator is the only argument to a function, you can omit the parentheses:
```python
sum(x ** 2 for x in range(5))  # Valid - no extra parentheses needed
```

---

## 5. Practical Examples

### Example 1: Simple Transformation

```python
# Double each number
doubled = (x * 2 for x in range(5))
print(list(doubled))  # Output: [0, 2, 4, 6, 8]
```

### Example 2: Filter with Condition

```python
# Even numbers only
evens = (x for x in range(10) if x % 2 == 0)
print(list(evens))  # Output: [0, 2, 4, 6, 8]
```

### Example 3: Check if Any Character is Digit

```python
text = "Password123"

# Short-circuit: stops as soon as first digit is found
has_digit = any(char.isdigit() for char in text)
print(has_digit)  # Output: True
```

### Example 4: Flatten a Matrix

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = (num for row in matrix for num in row)
print(list(flat))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Example 5: Processing Large Files

```python
# Read large file line by line (memory efficient)
def read_large_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

# Process with generator
lines = (line.upper() for line in read_large_file('data.txt'))
```

### Example 6: Chain Transformations

```python
numbers = range(10)

# Chain: filter even → square → filter > 10
result = (
    x ** 2
    for x in numbers
    if x % 2 == 0
)
filtered = (x for x in result if x > 10)

print(list(filtered))  # Output: [16, 36, 64]
```

---

## 6. When to Use Generators

### Use Generators When:

1. **Large datasets** - Won't fit in memory
2. **Single iteration** - Only need to process once
3. **Passing to functions** - Like `sum()`, `max()`, `any()`
4. **Short-circuit evaluation** - `any()` and `all()` can stop early
5. **Streaming data** - Processing data as it arrives

### Use List Comprehension When:

1. **Multiple iterations** - Need to loop more than once
2. **Random access** - Need indexing like `result[5]`
3. **Length needed** - Need `len()` before processing
4. **Debugging** - Easier to inspect contents
5. **Small datasets** - Memory isn't a concern

---

## 7. Quick Reference

### Syntax Patterns

| Pattern | Example |
|---------|---------|
| Basic | `(x for x in iterable)` |
| Transform | `(x * 2 for x in iterable)` |
| Filter | `(x for x in iterable if condition)` |
| Transform + Filter | `(x * 2 for x in iterable if x > 0)` |
| Nested | `(x for row in matrix for x in row)` |

### Common Functions with Generators

| Function | Purpose | Example |
|----------|---------|---------|
| `sum()` | Sum all values | `sum(x for x in range(5))` |
| `max()` | Find maximum | `max(x for x in range(5))` |
| `min()` | Find minimum | `min(x for x in range(5))` |
| `any()` | True if any true | `any(x > 3 for x in range(5))` |
| `all()` | True if all true | `all(x > 0 for x in range(5))` |
| `list()` | Convert to list | `list(x for x in range(5))` |
| `tuple()` | Convert to tuple | `tuple(x for x in range(5))` |

### Generator vs List Summary

| Need | Use |
|------|-----|
| Memory efficiency | Generator |
| Process once | Generator |
| Short-circuit with `any()`/`all()` | Generator |
| Multiple iterations | List |
| Random access by index | List |
| Need to know length first | List |

---

## Coverage Checklist

- [x] Generator expression syntax
- [x] Comparison with list comprehension
- [x] Multiple ways to use generators
- [x] Practical examples
- [x] When to use each type
- [x] Quick reference tables
