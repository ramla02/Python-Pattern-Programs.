n = 5

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if y <= x:
            print(str(n - x + 1) + "", end="  ")
        else:
             print(chr(x + 64) + "", end="  ")
    print()
