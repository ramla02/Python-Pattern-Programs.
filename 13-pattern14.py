#!/usr/bin/python3

n = 5

for x in range(1, n + 1):
    p = n - x + 1;
    for y in range(1, n + 1):
        print("{:2d}".format(p), end=" ")
        p = p + n
    print()
