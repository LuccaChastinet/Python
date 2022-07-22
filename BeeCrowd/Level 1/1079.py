N = int(input())

for x in range(N):
  a,b,c = input().split(" ")
  a,b,c = float(a),float(b),float(c)
  print(f"{((a*2 + b*3 + c *5)/10):.1f}")