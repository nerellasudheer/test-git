# Python `if __name__ == "__main__"` - Quick Guide

Understanding Python's main module check idiom.

---

## Table of Contents

1. [Overview](#1-overview)
2. [How It Works](#2-how-it-works)
3. [Practical Examples](#3-practical-examples)
4. [Use Cases](#4-use-cases)
5. [Quick Reference](#5-quick-reference)

---

## 1. Overview

### What is `if __name__ == "__main__"`?

This is a standard Python idiom that checks whether a Python file is being run directly as the main program or being imported as a module into another file.

### The `__name__` Variable

`__name__` is a built-in variable automatically created by the Python interpreter:

| How File is Used | Value of `__name__` |
|------------------|---------------------|
| Run directly | `"__main__"` |
| Imported as module | Module name (e.g., `"calculator"`) |

---

## 2. How It Works

### Running Directly

```python
# calculator.py
print(f"__name__ = {__name__}")
```

When running `python calculator.py`:
```
__name__ = __main__
```

### Importing as Module

```python
# main.py
import calculator
```

When running `python main.py`:
```
__name__ = calculator
```

### The Conditional Check

```python
if __name__ == "__main__":
    # This code only runs when the file is executed directly
    # It does NOT run when the file is imported
    pass
```

---

## 3. Practical Examples

### Example 1: Basic Structure

**calculator.py:**
```python
def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

# This block only runs when calculator.py is executed directly
if __name__ == "__main__":
    print("--- Running Calculator Directly ---")

    result_add = add(10, 5)
    print(f"10 + 5 = {result_add}")

    result_sub = subtract(10, 5)
    print(f"10 - 5 = {result_sub}")
```

**Running directly:** `python calculator.py`
```
--- Running Calculator Directly ---
10 + 5 = 15
10 - 5 = 5
```

### Example 2: Importing as Module

**main_app.py:**
```python
import calculator

print("--- Running Main Application ---")

# Call functions from the imported module
result = calculator.add(20, 7)
print(f"20 + 7 = {result}")
```

**Running main_app.py:** `python main_app.py`
```
--- Running Main Application ---
20 + 7 = 27
```

The test code inside `if __name__ == "__main__"` in calculator.py does NOT run.

---

## 4. Use Cases

### Testing Functions

```python
def process_data(data):
    """Process the input data."""
    return data.upper()

if __name__ == "__main__":
    # Test the function
    test_data = "hello world"
    result = process_data(test_data)
    print(f"Test result: {result}")
```

### Running Main Application

```python
def main():
    """Main entry point of the application."""
    print("Application started")
    # Application logic here

if __name__ == "__main__":
    main()
```

### Demo and Examples

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

if __name__ == "__main__":
    # Demo usage
    calc = Calculator()
    print("Demo: 5 + 3 =", calc.add(5, 3))
    print("Demo: 5 * 3 =", calc.multiply(5, 3))
```

---

## 5. Quick Reference

### Summary Table

| Execution Context | `__name__` Value | `if __name__ == "__main__"` | Result |
|-------------------|------------------|----------------------------|--------|
| Running file directly | `"__main__"` | `True` | Code inside block executes |
| Importing file as module | Module name | `False` | Code inside block is skipped |

### Best Practice Template

```python
def some_function():
    """Your function logic."""
    pass

def another_function():
    """Another function."""
    pass

def main():
    """Main entry point."""
    # Your main code here
    pass

if __name__ == "__main__":
    main()
```

### Key Points

1. **Dual Purpose** - File can be both executable and importable
2. **Testing** - Put test code inside the block for quick testing
3. **Clean Imports** - Prevents test code from running on import
4. **Best Practice** - Essential for writing reusable Python modules

---

## Coverage Checklist

- [x] What `__name__` variable is
- [x] How values change based on execution
- [x] Practical examples
- [x] Common use cases
- [x] Quick reference table
