N = int(input())

horas = N//3600
N = N-(horas*3600)
minutos = N//60
N = N-(minutos*60)

print("{}:{}:{}".format(horas,minutos,N))