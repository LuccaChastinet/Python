N = int(input())

M = int(input())

fig = [0] * N

while M != 0:
    
    M= M-1
    fig[int(input()) -1] = 1

falta = fig.count(0)
print(falta)