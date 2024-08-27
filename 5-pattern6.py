#!/usr/bin/python3

# python program that prints grid 5 rows and 5 columns
"""
n = 5
k = 1

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print("{:2d}".format(k), end="")
        k += 1
    print()

"""

# added user input
n = int(input("Enter the size of the grid "))
k = 1

for x in range(1, n + 1):
        for y in range(1, n + 1):
            print("{:5d}".format(k), end="")
            k += 1
        print()
