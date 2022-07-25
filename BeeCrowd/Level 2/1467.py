while True:
  try:
    lista = []
    A,B,C = input().split(" ")
    A,B,C = int(A),int(B),int(C)
    lista.append(A),lista.append(B),lista.append(C)
    contador1 = 0
    contador0 = 0
    if A == B and B == C:
      print("*")
    else:
      for x in lista:
        if x == 1:
          contador1 += 1
        else:
          contador0 += 1
      if contador1 > contador0:
        excecao = 0
      if contador0 > contador1:
        excecao = 1
      pos = 0
      for x in lista:
        if x != excecao:
          pos +=1
          pass
        else:
          if pos == 0:
            print("A")
          if pos == 1:
            print("B")
          if pos == 2:
            print("C")
  except EOFError:
    break