# Python OOP Basics - Complete Guide

Object-Oriented Programming fundamentals with encapsulation, inheritance, polymorphism, and abstraction.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Classes and Objects](#2-classes-and-objects)
3. [Encapsulation](#3-encapsulation)
4. [Inheritance](#4-inheritance)
5. [Polymorphism](#5-polymorphism)
6. [Abstraction](#6-abstraction)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is OOP?

Object-Oriented Programming is a programming paradigm that organizes code into objects that contain data (attributes) and behavior (methods).

### Four Pillars of OOP

| Pillar | Description |
|--------|-------------|
| **Encapsulation** | Bundle data and methods, hide internal details |
| **Inheritance** | Create new classes from existing ones |
| **Polymorphism** | Same interface, different implementations |
| **Abstraction** | Hide complexity, show only essentials |

### Basic Terminology

| Term | Description |
|------|-------------|
| Class | Blueprint for creating objects |
| Object | Instance of a class |
| Attribute | Variable belonging to object |
| Method | Function belonging to object |
| Constructor | Special method `__init__` to initialize |

---

## 2. Classes and Objects

### Defining a Class

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    def description(self):
        return f"{self.name} is {self.age} years old"
```

### Creating Objects (Instances)

```python
# Create instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access attributes
print(dog1.name)       # Buddy
print(dog2.age)        # 5
print(dog1.species)    # Canis familiaris

# Call methods
print(dog1.bark())     # Buddy says Woof!
print(dog2.description())  # Max is 5 years old
```

### The `self` Parameter

```python
class Example:
    def method(self):
        # 'self' refers to the instance calling the method
        print(f"Called on {self}")

obj = Example()
obj.method()  # self = obj
```

### Class vs Instance Attributes

```python
class Employee:
    # Class attribute - shared by all
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name):
        # Instance attribute - unique to each
        self.name = name
        Employee.employee_count += 1

emp1 = Employee("Alice")
emp2 = Employee("Bob")

print(Employee.company)          # TechCorp
print(Employee.employee_count)   # 2
print(emp1.name)                 # Alice
```

---

## 3. Encapsulation

### What is Encapsulation?

Bundling data and methods that operate on the data within a single unit (class), and restricting direct access to some components.

### Access Modifiers

| Convention | Access Level | Example |
|------------|--------------|---------|
| `name` | Public | Accessible from anywhere |
| `_name` | Protected | Internal use (convention) |
| `__name` | Private | Name mangling applied |

### Public Attributes

```python
class Person:
    def __init__(self, name):
        self.name = name  # Public

p = Person("Alice")
print(p.name)        # Alice
p.name = "Bob"       # Can modify directly
print(p.name)        # Bob
```

### Protected Attributes (Convention)

```python
class Person:
    def __init__(self, name):
        self._name = name  # Protected (by convention)

p = Person("Alice")
print(p._name)       # Alice (still accessible, but shouldn't)
```

### Private Attributes (Name Mangling)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(1000)
# print(account.__balance)       # Error! AttributeError
print(account.get_balance())     # 1000
print(account._BankAccount__balance)  # 1000 (name mangling)
```

### Getters and Setters

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter
    def get_age(self):
        return self._age

    # Setter with validation
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

p = Person("Alice", 25)
print(p.get_age())    # 25
p.set_age(30)
print(p.get_age())    # 30
# p.set_age(-5)       # ValueError
```

### @property Decorator (Pythonic Way)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter for radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Read-only property."""
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.radius)   # 5 (uses getter)
circle.radius = 10     # Uses setter
print(circle.area)     # 314.159
# circle.area = 100    # Error! No setter defined
```

---

## 4. Inheritance

### What is Inheritance?

Creating a new class (child) that inherits attributes and methods from an existing class (parent).

### Single Inheritance

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def speak(self):  # Override parent method
        return f"{self.name} says Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)       # Buddy (inherited)
print(dog.breed)      # Golden Retriever
print(dog.speak())    # Buddy says Woof!
```

### super() Function

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Initialize parent
        self.age = age

    def greet(self):
        # Call parent's greet and add to it
        parent_greeting = super().greet()
        return f"{parent_greeting}, I'm {self.age} years old"

child = Child("Alice", 10)
print(child.greet())  # Hello, I'm Alice, I'm 10 years old
```

### Method Overriding

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # Override
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Override
        return 3.14159 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())  # 20, 28.27...
```

### Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return "Flying!"

class Swimmable:
    def swim(self):
        return "Swimming!"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())     # Flying!
print(duck.swim())    # Swimming!
print(duck.quack())   # Quack!
```

### Method Resolution Order (MRO)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())     # B
print(D.mro())        # [D, B, C, A, object]
```

---

## 5. Polymorphism

### What is Polymorphism?

"Many forms" - the ability to use a common interface for different underlying data types.

### Method Overriding (Runtime Polymorphism)

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Same method, different behavior
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.speak())  # Woof!, Meow!, Moo!
```

### Duck Typing

```python
# "If it walks like a duck and quacks like a duck, it's a duck"
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep!"

# No common parent needed!
def make_speak(thing):
    print(thing.speak())

make_speak(Dog())    # Woof!
make_speak(Cat())    # Meow!
make_speak(Robot())  # Beep!
```

### Polymorphism with Functions

```python
# Built-in example: len() works on many types
print(len("hello"))      # 5
print(len([1, 2, 3]))    # 3
print(len({"a": 1}))     # 1

# Custom polymorphic function
def add(a, b):
    return a + b

print(add(1, 2))         # 3 (integers)
print(add("Hello", " World"))  # Hello World (strings)
print(add([1, 2], [3, 4]))     # [1, 2, 3, 4] (lists)
```

---

## 6. Abstraction

### What is Abstraction?

Hiding complex implementation details and showing only the necessary features.

### Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented."""
        pass

# shape = Shape()  # Error! Cannot instantiate abstract class

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print(rect.area())       # 20
print(rect.perimeter())  # 18
```

### Abstract Properties

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @property
    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    @property
    def max_speed(self):
        return 200

    def start(self):
        return "Car engine started"

car = Car()
print(car.max_speed)  # 200
print(car.start())    # Car engine started
```

### Practical Example

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

    def refund(self, amount):
        return f"Refunding ${amount} to Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

    def refund(self, amount):
        return f"Refunding ${amount} to PayPal account"

# Use same interface for different payment types
def checkout(processor, amount):
    print(processor.process_payment(amount))

checkout(CreditCardProcessor(), 100)  # Processing $100 via Credit Card
checkout(PayPalProcessor(), 50)       # Processing $50 via PayPal
```

---

## 7. Quick Reference

### Class Definition

```python
class ClassName:
    class_attr = value

    def __init__(self, params):
        self.instance_attr = params

    def method(self):
        pass
```

### Access Modifiers

| Symbol | Level | Usage |
|--------|-------|-------|
| `name` | Public | Normal access |
| `_name` | Protected | Internal convention |
| `__name` | Private | Name mangling |

### Inheritance Syntax

```python
# Single
class Child(Parent):
    pass

# Multiple
class Child(Parent1, Parent2):
    pass

# Call parent
super().__init__()
super().method()
```

### @property Pattern

```python
@property
def attr(self):
    return self._attr

@attr.setter
def attr(self, value):
    self._attr = value
```

### Abstract Class Pattern

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def method(self):
        pass
```

### OOP Principles Summary

| Principle | Key Concept |
|-----------|-------------|
| Encapsulation | Hide data, use getters/setters |
| Inheritance | Reuse code via parent classes |
| Polymorphism | Same interface, different behavior |
| Abstraction | Hide complexity with ABCs |

---

## Coverage Checklist

- [x] Classes and objects basics
- [x] __init__ constructor
- [x] Instance vs class attributes
- [x] Encapsulation (public, protected, private)
- [x] Getters and setters
- [x] @property decorator
- [x] Single inheritance
- [x] super() function
- [x] Method overriding
- [x] Multiple inheritance and MRO
- [x] Polymorphism and duck typing
- [x] Abstract base classes (ABC)
- [x] Quick reference tables
