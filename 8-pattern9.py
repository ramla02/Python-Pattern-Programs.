#!/usr/bin/python3

n = 10

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print("{:5d}".format(x * y), end="")
    print()
