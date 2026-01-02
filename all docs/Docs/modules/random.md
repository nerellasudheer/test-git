# Python random Module - Quick Reference

A guide to generating random numbers and making random selections in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Random Numbers](#2-random-numbers)
3. [Random Selection](#3-random-selection)
4. [Shuffling](#4-shuffling)
5. [Reproducibility](#5-reproducibility)
6. [Practical Examples](#6-practical-examples)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is the random Module?

The `random` module provides functions for generating pseudo-random numbers and making random selections from sequences.

### Import

```python
import random
```

### Main Capabilities

| Category | Functions |
|----------|-----------|
| Random numbers | `random()`, `randint()`, `uniform()`, `randrange()` |
| Selection | `choice()`, `choices()`, `sample()` |
| Shuffling | `shuffle()` |
| Reproducibility | `seed()` |

---

## 2. Random Numbers

### random.random()

Returns a random float between 0.0 and 1.0 (exclusive of 1.0).

```python
import random

print(random.random())  # e.g., 0.7352894521
print(random.random())  # e.g., 0.1284567932
```

### random.randint(a, b)

Returns a random integer between `a` and `b` (inclusive).

```python
print(random.randint(1, 10))     # e.g., 7 (1 to 10)
print(random.randint(100, 200))  # e.g., 134 (100 to 200)
print(random.randint(0, 1))      # e.g., 0 or 1 (coin flip)
```

### random.randrange(start, stop, step)

Returns a random integer from `range(start, stop, step)`.

```python
# Random even number from 0-10
print(random.randrange(0, 11, 2))  # e.g., 4 (0, 2, 4, 6, 8, or 10)

# Random number from 0-9
print(random.randrange(10))  # Same as randrange(0, 10)
```

### random.uniform(a, b)

Returns a random float between `a` and `b`.

```python
print(random.uniform(1, 5))    # e.g., 2.947328
print(random.uniform(0, 100))  # e.g., 67.82341
print(random.uniform(-1, 1))   # e.g., -0.234567
```

---

## 3. Random Selection

### random.choice(sequence)

Returns a single random element from a non-empty sequence.

```python
colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))  # e.g., 'blue'

# Works with strings too
print(random.choice('hello'))  # e.g., 'e'

# Works with tuples
directions = ('north', 'south', 'east', 'west')
print(random.choice(directions))  # e.g., 'west'
```

### random.choices(population, k=1)

Returns a list of `k` random elements **with replacement** (same element can be picked multiple times).

```python
nums = [1, 2, 3, 4, 5]

# Pick 3 random numbers (can repeat)
print(random.choices(nums, k=3))  # e.g., [4, 1, 4]

# Pick 5 random letters (can repeat)
print(random.choices('abc', k=5))  # e.g., ['a', 'c', 'b', 'a', 'c']
```

**With weights:**

```python
# Higher weight = more likely to be chosen
items = ['common', 'rare', 'legendary']
weights = [70, 25, 5]  # 70%, 25%, 5%

results = random.choices(items, weights=weights, k=10)
print(results)  # 'common' appears most often
```

### random.sample(population, k)

Returns a list of `k` **unique** random elements **without replacement**.

```python
nums = [1, 2, 3, 4, 5]

# Pick 3 unique numbers
print(random.sample(nums, 3))  # e.g., [2, 4, 1] (no repeats)

# Pick 4 unique numbers from range
print(random.sample(range(100), 4))  # e.g., [72, 15, 93, 41]
```

**Note:** `k` cannot be larger than the population size.

### choice vs choices vs sample

| Function | Replacement | Returns | Use Case |
|----------|-------------|---------|----------|
| `choice()` | N/A | Single element | Pick one item |
| `choices(k=n)` | With | List of n (can repeat) | Multiple picks, repeats OK |
| `sample(k=n)` | Without | List of n unique | Multiple unique picks |

---

## 4. Shuffling

### random.shuffle(sequence)

Shuffles a list **in place** (modifies the original list).

```python
cards = ['A', 'K', 'Q', 'J', '10']
random.shuffle(cards)
print(cards)  # e.g., ['Q', 'J', 'K', 'A', '10']

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)  # e.g., [3, 1, 5, 2, 4]
```

**Important:** Returns `None`, modifies list in place!

```python
# WRONG - shuffle returns None
result = random.shuffle([1, 2, 3])
print(result)  # None

# CORRECT - shuffle modifies the list
my_list = [1, 2, 3]
random.shuffle(my_list)
print(my_list)  # Shuffled list
```

**To get a shuffled copy without modifying original:**

```python
original = [1, 2, 3, 4, 5]
shuffled = random.sample(original, len(original))
print(original)  # [1, 2, 3, 4, 5] (unchanged)
print(shuffled)  # Shuffled version
```

---

## 5. Reproducibility

### random.seed(a)

Sets the seed for the random number generator. Same seed = same sequence of random numbers.

```python
# Set seed
random.seed(42)
print(random.random())  # 0.6394267984578837
print(random.randint(1, 100))  # 82

# Reset to same seed - get same results
random.seed(42)
print(random.random())  # 0.6394267984578837 (same!)
print(random.randint(1, 100))  # 82 (same!)
```

**Use cases:**
- Testing (reproducible results)
- Debugging random behavior
- Sharing results with others

---

## 6. Practical Examples

### Dice Roll Simulator

```python
import random

def roll_dice(sides=6):
    return random.randint(1, sides)

# Roll a 6-sided die
print(roll_dice())  # 1-6

# Roll a 20-sided die (D&D style)
print(roll_dice(20))  # 1-20
```

### Coin Flip

```python
def flip_coin():
    return random.choice(['Heads', 'Tails'])

print(flip_coin())  # 'Heads' or 'Tails'
```

### Password Generator

```python
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

print(generate_password())    # e.g., 'aB3$xY9@mNpQ'
print(generate_password(16))  # 16-character password
```

### Card Deck

```python
import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(rank, suit) for suit in suits for rank in ranks]

def deal_cards(deck, num_cards):
    return random.sample(deck, num_cards)

deck = create_deck()
hand = deal_cards(deck, 5)
print(hand)  # e.g., [('7', 'Hearts'), ('K', 'Spades'), ...]
```

### Lottery Numbers

```python
def lottery_numbers(num_count=6, max_num=49):
    return sorted(random.sample(range(1, max_num + 1), num_count))

print(lottery_numbers())  # e.g., [7, 12, 23, 31, 38, 45]
```

### Random Selection with Probabilities

```python
# Loot drop system
loot_table = ['common', 'uncommon', 'rare', 'epic', 'legendary']
weights = [50, 30, 15, 4, 1]  # Drop rates in %

drops = random.choices(loot_table, weights=weights, k=10)
print(drops)  # Most will be 'common', few 'legendary'
```

---

## 7. Quick Reference

### Function Summary

| Function | Returns | Range/Behavior |
|----------|---------|----------------|
| `random()` | float | 0.0 <= x < 1.0 |
| `randint(a, b)` | int | a <= x <= b |
| `randrange(start, stop, step)` | int | From range() |
| `uniform(a, b)` | float | a <= x <= b |
| `choice(seq)` | element | One random item |
| `choices(seq, k)` | list | k items (with replacement) |
| `sample(seq, k)` | list | k unique items |
| `shuffle(list)` | None | Shuffles in place |
| `seed(a)` | None | Set random seed |

### Common Patterns

| Task | Code |
|------|------|
| Random integer 1-10 | `random.randint(1, 10)` |
| Random float 0-1 | `random.random()` |
| Random float 0-100 | `random.uniform(0, 100)` |
| Pick one from list | `random.choice(my_list)` |
| Pick n with repeats | `random.choices(my_list, k=n)` |
| Pick n unique | `random.sample(my_list, n)` |
| Shuffle list | `random.shuffle(my_list)` |
| Reproducible random | `random.seed(42)` |

### Key Points

1. **Import required**: `import random`
2. **randint is inclusive**: `randint(1, 10)` can return 10
3. **shuffle modifies in place**: Returns `None`
4. **sample for unique**: No repeated elements
5. **choices for repeats**: Same element can appear multiple times
6. **seed for reproducibility**: Same seed = same results

---

## Coverage Checklist

- [x] Random number generation
- [x] Random selection methods
- [x] Shuffling
- [x] Seeds and reproducibility
- [x] Practical examples
- [x] Quick reference table
