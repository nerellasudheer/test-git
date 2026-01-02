# Python File Reading Methods

## Reading Methods Overview

| Method | Returns | Includes `\n`? | Memory Usage | Best Use Case |
|--------|---------|----------------|--------------|---------------|
| `read()` | Single string | Yes | High (entire file) | Small files, full content needed |
| `readline()` | Single line string | Yes | Low (one line) | Reading one line at a time |
| `readlines()` | List of strings | Yes | High (all lines) | Need all lines as list |
| `for line in f` | Iterator (each line) | Yes | Very Low | **Best for large files** |
| `read().splitlines()` | List of strings | No | High | **Cleanest way to get lines** |

---

## Basic Reading Methods

### 1. read() - Entire file as one string

**Returns:** Single string with all content (includes `\n`)

```python
with open("file.txt", "r") as f:
    content = f.read()
# Result: "line1\nline2\nline3\n"
```

**Use when:** You need the whole file as text (small files)

---

### 2. readline() - One line at a time

**Returns:** Single line string (includes `\n`)

```python
with open("file.txt", "r") as f:
    first_line = f.readline()   # "line1\n"
    second_line = f.readline()  # "line2\n"
```

**Use when:** Reading file line-by-line in a loop

---

### 3. readlines() - All lines as list

**Returns:** List of strings (each has `\n`)

```python
with open("file.txt", "r") as f:
    lines = f.readlines()
# Result: ["line1\n", "line2\n", "line3\n"]
```

**Use when:** You need all lines in memory at once

---

### 4. Iterate directly (BEST for most cases)

**Returns:** Each line one by one (includes `\n`)

```python
with open("file.txt", "r") as f:
    for line in f:
        print(line)  # Each line has \n
```

**Use when:** Processing large files efficiently

---

## Cleaning Methods (Remove `\n` and spaces)

### 5. strip() - Remove ALL whitespace from both ends

**Removes:** `\n`, spaces, tabs from start AND end

```python
"  hello\n".strip()  # "hello"
```

**Use when:** Lines may have extra spaces or tabs

---

### 6. rstrip() - Remove whitespace from RIGHT end only

**Removes:** `\n`, spaces, tabs from end only

```python
"  hello\n".rstrip()  # "  hello"
```

**Use when:** Keep leading spaces, remove trailing

---

### 7. lstrip() - Remove whitespace from LEFT end only

**Removes:** Spaces, tabs from start only

```python
"  hello\n".lstrip()  # "hello\n"
```

**Use when:** Remove indentation, keep `\n`

---

### 8. rstrip('\n') - Remove ONLY newline

**Removes:** Only `\n` character

```python
"hello  \n".rstrip('\n')  # "hello  " (spaces kept!)
```

**Use when:** Preserve all spaces, remove only newline

---

## Splitting Methods

### 9. split() - Split by whitespace

**Returns:** List of words (NO `\n`, no spaces)

```python
"hello world\n".split()  # ["hello", "world"]
```

**Use when:** Extract words from a line

---

### 10. split('\n') - Split by newline

**Returns:** List of lines (NO `\n`)

```python
"line1\nline2\n".split('\n')  # ["line1", "line2", ""]
```

**Use when:** Splitting multi-line string

---

### 11. splitlines() - Smart line splitting

**Returns:** List of lines (NO `\n`)

```python
"line1\nline2\n".splitlines()  # ["line1", "line2"]
```

**Use when:** Best for splitting text by lines (handles all line endings)

### split() vs splitlines()

```python
text = "Hello    World\nHow are you?"

# split() finds every word
print(text.split())
# Output: ['Hello', 'World', 'How', 'are', 'you?']

# splitlines() finds every line
print(text.splitlines())
# Output: ['Hello    World', 'How are you?']
```

---

## Quick Decision Guide

```
Need whole file? → read()
Need list of lines? → read().splitlines() ✅ CLEANEST
Processing line by line? → for line in f ✅ MOST EFFICIENT
Remove \n only? → rstrip('\n')
Remove all whitespace? → strip()
Extract words? → split()
```

---

## Practical Examples

### Example 1: Read numbers from file
```python
# file.txt contains:
# 10
# 20
# 30

with open("file.txt") as f:
    numbers = [int(line.strip()) for line in f]
# Result: [10, 20, 30]
```

---

### Example 2: Read CSV-like data
```python
# data.txt contains:
# name,age,city
# Alice,25,NYC

with open("data.txt") as f:
    for line in f:
        values = line.strip().split(',')
        print(values)
# ["name", "age", "city"]
# ["Alice", "25", "NYC"]
```

---

### Example 3: Keep exact formatting
```python
with open("file.txt") as f:
    lines = [line.rstrip('\n') for line in f]
# Removes \n but keeps all spaces
```

---

## Cleaning Methods Comparison

| Method | Removes From | What It Removes | Preserves Spaces? | Example Input | Example Output |
|--------|--------------|-----------------|-------------------|---------------|----------------|
| `strip()` | Both ends | `\n`, spaces, tabs | No | `"  hello  \n"` | `"hello"` |
| `rstrip()` | Right end only | `\n`, spaces, tabs | Left side | `"  hello  \n"` | `"  hello"` |
| `lstrip()` | Left end only | Spaces, tabs | Right side | `"  hello  \n"` | `"hello  \n"` |
| `rstrip('\n')` | Right end only | **Only** `\n` | All spaces | `"hello  \n"` | `"hello  "` |
| `strip('\n')` | Both ends | **Only** `\n` | All spaces | `"\nhello\n"` | `"hello"` |

---

## Splitting Methods Comparison

| Method | Splits By | Returns | Removes Empty? | Example Input | Example Output |
|--------|-----------|---------|----------------|---------------|----------------|
| `split()` | Any whitespace | List of words | Yes | `"hello world\n"` | `["hello", "world"]` |
| `split(' ')` | Space only | List of parts | No | `"a  b"` | `["a", "", "b"]` |
| `split('\n')` | Newline only | List of lines | No | `"line1\nline2\n"` | `["line1", "line2", ""]` |
| `splitlines()` | All line breaks | List of lines | Yes | `"line1\nline2\n"` | `["line1", "line2"]` |
| `split(',')` | Comma | List of values | No | `"a,b,c"` | `["a", "b", "c"]` |

---

## Common Mistakes vs Correct Approaches

| Inefficient/Wrong | Better Approach | Why? |
|-------------------|-----------------|------|
| `f.readlines()` | `for line in f` | Uses less memory |
| `read().split('\n')` | `read().splitlines()` | Handles all line endings correctly |
| `strip()` on numbers | `rstrip('\n')` | Preserves intentional spaces |
| Multiple `readline()` | `for line in f` | Cleaner and more Pythonic |
| Not using `with` | Always use `with open()` | Auto-closes file properly |

---

## Performance Comparison

| Method | Speed | Memory | Best For |
|--------|-------|--------|----------|
| `for line in f` | Fast | Minimal | Large files |
| `read()` | Medium | High | Small files |
| `readlines()` | Medium | High | Need all lines at once |
| `read().splitlines()` | Medium | High | Clean list without `\n` |

---

## Recommended Patterns

### Pattern 1: Read Numbers from File
```python
# Best approach
with open("numbers.txt") as f:
    numbers = [int(line.strip()) for line in f]
```

### Pattern 2: Read Lines Without `\n`
```python
# Most efficient
with open("file.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Cleanest (small files)
with open("file.txt") as f:
    lines = f.read().splitlines()
```

### Pattern 3: Process CSV Data
```python
# For CSV files
with open("data.csv") as f:
    for line in f:
        values = line.strip().split(',')
```

### Pattern 4: Read Entire Content
```python
# For small text files
with open("file.txt") as f:
    content = f.read()
    words = content.split()
    print(f"Total words: {len(words)}")
```

---

## Complete Example

```python
# Reading different file formats

# 1. Plain text file (with \n removed)
with open("text.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# 2. Numbers file
with open("numbers.txt") as f:
    numbers = [int(line.strip()) for line in f]

# 3. CSV file
with open("data.csv") as f:
    next(f)  # Skip header
    for line in f:
        name, age, city = line.strip().split(',')
        print(f"{name} is {age} from {city}")

# 4. Entire file content
with open("story.txt") as f:
    content = f.read()
    words = content.split()
    print(f"Total words: {len(words)}")
```

---

## Key Takeaways

1. **For large files:** Always use `for line in f` (memory efficient)
2. **To remove `\n`:** Use `rstrip('\n')` or `splitlines()`
3. **To remove all whitespace:** Use `strip()`
4. **To split into words:** Use `split()`
5. **For CSV data:** Use `split(',')` after `strip()`
6. **Always use:** `with open()` context manager
