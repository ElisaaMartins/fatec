compra1 = float(input("Digite o valor da primeira compra: "))
compra2 = float(input("Digite o valor da segunda compra: "))
compra3 = float(input("Digite o valor da terceira compra: "))

total = compra1 + compra2 + compra3

desc1 = total - (total * 0.20) 
desc2 = total - (total * 0.10) 
desc3 = total - (total * 0.05) 

if (total >= 300):
    print("Sua compra saiu de", total, "por:", desc1)
elif ((total >= 200) & (total <=299.99)):
    print("Sua compra saiu de", total, "por:", desc2)
elif (total <= 199.99):
    print("Sua compra saiu de", total, "por:", desc3)
else:
    print("Sua compra não possui desconto")

print ("Elisa Aparecida Martins de Oliveira - RA: 1051392411023")

