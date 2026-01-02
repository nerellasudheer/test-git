# Python Built-in Functions - Quick Reference

Essential built-in functions every Python developer should know.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Type Conversion](#2-type-conversion)
3. [Math Functions](#3-math-functions)
4. [Sequence Functions](#4-sequence-functions)
5. [Iteration Functions](#5-iteration-functions)
6. [Object Inspection](#6-object-inspection)
7. [I/O Functions](#7-io-functions)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What are Built-in Functions?

Functions that are always available in Python without importing any module.

### Most Common Built-ins

| Function | Purpose | Example |
|----------|---------|---------|
| `print()` | Output to console | `print("Hello")` |
| `len()` | Get length | `len([1,2,3])` → 3 |
| `type()` | Get type | `type(5)` → int |
| `input()` | Get user input | `input("Name: ")` |
| `range()` | Generate sequence | `range(5)` |

---

## 2. Type Conversion

### int() - Convert to Integer

```python
print(int("42"))      # 42
print(int(3.9))       # 3 (truncates, not rounds)
print(int("101", 2))  # 5 (binary to decimal)
print(int("ff", 16))  # 255 (hex to decimal)
```

### float() - Convert to Float

```python
print(float("3.14"))  # 3.14
print(float(5))       # 5.0
print(float("inf"))   # inf
```

### str() - Convert to String

```python
print(str(42))        # "42"
print(str(3.14))      # "3.14"
print(str([1,2,3]))   # "[1, 2, 3]"
```

### bool() - Convert to Boolean

```python
print(bool(1))        # True
print(bool(0))        # False
print(bool(""))       # False
print(bool("text"))   # True
print(bool([]))       # False
print(bool([1]))      # True
```

### list(), tuple(), set(), dict()

```python
# String to list
print(list("abc"))         # ['a', 'b', 'c']

# List to tuple
print(tuple([1,2,3]))      # (1, 2, 3)

# List to set (removes duplicates)
print(set([1,1,2,2,3]))    # {1, 2, 3}

# List of tuples to dict
print(dict([("a",1),("b",2)]))  # {'a': 1, 'b': 2}
```

---

## 3. Math Functions

### abs() - Absolute Value

```python
print(abs(-5))        # 5
print(abs(5))         # 5
print(abs(-3.14))     # 3.14
```

### round() - Round Number

```python
print(round(3.7))       # 4
print(round(3.2))       # 3
print(round(3.14159, 2))# 3.14
print(round(2.5))       # 2 (banker's rounding)
print(round(3.5))       # 4
```

### min() and max()

```python
# With multiple arguments
print(min(5, 3, 8, 1))    # 1
print(max(5, 3, 8, 1))    # 8

# With iterable
nums = [5, 3, 8, 1]
print(min(nums))          # 1
print(max(nums))          # 8

# With key function
words = ["apple", "pie", "banana"]
print(min(words, key=len))  # "pie"
print(max(words, key=len))  # "banana"
```

### sum()

```python
nums = [1, 2, 3, 4, 5]
print(sum(nums))          # 15
print(sum(nums, 10))      # 25 (start from 10)

# Sum of squares
print(sum(x**2 for x in range(5)))  # 30
```

### pow() and divmod()

```python
# pow(base, exp) = base ** exp
print(pow(2, 3))          # 8
print(pow(2, 3, 5))       # 3 (2^3 % 5)

# divmod(a, b) = (a // b, a % b)
print(divmod(17, 5))      # (3, 2)
```

---

## 4. Sequence Functions

### len() - Length

```python
print(len("hello"))       # 5
print(len([1, 2, 3]))     # 3
print(len({"a": 1}))      # 1
```

### sorted() - Return Sorted List

```python
nums = [3, 1, 4, 1, 5]
print(sorted(nums))           # [1, 1, 3, 4, 5]
print(sorted(nums, reverse=True))  # [5, 4, 3, 1, 1]

# Original unchanged
print(nums)                   # [3, 1, 4, 1, 5]

# Sort by key
words = ["banana", "apple", "cherry"]
print(sorted(words))                # ['apple', 'banana', 'cherry']
print(sorted(words, key=len))       # ['apple', 'banana', 'cherry']
```

### reversed() - Reverse Iterator

```python
nums = [1, 2, 3]
print(list(reversed(nums)))   # [3, 2, 1]

# In for loop
for x in reversed(nums):
    print(x)  # 3, 2, 1
```

### all() and any()

```python
# all() - True if ALL are truthy
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(all([1, 2, 3]))            # True
print(all([1, 0, 3]))            # False

# any() - True if ANY is truthy
print(any([False, False, True])) # True
print(any([False, False, False]))# False
print(any([0, 0, 1]))            # True

# Practical example
ages = [25, 30, 17, 40]
print(all(age >= 18 for age in ages))  # False
print(any(age < 18 for age in ages))   # True
```

---

## 5. Iteration Functions

### range() - Number Sequence

```python
# range(stop)
print(list(range(5)))         # [0, 1, 2, 3, 4]

# range(start, stop)
print(list(range(2, 6)))      # [2, 3, 4, 5]

# range(start, stop, step)
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]
```

### enumerate() - Index + Value

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start from different number
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
```

### zip() - Combine Iterables

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
# Alice is 25
# Bob is 30
# Charlie is 35

# Create dictionary
person_dict = dict(zip(names, ages))
print(person_dict)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Unequal lengths - stops at shortest
list(zip([1,2,3], ['a','b']))  # [(1,'a'), (2,'b')]
```

### map() - Apply Function to All

```python
nums = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25]

# Convert all to string
strings = list(map(str, nums))
print(strings)  # ['1', '2', '3', '4', '5']

# Multiple iterables
result = list(map(lambda x, y: x + y, [1,2,3], [10,20,30]))
print(result)  # [11, 22, 33]
```

### filter() - Filter by Condition

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6, 8, 10]

# Remove empty strings
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, words))
print(non_empty)  # ['hello', 'world', 'python']
```

---

## 6. Object Inspection

### type() - Get Type

```python
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type([1,2,3]))     # <class 'list'>

# Type checking
if type(x) == int:
    print("It's an integer")
```

### isinstance() - Check Type (Preferred)

```python
print(isinstance(42, int))         # True
print(isinstance("hi", str))       # True
print(isinstance([1,2], list))     # True

# Multiple types
print(isinstance(42, (int, float)))  # True

# Works with inheritance
class Animal: pass
class Dog(Animal): pass

dog = Dog()
print(isinstance(dog, Dog))    # True
print(isinstance(dog, Animal)) # True
```

### dir() - List Attributes

```python
# List methods of a string
print(dir("hello"))
# [..., 'upper', 'lower', 'split', ...]

# List methods of a list
print(dir([]))
# [..., 'append', 'pop', 'sort', ...]
```

### help() - Get Documentation

```python
help(str.split)  # Shows documentation for split method
help(len)        # Shows documentation for len function
```

### id() - Object Identity

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(id(x))        # Memory address of x
print(id(y))        # Same as x (same object)
print(id(z))        # Different (new object)

print(x is y)       # True
print(x is z)       # False
```

---

## 7. I/O Functions

### print() - Output

```python
# Basic print
print("Hello, World!")

# Multiple values
print("Name:", "Alice", "Age:", 25)

# Custom separator
print("a", "b", "c", sep="-")     # a-b-c

# Custom end
print("Hello", end=" ")
print("World")                    # Hello World

# Print to file
with open("output.txt", "w") as f:
    print("Hello", file=f)
```

### input() - User Input

```python
name = input("Enter your name: ")
print(f"Hello, {name}")

# Convert input
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

### open() - File Operations

```python
# Read file
with open("file.txt", "r") as f:
    content = f.read()

# Write file
with open("file.txt", "w") as f:
    f.write("Hello, World!")

# Append to file
with open("file.txt", "a") as f:
    f.write("\nNew line")
```

---

## 8. Quick Reference

### Type Conversion Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `int()` | To integer | `int("42")` → 42 |
| `float()` | To float | `float("3.14")` → 3.14 |
| `str()` | To string | `str(42)` → "42" |
| `bool()` | To boolean | `bool(1)` → True |
| `list()` | To list | `list("abc")` → ['a','b','c'] |
| `tuple()` | To tuple | `tuple([1,2])` → (1,2) |
| `set()` | To set | `set([1,1,2])` → {1,2} |
| `dict()` | To dict | `dict([("a",1)])` → {'a':1} |

### Math Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `abs()` | Absolute value | `abs(-5)` → 5 |
| `round()` | Round number | `round(3.7)` → 4 |
| `min()` | Minimum | `min(1,2,3)` → 1 |
| `max()` | Maximum | `max(1,2,3)` → 3 |
| `sum()` | Sum of iterable | `sum([1,2,3])` → 6 |
| `pow()` | Power | `pow(2,3)` → 8 |

### Sequence Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `len()` | Length | `len([1,2,3])` → 3 |
| `sorted()` | Sorted copy | `sorted([3,1,2])` → [1,2,3] |
| `reversed()` | Reverse iterator | `list(reversed([1,2,3]))` |
| `all()` | All truthy? | `all([True,True])` → True |
| `any()` | Any truthy? | `any([False,True])` → True |

### Iteration Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `range()` | Number sequence | `range(5)` → 0,1,2,3,4 |
| `enumerate()` | Index + value | `enumerate(['a','b'])` |
| `zip()` | Combine iterables | `zip([1,2],['a','b'])` |
| `map()` | Apply function | `map(str, [1,2,3])` |
| `filter()` | Filter by condition | `filter(bool, [0,1,2])` |

### Object Inspection

| Function | Purpose | Example |
|----------|---------|---------|
| `type()` | Get type | `type(42)` → int |
| `isinstance()` | Check type | `isinstance(42, int)` → True |
| `dir()` | List attributes | `dir([])` |
| `help()` | Documentation | `help(str.split)` |
| `id()` | Object identity | `id(x)` |

---

## Coverage Checklist

- [x] Type conversion functions
- [x] Math functions (abs, round, min, max, sum)
- [x] Sequence functions (len, sorted, reversed, all, any)
- [x] Iteration functions (range, enumerate, zip, map, filter)
- [x] Object inspection (type, isinstance, dir, help, id)
- [x] I/O functions (print, input, open)
- [x] Quick reference tables
