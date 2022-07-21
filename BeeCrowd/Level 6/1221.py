import math
def éprimo(n):
    if n%2 == 0 and n>2:
        return False
    return all(n%i for i in range(3,int(math.sqrt(n))+1, 2))


N = int(input())
for _ in range(N):
    a = int(input())
    if (éprimo(a)):
        print('Prime')
    else:
        print('Not Prime')