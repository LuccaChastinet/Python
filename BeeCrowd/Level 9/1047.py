x,y,z,w = input().split()
x,y,z,w = int(x),int(y),int(z),int(w)

if x == z and y == w: 
  print(f"O JOGO DUROU {24} HORA(S) E 0 MINUTO(S)")

if x > z:
  if y > w:
    print(f"O JOGO DUROU {24-x+z} HORA(S) E {(60-y+w)} MINUTO(S)")
  else:
    print(f"O JOGO DUROU {24-x+z} HORAS(S) E {y-w} MINUTO(S)")

if x < z:
  if z-x == 1:
    print(f"O JOGO DUROU 0 HORA(S) E {60-y+w} MINUTO(S)")
  elif y > w:
    print(f"O JOGO DUROU {z-x} HORA(S) E {60-y+w} MINUTO(S)")
  else:
    print(f"O JOGO DUROU {z-x} HORA(S) E {w-y} MINUTO(S)")

