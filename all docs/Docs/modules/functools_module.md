# Python functools Module - Quick Reference

Higher-order functions and operations on callable objects.

---

## Table of Contents

1. [Overview](#1-overview)
2. [reduce()](#2-reduce)
3. [partial()](#3-partial)
4. [wraps()](#4-wraps)
5. [lru_cache()](#5-lru_cache)
6. [total_ordering](#6-total_ordering)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is functools?

A module for higher-order functions - functions that act on or return other functions.

### Import

```python
from functools import reduce, partial, wraps, lru_cache
```

---

## 2. reduce()

### What is reduce?

Applies a function cumulatively to items, reducing to single value.

### Basic Usage

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# How it works:
# ((((1+2)+3)+4)+5) = 15
```

### With Initial Value

```python
from functools import reduce

numbers = [1, 2, 3]

# Start with initial value 10
total = reduce(lambda acc, x: acc + x, numbers, 10)
print(total)  # 16 (10 + 1 + 2 + 3)
```

### Common Use Cases

```python
from functools import reduce

# Product of all numbers
product = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print(product)  # 24

# Find maximum
maximum = reduce(lambda a, b: a if a > b else b, [3, 1, 4, 1, 5])
print(maximum)  # 5

# Flatten nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, nested)
print(flat)  # [1, 2, 3, 4, 5, 6]
```

---

## 3. partial()

### What is partial?

Creates a new function with some arguments pre-filled.

### Basic Usage

```python
from functools import partial

def power(base, exp):
    return base ** exp

# Create specialized functions
square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(5))  # 25
print(cube(5))    # 125
```

### Practical Examples

```python
from functools import partial

# Pre-fill print options
debug_print = partial(print, "[DEBUG]", end="\n\n")
debug_print("Something happened")  # [DEBUG] Something happened

# Pre-fill int base
binary_to_int = partial(int, base=2)
print(binary_to_int("1010"))  # 10

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))  # 255
```

### With Methods

```python
from functools import partial

# Create multiplier functions
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(10))  # 20
print(triple(10))  # 30
```

---

## 4. wraps()

### What is wraps?

Preserves metadata of original function when creating decorators.

### Problem Without wraps

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet someone."""
    return f"Hello, {name}"

print(greet.__name__)  # wrapper (wrong!)
print(greet.__doc__)   # Wrapper docstring (wrong!)
```

### Solution With wraps

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserve original function metadata
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet someone."""
    return f"Hello, {name}"

print(greet.__name__)  # greet (correct!)
print(greet.__doc__)   # Greet someone. (correct!)
```

### Always Use wraps in Decorators

```python
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.2f}s")
        return result
    return wrapper
```

---

## 5. lru_cache()

### What is lru_cache?

Memoization decorator that caches function results.

### Basic Usage

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call calculates
print(fibonacci(100))  # Very fast!

# Check cache stats
print(fibonacci.cache_info())
```

### Without vs With Cache

```python
from functools import lru_cache
import time

# Without cache - SLOW
def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

# With cache - FAST
@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n-1) + fib_fast(n-2)

# fib_slow(35)  # Takes several seconds
# fib_fast(35)  # Instant!
```

### Cache Options

```python
from functools import lru_cache

@lru_cache(maxsize=128)  # Cache up to 128 results
def func1(x):
    pass

@lru_cache(maxsize=None)  # Unlimited cache
def func2(x):
    pass

@lru_cache  # Default: maxsize=128
def func3(x):
    pass

# Clear cache
func1.cache_clear()
```

---

## 6. total_ordering

### What is total_ordering?

Auto-generates comparison methods from `__eq__` and one other.

### Without total_ordering

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    def __le__(self, other):
        return self.grade <= other.grade

    def __gt__(self, other):
        return self.grade > other.grade

    def __ge__(self, other):
        return self.grade >= other.grade
```

### With total_ordering

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    # Other comparisons auto-generated!

s1 = Student("Alice", 85)
s2 = Student("Bob", 90)
print(s1 < s2)   # True
print(s1 <= s2)  # True (auto-generated)
print(s1 >= s2)  # False (auto-generated)
```

---

## 7. Quick Reference

### Main Functions

| Function | Purpose |
|----------|---------|
| `reduce(func, it)` | Reduce to single value |
| `partial(func, *args)` | Pre-fill arguments |
| `wraps(func)` | Preserve function metadata |
| `lru_cache(maxsize)` | Cache function results |
| `total_ordering` | Generate comparison methods |

### reduce() Pattern

```python
from functools import reduce
result = reduce(lambda acc, x: acc + x, items, initial)
```

### partial() Pattern

```python
from functools import partial
new_func = partial(original_func, arg1, kwarg=value)
```

### Decorator with wraps()

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### lru_cache() Pattern

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(arg):
    return compute(arg)
```

---

## Coverage Checklist

- [x] reduce() with examples
- [x] partial() for pre-filling
- [x] wraps() for decorators
- [x] lru_cache() for memoization
- [x] total_ordering for comparisons
- [x] Quick reference
