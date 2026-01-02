"""
=========================================================
            OPERATOR OVERLOADING IN PYTHON
=========================================================

Operator Overloading allows the same operator to behave
differently depending on the operands.

Python supports operator overloading using special
methods (also called magic / dunder methods).

Examples:
+  -> __add__()
-  -> __sub__()
*  -> __mul__()
== -> __eq__()
<  -> __lt__()
>  -> __gt__()

NOTE:
✔ Built-in types already support operator overloading
✔ We CANNOT change behavior of built-in types globally
✔ We CAN overload operators for user-defined classes
"""

# =========================================================
# BUILT-IN OPERATOR OVERLOADING
# =========================================================
"""
Same operator behaves differently for built-in types
"""

print("\n--- Built-in Operator Overloading ---")

# + operator
print(1 + 2)                     # Integer addition
print("Geeks" + "For")           # String concatenation

# * operator
print(3 * 4)                     # Integer multiplication
print("Geeks" * 4)               # String repetition


# =========================================================
# OPERATOR OVERLOADING FOR USER-DEFINED TYPES
# =========================================================
"""
When we use operators on user-defined objects,
Python internally calls special methods.

obj1 + obj2  ->  obj1.__add__(obj2)
"""

class A:
    def __init__(self, a):
        self.a = a

    # Overloading +
    def __add__(self, other):
        return self.a + other.a


print("\n--- Overloading + Operator ---")

ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)     # Integer addition
print(ob3 + ob4)     # String concatenation

# Internal working
print(A.__add__(ob1, ob2))
print(ob1.__add__(ob2))


"""
Explanation:
ob1 + ob2
=> ob1.__add__(ob2)
=> self = ob1, other = ob2
"""


# =========================================================
# COMPLEX NUMBER ADDITION USING OPERATOR OVERLOADING
# =========================================================
"""
Adding complex numbers using + operator
"""

class Complex:
    def __init__(self, a, b):
        self.a = a    # real part
        self.b = b    # imaginary part

    def __add__(self, other):
        return self.a + other.a, self.b + other.b


print("\n--- Complex Number Addition ---")

Ob1 = Complex(1, 2)
Ob2 = Complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)   # (3, 5)


# =========================================================
# OVERLOADING COMPARISON OPERATORS
# =========================================================

# ---------- Overloading > ----------
class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        return self.a > other.a


print("\n--- Overloading > Operator ---")

ob1 = A(2)
ob2 = A(3)

if ob1 > ob2:
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")


# ---------- Overloading < and == ----------
class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return "ob1 is less than ob2" if self.a < other.a else "ob2 is less than ob1"

    def __eq__(self, other):
        return "Both are equal" if self.a == other.a else "Not equal"


print("\n--- Overloading < and == Operators ---")

ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob3 == ob4)


# =========================================================
# NON-ASSOCIATIVE OPERATORS
# =========================================================
"""
Some operators cannot be chained together.
Assignment operators (=, +=) are non-associative.
"""

a = 5
b = 10
c = 15

# INVALID (commented intentionally)
# a = b = (a < b) += (b < c)

"""
Explanation:
Assignment (=) and augmented assignment (+=)
cannot be used together in one expression.
"""


# =========================================================
# OVERLOADING BOOLEAN OPERATORS
# =========================================================
"""
Boolean operators can also be overloaded.

&  -> __and__()
|  -> __or__()
~  -> __invert__()
"""

class MyClass:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return MyClass(self.value and other.value)


print("\n--- Overloading Boolean AND (&) ---")

a = MyClass(True)
b = MyClass(False)
c = a & b

print(c.value)   # False


# =========================================================
# MAGIC METHODS REFERENCE (IMPORTANT FOR EXAMS)
# =========================================================
"""
BINARY OPERATORS
+   -> __add__(self, other)
-   -> __sub__(self, other)
*   -> __mul__(self, other)
/   -> __truediv__(self, other)
//  -> __floordiv__(self, other)
%   -> __mod__(self, other)
**  -> __pow__(self, other)

COMPARISON OPERATORS
<   -> __lt__(self, other)
>   -> __gt__(self, other)
<=  -> __le__(self, other)
>=  -> __ge__(self, other)
==  -> __eq__(self, other)
!=  -> __ne__(self, other)

ASSIGNMENT OPERATORS
+=  -> __iadd__(self, other)
-=  -> __isub__(self, other)
*=  -> __imul__(self, other)
/=  -> __itruediv__(self, other)
//= -> __ifloordiv__(self, other)
%=  -> __imod__(self, other)
**= -> __ipow__(self, other)

UNARY OPERATORS
-   -> __neg__(self)
+   -> __pos__(self)
~   -> __invert__(self)
"""


# =========================================================
# ADVANTAGES OF OPERATOR OVERLOADING
# =========================================================
"""
✔ Improves readability
✔ Makes code intuitive and natural
✔ Custom objects behave like built-in types
✔ Reduces boilerplate code
✔ Very useful in math, vectors, matrices, data structures

---------------------------------------------------------
ONE-LINE VIVA ANSWER
---------------------------------------------------------
Operator overloading allows operators to have different
meanings depending on the operands using magic methods.
"""
