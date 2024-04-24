# a expressão deverá, obrigatoriamente, deixar de ser verdadeira para que a repetição seja interrompida. 
# caso contrário a aplicação irá congelar/travar
# no exemplo ela não deixa de ser verdadeira, por isso quando roda ela fica infinita (trava)

cont = 0 

while (cont <= 5):
 print("Valor do contador i = " +str(cont))
cont = cont + 1