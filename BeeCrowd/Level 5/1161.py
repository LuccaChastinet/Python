while True:
  try:
    m,n = input().split(" ")
    m,n = int(m),int(n)
    fatorialm = 1
    fatorialn = 1
    for x in range(m):
      fatorialm = fatorialm*(x+1)
    for y in range(n):
      fatorialn = fatorialn*(y+1)
    print(fatorialn+fatorialm)


  except EOFError:
    break