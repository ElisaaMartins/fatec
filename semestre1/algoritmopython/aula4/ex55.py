def func():
 num = 1 # variável local na função
 print("Resultado da variavel local num = ", num)

print("Exemplo de variavel local e global com funções")

num = 10 # variável global

func() # chama a função

print("Resultado da variavel global num = ", num)

print("Obs: Não é recomendavel utilizar o mesmo nome para as variavel local e global")

# Rsumindo
# Função (Variavel local) --> num = 1
# Aplicação (Variavel global) --> num = 10