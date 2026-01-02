"""
========================================
GLOBAL AND LOCAL VARIABLES IN PYTHON
========================================

Overview:
---------
Variables in Python can be classified based on where
they are defined and where they can be accessed.

Two main types:
1. Local Variables
2. Global Variables

Understanding scope is essential for:
✔ Writing correct programs
✔ Avoiding unexpected bugs
✔ Interview questions
"""

# ========================================
# LOCAL VARIABLES
# ========================================
"""
Local variables are defined INSIDE a function.
They exist only during the execution of that function.
They cannot be accessed outside the function.
"""

# ---------- Example 1: Local variable inside function ----------

def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()

"""
Output:
-------
Hello from inside the function!
"""

"""
Explanation:
------------
- msg is created inside greet()
- It exists only while the function is executing
"""


# ---------- Example 2: Accessing local variable outside ----------

def greet():
    msg = "Hello!"
    print("Inside function:", msg)

greet()

# Uncommenting below line will cause an error
# print("Outside function:", msg)

"""
Error:
------
NameError: name 'msg' is not defined

Explanation:
------------
- msg is local to greet()
- It does not exist outside the function
"""


# ========================================
# GLOBAL VARIABLES
# ========================================
"""
Global variables are defined OUTSIDE all functions.
They can be accessed anywhere in the program,
including inside functions.
"""

msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)

"""
Output:
-------
Inside function: Python is awesome!
Outside function: Python is awesome!
"""

"""
Explanation:
------------
- msg is defined in global scope
- Accessible both inside and outside functions
"""


# ========================================
# LOCAL SHADOWING GLOBAL VARIABLES
# ========================================
"""
If a local variable has the SAME NAME as a global variable,
the local variable SHADOWS the global variable
inside the function.
"""

def fun():
    s = "Me too."   # Local variable
    print(s)

s = "I love Geeksforgeeks"   # Global variable

fun()
print(s)

"""
Output:
-------
Me too.
I love Geeksforgeeks
"""

"""
Explanation:
------------
- Inside fun(), local s is used
- Global s remains unchanged
"""


# ========================================
# MODIFYING GLOBAL VARIABLES INSIDE FUNCTION
# ========================================
"""
By default, Python does NOT allow modifying a global variable
inside a function unless declared using the 'global' keyword.
"""

# ---------- Without global keyword (Error) ----------

def fun():
    # s += " GFG"   # Uncommenting causes error
    pass

s = "I love GeeksforGeeks"
# fun()

"""
Error:
------
UnboundLocalError: local variable 's' referenced before assignment

Explanation:
------------
- Python assumes s is local because it is being modified
- But local s was never initialized
"""


# ---------- With global keyword (Correct way) ----------

s = "Python is great!"

def fun():
    global s
    s += " GFG"   # Modify global variable
    print(s)
    s = "Look for GeeksforGeeks Python Section"
    print(s)

fun()
print(s)

"""
Output:
-------
Python is great! GFG
Look for GeeksforGeeks Python Section
Look for GeeksforGeeks Python Section
"""

"""
Explanation:
------------
- global s tells Python to use global variable
- Modifications persist outside the function
"""


# ========================================
# GLOBAL vs LOCAL WITH SAME NAME
# ========================================

a = 1  # Global variable

def f():
    print("f():", a)   # Uses global a

def g():
    a = 2             # Local variable
    print("g():", a)

def h():
    global a
    a = 3             # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)

"""
Output:
-------
global: 1
f(): 1
global: 1
g(): 2
global: 1
h(): 3
global: 3
"""

"""
Explanation:
------------
- f() reads global variable
- g() creates local variable
- h() modifies global variable
"""


# ========================================
# GLOBAL vs LOCAL VARIABLES COMPARISON
# ========================================
"""
Comparison Table:

Basis           | Global Variable                  | Local Variable
--------------- | -------------------------------- | -----------------------------
Definition      | Declared outside functions       | Declared inside functions
Scope           | Accessible everywhere            | Accessible only in function
Lifetime        | Program start to end             | Function call duration
Data Sharing    | Shared across functions          | Not shared
Modification    | Affects entire program           | Affects only local scope
Storage         | Global namespace                 | Local namespace (stack frame)
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Local variables exist only inside functions
2. Global variables exist throughout the program
3. Local variables shadow globals with same name
4. global keyword is required to MODIFY global variables
5. Overusing global variables is BAD practice

Best Practice:
--------------
✔ Prefer local variables
✔ Pass values as parameters
✔ Return values instead of using globals

Understanding scope is CRITICAL for:
✔ Debugging
✔ Clean code
✔ Interviews
✔ Real-world Python programming
"""

"""
End of Global and Local Variables Module
----------------------------------------
"""
