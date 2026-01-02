"""
===========================================================
CLASS AND INSTANCE ATTRIBUTES IN PYTHON
===========================================================

In Python, attributes can belong either to:
1️⃣ The class itself (Class Attributes)
2️⃣ Individual objects (Instance Attributes)

Understanding the difference is crucial for OOP,
interviews, and real-world applications.
"""

# =========================================================
# CLASS ATTRIBUTES
# =========================================================
"""
Class Attributes:
✔ Belong to the class itself
✔ Shared among ALL instances of the class
✔ Defined inside the class body (outside methods)
✔ Usually placed at the top for readability
"""

class SampleClass:
    count = 0   # Class attribute

    def increase(self):
        # Modifying class attribute using class name
        SampleClass.count += 1


# Creating first object
s1 = SampleClass()
s1.increase()
print(s1.count)

# Creating second object
s2 = SampleClass()
s2.increase()
print(s2.count)

# Accessing class attribute directly via class
print(SampleClass.count)

"""
Output:
-------
1
2
2

Explanation:
✔ count is shared by all objects
✔ s1.increase() increments count to 1
✔ s2.increase() increments the SAME count to 2
✔ All objects and the class refer to a single copy
"""


# =========================================================
# IMPORTANT OBSERVATION
# =========================================================
"""
Even though we accessed count using s1.count and s2.count,
the attribute actually belongs to the class.

Best Practice:
✔ Modify class attributes using ClassName.attribute
✔ Avoid using self.attribute for class variables
"""


# =========================================================
# INSTANCE ATTRIBUTES
# =========================================================
"""
Instance Attributes:
✔ Belong to individual objects
✔ NOT shared between objects
✔ Created using self inside __init__()
✔ Each object has its own copy
"""

class Employee:
    def __init__(self):
        self.name = "xyz"     # Instance attribute
        self.salary = 4000   # Instance attribute

    def show(self):
        print(self.name)
        print(self.salary)


# Creating an object
e1 = Employee()

# vars() → shows instance attributes only
print("Dictionary form :", vars(e1))

# dir() → shows instance + class + inherited attributes
print(dir(e1))

"""
Output:
-------
Dictionary form : {'salary': 4000, 'name': 'xyz'}

['__doc__', '__init__', '__module__',
 'name', 'salary', 'show']

Explanation:
✔ vars(e1) returns only instance attributes
✔ dir(e1) returns:
   - instance attributes
   - class methods
   - inherited attributes
"""


# =========================================================
# DIFFERENCE BETWEEN vars() AND dir()
# =========================================================
"""
vars(object):
✔ Shows instance attributes only
✔ Returns a dictionary
✔ Very useful for debugging objects

dir(object):
✔ Shows everything accessible by the object
✔ Includes:
   - instance attributes
   - class attributes
   - methods
   - inherited attributes
"""


# =========================================================
# CLASS vs INSTANCE ATTRIBUTE SUMMARY
# =========================================================
"""
Feature                 Class Attribute       Instance Attribute
---------------------------------------------------------------
Defined In              Class body            __init__() method
Ownership               Class                 Individual object
Memory                  Single copy           Separate copy per object
Shared?                 Yes                   No
Accessed Using           ClassName.attr        object.attr
Modified Effect          Affects all objects   Affects one object only
"""


# =========================================================
# QUICK EXAM TIP
# =========================================================
"""
If you see SAME value across all objects → Class Attribute
If value differs per object → Instance Attribute

Viva Question:
Q: Where should constants be stored?
A: As class attributes
"""

"""
END OF CLASS AND INSTANCE ATTRIBUTES NOTES
===========================================================
"""
