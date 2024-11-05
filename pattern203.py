for x in range(0, 5):
    for y in range(1, 6):
      if y <= x:
          print("0", end="  ")
      else:
          print(x + y, end="  ")
    print()
