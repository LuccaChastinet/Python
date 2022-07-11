contador = 0
lista = []
while contador < 6:
  num = float(input())
  if num > 0:
    lista.append(num)
  contador +=1

print(f"{len(lista)} valores positivos")
