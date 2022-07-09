from num2words import num2words

def funcao():
  contador = 1
  x = int(input())
  num = num2words(x)
  
  while contador <1000:
    num = num2words(len(num))
    contador +=1
  return len(num)

print(funcao())