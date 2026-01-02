# Python Important Points - Quick Tips

A collection of useful Python tips and tricks to remember.

---

## Table of Contents

1. [Assignment Operators](#1-assignment-operators)
2. [Loop Tips](#2-loop-tips)
3. [Type Conversion](#3-type-conversion)
4. [Class Variables](#4-class-variables)
5. [Functions as Variables](#5-functions-as-variables)
6. [Global Variables](#6-global-variables)
7. [__init__ Method](#7-init-method)
8. [File Reading Methods](#8-file-reading-methods)
9. [String join()](#9-string-join)

---

## 1. Assignment Operators

### Augmented Assignment Operators

Shorthand for modifying a variable:

```python
age = 10
age += 2   # Same as: age = age + 2 → 12
age -= 3   # Same as: age = age - 3 → 9
age *= 2   # Same as: age = age * 2 → 18
age /= 3   # Same as: age = age / 3 → 6.0
```

| Operator | Example | Equivalent |
|----------|---------|------------|
| `+=` | `x += 2` | `x = x + 2` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |
| `//=` | `x //= 2` | `x = x // 2` |
| `%=` | `x %= 2` | `x = x % 2` |
| `**=` | `x **= 2` | `x = x ** 2` |

---

## 2. Loop Tips

### Reversed Range

Use `reversed()` to iterate in reverse order:

```python
# Forward
for i in range(1, 10):
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9

# Reversed
for i in reversed(range(1, 10)):
    print(i, end=" ")  # 9 8 7 6 5 4 3 2 1
```

---

## 3. Type Conversion

### String to List

Convert a string to a list of characters:

```python
s = "sudheer"
print(s)           # sudheer

y = list(s)
print(y)           # ['s', 'u', 'd', 'h', 'e', 'e', 'r']
```

### Tuple to List

Tuples are immutable, but you can convert to list to modify:

```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)   # [1, 2, 3]
my_list.append(4)          # [1, 2, 3, 4]
```

---

## 4. Class Variables

### Accessing Class Variables

Best practice: Access class variables using the class name, not the object:

```python
class School:
    current_school = "SVJC High School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = School("Sudheer", 30)
student2 = School("Raju", 25)

# Not recommended (works but unclear)
print(student1.current_school)

# Best practice (clear and explicit)
print(School.current_school)
```

---

## 5. Functions as Variables

### Assigning Functions to Variables

Functions can be assigned to variables and called through them:

```python
def welcome(name):
    print(f"Welcome {name}")

x = welcome    # Assign function to variable
x("Sudheer")   # Call function through variable
# Output: Welcome Sudheer
```

---

## 6. Global Variables

### Modifying Global Variables in Functions

Use `global` keyword to modify a global variable inside a function:

```python
count = 0

def increment():
    global count    # Declare we're using the global variable
    count += 1

increment()
print(count)  # 1

# Without global keyword, creates a new local variable
def increment_wrong():
    count = 10      # This creates a local variable, doesn't change global
```

---

## 7. __init__ Method

### Default Values and Fixed Values

```python
class Welcome:
    def __init__(self, name, age, height=10):
        self.name = name           # Required parameter
        self.age = age             # Required parameter
        self.height = height       # Optional, has default value
        self.gender = "male"       # Fixed value, user can't override

# Default value (height=10) used
person1 = Welcome("John", 25)
print(person1.height)  # 10

# User provides height, overwrites default
person2 = Welcome("Jane", 30, height=15)
print(person2.height)  # 15

# Fixed value (gender) is always "male"
print(person1.gender)  # male (can't be changed during init)
```

---

## 8. File Reading Methods

### readlines() vs splitlines()

| Method | Source | Purpose |
|--------|--------|---------|
| `readlines()` | File Object | Read file into list of lines |
| `splitlines()` | String Object | Split string into list of lines |

```python
# readlines() - from file
with open("data.txt", "r") as file:
    lines = file.readlines()
    # ['Line 1\n', 'Line 2\n', 'Line 3\n']

# splitlines() - from string
text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()
# ['Line 1', 'Line 2', 'Line 3']
```

**Note**: `splitlines()` removes newline characters; `readlines()` keeps them.

---

## 9. String join()

### Combining List Items into String

Use `" ".join()` to combine a list of strings with a separator:

```python
names = ["Alice", "Bob", "Charlie"]

# Join with space
result = " ".join(names)
print(result)  # Alice Bob Charlie

# Join with comma
result = ", ".join(names)
print(result)  # Alice, Bob, Charlie

# Join with no separator
result = "".join(names)
print(result)  # AliceBobCharlie
```

---

## Quick Reference

| Topic | Key Point |
|-------|-----------|
| `+=`, `-=`, etc. | Augmented assignment operators |
| `reversed(range())` | Iterate in reverse order |
| `list(string)` | Convert string to list of characters |
| `Class.variable` | Best way to access class variables |
| `x = function` | Functions can be assigned to variables |
| `global var` | Modify global variable in function |
| `height=10` | Default parameter value |
| `self.gender="male"` | Fixed value in __init__ |
| `readlines()` | File method, keeps newlines |
| `splitlines()` | String method, removes newlines |
| `" ".join(list)` | Combine list items into string |

---

## Coverage Checklist

- [x] Augmented assignment operators
- [x] Reversed range in loops
- [x] Type conversion tips
- [x] Class variable access best practice
- [x] Functions as variables
- [x] Global keyword usage
- [x] __init__ default and fixed values
- [x] readlines() vs splitlines()
- [x] String join() method
