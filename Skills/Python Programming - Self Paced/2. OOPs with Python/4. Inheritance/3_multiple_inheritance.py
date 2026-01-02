"""
=========================================================
            MULTIPLE INHERITANCE IN PYTHON
=========================================================

When a class inherits from MORE THAN ONE base class,
it is called Multiple Inheritance.

The derived (child) class inherits all attributes
and methods of its base (parent) classes.

---------------------------------------------------------
SYNTAX
---------------------------------------------------------

class Base1:
    pass

class Base2:
    pass

class Derived(Base1, Base2):
    pass
"""

# =========================================================
# BASIC MULTIPLE INHERITANCE EXAMPLE
# =========================================================

class Base1:
    def show1(self):
        print("Method from Base1")

class Base2:
    def show2(self):
        print("Method from Base2")

class Derived(Base1, Base2):
    def show(self):
        print("Method from Derived")

print("\n--- Basic Multiple Inheritance ---")
d = Derived()
d.show1()
d.show2()
d.show()


# =========================================================
# THE DIAMOND PROBLEM
# =========================================================
"""
Diamond Problem occurs when:

        Class1
        /    \
    Class2  Class3
        \    /
        Class4

- Class2 and Class3 inherit from Class1
- Class4 inherits from both Class2 and Class3
- If Class2 and Class3 override the same method,
  ambiguity arises.

Python solves this using:
👉 Method Resolution Order (MRO)
👉 C3 Linearization Algorithm
"""

# =========================================================
# METHOD RESOLUTION ORDER (MRO)
# =========================================================
"""
MRO defines the order in which Python searches for methods.

Rules:
- Current class is checked first
- Parents are searched LEFT to RIGHT
- Each class is visited only once

Ways to view MRO:
1. Class.mro()      → list
2. Class.__mro__    → tuple
"""

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        super().m()

print("\n--- MRO Demonstration ---")
print(Class4.mro())
print(Class4.__mro__)

obj = Class4()
obj.m()


# =========================================================
# EXAMPLE 1: Method overridden in BOTH parent classes
# =========================================================
"""
According to MRO:
Class4 → Class2 → Class3 → Class1

So Class2.m() is executed first
"""

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    pass

print("\n--- Example 1: Overridden in both parents ---")
obj = Class4()
obj.m()   # Class2.m() is called


# =========================================================
# EXAMPLE 2: Method overridden in ONLY ONE parent
# =========================================================
"""
Class2 does NOT override m()
Class3 overrides m()

MRO finds Class3.m()
"""

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    pass

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    pass

print("\n--- Example 2: Overridden in one parent ---")
obj = Class4()
obj.m()


# =========================================================
# EXAMPLE 3: ALL classes define same method
# =========================================================
"""
- Class4 overrides m()
- Parent methods can still be called explicitly
"""

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")

print("\n--- Example 3: All classes override method ---")
obj = Class4()
obj.m()
Class2.m(obj)
Class3.m(obj)
Class1.m(obj)


# =========================================================
# EXAMPLE 4: Explicit parent method calls (BAD PRACTICE)
# =========================================================
"""
Calling parent methods directly may cause:
- Duplicate calls
- Hard-to-maintain code
"""

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)

class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)

print("\n--- Example 4: Explicit calls ---")
obj = Class4()
obj.m()


# =========================================================
# SUPER() FUNCTION IN MULTIPLE INHERITANCE
# =========================================================
"""
super() is the RECOMMENDED way to handle multiple inheritance.

Advantages:
- Avoids duplicate method calls
- Automatically follows MRO
- Cleaner and safer than explicit calls
"""

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        super().m()

print("\n--- Using super() correctly ---")
obj = Class4()
obj.m()

"""
---------------------------------------------------------
SUMMARY (VERY IMPORTANT FOR EXAMS & VIVA)
---------------------------------------------------------

✔ Multiple inheritance allows a class to inherit from multiple parents
✔ Diamond Problem is resolved using MRO
✔ Python uses C3 Linearization for MRO
✔ super() ensures each method is called ONCE
✔ Avoid explicit parent calls in multiple inheritance
✔ MRO order is LEFT to RIGHT

MRO Example:
Class4 → Class2 → Class3 → Class1 → object
"""
