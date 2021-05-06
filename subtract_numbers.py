"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The result is " + str(num1 - num2))

# A more advanced solution, using functions (but not really necessary here since the program is rather short)

# def main():
#     print("This program subtracts one number from another.")
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     print("The result is " + str(subtract_two_nums(num1, num2)))

# def subtract_two_nums(a, b):
#     total = a - b
#     return total    

if __name__ == '__main__':
    main()
