# Como definir os tipos:

codigo = 10
salario = 1500.00
nome = "Jose"
situação = True

tipo = type(salario)

print(salario)
print(tipo)

# Concatenação:
codigo = 10
salario = 1500.00
nome = "Jose"
print("Codigo: ", codigo, "Nome: ", "O salario atual e de ", salario)

# Concatenando para converter valores que não são string para string.
codigo = 10
salario = 1500.00
nome = "Jose"

print(
    "Codigo: "
    + str(codigo)
    + " Nome: "
    + nome
    + " O salario atual e de "
    + str(salario)
)
