while True:
    X1,Y1,X2,Y2 = (input()).split(" ")

    X1 = int(X1)
    Y1 = int(Y1)
    X2 = int(X2)
    Y2 = int(Y2)

    if X1==0 and Y1 == 0 and X2 == 0 and Y2 == 0:
        break
    else:
        if X1 == X2 and Y1 == Y2:
                print(0)
        else:
            if X1 == X2 or Y1 == Y2:
                print(1)
            else:
                if ((X2-X1) == -(Y2-Y1) or -(X2-X1) == -(Y2-Y1) or -(X2-X1) == (Y2-Y1) or (X2-X1) == (Y2-Y1)):
                    print(1)
                else:
                    print(2)

        
            