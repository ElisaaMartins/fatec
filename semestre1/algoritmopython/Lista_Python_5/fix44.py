nome = str(input("Digite o nome do aluno: "))
n1 = float(input("Digite a nota da avaliação1: "))
n2 = float(input("Digite a nota da avaliação2: "))

media = (n1 * 4 + n2 * 6) / 10

if (media >= 9) & (media <= 10): 
    print("Aprovado - A")
elif (media >= 7) & (media <= 9):
    print("Aprovado - B")
elif (media >= 3) & (media <= 7): 
    print("Exame - C")
elif (media >= 0) & (media <= 3): 
    print("DP - D")
else:
    print("nota invalida")

print("Elisa Ap. Martins de Oliveira  RA:1051392411023 - Turma DSM 1°Semestre")


