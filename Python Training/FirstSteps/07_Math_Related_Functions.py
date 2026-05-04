# MATH RELATED FUNCTIONS
# ------------------------------------------------

# Python has several built-in functions that are useful when working with numbers.
# Some examples are:
# - round()
# - abs()
# - pow()
# - max()
# - min()


# --------------------
# ROUND FUNCTION
#
# round() rounds a number to the nearest whole number.

price = 9.75

print(round(price))   # 10



# --------------------
# ABSOLUTE VALUE
#
# abs() returns the absolute value of a number.
# This means it removes the negative sign.

temperature = -12

print(abs(temperature))   # 12



# --------------------
# POWER FUNCTION
#
# pow() raises a number to a power.
#
# Syntax:
# pow(base, exponent)

result = pow(3, 2)

print(result)   # 9



# --------------------
# MAX FUNCTION
#
# max() returns the highest value.

highest_score = max(12, 45, 23, 8)

print(highest_score)   # 45



# --------------------
# MIN FUNCTION
#
# min() returns the lowest value.

lowest_score = min(12, 45, 23, 8)

print(lowest_score)   # 8



# ------------------------------------------------
# MATH MODULE
# ------------------------------------------------

# Python also has a math module with more advanced math functions.
# To use it, we need to import it first.

import math



# --------------------
# PI CONSTANT
#
# math.pi gives the value of pi.

print(math.pi)   # 3.141592653589793



# --------------------
# SQUARE ROOT
#
# math.sqrt() returns the square root of a number.

number = 64

print(math.sqrt(number))   # 8.0



# --------------------
# CEIL FUNCTION
#
# math.ceil() rounds a number up.

price = 4.2

print(math.ceil(price))   # 5



# --------------------
# FLOOR FUNCTION
#
# math.floor() rounds a number down.

price = 4.9

print(math.floor(price))   # 4



# --------------------
# SIMPLE PRACTICE

radius = 5

circle_area = math.pi * pow(radius, 2)

print(round(circle_area, 2))   # 78.54