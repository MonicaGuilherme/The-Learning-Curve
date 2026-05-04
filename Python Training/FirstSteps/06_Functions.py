# FUNCTIONS
# ------------------------------------------------

# A function is a block of reusable code that performs a specific task.
# It helps organize code, avoid repetition, and improve readability.


# --------------------
# DEFINING A FUNCTION
#
# Use the keyword "def" followed by:
# - function name
# - parentheses ()
# - colon :

def greet():
    print("Hello!")


# Calling the function
greet()   # Output: Hello!



# --------------------
# PARAMETERS
#
# Parameters are variables passed into a function.

def greet_user(name):
    print("Hello " + name)


greet_user("Ana")     # Hello Ana
greet_user("John")    # Hello John



# --------------------
# MULTIPLE PARAMETERS

def add_numbers(a, b):
    print(a + b)


add_numbers(3, 5)     # 8
add_numbers(10, 2)    # 12



# --------------------
# RETURN VALUES
#
# Functions can return a value using "return".
# This allows you to store or reuse the result.

def multiply(a, b):
    return a * b


result = multiply(4, 3)
print(result)   # 12



# --------------------
# WHY USE RETURN INSTEAD OF PRINT?
#
# print() → only displays the result
# return  → gives the result back to be reused

def square(x):
    return x * x


value = square(5)
print(value + 10)   # 35



# --------------------
# DEFAULT PARAMETERS
#
# You can assign a default value to a parameter.

def greet_with_default(name="Guest"):
    print("Hello " + name)


greet_with_default()        # Hello Guest
greet_with_default("Mia")   # Hello Mia



# --------------------
# KEY CONCEPTS
#
# Function = reusable block of code
# Parameters = inputs
# Return = output



# --------------------
# SIMPLE PRACTICE

def is_even(number):
    return number % 2 == 0


print(is_even(6))   # True
print(is_even(7))   # False