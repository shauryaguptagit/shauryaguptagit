"""
========================================================
PYTHON OBJECT ORIENTED PROGRAMMING (OOP) CONCEPTS
========================================================

Object Oriented Programming (OOP) is a programming
paradigm that organizes code using:
✔ Classes
✔ Objects

OOP helps in building:
✔ Modular
✔ Maintainable
✔ Scalable
✔ Reusable applications
"""

# ======================================================
# WHY OOP?
# ======================================================
"""
✔ Organizes code into logical structures
✔ Encapsulates data and behavior together
✔ Supports code reuse through inheritance
✔ Allows flexibility using polymorphism
✔ Improves maintainability and scalability
"""


# ======================================================
# CORE OOP PRINCIPLES
# ======================================================
"""
1. Class
2. Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction
"""


# ======================================================
# 1. CLASS
# ======================================================
"""
A class is a blueprint for creating objects.

✔ Defined using the 'class' keyword
✔ Contains attributes (variables)
✔ Contains methods (functions)
"""

class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable


# ======================================================
# 2. OBJECT
# ======================================================
"""
An object is an instance of a class.

Object has:
✔ State      → attributes
✔ Behavior   → methods
✔ Identity   → unique existence
"""

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1.name)
print(dog2.age)
print(dog1.species)

"""
Output:
-------
Buddy
5
Canine
"""


# ======================================================
# SELF PARAMETER
# ======================================================
"""
self refers to the current object calling the method.
It allows access to instance variables and methods.
"""

print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)
print(Dog.species)


# ======================================================
# __init__ METHOD (CONSTRUCTOR)
# ======================================================
"""
__init__ is automatically called when an object is created.
Used to initialize instance variables.
"""

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
print(p1.name)


# ======================================================
# CLASS VARIABLES vs INSTANCE VARIABLES
# ======================================================
"""
Class Variables:
✔ Shared across all objects

Instance Variables:
✔ Unique to each object
"""

class Animal:
    species = "Mammal"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable


a1 = Animal("Dog")
a2 = Animal("Cat")

print(a1.species)
Animal.species = "Reptile"
print(a2.species)


# ======================================================
# 3. INHERITANCE
# ======================================================
"""
Inheritance allows a child class to reuse
properties and methods of a parent class.
"""

# Single Inheritance
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

c = Car()
c.move()
c.drive()

# Multilevel Inheritance
class ElectricCar(Car):
    def charge(self):
        print("Charging electric car")

e = ElectricCar()
e.move()
e.drive()
e.charge()

# Multiple Inheritance
class MusicSystem:
    def play_music(self):
        print("Playing music")

class SmartCar(Car, MusicSystem):
    pass

s = SmartCar()
s.drive()
s.play_music()


# ======================================================
# 4. POLYMORPHISM
# ======================================================
"""
Polymorphism means:
✔ Same method name
✔ Different behavior
"""

# Method Overriding (Run-time Polymorphism)
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

print(Dog().speak())

# Duck Typing
class Cat:
    def speak(self):
        return "Meow!"

def make_sound(obj):
    print(obj.speak())

make_sound(Dog())
make_sound(Cat())

# Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)


# ======================================================
# 5. ENCAPSULATION
# ======================================================
"""
Encapsulation binds data and methods together
and restricts direct access.

Access Modifiers:
✔ Public      → name
✔ Protected   → _name
✔ Private     → __name
"""

class Student:
    def __init__(self, name, marks):
        self.name = name          # Public
        self._course = "CS"       # Protected
        self.__marks = marks      # Private

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks

s = Student("Rahul", 85)
print(s.name)
print(s._course)
print(s.get_marks())

s.set_marks(90)
print(s.get_marks())


# ======================================================
# 6. ABSTRACTION
# ======================================================
"""
Abstraction hides implementation details
and shows only essential features.
"""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a shape")

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

r = Rectangle(4, 5)
r.describe()
print(r.area())


# ======================================================
# SUMMARY TABLE
# ======================================================
"""
Concept         | Purpose
--------------- | ----------------------------------
Class           | Blueprint for objects
Object          | Instance of a class
Encapsulation   | Data hiding
Inheritance     | Code reuse
Polymorphism    | One interface, many forms
Abstraction     | Hide implementation details
"""


# ======================================================
# KEY TAKEAWAYS
# ======================================================
"""
✔ OOP models real-world problems
✔ Improves code reuse and readability
✔ Essential for large-scale applications
✔ Very important for interviews and projects
✔ Python supports all major OOP concepts
"""

"""
End of Python OOP Concepts Module
--------------------------------
"""
