"""
=========================================================
                POLYMORPHISM IN PYTHON
=========================================================

Polymorphism means "many forms".

In Python, polymorphism refers to the ability of the SAME
method, function, or operator to behave DIFFERENTLY
depending on the object or context it is working with.

---------------------------------------------------------
WHY DO WE NEED POLYMORPHISM?
---------------------------------------------------------
✔ Ensures consistent interfaces across different classes
✔ Allows objects to respond differently to the same method
✔ Promotes loose coupling (focus on behavior, not type)
✔ Enables flexible and reusable code
✔ Simplifies testing and future code extension

---------------------------------------------------------
REAL LIFE EXAMPLE
---------------------------------------------------------
A remote control has one "power" button.
- TV → turns on display
- AC → starts cooling
- Music system → plays music

Same interface, different behavior → POLYMORPHISM
"""

# =========================================================
# TYPES OF POLYMORPHISM IN PYTHON
# =========================================================
"""
1. Compile-time Polymorphism (Not truly supported in Python)
2. Runtime Polymorphism (Method Overriding)
"""

# =========================================================
# 1. COMPILE-TIME POLYMORPHISM (SIMULATED)
# =========================================================
"""
Compile-time polymorphism means method behavior is decided
at compilation time (method overloading).

Python DOES NOT support true method overloading because:
- Python is dynamically typed
- Method calls are resolved at runtime

However, we can SIMULATE it using:
✔ Default arguments
✔ Variable-length arguments (*args)
"""

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

print("\n--- Compile-time Polymorphism (Simulated) ---")
calc = Calculator()

# Using default arguments
print(calc.multiply())          # 1
print(calc.multiply(4))         # 4

# Using multiple arguments
print(calc.multiply(2, 3))      # 6
print(calc.multiply(2, 3, 4))   # 24


# =========================================================
# 2. RUNTIME POLYMORPHISM (METHOD OVERRIDING)
# =========================================================
"""
Runtime polymorphism means method behavior is decided
WHILE the program is running.

Achieved using:
✔ Method Overriding
✔ Inheritance

Child class provides its own implementation
of a method already defined in parent class.
"""

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

print("\n--- Runtime Polymorphism (Method Overriding) ---")
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.sound())

"""
Explanation:
- Same method name: sound()
- Different behavior based on object type
- Decision happens at RUNTIME
"""


# =========================================================
# POLYMORPHISM IN BUILT-IN FUNCTIONS
# =========================================================
"""
Python built-in functions are polymorphic.

Same function name behaves differently
based on input type.
"""

print("\n--- Polymorphism in Built-in Functions ---")

# len() behaves differently
print(len("Hello"))        # String length
print(len([1, 2, 3]))      # List length

# max() behaves differently
print(max(1, 3, 2))        # Integers
print(max("a", "z", "m"))  # Strings


# =========================================================
# POLYMORPHISM USING FUNCTIONS (DUCK TYPING)
# =========================================================
"""
Duck Typing principle:
"If it looks like a duck and quacks like a duck,
it is a duck."

Python does NOT care about object type,
only whether it has the required method.
"""

class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

print("\n--- Polymorphism using Duck Typing ---")
perform_task(Pen())
perform_task(Eraser())

"""
Explanation:
- perform_task() does not care about class type
- As long as object has use() method, it works
"""


# =========================================================
# POLYMORPHISM IN OPERATORS (OPERATOR OVERLOADING)
# =========================================================
"""
Same operator behaves differently
based on operand types.

This is called OPERATOR POLYMORPHISM.
"""

print("\n--- Operator Polymorphism ---")

print(5 + 10)                    # Integer addition
print("Hello " + "World!")       # String concatenation
print([1, 2] + [3, 4])           # List concatenation


"""
---------------------------------------------------------
IMPORTANT EXAM SUMMARY
---------------------------------------------------------

✔ Polymorphism = same interface, different behavior
✔ Python supports RUNTIME polymorphism naturally
✔ Method overriding enables runtime polymorphism
✔ Python does NOT support true compile-time polymorphism
✔ Duck typing enables flexible function polymorphism
✔ Built-in functions like len(), max() are polymorphic
✔ Operators like + behave differently for different types

---------------------------------------------------------
ONE-LINE DEFINITION (VIVA)
---------------------------------------------------------
Polymorphism allows the same method or operation to behave
differently depending on the object or data type.
"""
