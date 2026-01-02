# Python Regular Expressions (re module) - Quick Reference

Pattern matching and text manipulation with regex.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic Functions](#2-basic-functions)
3. [Pattern Syntax](#3-pattern-syntax)
4. [Special Characters](#4-special-characters)
5. [Common Patterns](#5-common-patterns)
6. [Flags](#6-flags)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is Regex?

Regular expressions (regex) are patterns used to match, search, and manipulate text.

### Import

```python
import re
```

### Basic Example

```python
import re

text = "My email is user@example.com"
pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)
if match:
    print(match.group())  # user@example.com
```

---

## 2. Basic Functions

### re.search() - Find First Match

```python
import re

text = "Python is fun and Python is powerful"
match = re.search(r"Python", text)

if match:
    print(match.group())   # Python
    print(match.start())   # 0 (starting position)
    print(match.end())     # 6 (ending position)
```

### re.match() - Match at Beginning

```python
# Only matches at start of string
text = "Python is fun"
print(re.match(r"Python", text))  # Match object
print(re.match(r"fun", text))     # None (not at start)
```

### re.findall() - Find All Matches

```python
text = "cat bat rat cat mat"
matches = re.findall(r".at", text)
print(matches)  # ['cat', 'bat', 'rat', 'cat', 'mat']

# Extract numbers
text = "Price: $10, $25, $100"
numbers = re.findall(r"\d+", text)
print(numbers)  # ['10', '25', '100']
```

### re.finditer() - Find All with Details

```python
text = "cat bat rat"
for match in re.finditer(r".at", text):
    print(f"{match.group()} at position {match.start()}")
# cat at position 0
# bat at position 4
# rat at position 8
```

### re.sub() - Replace Matches

```python
text = "I have 2 cats and 3 dogs"

# Replace digits with X
result = re.sub(r"\d", "X", text)
print(result)  # I have X cats and X dogs

# Replace with function
def double(match):
    return str(int(match.group()) * 2)

result = re.sub(r"\d+", double, text)
print(result)  # I have 4 cats and 6 dogs
```

### re.split() - Split by Pattern

```python
text = "apple, banana; cherry orange"
parts = re.split(r"[,;\s]+", text)
print(parts)  # ['apple', 'banana', 'cherry', 'orange']
```

---

## 3. Pattern Syntax

### Character Classes

| Pattern | Matches |
|---------|---------|
| `[abc]` | a, b, or c |
| `[^abc]` | Not a, b, or c |
| `[a-z]` | Any lowercase letter |
| `[A-Z]` | Any uppercase letter |
| `[0-9]` | Any digit |
| `[a-zA-Z0-9]` | Any alphanumeric |

```python
# Match vowels
re.findall(r"[aeiou]", "Hello World")  # ['e', 'o', 'o']

# Match non-digits
re.findall(r"[^0-9]", "abc123")  # ['a', 'b', 'c']
```

### Quantifiers

| Pattern | Meaning |
|---------|---------|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n}` | Exactly n |
| `{n,}` | n or more |
| `{n,m}` | Between n and m |

```python
# Examples
re.findall(r"a+", "caaaat")    # ['aaaa']
re.findall(r"a*", "caaaat")    # ['', 'aaaa', '', '']
re.findall(r"a?", "caaaat")    # ['', 'a', 'a', 'a', 'a', '', '']
re.findall(r"a{2}", "caaaat")  # ['aa', 'aa']
re.findall(r"a{2,3}", "caaaat")# ['aaa']
```

### Anchors

| Pattern | Meaning |
|---------|---------|
| `^` | Start of string |
| `$` | End of string |
| `\b` | Word boundary |

```python
text = "Python is fun"

re.search(r"^Python", text)  # Matches
re.search(r"^fun", text)     # None
re.search(r"fun$", text)     # Matches
re.findall(r"\bfun\b", text) # ['fun']
```

---

## 4. Special Characters

### Predefined Character Classes

| Pattern | Matches | Equivalent |
|---------|---------|------------|
| `\d` | Any digit | `[0-9]` |
| `\D` | Non-digit | `[^0-9]` |
| `\w` | Word char | `[a-zA-Z0-9_]` |
| `\W` | Non-word char | `[^a-zA-Z0-9_]` |
| `\s` | Whitespace | `[ \t\n\r\f\v]` |
| `\S` | Non-whitespace | `[^ \t\n\r\f\v]` |
| `.` | Any char (except newline) | |

```python
text = "abc 123 !@#"

re.findall(r"\d+", text)   # ['123']
re.findall(r"\w+", text)   # ['abc', '123']
re.findall(r"\s+", text)   # [' ', ' ']
re.findall(r".", text)     # Each character
```

### Grouping and Capturing

```python
# Groups with parentheses
text = "John Smith, Jane Doe"
pattern = r"(\w+) (\w+)"

for match in re.finditer(pattern, text):
    print(f"Full: {match.group()}")
    print(f"First: {match.group(1)}")
    print(f"Last: {match.group(2)}")

# Named groups
pattern = r"(?P<first>\w+) (?P<last>\w+)"
match = re.search(pattern, "John Smith")
print(match.group("first"))  # John
print(match.group("last"))   # Smith
```

---

## 5. Common Patterns

### Email Validation

```python
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

emails = ["user@example.com", "invalid", "test@test.co.uk"]
for email in emails:
    if re.match(pattern, email):
        print(f"Valid: {email}")
```

### Phone Number

```python
pattern = r"\d{3}[-.]?\d{3}[-.]?\d{4}"

text = "Call 123-456-7890 or 987.654.3210"
print(re.findall(pattern, text))
# ['123-456-7890', '987.654.3210']
```

### URL Extraction

```python
pattern = r"https?://[\w.-]+(?:/[\w.-]*)*"

text = "Visit https://example.com/page or http://test.com"
print(re.findall(pattern, text))
```

### Date Format

```python
# MM/DD/YYYY or MM-DD-YYYY
pattern = r"\d{2}[/-]\d{2}[/-]\d{4}"

text = "Dates: 12/25/2024, 01-15-2025"
print(re.findall(pattern, text))
# ['12/25/2024', '01-15-2025']
```

### Remove Extra Whitespace

```python
text = "Hello    World   Python"
result = re.sub(r"\s+", " ", text)
print(result)  # "Hello World Python"
```

---

## 6. Flags

### Common Flags

| Flag | Meaning |
|------|---------|
| `re.IGNORECASE` or `re.I` | Case-insensitive |
| `re.MULTILINE` or `re.M` | ^ and $ match line starts/ends |
| `re.DOTALL` or `re.S` | . matches newlines |
| `re.VERBOSE` or `re.X` | Allow comments in pattern |

```python
# Case-insensitive
re.findall(r"python", "Python PYTHON python", re.I)
# ['Python', 'PYTHON', 'python']

# Multiline
text = """Line 1
Line 2
Line 3"""
re.findall(r"^Line", text, re.M)  # ['Line', 'Line', 'Line']

# Verbose pattern (readable)
pattern = re.compile(r"""
    \d{3}    # Area code
    [-.]?    # Optional separator
    \d{3}    # First 3 digits
    [-.]?    # Optional separator
    \d{4}    # Last 4 digits
""", re.VERBOSE)
```

---

## 7. Quick Reference

### Functions Summary

| Function | Purpose |
|----------|---------|
| `re.search(pattern, text)` | Find first match |
| `re.match(pattern, text)` | Match at beginning |
| `re.findall(pattern, text)` | Find all matches |
| `re.finditer(pattern, text)` | Find all with details |
| `re.sub(pattern, repl, text)` | Replace matches |
| `re.split(pattern, text)` | Split by pattern |
| `re.compile(pattern)` | Compile pattern for reuse |

### Character Classes

| Pattern | Matches |
|---------|---------|
| `\d` | Digit |
| `\w` | Word character |
| `\s` | Whitespace |
| `.` | Any character |

### Quantifiers

| Pattern | Meaning |
|---------|---------|
| `*` | 0+ |
| `+` | 1+ |
| `?` | 0 or 1 |
| `{n}` | Exactly n |

### Anchors

| Pattern | Meaning |
|---------|---------|
| `^` | Start |
| `$` | End |
| `\b` | Word boundary |

### Common Patterns

| Purpose | Pattern |
|---------|---------|
| Email | `[\w.-]+@[\w.-]+\.\w+` |
| Phone | `\d{3}[-.]?\d{3}[-.]?\d{4}` |
| Digits | `\d+` |
| Words | `\w+` |

---

## Coverage Checklist

- [x] Basic re functions
- [x] Pattern syntax
- [x] Character classes
- [x] Quantifiers
- [x] Anchors
- [x] Grouping
- [x] Common patterns
- [x] Flags
- [x] Quick reference
