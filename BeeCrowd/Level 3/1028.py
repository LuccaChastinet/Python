n = int(input())

def mdc(a,b):
  while b:
    a,b = b,a%b
  return a

for x in range(n):
  f1,f2 = input().split()
  f1,f2 = int(f1),int(f2)
  print(mdc(f1,f2))