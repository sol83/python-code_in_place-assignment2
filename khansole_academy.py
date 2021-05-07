"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random


def main():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    total = num1 + num2
    print("What is " + str(num1) + " + " + str(num2) + " ?")
    answer = int(input("Your answer: "))
    if answer != total:
        print("Incorrect. The expected answer is " + str(total))
    else:
        print("Correct!")


if __name__ == '__main__':
    main()
