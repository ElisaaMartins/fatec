trabalhador = str(input("Digite seu nome:"))
horasTrab = float(input("Digite aqui suas horas trabalhadas: "))
valorHora = float(input("Digite aqui o valor da sua hora trabalhada: "))
valorHoraExtra = float(input("Digite aqui o valor da sua hora extra: "))

print("Elisa Ap. Martins de Oliveira  RA:1051392411023 | Fernanda Victoria Felix Oliveira RA:1051392411027 - Turma DSM 1°Semestre")

def calcular_pagamento(horasTrab, valorHora, valorHoraExtra):
    if (horasTrab <= 40):
        salario = horasTrab * valorHora
        print ("De acordo com suas horas tarabalhadas", horasTrab, "e seu valor hora", valorHora, "seu salário será:", salario)
    else:
        horasExtra = horasTrab - 40
        salario = (40 * valorHora) + (horasExtra * valorHoraExtra)
        print ("De acordo com suas horas extra", horasExtra, "o seu salario será:",salario)

calcular_pagamento(horasTrab, valorHora, valorHoraExtra)
