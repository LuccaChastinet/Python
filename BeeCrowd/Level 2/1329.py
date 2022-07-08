while True:
    N = int(input())
    
    
    if N == 0:
        break
    else:
        X = list(map(int,input().split()))
        Maryvenceu = 0
        johnvenceu = 0
        for v in X:
            if(v==0):
                Maryvenceu = Maryvenceu + 1
            else:
                johnvenceu = johnvenceu + 1

    print("Mary won %d times and John won %d times" %(Maryvenceu,johnvenceu))
