# Python While Loops - Complete Guide

Execute code repeatedly while a condition is true.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic While Loop](#2-basic-while-loop)
3. [Loop Control](#3-loop-control)
4. [Common Patterns](#4-common-patterns)
5. [While with else](#5-while-with-else)
6. [Infinite Loops](#6-infinite-loops)
7. [While vs For](#7-while-vs-for)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What is a While Loop?

A while loop executes code repeatedly as long as a condition is True.

### Basic Syntax

```python
while condition:
    # code to execute
    # update condition to avoid infinite loop
```

### Key Points

| Aspect | Description |
|--------|-------------|
| Condition | Checked before each iteration |
| Body | Executes while condition is True |
| Exit | When condition becomes False |
| Danger | Can run forever if condition never False |

---

## 2. Basic While Loop

### Simple Counter

```python
count = 0

while count < 5:
    print(count)
    count += 1  # Important: update the condition!

# Output: 0, 1, 2, 3, 4
```

### Countdown

```python
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast off!")

# Output: 5, 4, 3, 2, 1, Blast off!
```

### User Input Loop

```python
user_input = ""

while user_input != "quit":
    user_input = input("Enter command (quit to exit): ")
    print(f"You entered: {user_input}")

print("Goodbye!")
```

---

## 3. Loop Control

### break - Exit Loop

```python
# Exit when condition met
count = 0

while True:  # Infinite loop
    print(count)
    count += 1
    if count >= 5:
        break  # Exit the loop

# Output: 0, 1, 2, 3, 4
```

### continue - Skip Iteration

```python
# Skip even numbers
count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip to next iteration
    print(count)

# Output: 1, 3, 5, 7, 9
```

### pass - Placeholder

```python
count = 0

while count < 5:
    if count == 3:
        pass  # TODO: handle this case
    print(count)
    count += 1
```

---

## 4. Common Patterns

### Input Validation

```python
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 120:
            break
        print("Age must be between 0 and 120")
    except ValueError:
        print("Please enter a valid number")

print(f"Your age is {age}")
```

### Menu System

```python
while True:
    print("\n--- Menu ---")
    print("1. Option A")
    print("2. Option B")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("You selected Option A")
    elif choice == "2":
        print("You selected Option B")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
```

### Processing Until Done

```python
items = ["apple", "banana", "cherry"]

while items:  # While list is not empty
    item = items.pop()
    print(f"Processing: {item}")

# Output: Processing: cherry, banana, apple
```

### Accumulator Pattern

```python
total = 0

while True:
    num = input("Enter a number (or 'done'): ")
    if num == "done":
        break
    total += int(num)

print(f"Total: {total}")
```

### Waiting for Condition

```python
import time

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    # Simulate checking for something
    if check_condition():  # Your condition
        print("Condition met!")
        break
    attempts += 1
    print(f"Attempt {attempts} failed, retrying...")
    time.sleep(1)
else:
    print("Max attempts reached")
```

---

## 5. While with else

### Syntax

The `else` block executes if the loop completes normally (no `break`).

```python
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed normally")

# Output: 0, 1, 2, 3, 4, Loop completed normally
```

### With break (else Skipped)

```python
count = 0

while count < 5:
    print(count)
    if count == 3:
        break
    count += 1
else:
    print("This won't print")

# Output: 0, 1, 2, 3
```

### Practical Example: Search

```python
numbers = [1, 3, 5, 7, 9]
target = 4
index = 0

while index < len(numbers):
    if numbers[index] == target:
        print(f"Found at index {index}")
        break
    index += 1
else:
    print(f"{target} not found")

# Output: 4 not found
```

---

## 6. Infinite Loops

### Intentional Infinite Loops

```python
# Server-like loop
while True:
    request = get_request()
    if request == "shutdown":
        break
    process(request)
```

### Accidental Infinite Loops (Avoid!)

```python
# BUG: Forgot to increment
count = 0
while count < 5:
    print(count)
    # count += 1  # Missing! Loop runs forever

# BUG: Condition never False
x = 10
while x > 0:
    print(x)
    x += 1  # Wrong! Should be x -= 1
```

### Preventing Infinite Loops

```python
# Use a safety counter
max_iterations = 1000
count = 0

while some_condition and count < max_iterations:
    # Your code
    count += 1

if count >= max_iterations:
    print("Warning: Max iterations reached")
```

---

## 7. While vs For

### When to Use While

| Use While When... | Example |
|-------------------|---------|
| Unknown iterations | User input until valid |
| Condition-based exit | Wait for event |
| Need manual control | Custom stepping |
| Reading until EOF | File processing |

### When to Use For

| Use For When... | Example |
|-----------------|---------|
| Known iterations | Loop n times |
| Iterating sequence | List, string, dict |
| Simple counting | `range(10)` |
| Cleaner syntax | Most cases |

### Conversion Examples

```python
# FOR to WHILE
# For loop
for i in range(5):
    print(i)

# Equivalent while loop
i = 0
while i < 5:
    print(i)
    i += 1

# WHILE to FOR (when possible)
# While loop
items = [1, 2, 3]
i = 0
while i < len(items):
    print(items[i])
    i += 1

# Better as for loop
for item in items:
    print(item)
```

---

## 8. Quick Reference

### Basic Syntax

```python
# Simple while
while condition:
    code

# While with else
while condition:
    code
else:
    runs_if_no_break

# Infinite loop with break
while True:
    if exit_condition:
        break
```

### Loop Control

| Statement | Effect |
|-----------|--------|
| `break` | Exit loop immediately |
| `continue` | Skip to next iteration |
| `pass` | Do nothing |
| `else` | Runs if no break |

### Common Patterns

| Pattern | Use Case |
|---------|----------|
| `while True: ... break` | Exit from middle |
| `while items:` | Until empty |
| `while condition:` | Until condition false |
| `while True: try/except` | Input validation |

### Safety Tips

| Tip | Why |
|-----|-----|
| Always update loop variable | Prevent infinite loop |
| Consider max iterations | Safety limit |
| Use for loop if possible | Cleaner, safer |
| Test edge cases | Empty lists, 0, etc. |

### Examples Summary

```python
# Counter
count = 0
while count < n:
    ...
    count += 1

# Input validation
while True:
    inp = input(...)
    if valid(inp):
        break

# Process until empty
while items:
    item = items.pop()
    process(item)

# Retry pattern
attempts = 0
while attempts < max_attempts:
    if success():
        break
    attempts += 1
```

---

## Coverage Checklist

- [x] Basic while loop syntax
- [x] Loop control (break, continue, pass)
- [x] Common patterns (input, menu, accumulator)
- [x] While with else clause
- [x] Infinite loops (intentional and accidental)
- [x] While vs For comparison
- [x] Safety tips
- [x] Quick reference tables
