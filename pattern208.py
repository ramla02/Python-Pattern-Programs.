n = 5

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y:
            print(str(x) + "", end="  ")
        else:
            print("0", end="  ")
    print()
