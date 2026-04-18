from random import randint
from time import sleep

def linha():
    print("-"*45)

def sorteio(lista):
    print("\n Somando números pares\n")
    for numero in range(5):
        numero = randint(1,10)
        lista.append(numero)
        print(numero, end=' ', flush=True)
        sleep(0.5)
    print(f"------->: Números adicionados {lista}")
    
linha()   
def somando_pares(lista):
    soma = 0
    
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"Nùmeros pares da lista: {soma}")

#programa principal    
lista_principal= []

sorteio(lista_principal)
linha()
somando_pares(lista_principal)

