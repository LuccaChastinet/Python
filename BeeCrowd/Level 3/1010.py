peça1,num1,valor1 = input().split(" ")
peça1 = int(peça1)
num1 = int(num1)
valor1 = float(valor1)

peça2,num2,valor2 = input().split(" ")
peça2 = int(peça2)
num2 = int(num2)
valor2 = float(valor2)

valorfinal = num1*valor1 + num2*valor2


print("VALOR A PAGAR: R$ %.2f" % valorfinal)
