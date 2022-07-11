tipo = input()
tipo2 = input()
tipo3 = input()

if tipo == "vertebrado":
  if tipo2 == "ave":
    if tipo3 == "carnivoro":
      print("aguia")
    if tipo3 == "onivoro":
      print("pomba")

  if tipo2 == "mamifero":
    if tipo3 == "onivoro":
      print("homem")
    if tipo3 == "herbivoro":
      print("vaca")
    
elif tipo == "invertebrado":
  if tipo2 == "inseto":
    if tipo3 == "hematofago":
      print("pulga")
    if tipo3 == "herbivoro":
      print("lagarta")

  if tipo2 == "anelideo":
    if tipo3 == "hematofago":
      print("sanguessuga")
    if tipo3 == "onivoro":
      print("minhoca")