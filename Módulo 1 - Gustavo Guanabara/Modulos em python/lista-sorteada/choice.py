#sorteando um nome na lista
from random import choice
n1 = str(input("Digite: "))
n2 = str(input("Digite: "))
n3 = str(input("Digite: "))
n4 = str(input("Digite: "))

lista = [n1,n2,n3,n4]

sorteio = choice(lista)
print(sorteio)