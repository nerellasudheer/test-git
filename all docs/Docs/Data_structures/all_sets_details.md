# Python Sets - Complete Guide

A comprehensive reference guide for Python Sets.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Creating Sets](#2-creating-sets)
3. [Set Methods](#3-set-methods)
4. [Set Operations](#4-set-operations)
5. [Hashability and Immutability](#5-hashability-and-immutability)
6. [Frozenset](#6-frozenset)
7. [Common Mistakes](#7-common-mistakes)
8. [Use Cases](#8-use-cases)
9. [Quick Reference](#9-quick-reference)

---

## 1. Overview

### What is a Set?

A set is an **unordered** collection of **unique** elements. Sets are mutable (you can add/remove elements), but elements themselves must be immutable (hashable).

### Key Characteristics

| Feature | Description |
|---------|-------------|
| Unordered | No specific order, no indexing |
| Unique Elements | Duplicates automatically removed |
| Mutable | Can add/remove elements |
| Elements Must Be Immutable | Only hashable types allowed |
| Fast Membership Testing | O(1) lookup time |

### Set vs List vs Tuple

| Feature | Set | List | Tuple |
|---------|-----|------|-------|
| Ordered | No | Yes | Yes |
| Duplicates | No | Yes | Yes |
| Mutable | Yes | Yes | No |
| Indexed | No | Yes | Yes |
| Use Case | Unique items | Ordered collection | Fixed data |

---

## 2. Creating Sets

### Basic Creation

```python
# Empty set (NOT {} - that creates empty dict!)
empty_set = set()

# Set with values
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# Duplicates are automatically removed
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # Output: {1, 2, 3}
```

### Creating from Other Types

```python
# From list (removes duplicates)
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3}

# From string (each character becomes element)
chars = set("hello")
print(chars)  # Output: {'h', 'e', 'l', 'o'}

# From tuple
my_set = set((1, 2, 3))
print(my_set)  # Output: {1, 2, 3}
```

### Important: Empty Set vs Empty Dict

```python
# WRONG - This creates empty dictionary!
not_a_set = {}
print(type(not_a_set))  # Output: <class 'dict'>

# CORRECT - Use set() for empty set
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>
```

---

## 3. Set Methods

### Adding Elements

#### add(element)

**Purpose**: Adds a single element to the set.

```python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Adding existing element does nothing
fruits.add("apple")
print(fruits)  # Output: {'apple', 'banana', 'cherry'}
```

---

#### update(iterable)

**Purpose**: Adds multiple elements from an iterable.

```python
fruits = {"apple", "banana"}
fruits.update(["cherry", "date"])
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'date'}

# Can update with multiple iterables
fruits.update(["elderberry"], {"fig", "grape"})
print(fruits)  # Contains all fruits
```

---

### Removing Elements

#### remove(element)

**Purpose**: Removes element. **Raises KeyError** if not found.

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# KeyError if element doesn't exist
# fruits.remove("grape")  # KeyError: 'grape'
```

---

#### discard(element)

**Purpose**: Removes element. **No error** if not found.

```python
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# No error if element doesn't exist
fruits.discard("grape")  # No error
print(fruits)  # Output: {'apple', 'cherry'}
```

---

#### pop()

**Purpose**: Removes and returns an arbitrary element.

```python
fruits = {"apple", "banana", "cherry"}
removed = fruits.pop()
print(removed)  # Output: (any element - sets are unordered)
print(fruits)   # Output: remaining elements

# Raises KeyError on empty set
# empty_set = set()
# empty_set.pop()  # KeyError: 'pop from an empty set'
```

---

#### clear()

**Purpose**: Removes all elements.

```python
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()
```

---

### Set Operations

#### union(other_set) or |

**Purpose**: Returns all elements from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Using method
result = a.union(b)
print(result)  # Output: {1, 2, 3, 4, 5}

# Using operator
result = a | b
print(result)  # Output: {1, 2, 3, 4, 5}
```

---

#### intersection(other_set) or &

**Purpose**: Returns elements common to both sets.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Using method
result = a.intersection(b)
print(result)  # Output: {3, 4}

# Using operator
result = a & b
print(result)  # Output: {3, 4}
```

---

#### difference(other_set) or -

**Purpose**: Returns elements in first set but not in second.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Using method
result = a.difference(b)
print(result)  # Output: {1, 2}

# Using operator
result = a - b
print(result)  # Output: {1, 2}

# Note: Order matters
print(b - a)  # Output: {5, 6}
```

---

#### symmetric_difference(other_set) or ^

**Purpose**: Returns elements in either set, but not both.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Using method
result = a.symmetric_difference(b)
print(result)  # Output: {1, 2, 5, 6}

# Using operator
result = a ^ b
print(result)  # Output: {1, 2, 5, 6}
```

---

### In-Place Operations

These modify the original set:

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Update (union in-place)
a.update(b)  # or a |= b

# Intersection update
a.intersection_update(b)  # or a &= b

# Difference update
a.difference_update(b)  # or a -= b

# Symmetric difference update
a.symmetric_difference_update(b)  # or a ^= b
```

---

### Comparison Methods

#### issubset(other_set) or <=

**Purpose**: Returns True if all elements are in other set.

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))   # Output: True
print(a <= b)          # Output: True
print(b.issubset(a))   # Output: False
```

---

#### issuperset(other_set) or >=

**Purpose**: Returns True if set contains all elements of other set.

```python
a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))  # Output: True
print(a >= b)           # Output: True
print(b.issuperset(a))  # Output: False
```

---

#### isdisjoint(other_set)

**Purpose**: Returns True if sets have no common elements.

```python
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

print(a.isdisjoint(b))  # Output: True (no common elements)
print(a.isdisjoint(c))  # Output: False (3 is common)
```

---

### Other Methods

#### copy()

**Purpose**: Returns a shallow copy of the set.

```python
original = {1, 2, 3}
copied = original.copy()

copied.add(4)
print(original)  # Output: {1, 2, 3} - unchanged
print(copied)    # Output: {1, 2, 3, 4}
```

---

## 4. Set Operations Visual Guide

```
Set A = {1, 2, 3, 4}
Set B = {3, 4, 5, 6}

Union (A | B):           {1, 2, 3, 4, 5, 6}  - All elements
Intersection (A & B):    {3, 4}              - Common elements
Difference (A - B):      {1, 2}              - In A, not in B
Symmetric Diff (A ^ B):  {1, 2, 5, 6}        - In A or B, not both
```

---

## 5. Hashability and Immutability

### What Can Be in a Set?

Sets can only contain **hashable** (immutable) elements:

| Type | Can Be Set Element? |
|------|---------------------|
| int | Yes |
| float | Yes |
| str | Yes |
| tuple | Yes (if contents are hashable) |
| frozenset | Yes |
| list | No |
| dict | No |
| set | No |

### Examples

```python
# VALID set elements
valid_set = {1, 2.5, "hello", (1, 2, 3)}
print(valid_set)

# INVALID - lists are mutable
# invalid_set = {[1, 2, 3]}  # TypeError: unhashable type: 'list'

# INVALID - dicts are mutable
# invalid_set = {{"a": 1}}  # TypeError: unhashable type: 'dict'

# INVALID - sets are mutable
# invalid_set = {{1, 2}}  # TypeError: unhashable type: 'set'
```

### Why Must Elements Be Hashable?

Sets use hashing for:
1. **Fast lookup** - O(1) time to check if element exists
2. **Uniqueness** - Hash determines if element already exists
3. **Structural integrity** - If elements could change, set would break

```python
# How hash works
print(hash(42))        # Works - integer is immutable
print(hash("hello"))   # Works - string is immutable
print(hash((1, 2)))    # Works - tuple is immutable

# print(hash([1, 2]))  # TypeError - list is mutable
```

---

## 6. Frozenset

### What is a Frozenset?

A frozenset is an **immutable** version of a set. Once created, it cannot be modified.

```python
# Create frozenset
fs = frozenset([1, 2, 3, 4])
print(fs)  # Output: frozenset({1, 2, 3, 4})

# Cannot modify
# fs.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
```

### When to Use Frozenset?

1. **As dictionary keys** (sets cannot be dict keys)
2. **As elements of another set** (sets cannot contain sets)
3. **When you need immutable set**

```python
# Frozenset as dictionary key
fs = frozenset([1, 2, 3])
my_dict = {fs: "value"}
print(my_dict[fs])  # Output: value

# Frozenset as set element
outer_set = {frozenset([1, 2]), frozenset([3, 4])}
print(outer_set)  # Output: {frozenset({1, 2}), frozenset({3, 4})}
```

### Available Frozenset Operations

Frozensets support all non-modifying set operations:

```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# These work
print(fs1 | fs2)  # Union
print(fs1 & fs2)  # Intersection
print(fs1 - fs2)  # Difference
print(fs1 ^ fs2)  # Symmetric difference
print(3 in fs1)   # Membership

# These don't work
# fs1.add(4)       # No add()
# fs1.remove(1)    # No remove()
```

---

## 7. Common Mistakes

### Mistake 1: Creating Empty Set with {}

```python
# WRONG - Creates empty dict
not_set = {}
print(type(not_set))  # Output: <class 'dict'>

# CORRECT
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>
```

### Mistake 2: Trying to Add Mutable Elements

```python
# WRONG
my_set = {1, 2, 3}
# my_set.add([4, 5])  # TypeError: unhashable type: 'list'

# CORRECT - Use tuple instead
my_set.add((4, 5))
print(my_set)  # Output: {1, 2, 3, (4, 5)}
```

### Mistake 3: Expecting Order

```python
# WRONG - Sets are unordered
my_set = {3, 1, 4, 1, 5, 9, 2, 6}
# Don't assume any specific order when iterating

# CORRECT - Sort if you need order
for item in sorted(my_set):
    print(item)
```

### Mistake 4: Using remove() on Potentially Missing Element

```python
my_set = {1, 2, 3}

# WRONG - Raises error if not found
# my_set.remove(5)  # KeyError: 5

# CORRECT - Use discard() for safe removal
my_set.discard(5)  # No error
```

---

## 8. Use Cases

### 1. Removing Duplicates from List

```python
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(my_list))
print(unique)  # Output: [1, 2, 3, 4]
```

### 2. Fast Membership Testing

```python
# Set is much faster than list for membership testing
allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # O(1) - very fast
    print("Access granted")
```

### 3. Finding Common Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = set(list1) & set(list2)
print(common)  # Output: {4, 5}
```

### 4. Finding Differences

```python
old_users = {"alice", "bob", "charlie"}
new_users = {"bob", "charlie", "david"}

# Who left?
left = old_users - new_users
print(left)  # Output: {'alice'}

# Who joined?
joined = new_users - old_users
print(joined)  # Output: {'david'}
```

---

## 9. Quick Reference

### Creating Sets

| Syntax | Description |
|--------|-------------|
| `set()` | Empty set |
| `{1, 2, 3}` | Set with values |
| `set([1, 2, 3])` | From list |
| `frozenset([1, 2, 3])` | Immutable set |

### Methods Summary

| Method | Purpose | Raises Error |
|--------|---------|--------------|
| `add(x)` | Add one element | - |
| `update(iter)` | Add multiple elements | - |
| `remove(x)` | Remove element | KeyError |
| `discard(x)` | Remove element safely | - |
| `pop()` | Remove arbitrary element | KeyError |
| `clear()` | Remove all | - |
| `copy()` | Shallow copy | - |

### Operations Summary

| Operation | Method | Operator | Returns |
|-----------|--------|----------|---------|
| Union | `union()` | `\|` | All elements |
| Intersection | `intersection()` | `&` | Common elements |
| Difference | `difference()` | `-` | In first, not second |
| Symmetric Diff | `symmetric_difference()` | `^` | In either, not both |

### Comparison Methods

| Method | Operator | Purpose |
|--------|----------|---------|
| `issubset()` | `<=` | All elements in other |
| `issuperset()` | `>=` | Contains all of other |
| `isdisjoint()` | - | No common elements |

### Set vs Frozenset

| Feature | Set | Frozenset |
|---------|-----|-----------|
| Mutable | Yes | No |
| Can be dict key | No | Yes |
| Can be set element | No | Yes |
| add/remove methods | Yes | No |

---

## Coverage Checklist

- [x] Creating sets (all methods)
- [x] All set methods documented
- [x] Set operations (union, intersection, etc.)
- [x] Hashability explained
- [x] Frozenset documented
- [x] Common mistakes explained
- [x] Use cases with examples
- [x] Quick reference tables
