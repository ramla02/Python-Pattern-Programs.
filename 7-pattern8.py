#!/usr/bin/python3

# Python program that prints 2 to 200 by adding 2 e.g(2,4,6......200)

n = 10
p = 2

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print("{:5d}".format(p), end="")
        p += 2
    print()
