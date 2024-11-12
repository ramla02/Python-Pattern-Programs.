n = 5

for x in range(n - 1, - 1, - 1):
    for y in range(0, n):
        print(abs(x - y), end="  ")
    print()
