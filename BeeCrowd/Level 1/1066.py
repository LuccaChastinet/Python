N = 5
contador = 0
valorpar = 0
valorimp = 0
valorpos = 0
valorneg = 0
while contador < N:
  num = int(input())
  if num % 2 == 0:
    valorpar += 1
  else:
    valorimp += 1
  if num < 0:
    valorneg += 1
  if num > 0:
    valorpos += 1
  contador +=1

print(f"{valorpar} valor(es) par(es)")
print(f"{valorimp} valor(es) impar(es)")
print(f"{valorpos} valor(es) positivo(s)")
print(f"{valorneg} valor(es) negativo(s)")