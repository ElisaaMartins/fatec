nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
notaExame = float(input("Digite a nota que tirou no exame: "))

media = ((nota1 + nota2) / 2 ) / 2

if (media >= 5):
    print ("Parabéns, você aproveitou a sua chance! Está aprovado. Média =", media)
elif (media < 5):
    print ("Estude mais para a próxima. Você não alcançou o mínimo necessário. Média =", media)
else:
    print("Nota inválida")

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")


