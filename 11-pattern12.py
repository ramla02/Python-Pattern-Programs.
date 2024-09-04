#!/usr/bin/python3

n = 5

for x in range(1, n + 1):
    p = x
    for y in range(1, n + 1):
        print("{:3d}".format(p), end=" ")
        p += n;
    print()
