# Python string Module - Quick Reference

A guide to string constants, templates, and the join() method in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [String Constants](#2-string-constants)
3. [String Template](#3-string-template)
4. [The join() Method](#4-the-join-method)
5. [Practical Examples](#5-practical-examples)
6. [Quick Reference](#6-quick-reference)

---

## 1. Overview

### What is the string Module?

The `string` module provides useful string constants (predefined character sets) and the `Template` class for simple string substitution.

### Import

```python
import string
```

### Module Components

| Component | Purpose |
|-----------|---------|
| String constants | Predefined character sets (letters, digits, etc.) |
| `Template` class | Simple string substitution with `$placeholders` |
| `Formatter` class | Advanced custom formatting (rarely used) |

**Note:** Most string manipulation is done with built-in `str` methods (`.upper()`, `.split()`, etc.), not the `string` module.

---

## 2. String Constants

### Available Constants

| Constant | Value | Description |
|----------|-------|-------------|
| `string.ascii_lowercase` | `'abcdefghijklmnopqrstuvwxyz'` | Lowercase letters |
| `string.ascii_uppercase` | `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'` | Uppercase letters |
| `string.ascii_letters` | lowercase + uppercase | All letters |
| `string.digits` | `'0123456789'` | Decimal digits |
| `string.hexdigits` | `'0123456789abcdefABCDEF'` | Hexadecimal digits |
| `string.octdigits` | `'01234567'` | Octal digits |
| `string.punctuation` | `'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'` | Punctuation |
| `string.whitespace` | `' \t\n\r\v\f'` | Whitespace characters |
| `string.printable` | All printable characters | Letters + digits + punctuation + whitespace |

### Usage Examples

```python
import string

# View the constants
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.digits)           # 0123456789
print(string.punctuation)      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Character Validation

```python
import string

char = 'A'

if char in string.ascii_letters:
    print(f"'{char}' is a letter")
elif char in string.digits:
    print(f"'{char}' is a digit")
elif char in string.punctuation:
    print(f"'{char}' is punctuation")

# Output: 'A' is a letter
```

### Combining Constants

```python
import string

# All alphanumeric characters
alphanumeric = string.ascii_letters + string.digits
print(alphanumeric)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

# Password-safe characters
password_chars = string.ascii_letters + string.digits + "!@#$%"
```

---

## 3. String Template

### What is Template?

`string.Template` provides simple string substitution using `$placeholder` syntax. It's safer than `%` formatting or `.format()` when substitution values come from users.

### Basic Syntax

```python
from string import Template

# Create template with $placeholders
t = Template('Hello, $name!')

# Substitute values
result = t.substitute(name='Alice')
print(result)  # Hello, Alice!
```

### substitute() vs safe_substitute()

| Method | Missing Key Behavior |
|--------|---------------------|
| `substitute()` | Raises `KeyError` |
| `safe_substitute()` | Leaves placeholder as-is |

```python
from string import Template

t = Template('Hello, $name! Your project is $project.')

# substitute() - raises error if key missing
try:
    result = t.substitute(name='Bob')
except KeyError as e:
    print(f"Missing key: {e}")  # Missing key: 'project'

# safe_substitute() - keeps placeholder if missing
result = t.safe_substitute(name='Bob')
print(result)  # Hello, Bob! Your project is $project.
```

### Template Syntax

| Syntax | Meaning |
|--------|---------|
| `$name` | Simple placeholder |
| `${name}` | Placeholder with braces (for adjacent text) |
| `$$` | Literal dollar sign |

```python
from string import Template

# Using ${} for adjacent text
t = Template('${item}s cost $$${price} each')
result = t.substitute(item='Apple', price='2')
print(result)  # Apples cost $2 each

# Note: $$ becomes a single $
```

### Using Dictionary

```python
from string import Template

t = Template('$product: $price')
data = {'product': 'Laptop', 'price': '$999'}

result = t.substitute(data)
print(result)  # Laptop: $999
```

---

## 4. The join() Method

### What is join()?

`join()` is a **string method** (not from the string module) that concatenates elements of an iterable into a single string, using the string as a separator.

### Syntax

```python
separator.join(iterable)
```

### Basic Examples

```python
# Join with empty string (no separator)
letters = ['H', 'e', 'l', 'l', 'o']
result = ''.join(letters)
print(result)  # Hello

# Join with space
words = ['Python', 'is', 'awesome']
result = ' '.join(words)
print(result)  # Python is awesome

# Join with comma
fruits = ['apple', 'banana', 'cherry']
result = ', '.join(fruits)
print(result)  # apple, banana, cherry

# Join with hyphen
date_parts = ['2024', '12', '06']
result = '-'.join(date_parts)
print(result)  # 2024-12-06

# Join with newline
lines = ['Line 1', 'Line 2', 'Line 3']
result = '\n'.join(lines)
print(result)
# Line 1
# Line 2
# Line 3
```

### Key Points About join()

| Point | Description |
|-------|-------------|
| Separator | The string before `.join()` goes between items |
| Empty string | `''.join()` concatenates with no separator |
| Only strings | Iterable must contain only strings |
| Efficient | Faster than `+` for multiple concatenations |

### Converting Non-Strings

```python
# WRONG - join requires strings
numbers = [1, 2, 3]
# result = '-'.join(numbers)  # TypeError!

# CORRECT - convert to strings first
result = '-'.join(str(n) for n in numbers)
print(result)  # 1-2-3

# Or use map()
result = '-'.join(map(str, numbers))
print(result)  # 1-2-3
```

---

## 5. Practical Examples

### Password Generator

```python
import string
import random

def generate_password(length=12):
    # Combine character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choices(characters, k=length))
    return password

print(generate_password())    # e.g., aB3$xY9@mNpQ
print(generate_password(16))  # 16-character password
```

### Secure Password (At Least One of Each Type)

```python
import string
import random

def secure_password(length=12):
    if length < 4:
        raise ValueError("Password must be at least 4 characters")

    # Ensure at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill rest with random characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to randomize positions
    random.shuffle(password)

    return ''.join(password)

print(secure_password())  # Guaranteed variety
```

### Input Validation

```python
import string

def is_valid_username(username):
    """Username: letters, digits, underscore only."""
    valid_chars = string.ascii_letters + string.digits + '_'
    return all(char in valid_chars for char in username)

def is_alphanumeric(text):
    """Check if text contains only letters and digits."""
    valid_chars = string.ascii_letters + string.digits
    return all(char in valid_chars for char in text)

print(is_valid_username("john_doe123"))  # True
print(is_valid_username("john@doe"))     # False
print(is_alphanumeric("Hello123"))       # True
print(is_alphanumeric("Hello 123"))      # False (space)
```

### Remove Punctuation

```python
import string

text = "Hello, World! How are you?"

# Remove all punctuation
clean = ''.join(char for char in text if char not in string.punctuation)
print(clean)  # Hello World How are you

# Using str.translate() (faster for large strings)
translator = str.maketrans('', '', string.punctuation)
clean = text.translate(translator)
print(clean)  # Hello World How are you
```

### Email Template

```python
from string import Template

email_template = Template("""
Dear $name,

Thank you for your order #$order_id.
Your total is $$${total}.

Best regards,
$company
""")

email = email_template.substitute(
    name='Alice',
    order_id='12345',
    total='99.99',
    company='TechStore'
)

print(email)
```

### Building Paths

```python
# Join path components
parts = ['home', 'user', 'documents', 'file.txt']
path = '/'.join(parts)
print(path)  # home/user/documents/file.txt

# For real file paths, use pathlib or os.path instead
```

### CSV Line Builder

```python
def to_csv_line(values):
    """Convert list of values to CSV line."""
    return ','.join(str(v) for v in values)

data = ['John', 25, 'New York', 50000]
csv_line = to_csv_line(data)
print(csv_line)  # John,25,New York,50000
```

---

## 6. Quick Reference

### String Constants

| Constant | Contains |
|----------|----------|
| `string.ascii_lowercase` | a-z |
| `string.ascii_uppercase` | A-Z |
| `string.ascii_letters` | a-z + A-Z |
| `string.digits` | 0-9 |
| `string.punctuation` | !"#$%&... |
| `string.whitespace` | space, tab, newline... |

### Template Syntax

| Pattern | Meaning |
|---------|---------|
| `$name` | Placeholder |
| `${name}` | Placeholder (explicit) |
| `$$` | Literal $ |
| `.substitute(dict)` | Requires all keys |
| `.safe_substitute(dict)` | Keeps missing placeholders |

### join() Patterns

| Code | Result |
|------|--------|
| `''.join(['a','b','c'])` | `'abc'` |
| `' '.join(['a','b','c'])` | `'a b c'` |
| `','.join(['a','b','c'])` | `'a,b,c'` |
| `'\n'.join(['a','b','c'])` | `'a\nb\nc'` |

### Key Points

1. **String constants** are for character sets, not manipulation
2. **Template** is safer for user-provided values
3. **join()** is a `str` method, not in `string` module
4. **join()** requires all elements to be strings
5. Use **built-in str methods** for most string operations

---

## Coverage Checklist

- [x] String constants overview
- [x] Template class with substitute/safe_substitute
- [x] join() method explained
- [x] Practical examples
- [x] Quick reference tables
