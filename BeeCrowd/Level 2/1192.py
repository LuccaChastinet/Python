N = int(input())
for x in range(N):
  lista = []
  num = str(input())
  for x in num:
    lista.append(x)
  letra = lista[1]
  if lista[0] == lista[2]:
    print(int(lista[0])**2)
  else:
    if letra.isupper():
      print(int(lista[2])-int(lista[0]))
      pass
    if letra.islower():
      print(int(lista[0]) + int(lista[2]))
      pass
  