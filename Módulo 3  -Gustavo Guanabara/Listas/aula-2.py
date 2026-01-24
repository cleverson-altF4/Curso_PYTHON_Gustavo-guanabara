numero = [0, 1, 2, 3, 4]
numero.remove(0) # O uso do remove ele elimina apenas a primeira ação do número que é o zero e ele apaga
if 5 in numero:
    numero.remove(5)
else:
    print("Não achei o número 5")
    
print(numero)