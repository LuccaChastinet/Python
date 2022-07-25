while True:
    n = int(input())
    
    if not n:
        break
    
    dX, dY = input().split(' ')
    dX = int(dX)
    dY = int(dY)

    for x in range(n):
        x, y = input().split(' ')
        x = int(x)
        y = int(y)

        if x == dX or y == dY:
            print ("divisa")
        elif x > dX and y > dY:
            print ("NE")
        elif x > dX and y < dY:
            print ("SE")
        elif x < dX and y > dY:
            print ("NO")
        else:
            print ("SO")