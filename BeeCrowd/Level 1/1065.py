N = 5
contador = 0
valor = 0
while contador < N:
  num = int(input())
  if num % 2 == 0:
    valor +=1
  contador +=1

print(f"{valor} valores pares")