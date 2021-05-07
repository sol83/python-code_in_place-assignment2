"""
TODO: Write a description here
"""

import random

CORRECT_ANSWERS_IN_A_ROW = 3

def main():
    count = 0
    while count < CORRECT_ANSWERS_IN_A_ROW:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        total = num1 + num2
        print("What is " + str(num1) + " + " + str(num2) + "?")
        answer = int(input("Your answer: "))
        if answer == total:
            count += 1
            print("Correct! You've gotten " + str(count) + " correct in a row.")
        else:
            count = 0 # Resets count to 0 if there in case of wrong answer
            print("Incorrect. The expected answer is " + str(total))
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
