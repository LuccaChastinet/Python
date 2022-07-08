import sys
sys.setrecursionlimit(100000000) # Cuidado, pode mexer com o computador, qualquer coisa, é só definir pra 1000 novamente e rodar o programa por completo
def josephus(n, k):
    if(n == 1):
        return 1
    else:
        return (josephus(n - 1, k) + k-1) % n + 1; 

nc = int(input())

for i in range(nc):
    n, m = input().split()
    n = int(n)
    m = int(m)

    j = josephus(n, m)
    print("Case {0}: {1}".format(i+1,j)) 