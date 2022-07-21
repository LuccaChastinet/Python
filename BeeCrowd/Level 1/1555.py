N = int(input())
contador = 0

while contador < N:
  x,y = input().split(" ")
  x,y = int(x), int(y)

  R = (3*x)**2 + y**2
  B = 2*(x**2) + (5*y)**2
  C = -100*x + y**3
  
  if R > B and R > C:
    print("Rafael ganhou")
  if B > R and B > C:
    print("Beto ganhou")
  if C > R and C > B:
    print("Carlos ganhou")

  contador +=1