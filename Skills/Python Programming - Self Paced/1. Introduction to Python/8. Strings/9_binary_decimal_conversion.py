"""
========================================
BINARY ↔ DECIMAL CONVERSION IN PYTHON
========================================

Overview:
---------
Binary and Decimal are two different number systems.

Decimal Number System:
----------------------
✔ Base 10
✔ Digits: 0–9

Binary Number System:
---------------------
✔ Base 2
✔ Digits: 0 and 1

This module covers:
1. Decimal to Binary conversion
2. Binary to Decimal conversion
Using:
✔ Loops
✔ Built-in functions
✔ Mathematical logic
"""

# ========================================
# DECIMAL TO BINARY CONVERSION
# ========================================

# ----------------------------------------
# METHOD 1: USING LOOP (MANUAL METHOD)
# ----------------------------------------
"""
Concept:
--------
Repeatedly divide the number by 2.
Store remainders in reverse order.

Steps:
------
1. Divide number by 2
2. Store remainder
3. Continue until number becomes 0
"""

for num in [8, 18]:
    n = num
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n //= 2
    print(f"Decimal {num} → Binary {b}")

"""
Output:
-------
Decimal 8 → Binary 1000
Decimal 18 → Binary 10010
"""


# ----------------------------------------
# METHOD 2: USING BUILT-IN bin()
# ----------------------------------------
"""
bin() converts a decimal number to binary.
It returns a string starting with '0b'.
"""

n = 8
print(bin(n).replace("0b", ""))

n = 18
print(bin(n).replace("0b", ""))

"""
Output:
-------
1000
10010
"""

"""
Explanation:
------------
- bin(n) → '0b1000'
- replace("0b", "") removes prefix
"""


# ----------------------------------------
# METHOD 3: USING format()
# ----------------------------------------
"""
format() can convert decimal to binary
using format specifier 'b'.
"""

n = 4
print('{0:b}'.format(n))

b = format(n, 'b')
print(b)

"""
Output:
-------
100
100
"""

"""
Note:
-----
format() works only for decimal → binary
"""


# ========================================
# BINARY TO DECIMAL CONVERSION
# ========================================

# ----------------------------------------
# METHOD 1: POSITIONAL (MATHEMATICAL) METHOD
# ----------------------------------------
"""
Concept:
--------
Binary digits are multiplied by powers of 2
based on their position.

Example:
--------
101 (binary)
= 1×2² + 0×2¹ + 1×2⁰
= 4 + 0 + 1
= 5
"""

def binary_to_decimal(b):
    d, p = 0, 0
    while b:
        d += (b % 10) * (2 ** p)
        b //= 10
        p += 1
    return d

for num in [100, 101]:
    print(f"Binary {num} → Decimal {binary_to_decimal(num)}")

"""
Output:
-------
Binary 100 → Decimal 4
Binary 101 → Decimal 5
"""


# ----------------------------------------
# METHOD 2: USING BUILT-IN int()
# ----------------------------------------
"""
int(string, base) converts a number
from a given base to decimal.
"""

for b in ['100', '101']:
    print(f"Binary {b} → Decimal {int(b, 2)}")

"""
Output:
-------
Binary 100 → Decimal 4
Binary 101 → Decimal 5
"""


# ========================================
# COMPARISON OF METHODS
# ========================================
"""
Conversion            | Method              | Remarks
----------------------|---------------------|-------------------------
Decimal → Binary      | Loop                | Good for logic building
Decimal → Binary      | bin()               | Fast & built-in
Decimal → Binary      | format()            | Clean formatting
Binary → Decimal      | Positional Method   | Mathematical clarity
Binary → Decimal      | int(b, 2)            | Best & simplest
"""


# ========================================
# WHICH METHOD TO USE?
# ========================================
"""
Recommendations:
----------------
✔ Use bin() or format() for decimal → binary
✔ Use int(binary, 2) for binary → decimal
✔ Use loop-based methods for exams & understanding

Interview Tip:
--------------
Explain manual logic first,
then mention built-in functions as optimization.
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Binary uses base 2, Decimal uses base 10
2. Decimal → Binary uses division by 2
3. Binary → Decimal uses powers of 2
4. Python provides powerful built-ins
5. int(b, 2) is the best for binary → decimal

These conversions are important for:
✔ Number system understanding
✔ Computer architecture basics
✔ Competitive programming
✔ Interview questions
"""

"""
End of Binary ↔ Decimal Conversion Module
-----------------------------------------
"""
