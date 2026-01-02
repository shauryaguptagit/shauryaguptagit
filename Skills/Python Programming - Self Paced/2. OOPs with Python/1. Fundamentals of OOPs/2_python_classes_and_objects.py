"""
===========================================================
PYTHON CLASSES AND OBJECTS
===========================================================

Python follows Object Oriented Programming (OOP) which helps
model real-world entities using classes and objects.

✔ Improves code organization
✔ Encourages reusability
✔ Makes programs easier to maintain
✔ Essential for medium to large applications
"""

# =========================================================
# WHAT IS A CLASS?
# =========================================================
"""
A class is a user-defined blueprint or template for creating
objects. It bundles data (attributes) and behavior (methods)
together.

✔ Defined using the 'class' keyword
✔ Represents a new data type
✔ Can have class variables and methods
"""

# Defining a class
class Dog:
    sound = "bark"  # Class attribute


# =========================================================
# WHAT IS AN OBJECT?
# =========================================================
"""
An object is an instance of a class.

✔ Each object has its own data
✔ Multiple objects can be created from the same class
✔ Objects can access class attributes and methods
"""

# Creating an object
dog1 = Dog()
print(dog1.sound)

"""
Output:
-------
bark

Explanation:
sound is a class attribute shared by all objects of Dog class.
"""


# =========================================================
# WHY DO WE NEED CLASSES AND OBJECTS?
# =========================================================
"""
✔ Supports real-world modeling
✔ Promotes modular and reusable code
✔ Simplifies complex programs
✔ Enables inheritance, encapsulation & polymorphism
"""


# =========================================================
# USING __init__() METHOD (CONSTRUCTOR)
# =========================================================
"""
__init__() is a special method that initializes object data.
It runs automatically when an object is created.
"""

class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable


# =========================================================
# CREATING OBJECTS USING __init__()
# =========================================================
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.species)

"""
Output:
-------
Buddy
Canine

Explanation:
Dog("Buddy", 3) creates an object and initializes attributes.
"""


# =========================================================
# SELF PARAMETER
# =========================================================
"""
self refers to the current object calling the method.
It allows access to instance variables and methods.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Buddy", 3)
dog1.bark()

"""
Output:
-------
Buddy is barking!
"""


# =========================================================
# __str__() METHOD
# =========================================================
"""
__str__() defines a custom string representation of an object.
Used when print(object) or str(object) is called.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)
print(dog2)

"""
Without __str__(), output would look like:
<__main__.Dog object at 0x00000123>
"""


# =========================================================
# CLASS VARIABLES vs INSTANCE VARIABLES
# =========================================================
"""
Class Variables:
✔ Shared by all objects
✔ Defined at class level

Instance Variables:
✔ Unique to each object
✔ Defined using self
"""

class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable


dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1.species)
print(dog1.name)
print(dog2.name)

# Modify instance variable
dog1.name = "Max"
print(dog1.name)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)
print(dog2.species)

"""
Explanation:
✔ Changing class variable affects all objects
✔ Changing instance variable affects only that object
"""


# =========================================================
# GETTER AND SETTER METHODS (@property)
# =========================================================
"""
Used to control access to attributes.
Supports encapsulation and validation.
"""

class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value


dog = Dog("Buddy", 3)
print(dog.name)
dog.age = 5
print(dog.age)


# =========================================================
# METHOD OVERRIDING
# =========================================================
"""
Method overriding occurs when a child class provides
its own implementation of a parent class method.
"""

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof")

dog = Dog()
dog.sound()

"""
Output:
-------
Woof
"""


# =========================================================
# STATIC METHODS AND CLASS METHODS
# =========================================================
"""
@staticmethod:
✔ No access to instance or class

@classmethod:
✔ Receives class as first argument (cls)
"""

class Dog:
    @staticmethod
    def info():
        print("Dogs are loyal animals.")

    @classmethod
    def count(cls):
        print("This method belongs to:", cls)


dog = Dog()
dog.info()
dog.count()


# =========================================================
# ABSTRACT CLASSES
# =========================================================
"""
Abstract classes define methods that must be implemented
by subclasses. They cannot be instantiated directly.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof")

dog = Dog()
dog.sound()


# =========================================================
# FINAL SUMMARY
# =========================================================
"""
Concept                Purpose
--------------------------------------------------
Class                  Blueprint for objects
Object                 Instance of class
__init__                Initializes object
self                   Refers to current object
__str__                Readable object output
Class Variable          Shared data
Instance Variable       Object-specific data
Getter / Setter         Controlled access
Method Overriding       Runtime polymorphism
Static Method           Utility logic
Class Method            Class-level behavior
Abstract Class          Enforced structure
"""

"""
END OF PYTHON CLASSES AND OBJECTS NOTES
===========================================================
"""
