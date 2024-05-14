import os

diretorioCorrente = os.getcwd()

print("Vc está no seguinte diretorio")
print(diretorioCorrente)

arq = open('./aula6/saudacao.txt', 'r', encoding="utf-8")
saudacao = arq.read()

print(arq.read())

#print(arq.readline())
#print(arq.readlines())
lista_saudacao = saudacao.split('\n')

print(lista_saudacao)
arq.close()
