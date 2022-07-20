N = 6
contador = 0
valores = 0
media = 0
while contador < N:
  num = float(input())
  if num > 0:
    valores +=1
    media += num
  contador +=1

print(f"{valores} valores positivos")
print(f"{media/valores:.1f}")