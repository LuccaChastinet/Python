F1,F2 = (input()).split(" ")

F1 = float(F1)
F2 = float(F2)

F2 = F2/100

total = 100 + F1

total = total + ((100+F1) * F2) - 100

print ('%2f'% total)

