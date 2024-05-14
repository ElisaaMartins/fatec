import os

diretorioCorrente = os.getcwd()
print("Vc está no seguinte diretorio")
print(diretorioCorrente)

arq = open('./aula6/arquivo.txt', 'r', encoding='utf-8')
print("Metodo read()")
print(arq.read())

arq.seek(0) #Volta para o inicio do codigo
print("Metodo readline()")
print(arq.readline())
print(arq.readline())

arq.seek(0) #Volta para o inicio do codigo
print("Metodo readlines()")
print(arq.readlines())
arq.close()