I = 1
J = 7
contador = 0

while J<=15:
  print(f"I={I} J={J}")
  contador +=1
  if contador > 2:
    I += 2 
    J += 4
    contador = 0
  else:
    J -=1
