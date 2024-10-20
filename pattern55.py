n = 4
d = 1

for x in range(1, n + 1):
    for y in range(1, x + 1):
        print("{:3d}".format(d * d), end="  ")
        d += 1
    print()
