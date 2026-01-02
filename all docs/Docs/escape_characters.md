# Python Escape Characters & Confusing Basics - Quick Reference

Essential escape sequences and commonly confused concepts.

---

## Table of Contents

1. [Escape Characters](#1-escape-characters)
2. [Raw Strings](#2-raw-strings)
3. [Commonly Confused Concepts](#3-commonly-confused-concepts)
4. [Truthy and Falsy Values](#4-truthy-and-falsy-values)
5. [Mutable vs Immutable](#5-mutable-vs-immutable)
6. [Pass by Reference vs Value](#6-pass-by-reference-vs-value)
7. [Quick Reference](#7-quick-reference)

---

## 1. Escape Characters

### What are Escape Characters?

Special characters preceded by a backslash (`\`) that represent characters difficult to type directly.

### Common Escape Sequences

| Escape | Description | Example Output |
|--------|-------------|----------------|
| `\n` | New line | Line break |
| `\t` | Tab | Horizontal tab |
| `\\` | Backslash | `\` |
| `\'` | Single quote | `'` |
| `\"` | Double quote | `"` |
| `\r` | Carriage return | Return to line start |
| `\b` | Backspace | Delete previous char |

### Newline (\n)

```python
# Create new line
print("Hello\nWorld")
# Output:
# Hello
# World

# Multiple lines
text = "Line 1\nLine 2\nLine 3"
print(text)
# Line 1
# Line 2
# Line 3
```

### Tab (\t)

```python
# Add horizontal tab
print("Name\tAge\tCity")
print("Alice\t25\tNYC")
print("Bob\t30\tLA")
# Output:
# Name    Age     City
# Alice   25      NYC
# Bob     30      LA

# Aligning columns
print("Item\t\tPrice")
print("Apple\t\t$1.00")
print("Banana\t\t$0.50")
```

### Backslash (\\)

```python
# Print a backslash
print("C:\\Users\\Documents")
# Output: C:\Users\Documents

# File paths on Windows
path = "C:\\Program Files\\Python"
print(path)

# Escaping in regex patterns
pattern = "\\d+"  # Matches digits
```

### Quotes (\' and \")

```python
# Single quote in single-quoted string
print('It\'s a beautiful day')
# Output: It's a beautiful day

# Double quote in double-quoted string
print("She said \"Hello\"")
# Output: She said "Hello"

# Alternative: use different quotes
print("It's a beautiful day")      # Use double quotes
print('She said "Hello"')          # Use single quotes
```

### Combined Examples

```python
# Tab-separated data
data = "Name\tAge\tScore\nAlice\t25\t95\nBob\t30\t87"
print(data)
# Name    Age     Score
# Alice   25      95
# Bob     30      87

# File path with quotes
message = "File saved to \"C:\\Users\\data.txt\""
print(message)
# File saved to "C:\Users\data.txt"
```

---

## 2. Raw Strings

### What are Raw Strings?

Strings prefixed with `r` that treat backslashes as literal characters (no escape processing).

### Syntax

```python
# Regular string (escape processed)
print("Hello\nWorld")
# Hello
# World

# Raw string (no escape processing)
print(r"Hello\nWorld")
# Hello\nWorld
```

### Use Cases

```python
# Windows file paths
path = r"C:\Users\Documents\file.txt"
print(path)  # C:\Users\Documents\file.txt

# Regular expressions
import re
pattern = r"\d{3}-\d{4}"  # Matches phone numbers like 123-4567
result = re.search(pattern, "Call 555-1234")

# LaTeX strings
latex = r"\frac{1}{2}"
```

### Raw String Limitation

```python
# Cannot end with single backslash
# path = r"C:\folder\"  # SyntaxError!

# Solution: concatenate
path = r"C:\folder" + "\\"
# Or use regular string
path = "C:\\folder\\"
```

---

## 3. Commonly Confused Concepts

### = vs ==

| Operator | Purpose | Example |
|----------|---------|---------|
| `=` | Assignment | `x = 5` |
| `==` | Comparison | `x == 5` → `True` |

```python
x = 5      # Assigns 5 to x
x == 5     # Compares x with 5, returns True
x == 10    # Returns False
```

### == vs is

| Operator | Checks | Use For |
|----------|--------|---------|
| `==` | Value equality | Comparing values |
| `is` | Identity (same object) | Comparing with None |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (same values)
print(a is b)   # False (different objects)
print(a is c)   # True (same object)

# Use 'is' for None
x = None
print(x is None)    # True (correct)
print(x == None)    # True (works but not recommended)
```

### and vs & | or vs |

| Operator | Type | Use For |
|----------|------|---------|
| `and`, `or` | Logical | Boolean conditions |
| `&`, `\|` | Bitwise | Bit manipulation |

```python
# Logical (short-circuit)
if x > 0 and y > 0:
    print("Both positive")

# Bitwise
flags = 0b1010 & 0b1100  # 0b1000 = 8
```

### append() vs extend()

```python
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]] - adds as single element

list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # [1, 2, 3, 4, 5] - adds each element
```

### sort() vs sorted()

```python
nums = [3, 1, 4, 1, 5]

# sort() - modifies in place, returns None
result = nums.sort()
print(result)  # None
print(nums)    # [1, 1, 3, 4, 5]

nums = [3, 1, 4, 1, 5]
# sorted() - returns new list, original unchanged
result = sorted(nums)
print(result)  # [1, 1, 3, 4, 5]
print(nums)    # [3, 1, 4, 1, 5]
```

### copy() vs Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy - nested objects still linked
shallow = original.copy()
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] - original changed!

# Deep copy - completely independent
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]] - original unchanged
```

---

## 4. Truthy and Falsy Values

### Falsy Values (Evaluate to False)

```python
# All of these are Falsy
False       # Boolean False
None        # None type
0           # Integer zero
0.0         # Float zero
""          # Empty string
[]          # Empty list
{}          # Empty dict
()          # Empty tuple
set()       # Empty set
```

### Truthy Values (Evaluate to True)

```python
# All of these are Truthy
True        # Boolean True
1           # Non-zero numbers
-1          # Negative numbers
"hello"     # Non-empty strings
[1, 2]      # Non-empty lists
{"a": 1}    # Non-empty dicts
" "         # String with space (not empty!)
```

### Practical Usage

```python
# Check if list has items
items = []
if items:
    print("Has items")
else:
    print("Empty list")  # This prints

# Default value pattern
name = "" or "Anonymous"
print(name)  # Anonymous

# Check for None
result = None
if result is None:
    print("No result")
```

---

## 5. Mutable vs Immutable

### Immutable Types

Cannot be changed after creation. Any "change" creates a new object.

```python
# Strings are immutable
s = "hello"
s = s.upper()  # Creates NEW string "HELLO"
print(id(s))   # Different object

# Numbers are immutable
x = 5
x = x + 1  # Creates NEW integer 6

# Tuples are immutable
t = (1, 2, 3)
# t[0] = 99  # Error! Cannot modify
```

### Mutable Types

Can be changed in place.

```python
# Lists are mutable
lst = [1, 2, 3]
lst[0] = 99  # Modifies in place
lst.append(4)  # Same object

# Dictionaries are mutable
d = {"a": 1}
d["b"] = 2  # Modifies in place

# Sets are mutable
s = {1, 2, 3}
s.add(4)  # Modifies in place
```

### Summary Table

| Type | Mutable? | Example |
|------|----------|---------|
| `int` | No | `5` |
| `float` | No | `3.14` |
| `str` | No | `"hello"` |
| `tuple` | No | `(1, 2, 3)` |
| `frozenset` | No | `frozenset({1, 2})` |
| `list` | Yes | `[1, 2, 3]` |
| `dict` | Yes | `{"a": 1}` |
| `set` | Yes | `{1, 2, 3}` |

---

## 6. Pass by Reference vs Value

### Python's Model: Pass by Object Reference

```python
# Immutable objects - changes don't affect original
def modify_string(s):
    s = s + " World"
    print(f"Inside: {s}")

text = "Hello"
modify_string(text)
print(f"Outside: {text}")
# Inside: Hello World
# Outside: Hello (unchanged)

# Mutable objects - changes affect original
def modify_list(lst):
    lst.append(4)
    print(f"Inside: {lst}")

numbers = [1, 2, 3]
modify_list(numbers)
print(f"Outside: {numbers}")
# Inside: [1, 2, 3, 4]
# Outside: [1, 2, 3, 4] (changed!)
```

### Reassignment vs Modification

```python
def reassign(lst):
    lst = [10, 20, 30]  # Creates new object
    print(f"Inside: {lst}")

def modify(lst):
    lst[0] = 10  # Modifies existing object
    print(f"Inside: {lst}")

original = [1, 2, 3]
reassign(original)
print(f"After reassign: {original}")  # [1, 2, 3]

modify(original)
print(f"After modify: {original}")    # [10, 2, 3]
```

---

## 7. Quick Reference

### Escape Characters

| Escape | Meaning |
|--------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |

### Raw Strings

```python
r"path\to\file"  # Backslashes are literal
```

### Common Confusions

| Confused | Difference |
|----------|------------|
| `=` vs `==` | Assignment vs comparison |
| `==` vs `is` | Value vs identity |
| `and` vs `&` | Logical vs bitwise |
| `append()` vs `extend()` | Add one vs add many |
| `sort()` vs `sorted()` | In-place vs returns new |
| shallow vs deep copy | Linked nested vs independent |

### Falsy Values

```python
False, None, 0, 0.0, "", [], {}, (), set()
```

### Mutable vs Immutable

| Immutable | Mutable |
|-----------|---------|
| int, float, str | list |
| tuple, frozenset | dict, set |

### Pass by Object Reference

| Object Type | Effect in Function |
|-------------|-------------------|
| Immutable | Changes don't affect original |
| Mutable | Changes affect original |

---

## Coverage Checklist

- [x] All escape characters (\n, \t, \\, \', \")
- [x] Raw strings
- [x] = vs == vs is
- [x] and/or vs &/|
- [x] append() vs extend()
- [x] sort() vs sorted()
- [x] Shallow vs deep copy
- [x] Truthy and falsy values
- [x] Mutable vs immutable types
- [x] Pass by reference vs value
- [x] Quick reference tables
