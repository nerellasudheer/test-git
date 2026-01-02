# Python String Methods - Complete Guide

A comprehensive reference guide for Python String Methods.

---

## Table of Contents

1. [Overview](#1-overview)
2. [String Basics](#2-string-basics)
3. [Case Conversion Methods](#3-case-conversion-methods)
4. [Search and Find Methods](#4-search-and-find-methods)
5. [Validation Methods](#5-validation-methods)
6. [Modification Methods](#6-modification-methods)
7. [Split and Join Methods](#7-split-and-join-methods)
8. [Strip Methods](#8-strip-methods)
9. [File Reading Methods](#9-file-reading-methods)
10. [Common Mistakes](#10-common-mistakes)
11. [Quick Reference](#11-quick-reference)

---

## 1. Overview

### What is a String?

A string is an **immutable** sequence of characters. In Python, strings are objects with many built-in methods for manipulation.

### Key Characteristics

| Feature | Description |
|---------|-------------|
| Immutable | Cannot change after creation |
| Indexed | Access characters by position |
| Iterable | Can loop through characters |
| Methods | Return new strings, don't modify original |

### Important Rule

All string methods return a **new string**. The original string is never modified.

```python
text = "hello"
text.upper()  # Returns "HELLO" but doesn't change text
print(text)   # Output: hello (unchanged!)

text = text.upper()  # Must reassign to save change
print(text)   # Output: HELLO
```

---

## 2. String Basics

### Creating Strings

```python
# Single quotes
s1 = 'Hello'

# Double quotes
s2 = "Hello"

# Triple quotes (multiline)
s3 = """This is a
multiline string"""

# Raw string (ignores escape characters)
s4 = r"C:\new\folder"  # Backslashes are literal
```

### Accessing Characters

```python
text = "Python"

# Indexing
print(text[0])    # Output: P
print(text[-1])   # Output: n (last character)

# Slicing
print(text[0:3])  # Output: Pyt
print(text[::2])  # Output: Pto (every 2nd char)
print(text[::-1]) # Output: nohtyP (reversed)
```

---

## 3. Case Conversion Methods

### upper()

**Purpose**: Converts all characters to uppercase.

```python
text = "Hello World"
print(text.upper())  # Output: HELLO WORLD
```

---

### lower()

**Purpose**: Converts all characters to lowercase.

```python
text = "Hello World"
print(text.lower())  # Output: hello world
```

---

### title()

**Purpose**: Converts first character of each word to uppercase.

```python
text = "hello world python"
print(text.title())  # Output: Hello World Python
```

---

### capitalize()

**Purpose**: Converts only the first character to uppercase, rest to lowercase.

```python
text = "hELLO wORLD"
print(text.capitalize())  # Output: Hello world
```

---

### swapcase()

**Purpose**: Swaps uppercase to lowercase and vice versa.

```python
text = "Hello World"
print(text.swapcase())  # Output: hELLO wORLD
```

---

### casefold()

**Purpose**: Aggressive lowercase (better for case-insensitive comparisons).

```python
text = "HELLO"
print(text.casefold())  # Output: hello

# Better for international characters
german = "Straße"
print(german.lower())     # Output: straße
print(german.casefold())  # Output: strasse
```

---

## 4. Search and Find Methods

### find()

**Purpose**: Returns index of first occurrence. Returns -1 if not found.

```python
text = "Hello World"

print(text.find("World"))  # Output: 6
print(text.find("Python")) # Output: -1 (not found)
print(text.find("o"))      # Output: 4 (first 'o')
print(text.find("o", 5))   # Output: 7 (search from index 5)
```

---

### index()

**Purpose**: Like find(), but raises ValueError if not found.

```python
text = "Hello World"

print(text.index("World"))  # Output: 6
# print(text.index("Python"))  # ValueError: substring not found
```

---

### rfind() / rindex()

**Purpose**: Like find/index, but searches from the right (last occurrence).

```python
text = "Hello World, Hello Python"

print(text.find("Hello"))   # Output: 0 (first)
print(text.rfind("Hello"))  # Output: 13 (last)
```

---

### count()

**Purpose**: Returns number of occurrences.

```python
text = "banana"

print(text.count("a"))   # Output: 3
print(text.count("na"))  # Output: 2
print(text.count("x"))   # Output: 0
```

---

### startswith()

**Purpose**: Returns True if string starts with specified prefix.

```python
filename = "document.pdf"

print(filename.startswith("doc"))       # Output: True
print(filename.startswith("Doc"))       # Output: False (case-sensitive)

# Multiple prefixes (tuple)
print(filename.startswith(("doc", "img")))  # Output: True
```

---

### endswith()

**Purpose**: Returns True if string ends with specified suffix.

```python
filename = "image.jpg"

print(filename.endswith(".jpg"))  # Output: True
print(filename.endswith(".png"))  # Output: False

# Multiple suffixes (tuple)
print(filename.endswith((".jpg", ".png", ".gif")))  # Output: True
```

---

## 5. Validation Methods

### isdigit()

**Purpose**: Returns True if all characters are digits (0-9).

```python
print("12345".isdigit())   # Output: True
print("123.45".isdigit())  # Output: False (decimal point)
print("-123".isdigit())    # Output: False (minus sign)
print("123 ".isdigit())    # Output: False (space)
print("".isdigit())        # Output: False (empty)
```

---

### isnumeric()

**Purpose**: Like isdigit(), but also includes numeric characters like fractions.

```python
print("123".isnumeric())    # Output: True
print("½".isnumeric())      # Output: True (fraction)
print("123".isdigit())      # Output: True
print("½".isdigit())        # Output: False
```

---

### isalpha()

**Purpose**: Returns True if all characters are alphabetic.

```python
print("Hello".isalpha())    # Output: True
print("Hello123".isalpha()) # Output: False
print("Hello World".isalpha()) # Output: False (space)
```

---

### isalnum()

**Purpose**: Returns True if all characters are alphanumeric (letters or digits).

```python
print("Hello123".isalnum())  # Output: True
print("Hello 123".isalnum()) # Output: False (space)
print("Hello_123".isalnum()) # Output: False (underscore)
```

---

### isspace()

**Purpose**: Returns True if all characters are whitespace.

```python
print("   ".isspace())      # Output: True
print("\t\n".isspace())     # Output: True
print("  a  ".isspace())    # Output: False
```

---

### islower() / isupper()

**Purpose**: Returns True if all cased characters are lowercase/uppercase.

```python
print("hello".islower())    # Output: True
print("Hello".islower())    # Output: False
print("HELLO".isupper())    # Output: True
print("hello123".islower()) # Output: True (123 ignored)
```

---

### istitle()

**Purpose**: Returns True if string is titlecased.

```python
print("Hello World".istitle())  # Output: True
print("Hello world".istitle())  # Output: False
print("HELLO WORLD".istitle())  # Output: False
```

---

## 6. Modification Methods

### replace()

**Purpose**: Replaces occurrences of substring with another string.

```python
text = "Hello World"

# Replace all occurrences
print(text.replace("World", "Python"))  # Output: Hello Python

# Limit replacements
text = "ha ha ha ha"
print(text.replace("ha", "he", 2))  # Output: he he ha ha
```

---

### center() / ljust() / rjust()

**Purpose**: Pad string with characters to specified width.

```python
text = "Python"

# Center with spaces
print(text.center(20))       # Output: "       Python       "
print(text.center(20, "-"))  # Output: "-------Python-------"

# Left justify
print(text.ljust(20, "-"))   # Output: "Python--------------"

# Right justify
print(text.rjust(20, "-"))   # Output: "--------------Python"
```

---

### zfill()

**Purpose**: Pads string with zeros on the left.

```python
num = "42"
print(num.zfill(5))   # Output: 00042

# Works with negative numbers
print("-42".zfill(5)) # Output: -0042
```

---

### format()

**Purpose**: Formats string with placeholders.

```python
# Positional arguments
template = "Hello, {}!"
print(template.format("Alice"))  # Output: Hello, Alice!

# Named arguments
template = "Hello, {name}! You are {age} years old."
print(template.format(name="Alice", age=25))
# Output: Hello, Alice! You are 25 years old.
```

---

## 7. Split and Join Methods

### split()

**Purpose**: Splits string into a list by separator.

```python
text = "Hello World Python"

# Default: split by whitespace
words = text.split()
print(words)  # Output: ['Hello', 'World', 'Python']

# Split by specific separator
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Limit splits
text = "one two three four"
print(text.split(" ", 2))  # Output: ['one', 'two', 'three four']
```

---

### rsplit()

**Purpose**: Like split(), but splits from the right.

```python
text = "one two three four"

print(text.split(" ", 2))   # Output: ['one', 'two', 'three four']
print(text.rsplit(" ", 2))  # Output: ['one two', 'three', 'four']
```

---

### splitlines()

**Purpose**: Splits string by line breaks.

```python
text = "Hello\nWorld\nPython"

lines = text.splitlines()
print(lines)  # Output: ['Hello', 'World', 'Python']

# Compare with split('\n')
print(text.split('\n'))  # Output: ['Hello', 'World', 'Python']
```

**Key Difference**: `splitlines()` handles different line endings (`\n`, `\r\n`, `\r`).

---

### join()

**Purpose**: Joins list elements into a string with separator.

**Important**: Called on the separator, not the list!

```python
words = ["Hello", "World", "Python"]

# Join with space
sentence = " ".join(words)
print(sentence)  # Output: Hello World Python

# Join with comma
csv = ",".join(words)
print(csv)  # Output: Hello,World,Python

# Join with nothing
letters = ["P", "y", "t", "h", "o", "n"]
word = "".join(letters)
print(word)  # Output: Python
```

---

### partition() / rpartition()

**Purpose**: Splits string into 3 parts: before, separator, after.

```python
text = "Hello World Python"

# partition from left
result = text.partition(" ")
print(result)  # Output: ('Hello', ' ', 'World Python')

# rpartition from right
result = text.rpartition(" ")
print(result)  # Output: ('Hello World', ' ', 'Python')
```

---

## 8. Strip Methods

### strip()

**Purpose**: Removes whitespace from both ends.

```python
text = "   Hello World   \n"

clean = text.strip()
print(repr(clean))  # Output: 'Hello World'

# Remove specific characters
text = "###Hello###"
print(text.strip("#"))  # Output: Hello
```

---

### lstrip()

**Purpose**: Removes whitespace/characters from left side only.

```python
text = "   Hello World   "
print(repr(text.lstrip()))  # Output: 'Hello World   '
```

---

### rstrip()

**Purpose**: Removes whitespace/characters from right side only.

```python
text = "   Hello World   \n"
print(repr(text.rstrip()))  # Output: '   Hello World'
```

---

## 9. File Reading Methods

These methods are for file objects, often used with string processing.

### read()

**Purpose**: Reads entire file as a single string.

```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)  # Entire file content
```

---

### readline()

**Purpose**: Reads one line at a time.

```python
with open("file.txt", "r") as f:
    line1 = f.readline()  # First line
    line2 = f.readline()  # Second line
```

---

### readlines()

**Purpose**: Reads all lines as a list (includes `\n`).

```python
with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['Line 1\n', 'Line 2\n', 'Line 3\n']
```

---

### Common Pattern: Clean File Reading

```python
# Method 1: readlines() + strip()
with open("file.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# Method 2: read() + splitlines() (cleanest)
with open("file.txt", "r") as f:
    lines = f.read().splitlines()

# Method 3: Iterate directly (most efficient)
with open("file.txt", "r") as f:
    lines = [line.strip() for line in f]
```

---

## 10. Common Mistakes

### Mistake 1: Forgetting Strings Are Immutable

```python
text = "hello"

# WRONG - Doesn't save the change
text.upper()
print(text)  # Output: hello (unchanged!)

# CORRECT - Reassign the result
text = text.upper()
print(text)  # Output: HELLO
```

### Mistake 2: Calling join() on the List

```python
words = ["Hello", "World"]

# WRONG
# result = words.join(" ")  # AttributeError!

# CORRECT - Call on the separator
result = " ".join(words)
print(result)  # Output: Hello World
```

### Mistake 3: Using find() Without Checking -1

```python
text = "Hello World"

# WRONG - Treating -1 as valid index
pos = text.find("Python")
print(text[pos])  # Gets last character! (index -1)

# CORRECT - Check for -1
pos = text.find("Python")
if pos != -1:
    print(text[pos])
else:
    print("Not found")
```

### Mistake 4: Boolean Check with find()

```python
text = "Python is great"

# WRONG - find() returns 0 if found at start (falsy!)
if text.find("Python"):  # 0 is falsy!
    print("Found")  # Won't print!

# CORRECT - Check for != -1
if text.find("Python") != -1:
    print("Found")

# BETTER - Use 'in' operator
if "Python" in text:
    print("Found")
```

---

## 11. Quick Reference

### Case Conversion

| Method | Purpose | Example |
|--------|---------|---------|
| `upper()` | All uppercase | `"hi".upper()` → `"HI"` |
| `lower()` | All lowercase | `"HI".lower()` → `"hi"` |
| `title()` | Title Case | `"hi there".title()` → `"Hi There"` |
| `capitalize()` | First char upper | `"hi".capitalize()` → `"Hi"` |
| `swapcase()` | Swap case | `"Hi".swapcase()` → `"hI"` |

### Search Methods

| Method | Purpose | Returns |
|--------|---------|---------|
| `find(sub)` | Find first occurrence | Index or -1 |
| `index(sub)` | Find first occurrence | Index or ValueError |
| `rfind(sub)` | Find last occurrence | Index or -1 |
| `count(sub)` | Count occurrences | Integer |
| `startswith(prefix)` | Check start | Boolean |
| `endswith(suffix)` | Check end | Boolean |

### Validation Methods

| Method | Returns True If |
|--------|-----------------|
| `isdigit()` | All digits (0-9) |
| `isalpha()` | All alphabetic |
| `isalnum()` | All alphanumeric |
| `isspace()` | All whitespace |
| `islower()` | All lowercase |
| `isupper()` | All uppercase |

### Modification Methods

| Method | Purpose |
|--------|---------|
| `replace(old, new)` | Replace substring |
| `strip()` | Remove whitespace both ends |
| `lstrip()` | Remove whitespace left |
| `rstrip()` | Remove whitespace right |

### Split and Join

| Method | Input | Output |
|--------|-------|--------|
| `split()` | String | List |
| `join()` | List | String |
| `splitlines()` | String | List (by lines) |

### Key Memory Tricks

- **split()** = Split pizza into slices (one → many)
- **join()** = Join hands in circle (many → one)
- **find()** = Returns -1 if not found (safe)
- **index()** = Raises error if not found (strict)
- **All methods return NEW strings** (original unchanged)

---

## Coverage Checklist

- [x] All case conversion methods
- [x] All search/find methods
- [x] All validation (is*) methods
- [x] Modification methods
- [x] Split and join methods
- [x] Strip methods
- [x] File reading methods
- [x] Common mistakes explained
- [x] Quick reference tables
