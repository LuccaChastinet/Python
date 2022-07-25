while True:
  try:
    a,b = input().split(" ")
    a,b = int(a),int(b)
    print(a*b*2)

  except EOFError:
    break