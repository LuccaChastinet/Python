N = int(input())

ano = N//365
N = N-(ano*365)
mes = N//30
N = N-(mes*30)

print(ano,"ano(s)")
print(mes,"mes(es)")
print(N,"dia(s)")