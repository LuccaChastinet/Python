def josephus(n, k):
    i = 1
    retorno = 0
    while i < n:
      retorno = (retorno + k) % i
      i += 1
    return retorno


while True:
  quantidade = int(input())
  if quantidade == 0:
    break
  pulo = 1
  while True:
    if josephus(quantidade,pulo) != 11:
      pulo +=1
    else:
      break
  print(pulo)
