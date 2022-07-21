N = int(input())

for num in range(N+1):
  if num % 2 == 0 and num != 0:
    print(f"{num}^2 = {num**2}")
