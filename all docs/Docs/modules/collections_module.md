# Python Collections Module - Quick Reference

Specialized container datatypes.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Counter](#2-counter)
3. [defaultdict](#3-defaultdict)
4. [namedtuple](#4-namedtuple)
5. [deque](#5-deque)
6. [OrderedDict](#6-ordereddict)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is collections?

The collections module provides specialized container datatypes as alternatives to Python's built-in containers.

### Import

```python
from collections import Counter, defaultdict, namedtuple, deque, OrderedDict
```

### Main Classes

| Class | Description |
|-------|-------------|
| `Counter` | Count hashable objects |
| `defaultdict` | Dict with default values |
| `namedtuple` | Tuple with named fields |
| `deque` | Double-ended queue |
| `OrderedDict` | Dict that remembers order |

---

## 2. Counter

### What is Counter?

A dictionary subclass for counting hashable objects.

### Basic Usage

```python
from collections import Counter

# Count items in list
colors = ["red", "blue", "red", "green", "blue", "red"]
count = Counter(colors)
print(count)  # Counter({'red': 3, 'blue': 2, 'green': 1})

# Count characters in string
char_count = Counter("mississippi")
print(char_count)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

### Counter Methods

```python
c = Counter(["a", "b", "a", "c", "a", "b"])

# Most common elements
print(c.most_common(2))  # [('a', 3), ('b', 2)]

# Access count
print(c["a"])  # 3
print(c["x"])  # 0 (not KeyError!)

# Update counts
c.update(["a", "d"])
print(c)  # Counter({'a': 4, 'b': 2, 'c': 1, 'd': 1})

# Total count
print(sum(c.values()))  # 8
```

### Counter Arithmetic

```python
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)  # Counter({'a': 4, 'b': 3})
print(c1 - c2)  # Counter({'a': 2})
```

---

## 3. defaultdict

### What is defaultdict?

A dictionary that provides default values for missing keys.

### Basic Usage

```python
from collections import defaultdict

# Default int (0)
counts = defaultdict(int)
counts["a"] += 1
counts["b"] += 1
counts["a"] += 1
print(counts)  # defaultdict(<class 'int'>, {'a': 2, 'b': 1})

# Default list
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["fruits"].append("banana")
groups["vegetables"].append("carrot")
print(groups)  # {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}
```

### Common Default Factories

| Factory | Default Value |
|---------|---------------|
| `int` | `0` |
| `list` | `[]` |
| `set` | `set()` |
| `str` | `""` |
| `lambda: value` | Custom default |

### Practical Example

```python
from collections import defaultdict

# Group items by category
items = [
    ("fruit", "apple"),
    ("vegetable", "carrot"),
    ("fruit", "banana"),
    ("vegetable", "broccoli")
]

grouped = defaultdict(list)
for category, item in items:
    grouped[category].append(item)

print(dict(grouped))
# {'fruit': ['apple', 'banana'], 'vegetable': ['carrot', 'broccoli']}
```

---

## 4. namedtuple

### What is namedtuple?

Creates tuple subclasses with named fields.

### Basic Usage

```python
from collections import namedtuple

# Define a namedtuple
Point = namedtuple("Point", ["x", "y"])

# Create instances
p = Point(3, 4)
print(p.x)      # 3
print(p.y)      # 4
print(p[0])     # 3 (still works like tuple)

# Unpack
x, y = p
```

### Alternative Field Definition

```python
# Space-separated string
Person = namedtuple("Person", "name age city")

# Create instance
person = Person("Alice", 25, "NYC")
print(person.name)  # Alice
print(person.age)   # 25
```

### namedtuple Methods

```python
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

# Convert to dict
print(p._asdict())  # {'x': 3, 'y': 4}

# Replace values (returns new tuple)
p2 = p._replace(x=10)
print(p2)  # Point(x=10, y=4)

# Get field names
print(p._fields)  # ('x', 'y')
```

### Practical Example

```python
from collections import namedtuple

# Database record representation
User = namedtuple("User", ["id", "name", "email"])

users = [
    User(1, "Alice", "alice@example.com"),
    User(2, "Bob", "bob@example.com")
]

for user in users:
    print(f"{user.name}: {user.email}")
```

---

## 5. deque

### What is deque?

Double-ended queue - efficient appends and pops from both ends.

### Basic Usage

```python
from collections import deque

# Create deque
d = deque([1, 2, 3])

# Add elements
d.append(4)        # Add to right: [1, 2, 3, 4]
d.appendleft(0)    # Add to left: [0, 1, 2, 3, 4]

# Remove elements
d.pop()            # Remove from right: [0, 1, 2, 3]
d.popleft()        # Remove from left: [1, 2, 3]

print(d)  # deque([1, 2, 3])
```

### deque Methods

```python
d = deque([1, 2, 3, 4, 5])

# Rotate
d.rotate(2)    # Rotate right: [4, 5, 1, 2, 3]
d.rotate(-2)   # Rotate left: [1, 2, 3, 4, 5]

# Extend
d.extend([6, 7])       # Add to right
d.extendleft([0, -1])  # Add to left (reversed)

# Count and index
print(d.count(3))  # 1
print(d.index(3))  # Position of element 3
```

### Fixed Size deque

```python
from collections import deque

# Keep only last 3 items
history = deque(maxlen=3)
history.append(1)
history.append(2)
history.append(3)
history.append(4)  # 1 is removed
print(history)  # deque([2, 3, 4], maxlen=3)
```

### Use Case: Queue and Stack

```python
from collections import deque

# Queue (FIFO)
queue = deque()
queue.append("first")
queue.append("second")
print(queue.popleft())  # "first"

# Stack (LIFO)
stack = deque()
stack.append("first")
stack.append("second")
print(stack.pop())  # "second"
```

---

## 6. OrderedDict

### What is OrderedDict?

Dictionary that remembers insertion order. (Note: Regular dicts maintain order since Python 3.7)

```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3

print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

### Move to End

```python
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

od.move_to_end("a")        # Move to last
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

od.move_to_end("c", last=False)  # Move to first
print(od)  # OrderedDict([('c', 3), ('b', 2), ('a', 1)])
```

---

## 7. Quick Reference

### Counter

```python
from collections import Counter
c = Counter(["a", "b", "a"])
c.most_common(2)     # Top 2 items
c["x"]               # 0 (missing key)
c.update(["c"])      # Add counts
```

### defaultdict

```python
from collections import defaultdict
d = defaultdict(list)
d["key"].append("value")  # No KeyError
```

### namedtuple

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x, p.y, p[0]      # Access methods
```

### deque

```python
from collections import deque
d = deque([1, 2, 3])
d.append(4)         # Right
d.appendleft(0)     # Left
d.pop()             # Right
d.popleft()         # Left
d.rotate(n)         # Rotate
```

### Summary Table

| Class | Use When |
|-------|----------|
| `Counter` | Counting items |
| `defaultdict` | Need default values |
| `namedtuple` | Readable tuple fields |
| `deque` | Fast appends/pops both ends |
| `OrderedDict` | Need move_to_end method |

---

## Coverage Checklist

- [x] Counter basics and methods
- [x] defaultdict with different factories
- [x] namedtuple creation and methods
- [x] deque operations
- [x] OrderedDict
- [x] Practical examples
- [x] Quick reference
