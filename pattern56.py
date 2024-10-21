n = 5
for x in range(1, n + 1):
    k = x
    for y in range(1, x + 1):
        print(str(k) + "", end="  ")
        k = k + (n - y)
    print()
