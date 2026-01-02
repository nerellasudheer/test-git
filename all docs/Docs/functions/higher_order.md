# Python Higher-Order Functions - Complete Guide

Functions that take functions as arguments or return functions.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Functions as Arguments](#2-functions-as-arguments)
3. [Functions as Return Values](#3-functions-as-return-values)
4. [Lambda Functions](#4-lambda-functions)
5. [Built-in Higher-Order Functions](#5-built-in-higher-order-functions)
6. [Closures](#6-closures)
7. [Practical Examples](#7-practical-examples)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What is a Higher-Order Function?

A higher-order function is a function that:
1. Takes one or more functions as arguments, OR
2. Returns a function as its result

### Why Use Higher-Order Functions?

| Benefit | Description |
|---------|-------------|
| Abstraction | Separate "what" from "how" |
| Reusability | Write generic functions |
| Flexibility | Change behavior by passing different functions |
| Cleaner Code | Reduce repetition |

### Simple Example

```python
def apply_operation(x, y, operation):
    """Higher-order function - takes function as argument."""
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Pass different functions
print(apply_operation(5, 3, add))      # 8
print(apply_operation(5, 3, multiply)) # 15
```

---

## 2. Functions as Arguments

### Basic Pattern

```python
def execute(func, value):
    """Executes func with value."""
    return func(value)

def double(x):
    return x * 2

def square(x):
    return x ** 2

print(execute(double, 5))  # 10
print(execute(square, 5))  # 25
```

### Process List with Custom Function

```python
def process_list(items, func):
    """Apply func to each item."""
    result = []
    for item in items:
        result.append(func(item))
    return result

numbers = [1, 2, 3, 4, 5]

print(process_list(numbers, double))  # [2, 4, 6, 8, 10]
print(process_list(numbers, square))  # [1, 4, 9, 16, 25]
print(process_list(numbers, str))     # ['1', '2', '3', '4', '5']
```

### Sorting with Key Function

```python
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade using key function
def get_grade(student):
    return student["grade"]

sorted_students = sorted(students, key=get_grade)
print([s["name"] for s in sorted_students])
# ['Charlie', 'Alice', 'Bob']

# With lambda (more concise)
sorted_students = sorted(students, key=lambda s: s["grade"])
```

---

## 3. Functions as Return Values

### Basic Factory Pattern

```python
def create_multiplier(n):
    """Returns a function that multiplies by n."""
    def multiplier(x):
        return x * n
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
print(double(10))  # 20
```

### Create Custom Validators

```python
def create_validator(min_val, max_val):
    """Returns a validation function."""
    def validate(value):
        return min_val <= value <= max_val
    return validate

age_validator = create_validator(0, 120)
percentage_validator = create_validator(0, 100)

print(age_validator(25))         # True
print(age_validator(150))        # False
print(percentage_validator(85))  # True
```

### Create Formatters

```python
def create_formatter(prefix, suffix=""):
    """Returns a formatting function."""
    def format_value(value):
        return f"{prefix}{value}{suffix}"
    return format_value

format_price = create_formatter("$", " USD")
format_percent = create_formatter("", "%")

print(format_price(99.99))    # $99.99 USD
print(format_percent(75))     # 75%
```

---

## 4. Lambda Functions

### What is Lambda?

A lambda is a small anonymous function defined in one line.

### Basic Syntax

```python
# Regular function
def add(a, b):
    return a + b

# Lambda equivalent
add = lambda a, b: a + b

print(add(5, 3))  # 8
```

### Lambda with Higher-Order Functions

```python
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Sort by custom key
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)  # ['apple', 'banana', 'cherry']
```

### Lambda Use Cases

| Use Case | Example |
|----------|---------|
| Sort key | `sorted(list, key=lambda x: x[1])` |
| Map transform | `map(lambda x: x*2, list)` |
| Filter condition | `filter(lambda x: x>0, list)` |
| Quick callback | `button.on_click(lambda: print("clicked"))` |

### Lambda vs Regular Function

| Use Lambda | Use Regular Function |
|------------|---------------------|
| Simple one-line operation | Multiple lines needed |
| Used once | Reused multiple times |
| With map/filter/sorted | Need docstring |
| Quick callback | Complex logic |

---

## 5. Built-in Higher-Order Functions

### map() - Transform Each Element

```python
# Syntax: map(function, iterable)
numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # [11, 22, 33]
```

### filter() - Select Elements

```python
# Syntax: filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Get positive numbers
nums = [-2, -1, 0, 1, 2]
positive = list(filter(lambda x: x > 0, nums))
print(positive)  # [1, 2]
```

### reduce() - Accumulate to Single Value

```python
from functools import reduce

# Syntax: reduce(function, iterable, initial)
numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# Product of all numbers
product = reduce(lambda acc, x: acc * x, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda acc, x: x if x > acc else acc, numbers)
print(maximum)  # 5
```

### sorted() with Key

```python
# Sort by custom criteria
data = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

# Sort by age
by_age = sorted(data, key=lambda x: x[1])
print(by_age)  # [('Charlie', 20), ('Alice', 25), ('Bob', 30)]

# Sort by name
by_name = sorted(data, key=lambda x: x[0])
print(by_name)  # [('Alice', 25), ('Bob', 30), ('Charlie', 20)]
```

---

## 6. Closures

### What is a Closure?

A closure is a function that remembers values from its enclosing scope, even after that scope has finished executing.

### Basic Closure

```python
def outer(x):
    # x is captured by inner function
    def inner(y):
        return x + y  # x is remembered
    return inner

add_5 = outer(5)
add_10 = outer(10)

print(add_5(3))   # 8  (5 + 3)
print(add_10(3))  # 13 (10 + 3)
```

### Closure as Counter

```python
def create_counter():
    count = 0

    def counter():
        nonlocal count  # Modify enclosing variable
        count += 1
        return count

    return counter

counter = create_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### Closure for Configuration

```python
def create_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

error_log = create_logger("ERROR")
info_log = create_logger("INFO")

error_log("Something went wrong")  # [ERROR] Something went wrong
info_log("Application started")    # [INFO] Application started
```

---

## 7. Practical Examples

### Custom Decorator (Higher-Order Function)

```python
def timer(func):
    """Decorator to measure execution time."""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

slow_function()  # slow_function took 1.0012s
```

### Event Handler System

```python
def create_event_handler():
    handlers = []

    def add_handler(func):
        handlers.append(func)

    def trigger(event):
        for handler in handlers:
            handler(event)

    return add_handler, trigger

on_click, click = create_event_handler()

# Add handlers
on_click(lambda e: print(f"Handler 1: {e}"))
on_click(lambda e: print(f"Handler 2: {e}"))

# Trigger event
click("button pressed")
# Handler 1: button pressed
# Handler 2: button pressed
```

### Pipeline Processing

```python
def pipeline(*functions):
    """Create a pipeline of functions."""
    def process(value):
        result = value
        for func in functions:
            result = func(result)
        return result
    return process

# Create processing pipeline
process_text = pipeline(
    str.strip,
    str.lower,
    lambda s: s.replace(" ", "_")
)

print(process_text("  Hello World  "))  # "hello_world"
```

---

## 8. Quick Reference

### Higher-Order Function Types

| Type | Description | Example |
|------|-------------|---------|
| Function as argument | Pass function to another | `sorted(list, key=func)` |
| Function as return | Return a function | `def outer(): return inner` |
| Both | Take and return function | Decorators |

### Lambda Syntax

```python
# Syntax
lambda arguments: expression

# Examples
lambda x: x * 2
lambda x, y: x + y
lambda: print("hello")
```

### Built-in Higher-Order Functions

| Function | Purpose | Signature |
|----------|---------|-----------|
| `map()` | Transform each | `map(func, iterable)` |
| `filter()` | Select matching | `filter(func, iterable)` |
| `reduce()` | Accumulate | `reduce(func, iterable)` |
| `sorted()` | Sort with key | `sorted(iterable, key=func)` |
| `min()/max()` | Find extreme | `min(iterable, key=func)` |

### Closure Pattern

```python
def create_func(config):
    def inner(arg):
        return config + arg  # config is captured
    return inner
```

### Common Patterns

| Pattern | Use Case |
|---------|----------|
| Factory | Create configured functions |
| Decorator | Add behavior to functions |
| Callback | Event handling |
| Pipeline | Chain transformations |
| Memoization | Cache results |

---

## Coverage Checklist

- [x] What higher-order functions are
- [x] Functions as arguments
- [x] Functions as return values
- [x] Lambda functions
- [x] map(), filter(), reduce()
- [x] Closures and nested functions
- [x] Practical examples
- [x] Quick reference tables
