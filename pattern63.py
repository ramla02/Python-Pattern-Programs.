n = 5

for x in range(1, n + 1):
    for y in range(1, x + 1):
        print(str((x + y) % 2) + " ", end=" ")
    print()
