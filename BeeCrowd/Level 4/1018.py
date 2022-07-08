din = int(input())
dinoriginal=din
nota100 = din//100
din = din-(nota100*100)
nota50 = din//50
din = din-(nota50*50)
nota20 = din//20
din = din-(nota20*20)
nota10 = din//10
din = din-(nota10*10)
nota5 = din//5
din = din-(nota5*5)
nota2 = din//2
din = din-(nota2*2)
nota1 = din


print(dinoriginal)
print(nota100, "nota(s) de R$ 100,00")
print(nota50, "nota(s) de R$ 50,00")
print(nota20, "nota(s) de R$ 20,00")
print(nota10, "nota(s) de R$ 10,00")
print(nota5, "nota(s) de R$ 5,00")
print(nota2, "nota(s) de R$ 2,00")
print(nota1, "nota(s) de R$ 1,00")