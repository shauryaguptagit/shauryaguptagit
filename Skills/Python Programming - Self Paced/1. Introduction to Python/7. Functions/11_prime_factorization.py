"""
========================================
PRIME FACTORIZATION IN PYTHON
========================================

Overview:
---------
Prime factorization is the process of breaking a number
into a product of prime numbers.

A PRIME number:
---------------
✔ Greater than 1
✔ Has only two factors: 1 and itself

Example:
--------
100 = 2 × 2 × 5 × 5 = 2² × 5²

This concept is widely used in:
✔ Mathematics
✔ Cryptography
✔ Competitive programming
✔ Algorithm design
"""

# ========================================
# WHAT IS PRIME FACTORIZATION?
# ========================================
"""
Prime factorization means repeatedly dividing a number
by prime numbers until the result becomes 1.

Example (n = 100):
------------------
100 ÷ 2 = 50
50  ÷ 2 = 25
25  ÷ 5 = 5
5   ÷ 5 = 1

Prime factors → 2, 2, 5, 5
"""


# ========================================
# STEP 1: PRIME CHECK FUNCTION
# ========================================
"""
We first need a function to check whether a number is prime.

Logic:
------
- Try dividing the number by all integers from 2 to x-1
- If divisible → not prime
- Otherwise → prime
"""

def is_prime(x):
    """Returns True if x is prime, False otherwise"""
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# ========================================
# STEP 2: PRIME FACTORIZATION FUNCTION
# ========================================
"""
Logic:
------
1. Loop from 2 to n
2. Check if the number is prime
3. If prime, check how many times it divides n
4. Print the prime factor each time it divides
"""

def print_prime_factors(n):
    """Prints prime factors of n"""
    for i in range(2, n + 1):
        if is_prime(i):
            x = i
            while n % x == 0:
                print(i)
                x = x * i


# ========================================
# MAIN EXECUTION
# ========================================

n = 100
print("Prime factors of", n, "are:")
print_prime_factors(n)

"""
Output:
-------
2
2
5
5
"""


# ========================================
# STEP-BY-STEP DRY RUN (n = 100)
# ========================================
"""
Iteration Details:
------------------
i = 2 → prime
100 % 2 == 0 → print 2
100 % 4 == 0 → print 2
100 % 8 != 0 → stop

i = 3 → prime
100 % 3 != 0 → skip

i = 5 → prime
100 % 5 == 0 → print 5
100 % 25 == 0 → print 5
100 % 125 != 0 → stop

Final Output:
-------------
2 2 5 5
"""


# ========================================
# VISUAL REPRESENTATION (TREE)
# ========================================
"""
Prime Factorization Tree for 100:

        100
       /   \
      2    50
         /   \
        2    25
             / \
            5   5

Leaf nodes are the prime factors.
"""


# ========================================
# LIMITATIONS OF THIS APPROACH
# ========================================
"""
This method:
✔ Is easy to understand
✔ Is beginner-friendly
✖ Is not optimized
✖ Uses repeated prime checks

Optimized versions use:
✔ Square root optimization
✔ Single loop division
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Prime factorization breaks a number into prime numbers
2. Smallest prime divisor is checked first
3. Repeated division extracts all occurrences
4. Helper function improves readability
5. Logic clarity > optimization for beginners

Important for:
✔ Exams
✔ Viva explanations
✔ Logic building
✔ Understanding number theory
"""

"""
End of Prime Factorization Module
---------------------------------
"""
