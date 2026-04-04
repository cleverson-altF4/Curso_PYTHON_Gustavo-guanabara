def par_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ìmpar'
    
    
print(f"{par_impar(10)}")
print(f"{par_impar(5)}")
input("\nDigite enter...")

#______________________________

def potencia(a, b):
    print(f"{a} ** {b}")
    return a ** b


print(f"{potencia(2,3)}")
input("\nDigite enter...")

#_____________________________


def maior_menor(numero):
    if numero >= 18:
        return 'Adulto'
    
    
print(maior_menor(18))
