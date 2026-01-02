# Python Inheritance and super() - Complete Guide

A comprehensive reference for understanding inheritance and the super() function in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Basic Inheritance](#2-basic-inheritance)
3. [The super() Function](#3-the-super-function)
4. [Method Resolution Order (MRO)](#4-method-resolution-order-mro)
5. [Multiple Inheritance](#5-multiple-inheritance)
6. [Practical Examples](#6-practical-examples)
7. [Common Mistakes](#7-common-mistakes)
8. [Quick Reference](#8-quick-reference)

---

## 1. Overview

### What is Inheritance?

Inheritance is a fundamental OOP concept where a new class (child/derived) is created from an existing class (parent/base). The child class automatically inherits the parent's attributes and methods.

### Key Definitions

| Term | Definition |
|------|------------|
| Parent/Base Class | The original class being inherited from |
| Child/Derived Class | The new class that inherits from parent |
| Inheritance | Mechanism to receive attributes/methods from parent |
| Method Overriding | Redefining a parent method in the child class |
| super() | Built-in function to call parent class methods |

### Why Use Inheritance?

- **Code Reusability**: Don't rewrite common functionality
- **Hierarchy**: Model real-world relationships
- **Extensibility**: Extend existing classes without modifying them
- **Polymorphism**: Child objects can be used where parent is expected

---

## 2. Basic Inheritance

### Syntax

```python
class Parent:
    pass

class Child(Parent):  # Child inherits from Parent
    pass
```

### Automatic Access to Parent Members

The child class automatically has access to parent's attributes and methods through `self`:

```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.species = "Unknown"

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    # No __init__ defined - uses parent's __init__
    def bark(self):
        return f"{self.name} says Woof!"  # Can access self.name

# Create child object
my_dog = Dog("Buddy")

# Access inherited attribute
print(my_dog.name)      # Buddy

# Access inherited method
print(my_dog.speak())   # Buddy makes a sound

# Access child's own method
print(my_dog.bark())    # Buddy says Woof!
```

### How Python Looks Up Members

When you access an attribute or method on an object, Python follows this order:

1. Check the instance itself
2. Check the instance's class
3. Check parent class(es) - following MRO

```python
class Parent:
    value = "parent"

class Child(Parent):
    pass

child = Child()
print(child.value)  # "parent" - found in Parent class
```

---

## 3. The super() Function

### What is super()?

`super()` returns a proxy object that allows you to call methods from a parent class. It's primarily used to:

1. Call the parent's `__init__` constructor
2. Call overridden parent methods from the child

### Syntax

```python
super().__init__(*args)      # Call parent's __init__
super().method_name(*args)   # Call parent's method
```

### Purpose 1: Calling Parent's __init__

When a child defines its own `__init__`, it **overrides** the parent's. Use `super()` to also run the parent's initialization:

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, doors):
        # Call parent's __init__ first
        super().__init__(make, model)
        # Then add child-specific attributes
        self.doors = doors

my_car = Car("Toyota", "Camry", 4)
print(my_car.make)   # Toyota (from parent)
print(my_car.model)  # Camry (from parent)
print(my_car.doors)  # 4 (from child)
```

### Purpose 2: Extending Overridden Methods

Call the parent's version of a method while adding extra functionality:

```python
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Cat(Animal):
    def make_sound(self):
        # Get parent's result
        parent_sound = super().make_sound()
        # Extend with child's behavior
        return f"{parent_sound} + Meow!"

cat = Cat()
print(cat.make_sound())  # Some generic sound + Meow!
```

### When super() is NOT Needed

For simple access to inherited attributes/methods, just use `self`:

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def call_greeting(self):
        # Just use self - no need for super()
        return self.greet()

child = Child()
print(child.call_greeting())  # Hello from Parent
```

### Summary: self vs super()

| Situation | Use |
|-----------|-----|
| Access inherited attribute/method | `self.attribute` or `self.method()` |
| Call overridden parent method | `super().method()` |
| Initialize parent in child's `__init__` | `super().__init__()` |

---

## 4. Method Resolution Order (MRO)

### What is MRO?

MRO defines the order in which Python searches for methods in class hierarchies. This is especially important with multiple inheritance.

### Viewing MRO

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# View MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

# Or use mro() method
print(D.mro())
```

### How MRO Works

Python uses C3 Linearization algorithm:
1. Child classes come before parents
2. Order of inheritance is preserved
3. Parents of a class come before `object`

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
print(d.method())  # "B" - found in B first (per MRO)
```

---

## 5. Multiple Inheritance

### Basic Multiple Inheritance

```python
class Flying:
    def fly(self):
        return "I can fly!"

class Swimming:
    def swim(self):
        return "I can swim!"

class Duck(Flying, Swimming):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())   # I can fly!
print(duck.swim())  # I can swim!
print(duck.quack()) # Quack!
```

### Diamond Problem and super()

The "diamond problem" occurs when a class inherits from two classes that share a common ancestor:

```python
class A:
    def __init__(self):
        print("A.__init__")

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

d = D()
# Output:
# D.__init__
# B.__init__
# C.__init__
# A.__init__

# super() ensures A.__init__ is called only once!
```

### Cooperative Multiple Inheritance

```python
class Base:
    def __init__(self, **kwargs):
        pass  # Absorb remaining kwargs

class Name(Base):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

class Age(Base):
    def __init__(self, age, **kwargs):
        self.age = age
        super().__init__(**kwargs)

class Person(Name, Age):
    def __init__(self, name, age):
        super().__init__(name=name, age=age)

p = Person("Alice", 30)
print(p.name)  # Alice
print(p.age)   # 30
```

---

## 6. Practical Examples

### Example 1: Basic Inheritance with super()

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name}: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        # Extend parent's method
        base_info = super().get_info()
        return f"{base_info} - Manages {self.department}"

manager = Manager("Alice", 75000, "Engineering")
print(manager.get_info())
# Alice: $75000 - Manages Engineering
```

### Example 2: Chain of Inheritance

```python
class LivingThing:
    def __init__(self, name):
        self.name = name
        self.alive = True

class Animal(LivingThing):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

class Pet(Animal):
    def __init__(self, name, species, owner):
        super().__init__(name, species)
        self.owner = owner

my_pet = Pet("Fluffy", "Cat", "Alice")
print(my_pet.name)     # Fluffy (from LivingThing)
print(my_pet.species)  # Cat (from Animal)
print(my_pet.owner)    # Alice (from Pet)
print(my_pet.alive)    # True (from LivingThing)
```

### Example 3: Overriding with Extension

```python
class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"A {self.color} shape"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def describe(self):
        base = super().describe()
        return f"{base} - Rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)

    def describe(self):
        base = super().describe()
        return base.replace("Rectangle", "Square")

square = Square("red", 5)
print(square.describe())  # A red shape - Square 5x5
print(square.area())      # 25
```

---

## 7. Common Mistakes

### Mistake 1: Forgetting super().__init__()

```python
# WRONG: Parent not initialized
class Child(Parent):
    def __init__(self, value):
        self.value = value
        # Missing: super().__init__()

# CORRECT: Initialize parent
class Child(Parent):
    def __init__(self, value):
        super().__init__()  # Initialize parent first
        self.value = value
```

### Mistake 2: Wrong Argument Passing

```python
class Parent:
    def __init__(self, name):
        self.name = name

# WRONG: Not passing required argument
class Child(Parent):
    def __init__(self, name, age):
        super().__init__()  # TypeError: missing 'name'
        self.age = age

# CORRECT: Pass required arguments
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Pass 'name' to parent
        self.age = age
```

### Mistake 3: Using Parent Class Name Instead of super()

```python
class Parent:
    def method(self):
        return "Parent"

# Works but NOT recommended
class Child(Parent):
    def method(self):
        return Parent.method(self) + " Child"

# BETTER: Use super()
class Child(Parent):
    def method(self):
        return super().method() + " Child"
```

### Mistake 4: Confusing When to Use super()

```python
class Parent:
    def greet(self):
        return "Hello"

class Child(Parent):
    def say_hello(self):
        # WRONG thinking: "I need super() to access parent"
        return super().greet()  # Works but unnecessary

    def say_hello_correct(self):
        # CORRECT: Just use self for inherited methods
        return self.greet()  # Simpler and cleaner
```

---

## 8. Quick Reference

### Inheritance Syntax

```python
class Parent:
    pass

class Child(Parent):       # Single inheritance
    pass

class Child(Parent1, Parent2):  # Multiple inheritance
    pass
```

### super() Usage Patterns

| Pattern | Usage |
|---------|-------|
| `super().__init__()` | Initialize parent class |
| `super().__init__(arg1, arg2)` | Initialize with arguments |
| `super().method()` | Call parent's method |
| `super().method(args)` | Call parent's method with args |

### Access Methods Summary

| Situation | Code | When to Use |
|-----------|------|-------------|
| Access inherited member | `self.member` | Normal inheritance |
| Call overridden method | `super().method()` | Extend parent behavior |
| Initialize parent | `super().__init__()` | Child has own `__init__` |

### Inheritance Best Practices

| Practice | Description |
|----------|-------------|
| Call super().__init__() | Always initialize parent in child's __init__ |
| Use super() not ParentName | Better for maintainability and MRO |
| Keep hierarchy shallow | Deep inheritance is hard to maintain |
| Prefer composition | Sometimes "has-a" is better than "is-a" |

### MRO Quick View

```python
# View method resolution order
ClassName.__mro__    # As tuple
ClassName.mro()      # As list
```

### Key Points

1. **Child inherits** all public attributes/methods from parent
2. **self** gives access to inherited members - no super() needed
3. **super()** is for calling **overridden** parent methods
4. **Always call super().__init__()** when child has own `__init__`
5. **MRO** determines method lookup order in multiple inheritance
6. **super() follows MRO** - not just immediate parent

---

## Coverage Checklist

- [x] Inheritance basics and syntax
- [x] Automatic member access
- [x] super() function and purposes
- [x] Method Resolution Order (MRO)
- [x] Multiple inheritance
- [x] Practical examples
- [x] Common mistakes
- [x] Quick reference tables
