# Python File Handling - Complete Guide

A comprehensive reference guide for file operations in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Opening and Closing Files](#2-opening-and-closing-files)
3. [File Modes](#3-file-modes)
4. [Reading Files](#4-reading-files)
5. [Writing Files](#5-writing-files)
6. [File Position Methods](#6-file-position-methods)
7. [File Properties](#7-file-properties)
8. [Path Operations](#8-path-operations)
9. [Error Handling](#9-error-handling)
10. [Best Practices](#10-best-practices)
11. [Quick Reference](#11-quick-reference)

---

## 1. Overview

### What is File Handling?

File handling is the ability to create, read, write, and manipulate files on a computer's storage system. It's fundamental for tasks like reading data, logging, and saving configurations.

### Core Concept

All file operations follow this pattern:
1. **Open** the file
2. **Perform** operations (read/write)
3. **Close** the file

---

## 2. Opening and Closing Files

### The open() Function

**Purpose**: Opens a file and returns a file object.

**Syntax**:
```python
file_object = open(filename, mode)
```

**Parameters**:
- `filename` (str): Path to the file
- `mode` (str): How to open the file (default: 'r')

**Basic Example**:
```python
# Open, read, close manually
f = open("data.txt", "r")
content = f.read()
f.close()  # Must close!
```

### The with Statement (Recommended)

**Purpose**: Automatically closes file after use, even if errors occur.

**Syntax**:
```python
with open(filename, mode) as file_object:
    # operations here
# File automatically closed here
```

**Example**:
```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
# File is automatically closed - no need for f.close()
```

**Benefits**:
- Automatic file closing
- Handles exceptions gracefully
- Cleaner, more readable code
- Prevents resource leaks

---

## 3. File Modes

### Common Modes

| Mode | Name | Description | File Must Exist | Creates New |
|------|------|-------------|-----------------|-------------|
| `r` | Read | Read only | Yes | No |
| `w` | Write | Write only (overwrites!) | No | Yes |
| `a` | Append | Add to end | No | Yes |
| `r+` | Read+Write | Both operations | Yes | No |
| `w+` | Write+Read | Both (overwrites!) | No | Yes |
| `x` | Exclusive | Create new only | Must NOT exist | Yes |

### Binary Modes

Add `b` for binary files (images, executables, etc.):

| Mode | Description |
|------|-------------|
| `rb` | Read binary |
| `wb` | Write binary |
| `ab` | Append binary |

### Mode Comparison

| Mode | Overwrites | Creates | Read | Write |
|------|------------|---------|------|-------|
| `r` | No | No | Yes | No |
| `w` | **Yes** | Yes | No | Yes |
| `a` | No | Yes | No | Yes |
| `r+` | No | No | Yes | Yes |
| `w+` | **Yes** | Yes | Yes | Yes |

---

## 4. Reading Files

### read() - Entire File

**Purpose**: Reads entire file as a single string.

```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
# Output: "Line 1\nLine 2\nLine 3"
```

**Read specific characters**:
```python
with open("file.txt", "r") as f:
    first_10 = f.read(10)  # Read first 10 characters
```

**Use when**: Small files, need entire content as string.

---

### readline() - One Line

**Purpose**: Reads one line at a time.

```python
with open("file.txt", "r") as f:
    line1 = f.readline()  # "First line\n"
    line2 = f.readline()  # "Second line\n"
```

**Use when**: Need manual control, processing conditionally.

---

### readlines() - All Lines as List

**Purpose**: Reads all lines, returns list (includes `\n`).

```python
with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)
# Output: ['Line 1\n', 'Line 2\n', 'Line 3\n']
```

**Use when**: Need all lines as list, access by index.

---

### File Iteration (Best for Large Files)

**Purpose**: Memory-efficient line-by-line reading.

```python
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

**With line numbers**:
```python
with open("file.txt", "r") as f:
    for index, line in enumerate(f, start=1):
        print(f"Line {index}: {line.strip()}")
```

**Use when**: Large files, memory constraints.

---

### Clean Line Reading Patterns

```python
# Pattern 1: read().splitlines() - Cleanest
with open("file.txt", "r") as f:
    lines = f.read().splitlines()  # No \n characters!
    print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# Pattern 2: List comprehension with strip()
with open("file.txt", "r") as f:
    lines = [line.strip() for line in f]

# Pattern 3: Reading numbers
with open("numbers.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]
```

---

## 5. Writing Files

### write() - Write String

**Purpose**: Writes a string to file.

```python
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Second line\n")
```

**Important**: Does NOT add newline automatically - add `\n` manually!

---

### writelines() - Write List

**Purpose**: Writes a list of strings.

```python
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

**Important**: Does NOT add newlines automatically!

```python
# Add newlines to list without them
lines = ["First", "Second", "Third"]
with open("output.txt", "w") as f:
    f.writelines(line + "\n" for line in lines)
```

---

### Appending to Files

```python
with open("log.txt", "a") as f:
    f.write("New log entry\n")
# Adds to end without overwriting existing content
```

---

## 6. File Position Methods

### tell() - Current Position

**Purpose**: Returns current position in file (bytes).

```python
with open("file.txt", "r") as f:
    print(f.tell())  # 0 (at start)
    f.read(5)
    print(f.tell())  # 5 (moved forward)
```

---

### seek() - Move Position

**Purpose**: Moves to a specific position.

**Syntax**:
```python
file.seek(offset, whence)
```

**Parameters**:
- `offset`: Number of bytes to move
- `whence`: Reference point
  - `0` = Start of file (default)
  - `1` = Current position
  - `2` = End of file

```python
with open("file.txt", "r") as f:
    f.read(10)      # Read 10 chars
    f.seek(0)       # Go back to start
    content = f.read()  # Read entire file again
```

---

## 7. File Properties

### Attributes and Methods

```python
with open("file.txt", "r") as f:
    print(f.name)       # "file.txt" - filename
    print(f.mode)       # "r" - mode
    print(f.closed)     # False - is closed?
    print(f.readable()) # True - can read?
    print(f.writable()) # False - can write?

print(f.closed)  # True (after with block)
```

---

## 8. Path Operations

### Using os Module

```python
import os

# Check existence
os.path.exists("file.txt")      # True/False
os.path.isfile("file.txt")      # Is it a file?
os.path.isdir("folder")         # Is it a directory?

# File info
os.path.getsize("file.txt")     # Size in bytes
os.path.abspath("file.txt")     # Full path

# Path manipulation
os.path.basename("/path/to/file.txt")  # "file.txt"
os.path.dirname("/path/to/file.txt")   # "/path/to"
os.path.join("folder", "file.txt")     # "folder/file.txt"
```

### Using pathlib Module (Modern)

```python
from pathlib import Path

path = Path("file.txt")

# Check existence
path.exists()      # True/False
path.is_file()     # Is it a file?
path.is_dir()      # Is it a directory?

# Read/Write
content = path.read_text()
path.write_text("Hello World")

# Path info
path.name          # "file.txt"
path.parent        # Parent directory
path.resolve()     # Absolute path
path.stat().st_size  # File size

# Create directory
Path("new_folder").mkdir(exist_ok=True)
```

---

## 9. Error Handling

### Basic Pattern

```python
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File does not exist")
except PermissionError:
    print("Error: No permission to access file")
except Exception as e:
    print(f"Error: {e}")
```

### Check Before Opening

```python
import os

if os.path.exists("file.txt"):
    with open("file.txt", "r") as f:
        content = f.read()
else:
    print("File does not exist")
```

### Create File If Missing

```python
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found - creating new file")
    with open("file.txt", "w") as f:
        f.write("Default content")
```

---

## 10. Best Practices

### 1. Always Use with Statement

```python
# GOOD
with open("file.txt", "r") as f:
    content = f.read()

# BAD - Must remember to close
f = open("file.txt", "r")
content = f.read()
f.close()
```

### 2. Use Proper Encoding

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### 3. Iterate for Large Files

```python
# GOOD - Memory efficient
with open("large.txt", "r") as f:
    for line in f:
        process(line)

# BAD - Loads entire file into memory
with open("large.txt", "r") as f:
    lines = f.readlines()  # All in memory!
```

### 4. Handle Errors Gracefully

```python
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    content = "default value"
```

### 5. Use Raw Strings for Windows Paths

```python
# GOOD options for Windows paths
path = r"C:\Users\Name\file.txt"  # Raw string
path = "C:/Users/Name/file.txt"   # Forward slashes
path = "C:\\Users\\Name\\file.txt"  # Escaped backslashes
```

---

## 11. Quick Reference

### Reading Methods

| Method | Returns | Includes `\n` | Best For |
|--------|---------|---------------|----------|
| `read()` | String | Yes | Small files |
| `readline()` | String | Yes | One line at a time |
| `readlines()` | List | Yes | All lines as list |
| `for line in f` | String/loop | Yes | Large files |
| `read().splitlines()` | List | **No** | Clean lines |

### Writing Methods

| Method | Input | Adds `\n` |
|--------|-------|-----------|
| `write(str)` | String | No |
| `writelines(list)` | List | No |

### String Cleanup

| Method | Removes |
|--------|---------|
| `strip()` | Whitespace from both ends |
| `lstrip()` | Whitespace from left |
| `rstrip()` | Whitespace from right |
| `rstrip('\n')` | Only newline from right |
| `splitlines()` | Returns list without `\n` |

### File Modes

| Mode | Read | Write | Creates | Overwrites |
|------|------|-------|---------|------------|
| `r` | Yes | No | No | No |
| `w` | No | Yes | Yes | **Yes** |
| `a` | No | Yes | Yes | No |
| `r+` | Yes | Yes | No | No |
| `w+` | Yes | Yes | Yes | **Yes** |

### Common Patterns

| Task | Code |
|------|------|
| Read entire file | `f.read()` |
| Read clean lines | `f.read().splitlines()` |
| Read large file | `for line in f:` |
| Write line | `f.write(text + "\n")` |
| Append | `open("f.txt", "a")` |
| Check exists | `os.path.exists("f.txt")` |

---

## Coverage Checklist

- [x] Opening and closing files
- [x] All file modes explained
- [x] All reading methods
- [x] All writing methods
- [x] File position methods
- [x] File properties
- [x] Path operations (os and pathlib)
- [x] Error handling patterns
- [x] Best practices
- [x] Quick reference tables
