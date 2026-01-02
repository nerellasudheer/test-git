# Matplotlib - Quick Reference

Data visualization and plotting in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic Plots](#2-basic-plots)
3. [Plot Customization](#3-plot-customization)
4. [Multiple Plots](#4-multiple-plots)
5. [Common Plot Types](#5-common-plot-types)
6. [Saving Figures](#6-saving-figures)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is Matplotlib?

Matplotlib is Python's primary plotting library for creating static, animated, and interactive visualizations.

### Installation and Import

```python
# Install
pip install matplotlib

# Import (standard convention)
import matplotlib.pyplot as plt
```

### Basic Workflow

```python
import matplotlib.pyplot as plt

# 1. Create data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create plot
plt.plot(x, y)

# 3. Customize (optional)
plt.title("My Plot")

# 4. Display
plt.show()
```

---

## 2. Basic Plots

### Line Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
```

### Scatter Plot

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()
```

### Bar Chart

```python
categories = ["A", "B", "C", "D"]
values = [25, 40, 30, 55]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()

# Horizontal bars
plt.barh(categories, values)
```

### Histogram

```python
import numpy as np

data = np.random.randn(1000)  # Random data

plt.hist(data, bins=30)
plt.title("Histogram")
plt.show()
```

### Pie Chart

```python
sizes = [30, 25, 20, 15, 10]
labels = ["A", "B", "C", "D", "E"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()
```

---

## 3. Plot Customization

### Colors and Styles

```python
# Line styles and colors
plt.plot(x, y, color="red", linestyle="--", linewidth=2)
plt.plot(x, y2, "b-.")  # Blue dash-dot (shorthand)

# Markers
plt.plot(x, y, marker="o", markersize=10)
plt.scatter(x, y, c="green", s=100, alpha=0.5)
```

### Style Shortcuts

| Character | Meaning |
|-----------|---------|
| `-` | Solid line |
| `--` | Dashed line |
| `-.` | Dash-dot line |
| `:` | Dotted line |
| `o` | Circle marker |
| `s` | Square marker |
| `^` | Triangle marker |
| `*` | Star marker |

### Colors

| Character | Color |
|-----------|-------|
| `b` | Blue |
| `g` | Green |
| `r` | Red |
| `c` | Cyan |
| `m` | Magenta |
| `y` | Yellow |
| `k` | Black |
| `w` | White |

### Labels and Titles

```python
plt.title("Main Title", fontsize=16)
plt.xlabel("X Label", fontsize=12)
plt.ylabel("Y Label", fontsize=12)
plt.legend(["Series 1", "Series 2"])
```

### Grid and Limits

```python
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(0, 100)
```

---

## 4. Multiple Plots

### Multiple Lines

```python
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label="Squared")
plt.plot(x, y2, label="Linear")
plt.legend()
plt.show()
```

### Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Access each subplot
axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Plot 1")

axes[0, 1].bar(categories, values)
axes[0, 1].set_title("Plot 2")

axes[1, 0].scatter(x, y)
axes[1, 0].set_title("Plot 3")

axes[1, 1].hist(data)
axes[1, 1].set_title("Plot 4")

plt.tight_layout()
plt.show()
```

### Simple Subplots

```python
# 2 rows, 1 column
plt.subplot(2, 1, 1)  # First plot
plt.plot(x, y1)

plt.subplot(2, 1, 2)  # Second plot
plt.plot(x, y2)

plt.show()
```

---

## 5. Common Plot Types

### Box Plot

```python
data = [np.random.randn(100) for _ in range(4)]
plt.boxplot(data, labels=["A", "B", "C", "D"])
plt.title("Box Plot")
plt.show()
```

### Error Bars

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
error = [0.5, 0.8, 0.3, 0.6, 0.4]

plt.errorbar(x, y, yerr=error, fmt="o-", capsize=5)
plt.show()
```

### Heatmap

```python
import numpy as np

data = np.random.rand(10, 10)
plt.imshow(data, cmap="hot")
plt.colorbar()
plt.title("Heatmap")
plt.show()
```

### Fill Between

```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.sin(x) + 1

plt.fill_between(x, y1, y2, alpha=0.3)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
```

---

## 6. Saving Figures

### Save to File

```python
plt.plot(x, y)
plt.title("My Plot")

# Save as PNG
plt.savefig("my_plot.png", dpi=300)

# Save as PDF
plt.savefig("my_plot.pdf")

# Save with tight boundaries
plt.savefig("my_plot.png", bbox_inches="tight")

plt.show()
```

### Figure Size

```python
# Set size before plotting
plt.figure(figsize=(12, 6))  # Width, Height in inches
plt.plot(x, y)
plt.show()
```

---

## 7. Quick Reference

### Basic Functions

| Function | Description |
|----------|-------------|
| `plt.plot(x, y)` | Line plot |
| `plt.scatter(x, y)` | Scatter plot |
| `plt.bar(x, y)` | Bar chart |
| `plt.hist(data)` | Histogram |
| `plt.pie(sizes)` | Pie chart |
| `plt.boxplot(data)` | Box plot |

### Customization

| Function | Description |
|----------|-------------|
| `plt.title()` | Set title |
| `plt.xlabel()` | X-axis label |
| `plt.ylabel()` | Y-axis label |
| `plt.legend()` | Add legend |
| `plt.grid()` | Toggle grid |
| `plt.xlim()` | X-axis limits |
| `plt.ylim()` | Y-axis limits |

### Multiple Plots

| Function | Description |
|----------|-------------|
| `plt.subplot(r, c, n)` | Create subplot |
| `plt.subplots(r, c)` | Create figure with subplots |
| `plt.tight_layout()` | Adjust spacing |

### Output

| Function | Description |
|----------|-------------|
| `plt.show()` | Display plot |
| `plt.savefig()` | Save to file |
| `plt.figure(figsize=)` | Set figure size |

### Common Options

| Option | Example |
|--------|---------|
| Color | `color="red"` or `c="r"` |
| Line style | `linestyle="--"` |
| Line width | `linewidth=2` |
| Marker | `marker="o"` |
| Transparency | `alpha=0.5` |
| Label | `label="Series 1"` |

---

## Coverage Checklist

- [x] Basic plot types
- [x] Customization (colors, styles, labels)
- [x] Multiple plots and subplots
- [x] Common plot types
- [x] Saving figures
- [x] Quick reference
