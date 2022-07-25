N = int(input())
lista = []
for x in range(N):
  num = int(input())
  lista.append(num)
lista.sort()

for x in range(0,2001):
  if lista.count(x) != 0:
    quantidade = lista.count(x)
    print(f"{x} aparece {quantidade} vez(es)")
