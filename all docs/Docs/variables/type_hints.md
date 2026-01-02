# Type Hints in Python

## Basic Information

**Data Type(s):** All Python types (int, str, list, dict, tuple, etc.) + typing module types

**Purpose:** Declares expected data types for function parameters and return values to improve code clarity, enable IDE autocomplete, and catch type-related bugs early.

**Syntax:**
```python
def function_name(param1: type, param2: type = default) -> return_type:
    return value

# Key Parameters:
# param: type - Declares parameter expects specific type
# param: type = default - Optional parameter with type and default value
# -> return_type - Declares what function returns
# Multiple types: Union[type1, type2] or type1 | type2 (Python 3.10+)
# Optional values: Optional[type] or type | None

# Returns:
# Type: Specified after -> arrow
# Behavior: Type hints don't enforce types at runtime
# Important: Type hints are for documentation and static analysis tools (mypy, pylance)
```

---

## Examples

### Basic Example
```python
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

result = greet("Alice", 25)
print(result)
# Output: Hello Alice, you are 25 years old

# Type hint shows IDE what types to expect
# greet("Bob", "30")  # IDE will warn: expected int, got str
```

### Real-World Example
```python
from typing import List, Dict, Optional

def calculate_average_price(products: List[Dict[str, float]]) -> float:
    """Calculate average price from product list"""
    total = sum(product['price'] for product in products)
    return total / len(products)

def find_user(user_id: int, database: Dict[int, str]) -> Optional[str]:
    """Returns username or None if not found"""
    return database.get(user_id)

# Usage
products = [
    {'name': 'Laptop', 'price': 999.99},
    {'name': 'Mouse', 'price': 29.99}
]
avg = calculate_average_price(products)
print(f"Average price: ${avg:.2f}")
# Output: Average price: $514.99

users = {1: 'Alice', 2: 'Bob'}
user = find_user(1, users)
print(user)
# Output: Alice
```

---

## Type Hints in Class Constructors (OOP)

### Basic Example
```python
# Without type hints (confusing for others)
class Calculator:
    def __init__(self, name):
        self.name = name

# With type hints (clear expectations)
class Calculator:
    def __init__(self, name: str):
        self.name = name

calc = Calculator("MyCalc")  # IDE knows 'name' should be a string
# Output: Calculator object created with name="MyCalc"
```

### Real-World Example
```python
from quiz_brain import QuizBrain

class QuizScreen:
    def __init__(self, q_brain: QuizBrain):
        """
        q_brain: QuizBrain means "I expect a QuizBrain object here"
        This helps your IDE autocomplete q_brain's methods
        """
        self.q_brain = q_brain
        self.score = 0

    def display_question(self):
        # IDE now shows all QuizBrain methods when you type q_brain.
        current_q = self.q_brain.get_next_question()
        print(current_q)

# Usage
quiz_brain = QuizBrain(question_list)
screen = QuizScreen(q_brain=quiz_brain)  # Pass QuizBrain object
```

---

## When to Use Type Hints

### Use When:
- Writing functions that will be used by others (APIs, libraries)
- Working in large codebases with multiple developers
- You want better IDE autocomplete and error detection
- Documenting expected data structures (nested dicts, lists, etc.)
- Working with custom classes as parameters
- Building larger projects where type clarity prevents bugs

### Don't Use When:
- Writing quick scripts or prototypes (adds overhead)
- Types are obvious from context (use sparingly)
- Working with highly dynamic data that changes types frequently
- You're a complete beginner still learning basic syntax

---

## Important Notes

1. **Type hints are optional** - Python ignores them at runtime; they're for developers and tools, not the interpreter
2. **No runtime type checking** - Python won't raise errors if you pass wrong types; use mypy or similar tools for validation
3. **Use typing module for complex types** - For List, Dict, Tuple, Optional, Union, and other advanced hints
4. **IDEs love type hints** - They enable autocomplete, show method suggestions, and catch potential errors before running code
5. **Imports are required** - You must import the class before using it as a type hint

---

## Best Practices

```python
# Good Practice: Clear, specific types
def process_order(items: List[str], quantities: List[int], discount: float = 0.0) -> Dict[str, float]:
    total = sum(quantities) * 10.0 * (1 - discount)
    return {'total': total, 'discount': discount}
# Why: Makes function contract clear; helps catch bugs early

# Good Practice: Use Optional for nullable values
def get_config(key: str) -> Optional[str]:
    config = {'debug': 'true'}
    return config.get(key)  # Returns None if key not found
# Why: Explicitly shows None is a valid return value

# Good Practice: Type hints for return values in methods
class QuizScreen:
    def __init__(self, q_brain: QuizBrain) -> None:
        self.q_brain = q_brain

    def get_score(self) -> int:
        return self.score
# Why: Complete documentation of inputs and outputs

# Avoid: Overly complex type hints
from typing import Union, List, Dict, Tuple, Optional
def complex_func(data: Union[List[Dict[str, Union[int, str]]], Tuple[str, ...]]) -> Optional[Dict[str, List[Union[int, float]]]]:
    pass
# Why: Hard to read; consider simplifying or using TypedDict/dataclasses

# Avoid: Type hints everywhere
x: int = 5  # Unnecessary, obvious from assignment
name: str = "Alice"  # Obvious types don't need hints
# Why: Clutters code; focus on function signatures
```

---

## Common Mistakes

### Mistake 1: Thinking Type Hints Enforce Types
```python
# Wrong Assumption
def add(a: int, b: int) -> int:
    return a + b

result = add("Hello", "World")  # Runs without error!
print(result)
# Output: HelloWorld

# Correct Approach
# Use static type checker: mypy script.py
# Or enable IDE type checking (VSCode: Pylance)
# Add runtime validation if needed
def add_validated(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a + b
# Output: TypeError raised for wrong types
# Why Wrong: Type hints are documentation, not enforcement
```

### Mistake 2: Using Wrong typing Imports
```python
# Wrong Approach (Python 3.9+)
from typing import List, Dict

def process(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

# Correct Approach (Python 3.9+)
def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
# Output: Same functionality, cleaner syntax
# Why Wrong: Use built-in list/dict for Python 3.9+; typing.List is for older versions
```

### Mistake 3: Forgetting Optional for None Values
```python
# Wrong Approach
def find_item(items: List[str], target: str) -> str:
    for item in items:
        if item == target:
            return item
    return None  # Type checker warns: expected str, got None

# Correct Approach
from typing import Optional

def find_item(items: List[str], target: str) -> Optional[str]:
    for item in items:
        if item == target:
            return item
    return None  # Now explicitly allowed
# Output: Type checker happy
# Why Wrong: Must indicate None is possible return value
```

### Mistake 4: Forgetting to Import the Type
```python
# Wrong Approach
class QuizScreen:
    def __init__(self, q_brain: QuizBrain):  # NameError!
        self.q_brain = q_brain
# Output: NameError: name 'QuizBrain' is not defined

# Correct Approach
from quiz_brain import QuizBrain

class QuizScreen:
    def __init__(self, q_brain: QuizBrain):
        self.q_brain = q_brain
# Output: Works correctly, IDE shows QuizBrain methods
# Why Wrong: Type hints reference classes, which must be imported first
```

### Mistake 5: Circular Import Confusion
```python
# Wrong Approach (causes circular import)
# quiz_screen.py
from quiz_brain import QuizBrain

class QuizScreen:
    def __init__(self, q_brain: QuizBrain):
        self.q_brain = q_brain

# quiz_brain.py
from quiz_screen import QuizScreen  # Circular import!

# Correct Approach (use string annotation)
# quiz_screen.py
class QuizScreen:
    def __init__(self, q_brain: 'QuizBrain'):  # String prevents import
        self.q_brain = q_brain

# Or use TYPE_CHECKING (professional way)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from quiz_brain import QuizBrain

class QuizScreen:
    def __init__(self, q_brain: 'QuizBrain'):
        self.q_brain = q_brain
# Output: No circular import, type hints still work in IDEs
# Why Wrong: Importing for type hints can create circular dependencies
```

---

## Similar Concepts (Easy to Confuse)

### Optional[type] vs Union[type, None] vs type | None

**Optional[type]:**
- What it does: Shorthand for "type or None"
- Key difference: Syntactic sugar for Union[type, None]
```python
from typing import Optional

def get_value(key: str) -> Optional[int]:
    data = {'a': 1}
    return data.get(key)

result = get_value('b')
print(result)
# Output: None
```

**Union[type, None]:**
- What it does: Explicitly allows type or None
- Key difference: More verbose, equivalent to Optional
```python
from typing import Union

def get_value(key: str) -> Union[int, None]:
    data = {'a': 1}
    return data.get(key)

result = get_value('b')
print(result)
# Output: None
```

**type | None:**
- What it does: Modern syntax for Union (Python 3.10+)
- Key difference: Cleaner syntax, requires Python 3.10+
```python
def get_value(key: str) -> int | None:
    data = {'a': 1}
    return data.get(key)

result = get_value('b')
print(result)
# Output: None
```

**Key Difference:** All three are equivalent; use `type | None` for Python 3.10+, `Optional[type]` for older versions.

---

## Related Methods & Alternatives

| Feature | Module | Purpose | Use When | Notes |
|---------|--------|---------|----------|-------|
| `List[type]` | typing | Type hint for lists | Function params/returns | Use `list[type]` in 3.9+ |
| `Dict[k, v]` | typing | Type hint for dicts | Function params/returns | Use `dict[k, v]` in 3.9+ |
| `Tuple[types]` | typing | Fixed-length tuples | Specific tuple structure | `Tuple[int, str, bool]` |
| `Any` | typing | Accept any type | When type varies | Avoid overuse |
| `TypedDict` | typing | Dict with typed keys | Structured dictionaries | Better than Dict |
| `dataclass` | dataclasses | Type-safe classes | Complex data structures | Best for objects |
| `isinstance()` | Built-in | Runtime type checking | Need validation | Actually enforces types |
| `typing.Union` | Module | Multiple allowed types | Accept str OR int | `Union[str, int]` |
| `typing.Optional` | Module | None or specific type | Optional parameters | `Optional[str]` = `Union[str, None]` |

---

## Additional Type Hint Examples

```python
# Multiple return types
def process_input(value: str) -> int | float:
    try:
        return int(value)
    except ValueError:
        return float(value)

# Callable type (functions as parameters)
from typing import Callable

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    return operation(x, y)

result = apply_operation(5, 3, lambda a, b: a + b)
# Output: 8

# Generic types
from typing import TypeVar, List

T = TypeVar('T')

def get_first_item(items: List[T]) -> T:
    return items[0]

# Works with any type
print(get_first_item([1, 2, 3]))      # Output: 1
print(get_first_item(['a', 'b', 'c']))  # Output: a
```

---

## Performance Notes

**Time Complexity:** O(1) - No runtime overhead (type hints are ignored during execution)

**Space Complexity:** O(1) - Minimal memory for storing annotations

**Performance Tip:** Type hints don't affect runtime performance but enable faster development through better tooling and fewer bugs.

---

## Quick Reference Summary

| Aspect | Details |
|--------|---------|
| **Data Type(s)** | All Python types + typing module |
| **Purpose** | Document expected types for better code quality |
| **Returns** | Specified after `->`, purely documentation |
| **Key Parameters** | `param: type`, `param: type = default` |
| **Similar To** | Comments, but machine-readable |
| **Use When** | Writing reusable functions, team projects |
| **Avoid When** | Quick scripts, obvious types |
| **Performance** | O(1) - no runtime impact |
| **Common Mistake** | Thinking hints enforce types at runtime |

---

## Key Takeaway

```python
def __init__(self, q_brain: QuizBrain):
```
This means: "I'm expecting a QuizBrain object to be passed here. This helps my IDE suggest QuizBrain methods when I type `q_brain.` but Python won't stop you from passing a string or anything else." It's documentation that makes your code easier to understand and work with!
