""" o código é lido em ordem sequencial - da esquerda para direita de  cima para baixo """
num, num2, num3,num4, num5, num6 = 10, 10 ,10 , 10 , 10,10

print("Parte I: valor inicial de num = " +str(num))
num += 1

print("Parte II: valor da variavel num + 1 = %i " %num)
num2 -= 1

print("Parte III: valor da variavel num2 - 1 = %i " %num2)
num3 *= 2

print("Parte IV: valor da variavel num3 * 2 = %i " %num3)
num4 /= 3

print("Parte V: valor da variavel num4 / 3 =" ,num4) #dá o resultado inteiro sem números após a vírgula
num5 //= 3

print("Parte VI: valor da variavel num5 // 3 = %i " %num5)