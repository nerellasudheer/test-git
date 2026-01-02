# Python Data Structures - Comparison Guide

A quick reference comparing common operations across List, Tuple, Dictionary, and Set.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Common Operations Comparison](#2-common-operations-comparison)
3. [Adding Elements](#3-adding-elements)
4. [Removing Elements](#4-removing-elements)
5. [Accessing Elements](#5-accessing-elements)
6. [Checking Existence](#6-checking-existence)
7. [Converting Between Types](#7-converting-between-types)
8. [When to Use Each](#8-when-to-use-each)
9. [Quick Reference](#9-quick-reference)

---

## 1. Overview

### Data Structure Characteristics

| Feature | List | Tuple | Dictionary | Set |
|---------|------|-------|------------|-----|
| Syntax | `[]` | `()` | `{}` | `{}` |
| Ordered | Yes | Yes | Yes (3.7+) | No |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | Keys: No | No |
| Indexed | Yes | Yes | By key | No |
| Hashable | No | Yes | Keys only | Elements only |

### Memory Tip

```
List    = [ ]  → Square brackets → Flexible (mutable)
Tuple   = ( )  → Parentheses    → Protected (immutable)
Dict    = { }  → Curly + colon  → Key:Value pairs
Set     = { }  → Curly alone    → Unique values only
```

---

## 2. Common Operations Comparison

| Operation | List | Tuple | Dictionary | Set |
|-----------|------|-------|------------|-----|
| Add element | `append(x)` | N/A | `d[key] = value` | `add(x)` |
| Add multiple | `extend(iter)` | N/A | `update({})` | `update(iter)` |
| Insert at index | `insert(i, x)` | N/A | N/A | N/A |
| Remove by value | `remove(x)` | N/A | `pop(key)` | `remove(x)` / `discard(x)` |
| Remove last | `pop()` | N/A | `popitem()` | `pop()` |
| Clear all | `clear()` | N/A | `clear()` | `clear()` |
| Access item | `list[i]` | `tuple[i]` | `dict[key]` | N/A |
| Check existence | `x in list` | `x in tuple` | `key in dict` | `x in set` |
| Get length | `len(list)` | `len(tuple)` | `len(dict)` | `len(set)` |
| Sort | `sort()` | N/A | N/A | N/A |
| Reverse | `reverse()` | N/A | N/A | N/A |

---

## 3. Adding Elements

### List

```python
my_list = [1, 2]

# Add single element
my_list.append(3)          # [1, 2, 3]

# Add multiple elements
my_list.extend([4, 5])     # [1, 2, 3, 4, 5]

# Insert at index
my_list.insert(0, 0)       # [0, 1, 2, 3, 4, 5]
```

### Dictionary

```python
my_dict = {"a": 1}

# Add single key-value
my_dict["b"] = 2           # {"a": 1, "b": 2}

# Add multiple key-values
my_dict.update({"c": 3, "d": 4})  # {"a": 1, "b": 2, "c": 3, "d": 4}
```

### Set

```python
my_set = {1, 2}

# Add single element
my_set.add(3)              # {1, 2, 3}

# Add multiple elements
my_set.update([4, 5])      # {1, 2, 3, 4, 5}
```

### Tuple

```python
my_tuple = (1, 2)

# Cannot add! Create new tuple instead
my_tuple = my_tuple + (3,)  # (1, 2, 3)
```

---

## 4. Removing Elements

### List

```python
my_list = [1, 2, 3, 2, 4]

# Remove by value (first occurrence)
my_list.remove(2)          # [1, 3, 2, 4]

# Remove by index and return
item = my_list.pop(0)      # item=1, list=[3, 2, 4]

# Remove last and return
last = my_list.pop()       # last=4, list=[3, 2]

# Clear all
my_list.clear()            # []
```

### Dictionary

```python
my_dict = {"a": 1, "b": 2, "c": 3}

# Remove by key and return value
value = my_dict.pop("a")   # value=1, dict={"b": 2, "c": 3}

# Remove last item
item = my_dict.popitem()   # item=("c", 3), dict={"b": 2}

# Delete by key
del my_dict["b"]           # {}

# Clear all
my_dict.clear()            # {}
```

### Set

```python
my_set = {1, 2, 3, 4}

# Remove (raises error if not found)
my_set.remove(2)           # {1, 3, 4}

# Discard (no error if not found)
my_set.discard(5)          # {1, 3, 4} (no error)

# Remove arbitrary element
item = my_set.pop()        # Removes random element

# Clear all
my_set.clear()             # set()
```

### Tuple

```python
my_tuple = (1, 2, 3)

# Cannot remove! Create new tuple instead
my_tuple = my_tuple[:1] + my_tuple[2:]  # (1, 3)
```

---

## 5. Accessing Elements

### List and Tuple (By Index)

```python
my_list = [10, 20, 30, 40]
my_tuple = (10, 20, 30, 40)

# By positive index
print(my_list[0])    # 10
print(my_tuple[1])   # 20

# By negative index
print(my_list[-1])   # 40 (last)
print(my_tuple[-2])  # 30 (second last)

# Slicing
print(my_list[1:3])  # [20, 30]
print(my_tuple[::2]) # (10, 30)
```

### Dictionary (By Key)

```python
my_dict = {"name": "Alice", "age": 25}

# By key (raises KeyError if not found)
print(my_dict["name"])     # Alice

# By key with get (returns None or default if not found)
print(my_dict.get("name"))           # Alice
print(my_dict.get("city"))           # None
print(my_dict.get("city", "Unknown")) # Unknown
```

### Set (Cannot Access by Index!)

```python
my_set = {1, 2, 3}

# CANNOT access by index
# print(my_set[0])  # TypeError!

# Can only iterate or check membership
for item in my_set:
    print(item)

print(2 in my_set)  # True
```

---

## 6. Checking Existence

```python
# List
my_list = [1, 2, 3]
print(2 in my_list)      # True

# Tuple
my_tuple = (1, 2, 3)
print(2 in my_tuple)     # True

# Dictionary (checks KEYS by default)
my_dict = {"a": 1, "b": 2}
print("a" in my_dict)        # True (key)
print(1 in my_dict)          # False (1 is a value, not a key)
print(1 in my_dict.values()) # True (check values)

# Set
my_set = {1, 2, 3}
print(2 in my_set)       # True
```

---

## 7. Converting Between Types

### To List

```python
# From tuple
list((1, 2, 3))      # [1, 2, 3]

# From set
list({3, 1, 2})      # [1, 2, 3] (order may vary)

# From dict (keys only)
list({"a": 1, "b": 2})  # ["a", "b"]

# From string
list("hello")        # ["h", "e", "l", "l", "o"]
```

### To Tuple

```python
# From list
tuple([1, 2, 3])     # (1, 2, 3)

# From set
tuple({3, 1, 2})     # (1, 2, 3) (order may vary)

# From string
tuple("hello")       # ("h", "e", "l", "l", "o")
```

### To Set

```python
# From list (removes duplicates)
set([1, 2, 2, 3])    # {1, 2, 3}

# From tuple
set((1, 2, 3))       # {1, 2, 3}

# From string
set("hello")         # {"h", "e", "l", "o"}
```

### To Dictionary

```python
# From list of tuples
dict([("a", 1), ("b", 2)])  # {"a": 1, "b": 2}

# From two lists using zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict(zip(keys, values))     # {"a": 1, "b": 2, "c": 3}
```

---

## 8. When to Use Each

### Use List When:

- You need **ordered** data
- You need to **modify** elements
- You need **duplicate** values
- You need **index-based** access

```python
# Shopping cart (ordered, can have duplicates)
cart = ["apple", "banana", "apple", "orange"]
```

### Use Tuple When:

- Data should **not change**
- You need it as a **dictionary key**
- Returning **multiple values** from a function
- **Fixed** collections (coordinates, RGB values)

```python
# Coordinates (fixed, immutable)
point = (10, 20)
location = {(0, 0): "origin", (10, 20): "destination"}
```

### Use Dictionary When:

- You need **key-value** pairs
- You need **fast lookup** by key
- Keys are **unique identifiers**

```python
# User data (access by meaningful keys)
user = {"name": "Alice", "age": 25, "email": "alice@email.com"}
```

### Use Set When:

- You need **unique** elements only
- You need **fast membership** testing
- You need **mathematical set operations**

```python
# Unique tags
tags = {"python", "programming", "tutorial"}
# Fast lookup: O(1) time
if "python" in tags:
    print("Found!")
```

---

## 9. Quick Reference

### Creation

| Type | Empty | With Values |
|------|-------|-------------|
| List | `[]` or `list()` | `[1, 2, 3]` |
| Tuple | `()` or `tuple()` | `(1, 2, 3)` |
| Dict | `{}` or `dict()` | `{"a": 1}` |
| Set | `set()` (NOT `{}`) | `{1, 2, 3}` |

### Common Methods

| Operation | List | Dict | Set |
|-----------|------|------|-----|
| Add one | `append(x)` | `d[k] = v` | `add(x)` |
| Add many | `extend(iter)` | `update({})` | `update(iter)` |
| Remove | `remove(x)` | `pop(k)` | `remove(x)` |
| Safe remove | N/A | `pop(k, default)` | `discard(x)` |
| Clear | `clear()` | `clear()` | `clear()` |
| Copy | `copy()` | `copy()` | `copy()` |

### Key Differences

| Feature | Ordered | Mutable | Duplicates | Indexed |
|---------|---------|---------|------------|---------|
| List | Yes | Yes | Yes | Yes |
| Tuple | Yes | No | Yes | Yes |
| Dict | Yes* | Yes | No (keys) | By key |
| Set | No | Yes | No | No |

*Python 3.7+

### Performance

| Operation | List | Dict | Set |
|-----------|------|------|-----|
| Access by index | O(1) | N/A | N/A |
| Access by key | O(n) | O(1) | N/A |
| Search | O(n) | O(1) | O(1) |
| Insert | O(1)* | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |

*append() is O(1), insert() is O(n)

---

## Coverage Checklist

- [x] All four data structures compared
- [x] Adding elements for each
- [x] Removing elements for each
- [x] Accessing elements for each
- [x] Checking existence
- [x] Converting between types
- [x] When to use each
- [x] Quick reference tables
