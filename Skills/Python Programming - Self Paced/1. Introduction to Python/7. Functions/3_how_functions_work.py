"""
========================================
HOW FUNCTIONS WORK IN PYTHON
========================================

Overview:
---------
Functions in Python execute in a well-defined sequence.
Understanding how control moves between functions is essential
for debugging, recursion, and writing efficient programs.

This file explains:
1. Function execution flow
2. Step-by-step execution order
3. Function call stack (LIFO)
4. Local variables and scope
"""

# ========================================
# FUNCTION EXECUTION FLOW
# ========================================
"""
Consider a program where one function calls another function.

Important Rule:
---------------
Python always executes code line-by-line.
When a function is called:
- Current execution pauses
- Control moves to the called function
- After completion, control returns back
"""

def fun2():
    print("Inside fun2")

def fun1():
    print("Before fun2")
    fun2()
    print("After fun2")

print("Before fun1")
fun1()
print("After fun1")


"""
Expected Output:
----------------
Before fun1
Before fun2
Inside fun2
After fun2
After fun1
"""


# ========================================
# STEP-BY-STEP EXECUTION EXPLANATION
# ========================================
"""
1. Program starts executing from the main code.
2. 'Before fun1' is printed.
3. fun1() is called → control moves to fun1.
4. 'Before fun2' is printed.
5. fun2() is called → control moves to fun2.
6. 'Inside fun2' is printed.
7. fun2 finishes → control returns to fun1.
8. 'After fun2' is printed.
9. fun1 finishes → control returns to main code.
10. 'After fun1' is printed.
"""


# ========================================
# FUNCTION CALL STACK
# ========================================
"""
Python internally uses a FUNCTION CALL STACK.

Stack Principle:
----------------
LIFO (Last In, First Out)

Each function call:
- Pushes a stack frame
Each function return:
- Pops the stack frame
"""

"""
Call Stack Visualization:

Main Code
↓
+-------------+
| Main Code   |
+-------------+
       ↓
+-------------+
| fun1        |
+-------------+
       ↓
+-------------+
| fun2        |
+-------------+
       ↓
+-------------+
| fun1        |
+-------------+
       ↓
+-------------+
| Main Code   |
+-------------+
"""

# Stack behavior demonstration using print statements
def stack_fun2():
    print("Entering stack_fun2")
    print("Exiting stack_fun2")

def stack_fun1():
    print("Entering stack_fun1")
    stack_fun2()
    print("Exiting stack_fun1")

print("\n--- Call Stack Demonstration ---")
stack_fun1()


# ========================================
# LOCAL VARIABLES AND SCOPE
# ========================================
"""
Each function call creates its own local scope.
Local variables:
- Exist only inside the function
- Are destroyed after function execution

Every function call creates a NEW set of local variables.
"""

def fun():
    x = 5
    y = 10
    x = y
    print(x, y)

# First call
fun()

# Second call
fun()

"""
Output:
-------
10 10
10 10
"""


# ========================================
# SCOPE EXPLANATION
# ========================================
"""
Execution Explanation:
----------------------
First Call:
- x = 5
- y = 10
- x = y → x becomes 10
- Prints: 10 10
- Function ends → x and y are destroyed

Second Call:
- New x and y are created again
- Same operations repeat
- Prints: 10 10

Conclusion:
-----------
Each function call is independent.
Local variables do NOT retain values between calls.
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Python executes code sequentially.
2. Function calls pause current execution.
3. Control returns after function completion.
4. Function calls are managed using a call stack.
5. Each function call has its own local variables.
6. Local variables are destroyed after execution.

Understanding this is essential for:
✔ Debugging
✔ Recursion
✔ Memory management
✔ Writing efficient programs
"""

"""
End of How Functions Work Module
--------------------------------
"""
