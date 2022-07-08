N = float(input())

nota100 = N//100
N = N-(nota100*100)
nota50 = N//50
N = N-(nota50*50)
nota20 = N//20
N = N-(nota20*20)
nota10 = N//10
N = N-(nota10*10)
nota5 = N//5
N = N-(nota5*5)
nota2 = N//2
N = N-(nota2*2)
moeda1 = N//1
N = N-(moeda1*1)
moeda50 = N//0.5
N = N-(moeda50*0.5)
moeda25 = N//0.25
N = N-(moeda25*0.25)
moeda10 = N//0.10
N = N-(moeda10*0.10)
moeda05 = N//0.05
N = N-(moeda05*0.05)
moeda01 = N//0.01
N = N-(moeda01*0.01)



print("NOTAS:")
print(int(nota100), "nota(s) de R$ 100.00")
print(int(nota50), "nota(s) de R$ 50.00")
print(int(nota20), "nota(s) de R$ 20.00")
print(int(nota10), "nota(s) de R$ 10.00")
print(int(nota5), "nota(s) de R$ 5.00")
print(int(nota2), "nota(s) de R$ 2.00")

print("MOEDAS:")
print(int(moeda1), "moeda(s) de R$ 1.00")
print(int(moeda50), "moeda(s) de R$ 0.50")
print(int(moeda25), "moeda(s) de R$ 0.25")
print(int(moeda10), "moeda(s) de R$ 0.10")
print(int(moeda05), "moeda(s) de R$ 0.05")
print(int(moeda01), "moeda(s) de R$ 0.01")