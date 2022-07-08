N = int(input())
contador = 0

while contador < N:
  lista = []
  texto = input()
  texto = list(texto)
  for x in texto:
    if x.isalpha():
      x = ord(x)+3
      x = chr(x)
      lista.append(x)
    else:
      lista.append(x)
  lista.reverse()
  contador2 = (len(lista))//2
  for x in lista[contador2:]:
    x = ord(x)-1
    x = chr(x)
    lista[contador2] = x
    contador2 += 1

  contador += 1
  final ="".join(lista)
  print(final)
  

