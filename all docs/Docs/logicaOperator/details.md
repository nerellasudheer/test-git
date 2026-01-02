# Python Logical Operators - Quick Reference

Understanding `and`, `or`, and `not` operators in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [and Operator](#2-and-operator)
3. [or Operator](#3-or-operator)
4. [not Operator](#4-not-operator)
5. [Operator Precedence](#5-operator-precedence)
6. [Short-Circuit Evaluation](#6-short-circuit-evaluation)
7. [Practical Examples](#7-practical-examples)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What are Logical Operators?

Logical operators combine conditional statements and evaluate to either `True` or `False`. They are essential for creating complex conditions in if statements, while loops, and other control flow structures.

### The Three Logical Operators

| Operator | Description | Returns True When |
|----------|-------------|-------------------|
| `and` | Logical AND | Both conditions are True |
| `or` | Logical OR | At least one condition is True |
| `not` | Logical NOT | The condition is False |

---

## 2. and Operator

### Basic Syntax

Returns `True` if **both** statements are true.

```python
x = 5
print(x > 3 and x < 10)  # True (both conditions are True)
print(x > 3 and x > 10)  # False (second condition is False)
```

### Truth Table

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Multiple Conditions

```python
age = 25
has_license = True
has_car = True

# All conditions must be True
can_drive = age >= 18 and has_license and has_car
print(can_drive)  # True
```

### With Non-Boolean Values

`and` returns the first falsy value, or the last value if all are truthy:

```python
print(5 and 10)       # 10 (returns last truthy value)
print(0 and 10)       # 0 (returns first falsy value)
print("" and "hello") # "" (empty string is falsy)
print("hi" and "bye") # "bye" (returns last truthy value)
```

---

## 3. or Operator

### Basic Syntax

Returns `True` if **at least one** statement is true.

```python
x = 5
print(x > 3 or x > 10)  # True (first condition is True)
print(x < 3 or x > 10)  # False (both conditions are False)
```

### Truth Table

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Multiple Conditions

```python
is_admin = False
is_moderator = True
is_owner = False

# At least one must be True
has_access = is_admin or is_moderator or is_owner
print(has_access)  # True
```

### With Non-Boolean Values

`or` returns the first truthy value, or the last value if all are falsy:

```python
print(5 or 10)        # 5 (returns first truthy value)
print(0 or 10)        # 10 (skips falsy, returns truthy)
print("" or "hello")  # "hello"
print(0 or "" or None)# None (all falsy, returns last)
```

### Default Value Pattern

```python
# Common pattern for default values
name = "" or "Anonymous"
print(name)  # "Anonymous"

user_input = None
username = user_input or "Guest"
print(username)  # "Guest"
```

---

## 4. not Operator

### Basic Syntax

Reverses the boolean value - returns `False` if true, `True` if false.

```python
x = 5
print(not(x > 3))           # False (x > 3 is True, not reverses it)
print(not(x > 10))          # True (x > 10 is False, not reverses it)
print(not(x > 3 and x < 10))# False
```

### Truth Table

| A | not A |
|---|-------|
| True | False |
| False | True |

### Practical Uses

```python
# Check if list is empty
my_list = []
if not my_list:
    print("List is empty")  # This prints

# Check if value is None
value = None
if not value:
    print("Value is not set")  # This prints

# Negate a condition
logged_in = False
if not logged_in:
    print("Please log in")  # This prints
```

### With Comparison Operators

```python
# Instead of not equal check
x = 5
print(not x == 10)  # True (but use x != 10 instead)
print(x != 10)      # True (preferred)

# Check if not in list
fruits = ["apple", "banana"]
print("cherry" not in fruits)  # True
print(not "apple" in fruits)   # False (less readable)
```

---

## 5. Operator Precedence

### Order of Evaluation

Logical operators have a specific precedence order:

| Priority | Operator | Description |
|----------|----------|-------------|
| 1 (Highest) | `not` | Evaluated first |
| 2 | `and` | Evaluated second |
| 3 (Lowest) | `or` | Evaluated last |

### Example

```python
# Without parentheses
result = True or False and False
print(result)  # True

# Evaluation order: and first, then or
# Step 1: False and False = False
# Step 2: True or False = True
```

### Using Parentheses for Clarity

```python
# Explicit grouping (recommended)
result = (True or False) and False
print(result)  # False

# Clear intentions
age = 25
is_student = True
has_id = True

# Without parentheses (confusing)
can_enter = age >= 18 or is_student and has_id

# With parentheses (clear)
can_enter = (age >= 18) or (is_student and has_id)
```

---

## 6. Short-Circuit Evaluation

### What is Short-Circuit Evaluation?

Python stops evaluating as soon as the result is determined.

### and Short-Circuit

If the first condition is `False`, Python doesn't check the second:

```python
def check_a():
    print("Checking A")
    return False

def check_b():
    print("Checking B")
    return True

# check_b() is never called!
result = check_a() and check_b()
# Output: Checking A
# result = False
```

### or Short-Circuit

If the first condition is `True`, Python doesn't check the second:

```python
def check_a():
    print("Checking A")
    return True

def check_b():
    print("Checking B")
    return True

# check_b() is never called!
result = check_a() or check_b()
# Output: Checking A
# result = True
```

### Practical Use

```python
# Safe dictionary access
data = {"name": "Alice"}
if "age" in data and data["age"] > 18:
    print("Adult")
# If "age" not in data, second condition is not evaluated
# This prevents KeyError

# Safe division
x = 0
if x != 0 and 10/x > 2:
    print("Result is greater than 2")
# Division is not attempted because x != 0 is False
```

---

## 7. Practical Examples

### Login Validation

```python
def validate_login(username, password):
    valid_username = len(username) >= 3
    valid_password = len(password) >= 8

    if valid_username and valid_password:
        return "Login successful"
    elif not valid_username and not valid_password:
        return "Both username and password are invalid"
    elif not valid_username:
        return "Username too short"
    else:
        return "Password too short"
```

### Grade Calculator

```python
def get_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"

# Using chained comparison (cleaner)
def get_grade_v2(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    # ... etc
```

### Access Control

```python
def check_access(user):
    is_admin = user.get("role") == "admin"
    is_owner = user.get("is_owner", False)
    is_verified = user.get("verified", False)

    # Admin or owner always has access
    # Regular users need to be verified
    if is_admin or is_owner:
        return True
    elif is_verified:
        return True
    else:
        return False

# Simplified
def check_access_v2(user):
    return (user.get("role") == "admin" or
            user.get("is_owner", False) or
            user.get("verified", False))
```

### Input Validation

```python
def validate_email(email):
    # Must have @ and at least one dot after @
    has_at = "@" in email
    has_dot_after_at = "." in email.split("@")[-1] if "@" in email else False
    not_empty = len(email) > 0

    return not_empty and has_at and has_dot_after_at

print(validate_email("test@example.com"))  # True
print(validate_email("invalid-email"))     # False
```

---

## 8. Quick Reference

### Summary Table

| Operator | Syntax | Returns True When |
|----------|--------|-------------------|
| `and` | `a and b` | Both a and b are True |
| `or` | `a or b` | At least one is True |
| `not` | `not a` | a is False |

### With Non-Boolean Values

| Expression | Result | Reason |
|------------|--------|--------|
| `5 and 10` | `10` | Returns last truthy |
| `0 and 10` | `0` | Returns first falsy |
| `5 or 10` | `5` | Returns first truthy |
| `0 or 10` | `10` | Returns first truthy |
| `not 0` | `True` | 0 is falsy |
| `not 5` | `False` | 5 is truthy |

### Falsy Values in Python

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

### Key Points

| Point | Description |
|-------|-------------|
| Precedence | `not` > `and` > `or` |
| Short-circuit | Evaluation stops early when result is known |
| Non-boolean | Returns actual values, not just True/False |
| Use parentheses | For clarity in complex expressions |

---

## Coverage Checklist

- [x] and operator explained
- [x] or operator explained
- [x] not operator explained
- [x] Truth tables for each operator
- [x] Operator precedence
- [x] Short-circuit evaluation
- [x] Non-boolean value behavior
- [x] Practical examples
- [x] Quick reference tables
