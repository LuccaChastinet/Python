import math

a,b,c = input().split(" ")
a,b,c = float(a),float(b),float(c)

delta = (b**2 - 4*a*c)
if a == 0.0:
  print("Impossivel calcular")
else:
  if delta < 0:
    print("Impossivel calcular")

  if  delta == 0:
    x = -b/(2*a)
    print("a raiz desta equação é",x)

  if delta > 0:
    deltaraiz = math.sqrt(b**2 - 4*a*c)
    y = (-b - deltaraiz)/(2*a)
    x = (-b + deltaraiz)/(2*a)
    
    print(f"R1 = {x:.5f}")
    print(f"R2 = {y:.5f}")

