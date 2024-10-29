n = 5
d = 1
e = n * (n * 2) - (n - 1)

for x in range(1, n + 1):
    px = d
    py = e
    
    for y in range(1, n + 1):
        if x <= n // 2 + 1:
            print("{:3d}".format(px), end=" ")
            px += 1
        else:
            print("{:3d}".format(py), end=" ")
            py += 1
    print()
    d = d + (n * 2)
    e = e - (n * 2)
