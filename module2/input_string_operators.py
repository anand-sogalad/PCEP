# """
# Lab1:
# Scenario
# Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
#
# The results have to be printed to the console.
#
# You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.
#
# Test your code - does it produce the results you expect?
#
# We won't show you any test data - that would be too simple.
# """
# x = float(input("Enter a value for variable x: "))
# y = float(input("Enter a value for variable : "))
#
# # output the result of addition here
# print(x + y)
#
# # output the result of subtraction here
# print(x - y)
#
# # output the result of multiplication here
# print(x * y)
#
# # output the result of division here
# print(x / y)
#
# print("\nThat's all, folks!")

"""
Lab2:
Scenario
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.

Test your code carefully. Hint: using the % operator may be the key to success.
"""


def calculate_end_time(hour, minute, duration):
    hour += ((minute + duration) // 60) % 24
    minute = (minute + duration) % 60
    print(f"{hour}:{minute:02}")


calculate_end_time(int(input("Enter hour: ")), int(input("Enter minute: ")), int(input("Enter duration: ")))
