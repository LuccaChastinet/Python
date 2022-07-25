N = int(input())
coelho = 0
rato = 0
sapo = 0
total = 0
for x in range(N):
  num,animal = input().split()
  num = int(num)
  if animal == "C":
    coelho += num
  if animal == "R":
    rato += num
  if animal == "S":
    sapo += num
  total += num

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {((coelho/total)*100):.2f} %")
print(f"Percentual de ratos: {((rato/total)*100):.2f} %")
print(f"Percentual de sapos: {((sapo/total)*100):.2f} %")
