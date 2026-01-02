# Python JSON Module - Quick Reference

Reading and writing JSON data.

---

## Table of Contents

1. [Overview](#1-overview)
2. [JSON to Python](#2-json-to-python)
3. [Python to JSON](#3-python-to-json)
4. [Working with Files](#4-working-with-files)
5. [Advanced Options](#5-advanced-options)
6. [Quick Reference](#6-quick-reference)

---

## 1. Overview

### What is JSON?

JSON (JavaScript Object Notation) is a lightweight data format for storing and exchanging data.

### Import

```python
import json
```

### Type Mapping

| JSON | Python |
|------|--------|
| object | dict |
| array | list |
| string | str |
| number (int) | int |
| number (real) | float |
| true | True |
| false | False |
| null | None |

---

## 2. JSON to Python

### json.loads() - Parse String

```python
import json

# JSON string to Python
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)

print(data)           # {'name': 'Alice', 'age': 25}
print(data["name"])   # Alice
print(type(data))     # <class 'dict'>
```

### Parse Different Types

```python
# Array
json_array = '[1, 2, 3, 4, 5]'
numbers = json.loads(json_array)
print(numbers)  # [1, 2, 3, 4, 5]

# Nested structure
json_nested = '''
{
    "user": {
        "name": "Bob",
        "scores": [85, 90, 78]
    }
}
'''
data = json.loads(json_nested)
print(data["user"]["scores"])  # [85, 90, 78]
```

---

## 3. Python to JSON

### json.dumps() - Convert to String

```python
import json

# Python to JSON string
data = {"name": "Alice", "age": 25, "active": True}
json_string = json.dumps(data)

print(json_string)  # {"name": "Alice", "age": 25, "active": true}
print(type(json_string))  # <class 'str'>
```

### Formatting Options

```python
data = {"name": "Alice", "hobbies": ["reading", "coding"]}

# Pretty print with indentation
formatted = json.dumps(data, indent=4)
print(formatted)
# {
#     "name": "Alice",
#     "hobbies": [
#         "reading",
#         "coding"
#     ]
# }

# Sort keys
sorted_json = json.dumps(data, sort_keys=True, indent=2)
```

---

## 4. Working with Files

### json.dump() - Write to File

```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "SQL"]
}

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### json.load() - Read from File

```python
import json

# Read from file
with open("data.json", "r") as f:
    data = json.load(f)

print(data["name"])  # Alice
print(data["skills"])  # ['Python', 'SQL']
```

### Practical Example

```python
import json

# Configuration file handling
def load_config(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_config(filename, config):
    with open(filename, "w") as f:
        json.dump(config, f, indent=4)

# Usage
config = load_config("settings.json")
config["theme"] = "dark"
save_config("settings.json", config)
```

---

## 5. Advanced Options

### Custom Serialization

```python
import json
from datetime import datetime

# Custom encoder for datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"event": "Meeting", "date": datetime.now()}
json_string = json.dumps(data, cls=DateTimeEncoder)
print(json_string)
```

### Handle Non-Serializable Types

```python
import json

data = {
    "name": "Alice",
    "data": {1, 2, 3}  # Sets are not JSON serializable
}

# Convert set to list before serializing
def convert_sets(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

json_string = json.dumps(data, default=convert_sets)
```

### Error Handling

```python
import json

json_string = '{"name": "Alice", "age": }'  # Invalid JSON

try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

---

## 6. Quick Reference

### Main Functions

| Function | Purpose | From/To |
|----------|---------|---------|
| `json.loads(str)` | Parse JSON string | String → Python |
| `json.dumps(obj)` | Convert to JSON string | Python → String |
| `json.load(file)` | Read JSON file | File → Python |
| `json.dump(obj, file)` | Write to JSON file | Python → File |

### Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `indent` | Pretty print | `json.dumps(data, indent=4)` |
| `sort_keys` | Sort dictionary keys | `json.dumps(data, sort_keys=True)` |
| `default` | Handle non-serializable | `json.dumps(data, default=str)` |

### Type Conversion

| Python | JSON |
|--------|------|
| `dict` | `{}` |
| `list`, `tuple` | `[]` |
| `str` | `"string"` |
| `int`, `float` | number |
| `True`/`False` | `true`/`false` |
| `None` | `null` |

### Common Patterns

```python
# Read JSON file
with open("data.json") as f:
    data = json.load(f)

# Write JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Pretty print
print(json.dumps(data, indent=2))
```

---

## Coverage Checklist

- [x] json.loads() and json.dumps()
- [x] json.load() and json.dump()
- [x] Type mapping
- [x] Formatting options
- [x] File operations
- [x] Custom serialization
- [x] Error handling
- [x] Quick reference
