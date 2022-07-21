N = int(input())
contador = 0
while contador < N:
  num = int(input())
  caracteristica = ""
  sinal = ""
  if num == 0:
    print("NULL")
    pass
  else:
    if num % 2 == 0:
      caracteristica = "EVEN"
    else:
      caracteristica = "ODD"
    if num > 0:
      sinal = "POSITIVE"
    else:
      sinal = "NEGATIVE"
  
    print(f"{caracteristica} {sinal}")
  contador += 1