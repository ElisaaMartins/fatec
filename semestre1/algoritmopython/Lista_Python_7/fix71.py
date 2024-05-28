horasTrab = float(input("Digite aqui suas horas trabalhadas: "))
valorHora = float(input("Digite aqui o valor da sua hora trabalhada: "))


def calcular_pagamento(horasTrab, valorHora):
    if (horasTrab < 40):
        salario = horasTrab * valorHora