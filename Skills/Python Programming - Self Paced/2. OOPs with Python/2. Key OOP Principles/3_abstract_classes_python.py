"""
===========================================================
ABSTRACT CLASSES IN PYTHON
===========================================================

An Abstract Class in Python:
✔ Cannot be instantiated directly
✔ Acts as a blueprint for other classes
✔ Enforces a common interface
✔ Ensures subclasses implement required methods

Implemented using:
✔ abc module
✔ ABC base class
✔ @abstractmethod decorator
"""


# =========================================================
# WHEN TO USE ABSTRACT CLASSES
# =========================================================
"""
Use abstract classes when you want to:
✔ Define a common interface for subclasses
✔ Enforce implementation of certain methods
✔ Provide shared behavior with flexibility
✔ Design scalable and maintainable systems

Example idea:
✔ All animals must have a sound()
✔ But each animal makes a different sound
"""


# =========================================================
# ABSTRACT BASE CLASS (ABC)
# =========================================================
"""
Abstract Base Class:
✔ Inherits from ABC
✔ Contains one or more abstract methods
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass   # Abstract method


class Dog(Animal):
    def sound(self):
        return "Bark"


dog = Dog()
print(dog.sound())

"""
Output:
-------
Bark

Explanation:
✔ Animal is abstract (inherits ABC)
✔ sound() has no implementation
✔ Dog must implement sound()
✔ Dog becomes a concrete class
"""


# =========================================================
# ABSTRACT METHODS
# =========================================================
"""
Abstract Method:
✔ Declared using @abstractmethod
✔ Has no implementation
✔ Must be implemented by subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# animal = Animal()   # ❌ TypeError

"""
Explanation:
✔ make_sound() has no body
✔ Animal is incomplete
✔ Instantiation is not allowed
"""


# =========================================================
# CONCRETE METHODS IN ABSTRACT CLASS
# =========================================================
"""
Concrete Method:
✔ Fully implemented
✔ Can exist inside abstract class
✔ Can be reused by subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return "Moving..."


class Dog(Animal):
    def make_sound(self):
        return "Bark"


dog = Dog()
print(dog.move())
print(dog.make_sound())

"""
Output:
-------
Moving...
Bark

Explanation:
✔ move() is inherited as-is
✔ make_sound() implemented by Dog
✔ Mix of enforced + reusable behavior
"""


# =========================================================
# ABSTRACT PROPERTIES
# =========================================================
"""
Abstract Properties:
✔ Used when attribute must exist in subclasses
✔ Defined using @property + @abstractmethod
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass


class Dog(Animal):
    @property
    def species(self):
        return "Canine"


dog = Dog()
print(dog.species)

"""
Output:
-------
Canine

Explanation:
✔ species is mandatory
✔ Dog must implement it
✔ Ensures consistent attributes
"""


# =========================================================
# ABSTRACT CLASS INSTANTIATION RULE
# =========================================================
"""
Abstract classes cannot be instantiated directly
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# animal = Animal()
# TypeError: Can't instantiate abstract class

"""
Explanation:
✔ Abstract methods are unimplemented
✔ Python blocks object creation
✔ Only fully implemented subclasses allowed
"""


# =========================================================
# INCOMPLETE SUBCLASS ALSO REMAINS ABSTRACT
# =========================================================
"""
If a subclass does NOT implement all abstract methods,
it also becomes abstract
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        return "Car started"


# car = Car()  # ❌ Still abstract

"""
Explanation:
✔ stop() not implemented
✔ Car remains abstract
✔ Must implement ALL abstract methods
"""


# =========================================================
# COMPLETE REAL-WORLD EXAMPLE
# =========================================================
"""
Payment System using Abstract Classes
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    def receipt(self, amount):
        return f"Payment of ₹{amount} received"


class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"


class UPI(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using UPI"


payments = [CreditCard(), UPI()]

for p in payments:
    print(p.pay(500))
    print(p.receipt(500))

"""
Output:
-------
Paid ₹500 using Credit Card
Payment of ₹500 received
Paid ₹500 using UPI
Payment of ₹500 received

Explanation:
✔ Payment defines interface
✔ pay() behavior differs
✔ receipt() reused
"""


# =========================================================
# ABSTRACT CLASS VS INTERFACE (EXAM NOTE)
# =========================================================
"""
Python does NOT have interfaces like Java
Abstract Classes act as interfaces + base classes

Abstract Class:
✔ Can have concrete methods
✔ Can have instance variables
✔ Can enforce method implementation
"""


# =========================================================
# FINAL SUMMARY
# =========================================================
"""
ABSTRACT CLASSES SUMMARY
------------------------------------------------------------
✔ Cannot be instantiated
✔ Use abc module
✔ Use ABC and @abstractmethod
✔ Enforce consistent structure
✔ Allow flexible implementations
✔ Improve code quality and scalability

KEY RULE:
A class with even ONE abstract method
→ CANNOT be instantiated
"""

"""
END OF ABSTRACT CLASSES NOTES
===========================================================
"""
