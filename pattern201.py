# Octal number pattern

n = 4
d = 1

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print("{:2o}".format(d), end="  ")
        d += 1
    print()
