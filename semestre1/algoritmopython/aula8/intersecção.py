#MESCLANDO ITENS DE 2 DICIONÁRIOS
#dicionario = {'1ra_chave':'1ro_valor’, '2a_chave':’2do_valor}
#Chave = Frutas
#Valor = Quantidade
estoqueFrutas1 = {'kiwis': 430,
 'bananas': 312,
 'laranjas': 525,
 'peras': 217
 }
estoqueFrutas2 = {'mangas': 130,
 'abacaxis': 150,
 'uvas': 325,
 'ameixas': 517
 }
print("Calculo da Soma (total) de frutas no estoque de frutas1 + estoque de frutas2")
estoqueFrutas1.update(estoqueFrutas2)
print("Total de frutas no estoque 1 ",estoqueFrutas1)
