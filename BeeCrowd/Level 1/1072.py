N = int(input())
contador = 0
lista = []
while contador < N:
  num = int(input())
  lista.append(num)
  contador +=1

dentro = 0
fora = 0
for x in lista:
  if x >= 10 and x <= 20:
    dentro +=1
  else:
    fora +=1

print(f"{dentro} in")
print(f"{fora} out")
  