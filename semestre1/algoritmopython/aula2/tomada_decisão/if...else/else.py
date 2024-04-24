num = int(input("Digite um número : "))

print("Programa que determina se o numero digitado é para ou impar")

if(not num % 2): #condição para determinar um numero impar ou par através da divisão e do resto
 print("O número digitado é par." ,num)
else:
 print("O número digitado é ímpar." ,num)