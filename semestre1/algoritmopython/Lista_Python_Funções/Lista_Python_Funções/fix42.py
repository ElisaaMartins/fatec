nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))



def mediaAluno (nota1, nota2):
    media = (nota1 + nota2) / 2 
    if (media >= 7):
        print ("Parabéns, você está aprovado! Média =", media)
        return media
    elif (media < 7):
        print ("Você ainda tem uma chance! Estude mais para o exame. Média =", media)
        return media
    else:
        print("Nota digitada inválida")

mediaAluno(nota1, nota2)

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")

