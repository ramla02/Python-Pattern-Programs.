n = 5
ch = 0

for x in range(0, n):
    for y in range(0, n):
        print(chr(x + y + 65) + " ", end=" ")
        if (ch < 26):
            ch += 1
        else:
            ch = 0
    print()
