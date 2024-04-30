texto = "Toda string em Python é imutável"
novaLista = texto.split(" ")
print(texto.split(" "))
print(novaLista)
print(novaLista[3] +" "+ novaLista[5])
print(id(texto))
print(id(novaLista))