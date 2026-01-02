# Python Variable Scope - Quick Reference

Understanding where variables are accessible in Python using the LEGB rule.

---

## Table of Contents

1. [Overview](#1-overview)
2. [LEGB Rule](#2-legb-rule)
3. [Local Scope](#3-local-scope)
4. [Enclosing Scope](#4-enclosing-scope)
5. [Global Scope](#5-global-scope)
6. [Built-in Scope](#6-built-in-scope)
7. [Modifying Variables](#7-modifying-variables)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What is Variable Scope?

Variable scope determines **where** a variable can be accessed in your code. When you use a variable name, Python searches for it in a specific order.

### The LEGB Rule

Python uses the **LEGB** rule to look up variable names:

| Letter | Scope | Description |
|--------|-------|-------------|
| **L** | Local | Inside the current function |
| **E** | Enclosing | Inside enclosing (outer) functions |
| **G** | Global | At the module level |
| **B** | Built-in | Python's pre-defined names |

```
Search Order: Local → Enclosing → Global → Built-in
```

---

## 2. LEGB Rule

### How Python Finds Variables

When you reference a variable, Python searches in this order:

```python
# Built-in scope (B) - len, print, str, etc.
# Global scope (G) - top-level of script
x = "global"

def outer():
    # Enclosing scope (E) - outer function
    x = "enclosing"

    def inner():
        # Local scope (L) - current function
        x = "local"
        print(x)  # Python finds x in Local first

    inner()

outer()
# Output: local
```

### If Not Found Locally

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        # No local x, looks in Enclosing
        print(x)

    inner()

outer()
# Output: enclosing
```

### Complete Search Path

```python
# Built-in: len is available
# Global: x = "global"

x = "global"

def outer():
    # Enclosing: y = "enclosing"
    y = "enclosing"

    def inner():
        # Local: z = "local"
        z = "local"

        print(x)    # Found in Global
        print(y)    # Found in Enclosing
        print(z)    # Found in Local
        print(len)  # Found in Built-in

    inner()

outer()
```

---

## 3. Local Scope

### Definition

Variables created inside a function are **local** to that function.

```python
def my_function():
    x = 10  # Local variable
    print(x)  # Works: 10

my_function()
# print(x)  # NameError! x doesn't exist outside
```

### Each Call Creates New Local Variables

```python
def counter():
    count = 0  # New local variable each call
    count += 1
    return count

print(counter())  # 1
print(counter())  # 1 (not 2!)
```

### Local Variables Shadow Global

```python
x = "global"

def my_function():
    x = "local"  # Creates new local, doesn't change global
    print(x)

my_function()     # local
print(x)          # global (unchanged)
```

---

## 4. Enclosing Scope

### Definition

In nested functions, inner functions can access variables from outer (enclosing) functions.

```python
def outer():
    message = "Hello from outer"  # Enclosing scope

    def inner():
        # inner can access message
        print(message)

    inner()

outer()
# Output: Hello from outer
```

### Multiple Levels of Nesting

```python
def level_1():
    x = "level 1"

    def level_2():
        y = "level 2"

        def level_3():
            z = "level 3"
            # Can access all: x, y, z
            print(f"{x}, {y}, {z}")

        level_3()

    level_2()

level_1()
# Output: level 1, level 2, level 3
```

### Closures

Inner functions can "remember" enclosing variables even after the outer function returns.

```python
def make_multiplier(n):
    # n is in enclosing scope

    def multiplier(x):
        return x * n  # Remembers n

    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

---

## 5. Global Scope

### Definition

Variables defined at the top level of a script or module are **global**.

```python
# Global variable
PI = 3.14159

def calculate_area(radius):
    # Can read global variable
    return PI * radius ** 2

print(calculate_area(5))  # 78.53975
```

### Accessing Global Variables

```python
count = 0  # Global

def show_count():
    print(count)  # Reading global is OK

show_count()  # 0
```

### Global Variables Across Functions

```python
user_name = "Alice"  # Global

def greet():
    print(f"Hello, {user_name}")

def farewell():
    print(f"Goodbye, {user_name}")

greet()     # Hello, Alice
farewell()  # Goodbye, Alice
```

---

## 6. Built-in Scope

### Definition

Python comes with pre-defined names (functions, types, exceptions) that are always available.

### Common Built-ins

| Type | Examples |
|------|----------|
| Functions | `print`, `len`, `range`, `input`, `type` |
| Types | `str`, `int`, `float`, `list`, `dict` |
| Values | `True`, `False`, `None` |
| Exceptions | `ValueError`, `TypeError`, `NameError` |

```python
# All these are built-in
print("Hello")
length = len([1, 2, 3])
numbers = list(range(5))
```

### Shadowing Built-ins (Avoid This!)

```python
# BAD: Don't do this!
list = [1, 2, 3]  # Shadows built-in list
# Now you can't use list() function!
# new_list = list("hello")  # TypeError!

# Fix: Use different name
my_list = [1, 2, 3]  # Better
```

### View All Built-ins

```python
import builtins
print(dir(builtins))  # Shows all built-in names
```

---

## 7. Modifying Variables

### The Problem

By default, you **cannot modify** outer scope variables from inner scopes:

```python
x = 10  # Global

def change_x():
    x = 20  # Creates NEW local variable!

change_x()
print(x)  # Still 10!
```

### global Keyword

Use `global` to modify a global variable inside a function:

```python
count = 0

def increment():
    global count  # Tell Python to use global count
    count += 1

increment()
increment()
print(count)  # 2
```

### nonlocal Keyword

Use `nonlocal` to modify an enclosing (but not global) variable:

```python
def outer():
    x = 10

    def inner():
        nonlocal x  # Tell Python to use enclosing x
        x = 20

    inner()
    print(x)  # 20 (modified!)

outer()
```

### Comparison

| Keyword | Scope Modified | Example Use |
|---------|---------------|-------------|
| `global` | Module-level (global) | Counters, configuration |
| `nonlocal` | Enclosing function | Closures, nested functions |

### When to Use (and When Not To)

```python
# AVOID global when possible - makes code harder to understand

# Instead, use parameters and return values:
def increment(count):
    return count + 1

count = 0
count = increment(count)
count = increment(count)
print(count)  # 2
```

---

## 8. Quick Reference

### LEGB Summary

| Scope | Location | Example |
|-------|----------|---------|
| Local | Inside current function | Function variables |
| Enclosing | Inside outer function(s) | Nested function variables |
| Global | Module/script top-level | Variables outside functions |
| Built-in | Python's pre-defined | `print`, `len`, `True` |

### Keywords

| Keyword | Purpose |
|---------|---------|
| `global` | Modify global variable in function |
| `nonlocal` | Modify enclosing variable in nested function |

### Scope Rules

| Rule | Description |
|------|-------------|
| Read | Can read from outer scopes |
| Write | Creates new local by default |
| Modify outer | Need `global` or `nonlocal` |

### Best Practices

| Practice | Reason |
|----------|--------|
| Avoid `global` | Makes code harder to understand |
| Use parameters | Pass values explicitly |
| Return values | Instead of modifying global state |
| Don't shadow built-ins | Don't name variables `list`, `str`, etc. |

### Complete Example

```python
# Built-in: print, len, range

# Global scope
name = "Global"

def outer():
    # Enclosing scope
    name = "Enclosing"

    def inner():
        # Local scope
        name = "Local"
        print(f"Local: {name}")

    inner()
    print(f"Enclosing: {name}")

outer()
print(f"Global: {name}")

# Output:
# Local: Local
# Enclosing: Enclosing
# Global: Global
```

---

## Coverage Checklist

- [x] LEGB rule explained
- [x] Local scope with examples
- [x] Enclosing scope and closures
- [x] Global scope
- [x] Built-in scope
- [x] global and nonlocal keywords
- [x] Best practices
- [x] Quick reference tables
