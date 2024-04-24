import math
valor = int(input("Digite um número inteiro: "))

def situacao1(valor):
    if ((valor == 1) or (valor == 2) or (valor == 3)):
        elevado = valor * valor
        print(valor, "elevado ao quadrado é", elevado)
    
    elif ((valor == 4) or (valor == 9)):
        raiz = math.sqrt((valor))
        print ("A raiz quadrada de ", valor, " é", raiz)
    
    elif ((valor == 6) or (valor == 7) or (valor == 8)):
        divisao = valor / 9 
        print ("Esse número dividido por 9 é", divisao)
    
    else:
        print("O nnúmero digitado é inválido ou não possui nenhuma condição")

situacao1(valor)

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")
