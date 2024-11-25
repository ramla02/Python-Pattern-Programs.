decr = 9

for x in range(5, 0, - 1):
    for y in range(x, 5):
        print(" ", end=" ")
    for z in range(1, decr + 1):
        print(z, end=" ")
    decr -= 2
    print()
