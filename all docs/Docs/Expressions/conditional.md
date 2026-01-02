# Python Conditional Expressions (Ternary Operator)

A quick reference for Python's conditional expression syntax.

---

## Overview

### What is a Conditional Expression?

A conditional expression (also called the **ternary operator**) allows you to write a simple `if-else` statement in a single line. It returns one of two values based on a condition.

### Basic Syntax

```python
value_if_true if condition else value_if_false
```

### Visual Formula

```
X if condition else Y
```

- If `condition` is `True` → returns `X`
- If `condition` is `False` → returns `Y`

---

## Basic Examples

### Example 1: Simple Comparison

```python
age = 20

# Traditional if-else
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Using conditional expression (same result)
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

### Example 2: Number Classification

```python
number = -5

result = "Positive" if number > 0 else "Non-positive"
print(result)  # Output: Non-positive
```

### Example 3: Maximum of Two Numbers

```python
a = 10
b = 20

maximum = a if a > b else b
print(maximum)  # Output: 20
```

### Example 4: String Transformation

```python
name = ""

display_name = name if name else "Anonymous"
print(display_name)  # Output: Anonymous
```

---

## Use Cases

### 1. Variable Assignment

```python
score = 85
grade = "Pass" if score >= 60 else "Fail"
```

### 2. Function Return Values

```python
def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"

print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd
```

### 3. List Comprehensions

```python
numbers = [1, 2, 3, 4, 5]

# Label each number
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

### 4. Default Values

```python
user_input = None

# Use default if input is None or empty
value = user_input if user_input else "default"
print(value)  # Output: default
```

### 5. Print Formatting

```python
count = 1
print(f"You have {count} item{'s' if count != 1 else ''}")
# Output: You have 1 item

count = 5
print(f"You have {count} item{'s' if count != 1 else ''}")
# Output: You have 5 items
```

---

## Chained (Nested) Conditional Expressions

You can chain multiple conditions, but use sparingly for readability.

```python
score = 85

# Nested ternary (use cautiously)
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)  # Output: B
```

**Better: Use regular if-elif for complex conditions:**

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

---

## Common Mistakes

### Mistake 1: Wrong Order

```python
# WRONG - Syntax error
# result = if x > 0 "Positive" else "Negative"

# CORRECT
result = "Positive" if x > 0 else "Negative"
```

### Mistake 2: Missing else

```python
# WRONG - Conditional expression MUST have else
# result = "Yes" if condition

# CORRECT
result = "Yes" if condition else "No"
```

### Mistake 3: Overcomplicating

```python
# BAD - Too complex
status = "Active" if user.is_logged_in and user.has_permission and not user.is_banned else "Inactive"

# BETTER - Use regular if-else
if user.is_logged_in and user.has_permission and not user.is_banned:
    status = "Active"
else:
    status = "Inactive"
```

---

## When to Use

### Use Conditional Expression When:

- Simple `if-else` with single values
- Assigning one of two values to a variable
- Default value fallback
- Short, readable one-liners

### Use Traditional if-else When:

- Multiple statements to execute
- Complex conditions
- More than 2 branches (elif)
- Readability is important

---

## Quick Reference

### Syntax Patterns

| Pattern | Example |
|---------|---------|
| Basic | `x if condition else y` |
| With expressions | `a + 1 if a > 0 else a - 1` |
| Nested (avoid if complex) | `a if cond1 else b if cond2 else c` |
| In list comprehension | `[x if cond else y for item in list]` |

### Comparison

| Approach | Code |
|----------|------|
| Traditional | `if x > 0: result = "pos"` <br> `else: result = "neg"` |
| Ternary | `result = "pos" if x > 0 else "neg"` |

---

## Coverage Checklist

- [x] Basic syntax explained
- [x] Multiple examples
- [x] Common use cases
- [x] Nested conditionals
- [x] Common mistakes
- [x] When to use guidelines
