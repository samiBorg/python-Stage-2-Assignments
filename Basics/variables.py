'''
1. Write any python program that makes use of variables, constants, operators, atleast 5 keywords and print statements
of different forms ?
'''


# Constants
PI = 3.14159

# Variables
radius = 5
name = "Samiksha"
age = 21

# Operators
circumference = 2 * PI * radius
birth_year = 2023 - age

# Keywords
if birth_year < 2000:
    is_old = True
else:
    is_old = False

# Print statements
print("Name:", name)
print("Age:", age)
print("Circumference:", circumference)
print("Birth Year:", birth_year)

# Formatted print statement
print(f"{name} is {age} years old.")

# Conditional print statement
if is_old:
    print("You are old!")
else:
    print("You are young!")
