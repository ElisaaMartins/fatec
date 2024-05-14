# usando math.ceil(), uma biblioteca do Python para fazer o arredondamento(para cima) dos resutados, pq a divisão por parte inteira (//) não vai
import math 

area = float(input("Digite a área que será pintada: "))

# é dividido por 6 pq 1 lata cobre 6m^2
quantDeTinta = (area / 6) + (10 * 0.10)

# situação a
quantLata = math.ceil(quantDeTinta / 18)
precoLata = quantLata * 80

# situação b
quantGalao = math.ceil(quantDeTinta / 3.6)
precoGalao = quantGalao * 35

# situação c
misturaLata = math.ceil(quantDeTinta / 18)
misturaGalao = math.ceil((quantDeTinta % (misturaLata * 18)) / 3.6)
precoGalaoLata = (misturaGalao * precoGalao) + (misturaLata * precoLata)

print("Quantidade de tinta a ser comprada:", quantDeTinta, "litros")
print("Situação a) Comprar apenas latas de 18 litros: ", quantLata, 
      "latas - Preço total: R$", precoLata)
print("Situação b) Comprar apenas galões de 3,6 litros: ", quantGalao, 
      "galões - Preço total: R$", precoGalao)
print("Situação c) Misturar latas e galões para o menor preço: ", misturaLata, 
      "latas e ", misturaGalao, "galões - Preço total: R$ ", precoGalaoLata)

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")



