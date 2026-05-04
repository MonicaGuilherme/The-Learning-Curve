# OPERATORS
# ------------------------------------------------
# Operators are symbols used to perform operations on variables and values.



# ------------------------------------------------
# MATH OPERATORS
# ------------------------------------------------
#
# Used to perform mathematical calculations.

# +  → Addition
print(5 + 3)   # 8

# -  → Subtraction
print(10 - 4)  # 6

# *  → Multiplication
print(6 * 2)   # 12

# /  → Division (always returns float)
print(10 / 3)  # 3.333...

# // → Floor Division (removes decimals)
print(10 // 3) # 3

# ** → Power (exponent)
print(2 ** 3)  # 8



# --------------------
# MODULO OPERATOR (%)
#
# The modulo operator returns the remainder of a division.
#
# Syntax:
# result = dividend % divisor
#
# - dividend → number being divided
# - divisor → number you divide by
# - result → remainder


# Example 1
result = 14 % 4   # 4 fits into 14 three times (12), remainder is 2
print(result)     # 2


# Example 2 (divisor greater than dividend)
result = 3 % 10   # 10 does not fit into 3, remainder is 3
print(result)     # 3


# --------------------
# COMMON USE: EVEN OR ODD

number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# ------------------------------------------------
# COMPARISON OPERATORS
# ------------------------------------------------
#
# Comparison operators are used to compare values.
# They return:
# - True  → if the condition is correct
# - False → otherwise


# ==  → Equal
print(5 == 5)   # True

# !=  → Not equal
print(5 != 3)   # True

# >   → Greater than
print(7 > 10)   # False

# <   → Less than
print(2 < 9)    # True

# >=  → Greater or equal
print(6 >= 6)   # True

# <=  → Less or equal
print(4 <= 1)   # False



# ------------------------------------------------
# LOGICAL OPERATORS
# ------------------------------------------------
#
# Used to combine multiple conditions.


# and → True if BOTH conditions are true
print(5 > 2 and 10 > 5)   # True

# or → True if AT LEAST ONE condition is true
print(5 > 10 or 3 < 8)    # True

# not → Reverses the result
print(not True)           # False



# --------------------
# PRACTICAL EXAMPLES

age = 18
has_id = True

# Can enter only if age >= 18 AND has ID
print(age >= 18 and has_id)   # True


temperature = 25

# Check if temperature is between 20 and 30
print(20 < temperature < 30)  # True



# --------------------
# QUICK PRACTICE

number = 11

print(number % 2 == 0)   # False → not even
print(number > 10)       # True
print(number < 5 or number > 10)  # True