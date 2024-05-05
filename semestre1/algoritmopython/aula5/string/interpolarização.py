# inserção de um trecho de texto dentro de outro

sexo = "masculino"
nome = "Henrique"
interpolar = "Sexo é igual a %s e o nome é igual %s "%(sexo, nome)
print("Saida 1 da interpolação = " + interpolar)

# agora, vamos colocar uma String entre chaves dentro do texto
# em seguida, com a função format(), vamos associar
# os nomes definidos entre chaves a texto passando-os
# como argumentos de função
interpolar = "Sexo é igual a {SEXO} e o nome é igual {NOME} ".format(SEXO=sexo,NOME=nome)
print("Saida 2 da interpolação = " + interpolar)

# Saida = 'Sexo é igual a masculino e o nome é igual Henrique '
