# Python Indexing and Slicing - Quick Reference

Understanding how to access elements in Python sequences.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Positive Indexing](#2-positive-indexing)
3. [Negative Indexing](#3-negative-indexing)
4. [Slicing](#4-slicing)
5. [Quick Reference](#5-quick-reference)

---

## 1. Overview

### What is Indexing?

Indexing means accessing elements of a sequence (string, list, tuple) using their position (index number).

### Key Points

- Python uses **zero-based indexing** - first element is at index 0
- **Positive indexing** starts from 0 (left to right)
- **Negative indexing** starts from -1 (right to left)
- Works with strings, lists, and tuples
- Index must be in range, else `IndexError`

---

## 2. Positive Indexing

### Index Positions (Left to Right)

```
String:  P   y   t   h   o   n
Index:   0   1   2   3   4   5
```

### Examples

```python
text = "Python"
print(text[0])   # P (first character)
print(text[1])   # y
print(text[5])   # n (last character)

numbers = [10, 20, 30, 40, 50]
print(numbers[0])   # 10
print(numbers[2])   # 30
print(numbers[4])   # 50
```

---

## 3. Negative Indexing

### Index Positions (Right to Left)

```
String:  P    y    t    h    o    n
Index:  -6   -5   -4   -3   -2   -1
```

### Examples

```python
text = "Python"
print(text[-1])   # n (last character)
print(text[-2])   # o
print(text[-6])   # P (first character)

numbers = [10, 20, 30, 40, 50]
print(numbers[-1])   # 50 (last)
print(numbers[-2])   # 40
print(numbers[-5])   # 10 (first)
```

---

## 4. Slicing

### Syntax

```python
sequence[start:stop:step]
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `start` | Starting index (inclusive) | 0 |
| `stop` | Ending index (exclusive) | End of sequence |
| `step` | Increment between elements | 1 |

### Basic Slicing

```python
text = "Python"

print(text[0:3])   # Pyt (index 0, 1, 2)
print(text[2:5])   # tho (index 2, 3, 4)
print(text[:3])    # Pyt (from start to index 2)
print(text[3:])    # hon (from index 3 to end)
print(text[:])     # Python (entire string)
```

### Slicing with Step

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (odd indices)
print(numbers[::3])    # [0, 3, 6, 9] (every 3rd element)
```

### Reverse with Negative Step

```python
text = "Python"
print(text[::-1])   # nohtyP (reversed)

numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])   # [5, 4, 3, 2, 1]
```

### Negative Indices in Slicing

```python
text = "Python"

print(text[-3:])     # hon (last 3 characters)
print(text[:-2])     # Pyth (all except last 2)
print(text[-4:-1])   # tho (from -4 to -2)
```

### Nested Indexing

```python
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[0])       # [1, 2]
print(nested[0][1])    # 2
print(nested[1][0])    # 3
print(nested[-1][-1])  # 6
```

---

## 5. Quick Reference

### Index Reference

| Index Type | First Element | Last Element |
|------------|---------------|--------------|
| Positive | `0` | `len(seq) - 1` |
| Negative | `-len(seq)` | `-1` |

### Slicing Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| `[n]` | Single element | `text[0]` → `'P'` |
| `[start:stop]` | Range | `text[0:3]` → `'Pyt'` |
| `[:stop]` | From beginning | `text[:3]` → `'Pyt'` |
| `[start:]` | To end | `text[3:]` → `'hon'` |
| `[:]` | Copy all | `text[:]` → `'Python'` |
| `[::step]` | Every nth | `text[::2]` → `'Pto'` |
| `[::-1]` | Reverse | `text[::-1]` → `'nohtyP'` |
| `[-n:]` | Last n elements | `text[-3:]` → `'hon'` |
| `[:-n]` | All except last n | `text[:-2]` → `'Pyth'` |

### Common Operations

```python
# Get first element
first = sequence[0]

# Get last element
last = sequence[-1]

# Get first n elements
first_n = sequence[:n]

# Get last n elements
last_n = sequence[-n:]

# Remove first element
without_first = sequence[1:]

# Remove last element
without_last = sequence[:-1]

# Reverse
reversed_seq = sequence[::-1]

# Every other element
every_other = sequence[::2]
```

---

## Coverage Checklist

- [x] Indexing overview
- [x] Positive indexing
- [x] Negative indexing
- [x] Basic slicing
- [x] Slicing with step
- [x] Reverse with negative step
- [x] Nested indexing
- [x] Quick reference tables
