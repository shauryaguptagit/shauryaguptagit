"""
===========================================================
ACCESS MODIFIERS IN PYTHON
Public, Protected and Private
===========================================================

Access modifiers control how class members (variables and methods)
can be accessed:
✔ from outside the class
✔ inside the class
✔ inside subclasses

Python supports access control using NAMING CONVENTIONS,
not strict enforcement (unlike Java/C++).
"""

# =========================================================
# 1. PUBLIC ACCESS MODIFIER
# =========================================================
"""
Public Members:
✔ Accessible from anywhere
✔ Default access level in Python
✔ No underscore prefix
"""

class Geek:
    def __init__(self, name, age):
        self.geekName = name      # Public variable
        self.geekAge = age        # Public variable

    def displayAge(self):        # Public method
        print("Age:", self.geekAge)


# Object creation
obj = Geek("R2J", 20)

# Accessing public members
print("Name:", obj.geekName)
obj.displayAge()

"""
Output:
-------
Name: R2J
Age: 20

Explanation:
✔ geekName and geekAge are public
✔ Can be accessed directly using object
✔ displayAge() is also public
✔ All members appear in dir(obj)
"""


# =========================================================
# 2. PROTECTED ACCESS MODIFIER
# =========================================================
"""
Protected Members:
✔ Start with single underscore (_)
✔ Convention-based protection
✔ Intended for use inside class & subclasses
✔ Still accessible directly (not enforced)
"""

class Student:
    def __init__(self, name, roll, branch):
        self._name = name          # Protected variable
        self._roll = roll
        self._branch = branch

    def _displayRollAndBranch(self):   # Protected method
        print("Roll:", self._roll)
        print("Branch:", self._branch)


class GeekStudent(Student):
    def displayDetails(self):
        print("Name:", self._name)          # Accessing protected member
        self._displayRollAndBranch()        # Accessing protected method


# Object creation
obj = GeekStudent("R2J", 1706256, "IT")
obj.displayDetails()

"""
Output:
-------
Name: R2J
Roll: 1706256
Branch: IT

Explanation:
✔ _name, _roll, _branch are protected
✔ Subclass can access protected members
✔ Direct access is allowed but discouraged
"""


# =========================================================
# 3. PRIVATE ACCESS MODIFIER
# =========================================================
"""
Private Members:
✔ Start with double underscore (__)
✔ Name Mangling is applied
✔ __var becomes _ClassName__var internally
✔ Prevents accidental access, not absolute security
"""

class GeekPrivate:
    def __init__(self, name, roll, branch):
        self.__name = name         # Private variable
        self.__roll = roll
        self.__branch = branch

    def __displayDetails(self):    # Private method
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    def accessPrivateFunction(self):
        # Allowed inside class
        self.__displayDetails()


obj = GeekPrivate("R2J", 1706256, "CSE")

# Accessing private data indirectly
obj.accessPrivateFunction()

# Access using name mangling
print(obj._GeekPrivate__name)

"""
Output:
-------
Name: R2J
Roll: 1706256
Branch: CSE
R2J

Explanation:
✔ Direct access: obj.__name ❌ AttributeError
✔ Name mangling: _ClassName__variable ✔
✔ Private methods callable only inside class
"""


# =========================================================
# COMBINED EXAMPLE: ALL ACCESS MODIFIERS
# =========================================================
"""
This example shows:
✔ Public access
✔ Protected access via subclass
✔ Private access via class method & name mangling
"""

class Super:
    publicData = "Public Data Member"
    _protectedData = "Protected Data Member"
    __privateData = "Private Data Member"

    def accessPrivateMembers(self):
        print("Accessing inside class:", self.__privateData)


class Sub(Super):
    def accessProtectedMembers(self):
        print("Accessing inside subclass:", self._protectedData)


obj = Sub()

# Public → Direct Access
print(obj.publicData)

# Protected → Accessible but discouraged
print(obj._protectedData)

# Private → Not directly accessible
# print(obj.__privateData)  # AttributeError

# Access private inside class
obj.accessPrivateMembers()

# Access private using name mangling
print(obj._Super__privateData)

"""
Output:
-------
Public Data Member
Protected Data Member
Accessing inside class: Private Data Member
Private Data Member
"""


# =========================================================
# FINAL SUMMARY TABLE
# =========================================================
"""
Access Modifier   Syntax           Accessibility
-------------------------------------------------
Public            variable         Everywhere
Protected         _variable        Class + Subclass (convention)
Private           __variable       Class only (name mangling)

IMPORTANT:
✔ Python uses conventions, not strict access control
✔ Private members can still be accessed using name mangling
"""


# =========================================================
# EXAM / VIVA QUICK POINTS
# =========================================================
"""
✔ Default access modifier in Python → Public
✔ Protected uses single underscore (_)
✔ Private uses double underscore (__)
✔ Python does NOT enforce strict privacy
✔ Name mangling prevents accidental override
"""

"""
END OF ACCESS MODIFIERS NOTES
===========================================================
"""
