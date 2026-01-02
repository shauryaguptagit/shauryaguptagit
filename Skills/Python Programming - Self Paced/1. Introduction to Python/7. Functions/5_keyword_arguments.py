"""
========================================
KEYWORD ARGUMENTS IN PYTHON
========================================

Overview:
---------
Keyword arguments allow passing values to a function
by explicitly specifying the parameter names.

This makes function calls:
✔ More readable
✔ Order-independent
✔ Less error-prone

Python supports two main types of arguments:
1. Positional Arguments
2. Keyword Arguments
"""

# ========================================
# POSITIONAL ARGUMENTS
# ========================================
"""
Positional arguments depend strictly on the order
in which values are passed.

The first value goes to the first parameter,
the second value to the second parameter, and so on.
"""

def printItem(id, name, price):
    print("Id is", id)
    print("Name is", name)
    print("Price is", price)

print("Using Positional Arguments:")
printItem(101, "abc", 100)


# ========================================
# KEYWORD ARGUMENTS
# ========================================
"""
Keyword arguments are passed using parameter names.
Order does NOT matter because Python matches
values with parameter names.
"""

print("\nUsing Keyword Arguments (Order Changed):")
printItem(id=102, price=200, name="xyz")

print("\nUsing Keyword Arguments (Different Order):")
printItem(name="abc", price=200, id=102)


"""
Output:
-------
Id is 101
Name is abc
Price is 100

Id is 102
Name is xyz
Price is 200

Id is 102
Name is abc
Price is 200
"""


# ========================================
# POSITIONAL vs KEYWORD ARGUMENTS
# ========================================
"""
Comparison:
-----------
Positional Arguments:
- Order matters
- Less readable
- More prone to mistakes

Keyword Arguments:
- Order does not matter
- Highly readable
- Safer for long parameter lists
"""


# ========================================
# MIXING POSITIONAL AND KEYWORD ARGUMENTS
# ========================================
"""
Rule:
-----
Positional arguments MUST come before keyword arguments.
"""

# Valid
print("\nValid Mixing:")
printItem(103, name="pqr", price=300)

# Invalid (uncomment to see error)
# printItem(id=104, "abc", 400)


# ========================================
# KEYWORD ARGUMENTS WITH DEFAULT PARAMETERS
# ========================================
"""
Important Rule:
---------------
All non-default parameters must appear before
default parameters in function definition.
"""

def product(id, name, price=0):
    print("Id:", id)
    print("Name:", name)
    print("Price:", price)

product(201, "Notebook")
product(202, "Pen", 20)
product(name="Pencil", id=203, price=10)


# ========================================
# ADVANTAGES OF KEYWORD ARGUMENTS
# ========================================
"""
1. Improves code readability
2. Order of arguments is not required
3. Reduces logical errors
4. Useful for functions with many parameters
5. Works very well with default arguments

Keyword arguments are widely used in:
✔ Python libraries
✔ Frameworks (Django, Flask)
✔ APIs
✔ Production-level code
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Positional arguments depend on order
2. Keyword arguments depend on parameter names
3. Keyword arguments improve clarity
4. Positional arguments must come before keyword arguments
5. Non-default parameters must be defined before default ones

Mastering keyword arguments is essential for:
✔ Clean code
✔ Interviews
✔ Real-world Python development
"""

"""
End of Keyword Arguments Module
--------------------------------
"""
