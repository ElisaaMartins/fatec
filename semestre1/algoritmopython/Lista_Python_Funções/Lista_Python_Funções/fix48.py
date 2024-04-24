nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

def fix48(salario):
    if salario <= 1500:
        acres1 = salario + (salario * 0.20)
        print("Seu salário aumentou de", salario, "para:", acres1)
        return acres1

    elif (salario > 1500) & (salario < 2500):
        acres2 = salario + (salario * 0.10)
        print("Seu salário aumentou de", salario, "para:", acres2)
        return acres2
    else:
        acres3 = salario + (salario * 0.05)
        print("Seu salário aumentou", salario, "para:", acres3)
        return acres3

fix48(salario)

print("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")

