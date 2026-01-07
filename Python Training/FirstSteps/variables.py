# A variable is a container used to store a value in memory.
# That value can be different data types such as:
# string, integer, float, or boolean, for example.
# A data type defines the kind of value a variable can store.

# Variable names should be descriptive and written in snake_case.

#----------
# STRINGS
# 
# Strings are used to store text.
# They must be written inside quotes (" " or ' ').

store_name = "Fresh From The Farm"
slogan = "Fruits and vegetables grown without pesticides"
website = "www.freshfromthefarm.com"



#----------
# INTEGERS
# 
# Integers are whole numbers (no decimals).

age_oldest_employee = 64
age_youngest_employee = 20


#----------
# FLOATS
#
# Floats are numbers with decimal points.

apples_price = 1.99
oranges_price = 2.99


#----------
# BOOLEANS
# 
# Booleans can only have two values: True or False.
# They are commonly used in conditions.

# The if statement checks if the value is True
# Example 1
is_open = False

if is_open:
    print("Fresh From The Farm is open to the public")
else:
    print("This establishment is closed right now")

# Example 2
has_website = True

if has_website:
    print(f"You can access Fresh From The Farm information and products here: {website}")
else:
    print("This website is not available at the moment")


#----------
# LIST (list)
# 
# Ordered collection of items.
# Lists are mutable (can be changed).

products = ["apples", "oranges", "bananas"]


#----------
# TUPLE (tuple)
# 
# Ordered collection of items.
# Tuples are immutable (cannot be changed).

store_location = ("Lisbon", "Portugal")


#----------
# SET (set)
# 
# Unordered collection of unique items.
# Duplicates are not allowed.

available_categories = {"fruit", "vegetables", "organic"}


#----------
# DICTIONARY (dict)
# 
# Stores data in key-value pairs.

store_info = {
    "name": "Fresh From The Farm",
    "employees": 12,
    "open": False
}


#----------
# NONE TYPE (NoneType)
# 
# Represents the absence of a value.

delivery_date = None


# ----------
# RANGE (range)
# 
# Represents a sequence of numbers, commonly used in loops.

days_open = range(1, 6)