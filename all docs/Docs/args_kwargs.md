# Python *args and **kwargs - Complete Guide

A comprehensive reference for handling variable arguments in Python functions.

---

## Table of Contents

1. [Overview](#1-overview)
2. [*args - Positional Arguments](#2-args---positional-arguments)
3. [**kwargs - Keyword Arguments](#3-kwargs---keyword-arguments)
4. [Using with Classes](#4-using-with-classes)
5. [Combining *args and **kwargs](#5-combining-args-and-kwargs)
6. [Unpacking Arguments](#6-unpacking-arguments)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What are *args and **kwargs?

| Syntax | Name | Purpose | Storage |
|--------|------|---------|---------|
| `*args` | Arguments | Accept unlimited positional arguments | Tuple |
| `**kwargs` | Keyword Arguments | Accept unlimited keyword arguments | Dictionary |

The names `args` and `kwargs` are conventions. You can use any name like `*numbers` or `**options`.

---

## 2. *args - Positional Arguments

### Definition

`*args` allows a function to accept any number of positional arguments, stored in a tuple.

### Basic Example

```python
def add_numbers(*args):
    print(type(args))  # <class 'tuple'>
    print(args)
    return sum(args)

result1 = add_numbers(10, 20)       # 30
result2 = add_numbers(10, 20, 30)   # 60
result3 = add_numbers(5)            # 5
```

### Why Tuple?

Tuples are immutable, which protects the arguments from accidental modification.

```python
def show_args(*args):
    print(f"Args: {args}")
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")

show_args('apple', 'banana', 'orange')
# Output:
# Args: ('apple', 'banana', 'orange')
# Argument 0: apple
# Argument 1: banana
# Argument 2: orange
```

### Combining with Regular Parameters

Regular parameters must come before `*args`:

```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "John", "Sarah", "Mike")
# Output:
# Hello, John!
# Hello, Sarah!
# Hello, Mike!
```

---

## 3. **kwargs - Keyword Arguments

### Definition

`**kwargs` allows a function to accept any number of keyword arguments, stored in a dictionary.

### Basic Example

```python
def display_info(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="John", age=25, city="New York")
# Output:
# {'name': 'John', 'age': 25, 'city': 'New York'}
# name: John
# age: 25
# city: New York
```

### Using .get() for Safe Access

Prevents KeyError when optional parameters are not provided:

```python
def create_user(**kwargs):
    name = kwargs.get('name', 'Anonymous')
    age = kwargs.get('age', 'Not specified')
    city = kwargs.get('city', 'Unknown')

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# All parameters
create_user(name="John", age=25, city="NY")
# Name: John, Age: 25, City: NY

# Missing parameters (uses defaults)
create_user(name="Sarah")
# Name: Sarah, Age: Not specified, City: Unknown
```

---

## 4. Using with Classes

### Class with **kwargs

```python
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Unknown')
        self.age = kwargs.get('age', 0)
        self.city = kwargs.get('city', 'Not specified')

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

# Full details
person1 = Person(name="John", age=25, city="NY")
person1.display()

# Partial details (uses defaults)
person2 = Person(name="Sarah")
person2.display()
```

### Dynamic Attribute Assignment

```python
class Configuration:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def show_config(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

config = Configuration(
    host="localhost",
    port=8080,
    debug=True
)
config.show_config()
# host: localhost
# port: 8080
# debug: True
```

---

## 5. Combining *args and **kwargs

### Parameter Order

Parameters must be in this order:

1. Regular positional parameters
2. `*args`
3. Keyword-only parameters
4. `**kwargs`

```python
def complex_function(required, *args, keyword_only="default", **kwargs):
    print(f"Required: {required}")
    print(f"Args (tuple): {args}")
    print(f"Keyword only: {keyword_only}")
    print(f"Kwargs (dict): {kwargs}")

complex_function(
    "mandatory",           # required
    10, 20, 30,            # *args
    keyword_only="custom", # keyword_only
    name="John",           # **kwargs
    age=25                 # **kwargs
)
```

### Practical Example: Logger

```python
class Logger:
    def log(self, level, message, *tags, **metadata):
        print(f"[{level}] {message}")

        if tags:
            print(f"Tags: {', '.join(tags)}")

        if metadata:
            print("Metadata:")
            for key, value in metadata.items():
                print(f"  {key}: {value}")

logger = Logger()
logger.log("ERROR", "Database failed",
           "database", "critical",
           server="db-01",
           error_code=500)
```

---

## 6. Unpacking Arguments

### Unpacking Lists/Tuples with *

```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

# Without unpacking - ERROR
# result = add(numbers)

# With unpacking
result = add(*numbers)  # Same as add(10, 20, 30)
print(result)  # 60
```

### Unpacking Dictionaries with **

```python
def create_user(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

user_data = {'name': 'John', 'age': 25, 'city': 'NY'}

# Without unpacking - ERROR
# create_user(user_data)

# With unpacking
create_user(**user_data)  # Same as create_user(name='John', age=25, city='NY')
```

---

## 7. Quick Reference

### Comparison Table

| Feature | Regular Parameters | *args | **kwargs |
|---------|-------------------|-------|----------|
| Number | Fixed count | Unlimited | Unlimited |
| Type | Positional | Positional | Keyword |
| Storage | Individual variables | Tuple | Dictionary |
| Access | By variable name | By index | By key |
| Optional | Can have defaults | Always optional | Always optional |

### Parameter Order Template

```python
def function(
    positional,          # 1. Regular positional
    *args,               # 2. Unlimited positional
    keyword_only,        # 3. Keyword-only
    **kwargs             # 4. Unlimited keyword
):
    pass
```

### *args Summary

| Aspect | Description |
|--------|-------------|
| Purpose | Accept unlimited positional arguments |
| Storage | Tuple (immutable) |
| Access | By index (`args[0]`) |
| Use Case | Unknown number of arguments |

### **kwargs Summary

| Aspect | Description |
|--------|-------------|
| Purpose | Accept unlimited keyword arguments |
| Storage | Dictionary (key-value pairs) |
| Access | By key (`kwargs['name']` or `kwargs.get('name')`) |
| Use Case | Flexible named parameters |

### Common Use Cases

- **Decorators**: Pass any arguments to wrapped function
- **Class Inheritance**: Flexible parameter passing
- **API Wrappers**: Handle variable parameters
- **Configuration**: Flexible settings and options

---

## Coverage Checklist

- [x] *args definition and usage
- [x] **kwargs definition and usage
- [x] Using .get() with kwargs
- [x] Classes with **kwargs
- [x] Combining *args and **kwargs
- [x] Unpacking with * and **
- [x] Parameter order rules
- [x] Quick reference tables
