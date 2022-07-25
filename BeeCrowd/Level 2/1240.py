N = int(input())

for x in range(N):
  maior,menor = input().split()
  if len(maior) < len(menor):
    print("nao encaixa")
  else:
    if maior[len(maior) - len(menor): len(maior)] == menor:
      print("encaixa")
    else:
      print("nao encaixa")
  

