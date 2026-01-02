"""
========================================
VARIABLE LENGTH ARGUMENTS IN PYTHON
========================================

Overview:
---------
In Python, functions are not limited to a fixed number of arguments.
They can accept a VARIABLE NUMBER of arguments, which provides great
flexibility while writing reusable and generic functions.

Python supports:
1. Variable Length Positional Arguments  (*args)
2. Variable Length Keyword Arguments     (**kwargs)
"""

# ========================================
# VARIABLE LENGTH POSITIONAL ARGUMENTS (*args)
# ========================================
"""
Basic Concept:
--------------
When a function definition uses *args, it means:
- Any extra positional arguments passed to the function
- Are captured as a TUPLE

This allows calling the function with:
✔ Zero arguments
✔ One argument
✔ Multiple arguments
"""

def sum_elements(*elements):
    """Returns sum of all provided elements"""
    result = 0
    for element in elements:
        result += element
    return result

# Function calls with different number of arguments
print(sum_elements(10, 20))       
print(sum_elements(10, 20, 30))   
print(sum_elements(10))           
print(sum_elements())             

"""
Output:
-------
30
60
10
0
"""

"""
Explanation:
------------
- elements is a tuple
- If no arguments are passed → empty tuple
- Loop runs safely in all cases
"""


# ========================================
# *args WITH ADDITIONAL FIXED PARAMETERS
# ========================================
"""
A function can have:
- Required (fixed) arguments
- Followed by variable length positional arguments

Rule:
-----
*args must come AFTER fixed positional arguments
"""

def sum_with_initial(initial_sum, *elements):
    """Adds elements to an initial value"""
    result = initial_sum
    for element in elements:
        result += element
    return result

print(sum_with_initial(0, 10, 20))        
print(sum_with_initial(5, 10, 15))        
print(sum_with_initial(0, 10, 20, 30))    

"""
Output:
-------
30
30
60
"""

"""
Explanation:
------------
- initial_sum is mandatory
- Remaining values are packed into elements tuple
"""


# ========================================
# VARIABLE LENGTH KEYWORD ARGUMENTS (**kwargs)
# ========================================
"""
Basic Concept:
--------------
When a function definition uses **kwargs:
- Any extra KEYWORD arguments
- Are captured as a DICTIONARY

Key → Parameter name
Value → Passed value
"""

def print_details(**details):
    """Prints key-value pairs"""
    for key, value in details.items():
        print(f"{key} is {value}")

print_details(ID=101, name="ABC", price=100)
print()
print_details(ID=102, name="XYZ")

"""
Output:
-------
ID is 101
name is ABC
price is 100
ID is 102
name is XYZ
"""

"""
Explanation:
------------
- details is a dictionary
- Can receive any number of named arguments
"""


# ========================================
# **kwargs WITH FIXED PARAMETERS
# ========================================
"""
A function can combine:
- Fixed parameters
- Variable length keyword arguments

Rule:
-----
**kwargs must come AFTER all other parameters
"""

def print_item(ID, **details):
    print(f"ID: {ID}")
    for key, value in details.items():
        print(f"{key} is {value}")

print_item(101, name="ABC", price=100)
print()
print_item(102, name="XYZ", color="black")

"""
Output:
-------
ID: 101
name is ABC
price is 100

ID: 102
name is XYZ
color is black
"""

"""
Explanation:
------------
- ID is mandatory
- Remaining keyword arguments go into details dictionary
"""


# ========================================
# COMBINING ALL TYPES OF ARGUMENTS
# ========================================
"""
Order of arguments in function definition:
------------------------------------------
1. Positional arguments
2. *args
3. Keyword-only arguments (if any)
4. **kwargs
"""

def demo(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, 4, 5, x=10, y=20)

"""
Output:
-------
a: 1
b: 2
args: (3, 4, 5)
kwargs: {'x': 10, 'y': 20}
"""


# ========================================
# ADVANTAGES OF VARIABLE LENGTH ARGUMENTS
# ========================================
"""
1. Flexibility:
   Functions can handle different numbers of arguments

2. Reusability:
   Same function works for multiple use cases

3. Readability:
   Keyword arguments clearly indicate meaning

4. Reduced Code Redundancy:
   No need to create multiple versions of similar functions

Used extensively in:
✔ Python built-ins (print, max, min)
✔ Libraries
✔ Frameworks
✔ API design
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. *args → variable length positional arguments (tuple)
2. **kwargs → variable length keyword arguments (dictionary)
3. Fixed arguments must come before *args and **kwargs
4. *args comes before **kwargs
5. Extremely useful for writing flexible, reusable code

Mastering variable length arguments is essential for:
✔ Real-world Python
✔ Interviews
✔ Clean API design
"""

"""
End of Variable Length Arguments Module
---------------------------------------
"""
