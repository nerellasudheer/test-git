# File Reading Methods - Comparison Guide

A quick reference comparing file reading and string processing methods.

---

## File Reading Methods

### read()

**Purpose**: Reads entire file as a single string.

```python
# File: "Hello\nWorld\nPython"

with open("file.txt", "r") as f:
    content = f.read()
    print(content)       # Hello\nWorld\nPython
    print(type(content)) # <class 'str'>
```

---

### readline()

**Purpose**: Reads one line at a time (includes `\n`).

```python
with open("file.txt", "r") as f:
    line1 = f.readline()  # "First line\n"
    line2 = f.readline()  # "Second line\n"
```

---

### readlines()

**Purpose**: Reads all lines as a list (each includes `\n`).

```python
# File:
# Hello
# World
# Python

with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['Hello\n', 'World\n', 'Python\n']
```

---

## String Processing Methods

### splitlines()

**Purpose**: Splits string by line breaks, removes `\n` characters.

```python
text = "Hello\nWorld\nPython"
lines = text.splitlines()
print(lines)  # ['Hello', 'World', 'Python'] - No \n!

# With file:
with open("file.txt", "r") as f:
    lines = f.read().splitlines()  # Clean list without \n
```

---

### split()

**Purpose**: Splits string by any separator (default: whitespace).

```python
# Split by whitespace (default)
text = "Hello World Python"
words = text.split()
print(words)  # ['Hello', 'World', 'Python']

# Split by comma
text = "apple,banana,orange"
fruits = text.split(',')
print(fruits)  # ['apple', 'banana', 'orange']

# Split by newline
text = "Hello\nWorld\nPython"
lines = text.split('\n')
print(lines)  # ['Hello', 'World', 'Python']
```

---

### strip()

**Purpose**: Removes whitespace from both ends.

```python
text = "  Hello World  \n"
clean = text.strip()
print(clean)  # "Hello World"
```

---

### lstrip()

**Purpose**: Removes whitespace from left side only.

```python
text = "  Hello World  "
result = text.lstrip()
print(result)  # "Hello World  " (right spaces remain)
```

---

### rstrip()

**Purpose**: Removes whitespace from right side only.

```python
text = "  Hello World  \n"
result = text.rstrip()
print(result)  # "  Hello World" (left spaces remain)
```

---

## Quick Comparison Table

| Method | Returns | Includes `\n`? | Use Case |
|--------|---------|----------------|----------|
| `read()` | Single string | Yes | Read entire file |
| `readline()` | One line (string) | Yes | Read line by line |
| `readlines()` | List of lines | Yes | Get all lines as list |
| `splitlines()` | List of lines | **No** | Clean list without `\n` |
| `split()` | List | Depends | Split by any separator |
| `strip()` | String | Removes | Clean both ends |
| `lstrip()` | String | Removes left | Clean left side |
| `rstrip()` | String | Removes right | Clean right side |

---

## Practical Example

```python
# File content:
#   123
#   456
#   789

# Method 1: readlines() + strip()
with open("numbers.txt", "r") as f:
    numbers = [line.strip() for line in f.readlines()]
    print(numbers)  # ['123', '456', '789']

# Method 2: read() + splitlines() (Cleanest)
with open("numbers.txt", "r") as f:
    numbers = f.read().splitlines()
    print(numbers)  # ['123', '456', '789']

# Method 3: Iterate directly (Most Efficient)
with open("numbers.txt", "r") as f:
    numbers = [line.strip() for line in f]
    print(numbers)  # ['123', '456', '789']
```

---

## Best Practices

| Task | Recommended Method |
|------|-------------------|
| Read numbers from file | `f.read().splitlines()` |
| Lines with extra spaces | `[line.strip() for line in f]` |
| Large files | `for line in f:` |
| Need clean list | `read().splitlines()` |

---

## Key Takeaways

1. **`readlines()`** - Returns list with `\n` at end of each line
2. **`splitlines()`** - Returns clean list without `\n`
3. **`strip()`** - Removes whitespace from both ends
4. **`split('\n')`** - May include empty strings if file ends with `\n`
5. **File iteration** - Most memory efficient for large files
