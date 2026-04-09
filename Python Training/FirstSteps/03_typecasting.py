# TYPE CASTING
# Type casting is the process of converting a value
# from one data type to another.

# There are two types of type casting in Python:
# 1. Implicit casting (automatic)
# 2. Explicit casting (manual)


# --------------------
# IMPLICIT TYPE CASTING
# 
# Python automatically converts data types during operations
# when it can be done without data loss.

x = 10        # int
y = 2.5       # float

result = x + y   # int + float → float
print(result)    # 12.5


# --------------------
# EXPLICIT TYPE CASTING
# 
# The programmer manually converts a value to another data type
# using built-in functions like int(), float(), str(), bool().

age = "25"              # string
age_as_int = int(age)   # string → int

print(age_as_int + 5)   # 30


price = 10
price_as_str = str(price)  # int → string

print("Price: " + price_as_str)


is_open_number = 1
is_open_bool = bool(is_open_number)  # int → boolean

print(is_open_bool)  # True


# --------------------
# More examples of explicit type casting

# The fruit store receives some data as strings
apples_price = "1.50"
oranges_price = "2.00"

apples_quantity = "4"
oranges_quantity = "3"

# Convert prices from string to float
apples_price = float(apples_price)
oranges_price = float(oranges_price)

# Convert quantities from string to int
apples_quantity = int(apples_quantity)
oranges_quantity = int(oranges_quantity)

# Calculate total cost
total = (apples_price * apples_quantity) + (oranges_price * oranges_quantity)

print(f"Total to pay: {total}€") # 12.0€

# The store status comes from the system as a string
# "1" means open, "0" means closed
store_status = "0"

store_status_int = int(store_status)
is_open = bool(store_status_int)

if is_open:
    print("The fruit store is open")
else:
    print("The fruit store is closed")


# --------------------
# IMPORTANT:

# Numbers → boolean
# Rule:
# 0 is False
# Any number different from 0 is True

bool(0)      # False
bool(1)      # True
bool(-1)     # True
bool(100)    # True


# Strings → boolean
# Rule:
# Empty string is False
# Any string with content is True

bool("")        # False
bool(" ")       # True (contains a space)
bool("False")   # True (it is text, not a boolean)
bool("0")       # True


# Other types → boolean
# Rule:
# Most values are True, except:
# 0, 0.0, "", None, empty collections ([], {}, ())


# --------------------
# Common error example

# int("abc")  # Raises ValueError (invalid conversion)
