contador = 0
num = 0
lista = []
maior = 0
while contador < 100:
  num = int(input())
  lista.append(num)
  contador +=1

for x in lista:
  if x > maior:
    maior = x

print(maior)
print(lista.index(maior)+1)


