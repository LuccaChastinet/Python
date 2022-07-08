C = int(input(""))

aux = 0
while C != aux:
    N = int(input(""))

    if  N <=8000:
        print("Inseto!")

    if N > 8000 and N <= 100000:
        print("Mais de 8000!")
    aux = aux + 1