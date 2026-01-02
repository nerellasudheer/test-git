# Python Match-Case Statement - Quick Reference

Understanding Python's structural pattern matching (introduced in Python 3.10).

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic Syntax](#2-basic-syntax)
3. [Pattern Types](#3-pattern-types)
4. [Practical Examples](#4-practical-examples)
5. [Quick Reference](#5-quick-reference)

---

## 1. Overview

### What is match-case?

`match-case` is Python's pattern matching feature introduced in **Python 3.10**. It works similar to `switch-case` in other languages (C, Java, JavaScript) but is more powerful.

### Why Use match-case?

- Cleaner alternative to multiple `if-elif-else` statements
- More readable and maintainable code
- Supports complex pattern matching (types, sequences, etc.)

---

## 2. Basic Syntax

```python
match variable:
    case value1:
        # code if value1 matches
    case value2:
        # code if value2 matches
    case _:
        # default case (like 'else')
```

### Simple Example

```python
def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid day"

print(day_of_week(3))   # Tuesday
print(day_of_week(10))  # Invalid day
```

---

## 3. Pattern Types

### Literal Patterns

Match specific values:

```python
def get_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"
```

### Type Patterns

Match based on data type:

```python
def check_type(value):
    match value:
        case int():
            return "Integer"
        case str():
            return "String"
        case list():
            return "List"
        case dict():
            return "Dictionary"
        case _:
            return "Unknown type"

print(check_type(42))        # Integer
print(check_type("hello"))   # String
print(check_type([1, 2, 3])) # List
```

### Sequence Patterns

Match and unpack sequences:

```python
point = (0, 10)

match point:
    case (0, y):
        print(f"Point is on Y-axis at {y}")
    case (x, 0):
        print(f"Point is on X-axis at {x}")
    case (x, y):
        print(f"Point is at ({x}, {y})")
    case _:
        print("Invalid point")
```

### OR Patterns

Match multiple values:

```python
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case _:
            return False

print(is_weekend("Saturday"))  # True
print(is_weekend("Monday"))    # False
```

### Guard Patterns

Add conditions with `if`:

```python
def classify_number(n):
    match n:
        case x if x < 0:
            return "Negative"
        case 0:
            return "Zero"
        case x if x > 0:
            return "Positive"

print(classify_number(-5))  # Negative
print(classify_number(0))   # Zero
print(classify_number(10))  # Positive
```

---

## 4. Practical Examples

### HTTP Response Handler

```python
def handle_response(response):
    match response:
        case {"status": 200, "data": data}:
            return f"Success: {data}"
        case {"status": 404}:
            return "Not Found"
        case {"status": 500, "error": error}:
            return f"Server Error: {error}"
        case _:
            return "Unknown response"

response = {"status": 200, "data": "User info"}
print(handle_response(response))  # Success: User info
```

### Command Parser

```python
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Exiting..."
        case ["hello", name]:
            return f"Hello, {name}!"
        case ["add", x, y]:
            return f"Sum: {int(x) + int(y)}"
        case _:
            return "Unknown command"

print(process_command("hello World"))  # Hello, World!
print(process_command("add 5 3"))      # Sum: 8
print(process_command("quit"))         # Exiting...
```

### Grading System

```python
def get_grade(score):
    match score:
        case n if n >= 90:
            return "A"
        case n if n >= 80:
            return "B"
        case n if n >= 70:
            return "C"
        case n if n >= 60:
            return "D"
        case _:
            return "F"

print(get_grade(95))  # A
print(get_grade(75))  # C
print(get_grade(50))  # F
```

---

## 5. Quick Reference

### Key Points

| Feature | Description |
|---------|-------------|
| Introduced in | Python 3.10 |
| Purpose | Pattern matching, cleaner than `if-elif-else` |
| `_` (underscore) | Wildcard, matches anything (default case) |
| Fall-through | Not supported (unlike C/Java) |
| Patterns | Literals, types, sequences, OR, guards |

### Comparison: if-elif vs match-case

**if-elif-else:**
```python
def get_day(n):
    if n == 1:
        return "Sunday"
    elif n == 2:
        return "Monday"
    elif n == 3:
        return "Tuesday"
    else:
        return "Unknown"
```

**match-case:**
```python
def get_day(n):
    match n:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case _:
            return "Unknown"
```

### Pattern Syntax Summary

| Pattern | Example | Description |
|---------|---------|-------------|
| Literal | `case 42:` | Match exact value |
| Wildcard | `case _:` | Match anything (default) |
| OR | `case 1 \| 2:` | Match multiple values |
| Type | `case int():` | Match by type |
| Sequence | `case (x, y):` | Match and unpack |
| Guard | `case x if x > 0:` | Match with condition |
| Dictionary | `case {"key": value}:` | Match dict pattern |

---

## Coverage Checklist

- [x] What match-case is
- [x] Basic syntax
- [x] Literal patterns
- [x] Type patterns
- [x] Sequence patterns
- [x] OR patterns
- [x] Guard patterns (if conditions)
- [x] Practical examples
- [x] Comparison with if-elif
- [x] Quick reference tables
