"""
Number Guesser

In this problem, you'll write a program that guesses the number between 1 and 100 that the user is thinking of.
The program works by guessing a number, and then getting feedback from the user as to whether that guess is correct,
or higher or lower than the correct number.

Here's a sample run of the program:

Is your number 95? lower
Is your number 75? lower
Is your number 18? higher
Is your number 28? higher
Is your number 36? higher
Is your number 47? lower
Is your number 39? higher
Is your number 46? lower
Is your number 43? lower
Is your number 41? higher
Is your number 42? correct
I win! It took me 11 guesses


Take a look at each individual guess,
and how the feedback the computer receives from the user affects its subsequent guesses.
For example, when the user tells the computer that the correct number is lower than 75,
the computer will only guess numbers below 75.
Later on, when the user tells the computer that the correct number is lower than 47,
it will only guess numbers below 47.

Conversely, when the user tells the computer that the correct answer is greater than 18,
the computer only guesses numbers above 18. When the user later tells the computer that the correct answer is greater than 36,
the computer only guesses numbers above 36.

This run indicates a few additional things you'll need to think about:

Each 'turn', the program guesses a number, and asks the user if its guess is correct.
The user can respond with one of three answers (which you can assume they will do):

--- lower, meaning that the correct number is less than what the computer guessed

--- higher, meaning that the correct number is greater than what the computer guessed

--- correct, meaning that the computer successfully guessed the correct number

When the computer guesses the correct number, it should print out how many guesses it took

The last problem you'll need to think about is how exactly the computer should guess a particular number.
One possible approach is to randomly choose a number in the correct range (making use of the random.randint function),
but see if you can think of a smarter strategy than that!
"""

import random

MIN_NUM = 1
MAX_NUM = 100

def main():
    num_guesses = 0
    lower_limit = MIN_NUM
    upper_limit = MAX_NUM
    while True:
        num_guesses += 1
        guess = random.randint(lower_limit, upper_limit)
        response = input("Is your number " + str(guess) + "? ")
        if response == "higher":
            lower_limit = guess + 1
        if response == "lower":
            upper_limit = guess - 1
        if response == "correct":
            break
    print()
    print("I win! It took me " + str(num_guesses) + " guesses")

if __name__ == "__main__":
    main()