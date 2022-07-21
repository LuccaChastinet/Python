n = int(input())

if n % 2 == 0:
  total = n**2
  print(f"{total//2} casas brancas e {total//2} casas pretas")
else:
  total = n**2
  metade = total//2
  print(f"{metade+1} casas brancas e {metade} casas pretas")
