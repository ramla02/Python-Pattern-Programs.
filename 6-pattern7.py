#!/usr/bin/python3

# python code that prints a grid of numbers where each number is incremented
# by 2 from the previous one.

n = 5
p = 1

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print("{:5d}".format(p), end="")
        p += 2
    print()
