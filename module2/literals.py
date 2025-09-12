# A literal is a data whose value is determined by itself.

print(123)  # always returns number in base 10
print(0o123)  # return this number in base 10, which means it converts the octal number to decimal (base 10)
print(0x123)  # return this number in base 10, which means it converts the hexadecimal number to decimal (base 10)

"""
Lab1:
Scenario
Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.

Expected output

"I'm"
""learning""
\"""Python\"""
"""
print("\"I'am\"", "\"\"learning\"\"", "\"\"\"Python\"\"\"", sep="\n")
print()  # just for new line
