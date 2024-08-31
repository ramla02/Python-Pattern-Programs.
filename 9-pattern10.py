#!/usr/bin/python3

# python program that prints 5x3 grid of numbers

for x in range(1, 6):
    for y in range(1, 4):
        print("{} {} ".format(y, x), end="")
    print()
