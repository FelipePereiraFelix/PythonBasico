# Está linha de código serve para ilustrar como While funciona.
# E serve também para mostrar como While é diferente de For.

qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1
    # Entrada de valores
    valor = float(input("Digite um valor: "))

# Caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n total da Soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média dos valores: ", media)
