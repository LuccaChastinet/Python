salario = float(input())

if salario > 0 and salario <= 400:
  nsalario = salario + (salario*15)/100
  reajuste = nsalario - salario
  print(f"Novo salario: {nsalario:.2f}")
  print(f"Reajuste ganho: {reajuste:.2f}")
  print("Em percentual: 15 %")

if salario > 400 and salario <= 800:
  nsalario = salario + (salario*12)/100
  reajuste = nsalario - salario
  print(f"Novo salario: {nsalario:.2f}")
  print(f"Reajuste ganho: {reajuste:.2f}")
  print("Em percentual: 12 %")

if salario > 800 and salario <= 1200:
  nsalario = salario + (salario*10)/100
  reajuste = nsalario - salario
  print(f"Novo salario: {nsalario:.2f}")
  print(f"Reajuste ganho: {reajuste:.2f}")
  print("Em percentual: 10 %")

if salario > 1200 and salario <= 2000:
  nsalario = salario + (salario*7)/100
  reajuste = nsalario - salario
  print(f"Novo salario: {nsalario:.2f}")
  print(f"Reajuste ganho: {reajuste:.2f}")
  print("Em percentual: 7 %")

if salario > 2000:
  nsalario = salario + (salario*4)/100
  reajuste = nsalario - salario
  print(f"Novo salario: {nsalario:.2f}")
  print(f"Reajuste ganho: {reajuste:.2f}")
  print("Em percentual: 4 %")