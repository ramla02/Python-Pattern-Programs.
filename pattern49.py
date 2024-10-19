n = 5
d = 1
e = n
for x in range(n, 0, -1):
    t1 = d
    t2 = e
    r1 = x
    r2 = x + 1
    
    for y in range(n, x - 1, -1):
        if (x + y) % 2 == 0:
            print("{:d}".format(t1), end="  ")
        else:
            print("{:2d}".format(t2), end="  ")
        t1 = t1 - r1
        t2 = t2 - r2
        
        r1 = r1 + 1
        r2 = r2 + 1
                
    e = e + x - 1
    d = d + x
    print()

