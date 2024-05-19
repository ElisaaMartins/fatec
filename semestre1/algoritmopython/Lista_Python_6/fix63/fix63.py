arq = open('./Lista_Python_6/fix63/senhas.txt', 'r', encoding="utf-8")
senha = arq.read()

listaSenha = senha.split('\n')
print(arq.read())

for _ in range(5):
    novaSenha = str(input("Digite sua senha aqui: "))
    listaSenha.append(novaSenha)
    print("Senhas adicionados com sucesso!")

print (listaSenha)
print("Elisa Aparecida Martins de Oliveira - RA: 1051392411023 - Turma DSM 1°Semestre")
arq.close()
