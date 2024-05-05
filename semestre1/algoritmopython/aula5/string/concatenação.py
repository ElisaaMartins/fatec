# concatenação de 2 trechos de texto

texto1 = "123"
texto2 = "456"
concatenacao = texto1 + texto2
print("Resultado da variavel concatenação = " +concatenacao) # Saida = '123456'

# declaração da variável `a` que foi associado ao texto `bra`
a = "bra"

# declaração da variável `b` que foi associado ao texto `sil`
b = "sil"

# ao escrevemos no prompt a + b temos que é impresso a CONCATENAÇÃO
print("concatenação de a + b = " + (a + b)) # Saida = 'brasil'

# agora, concatenamos e o resultado associamos a variável `c`
c = a + b
print("Resutado da variavel c = " + c) #Saida = 'brasil'

# agora, podemos dizer que o trecho de texto `bra`
# foi adicionado a esquerda da variável `b`
print("concatenação de b + a = " +(b + a)) #Saida = 'silbra'