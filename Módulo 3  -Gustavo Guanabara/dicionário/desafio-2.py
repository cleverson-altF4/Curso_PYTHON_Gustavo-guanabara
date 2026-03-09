#Crie um programa que onde 4 jogadores joguem um dado e tenham resultados.
#Guarde em um dicionário
#No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número do dado

from random import randint
from time import sleep
jogador = {}

for i in range(4):
    jogador = randint(1,6)
    print(f"O jogador - {i+1} tirou {jogador}")
    sleep(0.7)
    
print("-"*30)
print("   Ranking dos jogadores   ")



    
    