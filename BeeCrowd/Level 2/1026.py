while True:
    H1,M1,H2,M2 = (input()).split(" ")

    inicio = 0
    fim = 0

    H1 = int(H1)
    M1 = int(M1)
    H2 = int(H2)
    M2 = int(M2)

    if H1==0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    else:
        if H1 == 0:
            inicio = (24*60) + M1
        else:
            inicio = (H1*60) + M1

        if H2 == 0:
            fim = (24*60+M2)
        else:
            fim = (H2*60) + M2
        if fim > inicio:
            print(fim-inicio)
        else:
            print ((24*60)-(inicio-fim))
    
