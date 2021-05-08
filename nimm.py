"""
TODO: Write a description here
"""

import random

def main():
    stones = 20   
    while stones > 0:
        print("There are " + str(stones) + " stones left")
        p1_remove = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        while p1_remove != 1 and p1_remove != 2:
            p1_remove = int(input("Please enter 1 or 2: "))
        stones -= p1_remove
        print("")
        if stones == 0:
            print("Player 2 wins!")
            break
        print("There are " + str(stones) + " stones left")
        p2_remove = int(input("Player 2 would you like to remove 1 or 2 stones? "))
        while p2_remove != 1 and p2_remove != 2:
            p2_remove = int(input("Please enter 1 or 2: "))
        stones -= p2_remove
        print("")
        if stones == 0:
            print("Player 1 wins!")

if __name__ == '__main__':
    main()
