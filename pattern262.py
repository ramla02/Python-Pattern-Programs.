n = 5

for x in range(1, n + 1):
    for y in range(1, x + 1):
        if y % 2 == 0:
            print("*", end="  ")
        else:
            print("#", end="  ")
    print()
