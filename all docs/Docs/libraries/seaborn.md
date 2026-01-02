# Seaborn - Quick Reference

Statistical data visualization built on matplotlib.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Distribution Plots](#2-distribution-plots)
3. [Categorical Plots](#3-categorical-plots)
4. [Relational Plots](#4-relational-plots)
5. [Matrix Plots](#5-matrix-plots)
6. [Styling](#6-styling)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is Seaborn?

Seaborn is a statistical visualization library that provides a high-level interface for drawing attractive and informative statistical graphics.

### Installation and Import

```python
# Install
pip install seaborn

# Import
import seaborn as sns
import matplotlib.pyplot as plt
```

### Built-in Datasets

```python
# Load example datasets
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
```

---

## 2. Distribution Plots

### Histogram with KDE

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Histogram
sns.histplot(data=tips, x="total_bill")
plt.show()

# With KDE (kernel density estimation)
sns.histplot(data=tips, x="total_bill", kde=True)
plt.show()
```

### KDE Plot

```python
sns.kdeplot(data=tips, x="total_bill")
plt.show()

# Multiple distributions
sns.kdeplot(data=tips, x="total_bill", hue="time")
plt.show()
```

### Box Plot

```python
sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()

# With hue
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.show()
```

### Violin Plot

```python
sns.violinplot(data=tips, x="day", y="total_bill")
plt.show()
```

---

## 3. Categorical Plots

### Count Plot

```python
# Count occurrences
sns.countplot(data=tips, x="day")
plt.show()

# With hue
sns.countplot(data=tips, x="day", hue="sex")
plt.show()
```

### Bar Plot

```python
# Mean by category (with confidence interval)
sns.barplot(data=tips, x="day", y="total_bill")
plt.show()
```

### Strip Plot

```python
# Individual points
sns.stripplot(data=tips, x="day", y="total_bill")
plt.show()
```

### Swarm Plot

```python
# Non-overlapping points
sns.swarmplot(data=tips, x="day", y="total_bill")
plt.show()
```

---

## 4. Relational Plots

### Scatter Plot

```python
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()

# With hue and size
sns.scatterplot(data=tips, x="total_bill", y="tip",
                hue="day", size="size")
plt.show()
```

### Line Plot

```python
# Line plot with confidence interval
sns.lineplot(data=tips, x="size", y="total_bill")
plt.show()
```

### Regression Plot

```python
# Scatter with regression line
sns.regplot(data=tips, x="total_bill", y="tip")
plt.show()

# Using lmplot for faceting
sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.show()
```

### Joint Plot

```python
# Bivariate plot with marginal distributions
sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter")
plt.show()

# Different kinds: "scatter", "kde", "hist", "hex", "reg"
sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex")
plt.show()
```

### Pair Plot

```python
# All pairwise relationships
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()
```

---

## 5. Matrix Plots

### Heatmap

```python
import numpy as np

# Correlation matrix
tips = sns.load_dataset("tips")
corr = tips.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
```

### Cluster Map

```python
# Hierarchically clustered heatmap
sns.clustermap(corr, annot=True, cmap="coolwarm")
plt.show()
```

---

## 6. Styling

### Set Theme

```python
# Built-in themes
sns.set_theme(style="darkgrid")    # Default
sns.set_theme(style="whitegrid")
sns.set_theme(style="dark")
sns.set_theme(style="white")
sns.set_theme(style="ticks")
```

### Color Palettes

```python
# Set palette
sns.set_palette("husl")
sns.set_palette("Set2")
sns.set_palette("coolwarm")

# Custom palette
colors = ["#FF5733", "#33FF57", "#3357FF"]
sns.set_palette(colors)
```

### Context (Scale)

```python
# Scale for different contexts
sns.set_context("paper")    # Smallest
sns.set_context("notebook") # Default
sns.set_context("talk")     # Larger
sns.set_context("poster")   # Largest
```

### Figure Size

```python
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()
```

---

## 7. Quick Reference

### Distribution Plots

| Function | Description |
|----------|-------------|
| `sns.histplot()` | Histogram |
| `sns.kdeplot()` | Density plot |
| `sns.boxplot()` | Box plot |
| `sns.violinplot()` | Violin plot |

### Categorical Plots

| Function | Description |
|----------|-------------|
| `sns.countplot()` | Count of occurrences |
| `sns.barplot()` | Mean with CI |
| `sns.stripplot()` | Points |
| `sns.swarmplot()` | Non-overlapping points |

### Relational Plots

| Function | Description |
|----------|-------------|
| `sns.scatterplot()` | Scatter plot |
| `sns.lineplot()` | Line plot |
| `sns.regplot()` | Regression plot |
| `sns.jointplot()` | Joint distribution |
| `sns.pairplot()` | Pairwise relationships |

### Matrix Plots

| Function | Description |
|----------|-------------|
| `sns.heatmap()` | Heatmap |
| `sns.clustermap()` | Clustered heatmap |

### Common Parameters

| Parameter | Description |
|-----------|-------------|
| `data` | DataFrame |
| `x`, `y` | Column names |
| `hue` | Color by category |
| `size` | Size by value |
| `style` | Style by category |
| `palette` | Color palette |

### Themes

| Style | Description |
|-------|-------------|
| `darkgrid` | Dark background with grid |
| `whitegrid` | White background with grid |
| `dark` | Dark background |
| `white` | White background |
| `ticks` | White with ticks |

---

## Coverage Checklist

- [x] Distribution plots
- [x] Categorical plots
- [x] Relational plots
- [x] Matrix plots
- [x] Styling and themes
- [x] Quick reference
