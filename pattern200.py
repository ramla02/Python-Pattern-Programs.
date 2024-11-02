# Binary number pattern

n = 3
d = 1

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print("{:5b}".format(d), end="  ")
        d += 1
    print()
