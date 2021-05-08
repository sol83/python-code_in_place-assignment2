import random

def main():
    stones = 20
    player = 1
    while stones > 0:     
        print("There are " + str(stones) + " stones left")
        stones_removed = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        while stones_removed < 0 or stones_removed > 2:
            stones_removed = int(input("Please enter 1 or 2: "))
        print("")       
        if stones_removed == 1:
            stones -= 1
        else:
            stones -= 2
        if player == 1:
            player += 1
        else:
            player -= 1
    print("Player " +str(player) + " wins!")

if __name__ == '__main__':
    main()
