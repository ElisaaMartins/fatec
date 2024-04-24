print("Funções internas - builtin ou embutidas")

maior_numero = max(5.5, 5.6, 5.7, 8.3) #retorna o máximo
menor_numero = min(3, 6, 7, 10) #retorna o minimo 
maior_letra = max('a', 'b', 'c')
menor_letra = min('a', 'b', 'c')

print("O Nro maximo da lista =", maior_numero)
print("O Nro minimo da lista =", menor_numero)
print("A maior letra da lista =", maior_letra)
print("A menor letra da lista =", menor_letra)

nome = ""
nome.lower() #metodo que deixa letras minusculas
nome.upper() #metodo que deixa letras maiusculas
nome. capitalize() #metodo que deixa apenas a primeira letra maiuscula 

print("Nome em Upper case = " + nome.upper())
print("Nome em Lower case = " + nome.lower())
print("1ra letra com Maiscula = " + nome.capitalize())