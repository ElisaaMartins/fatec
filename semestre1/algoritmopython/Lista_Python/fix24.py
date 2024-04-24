genero = input("Digite seu genero: ")
altura = float(input("Digite sua altura: "))

pesoMulheres = (62.1 * altura) - 44.7 
pesoHomens = (72.7 * altura) - 58

if (genero == "mulher"):
    print ("Seu peso ideal é:", pesoMulheres)
elif (genero == "homem"):
    print ("Seu peso ideal é:", pesoHomens)
else:
    print ("Valor digitado é inválido. Escolha 'homem' ou 'mulher'")


print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")
