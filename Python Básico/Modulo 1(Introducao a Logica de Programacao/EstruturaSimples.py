# O código do exercío que é pedido no curso usa de
# PyCharm, e o código é sem "int" e funciona normalmente.
# Mas aqui houve a necessidade de uasr "int" para que funcionasse o código.
A = int(input("Informe um valor de variável A: "))
B = int(input("Informe um valor de variável B: "))

if A > B:
    aux = A
    A = B
    B = aux
print("O valor da variável A agora é: ", A)
print("O valor da variável B agora é: ", B)
