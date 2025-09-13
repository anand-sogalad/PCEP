import random
import time
from enum import nonmember

"""
Lab1:
Scenario
A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

Your task is to help the magician complete the code in the editor in such a way so that the code:

will ask the user to enter an integer number;
will use a while loop;
will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
The magician is counting on you! Don't disappoint him.
"""


def guessing_game():
    print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
    secret_number = random.randint(1, 100)
    while True:
        user_number = int(input("Guess the number: "))
        if user_number == secret_number:
            print("Well done, muggle! You are free now.")
            break
        else:
            print("Ha ha! You're stuck in my loop!")


"""
Lab2:
Scenario:
Printing Mississippi 5 times
"""


def count_mississippi():
    for i in range(5):
        print("Mississippi")
        time.sleep(1)
    print("Ready or not, here I come!")


"""
Lab3:
Scenario:
while loop
"""


def chupacabra():
    while True:
        user_input = input("Enter a word (possibly 'chupacabra': ")
        if user_input == "chupacabra":
            break


"""
Lab4:
scenario: Vowel eater
"""


def vowel_eater():
    user_input = input("Enter a word: ")
    for letter in user_input.upper().replace(" ", ""):
        if letter in "AEIOU":
            continue
        print(letter, end="")


"""
Lab5:
Scenario:
Checking the piramid height
"""


def piramid_height(bricks):
    height = 0
    in_layer = 1
    while in_layer <= bricks:
        height += 1
        bricks -= in_layer
        in_layer += 1
    return height


def main():
    # guessing game
    # guessing_game()

    # count mississippi
    # count_mississippi()

    # chupacabra
    # chupacabra()

    # vowel eater
    # vowel_eater()

    # piramid height
    print(piramid_height(1000))


if __name__ == "__main__":
    main()
