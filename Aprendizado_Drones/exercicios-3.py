#Lição de hoje — Módulos
#Módulos são arquivos com funções prontas que você importa no seu código. No drone você vai usar muito isso — time para temporizar ações, math para cálculos de navegação, random para simular sensores nos testes.

#1. Importando módulo completo

import time

print(f"Decolando")
#time.sleep(2)
print("Decolou")

input("\nEnter: ")

#2. Calculando distância entre dois pontos (usado em navegação)
from math import sqrt

posicao_x = 30
posicao_y = 20

raiz_quadrada = sqrt(posicao_x**2 + posicao_y**2)
print(f"Distância: {raiz_quadrada}M")

input("\nEnter: ")

#3. importa o math apelidos

import math as m

pI = m.pi
print(pI)

raiz = sqrt(16)
print(raiz)

input("\nEnter: ")

#4. Módulo random — muito usado para simular sensores

import random

def simular_sensores():
    return random.uniform(45.0,55.0)

distance = simular_sensores()
print(f"A distância {distance:.2f}m")



