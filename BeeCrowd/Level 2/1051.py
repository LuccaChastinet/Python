salario = float(input())

if salario <= 2000:
  print("Isento")

if salario > 2000 and salario <= 3000:
  print(f"R$ {(((salario-2000)*8)/100):.2f}")

if salario > 3000 and salario <= 4500:
  imposto = 80 + (((salario-3000)*18)/100)
  print(f"R$ {imposto:.2f}")

if salario > 4500:
  imposto = 350 + (((salario-4500)*28)/100)
  print(f"R$ {imposto:.2f}")
