"""
========================================
RETURNING MULTIPLE VALUES IN PYTHON
========================================

Overview:
---------
Python allows a function to return MORE THAN ONE value.
Internally, Python packs multiple returned values into
a single object, most commonly a TUPLE.

Returning multiple values is useful when:
✔ A function computes related results
✔ Multiple outputs are required from one operation
✔ Clean and readable code is needed
"""

# ========================================
# METHOD 1: USING TUPLE (MOST COMMON WAY)
# ========================================
"""
Concept:
--------
When multiple values are separated by commas in a return statement,
Python automatically packs them into a tuple.

The returned tuple can be unpacked into variables.
"""

def fun():
    return "geeksforgeeks", 20   # Tuple packing

s, x = fun()   # Tuple unpacking
print(s)
print(x)

"""
Output:
-------
geeksforgeeks
20
"""

"""
Explanation:
------------
- fun() returns a tuple: ("geeksforgeeks", 20)
- Values are unpacked into s and x
- This is the most commonly used approach
"""


# ========================================
# METHOD 2: USING DATA CLASS
# ========================================
"""
Concept:
--------
A dataclass is a special type of class designed to store data.
It automatically generates methods like __init__() and __repr__(),
making it clean and readable.

Best used when:
✔ Values are logically related
✔ Code readability matters
✔ Structured data is needed
"""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int

def get_student():
    return Student("Alice", 85)

student = get_student()
print(student.name)
print(student.marks)

"""
Output:
-------
Alice
85
"""

"""
Explanation:
------------
- get_student() returns a Student object
- Multiple values are grouped inside the object
- Accessed using dot notation
"""


# ========================================
# METHOD 3: USING DICTIONARY
# ========================================
"""
Concept:
--------
A dictionary stores values as key-value pairs.
It is useful when returned values need labels
and easy access by key.
"""

def fun():
    d = {"str": "GeeksforGeeks", "x": 20}
    return d

d = fun()
print(d)

"""
Output:
-------
{'x': 20, 'str': 'GeeksforGeeks'}
"""

"""
Explanation:
------------
- Values are returned with descriptive keys
- Order is not guaranteed (prior to Python 3.7)
- Useful when values have meaningful names
"""


# ========================================
# METHOD 4: USING OBJECT (CLASS INSTANCE)
# ========================================
"""
Concept:
--------
An object can store multiple values as attributes.
Returning an object allows grouping related data together.

Common in:
✔ Object-Oriented Programming
✔ Large applications
✔ Structured data handling
"""

class Info:
    def __init__(self):
        self.name = "Alice"
        self.age = 25

def get_info():
    return Info()

person = get_info()
print(person.name)
print(person.age)

"""
Output:
-------
Alice
25
"""

"""
Explanation:
------------
- get_info() returns an object of class Info
- Values are accessed using dot notation
- Similar to dataclass but more manual
"""


# ========================================
# METHOD 5: USING LIST
# ========================================
"""
Concept:
--------
A list is an ordered collection of items.
It can be used to return multiple values,
especially when the number of values is fixed.

Less preferred than tuple when immutability is desired.
"""

def fun():
    l = ["geeksforgeeks", 20]
    return l

data = fun()
print(data)

"""
Output:
-------
['geeksforgeeks', 20]
"""

"""
Explanation:
------------
- fun() returns a list containing multiple values
- Order is preserved
- List is mutable, unlike tuple
"""


# ========================================
# COMPARISON OF METHODS
# ========================================
"""
Method        | Use Case
--------------|-----------------------------------
Tuple         | Fast, simple, most common
Dataclass     | Clean, structured, readable
Dictionary    | Named values, flexible access
Object        | OOP-based structured data
List          | Ordered, mutable collection
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Python returns multiple values as a tuple internally
2. Tuple unpacking is the most common approach
3. Dataclasses provide clean and modern structure
4. Dictionaries are useful for labeled outputs
5. Objects are preferred in OOP design
6. Lists work but are less safe than tuples

Returning multiple values improves:
✔ Code clarity
✔ Function usability
✔ Real-world program design
"""

"""
End of Returning Multiple Values Module
---------------------------------------
"""
