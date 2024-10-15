p = 1

for x in range(5, 0, - 1):
    for y in range(6, x, - 1):
        print("{:2d}".format(p), end="  ")
        p += 2
    print()
