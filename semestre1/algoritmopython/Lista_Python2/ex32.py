nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 7):
    print ("Parabéns, você está aprovado! Média =", media)
elif (media < 7):
    print ("Você ainda tem uma chance! Estude mais para o exame. Média =", media)
else:
    print("Nota inválida")

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")

