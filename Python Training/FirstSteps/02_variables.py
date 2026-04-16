# ==========================================
# VARIABLES AND DATA TYPES IN PYTHON
# ==========================================
# A variable is a container used to store a value in memory.
# That value can have different data types, such as:
# string, integer, float, or boolean.
#
# A data type defines the kind of value a variable can store.
# Variable names should be descriptive and written in snake_case.



# ==========================================
# STRINGS (str)
# ==========================================
# Strings are used to store text.
# They must be written inside quotes (" " or ' ').

store_name = "Fresh From The Farm"
slogan = "Fruits and vegetables grown without pesticides"
website = "www.freshfromthefarm.com"

print(store_name)
print(slogan)



# ==========================================
# INTEGERS (int)
# ==========================================
# Integers are whole numbers (no decimal values).

age_oldest_employee = 64
age_youngest_employee = 20

print(age_oldest_employee)



# ==========================================
# FLOATS (float)
# ==========================================
# Floats are numbers with decimal points.

apples_price = 1.99
oranges_price = 2.99

print(apples_price)



# ==========================================
# BOOLEANS (bool)
# ==========================================
# Booleans can only have two values: True or False.
# They are commonly used in conditions (if statements).

# Example 1
is_open = False

if is_open:
    print("Fresh From The Farm is open to the public")
else:
    print("This establishment is closed right now")

# Example 2
has_website = True

if has_website:
    print(f"You can access Fresh From The Farm here: {website}")
else:
    print("This website is not available at the moment")



# ==========================================
# LIST (list)
# ==========================================
# Ordered collection of items.
# Lists are mutable → they can be changed after creation.

products = ["apples", "oranges", "bananas"]

print(products)



# ==========================================
# TUPLE (tuple)
# ==========================================
# Ordered collection of items.
# Tuples are immutable → they cannot be changed after creation.

store_location = ("Lisbon", "Portugal")

print(store_location)



# ==========================================
# SET (set)
# ==========================================
# Unordered collection of unique items.
# Duplicate values are automatically removed.

available_categories = {"fruit", "vegetables", "organic"}

print(available_categories)



# ==========================================
# DICTIONARY (dict)
# ==========================================
# Stores data in key-value pairs (key: value).

store_info = {
    "name": "Fresh From The Farm",
    "employees": 12,
    "open": False
}

print(store_info)



# ==========================================
# NONE TYPE (NoneType)
# ==========================================
# Represents the absence of a value.
# Often used as a placeholder when no value is assigned yet.

delivery_date = None

print(delivery_date)



# ==========================================
# RANGE (range)
# ==========================================
# Represents a sequence of numbers.
# Commonly used in loops.

days_open = range(1, 6)

print(days_open)



# ==========================================
# EXAMPLE
# ==========================================
# Describing a product in the store

product_name = "apple"
product_price = 1.50
in_stock = True

print(f"{product_name} costs {product_price}€ - In stock: {in_stock}")