nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

def aprovacao(idade):
    if (idade >= 65):
        print ("Bem vindo", nome, "você é maior de 65 anos")
    elif (idade >= 18):
        print ("Bem vindo", nome, "você é maior de idade")
    elif (idade < 18):
        print ("Bem vindo", nome, "você é menor de idade")
    else:
        print("Idade inválida")

aprovacao(idade)

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")


