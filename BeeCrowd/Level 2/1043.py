a,b,c = input().split()
a,b,c = float(a),float(b),float(c)

if abs(b - c)  < a < b + c or abs(a - c)  < b < a + c or abs(a - b)  < c < a + b:
  print(f"Perimetro = {(a+b+c):.1f}")
else:
  print(f"Area = {(((a+b)*c)/2):.1f}")
