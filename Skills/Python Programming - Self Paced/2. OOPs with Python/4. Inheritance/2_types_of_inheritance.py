"""
=====================================================
        TYPES OF INHERITANCE IN PYTHON
=====================================================

Inheritance is a core concept of Object-Oriented Programming (OOP)
that allows a child (derived) class to inherit properties and methods
from a parent (base) class.

Benefits of Inheritance:
- Code reusability
- Better maintainability
- Logical hierarchy
- Extensibility of programs

Types of inheritance in Python depend on the number of parent
and child classes involved.

Python supports the following types of inheritance:
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
"""

# =====================================================
# 1. SINGLE INHERITANCE
# =====================================================
"""
Single Inheritance:
A child class inherits from exactly ONE parent class.
The child can access parent methods and also define its own.

Structure:
Parent  --->  Child
"""

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

# Driver code
print("\n--- Single Inheritance ---")
obj = Child()
obj.func1()   # inherited from Parent
obj.func2()   # own method


# =====================================================
# 2. MULTIPLE INHERITANCE
# =====================================================
"""
Multiple Inheritance:
A child class inherits from MORE THAN ONE parent class.

Structure:
Parent1 + Parent2  --->  Child

Python resolves conflicts using MRO (Method Resolution Order).
"""

# Base class 1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver code
print("\n--- Multiple Inheritance ---")
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()


# =====================================================
# 3. MULTILEVEL INHERITANCE
# =====================================================
"""
Multilevel Inheritance:
A class is derived from another derived class.
Forms a chain-like structure.

Structure:
Grandparent ---> Parent ---> Child
"""

# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print("Grandfather name :", self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

# Driver code
print("\n--- Multilevel Inheritance ---")
s1 = Son("Prince", "Rampal", "Lal Mani")
s1.print_name()


# =====================================================
# 4. HIERARCHICAL INHERITANCE
# =====================================================
"""
Hierarchical Inheritance:
More than one child class inherits from the SAME parent class.

Structure:
        Parent
        /    \
    Child1  Child2
"""

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
print("\n--- Hierarchical Inheritance ---")
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()

object2.func1()
object2.func3()


# =====================================================
# 5. HYBRID INHERITANCE
# =====================================================
"""
Hybrid Inheritance:
Combination of two or more types of inheritance.
Often includes multiple + multilevel inheritance.

Python handles ambiguity using MRO.
"""

# Base class
class School:
    def func1(self):
        print("This function is in school.")

# Derived class (Single Inheritance)
class Student1(School):
    def func2(self):
        print("This function is in student 1.")

# Another derived class
class Student2(School):
    def func3(self):
        print("This function is in student 2.")

# Derived class (Multiple + Single = Hybrid)
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Driver code
print("\n--- Hybrid Inheritance ---")
obj = Student3()
obj.func1()
obj.func2()

"""
=====================================================
SUMMARY (Exam-Friendly)
=====================================================

Single Inheritance:
- One parent → one child

Multiple Inheritance:
- Multiple parents → one child

Multilevel Inheritance:
- Chain inheritance (A → B → C)

Hierarchical Inheritance:
- One parent → multiple children

Hybrid Inheritance:
- Combination of multiple inheritance types

Python uses MRO (Method Resolution Order) to resolve conflicts.
"""
