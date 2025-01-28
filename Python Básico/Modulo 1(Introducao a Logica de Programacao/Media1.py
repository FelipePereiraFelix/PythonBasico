# Aqui um exemplos de como usar funções em Python.
# Além do if e else que ja vimos anteriormente.
# Usamos também o def que facilita a criação de códigos.
# Neste exemplo, o programa calcula a média de duas notas e informa se o aluno
# foi aprovado ou reprovado.


def lernotas():
    n = float(input("Digite uma nota para o aluno(a): "))
    return n


def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
resultado(a, b)
