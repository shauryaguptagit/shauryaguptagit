"""
===========================================================
ENCAPSULATION IN PYTHON
===========================================================

Encapsulation means:
✔ Hiding internal data of a class
✔ Allowing access only through controlled methods
✔ Protecting data from accidental or unauthorized modification

In Python, encapsulation is achieved using:
✔ Access modifiers (public, protected, private)
✔ Getter and Setter methods
✔ Name mangling (__variable)
"""

# =========================================================
# BASIC EXAMPLE OF ENCAPSULATION
# =========================================================
"""
Private data cannot be accessed directly from outside the class.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public attribute
        self.__salary = salary    # Private attribute


emp = Employee("Fedrick", 50000)

print(emp.name)       # Public → Accessible

# print(emp.__salary)  # ❌ AttributeError (private attribute)

"""
Output:
-------
Fedrick

Explanation:
✔ name is public → accessible directly
✔ __salary is private → hidden using name mangling
"""


# =========================================================
# WHY DO WE NEED ENCAPSULATION?
# =========================================================
"""
✔ Protects sensitive data
✔ Prevents accidental modification
✔ Adds validation before updating data
✔ Improves modularity and maintainability
✔ Reflects real-world access control (bank balance, salary, etc.)
"""


# =========================================================
# ACCESS SPECIFIERS IN PYTHON
# =========================================================
"""
Python supports 3 access levels using naming conventions:
1. Public
2. Protected
3. Private
"""


# =========================================================
# 1. PUBLIC MEMBERS
# =========================================================
"""
✔ Accessible everywhere
✔ Default access level in Python
✔ No underscore prefix
"""

class EmployeePublic:
    def __init__(self, name):
        self.name = name   # Public attribute

    def display_name(self):   # Public method
        print(self.name)


emp = EmployeePublic("John")
emp.display_name()
print(emp.name)

"""
Output:
-------
John
John

Explanation:
✔ Public members can be accessed from anywhere
✔ __init__ runs automatically during object creation
"""


# =========================================================
# 2. PROTECTED MEMBERS
# =========================================================
"""
✔ Intended for class and subclasses
✔ Single underscore prefix (_)
✔ Convention-based (not enforced)
"""

class EmployeeProtected:
    def __init__(self, name, age):
        self.name = name      # Public
        self._age = age       # Protected


class SubEmployee(EmployeeProtected):
    def show_age(self):
        print("Age:", self._age)   # Accessing protected member


emp = SubEmployee("Ross", 30)
print(emp.name)
emp.show_age()

"""
Output:
-------
Ross
Age: 30

Explanation:
✔ _age is protected
✔ Accessible inside subclass
✔ Direct external access is discouraged but allowed
"""


# =========================================================
# 3. PRIVATE MEMBERS
# =========================================================
"""
✔ Not accessible directly outside the class
✔ Double underscore prefix (__)
✔ Name mangling applied: __var → _ClassName__var
"""

class EmployeePrivate:
    def __init__(self, name, salary):
        self.name = name          # Public
        self.__salary = salary    # Private

    def show_salary(self):
        print("Salary:", self.__salary)


emp = EmployeePrivate("Robert", 60000)
print(emp.name)
emp.show_salary()

# print(emp.__salary)  # ❌ AttributeError

"""
Output:
-------
Robert
Salary: 60000

Explanation:
✔ __salary is private
✔ Access allowed only inside class
✔ Name mangling prevents direct access
"""


# =========================================================
# PROTECTED AND PRIVATE METHODS
# =========================================================
"""
Methods can also be protected or private.
✔ _method → protected
✔ __method → private
"""

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):          # Protected method
        print(f"Balance: ₹{self.balance}")

    def __update_balance(self, amount):  # Private method
        self.balance += amount

    def deposit(self, amount):        # Public method
        if amount > 0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print("Invalid deposit amount!")


account = BankAccount()
account._show_balance()     # Allowed, but discouraged
account.deposit(500)

"""
Output:
-------
Balance: ₹1000
Balance: ₹1500

Explanation:
✔ _show_balance → intended for internal use
✔ __update_balance → accessible only inside class
✔ deposit() controls access safely
"""


# =========================================================
# GETTER AND SETTER METHODS
# =========================================================
"""
Getter → Read private data
Setter → Update private data with validation
"""

class EmployeeGS:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):     # Getter
        return self.__salary

    def set_salary(self, amount):  # Setter
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")


emp = EmployeeGS()
print(emp.get_salary())

emp.set_salary(60000)
print(emp.get_salary())

"""
Output:
-------
50000
60000

Explanation:
✔ Private data never accessed directly
✔ Validation logic inside setter
✔ Safe and controlled data modification
"""


# =========================================================
# FINAL SUMMARY
# =========================================================
"""
Encapsulation Summary:
------------------------------------------------------------
Public     → No underscore → Accessible everywhere
Protected  → _variable     → Class + subclass (convention)
Private    → __variable    → Class only (name mangling)

IMPORTANT POINTS:
✔ Python does NOT enforce strict access control
✔ Uses naming conventions + name mangling
✔ Getter & Setter provide controlled access
✔ Core pillar of Object-Oriented Programming
"""

"""
END OF ENCAPSULATION NOTES
===========================================================
"""
