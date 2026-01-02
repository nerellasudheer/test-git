# Python Format Specifiers - Quick Reference

A guide to formatting output in Python using format specifiers.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Format Specifier Structure](#2-format-specifier-structure)
3. [Alignment and Fill](#3-alignment-and-fill)
4. [Sign Display](#4-sign-display)
5. [Width and Padding](#5-width-and-padding)
6. [Precision](#6-precision)
7. [Type Specifiers](#7-type-specifiers)
8. [Thousands Separator](#8-thousands-separator)
9. [Quick Reference](#9-quick-reference)

---

## 1. Overview

### What are Format Specifiers?

Format specifiers are codes used inside strings to define how values should be formatted for output. They control decimal places, alignment, padding, and more.

### Usage Methods

```python
# f-strings (Python 3.6+)
name = "Alice"
print(f"Name: {name:<10}")

# str.format()
print("Name: {:<10}".format("Alice"))
```

---

## 2. Format Specifier Structure

### General Syntax

```
{value:[[fill]align][sign][#][0][width][,][.precision][type]}
```

| Component | Description | Example |
|-----------|-------------|---------|
| `fill` | Character used for padding | `*` |
| `align` | Alignment: `<` left, `>` right, `^` center | `<` |
| `sign` | Sign display: `+`, `-`, space | `+` |
| `width` | Minimum total width | `10` |
| `,` | Thousands separator | `12,345` |
| `.precision` | Decimal places for floats | `.2` |
| `type` | Data type format | `f`, `d`, `s` |

---

## 3. Alignment and Fill

### Left Alignment (`<`)

```python
print(f"{'Data':*<10}")
# Output: Data******
```

The string is left-aligned with `*` filling the remaining space.

### Right Alignment (`>`)

```python
print(f"{'Data':*>10}")
# Output: ******Data
```

### Center Alignment (`^`)

```python
print(f"{'Center':-^12}")
# Output: ---Center---
```

The string is centered with `-` as the fill character.

---

## 4. Sign Display

### Always Show Sign (`+`)

```python
print(f"Positive: {10:+d} Negative: {-10:+d}")
# Output: Positive: +10 Negative: -10
```

### Space for Positive Sign (` `)

```python
print(f"Positive: {10: d} Negative: {-10: d}")
# Output: Positive:  10 Negative: -10
```

A space is left in front of positive numbers for alignment.

---

## 5. Width and Padding

### Integer with Zero Padding

```python
print(f"ID: {5:03d}")
# Output: ID: 005
```

The number is padded with leading zeros to width 3.

### Float with Width

```python
print(f"Value: {12.5:10.2f}")
# Output: Value:      12.50
```

Total width of 10, with 2 decimal places.

---

## 6. Precision

### Limiting Decimal Places

```python
print(f"Price: ${19.999:.2f}")
# Output: Price: $20.00
```

The number is rounded to 2 decimal places.

### Scientific Notation

```python
print(f"Number: {12345678:.2e}")
# Output: Number: 1.23e+07
```

The `e` type with precision for scientific notation.

---

## 7. Type Specifiers

### Common Types

| Type | Description | Example |
|------|-------------|---------|
| `d` | Integer | `{42:d}` → `42` |
| `f` | Float | `{3.14159:.2f}` → `3.14` |
| `s` | String | `{"text":s}` → `text` |
| `b` | Binary | `{10:b}` → `1010` |
| `o` | Octal | `{10:o}` → `12` |
| `x` | Hexadecimal (lowercase) | `{255:x}` → `ff` |
| `X` | Hexadecimal (uppercase) | `{255:X}` → `FF` |
| `e` | Scientific notation | `{1000:.2e}` → `1.00e+03` |
| `%` | Percentage | `{0.75:.0%}` → `75%` |

### Examples

```python
# Float and Integer
print(f"Rate: {0.75:.2f} | Quantity: {100:d}")
# Output: Rate: 0.75 | Quantity: 100

# Binary
print(f"The number 10 in binary is {10:b}")
# Output: The number 10 in binary is 1010

# Hexadecimal
print(f"255 in hex is {255:x}")
# Output: 255 in hex is ff

# Percentage
print(f"Progress: {0.756:.1%}")
# Output: Progress: 75.6%
```

---

## 8. Thousands Separator

### Integer with Comma

```python
print(f"Population: {123456789:,d}")
# Output: Population: 123,456,789
```

### Float with Comma and Precision

```python
print(f"Value: ${12345.678:,.2f}")
# Output: Value: $12,345.68
```

---

## 9. Quick Reference

### Common Format Patterns

| Pattern | Output | Description |
|---------|--------|-------------|
| `{:d}` | `42` | Integer |
| `{:.2f}` | `3.14` | Float with 2 decimals |
| `{:,}` | `1,000,000` | Number with commas |
| `{:,.2f}` | `1,000.50` | Float with commas and decimals |
| `{:10}` | `"text      "` | Width of 10 (default left) |
| `{:>10}` | `"      text"` | Right-aligned, width 10 |
| `{:^10}` | `"   text   "` | Center-aligned, width 10 |
| `{:<10}` | `"text      "` | Left-aligned, width 10 |
| `{:*^10}` | `"***text***"` | Center with `*` fill |
| `{:05d}` | `00042` | Zero-padded integer |
| `{:+d}` | `+42` | Always show sign |
| `{:.2e}` | `1.23e+04` | Scientific notation |
| `{:.0%}` | `75%` | Percentage |
| `{:b}` | `1010` | Binary |
| `{:x}` | `2a` | Hexadecimal |

### Format Specifier Components

| Component | Options | Example |
|-----------|---------|---------|
| Fill | Any character | `*`, `-`, `0` |
| Align | `<` `>` `^` `=` | `{:>10}` |
| Sign | `+` `-` ` ` | `{:+d}` |
| Width | Integer | `{:10}` |
| Precision | `.n` | `{:.2f}` |
| Type | `d` `f` `s` `b` `x` `e` `%` | `{:d}` |

### Quick Examples

```python
# Align text in columns
print(f"{'Name':<15}{'Age':>5}{'City':^15}")
print(f"{'Alice':<15}{25:>5}{'New York':^15}")
# Output:
# Name                Age     City
# Alice                25    New York

# Format currency
price = 1234.567
print(f"Price: ${price:,.2f}")
# Output: Price: $1,234.57

# Format percentage
ratio = 0.857
print(f"Success rate: {ratio:.1%}")
# Output: Success rate: 85.7%

# Zero-padded numbers
for i in range(1, 4):
    print(f"File_{i:03d}.txt")
# Output:
# File_001.txt
# File_002.txt
# File_003.txt
```

---

## Coverage Checklist

- [x] Format specifier overview
- [x] Alignment and fill
- [x] Sign display
- [x] Width and padding
- [x] Precision
- [x] Type specifiers
- [x] Thousands separator
- [x] Quick reference tables
