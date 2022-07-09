x,y = input().split()
x,y = int(x),int(y)

if x == y:
  print(f"O JOGO DUROU {24} HORA(S)")

if x < y:
  print(f"O JOGO DUROU {(y-x)} HORA(S)")

if x > y:
  print(f"O JOGO DUROU {(24-x+y)} HORA(S)")