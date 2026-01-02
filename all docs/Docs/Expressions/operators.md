# Python Operators - Complete Reference

All Python operators with examples and use cases.

---

## Table of Contents

1. [Arithmetic Operators](#1-arithmetic-operators)
2. [Comparison Operators](#2-comparison-operators)
3. [Assignment Operators](#3-assignment-operators)
4. [Logical Operators](#4-logical-operators)
5. [Identity Operators](#5-identity-operators)
6. [Membership Operators](#6-membership-operators)
7. [Bitwise Operators](#7-bitwise-operators)
8. [Operator Precedence](#8-operator-precedence)
9. [Quick Reference](#9-quick-reference)

---

## 1. Arithmetic Operators

### Basic Arithmetic

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulus | `7 % 3` | `1` |
| `**` | Exponent | `2 ** 3` | `8` |

### Examples

```python
# Basic operations
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 // 3)  # 3 (floor division)
print(10 % 3)   # 1 (remainder)
print(2 ** 4)   # 16 (2 to the power 4)

# Negative floor division
print(-7 // 2)  # -4 (rounds down)

# Order of operations
print(2 + 3 * 4)      # 14 (multiplication first)
print((2 + 3) * 4)    # 20 (parentheses first)
```

### Use Cases

```python
# Check if number is even
is_even = number % 2 == 0

# Get last digit
last_digit = number % 10

# Integer division for pagination
pages = total_items // items_per_page
```

---

## 2. Comparison Operators

### All Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `5 <= 3` | `False` |

### Examples

```python
x = 10
y = 5

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= 10)  # True
print(x <= 5)   # False
```

### Chained Comparisons

```python
# Python allows chaining
x = 5
print(1 < x < 10)     # True (1 < 5 and 5 < 10)
print(1 < x < 3)      # False
print(0 <= x <= 10)   # True

# Equivalent to
print(1 < x and x < 10)  # True
```

### Comparing Different Types

```python
# Strings (lexicographic)
print("apple" < "banana")  # True
print("Apple" < "apple")   # True (uppercase < lowercase)

# Lists (element by element)
print([1, 2] < [1, 3])     # True
print([1, 2] < [1, 2, 3])  # True
```

---

## 3. Assignment Operators

### Basic Assignment

```python
x = 10
```

### Compound Assignment

| Operator | Example | Equivalent |
|----------|---------|------------|
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 5` | `x = x ** 5` |

### Examples

```python
x = 10

x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x /= 4    # x = 6.0
x //= 2   # x = 3.0
x **= 2   # x = 9.0
```

### Walrus Operator `:=` (Python 3.8+)

```python
# Assign and use in one expression
if (n := len(data)) > 10:
    print(f"List too long ({n} items)")

# In while loops
while (line := file.readline()):
    process(line)

# In list comprehensions
filtered = [y for x in data if (y := process(x)) is not None]
```

---

## 4. Logical Operators

### All Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | True if both True | `True and False` → `False` |
| `or` | True if one True | `True or False` → `True` |
| `not` | Negate | `not True` → `False` |

### Examples

```python
x = 5

# and - both must be True
print(x > 0 and x < 10)  # True

# or - at least one must be True
print(x < 0 or x > 3)    # True

# not - negate the result
print(not x > 10)        # True
```

### Short-Circuit Evaluation

```python
# and: stops at first False
result = False and expensive_function()  # expensive_function not called

# or: stops at first True
result = True or expensive_function()    # expensive_function not called
```

### Non-Boolean Values

```python
# and returns first falsy or last value
print(5 and 10)       # 10
print(0 and 10)       # 0

# or returns first truthy or last value
print(5 or 10)        # 5
print(0 or 10)        # 10

# Default value pattern
name = user_input or "Anonymous"
```

---

## 5. Identity Operators

### is and is not

| Operator | Description |
|----------|-------------|
| `is` | True if same object |
| `is not` | True if different objects |

### Examples

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# == checks value equality
print(a == b)       # True (same values)

# is checks identity (same object)
print(a is b)       # False (different objects)
print(a is c)       # True (same object)

# Common use with None
x = None
print(x is None)      # True (correct way)
print(x == None)      # True (works but not recommended)
```

### When to Use `is`

```python
# Use 'is' for:
if x is None:
    pass

if x is True:
    pass

if x is False:
    pass

# Use '==' for values:
if x == 5:
    pass

if x == "hello":
    pass
```

### Integer Caching (Be Aware)

```python
# Python caches small integers (-5 to 256)
a = 100
b = 100
print(a is b)  # True (cached)

a = 1000
b = 1000
print(a is b)  # False (not cached) - may vary by implementation
```

---

## 6. Membership Operators

### in and not in

| Operator | Description |
|----------|-------------|
| `in` | True if value found |
| `not in` | True if value not found |

### Examples

```python
# In strings
text = "Hello World"
print("Hello" in text)      # True
print("hello" in text)      # False (case-sensitive)
print("Python" not in text) # True

# In lists
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)    # True
print("grape" in fruits)    # False

# In dictionaries (checks keys)
person = {"name": "Alice", "age": 25}
print("name" in person)     # True
print("Alice" in person)    # False (values not checked)
print("Alice" in person.values())  # True
```

### Practical Use

```python
# Input validation
valid_choices = ["yes", "no", "maybe"]
if user_input in valid_choices:
    process(user_input)

# String containment
if "@" in email and "." in email:
    print("Looks like an email")

# Dictionary key check
if "age" in person:
    print(person["age"])
```

---

## 7. Bitwise Operators

### All Bitwise Operators

| Operator | Name | Example | Description |
|----------|------|---------|-------------|
| `&` | AND | `5 & 3` | Bits on in both |
| `\|` | OR | `5 \| 3` | Bits on in either |
| `^` | XOR | `5 ^ 3` | Bits on in one but not both |
| `~` | NOT | `~5` | Flip all bits |
| `<<` | Left shift | `5 << 1` | Multiply by 2 |
| `>>` | Right shift | `5 >> 1` | Divide by 2 |

### Examples

```python
a = 5   # binary: 0101
b = 3   # binary: 0011

print(a & b)   # 1  (0001) - AND
print(a | b)   # 7  (0111) - OR
print(a ^ b)   # 6  (0110) - XOR
print(~a)      # -6 (inverts all bits)
print(a << 1)  # 10 (1010) - left shift
print(a >> 1)  # 2  (0010) - right shift
```

### Practical Use Cases

```python
# Check if number is even (faster than modulo)
is_even = (number & 1) == 0

# Swap without temp variable
a, b = 5, 3
a ^= b
b ^= a
a ^= b  # Now a=3, b=5

# Flags/permissions
READ = 1    # 001
WRITE = 2   # 010
EXECUTE = 4 # 100

permissions = READ | WRITE  # 011 = 3
has_read = permissions & READ  # Check if READ flag is set
```

---

## 8. Operator Precedence

### Precedence Order (Highest to Lowest)

| Precedence | Operators |
|------------|-----------|
| 1 (Highest) | `()` Parentheses |
| 2 | `**` Exponent |
| 3 | `~`, `+x`, `-x` Unary |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` Bitwise AND |
| 8 | `^` Bitwise XOR |
| 9 | `\|` Bitwise OR |
| 10 | `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `in` |
| 11 | `not` |
| 12 | `and` |
| 13 (Lowest) | `or` |

### Examples

```python
# Without parentheses
print(2 + 3 * 4)        # 14 (not 20)
print(2 ** 3 ** 2)      # 512 (right-to-left: 3**2=9, then 2**9)

# With parentheses for clarity
print((2 + 3) * 4)      # 20
print((2 ** 3) ** 2)    # 64

# Complex expression
print(5 > 3 and 2 < 4 or 10 > 20)  # True
# Equivalent to: ((5 > 3) and (2 < 4)) or (10 > 20)
# = (True and True) or False = True
```

---

## 9. Quick Reference

### Arithmetic Operators

| Operator | Purpose | Example |
|----------|---------|---------|
| `+` | Add | `5 + 3` → `8` |
| `-` | Subtract | `5 - 3` → `2` |
| `*` | Multiply | `5 * 3` → `15` |
| `/` | Divide | `5 / 2` → `2.5` |
| `//` | Floor divide | `5 // 2` → `2` |
| `%` | Modulus | `5 % 2` → `1` |
| `**` | Power | `5 ** 2` → `25` |

### Comparison Operators

| Operator | Purpose |
|----------|---------|
| `==` | Equal |
| `!=` | Not equal |
| `>`, `<` | Greater/Less than |
| `>=`, `<=` | Greater/Less or equal |

### Logical Operators

| Operator | Purpose |
|----------|---------|
| `and` | Both true |
| `or` | Either true |
| `not` | Negate |

### Identity & Membership

| Operator | Purpose |
|----------|---------|
| `is` | Same object |
| `is not` | Different object |
| `in` | In sequence |
| `not in` | Not in sequence |

### Common Patterns

| Pattern | Use Case |
|---------|----------|
| `x % 2 == 0` | Check even |
| `x // 10` | Remove last digit |
| `x % 10` | Get last digit |
| `x is None` | Check for None |
| `key in dict` | Check key exists |

---

## Coverage Checklist

- [x] Arithmetic operators (+, -, *, /, //, %, **)
- [x] Comparison operators (==, !=, <, >, <=, >=)
- [x] Assignment operators (=, +=, -=, etc.)
- [x] Logical operators (and, or, not)
- [x] Identity operators (is, is not)
- [x] Membership operators (in, not in)
- [x] Bitwise operators (&, |, ^, ~, <<, >>)
- [x] Operator precedence
- [x] Walrus operator (:=)
- [x] Quick reference tables
