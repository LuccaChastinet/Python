L,R = 1,1

while L != 0 and R != 0:
  L,R = input().split()
  L,R = int(L),int(R)
  if L != 0 and R != 0:
    print(L+R)