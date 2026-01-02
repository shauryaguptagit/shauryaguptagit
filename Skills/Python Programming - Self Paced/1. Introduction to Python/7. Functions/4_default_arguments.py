"""
========================================
DEFAULT ARGUMENTS IN PYTHON
========================================

Overview:
---------
In Python, functions can have DEFAULT ARGUMENTS.
Default arguments are parameters that are assigned
a value at the time of function definition.

If a value is provided during function call:
→ Python uses the provided value

If a value is NOT provided:
→ Python uses the default value automatically

Default arguments make functions:
✔ Flexible
✔ Easier to use
✔ Less verbose in function calls
"""

# ========================================
# BASIC EXAMPLE OF DEFAULT ARGUMENT
# ========================================

def greet(name="Guest"):
    """Greets a user, uses default name if none provided"""
    print("Hello,", name)

# Function calls
greet()          # Uses default value
greet("Kate")   # Uses provided value

"""
Output:
-------
Hello, Guest
Hello, Kate
"""

"""
Explanation:
------------
- In greet(), no argument is passed → default value "Guest" is used
- In greet("Kate"), default value is overridden
"""


# ========================================
# SYNTAX OF DEFAULT ARGUMENTS
# ========================================
"""
General Syntax:
---------------
def function_name(param1=value1, param2=value2, ...):
    function body

Rules:
------
1. Each parameter must receive only ONE value
2. Default parameters must come AFTER required parameters
3. Keyword names must match exactly
4. Positional arguments follow strict order
"""


# ========================================
# EXAMPLE 1: DEFAULT ARGUMENTS WITH POSITIONAL CALLS
# ========================================

def student(fn, ln='Mark', std='Fifth'):
    print(fn, ln, 'studies in', std, 'Standard')

student('John')                          # 1 positional argument
student('John', 'Gates', 'Seventh')      # 3 positional arguments
student('John', 'Gates')                 # 2 positional arguments
student('John', 'Seventh')               # Positional confusion

"""
Output:
-------
John Mark studies in Fifth Standard
John Gates studies in Seventh Standard
John Gates studies in Fifth Standard
John Seventh studies in Fifth Standard
"""

"""
Explanation:
------------
- fn is mandatory
- ln and std use defaults if not provided
- Order MATTERS in positional arguments
- Wrong order can cause logical errors
"""


# ========================================
# EXAMPLE 2: DEFAULT ARGUMENTS WITH KEYWORD CALLS
# ========================================

def student(fn, ln='Mark', std='Fifth'):
    print(fn, ln, 'studies in', std, 'Standard')

student(fn='John')                     
student(fn='John', std='Seventh')      
student(ln='Gates', fn='John')         

"""
Output:
-------
John Mark studies in Fifth Standard
John Mark studies in Seventh Standard
John Gates studies in Fifth Standard
"""

"""
Explanation:
------------
- Keyword arguments allow passing values by name
- Order does NOT matter
- Makes function calls more readable and safer
"""


# ========================================
# EXAMPLE 3: INVALID USE OF DEFAULT ARGUMENTS
# ========================================

def student(fn, ln='Mark', std='Fifth'):
    print(fn, ln, 'studies in', std, 'Standard')

# student()                         ❌ Missing required argument
# student(fn='John', 'Seventh')     ❌ Positional after keyword
# student(sub='Maths')              ❌ Unknown keyword argument

"""
Explanation:
------------
1. fn is mandatory → missing required argument
2. Positional arguments cannot come after keyword arguments
3. Keyword name must exactly match function definition
"""


# ========================================
# COMMON PITFALL: MUTABLE DEFAULT ARGUMENTS (LIST)
# ========================================
"""
Default arguments are evaluated ONLY ONCE at function definition time.

If a mutable object (list, dict) is used as default:
→ Same object is reused across all function calls
"""

def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item('note'))
print(add_item('pen'))
print(add_item('eraser'))

"""
Output:
-------
['note']
['note', 'pen']
['note', 'pen', 'eraser']
"""

"""
Explanation:
------------
- The same list 'lst' is reused
- Items keep accumulating across calls
- This behavior is often unintended
"""


# ========================================
# COMMON PITFALL: MUTABLE DEFAULT ARGUMENTS (DICT)
# ========================================

def add_dict(item, qty, d={}):
    d[item] = qty
    return d

print(add_dict('note', 4))
print(add_dict('pen', 1))
print(add_dict('eraser', 1))

"""
Output:
-------
{'note': 4}
{'note': 4, 'pen': 1}
{'note': 4, 'pen': 1, 'eraser': 1}
"""

"""
Explanation:
------------
- Same dictionary is reused
- Data from previous calls persists
"""


# ========================================
# CORRECT WAY: USING None AS DEFAULT
# ========================================
"""
Best Practice:
--------------
Use None as default value
Create a new list or dictionary inside the function
"""

# Using list safely
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item('note'))
print(add_item('pen'))
print(add_item('eraser'))

# Using dictionary safely
def add_dict(item, qty, d=None):
    if d is None:
        d = {}
    d[item] = qty
    return d

print(add_dict('note', 4))
print(add_dict('pen', 1))
print(add_dict('eraser', 1))

"""
Output:
-------
['note']
['pen']
['eraser']
{'note': 4}
{'pen': 1}
{'eraser': 1}
"""

"""
Explanation:
------------
- None ensures a NEW object is created each call
- Prevents unintended data sharing
- This is the recommended professional approach
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Default arguments make functions flexible
2. If value is skipped → default is used
3. Positional arguments depend on order
4. Keyword arguments ignore order
5. NEVER use mutable objects as default arguments
6. Use None + initialization inside function

Understanding default arguments is CRITICAL for:
✔ Writing clean APIs
✔ Avoiding hidden bugs
✔ Interview questions
✔ Production-level Python code
"""

"""
End of Default Arguments Module
--------------------------------
"""
