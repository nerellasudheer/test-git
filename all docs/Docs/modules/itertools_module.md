# Python itertools Module - Quick Reference

Efficient iterators for looping and combinations.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Infinite Iterators](#2-infinite-iterators)
3. [Terminating Iterators](#3-terminating-iterators)
4. [Combinatoric Iterators](#4-combinatoric-iterators)
5. [Quick Reference](#5-quick-reference)

---

## 1. Overview

### What is itertools?

A module providing fast, memory-efficient tools for working with iterators.

### Import

```python
import itertools
# Or import specific functions
from itertools import chain, combinations, permutations
```

---

## 2. Infinite Iterators

### count() - Infinite Counter

```python
from itertools import count

# Count from 0
for i in count():
    if i > 5:
        break
    print(i)  # 0, 1, 2, 3, 4, 5

# Count with start and step
for i in count(10, 2):  # Start at 10, step 2
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20
```

### cycle() - Infinite Cycle

```python
from itertools import cycle

colors = cycle(["red", "green", "blue"])
for i in range(7):
    print(next(colors))
# red, green, blue, red, green, blue, red
```

### repeat() - Repeat Value

```python
from itertools import repeat

# Repeat n times
for x in repeat("Hello", 3):
    print(x)  # Hello, Hello, Hello

# Use with map
list(map(pow, range(5), repeat(2)))  # [0, 1, 4, 9, 16]
```

---

## 3. Terminating Iterators

### chain() - Combine Iterables

```python
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(chain(list1, list2))
print(result)  # [1, 2, 3, 4, 5, 6]

# Chain multiple
combined = list(chain("AB", "CD", "EF"))
print(combined)  # ['A', 'B', 'C', 'D', 'E', 'F']
```

### islice() - Slice Iterator

```python
from itertools import islice

# Slice first n elements
numbers = range(100)
first_five = list(islice(numbers, 5))
print(first_five)  # [0, 1, 2, 3, 4]

# Slice with start and stop
middle = list(islice(range(100), 10, 15))
print(middle)  # [10, 11, 12, 13, 14]
```

### groupby() - Group Consecutive Elements

```python
from itertools import groupby

# Must be sorted first!
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# A [('A', 1), ('A', 2)]
# B [('B', 3), ('B', 4)]
```

### zip_longest() - Zip with Fill

```python
from itertools import zip_longest

a = [1, 2, 3]
b = [4, 5]

# Regular zip stops at shortest
print(list(zip(a, b)))  # [(1, 4), (2, 5)]

# zip_longest fills missing
print(list(zip_longest(a, b, fillvalue=0)))
# [(1, 4), (2, 5), (3, 0)]
```

---

## 4. Combinatoric Iterators

### permutations() - All Orderings

```python
from itertools import permutations

# All permutations
items = [1, 2, 3]
perms = list(permutations(items))
print(perms)
# [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]

# Permutations of length 2
perms2 = list(permutations(items, 2))
print(perms2)
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
```

### combinations() - Unique Selections

```python
from itertools import combinations

items = [1, 2, 3, 4]

# Combinations of 2
combs = list(combinations(items, 2))
print(combs)
# [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

# Combinations of 3
combs3 = list(combinations(items, 3))
print(combs3)
# [(1,2,3), (1,2,4), (1,3,4), (2,3,4)]
```

### combinations_with_replacement()

```python
from itertools import combinations_with_replacement

items = [1, 2, 3]
combs = list(combinations_with_replacement(items, 2))
print(combs)
# [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]
```

### product() - Cartesian Product

```python
from itertools import product

# Like nested for loops
a = [1, 2]
b = ["a", "b"]

result = list(product(a, b))
print(result)
# [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

# Repeat same iterable
dice = list(product(range(1, 7), repeat=2))
# All combinations of rolling 2 dice
```

---

## 5. Quick Reference

### Infinite Iterators

| Function | Description | Example |
|----------|-------------|---------|
| `count(n)` | n, n+1, n+2, ... | `count(10)` |
| `cycle(it)` | Loop forever | `cycle([1,2,3])` |
| `repeat(x)` | x, x, x, ... | `repeat("hi", 3)` |

### Terminating Iterators

| Function | Description |
|----------|-------------|
| `chain(a, b)` | Combine iterables |
| `islice(it, n)` | Slice iterator |
| `groupby(it, key)` | Group consecutive |
| `zip_longest(a, b)` | Zip with fill |

### Combinatoric Iterators

| Function | Description |
|----------|-------------|
| `permutations(it, r)` | All orderings |
| `combinations(it, r)` | Unique selections |
| `product(a, b)` | Cartesian product |

### Common Use Cases

```python
# Flatten nested lists
nested = [[1,2], [3,4], [5,6]]
flat = list(chain.from_iterable(nested))  # [1,2,3,4,5,6]

# Take first n from infinite
first_10 = list(islice(count(), 10))

# All pairs from list
pairs = list(combinations([1,2,3,4], 2))

# Grid coordinates
grid = list(product(range(3), range(3)))
```

---

## Coverage Checklist

- [x] count(), cycle(), repeat()
- [x] chain(), islice(), groupby()
- [x] permutations(), combinations()
- [x] product()
- [x] Quick reference
