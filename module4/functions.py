"""
lab1:
scenario:
Scenario
Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.

The seed of the function is already shown in the skeleton code in the editor.

Note: we've also prepared a short testing code, which you can use to test your function.

The code uses two lists ‒ one with the test data, and the other containing the expected results. The code will tell you if any of your results are invalid.
"""


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


"""
lab2:
Scenario:
Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (while only February is sensitive to the year value, your function should be universal).

The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful. We encourage you to use a list filled with the months' lengths. You can create it inside the function - this trick will significantly shorten the code.

We've prepared a testing code. Expand it to include more test cases.
"""


def count_days(year, month):
    days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if month == 2:
        return 29 if is_leap_year(year) else days[month]
    return days[month]


"""
lab3:
find a day of the year
"""


def day_of_the_year(year, month, day):
    return sum(count_days(year, mnth) for mnth in range(1, month)) + day


"""
lab4:
scenario:
check if the number is prime
"""


def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def main():
    for year in (1900, 2000, 2016, 1987):
        print(is_leap_year(year), end=", ")

    print()

    for year, month in ((1900, 2), (2000, 2), (2016, 1), (1987, 11)):
        print(count_days(year, month), end=", ")

    print()

    print(day_of_the_year(2000, 12, 31))

    [print(i, end=", ") for i in range(2, 20) if is_prime(i)]


if __name__ == "__main__":
    main()
