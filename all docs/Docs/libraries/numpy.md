# NumPy - Quick Reference

Numerical computing with arrays in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Creating Arrays](#2-creating-arrays)
3. [Array Operations](#3-array-operations)
4. [Indexing and Slicing](#4-indexing-and-slicing)
5. [Array Manipulation](#5-array-manipulation)
6. [Mathematical Functions](#6-mathematical-functions)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is NumPy?

NumPy (Numerical Python) is the fundamental package for scientific computing. It provides fast array operations and mathematical functions.

### Installation and Import

```python
# Install
pip install numpy

# Import
import numpy as np
```

### Why NumPy?

| Feature | Benefit |
|---------|---------|
| Fast arrays | 50x faster than Python lists |
| Broadcasting | Operations on different shapes |
| Vectorization | No explicit loops needed |
| Math functions | Built-in statistics, linear algebra |

---

## 2. Creating Arrays

### Basic Array Creation

```python
import numpy as np

# From list
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]

# 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# [[1 2 3]
#  [4 5 6]]

# Data type specification
arr_float = np.array([1, 2, 3], dtype=float)
```

### Special Arrays

```python
# Zeros
zeros = np.zeros((3, 4))  # 3x4 matrix of zeros

# Ones
ones = np.ones((2, 3))    # 2x3 matrix of ones

# Identity matrix
identity = np.eye(3)      # 3x3 identity matrix

# Range
arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Linspace (evenly spaced)
arr = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

# Random
rand = np.random.rand(3, 3)      # Uniform [0, 1)
randn = np.random.randn(3, 3)    # Normal distribution
randint = np.random.randint(0, 10, (3, 3))  # Random integers
```

### Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)     # (2, 3) - dimensions
print(arr.ndim)      # 2 - number of dimensions
print(arr.size)      # 6 - total elements
print(arr.dtype)     # int64 - data type
```

---

## 3. Array Operations

### Arithmetic Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)    # [5, 7, 9]
print(a - b)    # [-3, -3, -3]
print(a * b)    # [4, 10, 18]
print(a / b)    # [0.25, 0.4, 0.5]
print(a ** 2)   # [1, 4, 9]
```

### Broadcasting

```python
# Scalar with array
arr = np.array([1, 2, 3])
print(arr + 10)   # [11, 12, 13]
print(arr * 2)    # [2, 4, 6]

# Different shapes
a = np.array([[1, 2, 3]])       # Shape (1, 3)
b = np.array([[1], [2], [3]])   # Shape (3, 1)
print(a + b)
# [[2, 3, 4],
#  [3, 4, 5],
#  [4, 5, 6]]
```

### Comparison Operations

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr > 3)        # [False, False, False, True, True]
print(arr == 3)       # [False, False, True, False, False]
print(arr[arr > 3])   # [4, 5] - Boolean indexing
```

---

## 4. Indexing and Slicing

### 1D Array

```python
arr = np.array([0, 1, 2, 3, 4, 5])

print(arr[0])      # 0
print(arr[-1])     # 5
print(arr[1:4])    # [1, 2, 3]
print(arr[::2])    # [0, 2, 4]
```

### 2D Array

```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix[0, 0])     # 1 (first element)
print(matrix[1, 2])     # 6 (row 1, col 2)
print(matrix[0])        # [1, 2, 3] (first row)
print(matrix[:, 0])     # [1, 4, 7] (first column)
print(matrix[0:2, 1:3]) # Submatrix
```

### Fancy Indexing

```python
arr = np.array([10, 20, 30, 40, 50])

# Index with array
indices = np.array([0, 2, 4])
print(arr[indices])  # [10, 30, 50]

# Boolean indexing
mask = arr > 25
print(arr[mask])     # [30, 40, 50]
```

---

## 5. Array Manipulation

### Reshaping

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to 2x3
reshaped = arr.reshape(2, 3)
print(reshaped)
# [[1, 2, 3],
#  [4, 5, 6]]

# Flatten to 1D
flat = reshaped.flatten()
print(flat)  # [1, 2, 3, 4, 5, 6]

# Transpose
transposed = reshaped.T
print(transposed)
# [[1, 4],
#  [2, 5],
#  [3, 6]]
```

### Concatenation

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concatenate
print(np.concatenate([a, b]))  # [1, 2, 3, 4, 5, 6]

# Stack vertically
print(np.vstack([a, b]))
# [[1, 2, 3],
#  [4, 5, 6]]

# Stack horizontally
print(np.hstack([a, b]))  # [1, 2, 3, 4, 5, 6]
```

### Splitting

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Split into 3 parts
parts = np.split(arr, 3)
print(parts)  # [array([1, 2]), array([3, 4]), array([5, 6])]
```

---

## 6. Mathematical Functions

### Basic Statistics

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))      # 15
print(np.mean(arr))     # 3.0
print(np.std(arr))      # 1.414...
print(np.min(arr))      # 1
print(np.max(arr))      # 5
print(np.argmin(arr))   # 0 (index of min)
print(np.argmax(arr))   # 4 (index of max)
```

### Math Functions

```python
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))     # [1, 2, 3, 4]
print(np.exp(arr))      # Exponential
print(np.log(arr))      # Natural log
print(np.sin(arr))      # Sine
print(np.abs([-1, -2])) # [1, 2]
```

### Axis Operations

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(matrix))           # 21 (total)
print(np.sum(matrix, axis=0))   # [5, 7, 9] (column sums)
print(np.sum(matrix, axis=1))   # [6, 15] (row sums)
```

---

## 7. Quick Reference

### Array Creation

| Function | Description |
|----------|-------------|
| `np.array(list)` | Create from list |
| `np.zeros(shape)` | Array of zeros |
| `np.ones(shape)` | Array of ones |
| `np.arange(start, stop, step)` | Range array |
| `np.linspace(start, stop, n)` | Evenly spaced |
| `np.random.rand(shape)` | Random [0,1) |

### Array Attributes

| Attribute | Description |
|-----------|-------------|
| `.shape` | Dimensions |
| `.ndim` | Number of dimensions |
| `.size` | Total elements |
| `.dtype` | Data type |

### Common Operations

| Operation | Description |
|-----------|-------------|
| `+`, `-`, `*`, `/` | Element-wise |
| `@` or `np.dot()` | Matrix multiplication |
| `.T` | Transpose |
| `.reshape()` | Change shape |
| `.flatten()` | To 1D |

### Statistics

| Function | Description |
|----------|-------------|
| `np.sum()` | Sum |
| `np.mean()` | Average |
| `np.std()` | Standard deviation |
| `np.min()`, `np.max()` | Min/Max |
| `np.argmin()`, `np.argmax()` | Index of min/max |

---

## Coverage Checklist

- [x] Array creation methods
- [x] Arithmetic operations
- [x] Broadcasting
- [x] Indexing and slicing
- [x] Reshaping and manipulation
- [x] Mathematical functions
- [x] Statistics
- [x] Quick reference
