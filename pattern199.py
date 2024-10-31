# prime number pattern

n = 5
cn = 1

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for p in range(cn + 1, 10000):
            cn = p
            count = 0
            
            for z in range(1, cn + 1):
                if cn % z == 0:
                    count += 1
                    
            if count == 2:
                print("{:2d}".format(cn), end="  ")
                break
    print()
