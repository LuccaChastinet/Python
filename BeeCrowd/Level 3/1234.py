while True:
    try:
        a=0
        b=str(input("")) 
        c="" 
        for i in b: 
            if i!=' ': 
                a=a+1 
            if a%2==0: 
                c=c+i.lower() 
            else: c=c+i.upper()

        print(c)
    except EOFError:
        break