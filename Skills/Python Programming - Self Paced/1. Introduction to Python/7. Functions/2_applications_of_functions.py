"""
========================================
APPLICATIONS OF FUNCTIONS IN PYTHON
========================================

Overview:
---------
Functions (also called methods in some languages) play a very important role
in programming, especially in large and complex software projects.

They help in:
1. Avoiding code redundancy
2. Enhancing code modularity
3. Providing abstraction
4. Avoiding variable name collisions (scope management)

This file explains each application with clear theory and practical examples.
"""

# ========================================
# 1. AVOIDING CODE REDUNDANCY
# ========================================
"""
Code redundancy means writing the same logic multiple times in a program.

Functions help us define a task once and reuse it wherever needed.
This makes the code:
✔ Shorter
✔ Easier to maintain
✔ Less error-prone

Real-life analogy:
If a company changes its tagline, updating it in one function is easier
than changing it everywhere in the code.
"""

def print_array(arr):
    """Prints all elements of an array"""
    for item in arr:
        print(item, end=" ")
    print()

def sort_array(arr):
    """Returns a sorted version of the array"""
    return sorted(arr)

def search_array(arr, key):
    """Searches for an element in the array"""
    return key in arr

# Using the same functions multiple times
data = [5, 2, 9, 1, 7]

print("Original Array:")
print_array(data)

print("Sorted Array:")
sorted_data = sort_array(data)
print_array(sorted_data)

print("Searching for 9:", search_array(data, 9))
print("Searching for 10:", search_array(data, 10))


# ========================================
# 2. ENHANCING CODE MODULARITY
# ========================================
"""
Modularity means dividing a large program into smaller, logical units.

Instead of writing everything in one block, functions allow us to separate:
1. Input logic
2. Processing logic
3. Output logic

This makes the program:
✔ Easier to understand
✔ Easier to debug
✔ Easier to modify
"""

def get_input():
    """Takes input from the user"""
    num = int(input("Enter a number: "))
    return num

def process_data(num):
    """Processes the data (square calculation)"""
    return num * num

def display_output(result):
    """Displays the output"""
    print("Result is:", result)

# Driver code
# (Uncomment to run interactively)
# n = get_input()
# res = process_data(n)
# display_output(res)


# ========================================
# 3. PROVIDING ABSTRACTION
# ========================================
"""
Abstraction means hiding internal implementation details
and exposing only what is necessary.

When we use built-in or library functions, we do not care
how they work internally, we only focus on what they do.

If the internal implementation improves, our code still works.
"""

numbers = [4, 1, 7, 3, 9]

# Using built-in abstraction
sorted_numbers = sorted(numbers)
print("Sorted numbers using built-in function:", sorted_numbers)

# We don't know or care about the sorting algorithm used internally


# ========================================
# 4. AVOIDING VARIABLE NAME COLLISIONS
# ========================================
"""
In large programs, using unique variable names everywhere is difficult.

Functions solve this problem by providing local scope.
Variables declared inside a function exist only inside that function.

Hence, the same variable name can be reused safely in different functions.
"""

def function_one():
    index = 10   # local variable
    print("Function One index:", index)

def function_two():
    index = 20   # different local variable
    print("Function Two index:", index)

function_one()
function_two()

# Global scope variable
index = 100
print("Global index:", index)


"""
========================================
SUMMARY
========================================
Applications of Functions:
1. Avoid code repetition
2. Improve readability and structure
3. Provide abstraction from complexity
4. Prevent variable name conflicts
5. Make large projects manageable

Functions are the backbone of clean,
scalable, and maintainable software.
"""
