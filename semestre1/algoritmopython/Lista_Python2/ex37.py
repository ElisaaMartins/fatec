nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

acres1 = salario + (salario * 0.20)
acres2 = salario + (salario * 0.10)
acres3 = salario + (salario * 0.05)

if salario <= 1500:
    print("Seu salário aumentou de", salario, "para:", acres1)
elif (salario > 1500) & (salario < 2500):
    print("Seu salário aumentou de", salario, "para:", acres2)
else:
    print("Seu salário aumentou", salario, "para:", acres3)

print("Elisa Aparecida Martins de Oliveira - RA: 105392411023")


