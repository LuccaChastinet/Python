while True:
  try:
    A,B = input().split()
    A,B = int(A),int(B)
    total = abs(A-B)
    print(total)
  except EOFError:
    break