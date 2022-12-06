valor_mes = int(input("Digite o valor investido por mês: "))
anos = int(input("Digite a quantidade de anos com o dinheiro investido: "))
juros = int(input("Digite o juros anuais: "))
juros_mes = juros/12

final = 0
meses = anos*12

for mes in range(meses):
  final = (final+valor_mes)*(1+(juros_mes/100))

projeção =  (final*(1+juros_mes/100)) - final
print(" ")
print(f"O seu patrimônio final é de: {final:.2f} reais")
print(" ")
print(f"Com um total de investimento de: {valor_mes*meses} reais")
print(" ")
print(f"O ganho por juros foi de: {(final-(valor_mes*meses)):.2f} reais")
print(" ")
print(f"Ao final, se não quiser mais nenhum investimento, o retorno mensal com a mesma taxa de juros é de: {projeção:.2f}")
