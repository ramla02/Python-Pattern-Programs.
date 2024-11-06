n = 5

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if y <= n // 2:
            print("0", end="  ")
        else:
            print(1, end="  ")
    print()
