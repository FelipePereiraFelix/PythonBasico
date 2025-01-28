# Máscara de Formatação na prática

codigo = int(input("Digite o codigo do funcionário"))
nome = input("Digite o nome do funcionário")
salario = float(input("Digite o salario do funcionário"))
ativo = True

"""
Summary:
    Este código demonstra a formatação de diferentes tipos de dados
    em Python,
    utilizando o operador `%` para exibir variáveis de tipos
    distintos
    (inteiro, string,
    float e booleano) com a formatação apropriada.

Args:
    Nenhum parâmetro de entrada é utilizado neste código.

Returns:
    Nenhum valor é retornado, o código apenas imprime as variáveis formatadas.

Exemplo de Saída:
    Codigo: 105
    Nome: Jose Santana
    Salario: 1650.000000
    Ativo: True
"""


print("Codigo: %d " % codigo)
print("Nome: %s " % nome)
print("Salario: %2f " % salario)
print("Ativo: %r " % ativo)
