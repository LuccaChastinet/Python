N = int(input())
contador = 0
while contador < N:
  valor = 0
  num = str(input())
  for x in num:
    if x == "1":
      valor += 2
    if x == "2":
      valor += 5
    if x == "3":
      valor += 5
    if x == "4":
      valor += 4
    if x == "5":
      valor += 5
    if x == "6":
      valor += 6
    if x == "7":
      valor += 3
    if x == "8":
      valor += 7
    if x == "9":
      valor += 6
    if x == "0":
      valor += 6
  contador += 1
  print(f"{valor} leds")

  