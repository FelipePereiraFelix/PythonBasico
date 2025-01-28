# Aqui faremos um cáculo de média de notas de um aluno.
notaA = float(input("Informe a primeira nota: "))
notaB = float(input("informe a segunda nota: "))

# calcular media
mediafinal = (notaA + notaB) / 2

# Verificação
if mediafinal >= 7.0:
    print("A Media: %.1f - Aprovado" % mediafinal)
else:
    print("A Media: %.1f - Reprovado" % mediafinal)
