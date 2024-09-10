#!/usr/bin/python3

n = 5
for x in range(1, n + 1):
    for y in range(1, n + 1):
        print("{:2d}".format((2 * (x + y)) - 3), end=" ")
    print()
