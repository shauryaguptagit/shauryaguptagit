"""
===========================================================
DATA ABSTRACTION IN PYTHON
===========================================================

Data Abstraction means:
✔ Showing only essential features
✔ Hiding complex internal implementation details

In Python, abstraction is achieved using:
✔ Abstract Base Classes (ABC)
✔ @abstractmethod decorator
✔ abc module

Goal:
User should focus on WHAT an object does,
not HOW it does it.
"""


# =========================================================
# REAL LIFE EXAMPLE (CONCEPT)
# =========================================================
"""
Smartphone Abstraction:
✔ You make calls, take photos
✔ You don't know how signals or hardware work

Same idea in programming:
✔ Expose necessary methods
✔ Hide internal logic
"""


# =========================================================
# WHY DO WE NEED DATA ABSTRACTION?
# =========================================================
"""
✔ Simplifies usage of complex systems
✔ Protects internal logic
✔ Reduces accidental misuse
✔ Improves maintainability
✔ Allows internal changes without affecting users
"""


# =========================================================
# ABSTRACT BASE CLASS (ABC)
# =========================================================
"""
Abstract Base Class:
✔ Acts as a blueprint
✔ Cannot be instantiated
✔ Forces subclasses to implement required methods
"""

from abc import ABC, abstractmethod


class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass   # Abstract method (no implementation)


class English(Greet):
    def say_hello(self):
        return "Hello!"


g = English()
print(g.say_hello())

"""
Output:
-------
Hello!

Explanation:
✔ Greet is abstract → cannot be instantiated
✔ English implements abstract method
✔ Structure enforced, behavior customizable
"""


# =========================================================
# COMPONENTS OF DATA ABSTRACTION
# =========================================================
"""
Main components:
1. Abstract Methods
2. Concrete Methods
3. Abstract Properties
4. Abstract Class Instantiation Rules
"""


# =========================================================
# 1. ABSTRACT METHOD
# =========================================================
"""
Abstract Method:
✔ Declared but not implemented
✔ Forces subclasses to provide implementation
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass   # No implementation


"""
Explanation:
✔ make_sound() has no body
✔ Any subclass MUST implement it
"""


# =========================================================
# 2. CONCRETE METHOD
# =========================================================
"""
Concrete Method:
✔ Fully implemented method
✔ Can exist inside abstract class
✔ Can be reused by subclasses
"""

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return "Moving"


class Dog(Animal):
    def make_sound(self):
        return "Bark"


dog = Dog()
print(dog.make_sound())
print(dog.move())

"""
Output:
-------
Bark
Moving

Explanation:
✔ make_sound() → implemented by subclass
✔ move() → inherited directly
✔ Code reuse + enforced structure
"""


# =========================================================
# 3. ABSTRACT PROPERTIES
# =========================================================
"""
Abstract Properties:
✔ Used when property must be implemented
✔ Declared using @property + @abstractmethod
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
✔ species is an abstract property
✔ Dog must implement it
✔ Enforces property implementation
"""


# =========================================================
# 4. ABSTRACT CLASS INSTANTIATION
# =========================================================
"""
Abstract classes CANNOT be instantiated
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# animal = Animal()  # ❌ TypeError

"""
Explanation:
✔ Animal has abstract method
✔ Python prevents object creation
✔ Only fully implemented subclasses allowed
"""


# =========================================================
# COMPLETE REAL-WORLD EXAMPLE
# =========================================================
"""
Vehicle System using Abstraction
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def fuel_type(self):
        return "Petrol/Diesel"


class Car(Vehicle):
    def start(self):
        return "Car engine started"


class Bike(Vehicle):
    def start(self):
        return "Bike engine started"


vehicles = [Car(), Bike()]

for v in vehicles:
    print(v.start())
    print(v.fuel_type())

"""
Output:
-------
Car engine started
Petrol/Diesel
Bike engine started
Petrol/Diesel

Explanation:
✔ Vehicle defines common interface
✔ start() behavior differs
✔ fuel_type() reused
"""


# =========================================================
# DIFFERENCE: ABSTRACTION vs ENCAPSULATION
# =========================================================
"""
Abstraction:
✔ Hides implementation
✔ Focuses on WHAT to do
✔ Achieved using abstract classes

Encapsulation:
✔ Hides data
✔ Focuses on HOW data is protected
✔ Achieved using access modifiers
"""


# =========================================================
# FINAL SUMMARY
# =========================================================
"""
DATA ABSTRACTION SUMMARY
------------------------------------------------------------
✔ Uses abc module
✔ Abstract methods enforce structure
✔ Concrete methods provide reuse
✔ Abstract properties enforce attributes
✔ Abstract classes cannot be instantiated
✔ Improves scalability and maintainability

CORE IDEA:
"Design first, implement later"
"""

"""
END OF DATA ABSTRACTION NOTES
===========================================================
"""
