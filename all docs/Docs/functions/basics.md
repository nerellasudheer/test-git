# Python Functions - Complete Guide

Reusable blocks of code that perform specific tasks.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Defining Functions](#2-defining-functions)
3. [Parameters and Arguments](#3-parameters-and-arguments)
4. [Return Statement](#4-return-statement)
5. [Default Parameters](#5-default-parameters)
6. [Keyword Arguments](#6-keyword-arguments)
7. [Docstrings](#7-docstrings)
8. [Function Scope](#8-function-scope)
9. [Quick Reference](#9-quick-reference)

---

## 1. Overview

### What is a Function?

A function is a reusable block of code that performs a specific task. It helps organize code, reduce repetition, and improve readability.

### Why Use Functions?

| Benefit | Description |
|---------|-------------|
| Reusability | Write once, use many times |
| Organization | Break complex problems into smaller parts |
| Maintainability | Fix bugs in one place |
| Readability | Clear, named operations |
| Testing | Test individual components |

### Basic Syntax

```python
def function_name(parameters):
    """Docstring explaining the function."""
    # Function body
    return result
```

---

## 2. Defining Functions

### Simple Function (No Parameters)

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

### Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

### Function with Multiple Parameters

```python
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(5, 3)  # Output: 5 + 3 = 8
```

### Function Naming Rules

| Rule | Example |
|------|---------|
| Use lowercase | `calculate_sum` |
| Use underscores | `get_user_name` |
| Be descriptive | `calculate_area` not `ca` |
| Start with verb | `get_`, `set_`, `is_`, `has_` |

---

## 3. Parameters and Arguments

### Terminology

| Term | Description | Example |
|------|-------------|---------|
| Parameter | Variable in function definition | `def greet(name):` |
| Argument | Value passed when calling | `greet("Alice")` |

### Positional Arguments

Arguments matched by position:

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet("dog", "Max")      # I have a dog named Max
describe_pet("Max", "dog")      # I have a Max named dog (wrong!)
```

### Multiple Parameters

```python
def calculate(a, b, c):
    return a + b + c

result = calculate(1, 2, 3)  # 6
```

### Parameter Order

```python
def func(positional, *args, default=10, **kwargs):
    pass

# Order: positional → *args → default → **kwargs
```

---

## 4. Return Statement

### Returning a Value

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

### Return vs Print

```python
# Return - gives value back
def add_return(a, b):
    return a + b

x = add_return(2, 3)  # x = 5
print(x * 2)          # 10

# Print - only displays, returns None
def add_print(a, b):
    print(a + b)

y = add_print(2, 3)   # Prints: 5
print(y)              # None
```

### Multiple Return Values

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}, Sum: {total}")
# Min: 1, Max: 5, Sum: 15
```

### Early Return

```python
def check_age(age):
    if age < 0:
        return "Invalid age"
    if age < 18:
        return "Minor"
    return "Adult"

print(check_age(-5))  # Invalid age
print(check_age(15))  # Minor
print(check_age(25))  # Adult
```

### Return None

```python
def greet(name):
    print(f"Hello, {name}")
    # No return statement = returns None

result = greet("Alice")
print(result)  # None
```

---

## 5. Default Parameters

### Basic Default Values

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", "Welcome") # Welcome, Charlie!
```

### Multiple Defaults

```python
def create_user(name, age=0, city="Unknown"):
    return {"name": name, "age": age, "city": city}

user1 = create_user("Alice")
user2 = create_user("Bob", 25)
user3 = create_user("Charlie", 30, "NYC")

print(user1)  # {'name': 'Alice', 'age': 0, 'city': 'Unknown'}
print(user3)  # {'name': 'Charlie', 'age': 30, 'city': 'NYC'}
```

### Default Parameter Gotcha (Mutable Default)

```python
# WRONG - mutable default
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] - Bug! Should be ['b']

# CORRECT - use None
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b'] - Correct!
```

---

## 6. Keyword Arguments

### Using Keyword Arguments

```python
def describe_pet(animal, name, age):
    print(f"{name} is a {age}-year-old {animal}")

# Positional
describe_pet("dog", "Max", 5)

# Keyword (any order)
describe_pet(name="Max", age=5, animal="dog")

# Mixed (positional first, then keyword)
describe_pet("dog", age=5, name="Max")
```

### Benefits of Keyword Arguments

```python
# Clear intent
create_user(
    name="Alice",
    email="alice@example.com",
    is_admin=False,
    notify=True
)
```

### Keyword-Only Arguments (After *)

```python
def greet(name, *, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Alice", greeting="Hi")  # Works
# greet("Alice", "Hi")         # Error! greeting must be keyword
```

---

## 7. Docstrings

### What is a Docstring?

A documentation string that describes what a function does.

### Basic Docstring

```python
def add(a, b):
    """Add two numbers and return the result."""
    return a + b
```

### Detailed Docstring

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If length or width is negative.

    Example:
        >>> calculate_area(5, 3)
        15
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be non-negative")
    return length * width
```

### Accessing Docstrings

```python
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}")

# Access docstring
print(greet.__doc__)  # Greet a person by name.
help(greet)           # Shows full documentation
```

---

## 8. Function Scope

### Local Variables

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # 10
# print(x)     # Error! x doesn't exist outside
```

### Global Variables

```python
x = 10  # Global variable

def my_function():
    print(x)  # Can read global

my_function()  # 10
```

### Modifying Global Variables

```python
count = 0

def increment():
    global count  # Declare global
    count += 1

increment()
print(count)  # 1
```

### Local Shadows Global

```python
x = "global"

def my_function():
    x = "local"  # Creates new local variable
    print(x)

my_function()  # local
print(x)       # global (unchanged)
```

---

## 9. Quick Reference

### Function Definition

```python
def function_name(param1, param2=default):
    """Docstring."""
    # Body
    return result
```

### Parameter Types

| Type | Example | Description |
|------|---------|-------------|
| Positional | `def f(a, b)` | Required, ordered |
| Default | `def f(a=1)` | Optional with default |
| *args | `def f(*args)` | Variable positional |
| **kwargs | `def f(**kwargs)` | Variable keyword |
| Keyword-only | `def f(*, a)` | Must use keyword |

### Return Values

| Pattern | Example |
|---------|---------|
| Single value | `return x` |
| Multiple values | `return x, y, z` |
| None (implicit) | No return statement |
| Early exit | `return` in middle |

### Best Practices

| Practice | Why |
|----------|-----|
| Descriptive names | `calculate_total` not `ct` |
| Single responsibility | One task per function |
| Document with docstrings | Explain purpose |
| Avoid mutable defaults | Use `None` instead |
| Limit parameters | Max 4-5 usually |

### Common Patterns

```python
# Guard clause (early return)
def process(data):
    if not data:
        return None
    # Process data

# Factory function
def create_user(name):
    return {"name": name, "active": True}

# Validation function
def is_valid_email(email):
    return "@" in email and "." in email
```

---

## Coverage Checklist

- [x] Function definition syntax
- [x] Parameters vs arguments
- [x] Return statement and values
- [x] Default parameters
- [x] Keyword arguments
- [x] Docstrings
- [x] Function scope (local/global)
- [x] Best practices
- [x] Quick reference tables
