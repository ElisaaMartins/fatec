import random

print("Funções do modulo random")
print("Valor da função random.randrange(50) =",random.randrange(50))
print( "Varlor da função random.randran(0, 60, 1) =",random.randrange(0, 60, 1))

prob = random.random()

print("Varlor da função random.random() =",prob)

lanceDado = random.randrange(1,7) # retorna um int, dentre 1,2,3,4,5,6

print("Valor do dado =", lanceDado)