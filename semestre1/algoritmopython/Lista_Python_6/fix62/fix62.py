arq = open('./Lista_Python_6/fix62/emails.txt', 'r', encoding="utf-8")
email = arq.read()

lista_email = email.split('\n')

for _ in range(3):
    novo_email = str(input("Digite um email aqui: "))
    lista_email.append(novo_email)
    print("Emails adicionados com sucesso!")

print(arq.read())

print (lista_email)
print("Elisa Aparecida Martins de Oliveira - RA: 1051392411023 - Turma DSM 1°Semestre")
arq.close()
