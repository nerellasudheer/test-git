# Python Decorators - Complete Guide

A comprehensive reference for understanding and using decorators in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic Decorator Structure](#2-basic-decorator-structure)
3. [Types of Decorators](#3-types-of-decorators)
4. [Decorators with Arguments](#4-decorators-with-arguments)
5. [Preserving Function Metadata](#5-preserving-function-metadata)
6. [Common Use Cases](#6-common-use-cases)
7. [Built-in Decorators](#7-built-in-decorators)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What is a Decorator?

A decorator is a function that takes another function as an argument, adds some functionality to it, and returns the enhanced function. It allows you to modify or extend behavior without permanently changing the original function's source code.

### Syntax

```python
@decorator_function
def original_function():
    pass
```

This is **syntactic sugar** for:

```python
def original_function():
    pass

original_function = decorator_function(original_function)
```

### Why Use Decorators?

- **DRY Principle**: Don't Repeat Yourself - add common functionality once
- **Separation of Concerns**: Keep core logic separate from cross-cutting concerns
- **Clean Code**: More readable than nested function calls
- **Reusability**: Apply same enhancement to multiple functions

---

## 2. Basic Decorator Structure

### Anatomy of a Decorator

```python
def my_decorator(func):
    """The decorator function receives the original function."""

    def wrapper(*args, **kwargs):
        """The wrapper adds functionality around the original."""
        # Code to run BEFORE the original function
        print("Before function call")

        result = func(*args, **kwargs)  # Call the original function

        # Code to run AFTER the original function
        print("After function call")

        return result  # Return the original function's result

    return wrapper  # Return the wrapper function
```

### Simple Example

```python
def simple_decorator(func):
    def wrapper():
        print("--- STARTING ---")
        func()
        print("--- ENDING ---")
    return wrapper

@simple_decorator
def greet():
    print("Hello, Python!")

# Calling the decorated function
greet()

# Output:
# --- STARTING ---
# Hello, Python!
# --- ENDING ---
```

### Decorator with Arguments Support

```python
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

result = add(3, 5)
# Output: Arguments: (3, 5), {}
print(result)  # 8
```

---

## 3. Types of Decorators

### 1. Function Decorators

The most common type - decorates standalone functions.

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def calculate(x, y):
    return x * y

calculate(4, 5)
# Output: Calling: calculate
```

### 2. Class Method Decorators

Decorators that work with class methods.

```python
def validate_positive(func):
    def wrapper(self, value):
        if value < 0:
            raise ValueError("Value must be positive")
        return func(self, value)
    return wrapper

class BankAccount:
    def __init__(self):
        self.balance = 0

    @validate_positive
    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount()
account.deposit(100)   # Works
# account.deposit(-50) # Raises ValueError
```

### 3. Class Decorators

Decorators that modify entire classes.

```python
def add_greeting(cls):
    cls.greet = lambda self: f"Hello from {self.__class__.__name__}!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.greet())  # Hello from Person!
```

---

## 4. Decorators with Arguments

### Decorator Factory Pattern

When you need to pass arguments to a decorator, you create a "decorator factory" - a function that returns the actual decorator.

```python
def repeat(num_times):
    """Decorator factory - takes arguments and returns decorator."""

    def decorator(func):
        """The actual decorator."""

        def wrapper(*args, **kwargs):
            """The wrapper that adds functionality."""
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Hello!
# Hello!
# Hello!
```

### Practical Example: Retry Decorator

```python
import time

def retry(max_attempts, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts < max_attempts:
                        time.sleep(delay)
            raise Exception(f"Failed after {max_attempts} attempts")
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unstable_function():
    # Simulating an unstable operation
    import random
    if random.random() < 0.7:
        raise ConnectionError("Connection failed")
    return "Success!"
```

---

## 5. Preserving Function Metadata

### The Problem

Without proper handling, decorated functions lose their original metadata:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """This is the example function."""
    pass

print(example.__name__)  # 'wrapper' (not 'example'!)
print(example.__doc__)   # None (not the docstring!)
```

### The Solution: functools.wraps

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """This is the example function."""
    pass

print(example.__name__)  # 'example' (correct!)
print(example.__doc__)   # 'This is the example function.' (correct!)
```

### Best Practice Template

```python
import functools

def decorator_template(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Pre-processing
        result = func(*args, **kwargs)
        # Post-processing
        return result
    return wrapper
```

---

## 6. Common Use Cases

### Logging

```python
import functools
import logging

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper
```

### Timing/Performance

```python
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"
```

### Access Control

```python
import functools

def require_auth(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("Authentication required")
        return func(user, *args, **kwargs)
    return wrapper

def require_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if role not in user.roles:
                raise PermissionError(f"Role '{role}' required")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
```

### Caching/Memoization

```python
import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Much faster than non-memoized version
print(fibonacci(100))
```

### Input Validation

```python
import functools

def validate_types(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type}, got {type(arg)}")
            return func(*args)
        return wrapper
    return decorator

@validate_types(int, int)
def add(a, b):
    return a + b

add(1, 2)      # Works
# add("1", 2)  # Raises TypeError
```

---

## 7. Built-in Decorators

### @staticmethod

Defines a method that doesn't receive implicit first argument.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

Math.add(3, 5)  # 8
```

### @classmethod

Defines a method that receives the class as first argument.

```python
class Dog:
    species = "Canis familiaris"

    @classmethod
    def get_species(cls):
        return cls.species

Dog.get_species()  # "Canis familiaris"
```

### @property

Defines a method accessible as an attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

c = Circle(5)
print(c.diameter)  # 10 (accessed without parentheses)
```

### @functools.lru_cache

Built-in memoization decorator.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## 8. Quick Reference

### Decorator Patterns

| Pattern | Structure | Use Case |
|---------|-----------|----------|
| Basic | `@decorator` | Simple enhancement |
| With arguments | `@decorator(arg)` | Configurable behavior |
| Stacked | `@dec1` `@dec2` | Multiple enhancements |
| Class decorator | `@decorator` on class | Modify class behavior |

### Execution Order (Stacked Decorators)

```python
@decorator1
@decorator2
def func():
    pass

# Equivalent to:
func = decorator1(decorator2(func))
# decorator2 wraps func first, then decorator1 wraps that
```

### Common Built-in Decorators

| Decorator | Module | Purpose |
|-----------|--------|---------|
| `@staticmethod` | built-in | Method without self/cls |
| `@classmethod` | built-in | Method with cls |
| `@property` | built-in | Attribute-like method access |
| `@functools.wraps` | functools | Preserve function metadata |
| `@functools.lru_cache` | functools | Memoization with LRU cache |
| `@dataclass` | dataclasses | Auto-generate class methods |

### Must-Know Points

| Point | Description |
|-------|-------------|
| Return value | Decorator must return a function (usually wrapper) |
| `*args, **kwargs` | Use to accept any arguments |
| `@functools.wraps` | Always use to preserve metadata |
| Order matters | Decorators apply bottom-to-top |
| Parentheses | `@decorator` vs `@decorator()` are different |

### Template

```python
import functools

def decorator_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Before
        result = func(*args, **kwargs)
        # After
        return result
    return wrapper
```

---

## Coverage Checklist

- [x] Definition and syntax
- [x] Basic decorator structure
- [x] Types of decorators
- [x] Decorators with arguments
- [x] Preserving metadata with functools.wraps
- [x] Common use cases with examples
- [x] Built-in decorators
- [x] Quick reference tables
