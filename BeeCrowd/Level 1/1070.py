x = int(input())
contadorpar = 1
contadorimp = 2
if x % 2 == 0:
  while contadorpar < 12:
    print(x +contadorpar)
    contadorpar += 2
else:
  print(x)
  while contadorimp < 12:
    print(x+contadorimp)
    contadorimp += 2
