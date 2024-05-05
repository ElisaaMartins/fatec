peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
sexo = str(input("Digite o sexo (use F ou M):"))

imc = peso / (altura * altura)

if sexo == "F":
    if imc < 19:
        print ("Está abaixo do peso")
    elif 19 <= imc < 24:
        print ("Está no peso ideal")
    elif imc >= 24:
        print ("Está acima do peso")
elif sexo == "M":
    if imc < 20:
        print ("Está abaixo do peso")
    elif 20 <= imc < 25:
        print ("Está no peso ideal")
    elif imc >= 25:
         print ("Está acima do peso")
else:
    print("Digite F ou M")

print("Elisa Aparecida Martins de Oliveira - RA: 1051392411023 - Turma DSM 1°Semestre")

