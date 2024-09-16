n = 5

for x in range(1, n + 1):
    for y in range(0, n):
        print(str((x * y) % 2) + " ", end=" ")
    print()
