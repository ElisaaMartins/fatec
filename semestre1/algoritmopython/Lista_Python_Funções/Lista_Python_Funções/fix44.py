import math
valor = int(input("Digite um número inteiro: "))

multiplo = valor % 3

def fix44(valor):
    if ((valor == 1) or (valor == 2)):
        elevado = valor * valor * valor
        print(valor, "elevado ao cubo é", elevado)
    
    elif (multiplo == 0):
        fatorial = math.factorial((valor))
        print ("O fatorial de", valor, " é", fatorial )

    elif ((valor == 4) or (valor == 5) or (valor == 7) or (valor == 8)):
        divisao = valor / 9 
        print ("Esse número dividido por 9 é", divisao)
    
    else:
        print("Valor inválido")

fix44(valor)

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")
