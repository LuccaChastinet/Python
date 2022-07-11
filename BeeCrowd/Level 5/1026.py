def Main(a, b):
  print(a^b)

while True:
  try:
    a, b = map(int ,input().split())
  except EOFError:
    break
  Main(a, b)