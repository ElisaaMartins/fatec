n1 = int(input("Digite a nota do primeiro aluno: "))
n2 = int(input("Digite a nota do segundo aluno: "))
n3= int(input("Digite a nota do terceiro aluno: "))
n4 = int(input("Digite a nota do quarto aluno: "))
n5 = int(input("Digite a nota do quinto aluno: "))

maiorNota =+1

if n1 > 10 or n2 > 10 or n3 > 10 or n4 > 10 or n5 > 10:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
else:
    while (maiorNota <= 10):
        if n1 > maiorNota:
            maiorNota = n1
        if n2 > maiorNota:
            maiorNota = n2
        if n3 > maiorNota:
            maiorNota = n3
        if n4 > maiorNota:
            maiorNota = n4
        if n5 > maiorNota:
            maiorNota = n5
        print("A maior nota da turma é", maiorNota)
        break

print("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")

