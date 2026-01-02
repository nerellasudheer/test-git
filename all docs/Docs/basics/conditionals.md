# Python Conditionals - Complete Guide

Control program flow with if, elif, and else statements.

---

## Table of Contents

1. [Overview](#1-overview)
2. [if Statement](#2-if-statement)
3. [if-else Statement](#3-if-else-statement)
4. [if-elif-else Statement](#4-if-elif-else-statement)
5. [Nested Conditionals](#5-nested-conditionals)
6. [Ternary Operator](#6-ternary-operator)
7. [Truthy and Falsy Values](#7-truthy-and-falsy-values)
8. [Common Patterns](#8-common-patterns)
9. [Quick Reference](#9-quick-reference)

---

## 1. Overview

### What are Conditionals?

Conditionals allow your program to make decisions and execute different code based on conditions.

### Basic Structure

```python
if condition:
    # code executes if condition is True
elif another_condition:
    # code executes if another_condition is True
else:
    # code executes if all conditions are False
```

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater than or equal | `x >= 5` |
| `<=` | Less than or equal | `x <= 5` |

---

## 2. if Statement

### Basic Syntax

```python
age = 18

if age >= 18:
    print("You are an adult")
```

### Multiple Statements in if Block

```python
temperature = 35

if temperature > 30:
    print("It's hot outside")
    print("Stay hydrated")
    print("Wear light clothes")
```

### Single Line if (Not Recommended for Complex Logic)

```python
x = 10
if x > 5: print("x is greater than 5")
```

---

## 3. if-else Statement

### Basic Syntax

```python
age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")
```

### Practical Example

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

---

## 4. if-elif-else Statement

### Basic Syntax

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")
```

### Multiple elif Blocks

```python
day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
elif day == "Friday":
    print("Almost weekend!")
elif day == "Monday":
    print("Start of the week")
else:
    print("Regular weekday")
```

### Order Matters!

```python
# WRONG - First condition always matches
score = 95
if score >= 60:
    print("D")  # This prints even for 95!
elif score >= 90:
    print("A")  # Never reached

# CORRECT - Check highest first
score = 95
if score >= 90:
    print("A")  # Correct!
elif score >= 60:
    print("D")
```

---

## 5. Nested Conditionals

### Basic Nesting

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You are too young to drive")
```

### Better Alternative (Combine Conditions)

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
elif age >= 18 and not has_license:
    print("You need a license to drive")
else:
    print("You are too young to drive")
```

### Deep Nesting (Avoid When Possible)

```python
# Hard to read - avoid this
if condition1:
    if condition2:
        if condition3:
            do_something()

# Better - use combined conditions or early returns
if condition1 and condition2 and condition3:
    do_something()
```

---

## 6. Ternary Operator

### Basic Syntax

```python
# value_if_true if condition else value_if_false
result = "adult" if age >= 18 else "minor"
```

### Examples

```python
# Simple assignment
x = 10
status = "positive" if x > 0 else "non-positive"

# In print statement
print("Pass" if score >= 60 else "Fail")

# With function calls
def get_discount(is_member):
    return 0.2 if is_member else 0.0

# Nested ternary (avoid - hard to read)
result = "A" if score >= 90 else "B" if score >= 80 else "C"
```

### When to Use

| Use Ternary | Use if-else |
|-------------|-------------|
| Simple assignments | Complex logic |
| Short conditions | Multiple statements |
| Clear one-liners | Better readability |

---

## 7. Truthy and Falsy Values

### Falsy Values (Evaluate to False)

| Value | Type |
|-------|------|
| `False` | bool |
| `None` | NoneType |
| `0` | int |
| `0.0` | float |
| `""` | str (empty) |
| `[]` | list (empty) |
| `{}` | dict (empty) |
| `()` | tuple (empty) |
| `set()` | set (empty) |

### Examples

```python
# Using truthy/falsy
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")

# Check if list has items
items = [1, 2, 3]
if items:
    print("List has items")

# Check if dictionary is empty
data = {}
if not data:
    print("Dictionary is empty")
```

### Practical Use Cases

```python
# Default value pattern
user_input = input("Enter name: ")
name = user_input if user_input else "Anonymous"

# Check for None
result = some_function()
if result is not None:
    process(result)
```

---

## 8. Common Patterns

### Checking Multiple Values

```python
# Using 'in' for multiple comparisons
day = "Saturday"
if day in ["Saturday", "Sunday"]:
    print("Weekend!")

# Instead of
if day == "Saturday" or day == "Sunday":
    print("Weekend!")
```

### Range Checking

```python
age = 25

# Chained comparison (Pythonic)
if 18 <= age <= 65:
    print("Working age")

# Instead of
if age >= 18 and age <= 65:
    print("Working age")
```

### Checking Type

```python
value = "hello"

if isinstance(value, str):
    print("It's a string")
elif isinstance(value, int):
    print("It's an integer")
```

### None Checking

```python
# Check for None specifically
result = get_data()

if result is None:
    print("No data")

# Check for any falsy value
if not result:
    print("No data or empty")
```

### Guard Clauses (Early Exit)

```python
def process_user(user):
    # Guard clauses - exit early for invalid cases
    if user is None:
        return "No user provided"

    if not user.get("name"):
        return "User has no name"

    if user.get("age", 0) < 0:
        return "Invalid age"

    # Main logic here
    return f"Processing {user['name']}"
```

---

## 9. Quick Reference

### Syntax Summary

```python
# Simple if
if condition:
    code

# if-else
if condition:
    code
else:
    other_code

# if-elif-else
if condition1:
    code1
elif condition2:
    code2
else:
    code3

# Ternary
result = value1 if condition else value2
```

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater or equal |
| `<=` | Less or equal |
| `is` | Same object |
| `is not` | Different object |
| `in` | In sequence |
| `not in` | Not in sequence |

### Logical Operators

| Operator | Usage |
|----------|-------|
| `and` | Both conditions true |
| `or` | At least one true |
| `not` | Negate condition |

### Best Practices

| Practice | Example |
|----------|---------|
| Use `in` for multiple values | `if x in [1, 2, 3]` |
| Chain comparisons | `if 0 < x < 10` |
| Use `is` for None | `if x is None` |
| Keep conditions simple | Split complex logic |
| Use guard clauses | Early return for edge cases |

---

## Coverage Checklist

- [x] if statement basics
- [x] if-else statement
- [x] if-elif-else statement
- [x] Nested conditionals
- [x] Ternary operator
- [x] Truthy and falsy values
- [x] Common patterns
- [x] Best practices
- [x] Quick reference tables
