#dicionario = {'1ra_chave':'1ro_valor’, '2a_chave':’2do_valor}
#Chave = Nome
#Valor = Telefone
retornar_ligacao = {
 "Andre": 30301122,
 "Carlos": 33547877,
 "Ana": 33381245,
 "Timoteo": 36458899
 }
print("Ligações pendentes", retornar_ligacao)
retornar_ligacao.popitem() # Exclui o ultimo par (chave/valor) do dicionario ("Timoteo": 36458899)
print("Ligações pendentes", retornar_ligacao)
retornar_ligacao.popitem() # Exclui o ultimo par (chave/valor) do dicionario ("Ana": 33381245)
print("Ligações pendentes", retornar_ligacao)
