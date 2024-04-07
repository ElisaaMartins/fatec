import math
num = int(input("Digite um número: "))

#situação a
if ((num == 1) | (num == 2) | (num == 3)):
 print( num, "elevado ao quadrado é", num * num )

#situação b
elif ((num == 4) | (num == 9)):
 print ("A raiz quadrada de ", num, " é = ", math.sqrt(num))

#situação c
elif ((num == 6) | (num == 7) | (num == 8)):
 print ("Esse número dividido por 9 é = ", num / 9)

else:
 print ("O número digitado é inválido ou não tem possui nenhuma condição")

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")
