import os

# letra A - descobrir o tamanho do arquivo
tamanhoArquivo = os.path.getsize('./Lista_Python_6/fix64/mensagem.txt') # método usado os.path.getsize = conta os bytes do arquivo
print("O tamanho do arquivo é", tamanhoArquivo, "bytes")

#letra B - lista de palavras dentro de mensagem.txt
arq = open('./Lista_Python_6/fix64/mensagem.txt', 'r', encoding="utf-8")
conteudo = arq.read()
palavras = conteudo.split() # método usado split = lê palavras no arquivo
print("Palavras dentro de 'mensagem.txt':", palavras)

print("Elisa Aparecida Martins de Oliveira - RA: 1051392411023 - Turma DSM 1°Semestre")
arq.close()
