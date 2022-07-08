A,B,C = input().split(" ")
pi = 3.14159

A = float(A)
B = float(B)
C = float(C)

areaT = (A*C)/2
areaC = pi*C*C
areaTrap = ((A+B)*C)/2
areaQ = B**2
AreaR = A*B

print(f"TRIANGULO: {areaT:.3f}")
print(f"CIRCULO: {areaC:.3f}")
print(f"TRAPEZIO: {areaTrap:.3f}")
print(f"QUADRADO: {areaQ:.3f}")
print(f"RETANGULO: {AreaR:.3f}")