# Python Lambda Functions - Complete Guide

Anonymous functions for quick, one-line operations.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic Syntax](#2-basic-syntax)
3. [Lambda with Built-ins](#3-lambda-with-built-ins)
4. [Practical Examples](#4-practical-examples)
5. [Lambda vs Regular Functions](#5-lambda-vs-regular-functions)
6. [Common Patterns](#6-common-patterns)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is a Lambda Function?

A lambda function is a small, anonymous function defined in a single line. It can have any number of arguments but only one expression.

### Key Characteristics

| Feature | Description |
|---------|-------------|
| Anonymous | No name required |
| Single expression | Only one expression allowed |
| Implicit return | Expression result is automatically returned |
| Inline | Can be defined where needed |

### When to Use Lambda

- Simple operations that don't need reuse
- As arguments to higher-order functions (map, filter, sorted)
- Quick callbacks and event handlers
- Simple key functions for sorting

---

## 2. Basic Syntax

### Syntax Structure

```python
lambda arguments: expression
```

### Simple Examples

```python
# No arguments
say_hello = lambda: "Hello!"
print(say_hello())  # Hello!

# One argument
double = lambda x: x * 2
print(double(5))  # 10

# Two arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Multiple arguments
calculate = lambda a, b, c: a + b * c
print(calculate(1, 2, 3))  # 7
```

### Equivalent Regular Functions

```python
# Lambda
square = lambda x: x ** 2

# Equivalent regular function
def square(x):
    return x ** 2
```

### Default Arguments in Lambda

```python
# With default value
greet = lambda name="World": f"Hello, {name}!"
print(greet())         # Hello, World!
print(greet("Alice"))  # Hello, Alice!
```

---

## 3. Lambda with Built-ins

### With sorted()

```python
# Sort by second element
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(2, 'a'), (1, 'b'), (3, 'c')]

# Sort dictionaries by value
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
by_grade = sorted(students, key=lambda s: s["grade"])
print([s["name"] for s in by_grade])  # ['Charlie', 'Alice', 'Bob']

# Sort strings by length
words = ["banana", "apple", "cherry", "date"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['date', 'apple', 'banana', 'cherry']
```

### With map()

```python
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert to strings
strings = list(map(lambda x: str(x), numbers))
print(strings)  # ['1', '2', '3', '4', '5']

# Transform data
names = ["alice", "bob", "charlie"]
capitalized = list(map(lambda n: n.capitalize(), names))
print(capitalized)  # ['Alice', 'Bob', 'Charlie']
```

### With filter()

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter positive numbers
nums = [-3, -2, -1, 0, 1, 2, 3]
positive = list(filter(lambda x: x > 0, nums))
print(positive)  # [1, 2, 3]

# Filter by condition
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30}
]
adults = list(filter(lambda p: p["age"] >= 18, people))
print([p["name"] for p in adults])  # ['Alice', 'Charlie']
```

### With reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# Find maximum
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)  # 5

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda a, b: a + b, words)
print(sentence)  # Hello World!
```

### With min() and max()

```python
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Find student with highest grade
best = max(students, key=lambda s: s["grade"])
print(best["name"])  # Bob

# Find student with lowest grade
worst = min(students, key=lambda s: s["grade"])
print(worst["name"])  # Charlie
```

---

## 4. Practical Examples

### Sorting Complex Data

```python
# Sort by multiple criteria
employees = [
    {"name": "Alice", "dept": "HR", "salary": 50000},
    {"name": "Bob", "dept": "IT", "salary": 60000},
    {"name": "Charlie", "dept": "HR", "salary": 55000},
    {"name": "Diana", "dept": "IT", "salary": 55000}
]

# Sort by department, then by salary (descending)
sorted_emp = sorted(employees, key=lambda e: (e["dept"], -e["salary"]))
for e in sorted_emp:
    print(f"{e['dept']}: {e['name']} - ${e['salary']}")
```

### Data Transformation

```python
# Clean and transform data
raw_data = ["  Alice  ", "  BOB  ", "charlie  "]

cleaned = list(map(lambda s: s.strip().title(), raw_data))
print(cleaned)  # ['Alice', 'Bob', 'Charlie']
```

### Quick Calculations

```python
# Calculate areas
rectangles = [(3, 4), (5, 6), (2, 8)]
areas = list(map(lambda r: r[0] * r[1], rectangles))
print(areas)  # [12, 30, 16]

# Percentage calculation
scores = [85, 90, 78, 92]
percentages = list(map(lambda s: f"{s}%", scores))
print(percentages)  # ['85%', '90%', '78%', '92%']
```

### Dictionary Operations

```python
# Transform dictionary values
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}

# Apply 10% discount
discounted = {k: round(v * 0.9, 2) for k, v in prices.items()}
print(discounted)  # {'apple': 0.9, 'banana': 0.45, 'cherry': 1.8}

# Using lambda with dict comprehension
discounted = dict(map(lambda item: (item[0], item[1] * 0.9), prices.items()))
```

---

## 5. Lambda vs Regular Functions

### Comparison

| Aspect | Lambda | Regular Function |
|--------|--------|------------------|
| Name | Anonymous | Named |
| Lines | Single expression | Multiple lines |
| Return | Implicit | Explicit |
| Docstring | Not supported | Supported |
| Debugging | Harder | Easier |
| Reusability | Limited | High |

### When to Use Lambda

```python
# GOOD - Simple, one-time use
sorted(items, key=lambda x: x["name"])
list(map(lambda x: x * 2, numbers))
list(filter(lambda x: x > 0, numbers))
```

### When to Use Regular Function

```python
# GOOD - Complex logic, reusable
def calculate_discount(price, discount_rate):
    """Calculate discounted price."""
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount_rate)
```

### Readability Comparison

```python
# Lambda - Less readable for complex operations
result = list(filter(lambda x: x % 2 == 0 and x > 5 and x < 20, numbers))

# Regular function - More readable
def is_valid_even(x):
    """Check if x is even and between 5 and 20."""
    return x % 2 == 0 and 5 < x < 20

result = list(filter(is_valid_even, numbers))
```

---

## 6. Common Patterns

### Conditional Expression in Lambda

```python
# Ternary operator in lambda
classify = lambda x: "positive" if x > 0 else "non-positive"
print(classify(5))   # positive
print(classify(-3))  # non-positive

# More complex condition
grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade(85))  # B
```

### Immediately Invoked Lambda (IIFE)

```python
# Call lambda immediately
result = (lambda x, y: x + y)(3, 4)
print(result)  # 7
```

### Lambda in List Comprehension

```python
# Create list of functions
multipliers = [lambda x, n=n: x * n for n in range(1, 6)]
print(multipliers[2](10))  # 30 (10 * 3)
```

### Lambda with Multiple Lists

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Combine using map with lambda
combined = list(map(lambda x, y: x + y, list1, list2))
print(combined)  # [11, 22, 33]
```

---

## 7. Quick Reference

### Basic Syntax

| Pattern | Example |
|---------|---------|
| No args | `lambda: "hello"` |
| One arg | `lambda x: x * 2` |
| Two args | `lambda x, y: x + y` |
| Default arg | `lambda x=10: x * 2` |
| Conditional | `lambda x: "yes" if x else "no"` |

### Common Use Cases

| Function | Lambda Example |
|----------|----------------|
| `sorted()` | `sorted(list, key=lambda x: x[1])` |
| `map()` | `map(lambda x: x*2, list)` |
| `filter()` | `filter(lambda x: x>0, list)` |
| `reduce()` | `reduce(lambda a,b: a+b, list)` |
| `min()`/`max()` | `max(list, key=lambda x: x['val'])` |

### Lambda Limitations

| Cannot Do | Alternative |
|-----------|-------------|
| Multiple statements | Use regular function |
| Assignments | Use regular function |
| Docstrings | Use regular function |
| Complex logic | Use regular function |

### Best Practices

| Do | Don't |
|----|-------|
| Use for simple operations | Use for complex logic |
| Use with map/filter/sorted | Assign to variable and reuse |
| Keep expressions short | Nest multiple lambdas |
| Use for one-time operations | Use when docstring needed |

---

## Coverage Checklist

- [x] What lambda functions are
- [x] Basic syntax and examples
- [x] Lambda with sorted(), map(), filter(), reduce()
- [x] Practical examples
- [x] Lambda vs regular functions comparison
- [x] Common patterns
- [x] Quick reference tables
