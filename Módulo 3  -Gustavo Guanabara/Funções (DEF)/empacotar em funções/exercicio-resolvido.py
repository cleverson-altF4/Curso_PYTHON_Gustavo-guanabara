from random import randint
from time import sleep


def sorteio(lista):
    print("\nSorteando 5 números\n")
    for numero in range(5):
        numero = randint(1,10)
        lista.append(numero)
        print(numero, end=' ', flush=True)
        sleep(1)
    print(f"---- > Números selecionados: {lista}")
    
    
def somando_pares(lista):
    soma = 0
    
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"A soma dos {i} números pares selecionados: {soma}")
            
            
lista_principal = []

sorteio(lista_principal)
somando_pares(lista_principal)
            
            

