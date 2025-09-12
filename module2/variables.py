# What is the difference between variable and indentifier?
# Variable is the stored location of the data. while identifier is the name of the variable.

# Naming convention for variables
# 1. variable names shoud start with alphabets
# 2. variable names should not start with numbers
# 3. variable names should contain only alphabets, numbers and underscore
# 4. variable names should not contain special characters like @, $, %, ^, &, *
# 5. variable names should not be reserved keywords like if, else, while, for, etc.

"""
Lab1:
Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

Your task is to:

create the variables: john, mary, and adam;
assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
now create a new variable named total_apples equal to addition of the three former variables.
print the value stored in total_apples to the console;
experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.).
Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
"""
john, mary, adam = 3, 5, 6
print(john, mary, adam, sep=", ")
total_apples = john + mary + adam
print(f"Total number of apples: {total_apples}")

"""
Lab2:
Scenario
Miles and kilometers are units of length or distance.

Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:

miles to kilometers;
kilometers to miles.
"""


def miles_to_km(miles):
    return round(miles * 1.61, 2)


def km_to_miles(km):
    return round(km / 1.61, 2)


kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles_to_km(miles)
kilometers_to_miles = km_to_miles(kilometers)

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

"""
Lab3:
y =3x3 - 2x2 + 3x - 1
"""


def y(x):
    return (3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1


test_data = [0, 1, -1]
for x in test_data:
    print(f"y({x}) = {y(x)}")
