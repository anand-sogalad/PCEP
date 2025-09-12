"""
Lab1:
Scenario
Using one of the comparison operators in Python,
write a simple two-line program that takes the parameter n as input, which is an integer,
and prints False if n is less than 100, and True if n is greater than or equal to 100.
Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.
"""


def is_greater_than_100(n):
    return n >= 100


for i in range(101):
    print(is_greater_than_100(i))

"""
Lab2:
Scenario
Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.

Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"


Write a program that utilizes the concept of conditional execution, takes a string as input, and:

prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!
"""


def is_spathiphyllum(s):
    if s == "Spathiphyllum":
        return "Yes - Spathiphyllum is the best plant ever!"
    elif s == "spathiphyllum":
        return "No, I want a big Spathiphyllum!"
    else:
        return "Spathiphyllum! Not " + s + "!"


for i in ["Spathiphyllum", "spathiphyllum", "Lilly"]:
    print(is_spathiphyllum(i))

"""
Scenario
Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits.
The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.

It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.

Look at the code in the editor - it only reads one input value and outputs a result, so you need to complete it with some smart calculations.

Test your code using the data we've provided.
"""


def calculate_tax(income):
    if income <= 85_528:
        tax = float(round(.18 * income - 556.2))
    else:
        tax = float(round(14839.2 + .32 * (income - 85_528)))
    return tax if tax > 0 else float(0)


for income in (10000, 100000, 1000, -100):
    print(calculate_tax(income))

"""
Lab3:
check if the given year is leap year
"""


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


for year in (2000, 1994, 1912, 3002, 1700, 1400):
    print(is_leap_year(year))
