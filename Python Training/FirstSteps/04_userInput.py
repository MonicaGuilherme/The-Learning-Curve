
# ==========================================
# USER INPUT IN PYTHON
# ==========================================
# input() allows the program to receive data typed by the user.
# Whatever the user types is stored as text (string) by default.

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}!")
print(f"You are {age} years old.")

# The program pauses and waits for the user to type an answer.
# After the user presses Enter, the value is stored in the variable.



# ==========================================
# EXERCISE 1 - MAD LIBS
# ==========================================
# Mad Libs is a simple word game.
# The user fills in random words, and the program uses them
# to create a funny or unexpected story.

print("\n--- Exercise 1: Mad Libs ---")
print("You are about to create a funny story about taking your pet to the vet.\n")

animal = input("Enter an animal type: ")
pet_name = input("Enter your pet's name: ")
adjective1 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
dr_name = input("Enter the vet's name: ")
adjective3 = input("Enter another adjective: ")
adjective4 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")
adjective5 = input("Enter another adjective: ")
noun3 = input("Enter another noun: ")
emotion = input("Enter an emotion: ")
adjective6 = input("Enter one last adjective: ")

print("\n--- Your Story ---")
print(f"Today I rushed my {animal} named {pet_name} to the vet because they were acting extremely {adjective1}.")
print(f"In the waiting room, my pet suddenly started to {verb1} on a {adjective2} {noun1}, terrifying everyone.")
print(f'The vet, Dr. {dr_name}, looked at us and said, "Hmm... this is very {adjective3}."')
print(f"Apparently, {pet_name} had eaten a {adjective4} {noun2} and now refuses to {verb2}.")
print(f"After some very {adjective5} treatment, everything was under control.")
print(f"We left the clinic with {noun3} and a sense of {emotion}.")
print(f"Honestly... just another {adjective6} day.")



# ==========================================
# EXERCISE 2 - AREA OF A RECTANGLE
# ==========================================
# input() gives us text, so we use float() to convert the values
# into numbers with decimals.
# Then we multiply length by width to calculate the area.

print("\n--- Exercise 2: Area of a Rectangle ---")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print(f"The area of the rectangle is {area} cm².")



# ==========================================
# EXERCISE 3 - GOING TO THE MOVIES
# ==========================================
# This exercise is similar to Mad Libs because it asks for information,
# but now we also do calculations.
#
# float() is used for prices because prices can have decimals.
# int() is used for quantities because tickets and popcorn buckets
# are whole numbers.
#
# round(total, 2) is used to show the final price with 2 decimal places.

print("\n--- Exercise 3: Going to the Movies ---")

movie = input("What movie would you like to see? ")
ticket_price = float(input("How much is one ticket? €"))
tickets = int(input("How many tickets do you want? "))
extras = input("Do you want popcorn? (yes/no) ")

popcorn_price = 0
buckets = 0

# Only ask for popcorn price and quantity if the user wants extras
if extras.lower() == "yes":
    popcorn_price = float(input("How much is one popcorn bucket? €"))
    buckets = int(input("How many popcorn buckets do you want? "))

# Total cost = ticket total + popcorn total
total = (ticket_price * tickets) + (popcorn_price * buckets)

print(f"\nYou bought {tickets} ticket(s) to see {movie}.")
print(f"You also ordered {buckets} popcorn bucket(s).")
print(f"Your total is €{round(total, 2)}.")

    



