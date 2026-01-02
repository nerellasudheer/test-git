# Python Dunder (Magic) Methods - Complete Guide

Special methods with double underscores that define object behavior.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Object Representation](#2-object-representation)
3. [Comparison Methods](#3-comparison-methods)
4. [Arithmetic Methods](#4-arithmetic-methods)
5. [Container Methods](#5-container-methods)
6. [Context Managers](#6-context-managers)
7. [Iterator Protocol](#7-iterator-protocol)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What are Dunder Methods?

Dunder (double underscore) methods, also called magic methods, are special methods that Python calls automatically in certain situations.

### Common Dunder Methods

| Method | Called When |
|--------|-------------|
| `__init__` | Object created |
| `__str__` | `str(obj)` or `print(obj)` |
| `__repr__` | `repr(obj)` or in console |
| `__len__` | `len(obj)` |
| `__add__` | `obj + other` |
| `__eq__` | `obj == other` |

### Basic Example

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title}"

    def __len__(self):
        return self.pages

book = Book("Python Guide", 300)
print(book)       # Python Guide (calls __str__)
print(len(book))  # 300 (calls __len__)
```

---

## 2. Object Representation

### __str__ - User-Friendly String

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Alice", 25)
print(p)           # Alice, 25 years old
print(str(p))      # Alice, 25 years old
```

### __repr__ - Developer String

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Alice", 25)
print(repr(p))     # Person('Alice', 25)
print(str(p))      # Alice, 25 years old

# In console or list:
print([p])         # [Person('Alice', 25)] - uses __repr__
```

### __str__ vs __repr__

| Method | Purpose | Called By |
|--------|---------|-----------|
| `__str__` | Human-readable | `str()`, `print()` |
| `__repr__` | Unambiguous, recreatable | `repr()`, console, containers |

```python
# Best practice: implement both
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"
```

---

## 3. Comparison Methods

### All Comparison Methods

| Method | Operator | Description |
|--------|----------|-------------|
| `__eq__` | `==` | Equal |
| `__ne__` | `!=` | Not equal |
| `__lt__` | `<` | Less than |
| `__le__` | `<=` | Less or equal |
| `__gt__` | `>` | Greater than |
| `__ge__` | `>=` | Greater or equal |

### Basic Example

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

m1 = Money(100)
m2 = Money(200)
m3 = Money(100)

print(m1 == m3)   # True
print(m1 < m2)    # True
print(m2 >= m1)   # True
```

### Using functools.total_ordering

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    # Other comparisons auto-generated!

s1 = Student("Alice", 85)
s2 = Student("Bob", 90)
print(s1 < s2)   # True
print(s1 <= s2)  # True (auto-generated)
```

---

## 4. Arithmetic Methods

### Basic Arithmetic

| Method | Operator | Example |
|--------|----------|---------|
| `__add__` | `+` | `a + b` |
| `__sub__` | `-` | `a - b` |
| `__mul__` | `*` | `a * b` |
| `__truediv__` | `/` | `a / b` |
| `__floordiv__` | `//` | `a // b` |
| `__mod__` | `%` | `a % b` |
| `__pow__` | `**` | `a ** b` |

### Example: Vector Class

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)    # Vector(4, 6)
print(v2 - v1)    # Vector(2, 2)
print(v1 * 3)     # Vector(3, 6)
```

### Reverse Operations

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __mul__(self, other):
        return Money(self.amount * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"${self.amount}"

m = Money(100)
print(m * 2)      # $200 (calls __mul__)
print(2 * m)      # $200 (calls __rmul__)
```

### In-Place Operations

| Method | Operator | Example |
|--------|----------|---------|
| `__iadd__` | `+=` | `a += b` |
| `__isub__` | `-=` | `a -= b` |
| `__imul__` | `*=` | `a *= b` |

```python
class Counter:
    def __init__(self, count=0):
        self.count = count

    def __iadd__(self, value):
        self.count += value
        return self

    def __repr__(self):
        return f"Counter({self.count})"

c = Counter(5)
c += 3
print(c)  # Counter(8)
```

---

## 5. Container Methods

### Basic Container Methods

| Method | Called By | Description |
|--------|-----------|-------------|
| `__len__` | `len(obj)` | Return length |
| `__getitem__` | `obj[key]` | Get item |
| `__setitem__` | `obj[key] = val` | Set item |
| `__delitem__` | `del obj[key]` | Delete item |
| `__contains__` | `item in obj` | Check membership |

### Example: Custom List

```python
class MyList:
    def __init__(self, items=None):
        self._items = items if items else []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]

    def __contains__(self, item):
        return item in self._items

    def __repr__(self):
        return f"MyList({self._items})"

ml = MyList([1, 2, 3, 4, 5])
print(len(ml))         # 5
print(ml[2])           # 3
print(3 in ml)         # True
ml[0] = 10
print(ml)              # MyList([10, 2, 3, 4, 5])
```

### Slicing Support

```python
class Sentence:
    def __init__(self, text):
        self.words = text.split()

    def __getitem__(self, index):
        # Supports both index and slice
        if isinstance(index, slice):
            return ' '.join(self.words[index])
        return self.words[index]

    def __len__(self):
        return len(self.words)

s = Sentence("Hello World from Python")
print(s[0])        # Hello
print(s[1:3])      # World from
print(s[-1])       # Python
```

---

## 6. Context Managers

### __enter__ and __exit__

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exception, False to propagate
        return False

# Usage with 'with' statement
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
# File automatically closed after 'with' block
```

### Timer Context Manager

```python
import time

class Timer:
    def __init__(self, name="Timer"):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        print(f"{self.name}: {self.end - self.start:.4f} seconds")
        return False

# Usage
with Timer("My Operation"):
    # Some code to time
    sum(range(1000000))
# Output: My Operation: 0.0234 seconds
```

### Database Connection Example

```python
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.host}")
        self.connection = "connected"  # Simulated
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        self.connection = None
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False

with DatabaseConnection("localhost") as db:
    print("Using database")
# Output:
# Connecting to localhost
# Using database
# Closing connection
```

---

## 7. Iterator Protocol

### __iter__ and __next__

```python
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Usage
for num in CountDown(5):
    print(num)  # 5, 4, 3, 2, 1

# Or
countdown = CountDown(3)
print(list(countdown))  # [3, 2, 1]
```

### Separate Iterator Class

```python
class Book:
    def __init__(self, title, chapters):
        self.title = title
        self.chapters = chapters

    def __iter__(self):
        return BookIterator(self)

class BookIterator:
    def __init__(self, book):
        self.chapters = book.chapters
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.chapters):
            raise StopIteration
        chapter = self.chapters[self.index]
        self.index += 1
        return chapter

book = Book("Python Guide", ["Intro", "Basics", "Advanced"])
for chapter in book:
    print(chapter)  # Intro, Basics, Advanced
```

### Infinite Iterator

```python
class InfiniteCounter:
    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

counter = InfiniteCounter()
for i, num in enumerate(counter):
    if i >= 5:
        break
    print(num)  # 0, 1, 2, 3, 4
```

---

## 8. Quick Reference

### Representation

| Method | Purpose |
|--------|---------|
| `__str__` | Human-readable string |
| `__repr__` | Developer string |

### Comparison

| Method | Operator |
|--------|----------|
| `__eq__` | `==` |
| `__ne__` | `!=` |
| `__lt__` | `<` |
| `__le__` | `<=` |
| `__gt__` | `>` |
| `__ge__` | `>=` |

### Arithmetic

| Method | Operator |
|--------|----------|
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__truediv__` | `/` |
| `__mod__` | `%` |
| `__pow__` | `**` |

### Container

| Method | Called By |
|--------|-----------|
| `__len__` | `len()` |
| `__getitem__` | `obj[key]` |
| `__setitem__` | `obj[key] = val` |
| `__contains__` | `in` |

### Context Manager

| Method | Purpose |
|--------|---------|
| `__enter__` | Setup (returns context) |
| `__exit__` | Cleanup (handle exceptions) |

### Iterator

| Method | Purpose |
|--------|---------|
| `__iter__` | Return iterator |
| `__next__` | Return next value |

### Other Useful Methods

| Method | Purpose |
|--------|---------|
| `__init__` | Initialize object |
| `__del__` | Object destruction |
| `__call__` | Make object callable |
| `__hash__` | Make object hashable |
| `__bool__` | Boolean conversion |

---

## Coverage Checklist

- [x] __str__ and __repr__
- [x] Comparison methods (__eq__, __lt__, __gt__, etc.)
- [x] Arithmetic methods (__add__, __sub__, __mul__, etc.)
- [x] Container methods (__len__, __getitem__, __setitem__)
- [x] Context managers (__enter__, __exit__)
- [x] Iterator protocol (__iter__, __next__)
- [x] Quick reference tables
