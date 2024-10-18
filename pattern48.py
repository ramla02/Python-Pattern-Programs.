a = 1
for x in range(5, 00, - 1):
    b = x;
    t = a;
    for y in range(6, x, - 1):
        print("{:2d}".format(t), end="  ")
        t = t - b
        b += 1
    a = a + x
    print()
