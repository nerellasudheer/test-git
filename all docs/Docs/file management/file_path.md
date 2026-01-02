# Python File Paths - Quick Guide

Understanding absolute and relative file paths in Python.

---

## Path Types

### Absolute Path

Starts from the root of the file system. Works from anywhere.

**Windows Example**:
```
C:/Users/Sudheer/Desktop/project/file.txt
```

**Linux/Mac Example**:
```
/home/user/project/file.txt
```

---

### Relative Path

Relative to the current working directory.

| Scenario | Path | Meaning |
|----------|------|---------|
| Same folder | `file.txt` | File in current directory |
| Subfolder | `subfolder/file.txt` | Go into subfolder |
| Parent folder | `../file.txt` | Go up one level |
| Two levels up | `../../file.txt` | Go up two levels |
| Sibling folder | `../other/file.txt` | Up one, into other |

---

## Examples

### Current Directory Structure

```
Desktop/
├── project/          ← You are here
│   ├── script.py
│   └── data/
│       └── file.txt
└── other/
    └── test.txt
```

### From script.py:

| Target | Path |
|--------|------|
| file.txt in data | `data/file.txt` |
| test.txt in other | `../other/test.txt` |
| Desktop | `../../` |

---

## Windows Path Conventions

Python interprets `\` as escape character. Use one of these:

| Convention | Example | Notes |
|------------|---------|-------|
| Raw string (Recommended) | `r"C:\Users\file.txt"` | Prefix with `r` |
| Forward slashes | `"C:/Users/file.txt"` | Works on Windows |
| Double backslashes | `"C:\\Users\\file.txt"` | Escape the backslash |

---

## Code Examples

```python
# Absolute path (always works)
with open("C:/Users/Sudheer/Desktop/data.txt", "r") as f:
    content = f.read()

# Relative path (depends on working directory)
with open("data/file.txt", "r") as f:
    content = f.read()

# Parent folder
with open("../other_folder/file.txt", "r") as f:
    content = f.read()

# Windows raw string
with open(r"C:\Users\Name\file.txt", "r") as f:
    content = f.read()
```

---

## Using pathlib (Modern Approach)

```python
from pathlib import Path

# Current directory
current = Path.cwd()

# Absolute path
path = Path("C:/Users/Name/file.txt")

# Relative path
path = Path("data/file.txt")

# Parent directory
parent = path.parent

# Join paths
full_path = Path("folder") / "subfolder" / "file.txt"
```

---

## Quick Reference

| Need | Path |
|------|------|
| Current folder | `file.txt` |
| Go into subfolder | `subfolder/file.txt` |
| Go up one level | `../file.txt` |
| Go up two levels | `../../file.txt` |
| Full Windows path | `r"C:\path\file.txt"` |

---

## Key Points

1. **Absolute paths** always start from root (`C:/` or `/`)
2. **Relative paths** depend on current working directory
3. Use `../` to go up one directory level
4. Use forward slashes `/` in Python (works on all OS)
5. Use raw strings `r"..."` for Windows paths with backslashes
