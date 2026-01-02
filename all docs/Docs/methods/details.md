# Python Methods - Complete Reference

A comprehensive guide to commonly used methods for strings, lists, dictionaries, and more.

---

## Table of Contents

1. [Overview](#1-overview)
2. [String Methods](#2-string-methods)
3. [List Methods](#3-list-methods)
4. [Dictionary Methods](#4-dictionary-methods)
5. [Set Methods](#5-set-methods)
6. [The split() Method in Detail](#6-the-split-method-in-detail)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is a Method?

A method is a function that belongs to an object. Methods are defined inside a class and perform actions or operations on the object's data. You can think of a method as a specialized function that "knows" about the object it's associated with.

### Syntax

```python
object.method(arguments)
```

### Function vs Method

| Aspect | Function | Method |
|--------|----------|--------|
| Definition | Standalone | Belongs to object |
| Call syntax | `function(object)` | `object.method()` |
| Example | `len(my_list)` | `my_list.append(5)` |

---

## 2. String Methods

### Case Conversion

| Method | Description | Example |
|--------|-------------|---------|
| `.upper()` | All uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | All lowercase | `"HELLO".lower()` → `"hello"` |
| `.title()` | Title case | `"hello world".title()` → `"Hello World"` |
| `.capitalize()` | First char upper | `"hello".capitalize()` → `"Hello"` |
| `.swapcase()` | Swap cases | `"Hello".swapcase()` → `"hELLO"` |

```python
text = "hello WORLD"
print(text.upper())      # "HELLO WORLD"
print(text.lower())      # "hello world"
print(text.title())      # "Hello World"
print(text.capitalize()) # "Hello world"
print(text.swapcase())   # "HELLO world"
```

### Whitespace Handling

| Method | Description | Example |
|--------|-------------|---------|
| `.strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `.lstrip()` | Remove leading whitespace | `"  hi  ".lstrip()` → `"hi  "` |
| `.rstrip()` | Remove trailing whitespace | `"  hi  ".rstrip()` → `"  hi"` |

```python
text = "  Hello, World!  "
print(text.strip())   # "Hello, World!"
print(text.lstrip())  # "Hello, World!  "
print(text.rstrip())  # "  Hello, World!"

# Chaining methods
cleaned = text.strip().upper()
print(cleaned)  # "HELLO, WORLD!"
```

### Searching and Checking

| Method | Description | Returns |
|--------|-------------|---------|
| `.find(sub)` | Find substring index | Index or -1 |
| `.index(sub)` | Find substring index | Index or raises ValueError |
| `.count(sub)` | Count occurrences | Integer |
| `.startswith(s)` | Check start | Boolean |
| `.endswith(s)` | Check end | Boolean |

```python
text = "Hello, World!"

print(text.find("World"))      # 7
print(text.find("Python"))     # -1 (not found)
print(text.count("l"))         # 3
print(text.startswith("Hello"))# True
print(text.endswith("!"))      # True
```

### Validation Methods

| Method | Returns True When |
|--------|-------------------|
| `.isdigit()` | All characters are digits |
| `.isalpha()` | All characters are letters |
| `.isalnum()` | All characters are alphanumeric |
| `.isspace()` | All characters are whitespace |
| `.isupper()` | All cased characters are uppercase |
| `.islower()` | All cased characters are lowercase |

```python
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("   ".isspace())     # True
print("HELLO".isupper())   # True
print("hello".islower())   # True
```

### Modification Methods

| Method | Description |
|--------|-------------|
| `.replace(old, new)` | Replace substring |
| `.split(sep)` | Split into list |
| `.join(iterable)` | Join list into string |
| `.center(width)` | Center with padding |
| `.ljust(width)` | Left justify with padding |
| `.rjust(width)` | Right justify with padding |
| `.zfill(width)` | Pad with zeros |

```python
text = "Hello World"

# Replace
print(text.replace("World", "Python"))  # "Hello Python"

# Split and Join
words = text.split()           # ["Hello", "World"]
joined = "-".join(words)       # "Hello-World"

# Padding
print("Hi".center(10, "*"))    # "****Hi****"
print("Hi".ljust(10, "-"))     # "Hi--------"
print("42".zfill(5))           # "00042"
```

---

## 3. List Methods

### Adding Elements

| Method | Description | Modifies List |
|--------|-------------|---------------|
| `.append(item)` | Add item to end | Yes |
| `.insert(i, item)` | Insert at index | Yes |
| `.extend(iterable)` | Add multiple items | Yes |

```python
numbers = [1, 2, 3]

numbers.append(4)       # [1, 2, 3, 4]
numbers.insert(0, 0)    # [0, 1, 2, 3, 4]
numbers.extend([5, 6])  # [0, 1, 2, 3, 4, 5, 6]
```

### Removing Elements

| Method | Description | Returns |
|--------|-------------|---------|
| `.pop()` | Remove and return last item | Removed item |
| `.pop(i)` | Remove and return item at index | Removed item |
| `.remove(item)` | Remove first occurrence | None |
| `.clear()` | Remove all items | None |

```python
numbers = [1, 2, 3, 4, 5]

last = numbers.pop()        # last = 5, numbers = [1, 2, 3, 4]
first = numbers.pop(0)      # first = 1, numbers = [2, 3, 4]
numbers.remove(3)           # numbers = [2, 4]
numbers.clear()             # numbers = []
```

### Searching and Counting

| Method | Description | Returns |
|--------|-------------|---------|
| `.index(item)` | Find index of item | Index (raises ValueError if not found) |
| `.count(item)` | Count occurrences | Integer |

```python
colors = ["red", "blue", "red", "green"]

print(colors.index("blue"))  # 1
print(colors.count("red"))   # 2
```

### Sorting and Ordering

| Method | Description | Modifies List |
|--------|-------------|---------------|
| `.sort()` | Sort in place | Yes |
| `.sort(reverse=True)` | Sort descending | Yes |
| `.reverse()` | Reverse in place | Yes |

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()              # [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]
numbers.reverse()           # [1, 1, 2, 3, 4, 5, 6, 9]
```

### Copying

```python
original = [1, 2, 3]

# Shallow copy
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)
```

---

## 4. Dictionary Methods

### Accessing Data

| Method | Description | Returns |
|--------|-------------|---------|
| `.keys()` | All keys | View object |
| `.values()` | All values | View object |
| `.items()` | All key-value pairs | View object |
| `.get(key, default)` | Get value safely | Value or default |

```python
student = {"name": "Alice", "age": 25, "grade": "A"}

print(student.keys())    # dict_keys(['name', 'age', 'grade'])
print(student.values())  # dict_values(['Alice', 25, 'A'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 25), ('grade', 'A')])

# Safe access with .get()
print(student.get("name"))           # "Alice"
print(student.get("email"))          # None
print(student.get("email", "N/A"))   # "N/A"
```

### Modifying Data

| Method | Description |
|--------|-------------|
| `.update(dict)` | Update with another dict |
| `.setdefault(key, default)` | Set default if key missing |
| `.pop(key)` | Remove and return value |
| `.popitem()` | Remove and return last item |
| `.clear()` | Remove all items |

```python
student = {"name": "Alice", "age": 25}

# Update
student.update({"grade": "A", "age": 26})
print(student)  # {'name': 'Alice', 'age': 26, 'grade': 'A'}

# Set default
student.setdefault("email", "unknown")
print(student["email"])  # "unknown"

# Pop
age = student.pop("age")  # age = 26
```

### Copying

```python
original = {"a": 1, "b": 2}

# Shallow copy
copy1 = original.copy()
copy2 = dict(original)
```

---

## 5. Set Methods

### Adding and Removing

| Method | Description |
|--------|-------------|
| `.add(item)` | Add single item |
| `.update(iterable)` | Add multiple items |
| `.remove(item)` | Remove item (raises error if not found) |
| `.discard(item)` | Remove item (no error if not found) |
| `.pop()` | Remove and return arbitrary item |
| `.clear()` | Remove all items |

```python
colors = {"red", "blue"}

colors.add("green")           # {"red", "blue", "green"}
colors.update(["yellow"])     # {"red", "blue", "green", "yellow"}
colors.discard("blue")        # {"red", "green", "yellow"}
colors.remove("red")          # {"green", "yellow"}
```

### Set Operations

| Method | Description | Operator |
|--------|-------------|----------|
| `.union(set)` | All items from both | `|` |
| `.intersection(set)` | Common items | `&` |
| `.difference(set)` | Items in first not second | `-` |
| `.symmetric_difference(set)` | Items in either but not both | `^` |

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.union(b))                  # {1, 2, 3, 4}
print(a.intersection(b))           # {2, 3}
print(a.difference(b))             # {1}
print(a.symmetric_difference(b))   # {1, 4}
```

---

## 6. The split() Method in Detail

### Overview

The `.split()` method breaks a string into a list of substrings based on a separator.

### Basic Syntax

```python
string.split(separator, maxsplit)
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `separator` | Character to split on | Whitespace |
| `maxsplit` | Maximum splits to perform | -1 (all) |

### Splitting by Whitespace (Default)

```python
sentence = "Python is a fun language"
words = sentence.split()

print(words)
# Output: ['Python', 'is', 'a', 'fun', 'language']
```

### Splitting by Specific Character

```python
# Comma separated
data = "apple,banana,cherry"
fruits = data.split(',')
print(fruits)  # ['apple', 'banana', 'cherry']

# Hyphen separated
date = "2024-01-15"
parts = date.split('-')
print(parts)  # ['2024', '01', '15']

# Semicolon separated
items = "a;b;c"
result = items.split(';')
print(result)  # ['a', 'b', 'c']
```

### Limiting the Number of Splits

```python
path = "C:/Users/Documents/file.txt"

# Split only on first two slashes
parts = path.split('/', 2)
print(parts)  # ['C:', 'Users', 'Documents/file.txt']

# Split only on first occurrence
text = "key=value=extra"
result = text.split('=', 1)
print(result)  # ['key', 'value=extra']
```

### Common Use Cases

```python
# Parse CSV line
csv_line = "John,25,Engineer"
name, age, job = csv_line.split(',')
print(f"{name} is a {age} year old {job}")

# Parse key-value pair
config = "username=admin"
key, value = config.split('=')
print(f"Key: {key}, Value: {value}")

# Get file extension
filename = "document.backup.txt"
parts = filename.rsplit('.', 1)  # Split from right
print(parts[-1])  # "txt"
```

### split() vs rsplit()

| Method | Description |
|--------|-------------|
| `.split()` | Split from left |
| `.rsplit()` | Split from right |

```python
text = "a.b.c.d"

print(text.split('.', 2))   # ['a', 'b', 'c.d']
print(text.rsplit('.', 2))  # ['a.b', 'c', 'd']
```

### Handling Edge Cases

```python
# Empty string
print("".split())      # []

# No separator found
print("hello".split(','))  # ['hello']

# Multiple consecutive separators
print("a,,b".split(','))   # ['a', '', 'b']

# Whitespace handling
print("  a  b  ".split())  # ['a', 'b'] (consecutive whitespace treated as one)
```

---

## 7. Quick Reference

### String Methods Summary

| Category | Methods |
|----------|---------|
| Case | `upper()`, `lower()`, `title()`, `capitalize()`, `swapcase()` |
| Whitespace | `strip()`, `lstrip()`, `rstrip()` |
| Search | `find()`, `index()`, `count()`, `startswith()`, `endswith()` |
| Validation | `isdigit()`, `isalpha()`, `isalnum()`, `isspace()` |
| Modification | `replace()`, `split()`, `join()` |

### List Methods Summary

| Category | Methods |
|----------|---------|
| Add | `append()`, `insert()`, `extend()` |
| Remove | `pop()`, `remove()`, `clear()` |
| Search | `index()`, `count()` |
| Order | `sort()`, `reverse()` |
| Copy | `copy()` |

### Dictionary Methods Summary

| Category | Methods |
|----------|---------|
| Access | `keys()`, `values()`, `items()`, `get()` |
| Modify | `update()`, `setdefault()`, `pop()`, `popitem()`, `clear()` |
| Copy | `copy()` |

### Set Methods Summary

| Category | Methods |
|----------|---------|
| Add/Remove | `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()` |
| Operations | `union()`, `intersection()`, `difference()`, `symmetric_difference()` |

### Key Points to Remember

| Point | Description |
|-------|-------------|
| Return values | Some methods return new objects, others modify in place |
| Immutability | String methods always return new strings |
| Mutability | List, dict, set methods often modify in place |
| Chaining | Methods can be chained: `text.strip().upper()` |
| None return | Methods that modify in place often return `None` |

---

## Coverage Checklist

- [x] What methods are
- [x] String methods (case, whitespace, search, validation)
- [x] List methods (add, remove, search, sort)
- [x] Dictionary methods (access, modify)
- [x] Set methods (add, remove, operations)
- [x] split() method in detail
- [x] Quick reference tables
