"""
========================================
PARAMETER PASSING IN PYTHON
========================================

Overview:
---------
Understanding how parameters are passed to functions in Python
is crucial, especially when working with mutable and immutable
data types.

Python does NOT strictly follow:
- Pass by Value
- Pass by Reference

Instead, Python uses:
✔ Pass by Object Reference (or Pass by Assignment)

This means:
- The reference to an object is passed
- Behavior depends on whether the object is mutable or immutable
"""

# ========================================
# BASICS OF PARAMETER PASSING
# ========================================
"""
When a variable is passed to a function:
- Both the caller and the function parameter
  initially refer to the SAME object

What happens next depends on:
1. Reassignment (new object created)
2. Modification (same object changed)
"""


# ========================================
# EXAMPLE 1: IMMUTABLE DATA TYPE (INTEGER)
# ========================================

x = 10

def fun(x):
    x = 15   # Reassignment (new object)
    
fun(x)
print(x)

"""
Output:
-------
10
"""

"""
Explanation:
------------
- x = 10 (immutable integer)
- Inside fun(), x is reassigned to 15
- A NEW object is created
- Original x outside remains unchanged
"""


# ========================================
# EXAMPLE 2: MUTABLE DATA TYPE (LIST)
# ========================================

l = [10, 20, 30]

def fun(l):
    l.append(15)   # Modification of same object
    
fun(l)
print(l)

"""
Output:
-------
[10, 20, 30, 15]
"""

"""
Explanation:
------------
- l refers to a list object
- append() modifies the SAME object
- Change is reflected outside the function
"""


# ========================================
# IMMUTABLE EXAMPLE: STEP-BY-STEP ANALYSIS
# ========================================
"""
1. x is assigned value 10
2. fun(x) is called
3. Inside function, x = 15 creates a new local reference
4. Original x outside the function is unchanged
"""


# ========================================
# MUTABLE EXAMPLE: STEP-BY-STEP ANALYSIS
# ========================================
"""
1. l is assigned a list [10, 20, 30]
2. fun(l) is called
3. append() modifies the existing list
4. Change is visible outside the function
"""


# ========================================
# USING id() TO UNDERSTAND OBJECT IDENTITY
# ========================================
"""
id() returns the unique identity of an object in memory
"""


# ---------- IMMUTABLE WITH id() ----------
x = 10

def fun(x):
    print("Local x before reassignment:", id(x))
    x = 15
    print("Local x after reassignment :", id(x))

print("Global x before function    :", id(x))
fun(x)
print("Global x after function     :", id(x))

"""
Observation:
------------
- Global x ID remains same
- Local x points to a new object after reassignment
"""


# ---------- MUTABLE WITH id() ----------
l = [10, 20, 30]

def fun(l):
    print("Local l before modification:", id(l))
    l.append(15)
    print("Local l after modification :", id(l))

print("Global l before function   :", id(l))
fun(l)
print("Global l after function    :", id(l))

"""
Observation:
------------
- Same ID before and after modification
- Local and global refer to the same object
"""


# ========================================
# MODIFYING vs REASSIGNING
# ========================================
"""
Key Difference:
---------------
MODIFYING:
- Changes the object itself
- Affects original object (mutable types)

REASSIGNING:
- Creates a new object reference
- Does NOT affect original object
"""


# ========================================
# REASSIGNMENT WITH MUTABLE TYPE
# ========================================

def fun(l):
    l = [40, 50]   # Reassignment to new list
    print("Inside function:", l)

l = [10, 20, 30]
fun(l)
print("Outside function:", l)

"""
Output:
-------
Inside function: [40, 50]
Outside function: [10, 20, 30]
"""

"""
Explanation:
------------
- l inside function is reassigned
- New list object is created
- Original list outside remains unchanged
"""


# ========================================
# FINAL CONCLUSION
# ========================================
"""
Python Parameter Passing Summary:
---------------------------------
✔ Python uses Pass-by-Object-Reference
✔ Mutable objects can be modified inside functions
✔ Immutable objects cannot be changed, only reassigned
✔ Reassignment never affects the original object
✔ Modification affects the original object (if mutable)

Common Interview Line:
----------------------
"Python is neither pass-by-value nor pass-by-reference,
it is pass-by-object-reference."

Understanding this concept is CRITICAL for:
✔ Debugging
✔ Writing safe functions
✔ Interview questions
✔ Real-world Python development
"""

"""
End of Parameter Passing Module
--------------------------------
"""
