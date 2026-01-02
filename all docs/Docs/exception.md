# Python Exception Handling - Complete Guide

A comprehensive reference for handling errors and exceptions gracefully in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Try-Except Block](#2-try-except-block)
3. [Else and Finally Clauses](#3-else-and-finally-clauses)
4. [Common Built-in Exceptions](#4-common-built-in-exceptions)
5. [Raising Exceptions](#5-raising-exceptions)
6. [Custom Exceptions](#6-custom-exceptions)
7. [Error Types](#7-error-types)
8. [Best Practices](#8-best-practices)
9. [Quick Reference](#9-quick-reference)

---

## 1. Overview

### What is Exception Handling?

Exception handling is a mechanism to manage runtime errors gracefully, preventing program crashes. When an error occurs, Python raises an exception object. If not handled, the program terminates abruptly.

### Why Use Exception Handling?

| Benefit | Description |
|---------|-------------|
| Prevents crashes | Program continues running after handling errors |
| User-friendly | Provides meaningful error messages |
| Separation of concerns | Keeps error handling separate from main logic |
| Debugging | Makes it easier to catch and log specific errors |
| Resource cleanup | Ensures proper cleanup even when errors occur |

### Basic Syntax

```python
try:
    # Code that might raise an exception
    risky_operation()
except ExceptionType:
    # Code to handle the exception
    handle_error()
```

---

## 2. Try-Except Block

### Simple Try-Except

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")
```

### Multiple Except Blocks

Handle different exceptions separately:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
    number = int(content)
except FileNotFoundError:
    print("File does not exist")
except ValueError:
    print("File content is not a valid number")
except PermissionError:
    print("No permission to read the file")
```

### Catching Multiple Exceptions Together

```python
try:
    result = 10 / int(input("Enter divisor: "))
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
```

### Getting Exception Details

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    # Output: Error occurred: division by zero

# Generic exception catching
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {type(e).__name__}")
    print(f"Error message: {str(e)}")
```

---

## 3. Else and Finally Clauses

### The else Clause

Executes only if no exception occurs in the try block:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
else:
    print(f"Successfully converted: {number}")
    # This runs only if no exception occurred
```

### The finally Clause

Always executes, whether exception occurs or not. Used for cleanup:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always closes the file
    print("Cleanup completed")
```

### Complete Example with All Components

```python
try:
    file = open("numbers.txt", "r")
    data = file.read()
    result = 100 / int(data)
except FileNotFoundError:
    print("File does not exist")
except ValueError:
    print("File contains invalid data")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")
finally:
    try:
        file.close()
        print("File closed successfully")
    except:
        print("File was never opened")
```

---

## 4. Common Built-in Exceptions

### ValueError

Raised when operation receives wrong type of value:

```python
try:
    number = int("abc")
except ValueError:
    print("Cannot convert string to integer")
```

### TypeError

Raised when operation is applied to wrong type:

```python
try:
    result = "5" + 5
except TypeError:
    print("Cannot add string and integer")
```

### KeyError

Raised when dictionary key is not found:

```python
try:
    person = {"name": "John"}
    age = person["age"]
except KeyError:
    print("Key does not exist in dictionary")
```

### IndexError

Raised when sequence index is out of range:

```python
try:
    numbers = [1, 2, 3]
    value = numbers[5]
except IndexError:
    print("Index out of range")
```

### FileNotFoundError

Raised when file operation fails:

```python
try:
    with open("nonexistent.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist")
```

### ZeroDivisionError

Raised when dividing by zero:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### AttributeError

Raised when attribute reference fails:

```python
try:
    number = 5
    number.append(10)
except AttributeError:
    print("Object has no such attribute")
```

---

## 5. Raising Exceptions

### Using raise

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems invalid")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")
```

### Re-raising Exceptions

```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Logging error...")
    raise  # Re-raises the same exception
```

### Raise from Another Exception

```python
try:
    data = fetch_data()
except ConnectionError as e:
    raise RuntimeError("Failed to fetch data") from e
```

---

## 6. Custom Exceptions

### Creating Custom Exceptions

```python
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds")
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
```

### Custom Exception with Details

```python
class InvalidAgeError(Exception):
    """Raised when age is invalid"""
    def __init__(self, age, message="Invalid age provided"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age, f"Invalid age: {age}")
    return age

try:
    set_age(-5)
except InvalidAgeError as e:
    print(e)
```

---

## 7. Error Types

### Error Types Summary

| Error Type | When It Occurs | Detection Time |
|------------|----------------|----------------|
| Syntax Error | Invalid Python grammar | Before execution |
| Runtime Error | During execution | During execution |
| Logical Error | Wrong program logic | After execution (wrong output) |
| Name Error | Undefined variable/function | During execution |
| Type Error | Incompatible data types | During execution |
| Value Error | Wrong value for operation | During execution |

### Syntax Errors

Mistakes in code structure detected before execution:

```python
# Missing colon - SyntaxError
if x > 5
    print("Greater")

# Fix:
if x > 5:
    print("Greater")
```

### Logical Errors

Code runs but produces incorrect results:

```python
# Logical Error - Wrong operator
def calculate_area(length, width):
    return length + width  # Should be length * width

# Fix with debugging and testing
def calculate_area(length, width):
    result = length * width
    assert result > 0, "Area must be positive"
    return result
```

---

## 8. Best Practices

### 1. Be Specific

Catch specific exceptions rather than generic Exception:

```python
# Bad: Catching everything
try:
    risky_code()
except:
    pass

# Good: Catch specific exceptions
try:
    risky_code()
except ValueError:
    handle_value_error()
except TypeError:
    handle_type_error()
```

### 2. Use Context Managers

Automatically handles resource cleanup:

```python
# Automatically closes file, even if error occurs
with open('data.txt', 'r') as file:
    data = file.read()
```

### 3. Don't Hide Errors

Avoid empty except blocks:

```python
# Bad
try:
    risky_code()
except:
    pass  # Silently ignoring all errors

# Good
try:
    risky_code()
except ValueError as e:
    logging.error(f"Value error: {e}")
    raise  # Re-raise after logging
```

### 4. Validate Input

Prevent errors before they occur:

```python
def get_valid_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if 0 <= age <= 150:
                return age
            else:
                print("Age must be between 0 and 150")
        except ValueError:
            print("Please enter a valid number")
```

### 5. Log Exceptions

Record errors for debugging:

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    risky_operation()
except Exception as e:
    logging.error(f"Error occurred: {e}", exc_info=True)
```

---

## 9. Quick Reference

### Exception Handling Structure

```python
try:
    # Code that might raise an exception
except ExceptionType as e:
    # Handle specific exception
except AnotherType:
    # Handle another exception
else:
    # Runs if no exception occurred
finally:
    # Always runs (cleanup)
```

### Common Exceptions

| Exception | Cause |
|-----------|-------|
| `ValueError` | Invalid value for operation |
| `TypeError` | Wrong data type |
| `KeyError` | Dictionary key not found |
| `IndexError` | Index out of range |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Attribute doesn't exist |
| `NameError` | Variable not defined |
| `ImportError` | Module import failed |

### Keywords

| Keyword | Purpose |
|---------|---------|
| `try` | Start exception handling block |
| `except` | Catch and handle exceptions |
| `else` | Run if no exception occurred |
| `finally` | Always run (cleanup) |
| `raise` | Trigger an exception |
| `as` | Bind exception to variable |

### Error Handling Priority

1. **Prevent** - Write defensive code with validation
2. **Detect** - Use linters, type checkers, tests
3. **Handle** - Use appropriate try-except blocks
4. **Log** - Record errors for debugging
5. **Recover** - Provide fallback options when possible

---

## Coverage Checklist

- [x] Try-except block basics
- [x] Multiple exception handling
- [x] Else and finally clauses
- [x] Common built-in exceptions
- [x] Raising and re-raising exceptions
- [x] Custom exceptions
- [x] Error types overview
- [x] Best practices
- [x] Quick reference tables
