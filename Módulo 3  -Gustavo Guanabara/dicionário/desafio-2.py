#Crie um programa que onde 4 jogadores joguem um dado e tenham resultados.
#Guarde em um dicionário
#No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número do dado



from random import randint
from time import sleep
from operator import itemgetter

jogador = {}

for i in range(1, 5):
    jogador[f'Jogador {i}'] = randint(1, 6)
    print(f"O jogador {i} tirou {jogador[f'Jogador {i}']}")
    
print("-"*30)
print("   Ranking   ")

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

for posicao, valor in enumerate(ranking):
    print(f"{posicao}º lugar {valor}")