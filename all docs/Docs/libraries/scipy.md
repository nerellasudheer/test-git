# SciPy - Quick Reference

Scientific computing and technical computing in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Statistics](#2-statistics)
3. [Optimization](#3-optimization)
4. [Interpolation](#4-interpolation)
5. [Linear Algebra](#5-linear-algebra)
6. [Signal Processing](#6-signal-processing)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is SciPy?

SciPy is a library for scientific computing that builds on NumPy, providing additional functionality for optimization, statistics, signal processing, and more.

### Installation and Import

```python
# Install
pip install scipy

# Import specific modules
from scipy import stats
from scipy import optimize
from scipy import interpolate
from scipy import linalg
```

### Main Modules

| Module | Description |
|--------|-------------|
| `scipy.stats` | Statistics |
| `scipy.optimize` | Optimization |
| `scipy.interpolate` | Interpolation |
| `scipy.linalg` | Linear algebra |
| `scipy.signal` | Signal processing |
| `scipy.integrate` | Integration |

---

## 2. Statistics

### Descriptive Statistics

```python
from scipy import stats
import numpy as np

data = np.random.randn(100)

# Descriptive stats
print(stats.describe(data))
# nobs, minmax, mean, variance, skewness, kurtosis
```

### Probability Distributions

```python
from scipy import stats

# Normal distribution
normal = stats.norm(loc=0, scale=1)  # mean=0, std=1

# Generate random samples
samples = normal.rvs(size=1000)

# PDF (probability density function)
pdf = normal.pdf(0)  # Value at x=0

# CDF (cumulative distribution function)
cdf = normal.cdf(1.96)  # P(X <= 1.96)

# Percent point function (inverse CDF)
ppf = normal.ppf(0.975)  # Value at 97.5%
```

### Common Distributions

```python
from scipy import stats

# Normal
norm = stats.norm(loc=0, scale=1)

# Uniform
uniform = stats.uniform(loc=0, scale=1)

# Binomial
binom = stats.binom(n=10, p=0.5)

# Poisson
poisson = stats.poisson(mu=5)

# Exponential
expon = stats.expon(scale=1)
```

### Hypothesis Tests

```python
from scipy import stats

# T-test (compare means)
group1 = [1, 2, 3, 4, 5]
group2 = [2, 3, 4, 5, 6]
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Chi-square test
observed = [10, 20, 30]
expected = [15, 20, 25]
chi2, p_value = stats.chisquare(observed, expected)

# Pearson correlation
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
corr, p_value = stats.pearsonr(x, y)
```

---

## 3. Optimization

### Find Minimum

```python
from scipy import optimize
import numpy as np

# Define function
def f(x):
    return x**2 + 10*np.sin(x)

# Find minimum
result = optimize.minimize(f, x0=0)
print(f"Minimum at x = {result.x}")
print(f"Minimum value = {result.fun}")
```

### Root Finding

```python
from scipy import optimize

# Find root of equation
def equation(x):
    return x**3 - 2*x - 5

root = optimize.root(equation, x0=2)
print(f"Root: {root.x}")

# Using brentq (bracketing method)
root = optimize.brentq(equation, 1, 3)
print(f"Root: {root}")
```

### Curve Fitting

```python
from scipy import optimize
import numpy as np

# Data
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([1, 2.7, 7.4, 20.1, 54.6])

# Model function
def model(x, a, b):
    return a * np.exp(b * x)

# Fit
params, covariance = optimize.curve_fit(model, x_data, y_data)
print(f"Parameters: a={params[0]:.2f}, b={params[1]:.2f}")
```

---

## 4. Interpolation

### 1D Interpolation

```python
from scipy import interpolate
import numpy as np

# Known points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Create interpolation function
f = interpolate.interp1d(x, y, kind='linear')

# Interpolate at new points
x_new = np.linspace(0, 4, 10)
y_new = f(x_new)

# Different kinds: 'linear', 'cubic', 'quadratic'
f_cubic = interpolate.interp1d(x, y, kind='cubic')
```

### Spline Interpolation

```python
from scipy import interpolate
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Univariate spline
spline = interpolate.UnivariateSpline(x, y, s=0)
y_spline = spline(np.linspace(0, 4, 100))
```

---

## 5. Linear Algebra

### Matrix Operations

```python
from scipy import linalg
import numpy as np

A = np.array([[1, 2], [3, 4]])

# Determinant
det = linalg.det(A)
print(f"Determinant: {det}")

# Inverse
inv = linalg.inv(A)
print(f"Inverse:\n{inv}")

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = linalg.eig(A)
print(f"Eigenvalues: {eigenvalues}")
```

### Solve Linear System

```python
from scipy import linalg
import numpy as np

# Solve Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

x = linalg.solve(A, b)
print(f"Solution: {x}")  # [2, 3]
```

### Matrix Decomposition

```python
from scipy import linalg
import numpy as np

A = np.array([[1, 2], [3, 4]])

# LU decomposition
P, L, U = linalg.lu(A)

# QR decomposition
Q, R = linalg.qr(A)

# SVD (Singular Value Decomposition)
U, s, Vh = linalg.svd(A)
```

---

## 6. Signal Processing

### Filtering

```python
from scipy import signal
import numpy as np

# Create a noisy signal
t = np.linspace(0, 1, 1000)
clean_signal = np.sin(2 * np.pi * 5 * t)
noisy_signal = clean_signal + 0.5 * np.random.randn(len(t))

# Design a low-pass filter
b, a = signal.butter(4, 0.1)

# Apply filter
filtered_signal = signal.filtfilt(b, a, noisy_signal)
```

### Finding Peaks

```python
from scipy import signal
import numpy as np

x = np.sin(np.linspace(0, 10, 100)) + 0.1 * np.random.randn(100)

# Find peaks
peaks, properties = signal.find_peaks(x, height=0.5)
print(f"Peak indices: {peaks}")
```

---

## 7. Quick Reference

### Statistics (scipy.stats)

| Function | Description |
|----------|-------------|
| `stats.describe()` | Descriptive statistics |
| `stats.norm()` | Normal distribution |
| `stats.ttest_ind()` | Independent t-test |
| `stats.pearsonr()` | Pearson correlation |
| `stats.chisquare()` | Chi-square test |

### Optimization (scipy.optimize)

| Function | Description |
|----------|-------------|
| `optimize.minimize()` | Find minimum |
| `optimize.root()` | Find root |
| `optimize.curve_fit()` | Fit curve to data |
| `optimize.brentq()` | Root in bracket |

### Interpolation (scipy.interpolate)

| Function | Description |
|----------|-------------|
| `interpolate.interp1d()` | 1D interpolation |
| `interpolate.UnivariateSpline()` | Spline fit |

### Linear Algebra (scipy.linalg)

| Function | Description |
|----------|-------------|
| `linalg.det()` | Determinant |
| `linalg.inv()` | Inverse |
| `linalg.eig()` | Eigenvalues |
| `linalg.solve()` | Solve linear system |
| `linalg.svd()` | SVD decomposition |

---

## Coverage Checklist

- [x] Statistics module
- [x] Probability distributions
- [x] Hypothesis tests
- [x] Optimization
- [x] Interpolation
- [x] Linear algebra
- [x] Signal processing basics
- [x] Quick reference
