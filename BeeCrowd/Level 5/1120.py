num = int
teste = int

while num != "0" and teste != "0":
  lista = []
  listaprint= []
  excecao = []
  num, teste = input().split()
  if num == "0" and teste == "0":
    break
  for x in teste:
    lista.append(x)
  for y in lista:
    if y != num:
      listaprint.append(y)
  final = "".join(listaprint)
  if len(listaprint) == 0:
    print("0")

  elif listaprint[0] == "0":
    lucca = []
    numero = "".join(listaprint)
    lucca.append(numero)
    res = [ele.lstrip("0") for ele in lucca]
    if res[0] == "":
      print("0")
    else:
      print(res[0])
  else:
    print(final)


  