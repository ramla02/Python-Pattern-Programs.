n = 4

for x in range(1, n + 1):
    for y in range(1, n * 2):
        if y == x or y == 2 * n - x or y == n:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()
