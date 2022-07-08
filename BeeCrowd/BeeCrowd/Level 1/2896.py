T = int(input())

while T != 0:
    N,K = input().split(" ")
    N = int(N)
    K = int(K)
    if N > K:
        print((N%K) + (N//K))
    if N < K:
        print(N)
    if N == K:
        print("1")
    T= T-1