n = 10
px = n // 2
py = n // 2

for x in range(1, n + 1):
    for y in range(1, n):
        if (x == 1 or x == n) and y == n // 2:
            print("*", end="  ")
        elif y == px:
            print("/", end="  ")
        elif y == py:
            print("\\", end="  ")
        else:
            print("", end="  ")
            
    if x == n // 2:
        t = px
        px = py
        py = t
    else:
        px -= 1
        py += 1
    print()
