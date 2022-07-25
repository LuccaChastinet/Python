while True:
  x,y = input().split()
  carry = 0
  mais = 0
  
  if x == "0" and y == "0":
    break
  while len(x) < len(y):
    x = "0" + x
  while len(y) < len(x):
    y = "0"+ y

  for i in reversed(range(0,len(x))):
    if (int(x[i]) + int(y[i])) > 9 or (int(x[i]) + int(y[i]) + mais) > 9:
      carry += 1
      mais = 1
    else:
      mais = 0
  if carry == 0:
    print("No carry operation.")
  elif carry == 1:
    print("1 carry operation.")
  else:
    print("%d carry operations."% carry)
