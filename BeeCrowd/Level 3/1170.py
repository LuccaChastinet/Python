N = int(input())
contador = 0

while contador < N:
  comida = float(input())
  dias = 0
  
  while comida > 1:
    comida = comida/2
    dias +=1
  print(f"{dias} dias")
  contador +=1