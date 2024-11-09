n = 5

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if y <= x:
            print("1", end="  ")
        else:
            print("0", end="  ")
    print()
