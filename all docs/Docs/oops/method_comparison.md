# Python OOP Method Types - Complete Comparison Guide

A comprehensive reference comparing self, cls, @staticmethod, @classmethod, @property, and other OOP concepts.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Instance Methods (self)](#2-instance-methods-self)
3. [Class Methods (cls)](#3-class-methods-cls)
4. [Static Methods](#4-static-methods)
5. [Property Methods](#5-property-methods)
6. [Magic Methods](#6-magic-methods)
7. [Private Members](#7-private-members)
8. [Complete Comparison](#8-complete-comparison)
9. [Full Example](#9-full-example)

---

## 1. Overview

### Method Types at a Glance

| Type | Decorator | First Argument | Access Level |
|------|-----------|----------------|--------------|
| Instance Method | None | `self` (instance) | Instance + Class |
| Class Method | `@classmethod` | `cls` (class) | Class only |
| Static Method | `@staticmethod` | None | Arguments only |
| Property | `@property` | `self` (instance) | Instance + Class |

### Quick Decision Guide

```
What do you need to access?
│
├── Instance data (self.attribute)?
│   └── Use Instance Method or Property
│
├── Class data only (cls.attribute)?
│   └── Use Class Method
│
└── Neither (just arguments)?
    └── Use Static Method
```

---

## 2. Instance Methods (self)

### Definition

Instance methods are the default method type. They receive the instance object as their first argument (`self`), allowing access to both instance and class attributes.

### Syntax

```python
class MyClass:
    def instance_method(self, arg1, arg2):
        # Can access self.attribute and MyClass.class_var
        return self.attribute + arg1
```

### Example

```python
class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    def bark(self):
        # Access instance data via self
        return f"{self.name} says Woof!"

    def describe(self):
        # Access both instance and class data
        return f"{self.name} is a {self.species}"

fido = Dog("Fido", 3)
print(fido.bark())      # Fido says Woof!
print(fido.describe())  # Fido is a Canis familiaris
```

### Key Points

| Point | Description |
|-------|-------------|
| First argument | `self` (instance reference) - automatic |
| Can access | Instance variables, class variables, other methods |
| Can modify | Instance state and class state |
| Call syntax | `object.method()` or `Class.method(object)` |

---

## 3. Class Methods (cls)

### Definition

Class methods receive the class itself as the first argument (`cls`) instead of an instance. They can access and modify class state but not instance state.

### Syntax

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1):
        return cls.class_variable + arg1
```

### Example

```python
class Employee:
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def get_company(cls):
        return cls.company

    @classmethod
    def get_count(cls):
        return cls.employee_count

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

# Usage
print(Employee.get_company())  # TechCorp
e1 = Employee("Alice")
e2 = Employee("Bob")
print(Employee.get_count())    # 2
Employee.change_company("NewCorp")
print(Employee.get_company())  # NewCorp
```

### Factory Methods (Common Use Case)

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor from string."""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """Alternative constructor for today's date."""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

# Multiple ways to create Date objects
date1 = Date(2024, 12, 25)
date2 = Date.from_string("2024-12-25")
date3 = Date.today()
```

### Key Points

| Point | Description |
|-------|-------------|
| Decorator | `@classmethod` required |
| First argument | `cls` (class reference) - automatic |
| Can access | Class variables and methods |
| Cannot access | Instance variables (no `self`) |
| Common use | Factory methods, class state management |

---

## 4. Static Methods

### Definition

Static methods don't receive any implicit first argument. They're essentially regular functions that belong to a class's namespace.

### Syntax

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        return arg1 + arg2
```

### Example

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# Call via class
print(MathUtils.add(5, 3))      # 8
print(MathUtils.is_even(4))     # True
print(MathUtils.factorial(5))   # 120

# Can also call via instance
utils = MathUtils()
print(utils.add(2, 3))          # 5
```

### Key Points

| Point | Description |
|-------|-------------|
| Decorator | `@staticmethod` required |
| First argument | None - no implicit argument |
| Can access | Only arguments passed to it |
| Cannot access | Instance or class state (unless hardcoded) |
| Common use | Utility functions, helpers |

---

## 5. Property Methods

### Definition

Properties allow you to define methods that are accessed like attributes. They provide controlled access to instance data with optional getter, setter, and deleter.

### Syntax

```python
class MyClass:
    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value
```

### Example: Read-Only Property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        """Calculated property - read only."""
        return self._radius * 2

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.diameter)  # 10 (accessed like attribute, no parentheses)
print(c.area)      # 78.54...
# c.diameter = 20  # AttributeError: can't set attribute
```

### Example: Getter and Setter

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter for celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Calculated property."""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature via Fahrenheit."""
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

temp.fahrenheit = 100   # Set via Fahrenheit
print(temp.celsius)     # 37.78...
```

### Key Points

| Point | Description |
|-------|-------------|
| Decorator | `@property` for getter |
| Setter decorator | `@property_name.setter` |
| Access syntax | `obj.property` (no parentheses) |
| Use case | Computed values, validation, encapsulation |

---

## 6. Magic Methods

### Definition

Magic methods (dunder methods) are special methods with double underscores that Python calls automatically in certain situations.

### Common Magic Methods

| Method | Called When |
|--------|-------------|
| `__init__` | Object creation |
| `__str__` | `str(obj)` or `print(obj)` |
| `__repr__` | `repr(obj)` or in interpreter |
| `__len__` | `len(obj)` |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` |
| `__add__` | `obj1 + obj2` |
| `__getitem__` | `obj[key]` |

### Example

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        """Human-readable string."""
        return f"{self.title}"

    def __repr__(self):
        """Developer-readable string."""
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        """Return page count."""
        return self.pages

    def __eq__(self, other):
        """Compare books by title."""
        return self.title == other.title

    def __lt__(self, other):
        """Compare by page count."""
        return self.pages < other.pages

book1 = Book("Python Guide", 300)
book2 = Book("Java Guide", 400)

print(book1)           # Python Guide (uses __str__)
print(repr(book1))     # Book('Python Guide', 300) (uses __repr__)
print(len(book1))      # 300 (uses __len__)
print(book1 < book2)   # True (uses __lt__)
```

---

## 7. Private Members

### Naming Conventions

| Convention | Example | Meaning |
|------------|---------|---------|
| Public | `name` | Accessible everywhere |
| Protected | `_name` | Convention: internal use |
| Private | `__name` | Name mangling applied |

### Private Attributes and Methods

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def __validate(self, amount):  # Private method
        return amount > 0

    def deposit(self, amount):
        if self.__validate(amount):
            self.__balance += amount
            return True
        return False

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150

# Cannot access directly:
# print(account.__balance)    # AttributeError
# account.__validate(10)      # AttributeError

# Name mangling - can access (but shouldn't):
print(account._BankAccount__balance)  # 150
```

### Protected vs Private

```python
class Parent:
    def __init__(self):
        self._protected = "protected"   # Convention only
        self.__private = "private"      # Name mangled

class Child(Parent):
    def access_parent(self):
        print(self._protected)    # Works (by convention)
        # print(self.__private)   # AttributeError!
```

---

## 8. Complete Comparison

### Method Types Comparison Table

| Feature | Instance | Class | Static | Property |
|---------|----------|-------|--------|----------|
| Decorator | None | `@classmethod` | `@staticmethod` | `@property` |
| First arg | `self` | `cls` | None | `self` |
| Access instance | Yes | No | No | Yes |
| Access class | Yes | Yes | Hardcoded only | Yes |
| Modify instance | Yes | No | No | Yes (setter) |
| Modify class | Yes | Yes | No | No |
| Call syntax | `obj.method()` | `Class.method()` | `Class.method()` | `obj.property` |

### When to Use What

| Situation | Use |
|-----------|-----|
| Work with object data | Instance method |
| Factory method / alternative constructor | Class method |
| Modify class-level state | Class method |
| Utility function | Static method |
| Computed attribute | Property (getter) |
| Validated attribute | Property (getter + setter) |
| Read-only attribute | Property (getter only) |

### Access Comparison

```python
class Demo:
    class_var = "class"

    def __init__(self):
        self.instance_var = "instance"

    def instance_method(self):
        # Can access both
        return f"{self.instance_var}, {self.class_var}"

    @classmethod
    def class_method(cls):
        # Can access class only
        return cls.class_var
        # Cannot: self.instance_var

    @staticmethod
    def static_method():
        # Cannot access either directly
        return Demo.class_var  # Must hardcode class name

    @property
    def computed(self):
        # Can access both
        return f"{self.instance_var} computed"
```

---

## 9. Full Example

### Complete Class with All Method Types

```python
class Car:
    # Class variable
    wheels = 4
    total_cars = 0

    def __init__(self, brand, model):
        # Instance variables
        self.brand = brand
        self.model = model
        self._mileage = 0  # Protected
        self.__vin = self.__generate_vin()  # Private
        Car.total_cars += 1

    # INSTANCE METHOD
    def drive(self, miles):
        """Instance method - works with object data."""
        self._mileage += miles
        return f"{self.brand} drove {miles} miles"

    # CLASS METHOD
    @classmethod
    def get_total_cars(cls):
        """Class method - works with class data."""
        return f"Total cars: {cls.total_cars}"

    @classmethod
    def from_string(cls, car_string):
        """Factory method - alternative constructor."""
        brand, model = car_string.split('-')
        return cls(brand, model)

    # STATIC METHOD
    @staticmethod
    def is_valid_year(year):
        """Static method - utility function."""
        return 1900 <= year <= 2024

    # PROPERTY - Getter
    @property
    def mileage(self):
        """Read-only property."""
        return self._mileage

    # PROPERTY - Getter and Setter
    @property
    def full_name(self):
        return f"{self.brand} {self.model}"

    @full_name.setter
    def full_name(self, value):
        self.brand, self.model = value.split(' ', 1)

    # PRIVATE METHOD
    def __generate_vin(self):
        """Private method for internal use."""
        import random
        return ''.join(str(random.randint(0, 9)) for _ in range(17))

    # MAGIC METHODS
    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}')"


# Usage Examples
print("=" * 50)

# Create instances
car1 = Car("Toyota", "Camry")
car2 = Car.from_string("Honda-Civic")  # Factory method

# Instance method
print(car1.drive(100))  # Toyota drove 100 miles

# Class method
print(Car.get_total_cars())  # Total cars: 2

# Static method
print(Car.is_valid_year(2020))  # True

# Property (getter)
print(car1.mileage)  # 100

# Property (setter)
car1.full_name = "Ford Mustang"
print(car1.brand)  # Ford
print(car1.model)  # Mustang

# Magic method
print(car1)        # Ford Mustang
print(repr(car2))  # Car('Honda', 'Civic')

# Class variable access
print(car1.wheels)  # 4
print(Car.wheels)   # 4
```

---

## Quick Reference Summary

### Syntax Quick Reference

```python
class MyClass:
    class_var = "shared"           # Class variable

    def __init__(self):            # Constructor
        self.instance_var = "unique"

    def instance_method(self):     # Instance method
        pass

    @classmethod
    def class_method(cls):         # Class method
        pass

    @staticmethod
    def static_method():           # Static method
        pass

    @property
    def prop(self):                # Property getter
        return self._value

    @prop.setter
    def prop(self, value):         # Property setter
        self._value = value
```

---

## Coverage Checklist

- [x] Instance methods (self)
- [x] Class methods (cls)
- [x] Static methods
- [x] Property methods (getter/setter)
- [x] Magic methods
- [x] Private members
- [x] Complete comparison table
- [x] Full example with all types
