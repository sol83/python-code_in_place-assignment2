"""
Hailstone

A separate problem you could consider writing is based on a problem in Douglas Hofstadter’s Pulitzer-prize-winning book Gödel, Escher, Bach.
That book contains many interesting mathematical puzzles, many of which can be expressed in the form of computer programs.
In Chapter XII, Hofstadter mentions a wonderful problem that is well within the scope of what you know.
The problem can be expressed as follows:

Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.

On page 401 of the Vintage edition of his book,
Hofstadter illustrates this process with the following example, starting with the number 15:

15 is odd, so I make 3n+1: 46
46 is even, so I take half: 23
23 is odd, so I make 3n+1: 70
70 is even, so I take half: 35
35 is odd, so I make 3n+1: 106
106 is even, so I take half: 53
53 is odd, so I make 3n+1: 160
160 is even, so I take half: 80
80 is even, so I take half: 40
40 is even, so I take half: 20
20 is even, so I take half: 10
10 is even, so I take half: 5
5 is odd, so I make 3n+1: 16
16 is even, so I take half: 8
8 is even, so I take half: 4
4 is even, so I take half: 2
2 is even, so I take half: 1

As you can see from this example, the numbers go up and down,
but eventually—at least for all numbers that have ever been tried—comes down to end in 1.
In some respects, this process is reminiscent of the formation of hailstones,
which get carried upward by the winds over and over again before they finally descend to the ground.
Because of this analogy, this sequence of numbers is usually called the Hailstone sequence,
although it goes by many other names as well.

You might want to write a Python program that reads in a number from the user
and then displays the Hailstone sequence for that number, just as in Hofstadter’s book,
followed by a line showing the number of steps taken to reach 1.
For example, here’s a sample run of what such a program might look like:

Enter a number: 17
17 is odd, so I make 3n + 1: 52
52 is even, so I take half: 26
26 is even, so I take half: 13
13 is odd, so I make 3n + 1: 40
40 is even, so I take half: 20
20 is even, so I take half: 10
10 is even, so I take half: 5
5 is odd, so I make 3n + 1: 16
16 is even, so I take half: 8
8 is even, so I take half: 4
4 is even, so I take half: 2
2 is even, so I take half: 1
The process took 12 steps to reach 1
"""

def main():
    num = int(input("Enter a number: "))
    count = 0
    while num != 1:
        if num % 2 == 0:
            new_num = num // 2
            print(str(num) + " is even, so I take half: " + str(new_num))
        else:
            new_num  = num * 3 + 1
            print(str(num) + " is odd, so I make 3n + 1: " + str(new_num))
        num = new_num
        count += 1
    print()
    print("The process took " + str(count) + " steps to reach 1")

if __name__ == "__main__":
    main()