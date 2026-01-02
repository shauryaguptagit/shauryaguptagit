"""
=========================================================
        MORE EXAMPLES OF POLYMORPHISM IN PYTHON
=========================================================

Polymorphism allows objects of different classes
to be treated as objects of a common type.

The key idea:
✔ Same method / function / operator name
✔ Different behavior depending on the object

---------------------------------------------------------
FOCUS OF THIS FILE
---------------------------------------------------------
✔ Method Overriding with Inheritance
✔ Polymorphism using a list of objects
✔ Polymorphism with unrelated classes (Duck Typing)
✔ Polymorphism in built-in functions
✔ Polymorphism in operators
"""

# =========================================================
# METHOD OVERRIDING (WITH INHERITANCE)
# =========================================================
"""
Method Overriding occurs when:
- A child class defines a method
- With SAME name and parameters
- As a method in its parent class

The child method overrides the parent method.
"""

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printDetails(self):
        print(self.id)
        print(self.name)


class SalesEmployee(Employee):
    def __init__(self, id, name, sales_incentive):
        super().__init__(id, name)
        self.salesInc = sales_incentive

    # Overriding parent method
    def printDetails(self):
        super().printDetails()
        print(self.salesInc)


print("\n--- Method Overriding Example ---")

# List containing objects of different classes
el = [
    Employee(101, "Sandup"),
    SalesEmployee(102, "Rahul", 5000)
]

# Polymorphic behavior
for x in el:
    x.printDetails()

"""
Explanation:
- Same method call: printDetails()
- Different behavior based on object type
- Decision happens at runtime
- This is Runtime Polymorphism
"""


# =========================================================
# POLYMORPHISM WITH UNRELATED CLASSES
# =========================================================
"""
Polymorphism does NOT require inheritance.

As long as objects have the same method name,
Python allows polymorphic behavior.
(This is Duck Typing)
"""

class Employee:
    def fun(self):
        print("fun() in Employee")

class Customer:
    def fun(self):
        print("fun() in Customer")

print("\n--- Polymorphism with Unrelated Classes ---")

l = [Employee(), Customer()]

for x in l:
    x.fun()

"""
Explanation:
- Employee and Customer are unrelated classes
- Both define fun()
- Python decides method at runtime
- Type of object matters, not class relationship
"""


# =========================================================
# POLYMORPHIC BUILT-IN FUNCTIONS
# =========================================================
"""
Python built-in functions are polymorphic.

They behave differently depending on input type.
"""

print("\n--- Polymorphic Built-in Functions ---")

# len() behaves differently
print(len("gfg"))                 # Length of string
print(len([10, 20, 30, 40]))      # Length of list

# Other polymorphic built-ins
print(type(10))                   # Type of integer
print(type("Python"))             # Type of string
print(id(100))                    # Memory identity


# =========================================================
# POLYMORPHIC OPERATORS
# =========================================================
"""
Operators in Python are also polymorphic.

Same operator symbol, different behavior
based on operand types.
"""

print("\n--- Polymorphic Operators ---")

# + operator
print(3 + 2)                      # Integer addition
print("geeks" + "for" + "geeks")  # String concatenation

# Comparison operators
print(10 <= 100)                  # Integer comparison
print("geeks" < "for")            # String comparison

# * operator
print(3 * 2)                      # Integer multiplication
print("geeks" * 2)                # String repetition


"""
---------------------------------------------------------
IMPORTANT EXAM POINTS
---------------------------------------------------------

✔ Method overriding enables runtime polymorphism
✔ Polymorphism works through inheritance AND duck typing
✔ Lists can hold objects of different classes
✔ Same method call behaves differently at runtime
✔ Built-in functions like len(), type(), id() are polymorphic
✔ Operators like +, *, < behave differently by data type

---------------------------------------------------------
ONE-LINE VIVA ANSWER
---------------------------------------------------------
Polymorphism allows the same method or operator to perform
different actions depending on the object or data type.
"""
