compra1 = float(input("Digite o valor da primeira compra: "))
compra2 = float(input("Digite o valor da segunda compra: "))
compra3 = float(input("Digite o valor da terceira compra: "))

def compra (compra1, compra2, compra3):
    total = compra1 + compra2 + compra3
    if (total >= 300):
        desc1 = total - (total * 0.20) 
        print("Sua compra saiu de", total, "por:", desc1)
        return desc1
    
    elif ((total >= 200) & (total <=299.99)):
        desc2 = total - (total * 0.10)
        print("Sua compra saiu de", total, "por:", desc2)
        return desc2
    
    elif (total <= 199.99):
        desc3 = total - (total * 0.05) 
        print("Sua compra saiu de", total, "por:", desc3)
        return desc3
    
    else:
        print("Sua compra não possui desconto")

compra(compra1, compra2, compra3)

print ("Elisa Aparecida Martins de Oliveira - RA: 105392411023")




 
