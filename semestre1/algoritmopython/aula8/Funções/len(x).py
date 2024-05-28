#dicionario = {'1ra_chave':'1ro_valor’, '2a_chave':’2do_valor}
#Chave = Frutas
#Valor = Quantidade
estoqueFrutas1 = {'kiwis': 430,
 'bananas': 312,
 'laranjas': 525,
 'peras': 217
 }
print("Conteúdo completo do dicionário (estoque) = " , estoqueFrutas1)
estoqueFrutas1['bananas'] = estoqueFrutas1['bananas'] + 200
numItens = len(estoqueFrutas1)
print("Numero de itens = " , numItens)
print("Estoque de bananas = ", estoqueFrutas1['bananas'])
print("Estoque total de frutas = ", estoqueFrutas1)